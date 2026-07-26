# 2026-07-26 12:00 Generation Prompt

## Trend decision

已讀取當次台灣 Google Trends。候選趨勢包括「辭職、東石漁人碼頭、股災、ghost rider、橄欖油、亞洲植物博覽會」等；沒有一個能比原創日常題材更自然地支撐笑點，且「股災」屬敏感財務語境，因此本次不硬套趨勢。

## Candidate scoring

評分順序：意外性／畫面反差／貓的殺傷力／轉發感，滿分 20。共 12 則，10 則為非職場題材。

| # | 題材 | 上句 | 貓的下句 | 分數 | 判定 |
|---|---|---|---|---:|---|
| 1 | 斷捨離（非職場） | 我最近很認真斷捨離 | 貓：垃圾車把你退貨了 | 5/5/5/4 = 19 | 入選；把主角降級成拒收垃圾，反轉具體且一眼成立 |
| 2 | 睡眠準備（非職場） | 我睡前都做好萬全準備 | 貓：你把明天設成選配了 | 5/4/5/4 = 18 | 前五；語意漂亮，但視覺需較多床邊物件才能讀懂 |
| 3 | 社交排毒（非職場） | 我最近在做社交排毒 | 貓：群組先把你排出去了 | 4/4/5/4 = 17 | 前五；反轉清楚，但手機畫面容易增加小字負擔 |
| 4 | 自助洗車（非職場） | 我開始自己照顧愛車 | 貓：停車場以為在辦告別式 | 4/5/4/4 = 17 | 前五；畫面強，但下句稍長且「告別式」不適合本次 |
| 5 | 露營（非職場） | 我來山上找回自己 | 貓：搜救隊叫你別再躲了 | 4/5/4/4 = 17 | 前五；場景新鮮，但搜救語境略有安全事件聯想 |
| 6 | 冰箱管理（非職場） | 我開始尊重食物期限 | 貓：考古隊已經接手了 | 4/4/4/4 = 16 | 合格未選；冰箱腐敗題材不夠討喜 |
| 7 | 健身（非職場） | 我今天專注核心訓練 | 貓：披薩盒不是瑜伽墊 | 3/5/4/4 = 16 | 合格未選；較接近描述畫面，反轉層次不足 |
| 8 | 閱讀（非職場） | 我最近都讀到忘記時間 | 貓：使用說明書也算一本喔 | 3/4/4/3 = 14 | 淘汰；近期已有外送菜單閱讀梗，主題重複 |
| 9 | 省電（非職場） | 我家很重視節能 | 貓：台電以為這戶沒人 | 4/4/4/3 = 15 | 合格未選；畫面容易太暗，人物辨識度受損 |
| 10 | 排隊（非職場） | 我很懂得把握零碎時間 | 貓：店員換班兩次了 | 3/4/4/4 = 15 | 合格未選；缺少足夠荒謬的具體行為 |
| 11 | 會議（職場） | 我讓每個人充分發言 | 貓：因為你睡著了 | 2/4/2/3 = 11 | 淘汰；直述畫面、職場句型老套 |
| 12 | 報表（職場） | 我正在提高數據透明度 | 貓：螢幕碎到看穿桌子了 | 3/4/3/3 = 13 | 淘汰；企業術語換皮，笑點不夠新 |

## Top five and rejection notes

1. **斷捨離 — 19/20（最終選擇）**：主角把自己包成待清運物，貓再揭露連垃圾車都拒收的後果；不是動作說明，而是身份降級。文字短、視覺可單場景完成，與最近 20 篇的題材、姿勢、場景及反轉機制皆不同。
2. **睡眠準備 — 18/20**：下句能重新定義「準備」，但中央畫面需要太多床邊道具，手機上一眼性稍弱。
3. **社交排毒 — 17/20**：群組先排除他的因果很準，但需要依賴手機介面或額外小字。
4. **自助洗車 — 17/20**：主角替老車做儀式的畫面夠荒謬，但死亡相關措辭不採用。
5. **露營 — 17/20**：戶外場景變化大，但搜救聯想不適合拿來當輕鬆日常梗。

## Final image-generation prompt

Use case: illustration-story  
Asset type: exactly one Instagram square single-panel meme  
Input image: `assets/main_character_reference.jpg` is the mandatory identity/likeness reference for the male protagonist, not an edit target.

Create exactly one polished, colorful, realistic-comic Taiwanese internet meme at exactly 1080×1080, 1:1. No collage, no panels, no speech bubbles, no watermark, and no additional text.

Fixed layout:

- Top 20–22%: a clean white band. Center one oversized rough hand-painted black Traditional Chinese headline, verbatim: **「我最近很認真斷捨離」**
- Middle 56–60%: one absurd outdoor residential alley scene in daylight. The protagonist has the recognizable identity from the reference: East Asian man, youthful round face, side-swept black hair, slightly sleepy eyes, black collared top with a gray zipper/placket. Preserve his facial likeness in a polished realistic-comic style, not generic anime. He sits bolt upright and absurdly solemn inside a large battered recycling cardboard box placed at the curb beside a few neatly discarded household objects. His posture is formal and dignified as if proudly demonstrating minimalist discipline, though he is visibly packaged as the main unwanted item. A small garbage/recycling truck is already driving away in the background without him. Include one black-and-white tuxedo cat prominently beside the box, staring at him with razor-sharp deadpan contempt, one paw resting on the rejected box flap. The cat must read as the roast character, not a cute accessory.
- Bottom 20–22%: a clean white band. Center one oversized rough hand-painted black Traditional Chinese punchline, verbatim: **「貓：垃圾車把你退貨了」**

Text rules: use only those two lines; render every Traditional Chinese character exactly; very large, heavy, immediately readable on a phone; keep all text fully inside at least 8% left/right safe margins and 5% top/bottom safe margins. Do not split either line awkwardly. No tiny labels on props.

Visual tone: 北七、靠杯、擺爛、一本正經講幹話. Bright saturated colors, crisp professional illustration, expressive but identity-preserving face. The protagonist remains completely solemn after the insult. Strong obvious visual contradiction in one glance.

Avoid: six-panel comic, multiple images, generic anime face, different clothing, extra people, other cat colors, cute cat expression, speech balloons, subtitles, signs, illegible or simplified Chinese, cropped text, cropped face, politics, danger, gore, death, disaster, brand logos.
