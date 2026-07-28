# 2026-07-28 20:30 Generation Prompt Record

## Context and de-duplication

- Read the current Taiwan Google Trends context. `costco` could support an everyday joke, but shopping carts, shopping desire, refrigerators, and stockpiling are already present in older posts or recent candidate records, so the trend was not forced.
- Political/public-figure and unclear news trends were excluded. The final is an original summer household joke.
- Read `analytics/latest.json` and `analytics/daily_strategy.md`. Recent shares are 0, so the concept targets one highly recognizable friend: the person who refuses to kill mosquitoes and becomes everyone else's mosquito problem.
- Compared the latest 20 post manifests, captions, and prompt records. Avoided recent toilet, social isolation, alarm clock, decluttering, reading menus, weight, clothes chair, luggage, fandom, receipts, walking, leaks, sunscreen, weather, instant noodles, and hiding-from-problems topics.
- Final mechanism: the protagonist claims moral superiority; the cat supplies a hidden customer-review consequence and downgrades him from compassionate human to an all-you-can-eat restaurant. This differs from the recent third-party nickname, institution-personification, and rejected-by-an-object mechanisms.

## 12 candidates and scores

Scores are Surprise / Visual contradiction / Cat-roast sharpness / Shareability.

| # | Setting | Setup | Punchline | Score | Decision |
|---|---|---|---|---:|---|
| 1 | Mosquito release, non-work | 我對生命都很尊重 | 貓：蚊子評你五星吃到飽 | 5/5/5/5 = 20 | Finalist; specific hidden consequence and instant identity downgrade |
| 2 | Bad parking, non-work | 我停車都替別人著想 | 貓：整條巷子都在替你祈禱 | 4/5/4/5 = 18 | Finalist; relatable, but roast is less specific |
| 3 | Buffet, non-work | 我吃到飽很重視回本 | 貓：老闆在門口幫你募款 | 5/4/5/5 = 19 | Finalist; strong consequence, but food/weight appeared recently |
| 4 | Camping, non-work | 我露營講究融入自然 | 貓：營區熊把你當廚餘了 | 5/5/5/4 = 19 | Finalist; vivid, but a Taiwan everyday share target is narrower |
| 5 | Karaoke, non-work | 我唱歌很會帶動氣氛 | 貓：隔壁包廂已經報警求安靜 | 4/4/5/5 = 18 | Finalist; shareable, but depends on a readable secondary room |
| 6 | Laundry, non-work | 我洗衣服都讓它自然乾 | 貓：氣象局拿你家當雨量站 | 4/4/4/4 = 16 | Qualified; weather-station metaphor needs an extra beat |
| 7 | Movie theater, non-work | 我看電影很尊重劇情 | 貓：你打呼把反派洗白了 | 5/4/5/4 = 18 | Qualified; visual sleep gag is too close to the recent alarm post |
| 8 | Night market, non-work | 我逛夜市很有自制力 | 貓：攤販都認得你的分期付款 | 4/4/4/5 = 17 | Qualified; less immediate central contradiction |
| 9 | Haircut, non-work | 我很信任設計師的判斷 | 貓：他剛剛把你封鎖了 | 4/5/4/5 = 18 | Qualified; punchline repeats a familiar social-rejection family |
| 10 | Recycling, non-work | 我垃圾分類做得很徹底 | 貓：資源回收車叫你本人上車 | 4/5/5/4 = 18 | Qualified; too close to the recent garbage-truck rejection |
| 11 | Family group photo, non-work | 我拍照都讓大家站舒服 | 貓：你把阿嬤裁成都市傳說了 | 5/4/5/5 = 19 | Qualified; requires a small phone screen to explain |
| 12 | Office presentation, workplace | 我簡報最重視現場互動 | 貓：投影機關掉後大家才鼓掌 | 4/4/4/4 = 16 | Qualified; workplace setting and presentation mechanism are less fresh |

Non-workplace candidates: #1–#11 (11 total).

