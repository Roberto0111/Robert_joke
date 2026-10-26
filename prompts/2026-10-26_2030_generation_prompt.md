# 2026-10-26_2030 — 辦公室最後半塊餅乾

## 任務與素材

- `content_mode`: `life_dialogue`；`mood`: `comic`。
- 使用內建 `image_gen`，每頁各生成一張完整場景；本人照片 `assets/main_character_reference.jpg` 是必要的身份參考。完成後保存五張 1080×1350 PNG。
- 已讀 README、daily_comic_style、daily_posting_workflow、本次 reference_context、trend_context、analytics/latest.json、daily_strategy，以及最新20篇 manifest/caption/相關場景紀錄。
- 這次僅生成圖片、caption、prompt record、manifest；不執行發布流程、不 push。30秒為下游 Reel 的閱讀時間規格，本任務不另製作影片。

## 參考貼文五段結構分析（私用）

研究對象為本輪已提供的8張參考輪播，全部已檢視。僅分析敘事，不使用參考圖作為生成視覺輸入。

1. **辨識鉤子**：先讓同一種資源在兩個處境中產生不同結果，製造一眼可讀的反差；觀眾不用先讀長篇背景。
2. **具體場景**：用行李、座椅、食物、相機等日常物件，把抽象主張變成能辨識的動作；每段的道具都承擔敘事功能。
3. **累積推進**：先建立反差，再以不同活動逐步展開選擇的代價，讓後一張承接前一張的未解問題。
4. **情緒轉折**：視角從計算得失移到「自己究竟想要什麼」，再以人物的實際行動回應。
5. **最後壓縮與傳送動機**：用少量字將前面多個場景收束成一個容易記住的立場；可能被傳給一直延後行動的熟人。這只是結構推測，不是來源成效證據。

**不採用的實質論點**：不接受以年齡預設體力、醫療花費、勇氣或人生價值的說法，也不沿用旅行消費必然帶來長期回報的論證。不使用旅行、退休、山路、熱氣球、人生最年輕時刻等內容。部分參考圖下緣原本已裁切；不補造看不到的字句。

**原創性檢查**：新故事是辦公室茶水間的最後一口餅乾，核心矛盾是「想吃卻怕成為吃光的人」，結尾把不明確的禮讓對象翻成掃地機。題目、文字、角色、服裝、結論、場景與動作均獨立設計。使用單頁單場景、上方單行人文黑體、暖白大留白；不使用參考貼文的雙格、下方密集粗字、綠髮紫衣角色或任何來源句式。

## 成效與趨勢使用界線

- 2026-10-26T12:31:24.150Z 的 latest.json 共50筆：總觸及1959、分享1、收藏0、總互動27。策略中 A 組3筆、平均觸及45.33；B 組2筆、平均107.50。樣本與分享訊號不足以斷言何者有效，仍照本輪 A 組執行。
- 近期唯一分享訊號只支持繼續測試具體尷尬場景，不能把某一篇的題材或結論當成成長公式。
- 本輪熱門搜尋以人物、財經、國際與體育為主，與這個日常選擇沒有自然連結；全數不使用，也不使用未查證流行語。
- 以下分數全是出圖前編輯判斷，不是觀看、分享、收藏的實測或預測保證。

## 12個不同候選

分數順序：共鳴／對話自然／洞察／收藏分享，各0–5。每個候選都先核對想要、行動、代價。共4個職場、8個非職場；只有最高分且通過原創門檻的故事可出圖。

