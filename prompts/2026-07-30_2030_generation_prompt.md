# 2026-07-30 20:30 Generation Prompt Record

## Context decision

- Trend context reviewed: 婦產科醫生、Taiwan news、七堵、分析師、日月光、SK 海力士、高市早苗、DAZN、涮乃葉、柯富仁。
- Most items were sensitive news, people, or niche searches. 「涮乃葉」 could support a food joke, but forcing a single-brand reference would narrow shareability, so this run uses an original everyday premise.
- Analytics reviewed: the strongest recent structure was a respectable self-description reversed by a concrete consequence involving a third party. Reach, shares, saves, and total interactions were treated as evidence; no prior caption was copied.
- Latest 20 post manifests/captions were checked. The final topic, parcel-filled apartment scene, seated pose, warehouse consequence, and cat reaction do not repeat their recent mechanisms or settings.

## Twelve candidates and scoring

Scores are **surprise / visual contradiction / cat-roast sharpness / shareability = total**. Candidates 1–10 are non-workplace; 11–12 are workplace.

1. 「我買東西都很有計畫。」／「貓：管理室已經加開倉庫。」— **5 / 5 / 5 / 5 = 20**
2. 「我洗澡都很節省時間。」／「貓：熱水器以為你失蹤了。」— **4 / 5 / 4 / 5 = 18**
3. 「我很懂得保養手機。」／「貓：插座已經是你監護人了。」— **4 / 5 / 5 / 4 = 18**
4. 「我最近作息很規律。」／「貓：太陽每天幫你關燈。」— **5 / 4 / 4 / 4 = 17**
5. 「我對料理很有耐心。」／「貓：泡麵都等到過熟了。」— **4 / 5 / 4 / 4 = 17**
6. 「我出門都會做好準備。」／「貓：公車司機已經下班了。」— **4 / 4 / 4 / 4 = 16**
7. 「我最近很常親近自然。」／「貓：陽台盆栽已經報警了。」— **4 / 4 / 4 / 4 = 16**
8. 「我看劇很懂得節制。」／「貓：片尾字幕都認得你了。」— **3 / 4 / 4 / 4 = 15**
9. 「我很會安排冰箱空間。」／「貓：醬料已經取得永久居留。」— **4 / 4 / 4 / 3 = 15**
10. 「我停車一向很有原則。」／「貓：拖吊場幫你留月租位了。」— **4 / 4 / 5 / 3 = 16**
11. 「我開會很重視傾聽。」／「貓：你的麥克風已經長眠了。」— **3 / 4 / 4 / 3 = 14**
12. 「我今天把工作都排好了。」／「貓：明天已申請禁止接近。」— **4 / 4 / 4 / 3 = 15**

## Top five review

1. **網購計畫，20/20**  
   Setup: 「我買東西都很有計畫。」  
   Punchline: 「貓：管理室已經加開倉庫。」  
   Rejection note: **Selected, not rejected.** The cat reveals a new, specific third-party consequence; the parcel fortress makes the contradiction readable before the punchline lands.
2. **省時洗澡，18/20**  
   Setup: 「我洗澡都很節省時間。」  
   Punchline: 「貓：熱水器以為你失蹤了。」  
   Rejection note: Strong personification, but an empty/dry bathroom makes the protagonist’s behavior less visually active.
3. **手機保養，18/20**  
   Setup: 「我很懂得保養手機。」  
   Punchline: 「貓：插座已經是你監護人了。」  
   Rejection note: Sharp downgrade, but the visual of sitting beside a charger is too ordinary and weaker at one-glance contradiction.
4. **規律作息，17/20**  
   Setup: 「我最近作息很規律。」  
   Punchline: 「貓：太陽每天幫你關燈。」  
   Rejection note: Elegant reversal, but sleeping/late-rising territory is too close to the recent alarm-clock post.
5. **料理耐心，17/20**  
   Setup: 「我對料理很有耐心。」  
   Punchline: 「貓：泡麵都等到過熟了。」  
   Rejection note: Immediate visual, but recent posts already used food and instant-noodle mechanisms, reducing novelty.

## Final selection reason

Candidate 1 is the only 20/20. It has a familiar friend-tagging behavior, a visually absurd parcel fortress, and a cat roast that does not narrate the image: 「管理室加開倉庫」 reveals an unseen consequence and upgrades the scale of the protagonist’s denial. The mechanism and setting differ from the latest 20 posts.

## Final image-generation prompt

Use case: illustration-story  
Asset type: one Instagram single-panel meme, exactly one image  
Input image: `assets/main_character_reference.jpg` is the mandatory identity/likeness reference for the male protagonist, not an edit target.

Create a polished colorful realistic-comic Taiwanese internet meme in an exact 1:1 square composition. Use the fixed three-zone layout only:

1. Top white band, about 18% of the canvas. Center one single line of oversized rough hand-painted black Traditional Chinese text, verbatim: **「我買東西都很有計畫」**. Keep every character correct, bold, immediately readable on a phone, and fully inside a generous 7% safe margin.
2. One continuous absurd central scene, about 64% of the canvas, no panels: inside a small Taiwanese apartment entryway, the male protagonist sits solemnly on a throne built from a ridiculous mountain of unopened delivery parcels. He holds a neat clipboard titled only with simple check marks (no readable extra words) and checks one more incoming box with the seriousness of a logistics commander. Preserve the reference identity: East Asian man, round youthful face, side-swept black hair, slightly sleepy eyes, black collared top with gray zipper/placket. He wears a tiny guilty half-smile and raises one eyebrow toward the cat. Beside him, a black-and-white tuxedo cat in a miniature warehouse safety vest stares deadpan at the parcel avalanche, one paw resting on a tiny toy pallet jack. Bright teal, orange, yellow, and coral accents; crisp realistic-comic rendering; highly expressive but not anime; funny visual contradiction at one glance.
3. Bottom white band, about 18% of the canvas. Center one single line of oversized rough hand-painted black Traditional Chinese text, verbatim: **「貓：管理室已經加開倉庫」**. Keep the colon and every character correct, bold, immediately readable, and fully inside the same safe margin.

Hard constraints: exactly 1080×1080; exactly one square single-panel image; exactly two main text lines total; no speech bubbles; no captions inside the scene; no extra readable text; no collage; no split panels; no six-panel comic; no watermark; no logo; no cropped text; no generic anime man; no other cats; the tuxedo cat must be clearly visible and deadpan. Preserve the protagonist’s facial identity with high fidelity to the reference photo.
