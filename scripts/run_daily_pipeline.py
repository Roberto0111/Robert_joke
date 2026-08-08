#!/usr/bin/env python3
import argparse
import datetime as dt
import json
import math
import os
import re
import shutil
import struct
import subprocess
import sys
import time
import urllib.request
import wave
import xml.etree.ElementTree as ET
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CODEX_BIN = Path(os.environ.get("CODEX_BIN", "/Applications/ChatGPT.app/Contents/Resources/codex"))
NODE_BIN = Path(os.environ.get(
    "NODE_BIN",
    "/Users/roberto/.cache/codex-runtimes/codex-primary-runtime/dependencies/node/bin/node",
))
SSH_KEY = Path(os.environ.get("ROBERT_JOKE_SSH_KEY", "/Users/roberto/.ssh/id_ed25519_robert_joke"))
CHARACTER_REFERENCE = ROOT / "assets" / "main_character_reference.jpg"
LOCK_FILE = ROOT / ".daily_pipeline.lock"
LOG_DIR = ROOT / "logs"
FFMPEG_BIN = Path(os.environ.get("FFMPEG_BIN", "/opt/homebrew/bin/ffmpeg"))
TIMEOUT_SECONDS = int(os.environ.get("ROBERT_JOKE_CODEX_TIMEOUT", "3600"))
POLL_SECONDS = int(os.environ.get("ROBERT_JOKE_POLL_SECONDS", "5"))
IG_IMAGE_WIDTH = 1080
IG_IMAGE_HEIGHT = 1350
REEL_WIDTH = 1080
REEL_HEIGHT = 1920
REEL_SECONDS = 12
REEL_PAGE_ONE_SECONDS = 5
FALLBACK_REEL_WEEKDAYS = {0, 2, 4, 6}  # Used only before analytics has enough evidence.


def main() -> int:
    parser = argparse.ArgumentParser(description="Generate a four-panel life dialogue, then publish its carousel or Reel.")
    parser.add_argument("--run-id", default=current_run_id(), help="Run id, default YYYY-MM-DD_HHMM in local time.")
    parser.add_argument("--generate-only", action="store_true", help="Only trigger Codex and wait for local files.")
    parser.add_argument("--post-only", action="store_true", help="Skip Codex and publish an existing run id.")
    parser.add_argument("--dry-run", action="store_true", help="Do not push or publish; useful for testing.")
    parser.add_argument(
        "--format",
        choices=("auto", "image", "reel"),
        default="auto",
        help="Publishing format. 'image' publishes the two-page carousel; auto follows performance strategy.",
    )
    args = parser.parse_args()

    LOG_DIR.mkdir(exist_ok=True)
    with locked():
        run_id = args.run_id
        paths = run_paths(run_id)
        ensure_dirs(paths)
        content_mode, content_reason = determine_content_mode(run_id)
        paths["content_mode"] = content_mode

        if not args.post_only:
            collect_growth_metrics(run_id)

        publish_format, format_reason = determine_publish_format(args.format, run_id)
        log(
            run_id,
            f"pipeline started content_mode={content_mode} content_reason={content_reason} "
            f"format={publish_format} format_reason={format_reason} "
            f"dry_run={args.dry_run} "
            f"generate_only={args.generate_only} post_only={args.post_only}",
        )

        if not args.post_only:
            fetch_trend_context(run_id, paths)
            trigger_codex(run_id, paths, content_mode, args.dry_run)
            if args.dry_run:
                log(run_id, "dry-run complete; skipping file wait, git push, and Instagram publish")
                return 0
            wait_for_generation(run_id, paths)

        for image_path in paths["images"]:
            normalize_image_for_instagram(run_id, image_path, paths["run_dir"])
        validate_generation(paths)
        prepare_publish_asset(run_id, paths, publish_format)

        if args.generate_only:
            log(run_id, f"generate-only complete format={publish_format}")
            return 0

        if args.dry_run:
            log(run_id, "dry-run complete; skipping git push and Instagram publish")
            return 0

        commit_and_push_generated(run_id, paths)
        media_id = publish_to_instagram(run_id, paths, publish_format)
        story_media_id = ""
        story_error = ""
        try:
            story_media_id = publish_story_to_instagram(run_id, paths, publish_format)
        except Exception as exc:
            story_error = redact(str(exc))[:500]
            log(run_id, f"Instagram Story failed after primary publish: {story_error}")
        mark_published(
            run_id,
            paths,
            media_id,
            publish_format,
            story_media_id=story_media_id,
            story_error=story_error,
        )
        commit_and_push_published(run_id, paths)
        log(run_id, f"pipeline complete media_id={media_id}")
        return 0


