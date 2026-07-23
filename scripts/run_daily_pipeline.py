#!/usr/bin/env python3
import argparse
import datetime as dt
import json
import os
import re
import shutil
import subprocess
import sys
import time
import urllib.request
import xml.etree.ElementTree as ET
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CODEX_BIN = Path(os.environ.get("CODEX_BIN", "/Applications/Codex.app/Contents/Resources/codex"))
NODE_BIN = Path(os.environ.get(
    "NODE_BIN",
    "/Users/roberto/.cache/codex-runtimes/codex-primary-runtime/dependencies/node/bin/node",
))
SSH_KEY = Path(os.environ.get("ROBERT_JOKE_SSH_KEY", "/Users/roberto/.ssh/id_ed25519_robert_joke"))
CHARACTER_REFERENCE = ROOT / "assets" / "main_character_reference.jpg"
LOCK_FILE = ROOT / ".daily_pipeline.lock"
LOG_DIR = ROOT / "logs"
TIMEOUT_SECONDS = int(os.environ.get("ROBERT_JOKE_CODEX_TIMEOUT", "3600"))
POLL_SECONDS = int(os.environ.get("ROBERT_JOKE_POLL_SECONDS", "5"))
IG_IMAGE_WIDTH = 1080
IG_IMAGE_HEIGHT = 1080


def main() -> int:
    parser = argparse.ArgumentParser(description="Trigger Codex generation, then publish the image to Instagram.")
    parser.add_argument("--run-id", default=current_run_id(), help="Run id, default YYYY-MM-DD_HHMM in local time.")
    parser.add_argument("--generate-only", action="store_true", help="Only trigger Codex and wait for local files.")
    parser.add_argument("--post-only", action="store_true", help="Skip Codex and publish an existing run id.")
    parser.add_argument("--dry-run", action="store_true", help="Do not push or publish; useful for testing.")
    args = parser.parse_args()

    LOG_DIR.mkdir(exist_ok=True)
    with locked():
        run_id = args.run_id
        paths = run_paths(run_id)
        ensure_dirs(paths)
        log(run_id, f"pipeline started dry_run={args.dry_run} generate_only={args.generate_only} post_only={args.post_only}")

        if not args.post_only:
            fetch_trend_context(run_id, paths)
            trigger_codex(run_id, paths, args.dry_run)
            if args.dry_run:
                log(run_id, "dry-run complete; skipping file wait, git push, and Instagram publish")
                return 0
            wait_for_generation(run_id, paths)

        normalize_image_for_instagram(run_id, paths)
        validate_generation(paths)

        if args.generate_only:
            log(run_id, "generate-only complete")
            return 0

        if args.dry_run:
            log(run_id, "dry-run complete; skipping git push and Instagram publish")
            return 0

        commit_and_push_generated(run_id, paths)
        media_id = publish_to_instagram(run_id, paths)
        mark_published(run_id, paths, media_id)
        commit_and_push_published(run_id, paths)
        log(run_id, f"pipeline complete media_id={media_id}")
        return 0


def current_run_id() -> str:
    return dt.datetime.now().strftime("%Y-%m-%d_%H%M")


def run_paths(run_id: str) -> dict[str, Path]:
    return {
        "run_dir": ROOT / "posts" / run_id,
        "image": ROOT / "assets" / f"{run_id}_deadpan_joke.png",
        "caption": ROOT / "captions" / f"{run_id}_deadpan_joke.md",
        "prompt": ROOT / "prompts" / f"{run_id}_generation_prompt.md",
        "manifest": ROOT / "posts" / run_id / "manifest.json",
        "trends": ROOT / "posts" / run_id / "trend_context.txt",
    }


def ensure_dirs(paths: dict[str, Path]) -> None:
    for key in ("run_dir",):
        paths[key].mkdir(parents=True, exist_ok=True)
    for key in ("image", "caption", "prompt"):
        paths[key].parent.mkdir(parents=True, exist_ok=True)


def trigger_codex(run_id: str, paths: dict[str, Path], dry_run: bool) -> None:
    if dry_run:
        prompt_file = paths["run_dir"] / "codex_prompt.txt"
        prompt_file.write_text(build_codex_prompt(run_id, paths), encoding="utf-8")
        log(run_id, f"dry-run: wrote codex prompt to {prompt_file}")
        return

    if not CODEX_BIN.exists():
        raise RuntimeError(f"Codex CLI not found: {CODEX_BIN}")
    if not CHARACTER_REFERENCE.exists():
        raise RuntimeError(f"Main character reference not found: {CHARACTER_REFERENCE}")

    prompt = build_codex_prompt(run_id, paths)
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


