# 2026-07-09_1200 Generation Prompt

Topic: 晚上喝咖啡當作焦慮液態管理

Reference image:
- `assets/main_character_reference.jpg`
- Mandatory likeness: East Asian man, round youthful face, side-swept black hair, slightly sleepy calm eyes, black collared top with gray zipper/placket.

Final panel text:
1. 「我不是晚上／喝咖啡。」
2. 「這叫把精神／轉成可管理／液體。」
3. 「睡不著吧？」
4. 「睡意不能／消失，／只能轉移到／明天。」
5. 「不是提神，／是替焦慮做／液態管理。」
6. Silent awkward aftertaste.

Image generation prompt:

```text
Use case: illustration-story
Asset type: Instagram 4:5 six-panel comic, final output 1080x1350 pixels.
Input image role: Image #1 / assets/main_character_reference.jpg is the mandatory likeness reference for the male protagonist. Preserve identity in stylized colorful manga/comic form: East Asian man, round youthful face, side-swept black hair, slightly sleepy calm eyes, black collared top with a gray zipper/placket. Do not make him a generic anime man.

Create exactly one colorful six-panel comic image in a clean 2-column x 3-row grid. Portrait 4:5 composition with generous inner safe margin; all panel borders, faces, blank speech bubbles, and important art must stay inside the safe area. Thick clean panel borders, IG-friendly readable composition, colorful office-life comic style, dry deadpan Taiwanese internet humor mood.

IMPORTANT TEXT INSTRUCTIONS: Leave all speech bubbles and small signs completely blank, with no lettering, no pseudo-text, no captions, no watermark. I will add Traditional Chinese text later. Blank white speech bubbles should be large and clean, but not touching panel edges.

Characters: male protagonist based closely on the reference photo, deadpan serious expression throughout, wearing black collared top with gray zipper/placket. Include a black-and-white tuxedo cat in panels 3 and 6 only, cold deadpan stare, not cute or playful.

Theme: coffee at night as productivity theater / anxiety liquid management.
Panel 1: night office desk, protagonist holding a coffee cup like a meeting document, very serious, laptop and desk lamp in background, one blank speech bubble.
Panel 2: close-up of coffee cup beside charts and sticky notes, protagonist points at it like a consultant explaining a workflow, one blank speech bubble.
Panel 3: tuxedo cat sits on desk staring at him skeptically while protagonist calmly takes notes, one blank cat speech bubble.
Panel 4: protagonist presents a whiteboard with simple icons: coffee cup, battery, tiny warning triangle, no readable words. One blank speech bubble.
Panel 5: main punchline panel, protagonist faces viewer with total seriousness, holding coffee like an official report; larger blank speech bubble, dramatic but still deadpan.
Panel 6: silent awkward aftertaste, no speech bubble if possible: protagonist and tuxedo cat sit in quiet office staring at the coffee; the monitor glow, awkward pause, empty space for silence.

Style constraints: colorful manga/comic, clean ink lines, warm office light mixed with cool night window tones, expressive but restrained faces. Keep all six panels clear and separate. No Instagram UI, no extra captions outside panels, no English dialogue, no readable text anywhere, no secrets/tokens/access keys.
```

Post-processing:
- Resized generated art to exactly `1080x1350`.
- Added Traditional Chinese dialogue with native macOS CJK font rendering.
- Left panel 6 silent.
