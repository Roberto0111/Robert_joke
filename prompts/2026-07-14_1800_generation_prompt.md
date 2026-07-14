# 2026-07-14_1800 Generation Prompt

Run ID: `2026-07-14_1800`

Topic: 印表機卡紙摩擦測試

Avoided old topics and exact punchlines: 偷懶, 提前抵達成果, 已讀不回, 開會, 拖延, 待辦清單, 密碼重設, 鬧鐘, 請假, 檔案命名, 訊息草稿, 清冰箱, 瀏覽器分頁, 行事曆, 軟體更新, 手機充電, 未讀信件, 發票, 截圖, 桌面整理, 午餐選擇, 咖啡, 視訊會議, 搜尋流程, 自動回覆, 健身房, 洗衣籃, 水杯, 通知治理, 購物車, 忘記附檔, 訂閱, 垃圾治理, 洗碗, 情緒快取, 使用條款, 降噪耳機.

## Final Panel Script

1. 主角站在辦公室印表機旁，拿著一張紙，表情像在開檢討會。Speech bubble:「我不是 / 印不出來。」
2. 主角指著白板上的文件、印表機、皺紙與風險圖示。Speech bubble:「我是在做 / 紙張路徑 / 風險盤點。」
3. 賓士貓趴在卡紙的印表機上冷眼看著。Cat speech bubble:「你只是 / 卡紙。」
4. 主角蹲在印表機旁，冷靜處理卡住的紙。Speech bubble:「卡住代表 / 文件開始 / 接觸現實。」
5. Main punchline panel. 主角雙手交疊像顧問下結論，印表機與賓士貓在旁邊。Speech bubble:「不是印不出來， / 是讓文件 / 先接受現實 / 摩擦測試。」
6. Silent awkward aftertaste. 印表機吐出一張空白紙，主角、同事與賓士貓沉默看著，沒有對話框。

## Image Generation Prompt

```text
Use case: illustration-story
Asset type: Instagram feed comic image, final-safe 4:5 portrait composition, requested canvas 1080x1350 pixels.
Input images: Image 1 is the mandatory identity and likeness reference for the male protagonist. Preserve the same person in stylized manga/comic form: East Asian man, round youthful face, side-swept black hair, slightly sleepy eyes, calm deadpan expression, black collared top with a gray zipper/placket. Do not make him a generic anime man.

Primary request: Create exactly one colorful six-panel comic base image for @roberto_joke. The humor style is dry Taiwanese internet humor, serious deadpan nonsense, office-life absurdity. The final dialogue will be added later, so the image must contain blank, clean speech-bubble areas and no readable text.

Composition/framing: 2 columns x 3 rows, exactly six clearly separated panels, all panel borders fully visible. 1080x1350 portrait, generous inner safe margin around the whole comic. Keep all faces, panel borders, blank speech bubbles, important props, and character heads well inside the outer safe area; nothing important touches the edges. Use thick clean comic gutters and crisp black panel borders. Each panel should be uncluttered and readable on a phone.

Scene/backdrop: Night office / copy-room setting with desk, laptop, whiteboard, jammed office printer, paper stack, fluorescent office lighting. Colorful comic palette with warm interior lights, teal shadows, clean line art, expressive but restrained manga/comic styling.

Characters: Main male protagonist based on Image 1, wearing black collared top with gray zipper/placket throughout. A black-and-white tuxedo cat appears in several panels, deadpan and unimpressed, never cute or playful. Optional coworker silhouette in panel 6.

Six panel beats, no readable text anywhere:
1. Protagonist stands beside an office printer with a serious manager expression, holding a single sheet of paper like evidence. Leave one blank white speech bubble near the top, fully inside the panel.
2. Protagonist points at a whiteboard with a simple icon-only flow diagram: document icon, printer icon, crumpled paper icon, and a risk arrow. No letters, no words, no numbers. Leave one blank speech bubble.
3. Tuxedo cat sits on the printer, staring flatly at wrinkled paper sticking out of the printer. Leave one blank speech bubble for the cat.
4. Protagonist kneels calmly near the jammed printer, treating the stuck paper like a formal audit item, face serious and sleepy. Leave one blank speech bubble.
5. Main punchline panel: protagonist faces viewer with hands folded like a consultant delivering a formal conclusion; jammed printer and paper stack visible; tuxedo cat judges silently beside him. Leave the largest blank white speech bubble in this panel, clear and high contrast.
6. Silent awkward aftertaste: printer spits out one blank page while the protagonist, coworker silhouette, and tuxedo cat all stare in awkward silence; no speech bubble needed, quiet pause, deadpan awkwardness.

Text constraints: absolutely no readable text, no fake Chinese, no English, no numbers, no UI captions, no watermarks, no logos. Blank speech bubbles only, clean white with black outlines. Do not include Instagram UI.

Style/medium: colorful Taiwanese manga/comic illustration, clean panel borders, readable character acting, serious dry tone, not photorealistic, not chibi, not generic anime. Preserve the reference identity strongly in the face and hair.
```

## Local Finishing

Generated base image was resized onto a 1080x1350 canvas, then exact Traditional Chinese dialogue was overlaid into the blank speech bubbles with a local Swift/AppKit renderer. Panel 5 contains the main punchline; panel 6 was left wordless.