def current_run_id() -> str:
    return dt.datetime.now().strftime("%Y-%m-%d_%H%M")


def determine_publish_format(requested: str, run_id: str) -> tuple[str, str]:
    if requested != "auto":
        return requested, "explicit"

    strategy_path = ROOT / "analytics" / "daily_strategy.json"
    try:
        strategy = json.loads(strategy_path.read_text(encoding="utf-8"))
        recommended = strategy.get("recommended_format")
        if recommended in {"image", "reel"}:
            return recommended, "daily_strategy"
    except (OSError, ValueError, TypeError):
        pass

    try:
        run_date = dt.datetime.strptime(run_id[:10], "%Y-%m-%d")
    except ValueError:
        run_date = dt.datetime.now()
    fallback = "reel" if run_date.weekday() in FALLBACK_REEL_WEEKDAYS else "image"
    return fallback, "fallback_schedule"


def determine_content_mode(run_id: str) -> tuple[str, str]:
    return "life_dialogue", "fixed_life_dialogue_series"


def run_paths(run_id: str) -> dict[str, Path]:
    image_1 = ROOT / "assets" / f"{run_id}_deadpan_joke_01.png"
    image_2 = ROOT / "assets" / f"{run_id}_deadpan_joke_02.png"
    return {
        "run_dir": ROOT / "posts" / run_id,
        "image": image_1,
        "image_1": image_1,
        "image_2": image_2,
        "images": (image_1, image_2),
        "caption": ROOT / "captions" / f"{run_id}_deadpan_joke.md",
        "prompt": ROOT / "prompts" / f"{run_id}_generation_prompt.md",
        "manifest": ROOT / "posts" / run_id / "manifest.json",
        "trends": ROOT / "posts" / run_id / "trend_context.txt",
        "reel": ROOT / "assets" / f"{run_id}_deadpan_joke_reel.mp4",
    }


def ensure_dirs(paths: dict[str, Path]) -> None:
    for key in ("run_dir",):
        paths[key].mkdir(parents=True, exist_ok=True)
    for key in ("image_1", "image_2", "caption", "prompt"):
        paths[key].parent.mkdir(parents=True, exist_ok=True)


def trigger_codex(run_id: str, paths: dict[str, Path], content_mode: str, dry_run: bool) -> None:
    if dry_run:
        prompt_file = paths["run_dir"] / "codex_prompt.txt"
        prompt_file.write_text(build_codex_prompt(run_id, paths, content_mode), encoding="utf-8")
        log(run_id, f"dry-run: wrote codex prompt to {prompt_file}")
        return

    if not CODEX_BIN.exists():
        raise RuntimeError(f"Codex CLI not found: {CODEX_BIN}")
    if not CHARACTER_REFERENCE.exists():
        raise RuntimeError(f"Main character reference not found: {CHARACTER_REFERENCE}")

    prompt = build_codex_prompt(run_id, paths, content_mode)
    prompt_file = paths["run_dir"] / "codex_prompt.txt"
    prompt_file.write_text(prompt, encoding="utf-8")

    cmd = [
        str(CODEX_BIN),
        "--ask-for-approval",
        "never",
        "exec",
        "-C",
        str(ROOT),
        "--sandbox",
        "workspace-write",
        "--skip-git-repo-check",
        "--image",
        str(CHARACTER_REFERENCE),
        "--output-last-message",
        str(paths["run_dir"] / "codex_last_message.txt"),
        "-",
    ]
    log(run_id, "starting codex exec")
    result = subprocess.run(
        cmd,
        input=prompt,
        text=True,
        cwd=ROOT,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        timeout=TIMEOUT_SECONDS,
    )
    (paths["run_dir"] / "codex_exec.log").write_text(result.stdout, encoding="utf-8")
    if result.returncode != 0:
        raise RuntimeError(f"codex exec failed with exit code {result.returncode}; see {paths['run_dir'] / 'codex_exec.log'}")


