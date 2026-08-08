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

1. 讀取 `prompts/daily_comic_style.md`、近期貼文、當次熱門搜尋與 IG 成效策略。
2. 使用 `assets/main_character_reference.jpg` 固定 Roberto 本人外型。
3. 構思並評分至少 12 個人生對話故事，選出總分至少 15/20 且第四格觀點最強的一則。
4. 生成兩張 1080x1350 圖：第 1 張放第 1、2 格，第 2 張放第 3、4 格。
5. 建立 caption、generation prompt 與 manifest；manifest 必須記錄 `content_mode`，`image_paths` 必須依序列出兩張圖。
6. Python 檢查兩張圖尺寸、檔案大小與 manifest，任何一項不符就停止。
7. 依每日 IG 成效決定發布形式：`image` 代表兩張圖的 carousel；`reel` 代表依序播放兩張圖的 12 秒直式影片。
8. commit 並用專用 deploy key push 到 GitHub，等待公開 URL 可讀後再呼叫 Instagram API。
9. 主貼文成功後同步發布 Story，並把 media id 與狀態寫回 manifest。

## Stop Conditions

圖片不是兩張、不是 1080x1350、不是四格、主角不像本人、賓士貓缺席、繁中錯字、兩張風格不連續、caption/manifest 缺失、GitHub push 或 IG API 失敗時，停止並留下明確 log，不得假裝成功。
