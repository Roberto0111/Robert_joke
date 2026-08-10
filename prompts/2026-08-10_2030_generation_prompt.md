# 2026-08-10 20:30 Generation Prompt Record

## Run constraints

- Content mode: `life_dialogue`
- Output: exactly two 1080×1350 PNG carousel pages, two stacked panels per page
- Character reference: `assets/main_character_reference.jpg` (mandatory likeness reference)
- Trend decision: no trend used. The available Taiwan trends were mostly finance, politics, public figures, or sensitive news and did not naturally support a grounded everyday-life question.
- Analytics decision: retain the two-page reveal and very short phone-readable dialogue. The life-dialogue sample is too small to justify topic imitation.
- Recent-20 comparison: avoided moving/renewing a lease, refusal/boundaries, profile photos, clothing, fitness equipment, gaming anger, cooking failure, KTV, fireworks/phone use, bathing, hiking, parcel shopping, convenience-store meals, mosquitoes, bathroom privacy, social exclusion, alarms, decluttering slogans, and reading/delivery-menu jokes.

## Brainstorm (R = relatability, N = natural dialogue, I = insight, S = save/share)

1. **Keeping a mistaken purchase** — “丟了像承認以前的我很笨” → “留下錯的東西，不會替以前的你變聰明。” R5 N5 I5 S5 = **20/20** (non-workplace)
2. **Rest feels wasted** — “一休息就覺得今天浪費了” → confusing motion with worth. R5 N5 I4 S5 = **19/20** (non-workplace)
3. **Waiting for friends to initiate** — silence is treated as an answer before the question is sent. R5 N5 I5 S4 = **19/20** (non-workplace)
4. **Saving the good clothes for later** — protecting clothes from life also prevents them from belonging to life. R4 N5 I5 S5 = **19/20** (non-workplace)
5. **Not opening a gifted item** — preserving gratitude turns the gift into an obligation. R4 N4 I5 S5 = **18/20** (non-workplace)
6. **Re-reading an old chat** — searching old words for a new answer. R5 N4 I4 S5 = **18/20** (non-workplace)
7. **Unable to choose a restaurant** — avoiding one small disappointment makes the whole evening disappear. R5 N5 I4 S4 = **18/20** (non-workplace)
8. **Keeping every photo** — fear that deleting evidence deletes the day. R4 N4 I4 S4 = **16/20** (non-workplace)
9. **Skipping a solo trip** — waiting for company quietly gives other people control of the calendar. R4 N4 I5 S4 = **17/20** (non-workplace)
10. **Not asking a neighbor to lower the volume** — paying for peace with several nights of sleep. R4 N5 I4 S4 = **17/20** (non-workplace)
11. **Avoiding a new task at work** — protecting a capable image prevents becoming capable at something new. R4 N4 I4 S4 = **16/20** (workplace)
12. **Not submitting an imperfect proposal** — no rejection also means no chance to be chosen. R4 N4 I4 S4 = **16/20** (workplace)

Non-workplace candidates: 10/12.

## Top five and rejection notes

1. **Keeping a mistaken purchase — 20/20 — SELECTED.** Most concrete prop-driven tension, highly natural admission, and the final line precisely separates accepting a past mistake from continuing to store it. It also supports a fresh setting, pose, and quiet visual action.
2. **Rest feels wasted — 19/20 — rejected.** Strong and relatable, but the productivity/self-worth mechanism is common social-media wisdom and risks sounding generic.
3. **Waiting for friends to initiate — 19/20 — rejected.** Strong reframe, but too close to the recent refusal/boundary preview and older social-exclusion setup.
4. **Saving the good clothes for later — 19/20 — rejected.** Memorable, but visually adjacent to the recent clothing post.
5. **Not opening a gifted item — 18/20 — rejected.** Insightful, but requires more backstory to make the gift and obligation legible in one short line.

## Selected four dialogue beats (verbatim)

1. `這些都用不到，但丟了好像很可惜。`
2. `貓：可惜的是錢，還是承認買錯？`
3. `承認買錯，就像以前的我很笨。`
4. `貓：留下錯的東西，不會替以前的你變聰明。`

## Image-generation spec

Use case: `illustration-story`

Asset type: one Instagram carousel story split across two portrait pages; each page contains exactly two equal stacked comic panels.

Input image: `assets/main_character_reference.jpg` is a mandatory likeness reference, not an edit target. Preserve the subject’s recognizable East Asian identity: round youthful face, side-swept black hair, slightly sleepy eyes, and black collared top with gray zipper/placket.

Continuity bible: original polished realistic Taiwanese webcomic; refined dark linework; expressive but restrained acting; warm teal, amber, muted coral, and cream palette; a small Taiwanese apartment storage room at night; same shelves, cardboard boxes, lamp, character proportions, wardrobe, facial identity, tuxedo-cat markings, rendering, line weight, and lighting across both pages.

Page 1 composition: 1080×1350 portrait, exactly two stacked panels separated by one thick black horizontal divider. Panel 1: medium-wide view, Roberto sits on the floor before an open storage shelf, hugging an unused appliance box and looking conflicted; tuxedo cat watches from a box at lower right. Panel 2: closer two-shot from a slightly lower angle; cat sits upright, calm and incisive, Roberto glances sideways while still holding the box. Leave a clean cream dialogue band at the top of each panel, generous safe margins, no text in the generated art.

Page 2 composition: same room and continuity. Panel 3: Roberto seated against the shelf, shoulders lowered, honestly admitting the fear while looking at the unused object; cat listens quietly. Panel 4: widest, calm final beat; Roberto places one unused item into a donation carton, expression thoughtful rather than triumphant; cat sits beside the carton with an even, perceptive gaze. Leave a clean cream dialogue band at the top of each panel, generous safe margins, no text in the generated art.

Typography production: add exactly one large bold Traditional Chinese dialogue line to each panel in the reserved cream band, fully within safe margins and never overlapping a face. No other text.

Avoid: generic anime face, chibi style, photorealism, a different male identity, wardrobe changes, cat color changes, extra panels, inset panels, speech balloons, captions generated inside the art, watermarks, logos, Instagram UI, clutter over the dialogue bands, exaggerated slapstick, motivational-poster styling.

## Production note

- Artwork generated with the built-in image-generation tool in two continuity-linked calls.
- Exact Traditional Chinese typography was added in the reserved cream bands during local production to guarantee spelling, safe margins, and phone readability.
- Final visual QA confirmed exactly two stacked panels per image, four total dialogue beats, both required characters on both pages, consistent identity/wardrobe/palette, and a visually distinct panel-four resolution.
