# 英文 — Past 詞彙題 Bank Analysis (83–115學測, 81–110指考)

GSAT-Tutor's data analysis of every past single-sentence vocabulary item (詞彙題) from the 學測 (incl. 83–88 推薦甄選 and 91/92 補考) and the 聯考／指考. It calibrates 詞彙題 writing, vocabulary teaching and study plans. It sits below the 考試說明 and the 111–115 papers in the authority order (SKILL.md §1). Treat it as tier-3/4 evidence, not policy.

## Provenance and license

- **Source**: the open item bank *JCEE-vocab-questions* by staresto-create (github.com/staresto-create/JCEE-vocab-questions, data built Oct 2026). It holds **843 items**: 500 學測 (`gsat/data.js`) and 343 聯考／指考 (`zhikao/data.js`). Each item has its sentence, options, key, Chinese gloss, the **詞彙表 level of every option** (111 list), and for 91–115 the **official 大考中心 答對率 and 鑑別度**. It also provides whole-paper word frequencies (35 學測 papers), a coverage list over levels 2–6, and teacher-written polysemy and look-alike sets.
- **License**: the repo's own analysis (解析, 中譯, 分類, 標註) is **CC BY-NC 4.0**. Attribute 「資料來源：JCEE-vocab-questions (staresto-create)，CC BY-NC 4.0」 when quoting its glosses or lists to students, and use them non-commercially. The exam items themselves are copyright 大考中心 (cite as 「114學測英文第3題」).
- **Verified**: spot checks show the repo's option levels match `vocabulary.md` (e.g. accustom [6], minimal [5], doubtful [3]). Statistics below were computed directly from the data files. Where a category is GSAT-Tutor's own judgment (e.g. "secondary sense"), it is labeled as such.
- Item-level citations for 111–115 are in §3. For 83–110, cite year and number from the student's own copy. Do not quote pre-111 items from memory.

## How to use this file

| Mode | Use |
|---|---|
| 觀念講解 | §6 secondary senses, §7 repeat keys, §9 look-alikes: teach a word with its tested frame and the trap. |
| 模擬出題 (詞彙題) | §4 rules on top of `item-writing.md` §2; §3 as the calibration set; §8 for "high-yield but never keyed" candidates. |
| 弱點診斷／讀書計畫 | §2 difficulty data to set realistic targets; §7–§8 as priority word lists, ordered by level. |

---

## 1. Dataset at a glance

| Era | Items | Format |
|---|---|---|
| 83–88 推薦甄選 | 10–20 per year | single words **and** phrase sets (gave in, called off, in common) |
| 89–110 學測 (+91, 92 補考) | 15 per year | 89–93 still include a 5-item phrase block; phrase-only option sets end after 95 |
| 111–115 學測 | 10 per year | single words only, 1分 each |
| 81–110 聯考／指考 | 10–15 per year | harder; keys skew to L5–L6 |

Phrase items (all four options are phrases) appear in 學測 85–93 and 95, and in 聯考 89–90. **They are gone from the 108課綱 學測.** Phrasal knowledge is now tested through collocation frames inside single-word items (§4) and through 綜合測驗.

## 2. What the numbers show

**Key level distribution** (counts; "—" = phrase or off-list):

| Era | L1 | L2 | L3 | L4 | L5 | L6 | — | Mean 答對率 |
|---|---|---|---|---|---|---|---|---|
| 學測 83–98 | 11 | 46 | 57 | 73 | 18 | 6 | 59 | 52% (91–98) |
| 學測 99–110 | 5 | 22 | 52 | 84 | 11 | 3 | 3 | 62% |
| **學測 111–115** | 1 | 5 | 13 | **21** | **10** | **0** | 0 | **49%** |
| 指考 81–110 | 5 | 34 | 34 | 94 | 101 | 47 | 28 | 53% (91–110) |

Takeaways:
1. **L4 is the modal key level; L5 has doubled since 111** (20% of keys vs 6% in 99–110). No 111–115 key is L6 or off-list, which matches the 考試說明 and `item-writing.md` (no L6 keys).
2. **The 108課綱 詞彙題 is harder.** Mean 答對率 fell from about 62% (99–110) to 49% (111–115), even though keys did not get rarer on average. Yearly means: 111 57%, 112 52%, 113 41%, 114 50%, 115 47%.
3. **Difficulty comes from usage, not rarity.** In 111–115, the 15 items GSAT-Tutor classifies as testing a common word's secondary sense or a fixed collocation average **38%** 答對率, against **54%** for the other 35. The six hardest 111–115 items are quest 16%, promises 15%, due 23%, counter 23%, graced 23%, grave 24%. Only quest is L5; due and promises are L2.
4. **Two items have negative 鑑別度**: 112-4 bare (−6) and 113-8 promises (−13). Strong students over-thought them, rejecting the plain fit because "too easy a word". In teaching, name the trap: when a low-level option fits the frame exactly, take it.
5. **Distractor levels relative to the key** (111–115, 149 distractors): same level 69, lower 42, higher 38. Level alone never gives the answer away.
6. **Options nearly always share part of speech and inflection** (e.g. all -ed, all -ly, all -ing). Inflected keys are common: roughly 40% of all keys end in -ly/-ed/-s/-ing.
7. **Context span**: 92% of items are solvable inside one sentence. Only 2 of 50 in 111–115 need a second clause or sentence (111-2 assistant, 112-6 recall). Cross-sentence items are not harder on average (55% vs 57%).
8. **POS balance** (all 843 keys): n. 28%, v. 26%, adj. 24%, adv. 14%, phrases 8%. Adverb keys are almost always -ly derivatives of L3–L5 adjectives (potentially, supposedly, randomly, verbally, initially).
9. **Whole-paper coverage** (35 學測 papers, 89,606 running words excluding proper nouns): L1 75.0%, cumulative L1–2 86.0%, L1–3 91.1%, L1–4 95.4%, **L1–5 97.3%**, L1–6 98.2%; off-list 1.8%. A student who knows L1–5 meets about 1 unknown word in 37 across the whole paper.

