# 2026-07-31 20:30 Generation Prompt

## Inputs and strategy

- Mandatory likeness reference: `assets/main_character_reference.jpg` (reference image only; preserve identity, clothing cues, and facial structure).
- Trend context considered: 「登山杖」可自然連到登山裝備；其餘趨勢不是敏感、就是與日常笑點連結偏弱。最終笑話不需要讀者知道趨勢也能成立。
- Analytics evidence: Reel reach is much higher than static-image reach; this square remains a strong, instantly readable Reel source. The best recent mechanism used a concrete third-party consequence, so reuse that structural strength without copying its topic or wording.
- Recent-20 comparison: avoid online shopping, boxed meals, mosquitoes, bathroom occupation, social exclusion, alarm clocks, decluttering, delivery menus, dieting, clothes piles, airports, concerts, receipts, step counts, leaks, sun avoidance, and heat. Final uses a mountain trail, a reckless ready-to-go pose, and the cat's skeptical side-eye.

## Twelve distinct candidates and scoring

Scores are Surprise / Visual contradiction / Cat-roast sharpness / Shareability (total out of 20).

1. **登山（非職場）** — 上：「爬山我都靠自己」／下：「貓：搜救隊也是自己人？」 — **5/5/5/4 = 19**. Strong specific consequence; the slippers and bubble tea contradict the solemn confidence without making the roast merely narrate them.
2. **手機充電（非職場）** — 上：「我很會控制手機用量」／下：「貓：行動電源有三班制。」 — **4/5/5/4 = 18**. Great prop gag and concrete downgrade; rejected because device-dependence is slightly less fresh visually.
3. **追劇（非職場）** — 上：「我看劇從來不拖進度」／下：「貓：片尾名單都認得你了。」 — **4/4/5/4 = 17**. Specific personification and binge-watch shareability; rejected because a sofa-screen scene is less immediate than the mountain setup.
4. **洗車（非職場）** — 上：「我很重視車子的清潔」／下：「貓：下雨天被你當員工了。」 — **4/4/4/4 = 16**. Reframes free rain as labor; rejected because the central contradiction needs weather context and reads slower.
5. **健身房（非職場）** — 上：「我去健身房都很自律」／下：「貓：冷氣已記住你的體溫。」 — **4/5/4/3 = 16**. Visual of sitting under AC while holding one dumbbell is clear; rejected because gym laziness is familiar.
6. **做菜（非職場）** — 上：「我最近都自己開伙」／下：「貓：瓦斯公司以為你在煉鋼。」 — **3/5/4/4 = 16**. Large flame gives a strong image; rejected because it leans on exaggeration more than a true reframe.
7. **排隊（非職場）** — 上：「我排隊最有耐心」／下：「貓：前面的人已經二訪了。」 — **4/3/4/3 = 14**. Rejected: timing logic is clever but requires explanation and the visual is weak.
8. **垃圾分類（非職場）** — 上：「我分類做得很徹底」／下：「貓：垃圾車叫你一起上車。」 — **3/4/4/3 = 14**. Rejected: overlaps the recent garbage-truck/decluttering topic.
9. **電影院（非職場）** — 上：「我看電影最守規矩」／下：「貓：你爆雷比字幕快。」 — **4/3/4/4 = 15**. Valid but rejected: the roast is verbal, not strongly supported by a single still image.
10. **曬衣服（非職場）** — 上：「我很會看天氣洗衣服」／下：「貓：氣象局正在跟你道歉。」 — **3/4/3/3 = 13**. Rejected: generic weather bad luck and no sharp downgrade.
11. **會議（職場）** — 上：「我開會都直奔重點」／下：「貓：午餐店先打烊了。」 — **3/4/4/3 = 14**. Rejected: workplace meeting overrun is overused and close to corporate-jargon territory.
12. **遠端工作（職場）** — 上：「我在家工作更有效率」／下：「貓：床已升任直屬主管。」 — **4/5/4/3 = 16**. Good contradiction, but rejected because sleeping-while-discussing-efficiency is a familiar series mechanism.

## Final selection

Candidate 1 wins at **19/20**. It is non-workplace, naturally echoes a current benign search trend, gives an instantly legible contradiction, and makes the reader infer a reckless hiking friend. The cat's question changes 「靠自己」 into dependence on a specific emergency service; it does not restate the slippers or drink. It also varies setting (outdoor trail), pose (confidently pointing uphill), and cat reaction (fully equipped, skeptical side-eye) from the latest posts.

## Final built-in image generation prompt

Use case: illustration-story
Asset type: exactly one Instagram single-panel square meme
Primary request: Create one colorful 1080x1080 polished realistic-comic Taiwanese internet meme. Preserve the identity of the man in the supplied reference photo; he must clearly be the same East Asian man with a youthful round face, side-swept black hair, slightly sleepy eyes, and a black collared top with gray zipper/placket. Do not make him a generic anime character.
Input image: `assets/main_character_reference.jpg` — mandatory likeness reference only, not an edit target.
Scene/backdrop: A bright Taiwanese mountain trailhead with a steep stone stair trail rising dramatically behind him, lush subtropical greenery, trail signs, warm daylight. No brands or logos.
Subject/action: The protagonist stands at the very start of the steep trail, solemn and overconfident, pointing uphill like an expedition leader. His visible absurd preparation: indoor flip-flops, one large hand-shaken drink, tiny crossbody pouch, no backpack, no water, no hiking pole. He wears his reference black collared top with gray zipper/placket. Beside him is one black-and-white tuxedo cat in tiny serious full hiking gear with a miniature backpack and trekking pole, giving him a razor-sharp skeptical side-eye. The cat must be prominent, deadpan, and readable as the roast character.
Style/medium: polished colorful realistic-comic illustration, expressive but identity-faithful, Taiwanese meme energy, absurd yet visually coherent, crisp details, strong subject separation.
Composition/framing: strict single panel, no split panels, no collage. White headline band across the top, central scene in the middle, white punchline band across the bottom. Generous 8% safe margins. Keep faces, cat, and all text fully inside the square. The middle scene must remain large and uncluttered.
Text (verbatim, Traditional Chinese only): Top band: 「爬山我都靠自己」 Bottom band: 「貓：搜救隊也是自己人？」
Typography: exactly two main text lines total; oversized rough hand-drawn black Traditional Chinese lettering, high contrast, centered, immediately readable on a phone. Render every character exactly. No speech bubbles, no labels, no extra writing.
Mood: protagonist is solemn with a tiny guilty/mischievous raised eyebrow; cat is unimpressed and judgmental.
Constraints: exactly one 1:1 image; one absurd central scene; white top and bottom bands; one male protagonist based on the reference; exactly one black-and-white tuxedo cat; no cropping; no watermark.
Avoid: six panels, multiple images, anime styling, generic face, extra people, extra cats, speech bubbles, explanatory text, Simplified Chinese, garbled glyphs, cut-off words, logos, dangerous injury imagery, rescue workers shown in the scene.

