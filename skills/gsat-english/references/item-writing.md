# 英文 — Item Writing Spec

Follow this exactly when generating 學測英文 practice items. Aim for an item a 大考中心 reviewer would accept: in scope (部定必修, 參考詞彙表 levels 1–5), natural English, one defensible key, formatted like the real paper.

## 1. Universal rules

- **Vocabulary control**: keys and most passage words come from levels 1–5 of `vocabulary.md`. Level-6 or off-list words may appear in passages only if inferable or glossed, and never as a 詞彙題 key. Check passage vocabulary against `vocabulary.md` using the host's text search. With local Python 3 and shell access, optionally run `python3 scripts/vocab_level.py --text passage.txt` from the skill directory. Fix or gloss flagged words; without the helper, do not claim an exhaustive automated check.
- **Passage length**: 180–400 words (考試說明). 綜合 passages are about 200–250 words; 閱讀 passages 300–400.
- **Authentic register**: expository or informational prose like news, magazines or popular science. Write original passages and label them 「GSAT-Tutor 自編」. Don't present invented facts as real: when a passage is about a real topic, stick to well-established facts, or say it is adapted or fictionalized.
- **American spelling** (the 詞彙表 standard).
- **Format**: instructions and section headers in Chinese, as on the real paper (說明︰第1題至第10題，每題1分。); items in English.

## 2. 詞彙題 (1分 each)

```
1. When Jeffery doesn't feel like cooking, he often orders pizza online and has it ______ to his house.
(A) advanced (B) delivered (C) offered (D) stretched
```
- One sentence and four single-word options of the **same part of speech and form**. Distractors at similar levels.
- Key mostly L3–L5. A collocation or cause–effect clue must be in the sentence, so the key is the only option that fits both meaning and collocation.
- Mix in -ly adverbs, derived adjectives and nouns, and occasionally a common word in a secondary sense (stand the test of time; the bus is due).

## 3. 綜合測驗 (1分 each, 2 × 5 blanks)

```
第 11 至 15 題為題組
<passage with   11   …   15   >
11. (A) … (B) … (C) … (D) …
```
- Per passage: about 2 lexical, 1–2 grammar (tense, participle, voice, relative clause), and 1–2 discourse items (transitions, phrases, topic-sentence key words).
- Grammar options should be forms of one verb (Have / Had / Having / Having been).

## 4. 文意選填 (1分 each, 10 blanks)

```
第 21 至 30 題為題組
<passage with   21   …   30   >
(A) possible (B) sensation (C) risky (D) cost (E) witnessed
(F) professional (G) called for (H) tried out (I) necessity (J) career
```
- 10 options for 10 blanks, each used once. Options are already in their final form (witnessed, called for), in mixed parts of speech: about 3 nouns, 3 verbs or phrasal verbs, 2–3 adjectives, 1 adverb or other.
- Every blank needs **both** grammatical and semantic fit. Check that no option fits two blanks equally well.

## 5. 篇章結構 (2分 each, 4 blanks, **5 options**)

```
第 31 至 34 題為題組
<passage with   31  …   34   (sentence-sized blanks)>
(A) … (B) … (C) … (D) … (E) …
```
- Since 115: **5 options, 4 used**. The distractor is on-topic but breaks reference or logic (wrong pronoun referent, wrong time frame, contradicts the next sentence).
- Blanks test: the passage's thesis sentence, a paragraph topic sentence, a within-paragraph link, and an inter-paragraph transition or conclusion.
- Each option must have a **cohesive hook** (this, such, another, however, these hotels) that fits only one blank.

## 6. 閱讀測驗 (2分 each, 3 passages × 4 items)