|ID|範疇與具體選擇：想要 → 實做 → 代價|分數|總分|具體傳送對象／判斷|
|---|---|---|---|---|
|W1|工作茶水間：想吃最後半塊餅乾又顧形象 → 一再掰小、留下一口 → 碎屑落桌落地，真正受益者轉成掃地機|5/5/4/5|19|每次都不肯拿最後一塊點心的同事；入選|
|N1|身材感受：想穿舒服的褲子 → 合身卻剪掉尺寸標籤 → 仍被尺碼的字困住|5/5/4/4|18|試衣先看尺寸才看舒適的朋友；非當日題材|
|N2|獨居飲食：想不浪費整包食材 → 一次煮四人份 → 接下來每天只能吃同一鍋|5/4/4/4|17|每次一人煮飯卻煮一週的朋友；結尾較弱|
|N3|買菜：想挑最划算的酪梨當晚餐 → 挑同價裡最大最硬的一顆 → 晚上無法吃、還得另找晚餐|4/5/4/4|17|買水果總挑最大顆的朋友；食品成熟度需更精確呈現|
|W2|借文具：想拿回自己的筆又不催人 → 再買一支代用 → 自己變成不能使用原物的人|5/4/4/4|17|不敢向同事拿回筆的人；與既有墊錢催款尷尬相近|
|W3|寄工作信：想被看見很努力 → 做完卻排到晚上寄 → 還得記住假裝工作的時段|4/4/3/4|15|會調整寄信時間的同事；與先前工時形象題接近，不選|
|W4|辦公室安靜：想專心又怕直接拒聊 → 戴沒有播放音樂的耳機假裝沒聽見 → 仍盯著別人是否靠近|4/4/3/3|14|戴耳機卻在看誰要說話的同事；近舊午休躲社交題，不選|
|N4|家務：想讓曬衣夾整齊配色 → 重夾已晾好的衣服 → 晚飯放涼仍在陽台|4/4/3/3|14|會為曬衣配色重做一次的家人；較像單格笑話|
|N5|休息：想選一部值得看的電影 → 反覆看預告與片單 → 可看正片的時間先用完|5/4/2/3|14|選片比看片久的朋友；熟悉老梗，洞察不足|
|N6|友情：想讓聚餐帳算得公平 → 分帳時不敢指出自己沒喝酒 → 回家對計算機重算|4/4/3/4|15|聚餐後才私下重算的朋友；容易變泛用界線勸說|
|N7|家庭：想留住媽媽手寫食譜 → 怕油污把紙封起來不拿出 → 做菜時仍得打電話重問|4/4/4/4|16|捨不得把家人的字跡放廚房的人；本輪不做家庭題|
|N8|數位生活：想拍好家貓的睡姿 → 為打光移燈、整枕頭 → 貓醒了只剩空枕頭|5/4/3/4|16|拍貓總想布置現場的朋友；近10/24貓片題，淘汰|

### 所有候選的五拍草稿

- **W1**：貓：半塊餅乾，你還掰？ → 我掰了三次，還不敢吃完。 → 貓：剩下那口要留誰？ → 不知道，吃最後一塊好像很貪心。 → 貓：再掰下去，就輪到掃地機了。
- **N1**：貓：褲子合身，標籤有罪？ → 穿著很舒服，我還是把尺碼剪了。 → 貓：哪裡太緊？ → 褲子沒有，是那個號碼看不順眼。 → 貓：布料放過你，兩個字還沒有。
- **N2**：貓：一個人吃，鍋怎麼滿了？ → 菜都拆了，乾脆一次煮完。 → 貓：明天想吃什麼？ → 想吃別的，可是還有三盒。 → 貓：你把菜救了，晚餐被扣留了。
- **N3**：貓：挑晚餐，怎麼只挑最大顆？ → 同樣價錢，當然拿重的。 → 貓：今天能吃嗎？ → 還很硬，晚上先吃泡麵。 → 貓：買晚餐，結果買到候補。
- **W2**：貓：自己的筆，也要借？ → 他還在用，我又買了一支。 → 貓：有問他拿回來嗎？ → 怕催一支筆，顯得很小氣。 → 貓：你大方到連失主都不敢當。
- **W3**：貓：寄封信還要等天黑？ → 下午做完，我排晚上寄。 → 貓：晚上還要改？ → 不用，只想讓人知道我很拚。 → 貓：你的工作做完了，演出還沒。
- **W4**：貓：沒放歌，你點什麼頭？ → 他一靠近，我就假裝沒聽見。 → 貓：只是想安靜？ → 對，可是直接說很難。 → 貓：耳機沒聲音，你倒演得很忙。
- **N4**：貓：衣服乾了，你還重夾？ → 藍衣服旁邊不能配紅夾子。 → 貓：誰會看？ → 我，站在這裡就忍不住。 → 貓：衣服下班了，夾子還在排隊。
- **N5**：貓：還在選？爆米花都吃完了。 → 預告看了十部，正片還沒開。 → 貓：還剩多久？ → 半小時，怕選錯浪費今晚。 → 貓：今晚已經讓預告演完了。
- **N6**：貓：飯吃完了，帳還在吃？ → 他們喝的酒，也算了我一份。 → 貓：剛剛怎麼沒說？ → 怕當場算清楚，很掃興。 → 貓：當場很熱鬧，計算機陪你生氣。
- **N7**：貓：食譜封起來，要怎麼煮？ → 媽的字，我怕沾到油。 → 貓：那比例呢？ → 每次煮還是打給她問。 → 貓：紙沒進廚房，她的聲音有。
- **N8**：貓：我睡覺，你在裝修？ → 我換個燈，再整理一下枕頭。 → 貓：拍好了？ → 還沒，你怎麼醒了？ → 貓：你要的那張，被你叫醒了。

