# 2026-07-18_1200 Generation Prompt

Run ID: `2026-07-18_1200`

Topic: 棉被熱部署

Caption punchline: 不是沒摺棉被，是讓睡眠保持熱部署。

Checked prior manifests, captions, prompts, and asset names. Avoided repeated topics and exact punchlines about 已讀不回, 開會, 鬧鐘, 請假, 檔案命名, 訊息草稿, 清冰箱, 瀏覽器分頁, 行事曆, 軟體更新, 手機充電, 未讀信件, 發票, 截圖, 桌面整理, 午餐選擇, 咖啡, 視訊會議, 搜尋流程, 自動回覆, 健身會員, 洗衣籃, 水杯堆積, 通知紅點, 購物車, 忘記附檔, 試用訂閱, 垃圾治理, 洗碗, 情緒快取, 使用條款, 降噪耳機, 印表機, 通勤, 外送追蹤, 履歷更新, 備忘錄資料湖治理, 驗證碼, 滑鼠游標存在證明, 稍後再看, 電梯按鈕, 雨傘風險移轉, 包裝盒退場機制, 待辦清單, and 密碼重設.

Final panel text:

1. 我不是  
   沒摺棉被。
2. 我是在做  
   睡眠系統  
   熱部署。
3. 你只是  
   還想睡。
4. 維持原狀，  
   才能快速回滾。
5. 不是沒摺棉被，  
   是讓睡眠保持熱部署。
6. Silent awkward aftertaste, no dialogue.

Base image generation prompt:

```text
Use case: illustration-story
Asset type: Instagram feed comic for @roberto_joke, final target 1080x1350, 4:5 portrait.
Input image: the attached photo assets/main_character_reference.jpg is the mandatory likeness reference for the male protagonist.
Primary request: Create exactly one colorful six-panel manga/comic image base, 2 columns x 3 rows, portrait 4:5 composition, with generous inner safe margin and clear black panel borders. This base art must have NO readable text and NO speech bubbles; leave clean open areas near the top of panels 1-5 for speech bubbles to be added later.

Main character identity: preserve the attached reference identity in stylized manga/comic form, not a generic anime man. East Asian man, round youthful face, side-swept black hair, slightly sleepy calm eyes, small mouth, understated deadpan expression. Outfit must visibly match the reference: black collared top with gray zipper/placket.

Topic/scene: dry Taiwanese internet humor about not making the bed, framed like a serious operations meeting. Daily bedroom/home-office morning setting with an unmade blanket treated like an IT deployment environment. Include a black-and-white tuxedo cat only; the cat should look cold, judgmental, and unimpressed, not cute or playful.

Panel-by-panel visual staging, with no text rendered:
1. Protagonist stands beside an unmade bed, holding a phone or clipboard like a meeting host, face serious and sleepy; leave upper area clear.
2. Protagonist points at a small whiteboard with only abstract diagram shapes, no letters or numbers, while the messy blanket is visible; leave upper area clear.
3. Black-and-white tuxedo cat sits on the rumpled blanket, staring coldly at the protagonist; leave upper area clear for a cat speech bubble.
4. Protagonist gently pats the blanket like checking a server rack, very formal posture; leave upper area clear.
5. Main punchline staging: protagonist faces viewer with hands folded like a manager delivering a final conclusion, unmade bed and tuxedo cat visible beside him, deadpan serious; leave the largest clean upper area for the main speech bubble.
6. Silent awkward aftertaste: no speech bubble, protagonist and tuxedo cat stare at the unmade bed in silence; the scene should feel awkward and dry.

Style/medium: colorful clean manga/comic, Taiwanese IG comic energy, crisp ink lines, expressive but restrained faces, colorful bedroom/home-office details, warm morning light, high contrast, polished but not glossy.
Composition/framing: exactly six panels, 2 columns by 3 rows, clear gutters, full image in 4:5 portrait. Keep all faces, panel borders, important objects, and future bubble areas well inside a generous safe margin; nothing important may touch outer edges. No cropping. No extra panels.
Text constraints: absolutely no readable Chinese, English, letters, numbers, pseudo-text, captions, signs, watermark, signature, logo, Instagram UI, app UI, tokens, access keys, or secrets. Blank art only, with clean open space for later local lettering.
```

Generation notes:

- Generated one base image with the built-in image generation tool using `assets/main_character_reference.jpg` as the likeness reference.
- Recombined the generated panel art into a centered 1080x1350 canvas with generous margins.
- Added crisp panel borders, white speech bubbles, and exact Traditional Chinese dialogue locally with Swift/AppKit.
- Panel 5 contains the main punchline; panel 6 is silent.
- No Instagram post was made and no git push was run.
