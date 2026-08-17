# Daily Posting Workflow

每天 20:30 執行一次，只產出並發布一則 `life_dialogue` 五頁情緒型人生對話。

## Output Naming

```text
posts/YYYY-MM-DD_HHMM/
assets/YYYY-MM-DD_HHMM_deadpan_joke_01.png
assets/YYYY-MM-DD_HHMM_deadpan_joke_02.png
assets/YYYY-MM-DD_HHMM_deadpan_joke_03.png
assets/YYYY-MM-DD_HHMM_deadpan_joke_04.png
assets/YYYY-MM-DD_HHMM_deadpan_joke_05.png
captions/YYYY-MM-DD_HHMM_deadpan_joke.md
prompts/YYYY-MM-DD_HHMM_generation_prompt.md
```

## Required Steps

1. 透過 Business Discovery 從 `@itsmumutime` 選取近期一篇未讀、偏情緒與生活觀察的貼文，把輪播圖下載到當次暫存資料夾；排除促銷與加盟內容。
2. 只分析參考貼文的情緒辨識鉤子、具體場景、推進、轉折、收束與收藏／分享動機，完成原創性檢查後換成不同題目與結論。
3. 讀取 `prompts/daily_comic_style.md`、近期貼文、當次熱門搜尋與 IG 成效策略；嚴格執行當日唯一的 `growth_experiment`，不要同時改動其他變因。
4. 使用 `assets/main_character_reference.jpg` 固定 Roberto 本人外型。
5. 構思並評分至少 12 個人生對話故事，選出總分至少 15/20 且第五頁觀點最強的一則。
6. 生成五張 1080x1350 單頁場景，依序完成情緒辨識、生活證據、貓的反問、真心坦白與情緒收束。
7. 建立 caption、generation prompt 與 manifest；manifest 必須記錄 `content_mode`，`image_paths` 必須依序列出五張圖。
8. Python 檢查五張圖尺寸、檔案大小與 manifest，任何一項不符就停止。
9. 製作至少 25 秒直式 Reel；每頁至少保留 5 秒，最後收束頁保留較久，搭配原創沉穩配樂，首幀不得黑畫面；五張原圖仍保留供內容檢查。
10. commit 並用專用 deploy key push 到 GitHub，等待公開 URL 可讀後再呼叫 Instagram API。
11. 主貼文成功後同步發布 Story，並把 media id 與狀態寫回 manifest。

## Stop Conditions

圖片不是五張、不是 1080x1350、主角不像本人、賓士貓缺席、繁中錯字、五張風格不連續、caption/manifest 缺失、GitHub push 或 IG API 失敗時，停止並留下明確 log，不得假裝成功。

參考貼文 API 暫時不可用時可退回固定五拍人生對話，不得因此停止整個日更；參考圖片與帳號 token 都不得 commit 到 GitHub。