## 前五名複核與取捨

1. **W1，19分，選用。** 五拍由「掰」這個可見動作一路推進；餅乾會碎，分得更小實際改變受益者。貓從詢問假設到指出意外後果，非勸人做自己。單一茶水間可演完，第一頁不靠caption解釋。
2. **N1，18分。** 尺碼對舒適的矛盾夠直接；末句仍較抽象，且非當日工作題。
3. **N2，17分。** 獨居煮飯很具體，惜食與選擇的交換可成立；「扣留」比喻較制式，後兩頁視覺推進較少。
4. **N3，17分。** 重量與當晚食用是兩個不同標準，轉折明確；成熟度牽涉看不見的時間，第一屏也較依賴台詞。
5. **W2，17分。** 遺失主人身分的反諷自然，但與8/17墊錢催款的深層困境太接近，不能只換成筆。

## editorial_decision

- **assigned_topic**：工作中的具體日常選擇；辦公室共享點心最後一塊。不談離職或沉沒成本。
- **assigned_hook_arm**：`organic_v3_opening_20261020_A`／貓先戳破一句。
- **audience_dilemma**：想吃剩下的餅乾，又想保留不貪心的形象；沒有具體等待的人，仍不敢吃完。
- **visible_first_frame_action**：Roberto站在辦公室茶水桌旁，雙手正要把已剩半塊的餅乾再掰小；空點心碟上已有少量碎屑，貓看著他的手，首句直接吐槽這個矛盾。
- **payoff_mechanism**：禮讓沒有明確受益者；不斷掰碎反而製造掃地機可清走的碎屑。P5指出未被計入的受益者，使前四頁的客氣變成荒謬的餵食流程。掃地機不出現在圖中，不以機器正在吃餅乾來重述文字。
- **specific_sharing_hypothesis**：觀眾可能想到辦公室每次把最後一塊點心再掰一半的那位同事。是假設，沒有要求觀眾分享或標記。
- **mood_reason**：`comic`；笑點來自一口餅乾被反覆掰小的自我打臉，以及貓指出最終可能吃到的是機器，並非情緒重量題。
- **soundtrack_reason**：下游對應 `playful_clown_instrumental_v1`，輕撥弦、短低音、木魚可配掰小與停手的喜劇節拍；無旁白，不添加音樂檔、不改既有配樂。
- **reading_timing**：5.5 / 5.5 / 5.5 / 6 / 7.5 秒，共30秒；每頁一句，末頁留下閱讀與笑點停頓。
- **difference_from_latest20**：工作題不再使用稿件、滑鼠、字體或尋找肯定；採站立／彎腰掰碎／停手／護著殘片／翻空手掌的身體動作。貓從桌邊凝視到伸掌追問，再看向落地碎屑；關係從同事間的社交假想轉到具體物理後果。

## 最新20篇逐篇去重