def build_codex_prompt(run_id: str, paths: dict[str, Path], content_mode: str) -> str:
    if content_mode != "life_dialogue":
        raise RuntimeError(f"Unsupported content mode: {content_mode}")
    content_brief = """
Content mode: LIFE DIALOGUE (人生對話)
- Start from one concrete adult-life tension such as comparison, rest, boundaries, uncertainty, loneliness, failure, or letting go.
- Panel 1: Roberto admits a real worry in plain spoken language.
- Panel 2: the tuxedo cat asks one short question that challenges the hidden assumption.
- Panel 3: Roberto answers honestly, revealing why he is stuck.
- Panel 4: the cat gives one concise insight that changes how panels 1-3 are understood.
- The final line may be quietly witty, but it should primarily feel true and memorable rather than insulting.
- Avoid generic motivational slogans, fake therapy language, diagnoses, absolute claims, moral superiority, and advice that needs a long explanation.
- Brainstorm scores: relatability, natural dialogue, insight, and save/share value, each 0-5.
- The caption must include #人生對話 and 2-4 other relevant hashtags.
""".strip()
    return f"""
You are generating one four-panel Instagram carousel story for @roberto_joke.

{content_brief}

Read:
- README.md
- prompts/daily_comic_style.md
- prompts/daily_posting_workflow.md

Attached image:
- assets/main_character_reference.jpg is the mandatory likeness reference for the male main character.

Current trend context:
- Read {paths["trends"]}. It contains current Taiwan Google search trends fetched immediately before this run.
- You may use a trend only when it naturally supports a grounded everyday life question. Never force a trend into the story.
- Skip politics, crime, disasters, deaths, medical scares, allegations, and other sensitive news.
- If web search is available, verify the meaning of any current Taiwanese meme phrase before using it. Never copy another creator's image or caption verbatim.
- Original everyday dilemmas are always acceptable and preferred over a weak trend reference.

Growth context:
- Read analytics/latest.json if it exists. Treat reach, shares, saves, and total interactions as evidence, not vanity metrics.
- Read analytics/daily_strategy.md if it exists and follow its instructions for pacing, dialogue clarity, and save/share value.
- Analytics may adjust format, pacing, and packaging only. It must never change the content mode away from LIFE DIALOGUE.
- The strategy file is recalculated before every post. Do not copy its best caption; reuse only evidence-backed structure.
- Do not repeat a weak topic merely because it was recently posted. Prefer concepts that a viewer would send to one specific friend.

Hard requirements:
- Generate exactly two colorful 1080x1350 images for one Instagram carousel. Each image contains exactly two stacked comic panels, for exactly four panels total.
- Keep the same characters, wardrobe, rendering, room palette, line weight, and facial identity across both images. They must feel like one continuous four-panel story.
- Follow the selected content mode's four-panel dialogue structure exactly.
- Put one large Traditional Chinese line in each panel. Text must be immediately readable on a phone, fully inside generous safe margins, and never overlap a face.
- The fourth-panel conclusion must be the strongest beat. It must reframe or deepen the first three panels, not explain the visible action.
- The male protagonist must be based on the attached reference photo: East Asian man, round youthful face, side-swept black hair, slightly sleepy eyes, wearing a black collared top with gray zipper/placket.
- Preserve the reference identity in a polished realistic-comic meme style. Do not use a generic anime man.
- Style: original polished Taiwanese webcomic, concise spoken Traditional Chinese, reflective and grounded, with expressive but restrained acting.
- Include a black-and-white tuxedo cat in every image. The cat is Roberto's perceptive, calmly incisive dialogue partner.
- The panel-four line should begin with "貓：" so the speaker is unmistakable.
- Use exactly four concise dialogue/caption beats, one per panel. Avoid explanatory paragraphs.
- Before generating the image, brainstorm at least 12 genuinely different life-dialogue story candidates. At least 8 must be non-workplace topics.
- Score every candidate for relatability, natural dialogue, insight, and save/share value. Select only the highest-scoring candidate with at least 15/20.
- A valid final line must reframe the setup, expose an overlooked assumption or consequence, or create a more precise way to understand the problem. It must not merely describe what the image already shows.
- Reject corporate-jargon reskins and generic social-media wisdom unless the wording creates a genuinely specific new meaning.
- Compare against the latest 20 posts. Vary the dilemma, insight mechanism, setting, pose, and cat reaction, not just the nouns.
- Record the top five candidate stories, scores, rejection notes, and the reason for the final selection in the generation prompt record. Still generate exactly one four-panel story across two images.
- Caption must use only 3-5 relevant hashtags and include the selected mode's required hashtag. Add one natural conversational question only when it fits; never use spammy engagement bait.
- Do not post to Instagram.
- Do not run git push.
- Do not print .env, tokens, access keys, or secrets.

Output these exact files:
- Carousel page 1 (panels 1-2): {paths["image_1"]}
- Carousel page 2 (panels 3-4): {paths["image_2"]}
- Caption: {paths["caption"]}
- Prompt record: {paths["prompt"]}
- Manifest: {paths["manifest"]}

Manifest JSON must include:
{{
  "run_id": "{run_id}",
  "content_mode": "{content_mode}",
  "topic": "<short topic>",
  "image_paths": [
    "assets/{run_id}_deadpan_joke_01.png",
    "assets/{run_id}_deadpan_joke_02.png"
  ],
  "caption_path": "captions/{run_id}_deadpan_joke.md",
  "prompt_path": "prompts/{run_id}_generation_prompt.md",
  "status": "generated"
}}

Avoid repeating old topics, setups, or exact punchlines already found in posts/, captions/, assets/.
The story must reward swiping: panels 1-3 reveal the tension naturally, then panel 4 delivers a mode-appropriate cat conclusion worth sharing or saving.
""".strip()