## 3. Calibration set: 111–115 學測 詞彙題 (all 50)

答對率 and 鑑別度 are official 大考中心 figures as compiled in the repo. "Tested frame" is the repo's collocation note (first clause).

| 題 | Key [L] | POS | 答對率 | 鑑別度 | Distractors [L] | Tested frame |
|---|---|---|---|---|---|---|
| 111-1 | **delivered** [2] | v. | 83% | 44 | advanced [3], offered [2], stretched [2] | has it ___ to his house |
| 111-2 | **assistant** [3] | n. | 74% | 60 | influence [2], contribution [4], politician [3] | the best ___ I have ever had |
| 111-3 | **puppet** [3] | n. | 50% | 57 | chat [3], quiz [2], variety [3] | traditional hand ___ shows |
| 111-4 | **potentially** [4] | adv. | 61% | 69 | delicately [4], ambiguously [4], optionally [5] | due to its ___ fatal side effects |
| 111-5 | **Tagging** [3] | v. | 70% | 45 | Flocking [3], Rolling [1], Snapping [3] | ___ the photos with dates and keywords |
| 111-6 | **agreeable** [4] | adj. | 52% | 24 | enormous [4], intimate [4], ultimate [5] | an ___ person is usually pleasant |
| 111-7 | **visible** [3] | adj. | 49% | 43 | identical [4], available [2], remarkable [4] | the entrance is barely ___ to passersby |
| 111-8 | **eventual** [4] | adj. | 67% | 62 | moderate [4], absolute [4], promising [4] | the ___ cost is likely to be 50 percent higher |
| 111-9 | **quest** [5] | n. | 16% | 15 | trial [2], route [4], strike [2] | go on a ___ for dinosaur fossils |
| 111-10 | **blushes** [5] | v. | 45% | 33 | bounces [4], polishes [4], transfers [4] | the valley ___ like a young bride |
| 112-1 | **sticky** [3] | adj. | 73% | 56 | greasy [4], clumsy [4], mighty [3] | it is ___ and very hard to remove |
| 112-2 | **pose** [2] | n. | 88% | 26 | clap [2], toss [3], snap [3] | adopt an elegant ___ for a camera shoot |
| 112-3 | **ancestors** [4] | n. | 64% | 68 | siblings [5], commuters [5], instructors [4] | trace her ___ back to their arrival |
| 112-4 | **bare** [3] | adj. | 28% | -6 | blank [2], hollow [3], queer [3] | find the shelves almost ___ |
| 112-5 | **sincerity** [4] | n. | 57% | 68 | liability [5], generosity [4], integrity [5] | did not feel any ___ in his apology |
| 112-6 | **recall** [4] | v. | 70% | 67 | resolve [4], fraction [5], privilege [4] | astonishing powers of ___ |
| 112-7 | **counter** [4] | vt. | 23% | 22 | provoke [5], expose [4], convert [5] | evidence to ___ the drug company’s claims |
| 112-8 | **crippled** [5] | v. | 41% | 53 | accelerated [5], rendered [5], ventured [5] | have ___ the country's economy |
| 112-9 | **choked** [4] | v. | 35% | 35 | disturbed [4], enclosed [4], injected [5] | were ___ with traffic all day |
| 112-10 | **supposedly** [5] | adv. | 37% | 29 | undoubtedly [5], roughly [3], understandably [—] | the ___ unbiased media |
| 113-1 | **slender** [3] | adj. | 54% | 43 | spicy [5], slight [4], slippery [3] | desire a ___ figure |
| 113-2 | **emerging** [4] | v. | 54% | 71 | flashing [3], rushing [3], floating [3] | watching the sun ___ from a sea of clouds |
| 113-3 | **due** [2] | adj. | 23% | 6 | apt [5], bound [5], docked [3] | what time the next bus is ___ |
| 113-4 | **humidity** [4] | n. | 59% | 65 | density [5], circulation [4], atmosphere [4] | the roasting heat and high ___ |
| 113-5 | **stand** [1] | v. | 47% | 59 | stay [1], take [1], serve [2] | will no doubt ___ the test of time |
| 113-6 | **compulsory** [5] | adj. | 34% | 27 | forceful [2], realistic [4], distinctive [5] | military service is ___ |
| 113-7 | **credit** [3] | n. | 29% | 31 | advantage [3], revenge [4], remedy [4] | always took the ___ for all the hard work |
| 113-8 | **promises** [2] | v. | 15% | -13 | proposes [2], contains [2], confirms [3] | the business hotel ___ not only good service |
| 113-9 | **appeal** [3] | n. | 39% | 48 | approach [2], operation [3], observation [4] | making an ___ for the public to donate blood |
| 113-10 | **randomly** [5] | adv. | 59% | 67 | eligibly [5], apparently [4], consequently [4] | would be ___ placed in a study group |
| 114-1 | **container** [4] | n. | 76% | 56 | border [2], timer [1], marker [3] | If you put a ___ under a leaking faucet |
| 114-2 | **produce** [2] | n. | 70% | 40 | fashion [2], brand [2], trend [3] | a variety of fresh seasonal ___ |
| 114-3 | **blurring** [5] | v. | 47% | 61 | trimming [5], draining [3], glaring [5] | many of my childhood memories are already ___ |
| 114-4 | **offensive** [4] | adj. | 52% | 65 | excessive [5], furious [4], stubborn [3] | Racist remarks are by nature ___ and hurtful |
| 114-5 | **draft** [4] | n. | 42% | 41 | text [2], brush [2], plot [4] | Not satisfied with the first ___ of her essay |
| 114-6 | **vacant** [3] | adj. | 54% | 61 | casual [3], fragile [4], remote [3] | Left ___ for years, the deserted house |
| 114-7 | **enormous** [4] | adj. | 49% | 31 | gigantic [4], exclusive [5], multiple [4] | The high school student showed ___ courage |
| 114-8 | **halted** [4] | v. | 47% | 61 | hatched [3], possessed [4], reinforced [5] | Publicly financed projects are often ___ or delayed |
| 114-9 | **graced** [4] | v. | 23% | 9 | praised [2], addressed [2], credited [3] | ___ the school’s graduation ceremony |
| 114-10 | **verbally** [5] | adv. | 42% | 59 | dominantly [4], legitimately [5], relevantly [4] | was sued for ___ abusing his colleagues |
| 115-1 | **tight** [3] | adj. | 57% | 54 | hasty [3], diligent [4], routine [3] | has such a ___ schedule |
| 115-2 | **amateur** [4] | adj. | 48% | 61 | official [2], instant [2], elementary [4] | Jane started as an ___ art designer |
| 115-3 | **vacancy** [4] | n. | 45% | 59 | career [3], expectation [3], inspiration [4] | The teaching ___ at the famous high school |
| 115-4 | **initially** [4] | adv. | 65% | 71 | genuinely [4], alternatively [4], fundamentally [4] | has created far more profit than ___ expected |
| 115-5 | **consumption** [5] | n. | 63% | 69 | dimension [5], integration [5], provision [5] | a balanced ___ of fruit and vegetables |
| 115-6 | **dreads** [4] | v. | 29% | 38 | stresses [2], wanders [3], escapes [2] | Timmy ___ the thought of speaking |
| 115-7 | **passion** [3] | n. | 66% | 48 | resource [3], impact [4], emphasis [4] | music is his life’s ___ |
| 115-8 | **assaulted** [5] | v. | 47% | 52 | shattered [5], overturned [5], condemned [5] | shouted at passers-by and ___ them with glass bottles |
| 115-9 | **elbow** [3] | v. | 29% | 21 | crash [3], tumble [4], struggle [2] | ___ my way through the crowd |
| 115-10 | **grave** [4] | adj. | 24% | 18 | swift [3], brutal [4], harsh [4] | have raised ___ concerns |

