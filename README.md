# Robert Joke

Roberto 與賓士貓的人生對話 Reels：每天用嚴肅、自然的四格對話談一個具體生活困惑。參考帳號只用來分析抽象敘事節奏，成品的題目、文字、結論與視覺都必須原創。

GitHub Pages 可使用 `index.html` 作為首頁。

## Instagram API 發文

這個 repo 也包含一個最小的 Instagram Graph API 發文腳本。

1. 先把圖片放到公開可讀的網址，例如 GitHub raw file：

   ```text
   https://raw.githubusercontent.com/Roberto0111/Robert_joke/main/assets/001_deadpan_nonsense_tuxedo_cat.png
   ```

2. 複製環境變數範本：

   ```bash
   cp .env.example .env
   ```

3. 編輯 `.env`：

   ```text
   IG_USER_ID=你的 Instagram Business/Creator IG User ID
   IG_ACCESS_TOKEN=你的 Instagram API access token
   IG_IMAGE_URL=https://raw.githubusercontent.com/Roberto0111/Robert_joke/main/assets/001_deadpan_nonsense_tuxedo_cat.png
   IG_CAPTION_FILE=captions/001_deadpan_nonsense_tuxedo_cat.md
   IG_API_MODE=instagram_login
   IG_GRAPH_VERSION=v23.0
   ```

4. 先檢查 token：

   ```bash
   npm run check:ig-token
   ```

5. 先 dry run 檢查 payload：

   ```bash
   npm run post:ig:dry-run
   ```

6. 發文：

   ```bash
   npm run post:ig
   ```

Instagram API 發圖或 Reel 的流程都是先建立 media container，再呼叫 publish。Reel 會先等待影片處理完成才發布。預設使用 Instagram Login token 路線，也就是 `graph.instagram.com`。如果你要改用 Facebook Graph API token，請把 `IG_API_MODE` 改成 `facebook_graph`。

## Python 排程流程

穩定版流程由 Python 主控：

```text
LaunchAgent com.roberto.robert-joke
  -> scripts/run_daily_pipeline.py
  -> 蒐集近期 IG 成效、台灣熱門搜尋與一篇參考帳號貼文
  -> 只學參考貼文的敘事結構，換題目、換結論並做原創性檢查
  -> codex exec 生成兩張四格輪播圖/caption/manifest
  -> 固定製作 16 秒沉穩風格直式 Reel
  -> Python 等兩張圖片檔出現並驗證為 1080x1350
  -> git push 到 GitHub
  -> Instagram API 發文
  -> manifest 寫入 IG media id
```

手動跑一次：

```bash
/usr/bin/python3 scripts/run_daily_pipeline.py
```

只測流程，不真的推 GitHub 或發 IG：

```bash
/usr/bin/python3 scripts/run_daily_pipeline.py --dry-run
```

已有圖片和 caption，只補發某一篇：

```bash
/usr/bin/python3 scripts/run_daily_pipeline.py --post-only --run-id 2026-07-03_1210
```

正式排程使用 macOS LaunchAgent：

```text
/Users/roberto/Library/LaunchAgents/com.roberto.robert-joke.plist
```

LaunchAgent 的工作目錄是：

```text
/Users/roberto/Automation/Robert_joke
```

目前日更模式：

```text
每天 20:30
每天發布「人生對話」
每天先分析 Reel 與圖片的觀看、觸及、分享、收藏
每日先讀一篇指定參考帳號貼文，只抽取抽象敘事方法，不複製內容或視覺
固定發布 Reel，依序播放兩張四格原稿，使用原創沉穩背景音，總長 16 秒
```

成長策略與基準記錄在 `growth/strategy.md`。IG 成效會每天寫入本機 `analytics/`，不會 commit token 或私密資料。

log 會寫到：

```text
logs/cron.log
logs/pipeline.log
posts/RUN_ID/codex_exec.log
posts/RUN_ID/instagram_publish.log
```
