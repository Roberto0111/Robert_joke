# Daily Posting Workflow

每次排程只做一篇 IG 貼文。

## Output Naming

使用台北時間建立資料：

```text
posts/YYYY-MM-DD_HHMM/
assets/YYYY-MM-DD_HHMM_deadpan_joke.png
captions/YYYY-MM-DD_HHMM_deadpan_joke.md
prompts/YYYY-MM-DD_HHMM_generation_prompt.md
```

## Required Steps

1. 讀取 `prompts/daily_comic_style.md`。
2. 使用 `assets/main_character_reference.jpg` 作為男主角本人照片參考，生成時必須保留本人特徵。
3. 檢查 `posts/` 舊貼文，避免重複主題與台詞。
4. 先構思一則新的「認真講幹話」六格腳本。
5. 用 imagegen 生成一張彩色六格漫畫。
5. 把圖存到 `assets/YYYY-MM-DD_HHMM_deadpan_joke.png`。
6. 產生 IG caption 到 `captions/YYYY-MM-DD_HHMM_deadpan_joke.md`。
7. 產生本次 prompt 到 `prompts/YYYY-MM-DD_HHMM_generation_prompt.md`。
8. 建立 `posts/YYYY-MM-DD_HHMM/manifest.json`，記錄圖片、caption、主題、是否發文。
9. commit 並 push 到 GitHub `main`，讓 raw image URL 可以公開存取。
10. 使用 Instagram API 發文：

```bash
IG_IMAGE_URL=https://raw.githubusercontent.com/Roberto0111/Robert_joke/main/assets/YYYY-MM-DD_HHMM_deadpan_joke.png \
IG_CAPTION_FILE=captions/YYYY-MM-DD_HHMM_deadpan_joke.md \
/Users/roberto/.cache/codex-runtimes/codex-primary-runtime/dependencies/node/bin/node scripts/post-to-instagram.mjs
```

11. 發文成功後，把 IG media id 寫入 manifest，再 commit/push 一次。

## Git Push

使用 repo 專用 deploy key：

```bash
git -c core.sshCommand="ssh -i /Users/roberto/.ssh/id_ed25519_robert_joke -o IdentitiesOnly=yes" push
```

## Stop Conditions

如果圖片生成失敗、圖片明顯不是六格、caption 不存在、GitHub push 失敗、或 IG API 回錯誤，停止，不要假裝成功。
