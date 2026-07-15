# 2026-07-15_1200 Generation Prompt

Topic: 外送追蹤供應鏈治理

Output:
- `assets/2026-07-15_1200_deadpan_joke.png`

Reference image:
- `assets/main_character_reference.jpg`
- Mandatory likeness: East Asian man, round youthful face, side-swept black hair, slightly sleepy calm eyes, black collared top with gray zipper/placket.

Final panel text:
1. 「我不是在／等外送。」
2. 「這叫供應鏈／能見度管理。」
3. 「你刷新／第十次了。」
4. 「資訊不流動，／我就幫它流動。」
5. 「不是肚子餓，／是需求正在／接受配送治理。」
6. Silent awkward aftertaste, no dialogue.

Image generation prompt:

```text
Use case: illustration-story
Asset type: Instagram feed six-panel comic for @roberto_joke, final target 1080x1350 pixels, 4:5 portrait.

Input image role: The attached reference photo / assets/main_character_reference.jpg is the mandatory likeness reference for the male protagonist. Preserve this identity in stylized colorful manga/comic form: East Asian man, round youthful face, side-swept black hair, slightly sleepy calm eyes, soft youthful facial features, wearing a black collared top with a gray zipper/placket. Do not make him a generic anime man.

Create exactly one colorful six-panel comic image in a clean 2-column x 3-row grid. Portrait 4:5 composition with generous inner safe margin; all panel borders, faces, blank speech bubbles, and important art must stay inside the safe area. Thick clean panel borders, IG-friendly readable composition, colorful Taiwanese webcomic / manga style, dry deadpan internet humor mood.

IMPORTANT TEXT INSTRUCTIONS: Leave all speech bubbles and small signs completely blank, with no lettering, no pseudo-text, no captions, no watermark. Blank white speech bubbles should be large and clean, safely inside each panel, not touching panel edges. No readable text anywhere in the image.

Characters: male protagonist based closely on the reference photo, deadpan serious expression throughout, wearing black collared top with gray zipper/placket. Include one black-and-white tuxedo cat in panels 3 and 6 only, cold unimpressed expression, not cute or playful.

Theme: delivery app tracking treated as a formal supply-chain visibility and governance system, while the protagonist is obviously just hungry and obsessively refreshing the app.

Panel 1: night office desk, protagonist holds a smartphone showing an abstract delivery-map interface with no readable words, very serious as if chairing a meeting, laptop and desk lamp in background, one blank speech bubble.
Panel 2: close-up of smartphone beside sticky notes and a simple flowchart made of icons only, protagonist points at the screen like a consultant explaining a supply chain workflow, one blank speech bubble.
Panel 3: tuxedo cat sits on desk staring skeptically at the protagonist while he refreshes the phone again, one blank cat speech bubble.
Panel 4: protagonist presents a whiteboard with simple icons only: scooter, food bag, arrows, clock, warning triangle, no readable words. One blank speech bubble.
Panel 5: main punchline panel, protagonist faces viewer with total seriousness, holding the phone like an official report; larger blank speech bubble, emphatic deadpan staging.
Panel 6: silent awkward aftertaste, no speech bubble if possible: protagonist and tuxedo cat sit in quiet office staring at the phone on the desk; the delivery icon on phone is still motionless, awkward empty pause.

Style constraints: colorful clean digital comic, crisp ink lines, balanced warm desk light and cool monitor glow, expressive but restrained faces. Keep all six panels clear and separate. 1080x1350 portrait ratio. No Instagram UI, no extra captions outside panels, no English dialogue, no readable text anywhere, no secrets, no tokens, no access keys.
```

Post-processing:
- Built-in image generation produced a 1122x1402 source image.
- Resized generated art to exactly `1080x1350`.
- Added Traditional Chinese dialogue locally with STHeiti CJK font rendering.
- Left panel 6 silent.
