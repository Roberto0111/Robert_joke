# 2026-07-25 18:00 Generation Prompt

## 趨勢與去重

- 已讀取 `posts/2026-07-25_1800/trend_context.txt`。熱門詞多為產品、企業、地名或敏感健康議題，沒有比自創日常梗更自然的切入，因此本次不套用趨勢。
- 已比較最近 20 則貼文與 caption；避開衣服山、機場行李、演唱會、發票、走路步數、漏水、防曬、節氣、泡麵、躲桌底與近期職場管理句型。
- 本次改用浴室、量體重作弊、炸雞與「物品成為受害者」的反轉機制。

## 12 則候選評分

評分順序：意外性／畫面反差／貓的殺傷力／轉發感，滿分 20。

| # | 題材 | 上句 | 貓的下句 | 分數 | 判定 |
|---|---|---|---|---:|---|
| 1 | 浴室量體重 | 我最近吃得很節制 | 貓：體重計已申請保護令 | 5/5/5/5 = 20 | 入選 |
| 2 | 冰箱消夜 | 我開始尊重身體的聲音 | 貓：冰箱說那是門鈴 | 5/4/5/5 = 19 | 前五 |
| 3 | 健身房 | 我很重視核心訓練 | 貓：教練說那是憋氣 | 4/5/4/5 = 18 | 前五 |
| 4 | 沙發追劇 | 我正在培養專注力 | 貓：遙控器已經長褥瘡 | 4/5/5/4 = 18 | 前五 |
| 5 | 超商微波 | 我三餐都精準控時 | 貓：店員已經是你主廚 | 4/4/5/4 = 17 | 前五 |
| 6 | 洗衣服 | 我對衣物採自然療法 | 貓：鄰居以為陽台在發酵 | 4/4/4/4 = 16 | 合格未選 |
| 7 | 捷運座位 | 我很懂得保存體力 | 貓：博愛座都替你尷尬 | 4/4/4/4 = 16 | 合格未選 |
| 8 | 停車 | 我停車很講究效率 | 貓：拖吊車也準時下班 | 4/4/4/4 = 16 | 合格未選 |
| 9 | 牙線 | 我開始重視細節 | 貓：菜渣終於收到都更通知 | 4/3/5/4 = 16 | 合格未選 |
| 10 | 廚房料理 | 我做菜保留食材原味 | 貓：火根本沒開 | 2/4/2/3 = 11 | 淘汰：只是描述畫面 |
| 11 | 睡前滑手機 | 我在進行睡眠管理 | 貓：天亮替你結案了 | 3/4/4/4 = 15 | 合格但題材常見 |
| 12 | 辦公簡報 | 我正在重新定義進度 | 貓：空白頁升任主管了 | 3/3/4/3 = 13 | 淘汰：企業術語換皮且近期職場梗過多 |

非職場候選共 11 則（#1–#11），符合至少 8 則的要求。

## 前五名比較與淘汰原因

1. **量體重／20**：畫面一眼可懂，炸雞、單腳作弊、`ERR` 三層矛盾；貓把體重計改寫成受害者，並未重述動作。最終入選。
2. **冰箱消夜／19**：把「身體聲音」改寫成冰箱門鈴很俐落，但中央畫面容易退化成普通開冰箱，視覺荒謬度略低。
3. **健身房／18**：憋氣冒充核心訓練很具體，但 punchline 比較接近直接拆穿動作。
4. **沙發追劇／18**：「遙控器長褥瘡」夠靠杯，但主角躺沙發的姿勢與近期擺爛題材較接近。
5. **超商微波／17**：店員升格主廚有生活感，但需要較多場景資訊才能讀懂，單眼閱讀速度較慢。

## 最終選擇理由

「我最近吃得很節制／貓：體重計已申請保護令」總分最高。下句讓體重計成為具體受害者，重新定義「節制」為對量測工具施壓；不是「你只是」句型，也不是把單腳作弊照字面說一遍。浴室、單腳踩秤、另一腳撐馬桶、懷抱炸雞及秤面 `ERR` 能在一眼內完成視覺反差。

## 實際生成提示

Use case: illustration-story

Asset type: exactly one Instagram single-panel meme image, polished colorful realistic-comic style.

Primary request: Create ONE square 1:1 Taiwanese internet meme, one scene only, no panels, no collage. Preserve the identity and recognizable facial likeness from `assets/main_character_reference.jpg`: East Asian man, youthful round face, side-swept black hair, slightly sleepy eyes, black collared top with gray zipper/placket. He must look absurdly solemn and dead serious, not generic anime.

Scene/backdrop: Bright colorful small Taiwanese apartment bathroom. The man is solemnly cheating on a digital bathroom scale: only the toes of one foot barely touch the scale while the other leg is clearly supported on the closed toilet lid, as if this were a dignified scientific procedure. He clutches a large bucket of fried chicken against his chest. The scale display visibly reads `ERR`. Beside the scale sits a black-and-white tuxedo cat with a razor-sharp deadpan, deeply unimpressed expression, staring at him like a witness documenting abuse.

Composition/framing: Exactly three horizontal zones. Top clean white band about 20%, one continuous central scene about 60%, bottom clean white band about 20%. Keep all faces, objects, and text inside a generous safe margin. Square composition designed for 1080x1080 Instagram feed with no cropping.

Style/medium: polished realistic-comic meme illustration, strong recognizable likeness, expressive but anatomically believable, vivid colors, crisp detail, Taiwanese absurd deadpan humor, slightly rough ink texture.

Text (verbatim): top white band contains exactly `我最近吃得很節制`; bottom white band contains exactly `貓：體重計已申請保護令`.

Typography: oversized rough hand-painted black Traditional Chinese characters, bold and immediately readable on a phone, centered, one line per band, fully inside safe margin. No speech bubbles.

Constraints: exactly one image; exactly one male protagonist and one black-and-white tuxedo cat; only two main text lines; white bands; colorful square single-panel meme; preserve reference identity and clothing.

Avoid: six-panel comic, multiple panels, collage, extra captions, speech bubbles, explanatory text, Simplified Chinese, watermark, cropped text, generic anime face, extra people, extra cats, politics, medical themes.

## 輸出檢查

- 單張單格：是
- 正方形 1080×1080：是
- 上下白帶與兩行文字：是
- 繁體中文文字正確且在安全區：是
- 主角依參考照保留辨識特徵：是
- 黑白賓士貓為吐槽役：是
- 未發 Instagram、未執行 git push：是