def fetch_trend_context(run_id: str, paths: dict[str, Path]) -> None:
    url = "https://trends.google.com/trending/rss?geo=TW"
    request = urllib.request.Request(url, headers={"User-Agent": "RobertJokeBot/1.0"})
    lines = [
        f"Fetched at: {dt.datetime.now().isoformat(timespec='seconds')}",
        f"Source: {url}",
        "Use only as optional inspiration. Skip sensitive topics and prefer an original life dialogue when uncertain.",
        "",
    ]
    try:
        with urllib.request.urlopen(request, timeout=15) as response:
            root = ET.fromstring(response.read())
        titles = []
        for item in root.findall("./channel/item"):
            title = (item.findtext("title") or "").strip()
            if title and title not in titles:
                titles.append(title)
        lines.extend(f"- {title}" for title in titles[:15])
        if not titles:
            lines.append("- No usable trend titles returned; create an original life dialogue.")
        log(run_id, f"trend context fetched topics={len(titles[:15])}")
    except (OSError, ET.ParseError) as exc:
        lines.append(f"- Trend fetch unavailable ({type(exc).__name__}); create an original life dialogue.")
        log(run_id, f"trend context unavailable: {type(exc).__name__}")
    paths["trends"].write_text("\n".join(lines) + "\n", encoding="utf-8")


def collect_growth_metrics(run_id: str) -> None:
    if not NODE_BIN.exists():
        log(run_id, f"analytics skipped: Node binary not found: {NODE_BIN}")
        return
    result = subprocess.run(
        [str(NODE_BIN), "scripts/collect-instagram-insights.mjs"],
        cwd=ROOT,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        timeout=180,
    )
    if result.returncode == 0:
        analysis = subprocess.run(
            [str(NODE_BIN), "scripts/analyze-instagram-performance.mjs"],
            cwd=ROOT,
            text=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            timeout=60,
        )
        if analysis.returncode == 0:
            log(run_id, "growth metrics collected and daily strategy updated")
        else:
            log(run_id, f"strategy analysis unavailable; continuing: {redact(analysis.stdout).strip()[:300]}")
    else:
        log(run_id, f"analytics unavailable; continuing: {redact(result.stdout).strip()[:300]}")


def normalize_image_for_instagram(run_id: str, image_path: Path, run_dir: Path) -> None:
    width, height = image_size(image_path)
    if (width, height) == (IG_IMAGE_WIDTH, IG_IMAGE_HEIGHT):
        log(run_id, f"image already Instagram safe: {width}x{height}")
        return

    backup = run_dir / f"{image_path.stem}_original_{width}x{height}{image_path.suffix}"
    if not backup.exists():
        shutil.copy2(image_path, backup)

    temp = run_dir / f"{image_path.stem}_ig_safe_tmp.png"
    aspect = width / height
    target_aspect = IG_IMAGE_WIDTH / IG_IMAGE_HEIGHT
    if aspect > target_aspect:
        resize_args = ["--resampleWidth", str(IG_IMAGE_WIDTH)]
    else:
        resize_args = ["--resampleHeight", str(IG_IMAGE_HEIGHT)]

    run(["sips", *resize_args, str(image_path), "--out", str(temp)], cwd=ROOT)
    run([
        "sips",
        "--padToHeightWidth",
        str(IG_IMAGE_HEIGHT),
        str(IG_IMAGE_WIDTH),
        "--padColor",
        "ffffff",
        str(temp),
        "--out",
        str(image_path),
    ], cwd=ROOT)
    temp.unlink(missing_ok=True)

    new_width, new_height = image_size(image_path)
    if (new_width, new_height) != (IG_IMAGE_WIDTH, IG_IMAGE_HEIGHT):
        raise RuntimeError(f"Instagram-safe resize failed: got {new_width}x{new_height}")
    log(run_id, f"normalized image for Instagram: {width}x{height} -> {new_width}x{new_height}")