|日期|既有困境、場景與轉折|本篇差異|
|---|---|---|
|10/25|家裡送蔥蛋，送禮變點菜；母親、花瓶|沒有替家人決定需求；是自己怕吃光共享食物|
|10/24|客廳跪拍貓，朋友熟的是貓|不拍攝、不借媒介聯繫朋友|
|10/23|新家抱枕回箱，搬完不等於拒絕晚餐|不製造任務留人，沒有第三者留不留下|
|10/22|門口醬油累積，散步變備貨|不累積庫存；食物反而越掰越小|
|10/20|計程車趕三攤，熟的是司機|不排滿邀約；物理碎屑產生意外受益者|
|10/19|露營搭帳煮飯，想要的是公園|不重新命名想去的地方|
|10/18|煮麵省錢買耳機，獎勵反吃省下的錢|無消費金額、補償購物|
|10/17|拍照蹲痠，要求對方同樣辛苦|沒有對等付出計分或第三者比較|
|10/16|工作桌換字體，空白內容先穿衣|不是工作拖延或裝忙；茶水間吃點心|
|10/15|工具換盒，爸爸成家裡新來者|不替別人整理或改變使用方式|
|10/14|床上退團購群，終身承諾錯覺|不是不敢退出舊關係，無長時間負擔|
|10/13|茶角摔杯道歉，要對方先安慰|沒有造成對方損失、索取安慰|
|10/12|地墊放下手把滑手機，興趣得預約|不是等待完美大段時間|
|10/11|試衣店買不喜歡的衣服，購物變報恩|沒有店員服務或人情回報；餅乾本來想吃|
|10/10|羽球場答錯名，演成另一個人|不是長期身份扮演或難以糾正他人|
|10/09|工作檯傳初稿，想改的是同事答案|不尋求認可回饋或拒絕修稿|
|10/08|沙發替爸按手機，教出繼續依賴|無教學或搶做，沒有另一人被剝奪學習|
|10/07|生日對名單，祝福變考試|沒有考核朋友是否懂自己|
|10/05|KTV取消新歌，掌聲替自己點歌|無重演獲肯定表現；重點是無人領取的食物|
|10/04|吃到飽選蝦不吃布丁，回本奪走選擇|不計價格；餅乾想吃卻不敢拿完，碎裂的物理後果決定尾句|

另查歷史：7/24的掃地機用於代走步數，本篇沒有步數、健身或把工作交給機器；掃地機只出現在最後一句的預期後果。舊私人候選曾寫讓最後一塊雞肉、等對方讓回來；本篇沒有互讓、第三者或交換期待，採半塊餅乾持續碎裂的獨立情節，未使用其句子。

## 定稿與逐句朗讀檢查（出圖前）

1. 貓：半塊餅乾，你還掰？
2. 我掰了三次，還不敢吃完。
3. 貓：剩下那口要留誰？
4. 不知道，吃最後一塊好像很貪心。
5. 貓：再掰下去，就輪到掃地機了。

已按口語連讀五句檢查節拍：問眼前動作 → 次數證據 → 追問受益者 → 坦白形象顧慮 → 具體後果。P1含說話者與標點共11字元，低於16。P2、P4由Roberto說，畫面以他的開口表情提示。五句沒有重複同一道理，caption不補第一句必要資訊。餅乾易碎才讓掃地機的轉折成立，若換成信件、筆、衣服即失效。

## 生成美術規格

- 五張單一完整場景、4:5；暖白紙底，細膩平塗與極輕紙紋，俐落炭黑輪廓，柔和珊瑚橘、青綠、蜂蜜木色重點色。
- Roberto依照片保留年輕圓潤東亞臉、黑色旁分瀏海、略睏小眼與自然嘴形；約2.5頭身的原創迷你小丑。炭黑短外套、黑翻領上衣、灰色拉鍊門襟／背心、小紅領結、每側臉頰極小暖紅短線。不是寫實拼貼或泛用動漫男。
- 黑白賓士貓：黑耳／頭頂／背／尾、白鼻樑與口鼻、白胸、四白掌、琥珀色半瞇眼、粉鼻；不穿衣，維持固定花色。
- 固定辦公室茶水間小島場景：蜂蜜木圓桌、青綠桌腳、珊瑚高凳、暖灰矮櫃與透明水壺、兩只同款空青綠杯；桌上單一奶油色點心小碟與一塊金黃酥餅。無其他人物、無完整房間、無logo。貓固定可以從高凳觀察桌面。
- 一行黑色人文無襯線繁中，字形略有柔和圓角；約50–58px等效字高，整行最多佔860px，置於上方y=145–210；左右至少100px安全距離，不把短句拉寬填滿。畫面主要落在x=110–970、y=440–1200，場景與人物都完整、文字不碰臉。
- 不使用對白框、第二段文字、頁碼、分格、誇張眼淚、文字貼紙、綠髮、紫色西裝、疤痕笑妝或DC角色。
- P1雙手掰半塊；P2彎腰捏小片、有碎屑落下；P3貓抬掌問、Roberto停手；P4肩膀內縮坦白，手中保留小片；P5Roberto攤開空手、另一手仍拿最後小片，貓冷眼看桌腳碎屑。掃地機不畫出，尾句保留意外推論。