Patterns in this set:
- **Frame-locked keys**: be choked with traffic, take the credit for, make an appeal for, go on a quest for, elbow one's way through, grace … with one's presence, stand the test of time, raise grave concerns, a tight schedule, fill a vacancy, have a passion for, dread + V-ing. Students who learned only the Chinese meaning fail these.
- **Conversion (詞性轉換)**: counter vt., elbow v., grace v., produce n., pose n., due adj. (arrival), stand v. (withstand). The familiar word appears in an unfamiliar part of speech.
- **Semantic-field distractors**: options come from the same field or same form class (blurring/trimming/draining/glaring; shattered/overturned/condemned/assaulted). They are not random words.
- **Look-alikes as distractors**: enormous vs gigantic (114-7: both "huge"; only enormous collocates with courage), vacant vs vacancy reused across 114 and 115.

## 4. Item-writing rules for 詞彙題 (refines `item-writing.md` §2)

Apply on top of the existing format rules.

1. **Key level**: target the 111–115 mix. For a 10-item set: about 1 at L1–2 (secondary sense), 3 at L3, 4 at L4, 2 at L5. Never L6 or off-list.
2. **Difficulty lever = frame, not rarity.** For harder items, test (a) a fixed collocation (verb + noun, adj + noun, preposition after the key), (b) a common word in a secondary sense or a converted part of speech (§6), or (c) an -ly/-ed derivative whose base the student knows. Don't make items harder by raising the key to L6.
3. **Every key needs a clue the student can point to**: the collocate (with traffic, for the public to donate blood), a contrast or cause signal, or a defining apposition. State the clue in the 解析, as the repo's "tested frame" does.
4. **Distractors**: same part of speech and same inflection as the key. Draw them from the key's semantic field or form family (§9), at mixed levels (some lower, some equal, some higher). Each must fail on meaning **or** on collocation, and the 解析 says which. Avoid a distractor that fits the collocation in some regional usage.
5. **Plain-word trap**: include about one item per set whose key is an L1–L3 word in a less familiar sense, alongside harder-looking distractors. This mirrors 113-8 promises and 112-4 bare.
6. **Avoid duplicating a past item.** Reusing a past key is realistic (§7 shows 72 repeats), but write a new sentence and new frame. When the key comes from §3, say 「改寫自 114學測第6題的考點」 in the 解析.
7. **No phrase-option sets** in 學測-style 詞彙題. Put phrasal verbs and idioms into 綜合測驗 or 中譯英 practice instead.
8. **Self-check additions**: (a) solve it again while ignoring the Chinese meaning; is the collocation alone decisive? (b) Would a strong student talk themselves out of the key? If so, keep it deliberately (rule 5) or sharpen the clue.

