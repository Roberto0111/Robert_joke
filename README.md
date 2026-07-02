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

1. 先把圖片放到公開可讀的網址，例如 GitHub Pages：

   ```text
   https://Roberto0111.github.io/Robert_joke/assets/001_deadpan_nonsense_tuxedo_cat.png
   ```

2. 複製環境變數範本：

   ```bash
   cp .env.example .env
   ```

3. 編輯 `.env`：

   ```text
   IG_USER_ID=你的 Instagram Business/Creator IG User ID
   IG_ACCESS_TOKEN=你的 Meta long-lived access token
   IG_IMAGE_URL=https://Roberto0111.github.io/Robert_joke/assets/001_deadpan_nonsense_tuxedo_cat.png
   IG_CAPTION_FILE=captions/001_deadpan_nonsense_tuxedo_cat.md
   ```

4. 先 dry run 檢查 payload：

   ```bash
   npm run post:ig:dry-run
   ```

5. 發文：

   ```bash
   npm run post:ig
   ```

Instagram Graph API 發圖流程是先建立 media container，再呼叫 publish。帳號需要是 Instagram Business 或 Creator，且 access token 要有發佈內容的權限。
