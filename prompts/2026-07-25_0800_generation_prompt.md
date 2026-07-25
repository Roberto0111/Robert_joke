# 2026-07-25 08:00 Generation Prompt

## 趨勢與去重

- 已讀取當次 Google Trends。人物、政治、國際與金融項目不適合自然地變成安全日常笑點，因此本次不硬套趨勢，採原創生活題材。
- 已比較最近 20 篇貼文、manifest、caption 與 generation prompt；避開追星、發票、走路、防曬、漏水、節氣、泡麵、躲桌底、視訊、充電線、檔案、辦公椅、會議紀錄、低電量、錯字、識別證、盆栽、微波爐、早睡、斷捨離與獨處等近期題材或候選機制。

## 12 個候選與評分

評分順序：意外性／畫面反差／貓的殺傷力／轉發感。

1. 非職場｜機場輕裝：上「我旅行都輕裝上陣」；下「貓：地勤把你歸類成行李了」；主角為省行李，把多層衣物、頸枕、鍋子與雜物全穿掛在身上。5／5／5／5＝20。
2. 非職場｜健康早餐：上「我開始吃健康早餐」；下「貓：營養師已經封鎖你了」；主角莊嚴地把牛奶倒進鹹酥雞碗。5／5／4／5＝19。
3. 非職場｜自然醒：上「我現在都自然醒」；下「貓：鄰居的電鑽算大自然？」；主角抱枕坐在施工牆邊，神情安詳。5／4／5／5＝19。
4. 非職場｜環保購物：上「我買東西都自備容器」；下「貓：店員在找失蹤的購物車」；主角推整台超市購物車回家裝宵夜。5／5／5／4＝19。
5. 非職場｜晨間儀式：上「我每天先整理思緒」；下「貓：馬桶已經開完三場會了」；主角穿正式上衣坐在馬桶上沉思，門外時鐘快速流逝。5／5／4／4＝18。
6. 非職場｜精準料理：上「我做菜很講究火候」；下「貓：消防隊比你準時」；主角拿秒錶守著冒煙平底鍋。4／5／4／5＝18。
7. 非職場｜閱讀習慣：上「我睡前固定閱讀」；下「貓：泡麵背面快被你考完了」；主角在床上用螢光筆研讀包裝。4／5／5／4＝18。
8. 非職場｜居家健身：上「我在訓練核心穩定」；下「貓：沙發先練會承重了」；主角躺著把啞鈴平衡在肚子上。4／5／4／4＝17。
9. 非職場｜省電生活：上「我最近很節能」；下「貓：電力公司在查空屋」；主角關掉所有燈，頭戴十幾支小手電筒。4／5／4／4＝17。
10. 非職場｜洗車哲學：上「我讓愛車回歸自然」；下「貓：鳥已經取得產權了」；主角在滿是鳥糞的車旁點香致敬。5／5／5／4＝19。
11. 職場｜收件匣：上「我讓信件自己沉澱」；下「貓：寄件人已經離職了」；主角把筆電放進透明沉澱缸旁等待。4／4／5／4＝17。
12. 職場｜會議準備：上「我開會前都充分暖身」；下「貓：大家已經先散場了」；主角在空會議室做伸展操。3／5／3／4＝15。

## 前五名、淘汰註記與最終選擇

1. 機場輕裝，20／20。最終選用：上句建立精明旅人形象，中央以「把行李穿成一個人」形成零閱讀門檻的荒謬反差；貓再揭露地勤的分類結果，把主角降級成行李，而非描述衣服很多。機場、站姿與身份降級機制均未出現在近期 20 篇。
2. 健康早餐，19／20。淘汰：鹹酥雞加牛奶的畫面很強，但貓的封鎖反應仍可套用到其他垃圾食物，專屬性略低。
3. 自然醒，19／20。淘汰：文字精準，但施工電鑽的聲音在靜態縮圖中不如機場穿戴行李直觀。
4. 環保購物，19／20。淘汰：隱藏後果明確，但近期已有「保全陪走」與「店員等待」類外部人物反應，機制較近。
5. 洗車哲學，19／20。淘汰：產權降級夠狠，但鳥糞會降低畫面的視覺舒適度與轉發意願。

## 最終內建 imagegen 提示

Use case: illustration-story  
Asset type: Instagram square single-panel meme for @roberto_joke  
Primary request: Create exactly one colorful 1:1 single-panel Taiwanese deadpan meme, polished realistic-comic style. The serious protagonist is absurdly over-dressed at a Taiwan airport because he has tried to avoid checking luggage by wearing and hanging every travel item on his body. A black-and-white tuxedo cat delivers the roast through the bottom text.  
Input image: `assets/main_character_reference.jpg` is the mandatory identity and likeness reference for the male protagonist. Preserve his East Asian identity, round youthful face, side-swept black hair, slightly sleepy eyes, and black collared top with gray zipper/placket visible beneath the ridiculous layers. Do not create a generic anime face.  
Scene/backdrop: One single airport check-in scene, no panels and no collage. The man stands absurdly solemn in front of a softly recognizable check-in counter. He wears many layered jackets and shirts, several travel neck pillows, and has harmless lightweight travel objects such as a small cooking pot, rolled towel, slippers, and pouches strapped or hanging from him. His stance and expression are dignified, as though this is expert travel technique. The tuxedo cat sits neatly in one small proper pet carrier beside him, staring up with a sharp, unimpressed deadpan expression. Background staff may be a blurred silhouette only; no extra readable signage, brands, screens, or labels.  
Style/medium: colorful polished realistic-comic meme, detailed expressive likeness, Taiwan internet meme energy, rough ink accents, slightly exaggerated physical comedy, not anime.  
Composition/framing: exact square composition designed for 1080x1080. Thick white band across the top, one central absurd scene, thick white band across the bottom. Keep every glyph, face, cat, carrier, and visual clue entirely within the inner 90% safe area.  
Typography: oversized rough hand-painted bold BLACK Traditional Chinese, centered, extremely legible on a phone, fully inside generous safe margins. Exactly two main text lines total, no speech bubbles and no extra text.  
Top text verbatim:「我旅行都輕裝上陣」  
Bottom text verbatim:「貓：地勤把你歸類成行李了」  
Lighting/mood: bright cheerful airport lighting and colorful travel objects; the man remains comically solemn and the cat remains cold and judgmental.  
Constraints: exactly one image; exactly one single scene; 1:1 square; Traditional Chinese text must be exact, complete, and readable; black-and-white tuxedo cat is mandatory; bottom begins exactly with「貓：」; preserve reference identity strongly.  
Avoid: six panels, multiple images, collage, speech bubbles, explanatory paragraphs, extra captions, cropped text, misspelled Chinese, simplified Chinese, generic anime man, cute smiling cat, other cat colors, logos, watermark, signature, politics, news, danger, cruelty, sensitive events, secrets, tokens.

## 選擇理由

「地勤把你歸類成行李」提供畫面之外的新後果，並把自認精明的旅客直接降級成托運物；它不是「你行李很多」的畫面解說，也沒有使用「你只是」句型。笑點由體面自我形象、明顯荒謬行為、具體身份降級三段在一眼內完成。
