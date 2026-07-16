# 2026-07-16_0800 Generation Prompt

Run ID: `2026-07-16_0800`

Topic: 備忘錄資料湖治理

## History Check

Read `README.md`, `prompts/daily_comic_style.md`, and `prompts/daily_posting_workflow.md`.

Checked prior manifests and captions. Avoided repeated topics and exact punchlines about 已讀不回, 開會, 鬧鐘, 請假, 檔案命名, 訊息草稿, 清冰箱, 瀏覽器分頁, 行事曆, 軟體更新, 手機充電, 未讀信件, 發票, 截圖, 桌面整理, 午餐選擇, 咖啡, 視訊會議, 搜尋流程, 自動回覆, 健身會員, 洗衣籃, 水杯堆積, 通知紅點, 購物車, 忘記附檔, 試用訂閱, 垃圾治理, 洗碗, 情緒快取, 使用條款, 降噪耳機, 印表機, 通勤, 外送追蹤, 履歷更新, 待辦清單, and 密碼重設.

## Panel Script

1. 主角正經看著手機備忘錄：「我不是亂開／備忘錄。」
2. 主角拿手機展示空白筆記：「空白標題，／是未定義需求。」
3. 黑白賓士貓冷臉吐槽：「你連標題／都懶。」
4. 主角指白板講流程：「先分類，／會讓問題失去彈性。」
5. 主 punchline：「不是太亂，／是把人生／先放進資料湖。」
6. 無台詞。主角和賓士貓一起沉默看著手機，留下尷尬後味。

## Image Generation Prompt

```text
Use case: illustration-story
Asset type: one Instagram feed comic image, 1080x1350 pixels, 4:5 portrait.
Input images: Image #1 is the mandatory likeness reference for the male protagonist.
Primary request: Create one colorful six-panel comic art layer with a clear 2 columns x 3 rows grid. Leave all lettering out; no readable text, no pseudo-text, no watermark. Leave clean open space in each panel for speech bubbles that will be added later.

Main character: preserve the identity from Image #1 in stylized manga/comic form, not a generic anime man. East Asian man, youthful round face, side-swept black hair with the same silhouette, slightly sleepy calm eyes, soft cheeks, serious deadpan expression. Outfit must match the reference: black collared top with gray zipper/placket.

Scene/topic: night office / desk scene about phone notes and messy memos as a formal data-lake governance strategy. Dry Taiwanese internet humor tone, but visual layer only.

Panel layout and visual beats:
1. Protagonist sits at office desk holding a phone notes app, serious consultant posture, room for a speech bubble near top.
2. Close-up / medium shot of phone with many note cards shown as blank rectangles, protagonist points at it like explaining a workflow, room for bubble.
3. Black-and-white tuxedo cat on desk stares coldly at protagonist; protagonist remains solemn with phone in hand, room for a small cat sign or bubble.
4. Protagonist points at a whiteboard with simple icons only: blank note cards, arrows, folder, lake/water icon; no readable text, room for bubble.
5. Main punchline panel staging: protagonist faces viewer deadpan, holding phone like an official report, tuxedo cat beside him, slightly more emphatic composition, large clear open space for a big speech bubble. Serious face, not laughing.
6. Silent awkward aftertaste: protagonist and tuxedo cat sit quietly at the desk under monitor glow, both staring at the phone; no bubble needed, lots of quiet empty space.

Style/medium: colorful clean digital comic, Taiwanese manga-inspired, crisp ink lines, expressive but restrained faces, warm desk lamp plus cool night window tones, polished Instagram comic look.
Composition/framing: 2 columns x 3 rows, six distinct panels with visible gutters and panel borders. Generous inner safe margin: keep every panel border, face, body, cat, and future bubble area away from the outer 5-7% edge. Important content must not touch outer edges.
Constraints: exactly six panels, 1080x1350 portrait ratio, no cropping. The tuxedo cat must be black-and-white if present. No text anywhere, no English, no captions, no UI labels, no watermark, no secrets/tokens/access keys.
```

## Local Finishing

Used Swift/AppKit locally to recompose the generated art into a `1080x1350` PNG, crop six panels into a 2x3 grid with a 54 px outer margin, draw safe speech bubbles, and add the exact Traditional Chinese dialogue above. Panel 6 was left silent.