def image_size(path: Path) -> tuple[int, int]:
    result = run(["sips", "-g", "pixelWidth", "-g", "pixelHeight", str(path)], cwd=ROOT)
    width_match = re.search(r"pixelWidth:\s*(\d+)", result.stdout)
    height_match = re.search(r"pixelHeight:\s*(\d+)", result.stdout)
    if not width_match or not height_match:
        raise RuntimeError(f"Could not read image size for {path}")
    return int(width_match.group(1)), int(height_match.group(1))


def wait_for_generation(run_id: str, paths: dict[str, Path]) -> None:
    deadline = time.time() + TIMEOUT_SECONDS
    required = [*paths["images"], paths["caption"], paths["prompt"], paths["manifest"]]
    while time.time() < deadline:
        if all(p.exists() and p.stat().st_size > 0 for p in required):
            log(run_id, "generation files detected")
            return
        time.sleep(POLL_SECONDS)
    missing = [str(p) for p in required if not p.exists() or p.stat().st_size == 0]
    raise TimeoutError(f"Timed out waiting for generated files: {missing}")


def validate_generation(paths: dict[str, Path]) -> None:
    for image_path in paths["images"]:
        if image_path.suffix.lower() not in {".png", ".jpg", ".jpeg"}:
            raise RuntimeError(f"Unsupported image file: {image_path}")
        if image_path.stat().st_size < 100_000:
            raise RuntimeError(f"Generated image looks too small: {image_path}")
        if image_size(image_path) != (IG_IMAGE_WIDTH, IG_IMAGE_HEIGHT):
            raise RuntimeError(f"Carousel image is not {IG_IMAGE_WIDTH}x{IG_IMAGE_HEIGHT}: {image_path}")
    caption = paths["caption"].read_text(encoding="utf-8").strip()
    if not caption:
        raise RuntimeError("Caption is empty")
    manifest = json.loads(paths["manifest"].read_text(encoding="utf-8"))
    if manifest.get("status") not in {"generated", "published"}:
        raise RuntimeError("Manifest status must be generated or published")
    if manifest.get("content_mode") != paths["content_mode"]:
        raise RuntimeError(f"Manifest content_mode must be {paths['content_mode']}")
    expected_images = [rel(path) for path in paths["images"]]
    if manifest.get("image_paths") != expected_images:
        raise RuntimeError(f"Manifest image_paths must be {expected_images}")


