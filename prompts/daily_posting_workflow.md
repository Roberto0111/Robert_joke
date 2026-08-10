# Daily Posting Workflow

每天 20:30 執行一次，只產出並發布一則 `life_dialogue` 人生對話四格故事。

## Output Naming

```text
posts/YYYY-MM-DD_HHMM/
assets/YYYY-MM-DD_HHMM_deadpan_joke_01.png
assets/YYYY-MM-DD_HHMM_deadpan_joke_02.png
captions/YYYY-MM-DD_HHMM_deadpan_joke.md
prompts/YYYY-MM-DD_HHMM_generation_prompt.md
```

## Required Steps

1. 透過 Business Discovery 選取指定參考帳號近期一篇未讀貼文，把輪播圖下載到當次暫存資料夾。
2. 只分析參考貼文的開場、推進、轉折、收束與收藏／分享動機，完成原創性檢查後換成不同題目與結論。
3. 讀取 `prompts/daily_comic_style.md`、近期貼文、當次熱門搜尋與 IG 成效策略。
4. 使用 `assets/main_character_reference.jpg` 固定 Roberto 本人外型。
5. 構思並評分至少 12 個人生對話故事，選出總分至少 15/20 且第四格觀點最強的一則。
6. 生成兩張 1080x1350 圖：第 1 張放第 1、2 格，第 2 張放第 3、4 格。
7. 建立 caption、generation prompt 與 manifest；manifest 必須記錄 `content_mode`，`image_paths` 必須依序列出兩張圖。
8. Python 檢查兩張圖尺寸、檔案大小與 manifest，任何一項不符就停止。
9. 固定製作 16 秒直式 Reel：第 1 頁停留 7 秒、第 2 頁停留 9 秒，搭配原創沉穩配樂；兩張原圖仍保留供內容檢查。
10. commit 並用專用 deploy key push 到 GitHub，等待公開 URL 可讀後再呼叫 Instagram API。
11. 主貼文成功後同步發布 Story，並把 media id 與狀態寫回 manifest。

## Stop Conditions

圖片不是兩張、不是 1080x1350、不是四格、主角不像本人、賓士貓缺席、繁中錯字、兩張風格不連續、caption/manifest 缺失、GitHub push 或 IG API 失敗時，停止並留下明確 log，不得假裝成功。

參考貼文 API 暫時不可用時可退回固定四拍人生對話，不得因此停止整個日更；參考圖片與帳號 token 都不得 commit 到 GitHub。
