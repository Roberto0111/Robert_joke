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
CAROUSEL_PAGE_COUNT = 5
REEL_SECONDS = 28
REEL_FPS = 30
REFERENCE_FETCH_PYTHON = Path(os.environ.get("REFERENCE_FETCH_PYTHON", "/opt/anaconda3/bin/python3"))
REFERENCE_FETCH_SCRIPT = ROOT / "scripts" / "fetch_reference_post.py"


def main() -> int:
    parser = argparse.ArgumentParser(description="Generate a five-page emotional life dialogue, then publish its carousel or Reel.")
    parser.add_argument("--run-id", default=current_run_id(), help="Run id, default YYYY-MM-DD_HHMM in local time.")
    parser.add_argument("--generate-only", action="store_true", help="Only trigger Codex and wait for local files.")
    parser.add_argument("--post-only", action="store_true", help="Skip Codex and publish an existing run id.")
    parser.add_argument("--dry-run", action="store_true", help="Do not push or publish; useful for testing.")
    parser.add_argument(
        "--preview-reel-from",
        metavar="RUN_ID",
        help="Render an animated preview from an existing run without generating, committing, or publishing.",
    )
    parser.add_argument(
        "--format",
        choices=("auto", "image", "reel"),
        default="auto",
        help="Publishing format. 'image' is available for manual previews; auto publishes the daily serious Reel.",
    )
    args = parser.parse_args()

    LOG_DIR.mkdir(exist_ok=True)
    if args.preview_reel_from:
        preview = render_reel_preview(args.preview_reel_from)
        print(preview)
        return 0
    with locked():
        run_id = args.run_id
        paths = run_paths(run_id)
        ensure_dirs(paths)
        content_mode, content_reason = determine_content_mode(run_id)
        paths["content_mode"] = content_mode

        if not args.dry_run and not args.generate_only:
            maintain_instagram_token(run_id)

        if not args.post_only:
            collect_growth_metrics(run_id)

        paths["growth_experiment"] = load_growth_experiment()
        publish_format, format_reason = determine_publish_format(args.format, run_id)
        log(
            run_id,
            f"pipeline started content_mode={content_mode} content_reason={content_reason} "
            f"format={publish_format} format_reason={format_reason} "
            f"experiment={paths['growth_experiment'].get('id', 'control')} "
            f"dry_run={args.dry_run} "
            f"generate_only={args.generate_only} post_only={args.post_only}",
        )

        if not args.post_only:
            fetch_trend_context(run_id, paths)
            fetch_reference_context(run_id, paths)
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
    return "reel", "fixed_serious_life_dialogue_reel"


def determine_content_mode(run_id: str) -> tuple[str, str]:
    return "life_dialogue", "fixed_life_dialogue_series"


def run_paths(run_id: str) -> dict[str, Path]:
    images = tuple(
        ROOT / "assets" / f"{run_id}_deadpan_joke_{index:02d}.png"
        for index in range(1, CAROUSEL_PAGE_COUNT + 1)
    )
    return {
        "run_dir": ROOT / "posts" / run_id,
        "image": images[0],
        "images": images,
        "caption": ROOT / "captions" / f"{run_id}_deadpan_joke.md",
        "prompt": ROOT / "prompts" / f"{run_id}_generation_prompt.md",
        "manifest": ROOT / "posts" / run_id / "manifest.json",
        "trends": ROOT / "posts" / run_id / "trend_context.txt",
        "reference_dir": ROOT / "posts" / run_id / "reference",
        "reference_metadata": ROOT / "posts" / run_id / "reference_post.json",
        "reference_context": ROOT / "posts" / run_id / "reference_context.txt",
        "reel": ROOT / "assets" / f"{run_id}_deadpan_joke_reel.mp4",
    }


def ensure_dirs(paths: dict[str, Path]) -> None:
    for key in ("run_dir", "reference_dir"):
        paths[key].mkdir(parents=True, exist_ok=True)
    for image_path in paths["images"]:
        image_path.parent.mkdir(parents=True, exist_ok=True)
    for key in ("caption", "prompt"):
        paths[key].parent.mkdir(parents=True, exist_ok=True)