## Top five review

1. **Mosquito release — 20/20, selected.** The release gesture, swollen bites, and delighted mosquito swarm create an immediate contradiction. The cat does not say that he is getting bitten; it reveals a specific off-screen review and recasts him as a five-star buffet. Short, blunt, summer-relevant, and highly sendable.
2. **Buffet — 19/20, rejected.** The owner fundraising for the customer is a strong consequence, but food and body-weight humor appeared in a very recent post.
3. **Camping — 19/20, rejected.** The bear/food-waste downgrade is sharp and visual, but the scenario is less universally everyday and introduces a third animal competing with the mandatory cat.
4. **Family group photo — 19/20, rejected.** “都市傳說” is a surprising downgrade, but the crop error would need a small phone image and weaken one-glance readability.
5. **Bad parking — 18/20, rejected.** The setting is relatable and visually absurd, but “替你祈禱” is broader and less concrete than the mosquito review.

## Final selection reason

Candidate #1 is the sole 20/20 idea. It creates a clean moral-image reversal without the banned `你只是` construction, does not literally narrate the release or bites, and adds the unexpected consequence that mosquitoes rate the protagonist as a restaurant. The cat is an active deadpan corrective presence with an electric swatter, not decoration. The scene, release pose, summer-home setting, and review-based roast differ from the latest 20 posts.

## Built-in image generation prompt

Use case: illustration-story  
Asset type: Instagram square single-panel meme  
Primary request: Create exactly one colorful 1:1 single-panel Taiwanese internet meme, polished realistic-comic style. Preserve the identity and facial likeness from the supplied reference photograph; do not make a generic anime character.  
Input image: `assets/main_character_reference.jpg` — mandatory identity/likeness reference for the male protagonist.  
Scene/backdrop: A Taiwanese apartment living room on a humid summer evening. An open window with warm city light. The protagonist solemnly and delicately releases one mosquito from a clear cup as though performing a noble wildlife rescue. His face and forearms have several obvious swollen mosquito bites. Behind him, a small delighted swarm is already flying in through the open window; keep the insects readable as mosquitoes but not grotesque. A black-and-white tuxedo cat sits prominently on a side table, deadpan and judgmental, one paw resting on an electric mosquito swatter like the competent adult in the room.  
Subject: East Asian man with a round youthful face, side-swept black hair, slightly sleepy eyes, wearing a black collared top with a gray zipper/placket matching the reference. Expression is solemnly proud with a tiny self-satisfied smile, caught in the act.  
Style/medium: Refined colorful realistic-comic meme illustration, expressive natural likeness, crisp ink texture, lively summer teal/orange palette, Taiwanese deadpan absurdity. Not anime.  
Composition/framing: Exactly three horizontal zones, not panels: top white band about 21%, one continuous central scene about 58%, bottom white band about 21%. All text, faces, cat, hands, mosquito cup, and swatter inside generous safe margins, with nothing important in the outermost 5%.  
Text (verbatim, Traditional Chinese only): Top white band: `我對生命都很尊重` Bottom white band: `貓：蚊子評你五星吃到飽`  
Typography: Exactly two main text lines total. Oversized rough hand-painted black Traditional Chinese lettering, centered, extremely legible on a phone, with generous padding. Each band contains its text on one line. Render every glyph exactly.  
Constraints: Exactly one image, one single scene, one protagonist, and one tuxedo cat. Square feed-safe composition. No speech bubbles, no extra captions, no readable secondary text, no logos, no brand marks, no watermark. The cat must look sharp, unimpressed, and visibly responsible for the bottom roast.  
Avoid: six panels, multiple panels, collage, generic anime man, neutral passport expression, cute-only cat, additional animals, horror insects, malformed hands, cropped text, simplified Chinese, misspelled Chinese, extra words.

Generation method: built-in image generation, one call only. The reference image is used solely as the mandatory likeness reference. The output is saved to `assets/2026-07-28_2030_deadpan_joke.png`.