## 5. Difficulty targets for diagnosis

Use these to set expectations, not to promise scores.

| Student profile | Expected 詞彙題 accuracy (10 items) | Focus |
|---|---|---|
| Knows L1–3 well, L4 patchy | 3–5 | L3–4 core with collocations; §7 repeat keys |
| Solid L1–4, some L5 | 5–7 | L5 recognition; §6 secondary senses; frames in §3 |
| Strong (前標 and up) | 7–9 | §6 conversions; plain-word trap; 指考-level L5–6 for reading only |

Official mean for 111–115 is about 5 of 10. Any student consistently at 7+ on realistic sets is above average.

## 6. Common words in secondary senses (polysemy list)

Teacher-curated in the repo: 135 words whose exam use differs from the sense students learn first. Format: `word [level]: familiar sense → **tested or exam-relevant sense**`. Use in 觀念講解 and when writing plain-word-trap items. Senses quoted from the repo (CC BY-NC 4.0).

- book [1]: book n. 書 → **book v. 預訂**
- grace [4]: grace n. 優雅 → **grace v. 光臨，使（場合）增光**
- elbow [3]: elbow n. 手肘 → **elbow v. 用手肘推擠**
- counter [4]: counter n. 櫃台 → **counter v. 反駁**
- shelter [4]: shelter n. 避難所 → **shelter v. 保護，使免受（風雨、炎熱）**
- remedy [4]: remedy n. 療法，解決辦法 → **remedy v. 補救，彌補**
- urge [4]: urge n. 衝動 → **urge v. 力勸，敦促**
- produce [2]: produce v. 生產 → **produce n. 農產品**
- commercial [2]: commercial n. 廣告 → **commercial adj. 商業的，以營利為目的的**
- grave [4]: grave n. 墳墓 → **grave adj. 嚴重的，重大的**
- prompt [4]: prompt v. 促使； n. 提示 → **prompt adj. 迅速的，及時的**
- mean [1]: mean v. 意思是 → **mean adj. 刻薄的，卑鄙的**
- earnest [4]: earnest adj. 認真的 → **in earnest（真心地，認真地；earnest 當名詞）**
- command [2]: command n. 命令，指揮 → **command n. （對語言、知識的）掌握**
- fortune [3]: fortune n. 運氣，命運 → **fortune n. 一大筆錢，財富**
- practice [1]: practice n. 練習 → **practice n. （醫師、律師的）執業**
- screen [2]: screen n. 螢幕； v. 放映 → **screening n. 篩檢，檢查**
- light [1]: light n. 光； adj. 輕的 → **light adj. （交通）順暢的，車流少的**
- defensive [4]: defensive adj. （比賽中）防守的 → **defensive adj. 防衛心重的，聽不得批評的**
- roughly [3]: roughly adv. 粗糙地，粗暴地 → **roughly adv. 大約，大致上**
- mock [5]: mock adj. 模擬的，假的 → **mock v. 嘲笑，嘲弄**
- pedal [5]: pedal n. 踏板 → **pedal v. 踩踏板騎（腳踏車）**
- hail [6]: hail n. 冰雹 → **hail v. 讚譽為，稱頌**
- appeal [3]: appeal v. 吸引，對……有吸引力 → **appeal n. 呼籲，懇求**
- rise [1]: rise v. 上升，升起 → **rise n. 上升，增加（on the rise 正在增加）**
- release [3]: release v. 釋放 → **release n. 新推出的作品（新書、新片、新專輯）**
- spark [4]: spark n. 火花 → **spark v. 引發，激發**
- lower [2]: lower adj. 較低的，下面的 → **lower v. 降低**
- stem [4]: stem n. （植物的）莖 → **stem v. 源自，起因於（stem from）**
- credit [3]: credit n. 信用，賒帳（credit card 信用卡） → **credit n. 功勞，讚揚**
- orientation [4]: orientation n. 方向，取向 → **orientation n. 新生訓練，職前說明會**
- edge [2]: edge n. 邊緣 → **edge n. 優勢**
- robust [6]: robust adj. （人）強壯的，健壯的 → **robust adj. 強勁的，穩健的**
- choke [4]: choke v. 噎住，窒息 → **choke v. （道路）塞滿，堵塞**
- acknowledge [5]: acknowledge v. 承認 → **acknowledge v. 公開致謝，感謝**
- unfold [5]: unfold v. 攤開，打開（摺起來的東西） → **unfold v. （事件）逐步展開，發展**
- strike [2]: strike v. 打，撞擊 → **strike v. （想法）突然浮現在腦中（it strikes sb that…）**
- work [1]: work v. 工作 → **work v. （機器）運作；（方法）管用，有效**
- stand [1]: stand v. 站立 → **stand v. 經得起，禁得起（考驗）**
- catch [1]: catch v. 接住，抓住；趕上（車） → **catch v. 吸引（注意）**
- occur [2]: occur v. 發生 → **occur v. （想法）浮現在腦中（occur to sb）**
- serve [2]: serve v. 端上（飯菜），服務 → **serve v. 充當，作為（serve as）**
- decline [5]: decline v. 婉拒 → **decline v. 減少，衰退**
- purchase [5]: purchase v. 購買 → **purchase n. 買的東西**
- trace [3]: trace n. 痕跡 → **trace v. 追溯（起源）**
- honor [3]: honor n. 榮譽 → **honor v. 向……致敬，紀念**
- last [1]: last adj. 最後的 → **last v. 持續，維持**
- favor [2]: favor n. 恩惠，幫忙（do sb a favor） → **favor v. 偏好，比較喜歡**
- share [1]: share v. 分享 → **share n. （該盡的）一份，本分**
- even [1]: even adv. 甚至； adj. 平坦的，偶數的 → **even v. 使平均，使平衡（even out）**
- demanding [4]: demand v. 要求 → **demanding adj. 費力的，要求高的**
- alert [4]: alert adj. 警覺的，機警的 → **alert v. 使警覺，提醒**
- combat [5]: combat n. 戰鬥 → **combat v. 對抗，防治**
- due [2]: due to phr. 由於 → **due adj. 應有的，應給的**
- house [1]: house n. 房子 → **house v. 收藏，容納**
- turn [1]: turn v. 轉動，轉彎 → **turn n. 轉彎處（at every turn 處處）**
- worship [5]: worship n. 崇拜，禮拜（a place of worship 禮拜場所） → **worship v. 敬拜（神明）**
- age [1]: age n. 年齡 → **age v. 使老化，使變舊**
- medium [3]: medium adj. 中等的（medium size 中號） → **medium n. 媒介，表現形式（複數 media）**
- leading [1]: lead v. 帶領 → **leading adj. 頂尖的，居領導地位的**
- delight [4]: delight n. 欣喜，快樂 → **delight v. 使欣喜**
- depart [4]: depart v. 離開，出發 → **departed adj. 已故的**
- wear [1]: wear v. 穿，戴 → **worn out adj. 筋疲力盡的（wear 另一個意思是「磨損」）**
- tear [2]: tear [tɪr] n. 眼淚 → **tear [tɛr] v. 撕破，撕開（過去式 tore，過去分詞 torn）**
- novel [2]: novel n. 小說 → **novel adj. 新穎的，新奇的**
- move [1]: move v. 移動，搬家 → **move n. 措施，做法**
- subject [1]: subject n. 科目，主題 → **subject adj. 容易遭受……的（be subject to）**
- dispute [4]: dispute v. 爭論，對……提出異議 → **dispute n. 糾紛，爭議**
- shield [5]: shield n. 盾牌 → **shield v. 保護，遮擋（shield sb from）**
- present [1]: present n. 禮物； adj. 現在的 → **present adj. 在場的，出席的**
- involve [4]: involve v. 牽涉，包含 → **involved adj. 參與其中的（those involved）**
- flight [2]: flight n. 飛行，班機 → **flight n. （兩層樓之間的）一段樓梯**
- celebrate [1]: celebrate v. 慶祝（節日、生日） → **celebrate v. 頌揚，讚揚**
- publication [4]: publication n. 出版，發行 → **publication n. 出版品，發表的作品**
- responsible [2]: responsible adj. （人）負責的 → **responsible adj. （事物）造成……的（be responsible for）**
- deny [2]: deny v. 否認 → **deny v. 不准，拒絕給予**
- mark [1]: mark v. 做記號，標示 → **mark v. 紀念（日子、事件）**
- cater [6]: cater v. 承辦酒席，提供外燴 → **cater v. 迎合，滿足……的需求（cater to）**
- retreat [4]: retreat v. （軍隊）撤退 → **retreat v. 退到（安靜、安全的地方），躲開**
- adapt [4]: adapt v. 適應（adapt to） → **adapt v. 改編（adapt A into B）**
- supposedly [5]: suppose v. 認為；be supposed to（應該） → **supposedly adv. 據說，據稱**
- cover [1]: cover v. 覆蓋；涵蓋 → **cover v. 採訪，報導（新聞事件）**
- break down [1]: break down phr. （機器）故障；（人）情緒崩潰 → **break down phr. 把……拆解、化約（break down A into B）**
- immediate [3]: immediate adj. 立即的，馬上的 → **immediate adj. 迫在眉睫的，迫切的**
- become [1]: become v. 變成，成為 → **become v. （……的）下場如何，後來怎麼了（what becomes of）**
- aged [1]: aged adj. 年老的（the aged 老年人） → **aged adj. （後接數字）……歲的**
- greet [2]: greet v. 打招呼，問候 → **greet v. （以某種反應）回應，迎接（be greeted with／by）**
- represent [3]: represent v. 代表（某人、某單位） → **represent v. 象徵，表示**
- difficult [1]: difficult adj. 困難的 → **difficult adj. （人）難相處的，難搞的**
- area [1]: area n. 面積，地區 → **area n. （抽象的）方面，地方（areas for improvement）**
- circulate [4]: circulate v. （血液）循環 → **circulate v. （消息、想法）流通，傳開**
- match [2]: match n. 比賽；火柴 → **match v. 相符，一致**
- measure [2]: measure v. 測量 → **measure n. 措施（常用複數）**
- recognition [4]: recognition n. 認出，辨識（face recognition 人臉辨識） → **recognition n. 肯定，賞識**
- disorder [4]: disorder n. （身心的）失調，疾病 → **disorder n. 凌亂，雜亂**
- attend [2]: attend v. 參加，出席 → **unattended adj. 沒人照料的，無人看管的（attend 另一個意思：照料）**
- tell [1]: tell v. 告訴 → **tell v. 分辨，確定**
- chronic [5]: chronic adj. 慢性的（chronic disease 慢性病） → **chronic adj. 長期的，慢性的（不限於疾病）**
- exhausted [4]: exhausted adj. （人）筋疲力盡的 → **exhausted adj. （資源）用光的，耗盡的**
- taste [1]: taste n. 味道，味覺 → **taste n. （個人的）喜好，品味**
- promote [3]: promote v. 升遷；促銷 → **promote v. 提倡，推廣**
- status [4]: status n. 地位，身分 → **status n. 狀態**
- stretch [2]: stretch v. 伸展（四肢），伸懶腰 → **stretch v. （土地、物體）延伸，綿延（stretch for miles）**
- reference [4]: reference n. 參考（a reference book 參考書） → **reference n. 提到，提及（reference to）**
- point to [1]: point to phr. 用手指向，指著 → **point to phr. 顯示可能是，表示（可能有某種情況）**
- ground [1]: ground n. 地面 → **ground n. 根據，理由（on this ground；on the grounds that）**
- dismiss [4]: dismiss v. 讓……離開，下課（dismiss the class） → **dismiss v. 不當一回事，認為不值得考慮而拋開**
- conduct [5]: conduct v. 進行（研究、調查）（conduct a survey） → **conduct v. 指揮（樂團、樂手）**
- succeed [2]: succeed v. 成功（succeed in V-ing） → **succeed v. 接替，繼任（succeed sb as…）**
- turn to [1]: turn to phr. 翻到（第幾頁）；轉向 → **turn to phr. （心情不好時）轉而依賴，求助於**
- bear [1]: bear v. 忍受（can’t bear）； n. 熊 → **bear v. 帶有，具有（名字、記號、相似之處）**
- kind [1]: kind adj. 親切的，仁慈的 → **kind n. 種類，同類（the first of its kind 同類產品中的第一個）**
- head [1]: head n. 頭 → **head v. 朝……前進，前往（head for）**
- note [1]: note n. 筆記； v. 注意 → **noted adj. 著名的，以……出名的（be noted for）**
- regard [2]: regard v. 把……看作（regard A as B） → **regard n. 方面，這一點（in this regard）**
- interest [1]: interest n. 興趣 → **interest n. 利益，好處（in／to the best interest of）**
- content [4]: content [ˈkɑnˌtɛnt] n. 內容 → **content [kənˈtɛnt] adj. 滿足的，甘願的（be content to V／with）**
- hold [1]: hold v. 握著，拿著；舉行（hold a meeting） → **hold v. 認為，主張（hold that）**
- line [1]: line n. 線；隊伍（wait in line） → **line n. 行業，職業（this line of work）**
- upset [2]: upset adj. 難過的，不高興的 → **upset v. 打亂，破壞（原有的平衡、秩序）**
- meet [1]: meet v. 遇見，和……見面 → **meet v. 滿足，達到（需求、期望、標準）**
- pronounced [3]: pronounce v. 發音（pronounced 是它的過去分詞） → **pronounced adj. 明顯的，顯著的**
- bill [2]: bill n. 帳單（pay the bill） → **bill v. 宣傳為，標榜為（bill oneself as）**
- want [1]: want v. 想要 → **want n. 缺乏，不足（for want of）**
- institution [5]: institution n. 機構（educational institutions 教育機構） → **institution n. （由來已久的）習俗，制度**
- chapter [2]: chapter n. （書的）章，回 → **chapter n. （歷史、人生的）一段時期，新的一頁**
- issue [4]: issue n. 議題，問題（safety issues 安全問題） → **issue v. 發行，核發（錢幣、證件）**
- fine [1]: fine adj. 好的；健康的（I’m fine.） → **fine v. 罰款，處以罰金； n. 罰金**
- fair [2]: fair adj. 公平的，公正的 → **fair n. 博覽會，展覽會（book fair）**
- address [2]: address n. 地址 → **address v. 處理，設法解決（問題）**
- rate [3]: rate n. 比率；速度（birth rate 出生率） → **rate v. 評價，評為（rate A as B）**
- order [1]: order v. 點（餐）；命令 → **order n. 整齊，井然有序（in order）**
- pass [1]: pass v. 通過（pass the exam） → **pass n. 山口，隘口（山間的通道）**
- plant [1]: plant n. 植物 → **plant n. 工廠，發電廠**
- scale [3]: scale n. 規模（on a large scale 大規模地） → **scale n. 音階**