def prepare_publish_asset(run_id: str, paths: dict[str, Path], publish_format: str) -> None:
    manifest = json.loads(paths["manifest"].read_text(encoding="utf-8"))
    manifest["publish_format"] = publish_format
    if publish_format == "reel":
        create_reel(run_id, paths)
        manifest["video_path"] = rel(paths["reel"])
    else:
        manifest.pop("video_path", None)
    paths["manifest"].write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def create_reel(run_id: str, paths: dict[str, Path]) -> None:
    if not FFMPEG_BIN.exists():
        raise RuntimeError(f"ffmpeg not found: {FFMPEG_BIN}")
    soundtrack = paths["run_dir"] / "playful_soundtrack.wav"
    create_playful_soundtrack(soundtrack)
    foreground_size = 1000
    foreground_height = 1250
    foreground_y = (REEL_HEIGHT - foreground_height) // 2
    page_durations = (REEL_PAGE_ONE_SECONDS, REEL_SECONDS - REEL_PAGE_ONE_SECONDS)
    filter_graph = (
        f"[0:v]split=2[bg0src][fg0src];"
        f"[bg0src]scale={REEL_WIDTH}:{REEL_HEIGHT}:force_original_aspect_ratio=increase,"
        f"crop={REEL_WIDTH}:{REEL_HEIGHT},boxblur=35:12[bg0];"
        f"[fg0src]scale={foreground_size}:{foreground_height}[fg0];"
        f"[bg0][fg0]overlay=(W-w)/2:{foreground_y},"
        f"fade=t=in:st=0:d=0.25,fade=t=out:st={page_durations[0] - 0.18}:d=0.18,"
        f"setpts=PTS-STARTPTS[v0];"
        f"[1:v]split=2[bg1src][fg1src];"
        f"[bg1src]scale={REEL_WIDTH}:{REEL_HEIGHT}:force_original_aspect_ratio=increase,"
        f"crop={REEL_WIDTH}:{REEL_HEIGHT},boxblur=35:12[bg1];"
        f"[fg1src]scale={foreground_size}:{foreground_height}[fg1];"
        f"[bg1][fg1]overlay=(W-w)/2:{foreground_y},"
        f"fade=t=in:st=0:d=0.18,fade=t=out:st={page_durations[1] - 0.5}:d=0.5,"
        f"setpts=PTS-STARTPTS[v1];"
        f"[v0][v1]concat=n=2:v=1:a=0,format=yuv420p[v]"
    )
    command = [str(FFMPEG_BIN), "-y"]
    for image_path, duration in zip(paths["images"], page_durations):
        command.extend(["-loop", "1", "-framerate", "30", "-t", str(duration), "-i", str(image_path)])
    command.extend([
        "-i", str(soundtrack),
        "-filter_complex",
        filter_graph,
        "-map",
        "[v]",
        "-map",
        "2:a",
        "-t",
        str(REEL_SECONDS),
        "-r",
        "30",
        "-c:v",
        "libx264",
        "-preset",
        "medium",
        "-crf",
        "20",
        "-maxrate",
        "8M",
        "-bufsize",
        "16M",
        "-c:a",
        "aac",
        "-b:a",
        "128k",
        "-ar",
        "48000",
        "-movflags",
        "+faststart",
        str(paths["reel"]),
    ])
    run(command, cwd=ROOT)
    if paths["reel"].stat().st_size < 100_000:
        raise RuntimeError(f"Generated Reel looks too small: {paths['reel']}")
    log(run_id, f"Reel created: {paths['reel'].name}")


def create_playful_soundtrack(output: Path) -> None:
    sample_rate = 48_000
    total_samples = REEL_SECONDS * sample_rate
    audio = [0.0] * total_samples

    # Fast prank-vlog rhythm: bouncy plucks, a page turn, then a cartoon reveal.
    beat = 60.0 / 132.0
    reveal_time = REEL_PAGE_ONE_SECONDS + 3.0
    melody = [392.00, 493.88, 587.33, 493.88, 440.00, 523.25, 659.25, 523.25]
    notes = []
    for index in range(math.ceil(REEL_SECONDS / (beat / 2))):
        start = index * beat / 2
        if reveal_time - 0.28 <= start < reveal_time:
            continue
        notes.append((start, 0.105, melody[index % len(melody)], 0.27))
    bass_notes = [98.00, 98.00, 110.00, 98.00, 130.81, 110.00, 98.00, 98.00]
    for index in range(math.ceil(REEL_SECONDS / beat)):
        frequency = bass_notes[index % len(bass_notes)]
        start = index * beat
        if reveal_time - 0.28 <= start < reveal_time:
            continue
        notes.append((start, 0.16, frequency, 0.24))

    for start, duration, frequency, volume in notes:
        start_sample = int(start * sample_rate)
        note_samples = int(duration * sample_rate)
        for index in range(note_samples):
            position = start_sample + index
            if position >= total_samples:
                break
            elapsed = index / sample_rate
            decay = math.exp(-17.0 * elapsed)
            attack = min(1.0, elapsed / 0.003)
            tone = (
                math.sin(2 * math.pi * frequency * elapsed)
                + 0.31 * math.sin(2 * math.pi * frequency * 2 * elapsed)
                + 0.12 * math.sin(2 * math.pi * frequency * 4 * elapsed)
            )
            audio[position] += volume * attack * decay * tone / 1.43

    reveal_start = int(reveal_time * sample_rate)
    reveal_samples = int(0.62 * sample_rate)
    phase = 0.0
    for index in range(reveal_samples):
        position = reveal_start + index
        elapsed = index / sample_rate
        progress = index / reveal_samples
        frequency = 880.0 * ((220.0 / 880.0) ** progress)
        phase += 2 * math.pi * frequency / sample_rate
        envelope = math.sin(math.pi * progress) ** 0.65
        wobble = 0.66 + 0.34 * math.sin(2 * math.pi * 10.0 * elapsed)
        audio[position] += 0.38 * envelope * wobble * math.sin(phase)

    for index in range(math.ceil(REEL_SECONDS / (beat / 2))):
        hit_time = index * beat / 2 + beat / 4
        if reveal_time - 0.30 <= hit_time < reveal_time or hit_time >= REEL_SECONDS:
            continue
        start_sample = int(hit_time * sample_rate)
        hit_samples = int(0.028 * sample_rate)
        for index in range(hit_samples):
            position = start_sample + index
            elapsed = index / sample_rate
            click = (
                math.sin(2 * math.pi * 1680 * elapsed)
                + 0.35 * math.sin(2 * math.pi * 2320 * elapsed)
            ) * math.exp(-105 * elapsed)
            audio[position] += 0.10 * click

    # A soft double tap marks the punchline without overpowering the text reveal.
    for hit_time, frequency in ((reveal_time, 185.00), (reveal_time + 0.14, 138.59)):
        start_sample = int(hit_time * sample_rate)
        hit_samples = int(0.18 * sample_rate)
        for index in range(hit_samples):
            position = start_sample + index
            elapsed = index / sample_rate
            audio[position] += (
                0.22
                * math.sin(2 * math.pi * frequency * elapsed)
                * math.exp(-18 * elapsed)
            )

    peak = max(max(abs(sample) for sample in audio), 0.001)
    scale = 0.78 / peak
    output.parent.mkdir(parents=True, exist_ok=True)
    with wave.open(str(output), "wb") as wav_file:
        wav_file.setnchannels(2)
        wav_file.setsampwidth(2)
        wav_file.setframerate(sample_rate)
        frames = bytearray()
        for sample in audio:
            value = int(max(-1.0, min(1.0, sample * scale)) * 32767)
            packed = struct.pack("<h", value)
            frames.extend(packed)
            frames.extend(packed)
        wav_file.writeframes(frames)