def build_codex_prompt(run_id: str, paths: dict[str, Path]) -> str:
    return f"""
You are generating exactly one Instagram single-panel meme for @roberto_joke.

Read:
- README.md
- prompts/daily_comic_style.md
- prompts/daily_posting_workflow.md

Attached image:
- assets/main_character_reference.jpg is the mandatory likeness reference for the male main character.

Current trend context:
- Read {paths["trends"]}. It contains current Taiwan Google search trends fetched immediately before this run.
- You may use a trend only when its context naturally supports a funny everyday joke. Never force a trend into the image.
- Skip politics, crime, disasters, deaths, medical scares, allegations, and other sensitive news.
- If web search is available, verify the meaning of any current Taiwanese meme phrase before using it. Never copy another creator's image or caption verbatim.
- Original jokes are always acceptable and preferred over a weak trend reference.

Hard requirements:
- Generate exactly one colorful square single-panel meme image. Never generate a six-panel comic or multiple images.
- Image must be 1080x1080 pixels, 1:1 square, safe for Instagram feed with no cropping.
- Use the fixed meme layout: oversized rough black Traditional Chinese headline on a white band at the top, one absurd central scene, and an oversized rough black Traditional Chinese punchline on a white band at the bottom.
- The top line is a serious setup. The bottom line is a short, stupid, blunt reversal. Both lines must be immediately readable on a phone and must stay fully inside a generous safe margin.
- The male protagonist must be based on the attached reference photo: East Asian man, round youthful face, side-swept black hair, slightly sleepy eyes, wearing a black collared top with gray zipper/placket.
- Preserve the reference identity in a polished realistic-comic meme style. Do not use a generic anime man.
- Style: 北七、靠杯、擺爛、一本正經講幹話的台灣網路迷因，使用繁體中文。The protagonist should look absurdly solemn while visibly doing something stupid.
- Include a black-and-white tuxedo cat in every image. The cat is the sharp deadpan roast character: it should expose, insult, or bluntly correct the protagonist's nonsense.
- The bottom punchline should usually be the cat's line and begin with "貓：" so the speaker is unmistakable.
- Prefer an obvious visual contradiction: hiding while discussing management, sleeping while discussing efficiency, giving up while presenting strategy, or similar everyday nonsense. Do not limit topics to offices or companies.
- Use no more than two main text lines. Avoid speech bubbles and explanatory paragraphs.
- Before generating the image, brainstorm at least 12 genuinely different joke candidates. At least 8 must be non-workplace topics.
- Score every candidate from 0-5 for surprise, visual contradiction, cat-roast sharpness, and shareability. Select only the highest-scoring candidate with at least 15/20.
- A valid bottom line must REFRAME the setup, expose a hidden consequence, or downgrade the protagonist in an unexpected specific way. It must not merely describe what the image already shows.
- Reject generic explanatory roasts such as "你只是在...", "你根本沒...", or a literal statement of the protagonist's action. Do not use the "你只是" construction in the final joke.
- Reject corporate-jargon reskins (risk management, process optimization, crisis response, strategic planning) unless the wording creates a genuinely new double meaning.
- Compare against the latest 20 posts. Vary the joke mechanism, setting, pose, and cat reaction, not just the nouns.
- Record the top five candidate setups, punchlines, scores, rejection notes, and the reason for the final selection in the generation prompt record. Still generate exactly one image.
- Do not post to Instagram.
- Do not run git push.
- Do not print .env, tokens, access keys, or secrets.

Output these exact files:
- Image: {paths["image"]}
- Caption: {paths["caption"]}
- Prompt record: {paths["prompt"]}
- Manifest: {paths["manifest"]}

Manifest JSON must include:
{{
  "run_id": "{run_id}",
  "topic": "<short topic>",
  "image_path": "assets/{run_id}_deadpan_joke.png",
  "caption_path": "captions/{run_id}_deadpan_joke.md",
  "prompt_path": "prompts/{run_id}_generation_prompt.md",
  "status": "generated"
}}

Avoid repeating old topics, setups, or exact punchlines already found in posts/, captions/, assets/.
The joke must work in one glance: serious setup at the top, ridiculous visual evidence in the middle, blunt reversal at the bottom.
""".strip()