## 7. Repeat keys (keyed in two or more papers)

72 entries have been the answer in at least two 詞彙題 across 學測 and 指考 (word forms grouped by 詞彙表 entry). 學 = 學測, 指 = 指考/聯考; years in order. Double entries in 91 and 92 come from the regular and 補考 papers.

anxious [3] (學95/指96/學107), individual [2] (學87/指93/指100), narrow [2] (學91/學95), occasional [4] (指84/學85/學105), recall [4] (指83/指100/學112), resist [3] (指83/學94/學99), amaze(ment) [3] (學96/學109), apparent [4] (指86/學99), average [2] (指83/學100), awake [3] (學86/學99), aware [3] (指84/學106), bare [3] (學103/學112), blush [5] (指90/學111), brief [2] (指88/學100), cancel [2] (學92/學100), commercial [2] (學91), commit [4] (指98/學110), complaint [3] (指82/學84), conscious [3] (指83/學91), considerable [3] (學90/學101), consistent [4] (指100/指110), constant [3] (學88/學102), constructive [4] (學86/指108), courtesy [4] (學85/指96), credit [3] (指109/學113), definite [4] (指83/指89), delight [4] (指86/學100), delivery [2] (學91), demand [4] (指98/學107), disturb [4] (學83/指87), entertain(ment) [4] (指82/學102), equal [2] (學97/指98), explicit [5] (學89/指104), financial [4] (指82/指96), flexible [4] (指86/學104), flock [3] (指84/學102), generosity [4] (指87/學105), interpret [4] (學90/學101), interrupt [3] (指82/學92), necessary [2] (指83/指93), negotiate [4] (指86/學96), objective [4] (學85/學92), observation [4] (學92/學106), original [3] (學85/學95), passive [4] (學86/指95), patient [2] (學84/指86), personal [2] (學85/指93), persuasive [4] (學87/指102), postpone(ment) [3] (學92/學102), potential [4] (學96/學111), preserve [4] (學98/學99), primary [2] (指90/指98), priority [4] (指93/學94), privilege [4] (學88/學97), rare [2] (學94/指107), reckless [6] (指83/指109), recommend [5] (指99/指105), relief [3] (學88/學101), remove [2] (學91), replace(ment) [3] (學94/學102), represent [3] (學86/指92), reveal [3] (指88/指110), suspend [5] (學89/指98), temporary [3] (指91/學92), tight [3] (學99/學115), tolerate [4] (指86/學97), trace [3] (學87/學106), twist [3] (指84/學107), vacant [3] (學94/學114), verbal [5] (指105/學114), visible [3] (學84/學111), vivid [3] (學98/學108)

