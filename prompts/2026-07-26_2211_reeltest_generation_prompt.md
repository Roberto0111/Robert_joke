# 2026-07-26_2211_reeltest Generation Prompt

## Context review

- Read `README.md`, `prompts/daily_comic_style.md`, and `prompts/daily_posting_workflow.md`.
- Used `assets/main_character_reference.jpg` as the mandatory likeness reference.
- Reviewed `posts/2026-07-26_2211_reeltest/trend_context.txt`. The listed trends were either sensitive, ambiguous, or weaker than an original everyday joke, so none were forced into the concept.
- Reviewed `analytics/latest.json`. Recent reach was 1–3, shares and saves were 0, so no weak recent topic was repeated; the selection favors a joke that viewers can send to a socially absent friend.
- Compared the latest 20 post/caption records. Avoided recent mechanisms and settings involving alarms, decluttering, delivery menus, overeating, clothing piles, travel, concerts, receipts, step counts, leaks, sun avoidance, cooking disasters, and office-management jargon.

## Twelve candidates and scores

Scores are `surprise / visual contradiction / cat-roast sharpness / shareability = total`.

| # | Setting | Setup | Cat punchline | Score | Decision note |
|---|---|---|---|---|---|
| 1 | Hot-pot gathering (non-workplace) | 我最近學會享受獨處 | 貓：群組已經另開一個了 | 5/5/5/4 = **19** | Selected: the unseen replacement group abruptly reframes his proud solitude as social demotion; the empty banquet creates an instant visual contradiction. |
| 2 | Karaoke room (non-workplace) | 我唱歌越來越有自信 | 貓：隔壁包廂剛續三小時 | 4/4/4/5 = **17** | Rejected: shareable, but the consequence depends on inferring that people fled next door and is slightly less immediate. |
| 3 | Convenience store (non-workplace) | 我買東西都先看成分 | 貓：餘額不夠看價格 | 4/4/5/4 = **17** | Rejected: sharp financial reframe, but the visual needs a readable payment failure and risks introducing a third text element. |
| 4 | Beach (non-workplace) | 我現在很懂得放空 | 貓：救生員以為你是漂流物 | 4/5/4/4 = **17** | Rejected: strong image, but it edges toward danger and the roast is more literal than the winner. |
| 5 | Cinema (non-workplace) | 我看電影很尊重安靜 | 貓：工作人員忘了這廳有人 | 4/4/4/4 = **16** | Rejected: clean hidden consequence, but less surprising and less personally sendable than the winner. |
| 6 | Family dinner (non-workplace) | 我最近很少跟人爭 | 貓：家族群已經把你靜音 | 4/3/4/4 = **15** | Rejected: the group-chat mechanism overlaps the winner but has a weaker central visual contradiction. |
| 7 | Parking lot (non-workplace) | 我停車越來越有耐心 | 貓：拖吊場都幫你留位了 | 4/4/4/3 = **15** | Rejected: specific consequence, but vehicle context is busier and less universal. |
| 8 | Laundromat (non-workplace) | 我很會延長衣服壽命 | 貓：洗衣店以為你失蹤了 | 3/4/3/3 = **13** | Rejected: too close to the recent clothing-life topic and therefore not novel enough. |
| 9 | Gym (non-workplace) | 我健身都重視恢復 | 貓：教練已經幫你辦告別式 | 4/5/4/3 = **16** | Rejected: vivid contradiction, but the death metaphor violates the sensitive-topic filter. |
| 10 | Train station (non-workplace) | 我旅行開始順其自然 | 貓：末班車也順便走了 | 3/4/4/3 = **14** | Rejected: pleasant wording but too close to the recent travel topic and not sharp enough. |
| 11 | Office presentation (workplace) | 我讓簡報自己說話 | 貓：同事叫它不要再聯絡 | 4/4/4/3 = **15** | Rejected: workplace setting and corporate-adjacent mechanism are overrepresented in the archive. |
| 12 | Remote meeting (workplace) | 我現在開會很會抓重點 | 貓：大家抓的是你沒穿褲子 | 3/5/3/4 = **15** | Rejected: obvious visual gag, but it resembles earlier video-meeting material and the roast mostly explains the image. |

Non-workplace candidates: 10 of 12.

## Top-five comparison and final selection

The top five were candidates 1, 2, 3, 4, and 5. Candidate 1 was the sole 19/20 concept. It varies the recent archive with a private hot-pot gathering, a centered toast pose, a crooked party hat, many empty place settings, and a cat seated as a disappointed guest. The punchline does not describe the empty seats; it adds a new off-screen fact—his friends created a replacement group—which downgrades his dignified “solitude” into being excluded. It is specific, readable in one glance, and naturally sendable to one absent friend.

## Final image-generation prompt

Use case: `illustration-story`.

Create exactly one colorful 1080×1080 Instagram single-panel meme. Use the mandatory reference image to preserve the protagonist’s recognizable identity: East Asian man, round youthful face, side-swept black hair, slightly sleepy eyes, wearing a black collared top with gray zipper/placket. Do not make him a generic anime man.

Use a top white band, one central scene, and a bottom white band. The only text is:

- Top, exact Traditional Chinese: `我最近學會享受獨處`
- Bottom, exact Traditional Chinese: `貓：群組已經另開一個了`

Both lines must be oversized rough hand-painted black Traditional Chinese, fully inside generous safe margins, with no speech bubbles or other text.

In the central polished realistic-comic scene, show the protagonist alone at the center of an absurdly long hot-pot restaurant table set for a lively gathering, with eight empty place settings. He wears a slightly crooked tiny party hat and solemnly raises a cup to all the empty chairs, with a faint guilty half-smile and one raised eyebrow. Include a small untouched party cake. Place a prominent black-and-white tuxedo cat upright on the adjacent chair, staring at him with narrowed, unimpressed eyes and one paw on a face-down phone. Warm Taiwanese hot-pot restaurant lighting; colorful, crisp, absurd, deadpan, and immediately legible.

Avoid multiple panels, split screens, extra people, generic anime styling, neutral expression, cute chibi cat, extra text, simplified Chinese, cropped typography, English, logos, and watermarks.

## Generation result

- Built-in ImageGen was used exactly once.
- The generated square was copied into the project and normalized to exactly 1080×1080 PNG.
- Final asset: `assets/2026-07-26_2211_reeltest_deadpan_joke.png`