def fetch_trend_context(run_id: str, paths: dict[str, Path]) -> None:
    url = "https://trends.google.com/trending/rss?geo=TW"
    request = urllib.request.Request(url, headers={"User-Agent": "RobertJokeBot/1.0"})
    lines = [
        f"Fetched at: {dt.datetime.now().isoformat(timespec='seconds')}",
        f"Source: {url}",
        "Use only as optional inspiration. Skip sensitive topics and prefer an original joke when uncertain.",
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
            lines.append("- No usable trend titles returned; create an original joke.")
        log(run_id, f"trend context fetched topics={len(titles[:15])}")
    except (OSError, ET.ParseError) as exc:
        lines.append(f"- Trend fetch unavailable ({type(exc).__name__}); create an original joke.")
        log(run_id, f"trend context unavailable: {type(exc).__name__}")
    paths["trends"].write_text("\n".join(lines) + "\n", encoding="utf-8")


def normalize_image_for_instagram(run_id: str, paths: dict[str, Path]) -> None:
    width, height = image_size(paths["image"])
    if (width, height) == (IG_IMAGE_WIDTH, IG_IMAGE_HEIGHT):
        log(run_id, f"image already Instagram safe: {width}x{height}")
        return

    backup = paths["run_dir"] / f"{paths['image'].stem}_original_{width}x{height}{paths['image'].suffix}"
    if not backup.exists():
        shutil.copy2(paths["image"], backup)

    temp = paths["run_dir"] / f"{paths['image'].stem}_ig_safe_tmp.png"
    aspect = width / height
    target_aspect = IG_IMAGE_WIDTH / IG_IMAGE_HEIGHT
    if aspect > target_aspect:
        resize_args = ["--resampleWidth", str(IG_IMAGE_WIDTH)]
    else:
        resize_args = ["--resampleHeight", str(IG_IMAGE_HEIGHT)]

    run(["sips", *resize_args, str(paths["image"]), "--out", str(temp)], cwd=ROOT)
    run([
        "sips",
        "--padToHeightWidth",
        str(IG_IMAGE_HEIGHT),
        str(IG_IMAGE_WIDTH),
        "--padColor",
        "ffffff",
        str(temp),
        "--out",
        str(paths["image"]),
    ], cwd=ROOT)
    temp.unlink(missing_ok=True)

    new_width, new_height = image_size(paths["image"])
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
    required = [paths["image"], paths["caption"], paths["prompt"], paths["manifest"]]
    while time.time() < deadline:
        if all(p.exists() and p.stat().st_size > 0 for p in required):
            log(run_id, "generation files detected")
            return
        time.sleep(POLL_SECONDS)
    missing = [str(p) for p in required if not p.exists() or p.stat().st_size == 0]
    raise TimeoutError(f"Timed out waiting for generated files: {missing}")


def validate_generation(paths: dict[str, Path]) -> None:
    if paths["image"].suffix.lower() not in {".png", ".jpg", ".jpeg"}:
        raise RuntimeError(f"Unsupported image file: {paths['image']}")
    if paths["image"].stat().st_size < 100_000:
        raise RuntimeError(f"Generated image looks too small: {paths['image']}")
    caption = paths["caption"].read_text(encoding="utf-8").strip()
    if not caption:
        raise RuntimeError("Caption is empty")
    manifest = json.loads(paths["manifest"].read_text(encoding="utf-8"))
    if manifest.get("status") not in {"generated", "published"}:
        raise RuntimeError("Manifest status must be generated or published")


def commit_and_push_generated(run_id: str, paths: dict[str, Path]) -> None:
    git(["add", rel(paths["image"]), rel(paths["caption"]), rel(paths["prompt"]), rel(paths["manifest"])])
    if has_staged_changes():
        git(["commit", "-m", f"Add daily joke comic {run_id}"])
    git_push()


def publish_to_instagram(run_id: str, paths: dict[str, Path]) -> str:
    if not NODE_BIN.exists():
        raise RuntimeError(f"Node binary not found: {NODE_BIN}")
    image_url = f"https://raw.githubusercontent.com/Roberto0111/Robert_joke/main/assets/{run_id}_deadpan_joke.png"
    env = os.environ.copy()
    env["IG_IMAGE_URL"] = image_url
    env["IG_CAPTION_FILE"] = f"captions/{run_id}_deadpan_joke.md"
    result = subprocess.run(
        [str(NODE_BIN), "scripts/post-to-instagram.mjs"],
        cwd=ROOT,
        env=env,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        timeout=120,
    )
    (paths["run_dir"] / "instagram_publish.log").write_text(redact(result.stdout), encoding="utf-8")
    if result.returncode != 0:
        raise RuntimeError(f"Instagram publish failed; see {paths['run_dir'] / 'instagram_publish.log'}")
    match = re.search(r'"id"\s*:\s*"([^"]+)"', result.stdout)
    if not match:
        raise RuntimeError("Could not parse Instagram media id from publish output")
    return match.group(1)


def mark_published(run_id: str, paths: dict[str, Path], media_id: str) -> None:
    manifest = json.loads(paths["manifest"].read_text(encoding="utf-8"))
    manifest["status"] = "published"
    manifest["instagram_media_id"] = media_id
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