Most-seen option words (key or distractor, all eras, ≥5 appearances): intimate [4] ×9, dismiss [4] ×8, individual [2] ×8, original [3] ×8, conscious [3] ×7, efficient [3] ×7, flexible [4] ×7, persuasive [4] ×7, confirm [3] ×6, considerate [5] ×6, convince [4] ×6, enormous [4] ×6, estimate [4] ×6, expressive [3] ×6, generous [2] ×6, gradual [2] ×6, hardly [2] ×6, mutual [4] ×6, necessary [2] ×6, objective [4] ×6, occasional [4] ×6, operation [3] ×6, patient [2] ×6, permanent [4] ×6, portable [4] ×6, potential [4] ×6, precise [4] ×6, relieve [4] ×6, temporary [3] ×6, transfer [4] ×6, various [3] ×6, access [4] ×5, amaze(ment) [3] ×5, anxious [3] ×5, apparent [4] ×5, appeal [3] ×5, balance [2] ×5, cautious [5] ×5, connection [2] ×5, contain [2] ×5, contest [4] ×5, convey [4] ×5, credit [3] ×5, definite [4] ×5, demand [4] ×5, depart [4] ×5, display [2] ×5, eliminate [4] ×5, evident [4] ×5, extension [5] ×5, favorable [4] ×5, frequent [3] ×5, inform [3] ×5, inspire [4] ×5, liberal [2] ×5, narrow [2] ×5, noticeable [5] ×5, numerous [4] ×5, optional [5] ×5, promote [3] ×5, regular [2] ×5, reserve [3] ×5, resist [3] ×5, reward [4] ×5, roughly [3] ×5, scarcely [4] ×5, thorough [4] ×5, typical [2] ×5.

