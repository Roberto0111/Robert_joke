# Robert Joke

認真講幹話六格漫畫。

目前收錄：

- `assets/001_deadpan_nonsense_tuxedo_cat.png`
- `captions/001_deadpan_nonsense_tuxedo_cat.md`

IG 文案：

```text
不是偷懶，是提前抵達成果。

#認真講幹話 #六格漫畫 #賓士貓 #台式幽默 #IG漫畫
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

Instagram API 發圖流程是先建立 media container，再呼叫 publish。預設使用 Instagram Login token 路線，也就是 `graph.instagram.com`。如果你要改用 Facebook Graph API token，請把 `IG_API_MODE` 改成 `facebook_graph`。

## Python 排程流程

穩定版流程由 Python 主控：

```text
LaunchAgent com.roberto.robert-joke
  -> scripts/run_daily_pipeline.py
  -> codex exec 生成圖片/caption/manifest
  -> Python 等圖片檔出現
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

排程時間：

```text
08:00
12:00
18:00
```

log 會寫到：

```text
logs/cron.log
logs/pipeline.log
posts/RUN_ID/codex_exec.log
posts/RUN_ID/instagram_publish.log
```