def load_growth_experiment() -> dict:
    strategy_path = ROOT / "analytics" / "daily_strategy.json"
    fallback = {
        "id": "control_emotional_carousel_28",
        "label": "28 秒五頁情緒故事控制組",
        "hook_style": "先說出觀眾不太敢承認的具體感受",
        "topic_pillar": "日常選擇",
        "conclusion_style": "貓把隱藏假設壓成一句可收藏的新視角",
        "cta_style": "自然短問句",
        "reel_seconds": REEL_SECONDS,
    }
    if not strategy_path.exists():
        return fallback
    try:
        strategy = json.loads(strategy_path.read_text(encoding="utf-8"))
        experiment = strategy.get("next_experiment")
        if not isinstance(experiment, dict) or not experiment.get("id"):
            return fallback
        return {**fallback, **experiment}
    except (OSError, ValueError, TypeError):
        return fallback


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
    ]
    for reference_image in paths.get("reference_images", ()):
        cmd.extend(["--image", str(reference_image)])
    cmd.extend([
        "--output-last-message",
        str(paths["run_dir"] / "codex_last_message.txt"),
        "-",
    ])
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
Content mode: EMOTIONAL LIFE DIALOGUE (情緒型人生對話)
- Start from one concrete adult-life tension such as comparison, rest, boundaries, uncertainty, loneliness, failure, body image, work, friendship, or letting go.
- Page 1: a private feeling viewers rarely admit out loud. It must create immediate recognition, not explain the lesson.
- Page 2: one concrete everyday scene showing how that feeling changes Roberto's behavior.
- Page 3: the tuxedo cat asks one short question that exposes the hidden assumption.
- Page 4: Roberto answers honestly and names the fear, shame, or need underneath the behavior.
- Page 5: the cat compresses the emotional turn into one concise, specific insight that changes how pages 1-4 are understood.
- The tone is serious, observant, emotionally grounded, and human. A trace of dry wit is allowed, but no prank energy or forced punchline.
- Avoid generic motivational slogans, fake therapy language, diagnoses, absolute claims, moral superiority, and advice that needs a long explanation.
- Brainstorm scores: relatability, natural dialogue, insight, and save/share value, each 0-5.
- The caption must include #人生對話 and 2-4 other relevant hashtags.
""".strip()
    experiment = paths.get("growth_experiment", {})
    experiment_brief = f"""
Controlled growth experiment for this post:
- Experiment ID: {experiment.get('id', 'control_emotional_carousel_28')}
- Package: {experiment.get('label', '28 秒五頁情緒故事控制組')}
- Required first-page hook: {experiment.get('hook_style', '先說出觀眾不太敢承認的具體感受')}
- Preferred topic pillar: {experiment.get('topic_pillar', '日常選擇')}
- Required conclusion mechanism: {experiment.get('conclusion_style', '貓把隱藏假設壓成一句可收藏的新視角')}
- Caption ending: {experiment.get('cta_style', '自然短問句')}
- Reel target reading time: {experiment.get('reel_seconds', REEL_SECONDS)} seconds total. The pipeline will enforce a readable minimum for five pages.
Treat these as controlled packaging variables. Do not change the fixed characters, originality rules, or five-page emotional-dialogue identity.
""".strip()
    return f"""
You are generating one five-page Instagram carousel story for @roberto_joke.

{content_brief}

{experiment_brief}

Read:
- README.md
- prompts/daily_comic_style.md
- prompts/daily_posting_workflow.md

Attached image:
- assets/main_character_reference.jpg is the mandatory likeness reference for the male main character.
- Any images attached after the likeness reference are slides from one reference post selected for this run.

