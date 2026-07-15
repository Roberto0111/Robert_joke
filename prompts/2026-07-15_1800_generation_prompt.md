# 2026-07-15_1800 Generation Prompt

Topic: 履歷更新人才流失壓力測試

Output:
- `assets/2026-07-15_1800_deadpan_joke.png`

Reference image:
- `assets/main_character_reference.jpg`
- Mandatory likeness: East Asian man, round youthful face, side-swept black hair, slightly sleepy calm eyes, black collared top with gray zipper/placket.

Final panel text:
1. 「我不是在／更新履歷。」
2. 「這叫職涯／災備演練。」
3. 「你在公司／電腦開？」
4. 「風險要在／現場測。」
5. 「不是想離職，／是替公司做／人才流失壓力測試。」
6. Silent awkward aftertaste, no dialogue.

Image generation prompt:

```text
Use case: illustration-story
Asset type: Instagram feed six-panel comic for @roberto_joke, final target 1080x1350 pixels, 4:5 portrait.

Input image role: Image #1 / assets/main_character_reference.jpg is the mandatory likeness reference for the male protagonist. Preserve this person's identity in stylized colorful Taiwanese manga/comic form: East Asian man, round youthful face, side-swept black hair with the same volume and parting, slightly sleepy calm eyes, soft youthful facial features, wearing a black collared top with a gray zipper/placket. Do not make him a generic anime man.

Create exactly one colorful six-panel comic image in a clean 2-column x 3-row grid. Portrait 4:5 composition with generous inner safe margin. Keep all panel borders, faces, character bodies, future speech-bubble space, and important art at least 5% away from the outer edge. Thick clean black panel borders, IG-friendly readable composition, colorful Taiwanese webcomic / manga style, dry deadpan internet humor mood.

IMPORTANT TEXT INSTRUCTIONS: Create the artwork with absolutely no readable text, no letters, no numbers, no pseudo-text, no captions, no watermark, no UI words. Do not draw speech bubbles. Instead leave clean uncluttered negative space near the top or upper side of panels 1-5 where speech bubbles will be added later. Panel 6 should have no speech bubble space if possible, just an awkward silent pause.

Characters: male protagonist based closely on the reference photo, deadpan serious expression throughout, black collared top with gray zipper/placket. Include one black-and-white tuxedo cat in panels 3 and 6 only, cold unimpressed expression, not cute or playful.

Theme: updating a resume on a company computer framed as formal career disaster recovery and talent-loss stress testing. The protagonist acts like a serious consultant while obviously doing something awkward at work.

Panel 1: night office desk. Protagonist sits at laptop with a blank resume-like document layout made only of abstract boxes and lines, no readable words. He looks extremely serious, as if chairing a meeting. Leave clear blank space for a speech bubble.
Panel 2: protagonist stands beside a whiteboard with only icons and arrows: suitcase, shield, backup cloud, career path arrow, warning triangle. No letters or words. He points like a consultant explaining disaster recovery. Leave clear blank space for a speech bubble.
Panel 3: tuxedo cat sits on the desk staring skeptically at the protagonist. The laptop is open toward the cat, showing only abstract document blocks. Protagonist freezes with one hand on the trackpad. Leave clear blank space for a cat speech bubble.
Panel 4: close office cubicle view. Protagonist looks around carefully while holding a plain folder and a USB stick, testing the risk in the actual workplace. Background monitors show only icon shapes and colored rectangles, no words. Leave clear blank space for a speech bubble.
Panel 5: main punchline panel. Protagonist faces the viewer with total seriousness, holding the plain folder like an official report, dramatic office monitor glow, confident deadpan expression. Leave a large clean blank space for the biggest speech bubble.
Panel 6: silent awkward aftertaste. No speech bubble. Protagonist and tuxedo cat sit side by side at the desk staring silently at the laptop; an empty office hallway behind them, awkward pause, cool monitor glow.

Style constraints: colorful clean digital comic, crisp ink lines, expressive but restrained faces, balanced warm desk light and cool monitor glow, modern Taiwanese office interiors. Keep all six panels clear and separate. 1080x1350 portrait ratio, safe for Instagram feed with no cropping. No Instagram UI, no extra captions outside panels, no English dialogue, no readable text anywhere, no secrets, no tokens, no access keys.
```

Post-processing:
- Built-in image generation produced a 997x1577 source image.
- Scaled the generated art into an exact 1080x1350 canvas with generous safe margins and no cropping.
- Added Traditional Chinese dialogue locally with macOS AppKit font rendering.
- Left panel 6 silent.