## 實際工具提示與完成驗證

實際工具提示如下；P1用本人照片，後續各頁用本人照片＋本篇核准P1，未將研究貼文送入生成工具。

### P4與P5出圖前追加的殘片大小限制

```text
IMPORTANT COOKIE CONTINUITY: only a TINY fingernail-sized cookie piece remains, about 12 by18px at1080px output, much smaller than the HALF COOKIE in reference page1. Do not redraw a half or quarter cookie. It must be pinched between two fingertips, not fill a hand.
```

### P3定向修正提示（原文）

```text
Edit input IMAGE 1, our approved PAGE 3, with one SMALL COOKIE continuity correction. Image 2 is PAGE 2 only to show the small crumb-sized cookie. In PAGE 3 the golden cookie remnant pinched between Roberto's fingers is TOO BIG. Reduce JUST THAT COOKIE to a fingernail-sized morsel about 12x18 pixels at1080px-wide output, like the small piece in PAGE2. Keep it naturally pinched between the same two fingertips; minimally close the gap if needed. It should not be a half or quarter cookie. Do not remove the cookie entirely.
Preserve EVERYTHING ELSE of IMAGE1: exact single-line headline "貓：剩下那口要留誰？", font, character and cat identity, faces, costumes, body positions, cat's raised paw, warm-white paper, scene scale, cabinet, pitcher, two cups, cream plate, all crumbs including floor crumbs, and furniture. Do not redraw the scene or change text. No new objects or words. Portrait4:5, final1080x1350.
```

### P4定向修正提示（原文）

```text
Edit input IMAGE1, our approved PAGE4, for continuity of ONLY a few GOLDEN COOKIE CRUMBS. Image2 is PAGE2 showing the already-dropped crumbs.
Add exactly THREE small golden cookie crumbs on the floor next to the FRONT-LEFT TEAL TABLE LEG, in the same area as image2 (near x370..420,y1145..1165 in1080x1350 equivalent). Add four tiny crumbs on the tabletop just outside the cream plate. These are tiny warm-gold broken-cookie crumbs, not large pebbles. Preserve cookie piece held near Roberto's chest.
Preserve EVERYTHING ELSE of IMAGE1: exact one-line Traditional Chinese headline "不知道，吃最後一塊好像很貪心。", typography, face/hair/gray collar-placket/red bowtie/cheek paint, posture scratching head, cat's crouching posture and markings, all furniture, cabinet, pitcher, two cups, plate and existing crumbs, rendering, scale, margins and background. Do not change wardrobe, faces, text or layout. No new objects except those specified crumbs. Portrait4:5, final1080x1350.
```

### P5定向修正提示（原文）

```text
Edit input IMAGE1, our approved PAGE5, for continuity of ONLY the scattered GOLDEN COOKIE CRUMBS. Image2 is PAGE2 showing the already-dropped crumbs.
Add exactly THREE small golden cookie crumbs on the floor next to the FRONT-LEFT TEAL TABLE LEG in the same area as image2 (near x370..420,y1145..1165 in1080x1350 equivalent). Add THREE small golden crumbs back onto the cream snack plate, which should not become completely empty. Keep the two existing tabletop crumbs and Roberto's tiny pinched cookie piece unchanged.
Preserve EVERYTHING ELSE of IMAGE1: exact single-line Traditional Chinese headline "貓：再掰下去，就輪到掃地機了。", font/margins, Roberto and cat identities/expressions, all fingers and poses, gray collar/zipper placket, tiny red bowtie, coat, cheek paint, stool/table/cabinet/pitcher/two cups, scene scale, paper and rendering. No vacuum cleaner; the joke stays in the text. Do not add any other object, word or panel. Portrait4:5, final1080x1350.
```