Daily reference study:
- Read {paths["reference_context"]}. If reference images are attached, study the complete post before brainstorming.
- Privately identify its abstract mechanics: recognition hook, concrete scene, escalation, emotional turn, final compression, and why someone might save or share it.
- Borrow only those abstract mechanics. The output must use a clearly different topic, wording, examples, conclusion, setting, composition, typography, characters, and visual identity.
- Never translate, paraphrase, remix, or imitate a recognizable sentence from the reference. Never mention the source account in the finished post.
- Reject the reference post's substance when it depends on stereotypes, manipulation, absolutist claims, or unsupported relationship/financial advice. Structural study is not endorsement.
- Record the five-part structural analysis and a short originality check in the generation prompt record, not in the caption or artwork.
- If the reference fetch is unavailable, follow the same serious five-beat structure using an original everyday dilemma.

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
- Generate exactly five colorful 1080x1350 images for one Instagram carousel. Each image is one full-page scene with one story beat; do not split a page into comic panels.
- Keep the same characters, wardrobe, rendering, room palette, line weight, and facial identity across all five images. They must feel like one continuous story.
- Follow the selected content mode's five-page emotional structure exactly.
- Put one large Traditional Chinese line on each page. Text must be immediately readable on a phone, fully inside generous safe margins, and never overlap a face.
- The fifth-page conclusion must be the strongest beat. It must reframe or deepen the first four pages, not explain the visible action.
- The male protagonist must be based on the attached reference photo: East Asian man, round youthful face, side-swept black hair, slightly sleepy eyes, wearing a black collared top with gray zipper/placket.
- Preserve the reference identity in a polished realistic-comic meme style. Do not use a generic anime man.
- Style: original polished Taiwanese editorial webcomic with a cinematic, subdued palette, concise spoken Traditional Chinese, and restrained natural acting.
- Use soft practical lighting, calm framing, believable rooms or streets, and subtle facial expressions. Avoid meme fonts, comic explosion lines, exaggerated reaction faces, prank-video energy, stickers, and loud decorative effects.
- Include a black-and-white tuxedo cat in every image. The cat is Roberto's perceptive, calmly incisive dialogue partner.
- The page-five line should begin with "貓：" so the speaker is unmistakable. Page three may also begin with "貓：" when the cat asks its question.
- Use exactly five concise dialogue/caption beats, one per page. Avoid explanatory paragraphs.
- Before generating the image, brainstorm at least 12 genuinely different life-dialogue story candidates. At least 8 must be non-workplace topics.
- Score every candidate for relatability, natural dialogue, insight, and save/share value. Select only the highest-scoring candidate with at least 15/20.
- A valid final line must reframe the setup, expose an overlooked assumption or consequence, or create a more precise way to understand the problem. It must not merely describe what the image already shows.
- Reject corporate-jargon reskins and generic social-media wisdom unless the wording creates a genuinely specific new meaning.
- Compare against the latest 20 posts. Vary the dilemma, insight mechanism, setting, pose, and cat reaction, not just the nouns.
- Record the top five candidate stories, scores, rejection notes, and the reason for the final selection in the generation prompt record. Still generate exactly one five-page story across five images.
- Caption must use only 3-5 relevant hashtags and include the selected mode's required hashtag. Add one natural conversational question only when it fits; never use spammy engagement bait.
- Do not post to Instagram.
- Do not run git push.
- Do not print .env, tokens, access keys, or secrets.

Output these exact files:
{chr(10).join(f'- Carousel page {index}: {path}' for index, path in enumerate(paths['images'], start=1))}
- Caption: {paths["caption"]}
- Prompt record: {paths["prompt"]}
- Manifest: {paths["manifest"]}

Manifest JSON must include:
{{
  "run_id": "{run_id}",
  "content_mode": "{content_mode}",
  "topic": "<short topic>",
  "image_paths": {json.dumps([f"assets/{run_id}_deadpan_joke_{index:02d}.png" for index in range(1, CAROUSEL_PAGE_COUNT + 1)], ensure_ascii=False, indent=2)},
  "caption_path": "captions/{run_id}_deadpan_joke.md",
  "prompt_path": "prompts/{run_id}_generation_prompt.md",
  "status": "generated"
}}

Avoid repeating old topics, setups, or exact punchlines already found in posts/, captions/, assets/.
The story must reward swiping: pages 1-4 deepen one recognizable tension naturally, then page 5 delivers a cat conclusion worth sharing or saving.
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


def fetch_reference_context(run_id: str, paths: dict[str, Path]) -> None:
    fallback = (
        "Reference study unavailable for this run. Use an original serious life dialogue and the fixed five-beat structure.\n"
    )
    paths["reference_images"] = ()
    if not REFERENCE_FETCH_PYTHON.exists() or not REFERENCE_FETCH_SCRIPT.exists():
        paths["reference_context"].write_text(fallback, encoding="utf-8")
        log(run_id, "reference study unavailable: fetch runtime or script missing")
        return

    result = subprocess.run(
        [
            str(REFERENCE_FETCH_PYTHON),
            str(REFERENCE_FETCH_SCRIPT),
            "--run-id",
            run_id,
            "--output-dir",
            str(paths["reference_dir"]),
            "--metadata",
            str(paths["reference_metadata"]),
            "--context",
            str(paths["reference_context"]),
        ],
        cwd=ROOT,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        timeout=120,
    )
    if result.returncode != 0:
        paths["reference_context"].write_text(fallback, encoding="utf-8")
        log(run_id, f"reference study unavailable; continuing: {redact(result.stdout).strip()[:300]}")
        return
    try:
        metadata = json.loads(result.stdout.strip().splitlines()[-1])
        images = tuple(Path(path) for path in metadata.get("downloaded_files", []))
    except (ValueError, TypeError, IndexError):
        images = ()
    paths["reference_images"] = tuple(path for path in images if path.exists())
    log(run_id, f"reference study ready slides={len(paths['reference_images'])}")


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


