# 2026-07-24 12:00 Generation Prompt

## 趨勢與去重

- 讀取趨勢：周天成、發票、gundam xarx zero、碰撞、防空演習、欣西亞、ug、洛杉磯道奇、黃如意、王文洋。
- 僅「發票」能自然連結安全的台灣日常笑點，因此採用；其餘不是語意不明、容易硬套，就是屬於不適合玩笑的敏感脈絡。
- 已比較最近 20 篇 manifest 與 caption。本次避開走路、漏水、防曬、節氣、泡麵、躲藏、視訊會議、借充電線、檔案整理、辦公椅、會議紀錄、低電量、錯字、識別證、盆栽、微波、掃碼點餐、冷氣與棉被等近期主題。

## 12 個候選與評分

評分順序為：意外性／畫面反差／貓的殺傷力／轉發感，滿分 20。

1. 發票神壇（非職場）：「我對發票保持敬意」／「貓：它比你有機會翻身」— 5／5／5／5＝20
2. 冰箱修行（非職場）：「我最近開始斷食」／「貓：外送員以為你搬家了」— 5／4／5／5＝19
3. 雨傘人格（非職場）：「我做人一向有備無患」／「貓：你家有七把，外面一把都沒有」— 4／5／5／5＝19
4. 健身房會員（非職場）：「我固定投資健康」／「貓：健身房靠你退休」— 5／4／5／5＝19
5. 追劇自律（非職場）：「我很尊重睡眠品質」／「貓：所以你都醒著監督它」— 5／4／5／4＝18
6. 洗衣分類（非職場）：「我很重視衣物管理」／「貓：椅子已經升格衣櫃」— 4／4／4／5＝17
7. 行動電源（非職場）：「我隨時保持滿格」／「貓：只有行動電源有」— 3／4／3／4＝14
8. 冰塊咖啡（非職場）：「我懂得慢慢品味」／「貓：剩下的水比較有耐心」— 4／3／4／3＝14
9. 捷運站出口（非職場）：「我相信直覺帶路」／「貓：同一個出口見你三次了」— 4／4／4／4＝16
10. 超商集點（非職場）：「我消費很有目標」／「貓：目標比贈品貴兩千」— 4／4／5／5＝18
11. 信箱未讀（職場）：「我在培養訊息判斷力」／「貓：紅點已經比你資深」— 4／4／4／4＝16
12. 簡報遙控器（職場）：「我掌握全場節奏」／「貓：投影機還沒認識你」— 3／4／4／3＝14

非職場候選共 10 個。

## 前五名、淘汰註記與選擇理由

1. 發票神壇，20：入選。下句不是描述跪拜，而是把「翻身機率」轉移給發票，具體降級主角；神壇畫面一眼成立，也自然承接當日「發票」趨勢。
2. 冰箱修行，19：淘汰。外送與斷食反差清楚，但畫面需要同時交代冰箱、外送紀錄，單格資訊稍多。
3. 雨傘人格，19：淘汰。生活感強，但「出門忘帶傘」是常見梗，意外性略低於發票。
4. 健身房會員，19：淘汰。貓的降級很狠，但健身房會員沒去的題材過於普遍。
5. 追劇自律，18：淘汰。語言反轉漂亮，但深夜追劇的畫面機制不如供奉發票新鮮。

最終選擇「發票神壇」：四項皆為 5 分，總分最高；趨勢使用自然、安全，與近期 20 篇的主題、場景、姿勢和反轉機制均不同。貓的下句提供新事實層次，將發票的中獎可能變成對主角人生機率的具體羞辱，不是畫面解說，也未使用「你只是」句型。

## 最終生成規格

Use case: illustration-story  
Asset type: exactly one Instagram single-panel meme, 1080x1080 square.  
Input image: `assets/main_character_reference.jpg` is the mandatory identity/likeness reference. Preserve the recognizable East Asian man: youthful round face, side-swept black hair, slightly sleepy eyes, black collared top with gray zipper/placket. Do not make him generic anime.

Create ONE colorful square polished realistic-comic Taiwanese internet meme, one unified scene only, no panels and no collage.

Fixed layout: a top white band occupying about 20%, a colorful central scene about 60%, and a bottom white band about 20%. Use oversized rough hand-drawn black Traditional Chinese typography, perfectly spelled, centered, extremely readable on a phone, with generous safe margins. No other text anywhere.

Top text verbatim:「我對發票保持敬意」  
Bottom text verbatim:「貓：它比你有機會翻身」

Central scene: In a modest Taiwanese apartment living room, the referenced man kneels with absurdly solemn ceremonial dignity before a ridiculously improvised tiny household shrine. A single ordinary Taiwan receipt is reverently displayed upright under a warm desk lamp, with harmless comedic offerings such as one convenience-store tea egg and a tiny cup. His palms are pressed together, expression utterly serious and sleepy-eyed, as if worshipping his last hope. Beside the shrine sits a black-and-white tuxedo cat with a sharp, deadpan, judgmental face, staring at the man with withering contempt. The cat is unmistakably the roast character.

Style: polished colorful realistic-comic meme, recognizable reference likeness, expressive but not anime, Taiwanese everyday details, absurdly solemn, 北七、靠杯、擺爛、一本正經講幹話. Warm central colors contrasted with clean white text bands.

Constraints: exactly one image, one single scene, and two main text lines; Traditional Chinese only; no speech bubbles, scene captions, logos, or watermark. Keep every glyph and all faces fully inside safe margins. The receipt itself has no readable text or numbers. Bottom line begins exactly with「貓：」.

Avoid: six panels, multiple images, comic strip, extra text, misspelled Chinese, cropped typography, generic anime man, other cat colors, cute cheerful cat, political/news imagery, lottery balls, money raining, and brand marks.

## 產出與驗證

- 使用內建 imagegen，以本人照片作為 mandatory likeness reference。
- 生成一張單格圖，未生成其他候選圖。
- 原始正方形成品以等比例縮放至 1080x1080 PNG，未裁切。
- 視覺檢查：上下文字正確完整、單一中央場景、本人特徵可辨、黑白賓士貓明確、無對話框與額外可讀文字。