### 原始生成檔紀錄

基礎目錄：`/Users/roberto/.codex/generated_images/01a17831-dc97-73c2-ab45-bb375dcc19d0/`。本次使用內建 image_gen，無CLI/API fallback，沒有程式疊字或替代繪圖。共五頁生成與四次定向修正，交付只含五張核准頁。

|頁|核准原始檔|處理|
|---|---|---|
|1|exec-94ff598e-72e9-4b55-bdb0-0064831d3d9e.png|縮小場景、補齊櫃邊與留白|
|2|exec-9aa0608d-b520-43d1-adcc-9c936e7c5c72.png|首次輸出核准|
|3|exec-32458112-34ff-45eb-a47e-35354c15b776.png|縮小手中餅乾殘片|
|4|exec-e412bd79-e623-4325-aac3-bec51479b47b.png|補回桌上與地上碎屑|
|5|exec-9e9d430f-2904-4fbb-ae18-6b3e6a1deb02.png|補回碟上與地上碎屑|

原始生成檔保留在內建工具目錄。以 macOS `sips -z 1350 1080` 另存到使用者指定的五個PNG路徑，只做尺寸規格化，不加字、不裁切或合成。未改動照片與參考圖。


### 共同基礎提示（原文）

```text
Use case: illustration-story.
Create ONE finished original Taiwanese mini-clown editorial cartoon Instagram carousel page, portrait 4:5, intended final 1080x1350. ONE full-page scene, not panels.
INPUT IMAGE 1 is Roberto's mandatory real portrait, used only for likeness. Preserve his youthful ROUND East Asian face, natural broad small nose, side-swept BLACK fringe, small slightly sleepy mischievous eyes, natural small mouth. Translate into a fully drawn polished 2.5-head-tall chibi caricature, NEVER photographic face/skin/hair and NEVER a generic anime man.
Fixed wardrobe: charcoal-black short coat over black collared top with GRAY collar/zipper placket or vest, tiny RED bow tie, charcoal trousers and small black shoes. Very subtle original clown paint: just one short warm-red dash on each cheek. No whiteface, green hair, purple suit, scarred smile, or copyrighted movie costume.
Fixed companion: ONE black-and-white tuxedo cat with black ears/crown/back/tail, narrow centered WHITE nose blaze, white muzzle/chest and four WHITE paws, half-lidded amber eyes, small pink nose. Natural cat body, no clothing, no clown paint. It is a dry observant speaking partner.
Style: refined hand-drawn editorial illustration with crisp consistent dark charcoal contours, selective soft flat color and very light colored-pencil shading. WARM-WHITE paper background with very subtle fine paper grain, generous negative space. Playful COMIC mood, physical self-own rather than inspirational tone. Palette: honey oak, muted teal, soft coral, gold cookie, warm gray. No cinematic room, no photorealism, no generic anime.
Setting: a compact uncluttered OFFICE TEA CORNER, isolated small furniture vignette on warm-white paper: a honey-oak ROUND tabletop with muted TEAL legs, a CORAL round high stool for the cat, a small WARM-GRAY cabinet behind at right with ONE transparent water pitcher and TWO identical plain teal cups. On the round table ONE small CREAM plate for shared snacks. No other people, no robot vacuum, no plants, no extra props, no logos, no UI or labels.
TYPOGRAPHY AND SAFETY: exactly ONE horizontal line of black Traditional Chinese at top, clean bold HUMANIST SANS with gently rounded strokes, not condensed and not brush calligraphy. Glyph ink height about 52–58px at 1080 output. Do NOT enlarge short lines to fill width. Entire sentence must fit x=110..970 at 1080-equivalent width, baseline about y=205. Top and side margins generous. No quote marks around text. No additional text anywhere, no page number, speech balloon, watermark or decorative sticker.
CRITICAL COMPOSITION: keep the ENTIRE lower furniture-and-character illustration SMALL, fully within x=110..970 and y=440..1200 at 1080x1350-equivalent. All feet, tail, tabletop, cabinet and pitcher entirely visible, never cropped. Lots of warm-white paper above and around. All faces far below the headline, absolutely no overlap. Not a full-bleed scene.
```

