# 2026-07-17_1800 Generation Prompt

Topic: 雨傘風險移轉

Use case: illustration-story
Asset type: Instagram comic for @roberto_joke, final 1080x1350 portrait 4:5 feed-safe image.

Reference image:
- `assets/main_character_reference.jpg`
- Mandatory likeness reference for the male protagonist.
- Preserve the reference identity in stylized manga/comic form: East Asian man, round youthful face, side-swept black hair, slightly sleepy calm eyes, black collared top with gray zipper/placket.

Visual generation prompt:

```text
Create exactly one colorful six-panel comic page in a clean 2-column x 3-row grid. Keep a generous inner safe margin around the whole page so all panel borders, faces, blank speech bubbles, and visual story elements stay well away from the outer edges. Each panel must have clear black borders and consistent gutters.

Main character: East Asian man based on the reference photo: round youthful face, side-swept black hair with volume, slightly sleepy calm eyes, deadpan expression, wearing a black collared top with a gray zipper/placket. He should look recognizably like the reference person in a stylized Taiwanese manga/comic style.

Supporting character: A black-and-white tuxedo cat only, with a dry unimpressed expression.

Story/theme: Forgetting an umbrella reframed as serious weather-risk transfer office methodology. Dry Taiwanese internet humor, serious businesslike nonsense.

Panel 1: Night office or daily-life workspace, rainy window visible. The protagonist checks a phone weather app with a serious face. One large empty white speech bubble near the top, safely inside the panel.
Panel 2: The protagonist sits at a desk beside the unimpressed black-and-white tuxedo cat. He gestures like a consultant explaining a policy. One large empty white speech bubble near the top, safely inside the panel.
Panel 3: Meeting-room whiteboard scene. The protagonist points at a diagram with simple icons only: umbrella icon on one side, rain cloud icon on the other side. No readable words on the whiteboard. One large empty white speech bubble near the top, safely inside the panel.
Panel 4: Close-up of the tuxedo cat on the desk, flat unimpressed eyes. The cat can have one small blank placard or one empty white speech bubble, safely inside the panel.
Panel 5: Main punchline panel. The protagonist faces forward very seriously in front of rainy glass doors, like announcing an executive conclusion. One large empty white speech bubble with plenty of room for a short bold line, safely inside the panel.
Panel 6: Silent awkward aftertaste. Outside under a small awning in heavy rain, the protagonist and tuxedo cat stand still with blank deadpan expressions. No speech bubble and no text in this panel.

Style/medium: Colorful polished comic illustration, Taiwanese Instagram six-panel comic, crisp clean line art, expressive but restrained faces, white speech bubbles, readable bubble shapes, gentle office lighting, rainy-night blues mixed with warm indoor colors.
Composition/framing: 1080x1350 portrait, six panels exactly, 2 columns x 3 rows, even gutters, all important content inside inner safe margin.
Text handling: Do not draw any Chinese, English, fake letters, gibberish, captions, watermarks, logos, or readable words anywhere. Leave speech bubbles and placards completely blank pure white so text can be added later.
Constraints: exactly one comic page; exactly six panels; 2x3 grid; preserve reference identity; protagonist must wear black collared top with gray zipper/placket; cat must be black-and-white tuxedo; all panel borders, bubbles, faces, and important content inside generous safe margins.
Avoid: generic anime male, wrong hair, wrong outfit, extra panels, missing panel borders, cluttered text, pseudo text, watermarks, logos, cropped elements, tiny bubbles, edge-to-edge important content, cute upbeat tone, exaggerated laughing expression.
```

Final overlaid Traditional Chinese text:

```text
Panel 1: 我今天／故意沒帶傘。
Panel 2: 不是失誤，／是風險移轉。
Panel 3: 帶傘，責任在我；／不帶，責任在天氣。
Panel 4: 你只是懶。
Panel 5: 沒帶傘，才能讓天氣／對我的人生負責。
Panel 6: Silent, no text.
```

Post-processing:
- Fit the generated source image onto a 1080x1350 canvas without cropping.
- Render exact Traditional Chinese dialogue locally using the system CJK font.
- Keep all text inside existing speech bubbles and preserve the silent panel 6 aftertaste.