def commit_and_push_generated(run_id: str, paths: dict[str, Path]) -> None:
    generated = [
        *(rel(path) for path in paths["images"]),
        rel(paths["caption"]),
        rel(paths["prompt"]),
        rel(paths["manifest"]),
    ]
    if paths["reel"].exists():
        generated.append(rel(paths["reel"]))
    git(["add", *generated])
    if has_staged_changes():
        git(["commit", "-m", f"Add daily joke comic {run_id}"])
    git_push()


def publish_to_instagram(run_id: str, paths: dict[str, Path], publish_format: str) -> str:
    if not NODE_BIN.exists():
        raise RuntimeError(f"Node binary not found: {NODE_BIN}")
    image_urls = [
        f"https://raw.githubusercontent.com/Roberto0111/Robert_joke/main/"
        f"assets/{run_id}_deadpan_joke_{index:02d}.png"
        for index in range(1, 3)
    ]
    env = os.environ.copy()
    env["IG_IMAGE_URL"] = image_urls[0]
    env["IG_CAROUSEL_IMAGE_URLS"] = json.dumps(image_urls)
    env["IG_CAPTION_FILE"] = f"captions/{run_id}_deadpan_joke.md"
    env["IG_MEDIA_TYPE"] = "REELS" if publish_format == "reel" else "CAROUSEL"
    if publish_format == "reel":
        env["IG_VIDEO_URL"] = (
            f"https://raw.githubusercontent.com/Roberto0111/Robert_joke/main/"
            f"assets/{run_id}_deadpan_joke_reel.mp4"
        )
    result = subprocess.run(
        [str(NODE_BIN), "scripts/post-to-instagram.mjs"],
        cwd=ROOT,
        env=env,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        timeout=300,
    )
    (paths["run_dir"] / "instagram_publish.log").write_text(redact(result.stdout), encoding="utf-8")
    if result.returncode != 0:
        raise RuntimeError(f"Instagram publish failed; see {paths['run_dir'] / 'instagram_publish.log'}")
    match = re.search(r'"id"\s*:\s*"([^"]+)"', result.stdout)
    if not match:
        raise RuntimeError("Could not parse Instagram media id from publish output")
    return match.group(1)