### P1提示與第一次修正（原文）

```text
PAGE 1 OF 5. Exact sole headline: "貓：半塊餅乾，你還掰？"
Concrete opening contradiction: Roberto stands LEFT of the snack table, leaning over in comically over-careful concentration with puckered hungry lips and slightly sleepy side-eye. He is HOLDING one HALF of a round golden crumbly cookie between the thumb and forefinger of BOTH hands directly above the cream plate, poised to BREAK that already-small HALF into smaller pieces again. The flat broken edge and curved outer edge of this half-cookie should be clear. Only a few crumbs on the plate; no other whole cookies. Cat is sitting upright on the CORAL stool at the right/front of the table, looking at his pinching fingers with one eyebrow raised and tiny mouth open, delivering the headline. Roberto and cat both visible immediately. No person looking at camera. This is our master character and setting design for the remaining four pages.
```

```text
Edit this original PAGE 1 with ONE targeted layout correction. Preserve the existing drawn Roberto face/likeness, round cheeks, sleepy eyes, black side-swept hair, puckered mouth, hands holding half-cookie, gray collar/placket, tiny red bowtie, charcoal short coat, cheek dashes, the tuxedo cat and its markings and expression, furniture, pitcher, cups, plate, colors, paper texture and rendering. Exact headline remains "貓：半塊餅乾，你還掰？" on ONE line.
The lower scene is currently oversized and the cabinet is cut off. SHRINK the whole illustration uniformly to about 78% of its current size, and center the resulting small vignette in the lower part of the page. Complete the missing right edge and feet of the SAME warm-gray cabinet so the whole cabinet is visible. Keep relative positions of Roberto, table, stool, cat, cabinet, pitcher and cups. At intended 1080x1350, all illustrated objects must be fully inside x=110..970, y=440..1200 with >=110px blank paper at sides and >=150px below. Do not crop feet, tail or furniture.
Also keep the same headline typeface but set the entire ONE LINE at an actual ink glyph height of about58px, centered horizontally around y=175 with generous margins. Do NOT fill the entire width. Keep all 11 characters and punctuation correct, no new text.
Fill expanded space with identical warm-white paper. No new scene, no new props, no logo, no panels. Output portrait 4:5, target1080x1350.
```

### P2–P5連續性提示（原文）

```text

INPUT IMAGE 2 is the APPROVED PAGE 1 of this exact original story and is the strict continuity master. Match its actual drawn face/hair/skin simplification, coat/collar/placket/red bowtie, cheek dashes, cat markings and amber eyes, hand-drawn rendering, fine paper texture, charcoal outlines, honey round table with teal legs, coral stool, small warm-gray cabinet, transparent pitcher and two teal cups. Keep its SMALL inset lower-page scene, white margins, identical headline font and y position. Do not enlarge scene to fill the page. Long headlines must be smaller enough to remain ONE SINGLE HORIZONTAL LINE with >=100px left/right margins. Exactly the new page's sentence replaces the old sentence; no extra text. The reference photo controls likeness only; do not make later faces more realistic. Vary real body action per the following beat.
```

### P2場景提示（原文）

```text
PAGE 2 OF 5. Exact sole headline: "我掰了三次，還不敢吃完。"
Everyday evidence and escalation. Roberto now BENDS far forward over the SAME table, shoulders raised, lips slightly open as he speaks sheepishly. One hand pinches a very SMALL bite-sized golden cookie remnant above the cream plate; the other pinches a tiny crumb, as if he has divided it yet again. No half-cookie remains now. A few clearly visible golden crumbs lie on the cream plate and tabletop, and just THREE crumbs have dropped near the front teal table leg on the floor. Cat on the SAME coral stool is now standing with its white front paws braced at the edge of the tabletop, watching his fussy fingers with unimpressed narrowed eyes. Change actual body acting, not just camera zoom. Keep the cabinet, water pitcher, two teal cups and furniture perfectly consistent.
```

### P3場景提示（原文）

