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