def maintain_instagram_token(run_id: str) -> None:
    result = subprocess.run(
        [str(NODE_BIN), "scripts/maintain-instagram-token.mjs"],
        cwd=ROOT,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        timeout=60,
    )
    output = redact(result.stdout.strip())
    if result.returncode != 0:
        log(run_id, f"Instagram token preflight failed: {output[:1000]}")
        raise RuntimeError(
            "Instagram authorization is invalid or expired; generation stopped before creating new assets"
        )
    log(run_id, f"Instagram token preflight passed: {output[:1000]}")


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
    manifest["growth_experiment"] = paths.get("growth_experiment", {})
    if publish_format == "reel":
        create_reel(run_id, paths)
        manifest["video_path"] = rel(paths["reel"])
        manifest["motion_style"] = "cinematic_2_5d_v1"
        reel_seconds, page_durations = reel_timing(paths)
        manifest["reel_seconds"] = reel_seconds
        manifest["page_durations"] = page_durations
    else:
        manifest.pop("video_path", None)
    paths["manifest"].write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def render_reel_preview(source_run_id: str) -> Path:
    paths = run_paths(source_run_id)
    missing = [str(path) for path in paths["images"] if not path.exists()]
    if missing:
        raise RuntimeError(f"Preview source images not found: {missing}")
    preview_dir = ROOT / "previews"
    preview_dir.mkdir(parents=True, exist_ok=True)
    paths["reel"] = preview_dir / f"{source_run_id}_motion_preview.mp4"
    create_reel(f"preview-{source_run_id}", paths)
    return paths["reel"]


def build_reel_filter_graph(page_durations: tuple[float, ...]) -> str:
    foreground_size = 1000
    foreground_height = 1250
    foreground_y = (REEL_HEIGHT - foreground_height) // 2
    segments = []
    for index, duration in enumerate(page_durations):
        frames = max(2, int(round(duration * REEL_FPS)))
        zoom_amount = 0.018 if index == 0 else 0.032
        horizontal_direction = 1 if index == 0 else -1
        vertical_direction = -1 if index == 0 else 1
        segments.append(
            f"[{index}:v]split=2[bg{index}src][fg{index}src];"
            f"[bg{index}src]scale=1200:2134:force_original_aspect_ratio=increase,"
            f"crop={REEL_WIDTH}:{REEL_HEIGHT}:"
            f"x='(in_w-out_w)/2+{horizontal_direction}*18*sin(t*0.34)':"
            f"y='(in_h-out_h)/2+{vertical_direction}*12*cos(t*0.27)',"
            f"boxblur=35:12[bg{index}];"
            f"[fg{index}src]scale={foreground_size}:{foreground_height}[fg{index}];"
            f"[bg{index}][fg{index}]overlay="
            f"x='(W-w)/2+4*sin(t*0.72+{index})':"
            f"y='{foreground_y}+3*sin(t*1.15+{index})':eval=frame[scene{index}];"
            f"[scene{index}]zoompan="
            f"z='1+{zoom_amount}*pow(on/{frames - 1},1.15)':"
            f"x='iw/2-(iw/zoom/2)+2*sin(on/18+{index})':"
            f"y='ih/2-(ih/zoom/2)+2*cos(on/24+{index})':"
            f"d=1:s={REEL_WIDTH}x{REEL_HEIGHT}:fps={REEL_FPS},"
            f"fps={REEL_FPS},setsar=1,settb=AVTB,setpts=PTS-STARTPTS[v{index}]"
        )
    streams = "".join(f"[v{index}]" for index in range(len(page_durations)))
    segments.append(f"{streams}concat=n={len(page_durations)}:v=1:a=0,format=yuv420p[v]")
    return ";".join(segments)