## 8. High-yield words across whole 學測 papers

From the repo's frequency count over all 35 學測 papers (83–115, every passage, question and option). Number = how many of the 35 papers the word appears in. Use these for reading-oriented word lists. Many are rarely or never keyed in 詞彙題 and so make good fresh keys for mock items.

- **L4 (most widespread)**: research (22), physical (17), researcher (16), percent (16), issue (16), eventual (15), behavior (14), competition (14), despite (14), communication (13), severe (13), demand (13), impact (12), involve(ment) (12), contrast (12), equip(ment) (12), device (11), establish(ment) (11), popularity (11), professional (11), content (10), injure (10), potential (10), associate (10), moreover (10), adopt (10), essential (10), initial (10), annual (10), furthermore (10), estimate (10), inspire (10), preserve (10), transfer (10), invention (9), route (9), site (9), evidence (9), predict (9), reward (9)
- **L5**: document (9), highlight (9), evolve (9), participant (9), consumption (8), innovative (8), version (7), ceremony (7), extraordinary (7), substitute (7), viewer (6), generate (6), purchase (6), preference (6), conduct (6), facilitate (6), scent (6), series (6), recommend (5), architect (5), destination (5), genetic (5), depress (5), commute (5), executive (5), infect (5), trait (5), beneficial (5), interpretation (5), layer (5), risky (5), stimulate (5), widespread (5), specialist (4), symptom (4), trigger (4), architecture (4), carbon (4), confine (4), initiate (4)
- **L6 (appear, but gloss in generated passages)**: astronaut (5), beforehand (5), originate (5), medieval (4), beverage (4), discomfort (4), accustom (4), disable (4), enhance(ment) (4), fragrance (4), navigate (4), refresh(ment) (4), span (4), accordingly (4), literal (4), mainland (4), glacier (3), hemisphere (3), capsule (3), orphanage (3), aboriginal (3), fable (3), accessory (3), dispose (3), glide (3), graze (3), lighten (3), sociable (3), broaden (3), deem (3)