```
第 35 至 38 題為題組
<passage 300–400 words>
35. What is this passage mainly about?
(A) … (B) … (C) … (D) …
```
- Four options, one key. Per passage, mix 4 different item types (`trends.md` §4): main idea or question answered, detail, inference, vocabulary or idiom in context, reference (it/this/them), purpose or organization, sentence insertion, sequence, picture or map matching, NOT-mentioned, fact vs opinion.
- At least one item per paper should use **a picture, table or map**. In text output, describe the options (e.g. "(A) a light with red above green, mounted on a pole…") or give a simple table.
- Distractors: true but irrelevant, true for another part of the text, exaggerated (always, all, only), reversed cause.

## 7. 混合題 (10分, default 112–115 format)

```
第貳部分、混合題（占 10 分）
說明︰本部分共有1題組，每一子題配分標於題末。限在答題卷標示題號的作答區內作答……

第 47 至 50 題為題組
<multi-voice or parallel text: forum posts A–J, two profiles, store listings A–F, two species …>

47-48 下列簡短敘述摘記上方文章重點。請從文章中找出最適當的單詞（word）填入下列句子空格中，並視句型結構需要做適當的字形變化，使句子語意完整、語法正確，並符合全文文意。每格限填一個單詞（word）。（填充題，4分）
<summary sentence with   47   and   48  >
49. From (A) to (F) …, which ONES …?（多選題，4分）
50. Which phrase in the … means "…"?（簡答題，2分）
```
- 47–48: the answer word must appear in the passage in **another form** (participate → participating; confine → confined; innovative → innovation), so the form change is tested.
- 49: 6–10 options; the key has 2–4 correct.
- 50: a 2–4-word phrase from the text matched to a paraphrased definition.
- Provide the key with accepted alternatives and the official 2/1/0 rule (`grading.md` §3).

## 8. 中譯英 (2 × 4分)

```
一、中譯英（占 8 分）
說明：依題號將以下中文句子譯成正確、通順、達意的英文。每題4分，共8分。
1. ……
2. ……
```
- Two **linked** sentences on one current topic, each 18–30 Chinese characters.
- Each sentence centres on **one key structure** (passive, present perfect, relative clause, participial construction, comparison or superlative, not…but…, as long as, it is…that…) and 4–6 target words at levels 1–4.
- Answer key: one model translation with alternatives in braces, the list of target words, the structure, and the four official deduction rules.

## 9. 英文作文 (20分)

```
二、英文作文（占 20 分）
說明︰依提示寫一篇英文作文，文長至少120個單詞（words）。
提示︰<context>。請……寫一篇英文作文，文分兩段。第一段……；第二段……。
<pictures described in words or as a simple layout>
```
- Default to **看圖寫作 with two paragraphs**: P1 describe the picture(s) or phenomenon; P2 explain, evaluate, choose or solve. Variants: 信函 (with a given signature name, not the student's real name) and 主題寫作.
- Topics from teen life and social trends; no specialist knowledge.
- Provide: the four-part rubric (`grading.md` §1.1), a prompt-specific checklist, a sample outline and, on request, a 150–200-word model labelled 「GSAT-Tutor 範文（非官方）」.

## 10. Output and self-check

Output per item: 題目 → separator → 參考答案 → 測驗目標 (T1–T8) → 解析 (the clue in the text, why the distractors fail; give a Chinese gloss for each option in 詞彙題, as the official 解析 does) → for words, the 詞彙表 level. Label everything **GSAT-Tutor 模擬題**.

- [ ] Keys verified by re-solving; exactly one defensible answer (or the stated set for 多選).
- [ ] 詞彙題 options share part of speech and form; key level 2–5 (run `scripts/vocab_level.py` on the options).
- [ ] Passage within 180–400 words; flagged level-6 or off-list words glossed or replaced.
- [ ] 文意選填: 10 options, 10 blanks, no double fits. 篇章: 5 options, 4 blanks, one plausible distractor.
- [ ] 混合 47–48 require a form change; 50's phrase appears verbatim in the text.
- [ ] 中譯英 has one clear key structure per sentence and a full model answer.
- [ ] 作文 prompt specifies both paragraphs' content and ≥120 words.
