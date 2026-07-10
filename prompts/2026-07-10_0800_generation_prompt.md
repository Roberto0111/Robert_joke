# 2026-07-10_0800 Generation Prompt

Topic: 搜尋流程當作責任預熱

Output: assets/2026-07-10_0800_deadpan_joke.png

Reference image: assets/main_character_reference.jpg is the mandatory likeness reference for the male protagonist. Preserve the identity in stylized manga/comic form: East Asian man, round youthful face, side-swept black hair, slightly sleepy calm eyes, wearing a black collared top with gray zipper/placket. Do not make him a generic anime man.

Comic requirements:
- Exactly one colorful six-panel comic, 2 columns x 3 rows.
- Final canvas must be 1080x1350 pixels, 4:5 portrait ratio.
- Keep all panel borders, speech bubbles, faces, and Traditional Chinese text inside a generous Instagram-safe inner margin.
- Style: 認真講幹話, dry Taiwanese internet humor, colorful clean manga/comic, deadpan expressions.
- If a cat appears, it must be a black-and-white tuxedo cat.
- Do not post to Instagram. Do not run git push. Do not print secrets.

Final panel text:
1. 「我不是在／查資料。」
2. 「我是讓問題／先進入／搜尋流程。」
3. 「所以你有／開始做嗎？」
4. 「知識要先／被治理，／才可以被忽略。」
5. 「不是不會做，／是把責任交給／搜尋框先熱身。」
6. Silent awkward aftertaste, no dialogue.

Image generation prompt:

```text
Use case: illustration-story
Asset type: Instagram feed six-panel comic for @roberto_joke, final target 1080x1350 pixels, 4:5 portrait.

Input image role: Image #1 / assets/main_character_reference.jpg is the mandatory likeness reference for the male protagonist. Preserve identity in stylized colorful manga/comic form: East Asian man, round youthful face, side-swept black hair, slightly sleepy calm eyes, soft facial features, wearing a black collared top with a gray zipper/placket. Do not make him a generic anime man.

Create exactly one colorful six-panel comic image in a clean 2-column x 3-row grid. Portrait 4:5 composition with generous inner safe margin; all panel borders, faces, blank speech bubbles, and important art must stay inside the safe area. Thick clean panel borders, IG-friendly composition, colorful Taiwanese webcomic / manga style, dry deadpan internet humor mood.

IMPORTANT TEXT INSTRUCTIONS: Leave all speech bubbles and small signs completely blank, with no lettering, no pseudo-text, no captions, no watermark. I will add Traditional Chinese text later. Blank white speech bubbles should be large and clean, safely inside each panel, not touching panel edges.

Characters: male protagonist based closely on the reference photo, deadpan serious expression throughout, wearing black collared top with gray zipper/placket. Include one black-and-white tuxedo cat in panels 3 and 6 only, cold unimpressed expression, not cute or playful.

Theme: using search tabs as a formal knowledge governance system, actually avoiding doing the task.
Panel 1: night office desk, protagonist sits at laptop with many search result tabs open, holding a pen like a consultant, very serious, one blank speech bubble.
Panel 2: close-up of laptop search bar and notes, protagonist points at the screen like presenting a process, one blank speech bubble.
Panel 3: tuxedo cat sits on desk beside the laptop, staring skeptically at the protagonist, one blank cat speech bubble.
Panel 4: protagonist presents a whiteboard with simple icons only: search magnifying glass, arrows, question mark, folder, no readable words. One blank speech bubble.
Panel 5: main punchline panel, protagonist faces viewer with total seriousness, holding the laptop like an official report; larger blank speech bubble, emphatic deadpan staging.
Panel 6: silent awkward aftertaste, no speech bubble if possible: protagonist and tuxedo cat sit in quiet office staring at a laptop with too many tabs; awkward empty pause.

Style constraints: colorful clean digital comic, crisp ink lines, balanced warm desk light and cool monitor glow, expressive but restrained faces. Keep all six panels clear and separate. No Instagram UI, no extra captions outside panels, no English dialogue, no readable text anywhere, no secrets/tokens/access keys.
```

Post-processing:
- The built-in image generator produced a 1122x1402 source image.
- The generated art was resized to exactly 1080x1350.
- Traditional Chinese dialogue was overlaid locally with macOS CJK font rendering.
- Panel 6 was left silent.