```text
PAGE 3 OF 5. Exact sole headline: "貓：剩下那口要留誰？"
The cat questions the imagined beneficiary. Cat now sits upright on the SAME coral stool, raises ONE white forepaw palm-up toward the small remaining cookie, mouth slightly open, level deadpan amber eyes looking at Roberto. Roberto has STRAIGHTENED halfway, frozen with the small cookie pinched in his left hand above the plate, right hand halted open; his face turns toward the cat, eyebrows slightly lifted as the question catches him. Same one small cookie remnant, crumbs on plate/table and three floor crumbs at front teal leg. No additional cookies, people, text or thought bubbles. Same scene continuity, a genuine new pose.
```

### P4場景提示（原文）

```text
PAGE 4 OF 5. Exact sole headline: "不知道，吃最後一塊好像很貪心。"
Vulnerable silly admission, still COMIC. Roberto stands at the SAME table but tucks his shoulders and elbows inward, holding the SAME tiny cookie remnant protectively near his chest in one hand, other hand scratching the back of his head. Sleepy eyes glance sideways down at the empty cream snack plate, mouth slightly open, small embarrassed crooked natural smile, no tears. Cat now settles low on the SAME coral stool with both white front paws together and a patient unimpressed stare at Roberto. Keep crumbs on the same plate/table and the three floor crumbs. Do not introduce a second person or new props. Same furniture and exact black/gray/red costume.
```

### P5場景提示（原文）

```text
PAGE 5 OF 5. Exact sole headline: "貓：再掰下去，就輪到掃地機了。"
Strongest dry comic turn. Roberto now holds the tiny cookie remnant still in his LEFT hand, away from his mouth, while opening his RIGHT palm and lowering it toward the crumb-covered table in a sheepish caught-out shrug. His black-fringed round face goes blank with realization, lips pursed, not a big grin. Cat is perched on the SAME coral stool, leans its head and ONE white forepaw toward the three GOLDEN CRUMBS by the front teal table leg, with half-lidded amber eyes and a small talking mouth. The cat has figured out the accidental beneficiary. Do NOT show a vacuum cleaner or any eating machine: the headline supplies an unexpected future consequence, not a literal depiction. Keep the cream plate, tiny cookie remnant, crumbs, table/cabinet/pitcher/two cups and all fixed colors consistent. Same small vignette with generous silence around it.
```


## 最終完成驗證

- 五張最終指定PNG均重新開啟目視：繁中與標點逐句符合定稿，一頁只有一句單行標題及一個完整場景，沒有裁字或壓臉。
- Roberto圓臉、旁分黑髮、灰翻領與門襟、炭黑短外套、小紅領結及兩頰短線連續；貓的白鼻口、白胸、白掌、黑背尾與琥珀眼連續。P3眼睛略睜大是被問住的表演，仍保持同一張臉。
- 蜂蜜木圓桌、青綠桌腳、珊瑚凳、暖灰櫃、水壺及兩只青綠杯一致。餅乾從半塊變為小殘片；P3已修正尺寸，P4、P5已補回落地碎屑。小碎屑在各頁的具體散布略有手繪差異，不影響物件與動作連續。
- P5實際貓爪指向桌面碎屑，地上碎屑同時可見；沒有畫掃地機。文字提出未發生的意外後果，沒有只描述圖中動作。
- 像素規格、解碼、非空檔與五個不同SHA-256均通過。五張為RGB PNG、1080×1350，單檔約1.9–2.1MB。標題墨跡字高64–72px，左右安全距離最低99px；在手機尺寸仍清楚。
- 最終左右文字邊距依頁為151/142、122/122、166/172、99/100、106/106px。只有對字色區域作像素量測，未聲稱OCR辨識通過；文字採逐張視覺核對。
- 首句完整11字元（含貓、冒號及標點）；第五句以「貓：」開頭。Caption有4個相關hashtag，包含#人生對話，最後一行等於第五頁句子，沒有索取互動。
- 舊caption逐字搜尋無五句定稿的重複。12候選（8非職場）、前5名、評分與淘汰原因、參考結構、原創檢查、近20篇差異、editorial_decision與配樂原因皆已記錄。
- Manifest狀態為generated，列出五張順序正確的相對路徑、caption、prompt、comic及30秒閱讀配置。沒有製作額外故事、影片或音訊，也沒有執行Instagram發布或git push。