Coverage of the 詞彙表 by 詞彙題 options (keys and distractors, base form or derivative, 學測 + 指考): L2 26%, L3 30%, L4 **53%**, L5 30%, L6 18%. About 475 L4 and about 700 L5 entries have never appeared in any 詞彙題 option. These are legitimate and untapped for new items. Check level in `vocabulary.md` first.

## 9. Look-alike word sets (拼字相近)

The repo groups 317 spelling-alike sets, each with a root or prefix explanation. These are the classic 詞彙題 distractor families and the 中譯英 spelling-error source. The first 60:

depression／expression／impression／expressive／impressive; conform／inform／perform／reform／transform; intense／intensive／extensive／tense／tentative; mature／manual／mutual; attain／obtain／contain／sustain; command／recommend／comment／demand／cement; assist／consist／insist／persist／resist／exist; content／contest／context／contempt; conserve／preserve／reserve／observe; acquire／inquire／require／request／quest; considerable／considerate; intimacy／intimate; depress／express／impress／oppress／suppress／press; admit／commit／permit／submit／omit／transmit; objection／objective／subjective; expose／impose／compose／dispose／deposit; access／excess／assess／process; distinct／extinct／distinctive; mission／missionary／commission／commitment; propose／purpose／oppose／suppose; effective／efficient; concise／precious／precise; transfer／transform; construction／destruction／instruction; contribution／distribution／tribute; assign／design／resign; conservation／conservative／observation／preservation／reservation; conclude／include／exclusive／inclusive／exclude; literal／literary／literate／liberal; explode／exploit／explore; general／generous; conscience／conscious; adapt／adopt／apt; protect／protest／detect; contract／contrast／contact／contrary; retain／maintain／detain; attribute／contribute／distribute; instance／instant／constant; constitute／institute／substitute／constitution／institution; consent／dissent／resent／present／represent; sensible／sensitive; essence／essential／license／innocence; accent／decent／descent／percent／recent; confirm／conform／affirm; desert／dessert／deserve／insert／assert; patent／patience／patient／potent; abundant／reluctant; primary／primitive; conference／interference／preference／reference; convention／intervention／invention／prevention; serve／deserve／persevere; aspire／expire／inspire; award／reward; consistent／persistent／resistant; disrupt／erupt／interrupt; respectable／respectful／respective; introduce／produce／reduce／induce／seduce; extend／expand; definite／definitive／infinite; though／thorough／through／thought

Use them in two ways: as distractor pools (rule 4), and in 觀念講解, explaining the shared root (press = 壓: de-/ex-/im-press) so the student learns the set rather than one word.

## 10. Notes for advanced students (指考 data)

- 指考 keys are about 43% L5–L6 (vs 20% L5, 0% L6 in 111–115 學測), with heavier abstract vocabulary (minimal, hostile, reckless, explicit, suspend). They make a good stretch set for students already at 8+/10. Say clearly that this exceeds the 學測 scope (考試說明: L1–5 core).
- 指考 repeat keys overlap heavily with 學測 (anxious, recall, resist, occasional, individual). The shared core is the safest L3–L5 study list.
