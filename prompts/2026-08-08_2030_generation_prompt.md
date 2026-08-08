# 2026-08-08 20:30 Generation Prompt Record

## Inputs reviewed

- `README.md`
- `prompts/daily_comic_style.md`
- `prompts/daily_posting_workflow.md`
- `posts/2026-08-08_2030/trend_context.txt`
- `analytics/latest.json`
- `analytics/daily_strategy.md`
- Latest 20 post folders/manifests and latest 20 captions
- Mandatory likeness reference: `assets/main_character_reference.jpg`

Trend decision: no trend used. The available safe trends (oil prices and domestic-travel subsidy) did not improve the joke naturally; politics, flooding, illness, defense, and other sensitive items were rejected.

Growth decision: retain the proven two-page delayed reveal and concise everyday setup, while changing the mechanism from recent third-party consequence roasts to a purpose-reversal. Optimize for a joke viewers can send to a friend with a notoriously bad profile photo.

## Brainstorm scores

Scores are Surprise / Visual contradiction / Cat-roast sharpness / Shareability = total. Workplace status is explicit; 11 of 12 are non-workplace.

1. **ID photo as dating profile picture** (non-workplace): 5 / 5 / 5 / 5 = **20**
   - Beats:「我交朋友最重視真誠。」／「真誠，就要從照片開始。」／「所以我用身分證照片當大頭貼。」／「貓：戶政拍你，是怕認錯人。」
2. **Carry an empty cup to “leave room” for bubble tea** (non-workplace): 4 / 5 / 4 / 5 = **18**
   - Cat reveals the shop weighed Roberto as packaging; rejected because the precise final wording felt less natural.
3. **Give every buffet dish a second chance** (non-workplace): 4 / 5 / 4 / 5 = **18**
   - Cat says the restaurant has started charging him by floor area; rejected because the overflowing-table consequence resembles recent excess/warehouse mechanisms.
4. **Use a refrigerator as one-person air-conditioning** (non-workplace): 4 / 5 / 4 / 4 = **17**
   - Cat says the refrigerator has listed him as a roommate; rejected because the roast mostly describes the visible action.
5. **Trust a hairstylist enough to request unrestricted freedom** (non-workplace): 4 / 5 / 4 / 4 = **17**
   - Cat reveals Roberto was used as an end-of-day experiment; rejected because it risks framing an identifiable service worker as malicious.
6. **Push a scooter to the gas station to save fuel before refueling** (non-workplace): 4 / 5 / 3 / 4 = **16**
   - Rejected: oil-price trend connection felt forced and the punchline depended on a traffic queue.
7. **Wear wet laundry outside to combine drying and commuting** (non-workplace): 4 / 5 / 3 / 4 = **16**
   - Rejected: cat reversal did not add a sufficiently new fact.
8. **Use an ID-style neutral face in every family photo for consistency** (non-workplace): 3 / 5 / 3 / 4 = **15**
   - Rejected: too close to candidate 1 and less socially recognizable.
9. **Reserve half the bed for clothes so they do not feel abandoned** (non-workplace): 3 / 5 / 3 / 4 = **15**
   - Rejected: repeats the old chair/clothes-home topic.
10. **Bring home dishes to a picnic so nature feels like a restaurant** (non-workplace): 3 / 4 / 3 / 4 = **14**
    - Rejected: below threshold and lacks a sharp purpose reversal.
11. **Attend an online meeting from directly outside the office** (workplace): 4 / 5 / 3 / 3 = **15**
    - Rejected: workplace premise and corporate-adjacent logic are too familiar.
12. **Photograph every supermarket price tag to shop rationally** (non-workplace): 3 / 4 / 3 / 4 = **14**
    - Rejected: below threshold; consequence becomes explanatory.

## Top five and selection

1. ID photo as dating profile picture — 20/20 — selected.
2. Empty cup for bubble tea — 18/20 — rejected: weaker and less natural final line.
3. Buffet second chances — 18/20 — rejected: mechanism overlaps recent excess jokes.
4. Refrigerator air-conditioning — 17/20 — rejected: roast describes the visible gag.
5. Unrestricted haircut — 17/20 — rejected: relies on blaming a service worker.

Selected because all four beats form one clean escalation, the phone portrait creates an immediate visual contradiction, and panel four reframes the institutional purpose of an ID photo rather than merely commenting on Roberto's lack of matches. It is specific, embarrassing, non-workplace, and easily shareable to one friend.

## Final dialogue (verbatim)

1. 我交朋友最重視真誠。
2. 真誠，就要從照片開始。
3. 所以我用身分證照片當大頭貼。
4. 貓：戶政拍你，是怕認錯人。

## Shared image-generation specification

Use case: illustration-story
Asset type: Instagram carousel, two 1080x1350 PNG pages, each containing exactly two equal stacked panels.
Input image: `assets/main_character_reference.jpg` is the mandatory identity/likeness reference only.
Primary request: Create one continuous four-panel deadpan Taiwanese webcomic across two pages. Page 1 contains panels 1-2; page 2 contains panels 3-4.
Subject: Roberto is the same youthful East Asian man as the reference: recognizable round face, side-swept black hair, slightly sleepy eyes, black collared top with gray zipper/placket. A black-and-white tuxedo cat appears on both pages as his skeptical dialogue partner.
Setting: Same cozy modern Taipei apartment living room at night on both pages; muted teal walls, warm amber lamp, coral and mustard accents, dark blue-gray furnishings.
Style: Original polished realistic-comic meme illustration, expressive but restrained acting, clean confident ink line, colorful editorial shading, not generic anime.
Layout: Clear thick black horizontal divider; generous 80px outer safe margins; one large Traditional Chinese line in a high-contrast cream speech/caption box near the upper-left of each panel; never overlap faces; no extra text.
Continuity: Lock face, hair, wardrobe, cat markings, room layout, palette, rendering, and line weight across both pages.
Avoid: extra panels, extra dialogue, small print, Simplified Chinese, misspellings, cropped text, watermark, logo, Instagram UI, photorealism, generic anime face.

### Page 1 prompt

Panel 1: Medium shot. Roberto sits upright on the sofa, one hand respectfully over his chest, serious and sincere. Tuxedo cat sits on the sofa arm watching him sideways. Exact text:「我交朋友最重視真誠。」

Panel 2: Slightly closer continuity shot. Roberto raises one index finger like presenting an important principle; cat remains skeptical. A phone lies face-down on the coffee table, foreshadowing only. Exact text:「真誠，就要從照片開始。」

### Page 2 prompt

Panel 3: Same room and wardrobe. Roberto confidently holds up his phone beside his face. The phone clearly shows a deliberately unflattering ID-style headshot of the same Roberto: flat expression, plain pale background, severe official framing; an unmistakable generic dating/profile screen with zero readable interface words or numbers. Cat stares at the phone in disbelief. Exact text:「所以我用身分證照片當大頭貼。」

Panel 4: Strongest beat. Cat is foregrounded with half-lidded, devastatingly blunt expression, one paw resting on the phone; Roberto is behind it, suddenly embarrassed, shoulders tucked and avoiding eye contact. Preserve the same room. Exact text:「貓：戶政拍你，是怕認錯人。」

