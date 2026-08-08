# Robert Joke

Roberto 與賓士貓四格輪播：五天認真講幹話，週三與週日用角色對話談人生觀點。

目前收錄：

- `assets/001_deadpan_nonsense_tuxedo_cat.png`
- `captions/001_deadpan_nonsense_tuxedo_cat.md`
- `ai_shorts/pilot_001_landlord_cat/output/roberto_joke_pilot_001.mp4`

IG 文案：

```text
我沒有在逃避問題。
我是讓問題找不到我。

#認真講幹話 #四格漫畫 #賓士貓 #台式幽默 #擺爛哲學
```

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
  -> 蒐集近期 IG 成效與台灣熱門搜尋
  -> codex exec 生成兩張四格輪播圖/caption/manifest
  -> 依每日 IG 成效決定兩張 carousel 或 12 秒直式 Reel
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

14 天成長模式排程：

```text
每天 20:30
週三、週日發布「人生對話」，其餘五天發布「認真講幹話」
每天先分析 Reel 與圖片的觀看、觸及、分享、收藏
目前 Reel 觸及明顯領先，因此每日優先發布 Reel
只有 carousel 成效明顯反超，或分析樣本不足時，才切回兩張輪播／備援星期表
Reel 會依序播放兩張四格原稿，使用原創惡整 Vlog 感背景音，總長 12 秒
```

成長策略與基準記錄在 `growth/strategy.md`。IG 成效會每天寫入本機 `analytics/`，不會 commit token 或私密資料。

log 會寫到：

```text
logs/cron.log
logs/pipeline.log
posts/RUN_ID/codex_exec.log
posts/RUN_ID/instagram_publish.log
```
