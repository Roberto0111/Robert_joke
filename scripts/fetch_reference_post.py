#!/usr/bin/env python3
from __future__ import annotations

import argparse
import importlib.util
import json
import os
from datetime import datetime
from io import BytesIO
from pathlib import Path
from typing import Any

import requests
from PIL import Image, ImageOps


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_STOCK_ROOT = Path("/Users/roberto/Automation/stock_fund_flow_project")
DEFAULT_USERNAME = "itsmumutime"
STATE_PATH = ROOT / ".reference_state.json"
PREFERRED_KEYWORDS = (
    "人生",
    "生活",
    "自己",
    "工作",
    "同事",
    "朋友",
    "職場",
    "胖",
    "身材",
    "焦慮",
    "界線",
    "父母",
    "家庭",
    "關係",
    "錯過",
    "放下",
    "煩惱",
    "善待",
    "用力",
    "原生家庭",
)
AVOID_KEYWORDS = (
    "選妻",
    "上位",
    "改命",
    "賺錢",
    "段位",
    "加盟",
    "優惠",
    "限時",
    "私訊",
    "下單",
    "購買",
    "經營者",
)


def load_stock_instagram_config(stock_root: Path) -> tuple[dict[str, Any], str]:
    module_path = stock_root / "post_to_instagram.py"
    config_path = stock_root / "config.toml"
    if not module_path.exists() or not config_path.exists():
        raise RuntimeError("Stock Instagram configuration is unavailable")

    spec = importlib.util.spec_from_file_location("stock_post_to_instagram", module_path)
    if spec is None or spec.loader is None:
        raise RuntimeError("Could not load the stock Instagram helper")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    config = module.load_config(config_path)
    ig_config = config.get("instagram", {})
    token = module.get_token(ig_config, None)
    return ig_config, token


def fetch_posts(username: str, stock_root: Path) -> list[dict[str, Any]]:
    ig_config, token = load_stock_instagram_config(stock_root)
    user_id = str(ig_config.get("ig_user_id") or "").strip()
    api_version = str(ig_config.get("api_version") or "v20.0").strip()
    if not user_id:
        raise RuntimeError("Stock Instagram user id is unavailable")

    fields = (
        f"business_discovery.username({username})"
        "{username,media.limit(30){id,caption,media_type,media_url,thumbnail_url,like_count,comments_count,"
        "permalink,timestamp,children.limit(20){id,media_type,media_url,thumbnail_url,permalink}}}"
    )
    response = requests.get(
        f"https://graph.facebook.com/{api_version}/{user_id}",
        params={"fields": fields, "access_token": token},
        timeout=30,
    )
    if not response.ok:
        try:
            error = response.json().get("error", {})
            message = error.get("message") or f"HTTP {response.status_code}"
        except ValueError:
            message = f"HTTP {response.status_code}"
        raise RuntimeError(f"Instagram reference lookup failed: {message}")

    discovery = response.json().get("business_discovery") or {}
    media = discovery.get("media") or {}
    return list(media.get("data") or [])


def load_state() -> dict[str, Any]:
    try:
        return json.loads(STATE_PATH.read_text(encoding="utf-8"))
    except (OSError, ValueError, TypeError):
        return {"history": []}


def select_post(posts: list[dict[str, Any]]) -> tuple[dict[str, Any], str]:
    usable = []
    for post in posts:
        caption = str(post.get("caption") or "").strip()
        children = (post.get("children") or {}).get("data") or []
        if caption and (len(children) >= 3 or post.get("media_url") or post.get("thumbnail_url")):
            usable.append(post)
    if not usable:
        raise RuntimeError("The reference account returned no usable visual posts")

    history = load_state().get("history") or []
    recent_ids = {str(item.get("media_id")) for item in history[-10:] if item.get("media_id")}
    unused = [post for post in usable if str(post.get("id")) not in recent_ids]
    pool = unused or usable

    non_problematic = [
        post
        for post in pool
        if not any(keyword in str(post.get("caption") or "") for keyword in AVOID_KEYWORDS)
    ]
    if non_problematic:
        pool = non_problematic

    def rank(post: dict[str, Any]) -> tuple[int, int, str]:
        caption = str(post.get("caption") or "")
        preferred = sum(keyword in caption for keyword in PREFERRED_KEYWORDS)
        engagement = int(post.get("like_count") or 0) + int(post.get("comments_count") or 0) * 4
        return preferred, engagement, str(post.get("timestamp") or "")

    selected = max(pool, key=rank)
    reason = "newest_unused_serious_life_topic" if unused else "reference_cycle_restarted"
    return selected, reason


