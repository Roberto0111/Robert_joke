# 2026-08-06 20:30 Generation Prompt Record

## Context and selection rules

- Format: exactly one 1080×1080 single-panel Instagram meme.
- Mandatory likeness reference: `assets/main_character_reference.jpg`.
- Trend decision: no trend used. Most supplied trends involved public figures, politics, allegations, industrial news, or potentially sensitive weather/disaster context; forcing them would weaken an everyday joke.
- Growth evidence: recent reach favors Reel delivery, but this run produces the required square source image. The best recent structure used a respectable self-description followed by a specific hidden victim/consequence. Reused the pacing only, not its topic or wording.
- Latest-post comparison: avoided the recent game/Wi-Fi, cooking, KTV, fireworks, showering, hiking, online shopping, lunchbox, mosquito, bathroom, solitude, alarm, decluttering, reading, and overeating topics. The selected exercise/living-room setting, sprawled pose, object-personification reversal, and evidence-presenting cat reaction are distinct.

## All 12 candidates and scoring

Scores are Surprise / Visual contradiction / Cat-roast sharpness / Shareability (0–5 each).

1. **Exercise / sofa** — Setup:「我每天都有練核心」 Punchline:「貓：沙發先練出腹肌了。」 — **5/5/5/4 = 19**
2. **Laundry / wardrobe** — Setup:「我很會整理衣服」 Punchline:「貓：洗衣機以為自己是衣櫃。」 — **4/5/4/5 = 18**
3. **Parking / tow yard** — Setup:「我停車很有方向感」 Punchline:「貓：拖吊場都幫你留位了。」 — **4/4/5/4 = 17**
4. **Plant care / inheritance** — Setup:「我很會照顧植物」 Punchline:「貓：花盆開始辦繼承了。」 — **5/4/4/4 = 17**
5. **Travel packing / moving house** — Setup:「我旅行都輕裝上路」 Punchline:「貓：航空公司以為你搬家。」 — **4/5/4/4 = 17**
6. **Dating / punctuality** — Setup:「我約會從不讓人等」 Punchline:「貓：因為對方沒答應。」 — **5/3/5/4 = 17**
7. **Air-conditioning / summer** — Setup:「我很能適應夏天」 Punchline:「貓：台電把你列成景點。」 — **4/4/4/4 = 16**
8. **Photography / memories** — Setup:「我很會記錄生活」 Punchline:「貓：你的鏡頭只認得午餐。」 — **3/4/4/4 = 15**
9. **Movie night / spoilers** — Setup:「我看電影很尊重別人」 Punchline:「貓：片頭你就公布兇手。」 — **3/4/4/4 = 15**
10. **Office / meeting preparation** — Setup:「我開會前準備充分」 Punchline:「貓：你連請假理由都做簡報。」 — **3/4/4/3 = 14**
11. **Office / inbox** — Setup:「我每天都有清信箱」 Punchline:「貓：垃圾桶比主管早收到。」 — **3/3/3/3 = 12**
12. **Office / desk organization** — Setup:「我桌面一直很乾淨」 Punchline:「貓：因為文件都在地上。」 — **2/4/2/3 = 11**

Non-workplace candidates: 1–9 (9 total). Workplace candidates: 10–12 (3 total).

## Top five review and rejection notes

1. **Exercise / sofa — 19/20 — selected.** The punchline transfers the claimed fitness result to the sofa, sharply reframing the setup. The sofa becomes the specific victim and the six cushion dents make an absurd one-glance contradiction. Highly taggable without echoing a recent topic.
2. **Laundry / wardrobe — 18/20 — rejected.** Very relatable and visual, but the washing-machine-as-wardrobe joke is more familiar and the cat's line is slightly more descriptive than transformative.
3. **Parking / tow yard — 17/20 — rejected.** Specific consequence and good roast, but traffic-adjacent material sits too close to the supplied「交通違規」trend and could feel like a forced current-event reference.
4. **Plant care / inheritance — 17/20 — rejected.** Strong surprise and personification, but dead plants can make the center scene visually busier and less immediate than the sofa silhouette.
5. **Travel packing / moving house — 17/20 — rejected.** Clear physical contradiction, but luggage quantity needs several props and risks reducing phone-size readability.

## Final image-generation prompt

Use case: `illustration-story`.

Create exactly one colorful square single-panel Instagram meme in a polished realistic-comic Taiwanese internet-meme style. Use the supplied reference image as the mandatory identity reference, not an edit target. Preserve the East Asian male protagonist's youthful round face, side-swept black hair, slightly sleepy eyes, and black collared top with gray zipper/placket; do not make him a generic anime character.

Fixed layout: a top white band with oversized rough black Traditional Chinese text rendered verbatim as「我每天都有練核心」; one central living-room scene; a bottom white band with oversized rough black Traditional Chinese text rendered verbatim as「貓：沙發先練出腹肌了。」 Keep both lines centered and fully inside generous safe margins. No other text and no speech bubbles.

Central scene: the protagonist sprawls deeply and solemnly on a sofa, holding a TV remote like a fitness coach and looking self-satisfied. Six rounded cushion dents/bulges resemble abdominal muscles, as if the sofa developed a six-pack from carrying him. A pristine unused exercise mat sits nearby, while an ab roller supports a snack tray. Include exactly one black-and-white tuxedo cat with narrowed deadpan eyes, pointing one paw at the sofa's six-pack as evidence. Warm colorful living-room lighting; serious visual treatment of stupid behavior.

Avoid: extra panels, collage, extra people or cats, cute cheerful cat, extra writing, malformed/cropped text, watermark, logo, UI, brand marks, generic anime styling, and any content outside the two required lines.

## Output handling

- Generated with the built-in image-generation tool using the mandatory likeness reference.
- The square result is resized without cropping to exactly 1080×1080 and saved as `assets/2026-08-06_2030_deadpan_joke.png`.
