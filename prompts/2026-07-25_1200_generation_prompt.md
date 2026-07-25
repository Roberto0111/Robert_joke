# 2026-07-25 12:00 Generation Prompt Record

## Trend decision

已讀取本次台灣 Google Trends。清單以人物、演唱會、司法與活動搜尋為主，其中部分敏感、部分缺乏自然日常反差；為避免硬套或誤用，本次選擇原創生活梗。

## Recent-post comparison

已比較最新 20 篇可用貼文與 caption。本次避開近期的旅行行李、追星黃牛、發票翻身、一萬步、漏水、防曬、大暑、泡麵、躲問題，以及舊有職場六格題材。最終採用臥室衣服山、照護姿勢與貓冷眼判決，笑點機制是「把拖延累積物降級成長照機構」，並非換皮企業術語或重述畫面。

## Twelve candidates and scores

評分順序：意外性／畫面反差／貓的殺傷力／轉發感；滿分 20。

1. 非職場｜上：我很重視衣服壽命｜下：貓：那張椅子已經是安養院了｜5／5／5／5＝20
2. 非職場｜上：我最近很享受獨處｜下：貓：群組先享受到了｜5／4／5／5＝19
3. 非職場｜上：我開始尊重食物原貌｜下：貓：瓦斯爐已經不認識你了｜4／5／5／4＝18
4. 非職場｜上：我對感情順其自然｜下：貓：自然界也沒有回你｜5／3／5／5＝18
5. 非職場｜上：我現在很懂得放手｜下：貓：垃圾車等你三個禮拜了｜4／5／5／4＝18
6. 非職場｜上：我睡前都會清空思緒｜下：貓：白天也沒補貨｜4／4／5／4＝17
7. 非職場｜上：我最近都自己帶便當｜下：貓：微波爐才是主廚｜3／5／4／4＝16
8. 非職場｜上：我開始管理手機時間｜下：貓：充電線在上大夜班｜4／4／4／4＝16
9. 非職場｜上：我很會維持體態｜下：貓：體重計已經轉職地磚｜3／4／4／4＝15
10. 非職場｜上：我現在很重視居家安全｜下：貓：外送員比家人更熟門牌｜3／3／4／4＝14
11. 職場｜上：我把工作留給專業的｜下：貓：同事已經把你留給人資｜4／3／4／4＝15
12. 職場｜上：我最近會議都很準時｜下：貓：散會前五分鐘才登入｜3／3／3／3＝12

## Top five review

1. 「衣服壽命／椅子安養院」20：入選。照護衣服山的荒謬視覺非常直接；「安養院」同時揭露累積時間與椅子的新身分，並非描述動作。
2. 「享受獨處／群組先享受」19：淘汰。文字反轉強，但退出群組需要額外介面小字才能讓中央畫面同樣有力。
3. 「食物原貌／瓦斯爐不認識」18：淘汰。廚房與泡麵災難近期已用過，場景重複風險較高。
4. 「順其自然／自然界沒回」18：淘汰。文字很靠杯，但單格中央動作不如衣服山具體。
5. 「懂得放手／垃圾車等三週」18：淘汰。視覺可做成抓垃圾袋不放，但下句對畫面依賴略高，反轉層次較薄。

## Final selection

選擇「我很重視衣服壽命／貓：那張椅子已經是安養院了」。總分最高 20／20，非職場、題材未見於近期貼文；主角像醫護人員般照顧衣服山，畫面先建立荒謬證據，貓再用「安養院」揭露長期堆放的隱藏時間成本並把椅子降級成機構。笑點一眼成立，且未使用「你只是」或解說式吐槽。

## Final image-generation prompt

Use case: illustration-story

Asset type: exactly one Instagram single-panel meme, square 1:1.

Input image: `assets/main_character_reference.jpg` is the mandatory identity/likeness reference for the male protagonist, not an edit target.

Create one polished colorful realistic-comic Taiwanese internet meme. Preserve the reference identity: East Asian man, round youthful face, side-swept black hair, slightly sleepy eyes, black collared top with a gray zipper/placket. Do not make him a generic anime character.

Fixed layout: exactly three horizontal zones, no panels and no collage. Top white band about 20% height with one oversized rough hand-painted black Traditional Chinese headline. Middle central scene about 60%. Bottom white band about 20% with one oversized rough hand-painted black Traditional Chinese punchline. Center all text and keep everything inside a generous safe margin.

Text, verbatim and only these two lines:

- Top:「我很重視衣服壽命」
- Bottom:「貓：那張椅子已經是安養院了」

Scene: in a colorful Taiwanese apartment bedroom, the protagonist looks absurdly solemn like a devoted medical caregiver while tending a dining chair buried under a huge long-accumulated mound of worn clothes. He tucks a small blanket around the clothes and holds a clipboard. Include one comically unnecessary IV stand with no readable small text. One black-and-white tuxedo cat sits prominently at the foot of the chair with a razor-sharp deadpan judging expression.

Style: polished realistic-comic illustration, recognizable face, crisp contours, rich color, slightly exaggerated absurdity, Taiwanese meme energy：北七、靠杯、擺爛、一本正經講幹話。

Constraints: exactly one square image; one continuous scene; exactly one male protagonist and one tuxedo cat; no speech bubbles, extra captions, logos, watermark, collage, split screen, extra people, extra cats, simplified Chinese, garbled glyphs, or text touching the edges.

## Validation

- Exactly one generated image
- Single continuous panel, 1:1
- Final PNG normalized to 1080×1080
- Two main text lines only; Traditional Chinese text matches verbatim
- Mandatory likeness, black collared top, gray placket, and tuxedo cat present
- No Instagram posting and no git push performed