def create_reel(run_id: str, paths: dict[str, Path]) -> None:
    if not FFMPEG_BIN.exists():
        raise RuntimeError(f"ffmpeg not found: {FFMPEG_BIN}")
    soundtrack = paths["run_dir"] / "reflective_soundtrack.wav"
    reel_seconds, page_durations = reel_timing(paths)
    transition_times = tuple(sum(page_durations[:index]) for index in range(1, len(page_durations)))
    create_reflective_soundtrack(soundtrack, reel_seconds, transition_times)
    filter_graph = build_reel_filter_graph(page_durations)
    command = [str(FFMPEG_BIN), "-y"]
    for image_path, duration in zip(paths["images"], page_durations):
        command.extend(["-loop", "1", "-framerate", str(REEL_FPS), "-t", str(duration), "-i", str(image_path)])
    command.extend([
        "-i", str(soundtrack),
        "-filter_complex",
        filter_graph,
        "-map",
        "[v]",
        "-map",
        f"{len(paths['images'])}:a",
        "-t",
        str(reel_seconds),
        "-r",
        str(REEL_FPS),
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


def reel_timing(paths: dict) -> tuple[int, tuple[float, ...]]:
    experiment = paths.get("growth_experiment", {})
    page_count = len(paths["images"])
    minimum_seconds = page_count * 5
    reel_seconds = max(minimum_seconds, min(36, int(experiment.get("reel_seconds", REEL_SECONDS))))
    first_seconds = 5.0
    last_seconds = 6.0
    if page_count == 1:
        return reel_seconds, (float(reel_seconds),)
    if page_count == 2:
        return reel_seconds, (first_seconds, reel_seconds - first_seconds)
    middle_seconds = (reel_seconds - first_seconds - last_seconds) / (page_count - 2)
    durations = (first_seconds, *(middle_seconds for _ in range(page_count - 2)), last_seconds)
    return reel_seconds, tuple(round(value, 3) for value in durations)


def create_reflective_soundtrack(
    output: Path,
    reel_seconds: int,
    transition_times: tuple[float, ...],
) -> None:
    sample_rate = 48_000
    total_samples = reel_seconds * sample_rate
    audio = [0.0] * total_samples

    # Slow original underscore: soft minor-seventh chords and a restrained page-turn chime.
    beat = 60.0 / 72.0
    chord_progression = (
        (220.00, 261.63, 329.63, 392.00),
        (174.61, 220.00, 261.63, 329.63),
        (196.00, 246.94, 293.66, 369.99),
        (164.81, 207.65, 261.63, 329.63),
    )
    notes = []
    for chord_index in range(math.ceil(reel_seconds / (beat * 2))):
        start = chord_index * beat * 2
        chord = chord_progression[chord_index % len(chord_progression)]
        for note_index, frequency in enumerate(chord):
            notes.append((start + note_index * 0.055, 1.65, frequency, 0.095))
        notes.append((start, 1.2, chord[0] / 2, 0.12))

    for start, duration, frequency, volume in notes:
        start_sample = int(start * sample_rate)
        note_samples = int(duration * sample_rate)
        for index in range(note_samples):
            position = start_sample + index
            if position >= total_samples:
                break
            elapsed = index / sample_rate
            decay = math.exp(-2.0 * elapsed)
            attack = min(1.0, elapsed / 0.045)
            tone = (
                math.sin(2 * math.pi * frequency * elapsed)
                + 0.18 * math.sin(2 * math.pi * frequency * 2 * elapsed)
            )
            audio[position] += volume * attack * decay * tone / 1.18

    for transition_time in transition_times:
        for hit_time, frequency in ((transition_time, 659.25), (transition_time + 0.12, 880.00)):
            start_sample = int(hit_time * sample_rate)
            hit_samples = int(0.65 * sample_rate)
            for index in range(hit_samples):
                position = start_sample + index
                if position >= total_samples:
                    break
                elapsed = index / sample_rate
                audio[position] += (
                    0.065
                    * math.sin(2 * math.pi * frequency * elapsed)
                    * math.exp(-5.2 * elapsed)
                )

    peak = max(max(abs(sample) for sample in audio), 0.001)
    scale = 0.62 / peak
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
        for index in range(1, CAROUSEL_PAGE_COUNT + 1)
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
