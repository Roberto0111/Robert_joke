# 2026-07-17 1200 Generation Prompt

Run ID: `2026-07-17_1200`

Topic: 電梯按鈕需求證據補強

Reference image: `assets/main_character_reference.jpg`

Checked prior manifests, captions, prompts, and asset names. Avoided repeated topics and exact punchlines about 已讀不回, 開會, 鬧鐘, 請假, 檔案命名, 訊息草稿, 清冰箱, 瀏覽器分頁, 行事曆, 軟體更新, 手機充電, 未讀信件, 發票, 截圖, 桌面整理, 午餐選擇, 咖啡, 視訊會議, 搜尋流程, 自動回覆, 健身會員, 洗衣籃, 水杯堆積, 通知紅點, 購物車, 忘記附檔, 試用訂閱, 垃圾治理, 洗碗, 情緒快取, 使用條款, 降噪耳機, 印表機, 通勤, 外送追蹤, 履歷更新, 備忘錄資料湖, 驗證碼登入, 滑鼠游標存在證明, 稍後再看知識冷藏, 待辦清單, and 密碼重設.

## Comic Script

1. 我沒有一直  
   按電梯。
2. 我是在做  
   需求訊號  
   備援。
3. 它已經  
   亮了。
4. 亮只是收到，  
   不代表理解。
5. 不是沒耐心，  
   是替系統補齊  
   需求證據。
6. ……

## Image Generation Prompt

Use case: illustration-story

Asset type: Instagram 4:5 six-panel comic base art for @roberto_joke

Primary request: Create exactly one colorful six-panel comic image in a clean 2-column x 3-row grid, portrait 1080x1350 composition, with generous inner safe margin. This is the illustrated base art for later local lettering: do not render any readable text, letters, captions, labels, watermarks, signatures, or logos.

Input image: Use the attached reference photo as the mandatory identity reference for the male protagonist. Preserve his likeness in stylized manga/comic form: East Asian man, round youthful face, side-swept black hair, slightly sleepy calm eyes, small straight mouth, wearing a black collared top with a gray zipper/placket. He must look like the same person from the reference photo, not a generic anime man.

Scene/backdrop: Modern Taipei apartment or office elevator lobby, everyday setting, elevator doors, elevator call button panel, muted lobby lights, small potted plant, tiled floor, soft city-night feeling. Dry Taiwanese internet humor mood, deadpan and awkward.

Subject and panel beats:

1. The protagonist stands in front of an elevator and presses the call button with a very serious consultant expression; leave uncluttered space for a speech bubble.
2. Close view of his finger hovering near the glowing elevator button while he studies it like system evidence; no readable symbols or letters.
3. A black-and-white tuxedo cat sits on the floor beside the elevator panel, staring coldly at the already-lit button; leave room for a speech bubble.
4. The protagonist gestures at a small blank clipboard or blank flowchart-like board, explaining seriously as if running a process audit; no readable marks.
5. Main punchline staging: protagonist faces viewer with hands folded like a manager delivering a formal conclusion, elevator button and tuxedo cat visible beside him; leave the largest clean space for one large speech bubble.
6. Silent awkward aftertaste: elevator doors are open, the protagonist and tuxedo cat stand still and stare into the empty elevator, expressionless; leave a small clean space for a tiny ellipsis bubble.

Style/medium: colorful Taiwanese manga/comic, crisp ink lines, expressive but restrained deadpan faces, clear comic paneling, Instagram-readable framing.

Composition/framing: exactly six rectangular panels, 2 columns x 3 rows, all panel borders visible, outer safe margin around the whole grid, important faces and objects not touching outer edges. Leave uncluttered areas near the top or side of each panel for later speech bubbles.

Lighting/mood: warm lobby lighting mixed with cool elevator light; funny but dry, not cute or inspirational.

Color palette: varied lobby colors, teal elevator glow, warm beige wall lights, muted black and gray clothing, white speech-bubble-safe spaces.

Constraints: no readable text anywhere; no gibberish text; no cropped faces; no content touching image edges; no extra characters besides the protagonist and one black-and-white tuxedo cat; no duplicate comic pages; no watermark; no Instagram UI; no oversized outer-edge content; protagonist identity must match the reference photo in stylized form.

## Local Post-Processing

Generated one base image with the built-in image generation tool. The generated base was 916x1717, so it was fitted without cropping onto a 1080x1350 canvas and exact Traditional Chinese dialogue was overlaid locally with Swift/AppKit. Panel 5 contains the main punchline; panel 6 is the silent awkward aftertaste. No Instagram post was made and no git push was run.