def publish_story_to_instagram(run_id: str, paths: dict[str, Path], publish_format: str) -> str:
    if not NODE_BIN.exists():
        raise RuntimeError(f"Node binary not found: {NODE_BIN}")
    env = os.environ.copy()
    env["IG_MEDIA_TYPE"] = "STORIES"
    env["IG_CAPTION_FILE"] = f"captions/{run_id}_deadpan_joke.md"
    if publish_format == "reel":
        env["IG_VIDEO_URL"] = (
            f"https://raw.githubusercontent.com/Roberto0111/Robert_joke/main/"
            f"assets/{run_id}_deadpan_joke_reel.mp4"
        )
        env.pop("IG_IMAGE_URL", None)
    else:
        env["IG_IMAGE_URL"] = (
            f"https://raw.githubusercontent.com/Roberto0111/Robert_joke/main/"
            f"assets/{run_id}_deadpan_joke_01.png"
        )
        env.pop("IG_VIDEO_URL", None)
    result = subprocess.run(
        [str(NODE_BIN), "scripts/post-to-instagram.mjs"],
        cwd=ROOT,
        env=env,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        timeout=300,
    )
    (paths["run_dir"] / "instagram_story_publish.log").write_text(
        redact(result.stdout), encoding="utf-8"
    )
    if result.returncode != 0:
        raise RuntimeError(
            f"Instagram Story publish failed; see {paths['run_dir'] / 'instagram_story_publish.log'}"
        )
    match = re.search(r'"id"\s*:\s*"([^"]+)"', result.stdout)
    if not match:
        raise RuntimeError("Could not parse Instagram Story media id from publish output")
    return match.group(1)


def mark_published(
    run_id: str,
    paths: dict[str, Path],
    media_id: str,
    publish_format: str,
    *,
    story_media_id: str,
    story_error: str,
) -> None:
    manifest = json.loads(paths["manifest"].read_text(encoding="utf-8"))
    manifest["status"] = "published"
    manifest["publish_format"] = publish_format
    manifest["instagram_media_id"] = media_id
    manifest["instagram_story_media_id"] = story_media_id
    manifest["instagram_story_status"] = "published" if story_media_id else "failed"
    if story_error:
        manifest["instagram_story_error"] = story_error
    else:
        manifest.pop("instagram_story_error", None)
    manifest["published_at"] = dt.datetime.now().isoformat(timespec="seconds")
    paths["manifest"].write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def commit_and_push_published(run_id: str, paths: dict[str, Path]) -> None:
    git(["add", rel(paths["manifest"])])
    if has_staged_changes():
        git(["commit", "-m", f"Mark daily joke comic {run_id} published"])
    git_push()


def git(args: list[str]) -> subprocess.CompletedProcess[str]:
    return run(["git", *args], cwd=ROOT)


def git_push() -> None:
    run([
        "git",
        "-c",
        f"core.sshCommand=ssh -i {SSH_KEY} -o IdentitiesOnly=yes",
        "push",
    ], cwd=ROOT)


def has_staged_changes() -> bool:
    result = subprocess.run(["git", "diff", "--cached", "--quiet"], cwd=ROOT)
    return result.returncode != 0


def run(cmd: list[str], cwd: Path) -> subprocess.CompletedProcess[str]:
    result = subprocess.run(cmd, cwd=cwd, text=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    if result.returncode != 0:
        raise RuntimeError(f"Command failed: {' '.join(cmd)}\n{redact(result.stdout)}")
    return result


def rel(path: Path) -> str:
    return str(path.relative_to(ROOT))


def locked():
    class Lock:
        def __enter__(self):
            if LOCK_FILE.exists():
                raise RuntimeError(f"Pipeline lock exists: {LOCK_FILE}")
            LOCK_FILE.write_text(str(os.getpid()), encoding="utf-8")
            return self

        def __exit__(self, exc_type, exc, tb):
            try:
                LOCK_FILE.unlink()
            except FileNotFoundError:
                pass

    return Lock()


def log(run_id: str, message: str) -> None:
    LOG_DIR.mkdir(exist_ok=True)
    line = f"{dt.datetime.now().isoformat(timespec='seconds')} {run_id} {message}\n"
    with (LOG_DIR / "pipeline.log").open("a", encoding="utf-8") as fh:
        fh.write(line)
    print(line, end="")


def redact(text: str) -> str:
    return re.sub(r"(IG_ACCESS_TOKEN=)[^\s]+", r"\1<redacted>", text)


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except Exception as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        raise SystemExit(1)