def media_items(post: dict[str, Any], limit: int = 8) -> list[dict[str, Any]]:
    children = list(((post.get("children") or {}).get("data") or []))
    items = children or [post]
    if len(items) <= limit:
        return items
    indices = sorted({round(index * (len(items) - 1) / (limit - 1)) for index in range(limit)})
    return [items[index] for index in indices]


def download_images(post: dict[str, Any], output_dir: Path) -> list[Path]:
    output_dir.mkdir(parents=True, exist_ok=True)
    downloaded = []
    for index, item in enumerate(media_items(post), start=1):
        url = item.get("media_url") or item.get("thumbnail_url")
        if not url:
            continue
        response = requests.get(
            str(url),
            headers={"User-Agent": "RobertJokeReferenceReader/1.0"},
            timeout=30,
        )
        if not response.ok:
            raise RuntimeError(f"Reference slide download failed with HTTP {response.status_code}")
        try:
            with Image.open(BytesIO(response.content)) as source:
                image = ImageOps.exif_transpose(source).convert("RGB")
                image.thumbnail((1800, 1800), Image.Resampling.LANCZOS)
                destination = output_dir / f"slide_{index:02d}.jpg"
                image.save(destination, format="JPEG", quality=94, optimize=True)
        except (OSError, ValueError) as exc:
            raise RuntimeError("Reference slide was not a readable image") from exc
        downloaded.append(destination)
    if not downloaded:
        raise RuntimeError("Reference post images could not be downloaded")
    return downloaded


def write_state(media_id: str, run_id: str, permalink: str) -> None:
    state = load_state()
    history = [item for item in state.get("history", []) if str(item.get("media_id")) != media_id]
    history.append({"media_id": media_id, "run_id": run_id, "permalink": permalink})
    state = {"updated_at": datetime.now().isoformat(timespec="seconds"), "history": history[-30:]}
    temp = STATE_PATH.with_suffix(".tmp")
    temp.write_text(json.dumps(state, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    temp.replace(STATE_PATH)


def existing_result(metadata_path: Path) -> dict[str, Any] | None:
    try:
        metadata = json.loads(metadata_path.read_text(encoding="utf-8"))
    except (OSError, ValueError, TypeError):
        return None
    image_paths = [Path(path) for path in metadata.get("downloaded_files", [])]
    if image_paths and all(path.exists() and path.stat().st_size > 0 for path in image_paths):
        return metadata
    return None


def main() -> int:
    parser = argparse.ArgumentParser(description="Fetch one recent life-lesson post for structural study.")
    parser.add_argument("--run-id", required=True)
    parser.add_argument("--output-dir", type=Path, required=True)
    parser.add_argument("--metadata", type=Path, required=True)
    parser.add_argument("--context", type=Path, required=True)
    parser.add_argument("--username", default=os.environ.get("JOKE_REFERENCE_USERNAME", DEFAULT_USERNAME))
    parser.add_argument(
        "--stock-root",
        type=Path,
        default=Path(os.environ.get("REFERENCE_GRAPH_ROOT", str(DEFAULT_STOCK_ROOT))),
    )
    args = parser.parse_args()

    existing = existing_result(args.metadata)
    if existing:
        print(json.dumps(existing, ensure_ascii=False))
        return 0

    posts = fetch_posts(args.username, args.stock_root)
    selected, selection_reason = select_post(posts)
    downloaded = download_images(selected, args.output_dir)
    caption = str(selected.get("caption") or "").strip()
    permalink = str(selected.get("permalink") or "").strip()
    metadata = {
        "username": args.username,
        "media_id": str(selected.get("id") or ""),
        "caption": caption,
        "permalink": permalink,
        "timestamp": str(selected.get("timestamp") or ""),
        "like_count": int(selected.get("like_count") or 0),
        "comments_count": int(selected.get("comments_count") or 0),
        "source_slide_count": len(((selected.get("children") or {}).get("data") or [])) or 1,
        "downloaded_files": [str(path) for path in downloaded],
        "selection_reason": selection_reason,
    }
    args.metadata.parent.mkdir(parents=True, exist_ok=True)
    args.metadata.write_text(json.dumps(metadata, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    args.context.write_text(
        "\n".join(
            [
                f"Reference account: @{args.username}",
                f"Reference permalink: {permalink}",
                f"Reference timestamp: {metadata['timestamp']}",
                f"Reference caption: {caption}",
                "",
                "Use this post only to study abstract storytelling mechanics: recognition hook, concrete scene, tension, emotional turn, compression, and save/share value.",
                "Do not copy or closely paraphrase its wording, topic, conclusion, examples, imagery, layout, typography, characters, or branding.",
                "The Roberto Joke result must use a different topic and an independently reasoned conclusion.",
            ]
        )
        + "\n",
        encoding="utf-8",
    )
    write_state(metadata["media_id"], args.run_id, permalink)
    print(json.dumps(metadata, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
