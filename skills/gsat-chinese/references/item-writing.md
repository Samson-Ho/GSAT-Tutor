# 國綜 — Item Writing Spec

Follow this when generating 國綜 practice items. Aim for an item a 大考中心 reviewer would accept: in scope (部定必修), tagged with 測驗目標, unambiguous, answerable from the text plus 必修-level knowledge, and formatted like the real paper.

## 1. Universal rules

- **Scope**: 部定必修 only (`scope.md`). Knowledge unique to 加深加廣選修 (國學常識 etc.) must be supplied in the stem.
- **Tag every item** with 1–3 測驗目標 codes (A1–A6, B1–B5).
- **Material**:
  - Real texts need accurate quotation and attribution in the official style: 「（改寫自林文月〈京都的庭園〉）」 or 「（王充《論衡》）」. **Never fabricate a quotation and attribute it to a real author or classic.** If you are not certain of a classical passage's exact wording, either write a self-composed passage labelled 「GSAT-Tutor 自編」 or tell the user to verify the text.
  - Self-written modern passages are fine for informational and cross-field 題組. Label them 「GSAT-Tutor 自編素材」.
  - Add 注釋 (e.g. 「醅：沒過濾的酒。」) for rare classical words, as real papers do.
- **文言／白話 balance**: about 35–45% 文言 across a mock paper.
- **Language**: 繁體中文, official phrasing. Typical stems: 「下列……，最適當的是：」「……敘述適當的是：」 (多選); 「依據上文，……」; 「關於①、②是否符合上文……，最適當的研判是：」; 「下列「」內的字，讀音前後相同的是：」.

## 2. 單選題 (2分)

```
5. ［題幹］最適當的是：
(A) ……　(B) ……
(C) ……　(D) ……
```
- **Four options (A)–(D)**, exactly one correct. Use 「最適當」 (best) or 「不適當」／「最不可能」 (negative stems: bold or space the negation, as in 「最 不適當」).
- Distractors should be plausible misreadings: right detail with the wrong cause, overgeneralization (總是、皆、完全), reversed relation, a statement true in the world but not supported by the text.
- **①② 研判 format**: list two (or three) statements, then options like `(A)①、②皆符合 (B)①、②皆不符合 (C)①符合，②不符合 (D)①不符合，②無法判斷`. Include 「無法判斷」 options when the text is silent, and make sure your key respects that distinction.

## 3. 多選題 (4分)

```
26. ［題幹］，適當的是：
(A) ……
(B) ……
(C) ……
(D) ……
(E) ……
```
- **Five options (A)–(E)**, **at least one** correct. 111–115 keys have 2–4 correct. Don't state how many to choose: 國綜 doesn't.
- Every option must be decidable as clearly true or clearly false from the text or from 必修 knowledge.
- Standard types:
  - **字義**: 「下列各組「」內的詞，意義前後相同的是：」. Five pairs of textbook or classical sentences.
  - **成語／詞語運用**: 「下列文句畫底線的詞語，運用適當的是：」. Modern sentences, some with a misused idiom.
  - **語法 by example**: define the pattern in the stem with one example (e.g. 「以」 after an action shows purpose: 「保持距離，以策安全」), then five sentences.
  - **Reading multi-select** on a passage or a set of data.

## 4. 題組

- Header: 「6-8為題組。閱讀下文，回答 6-8 題。」 Paired texts are labelled 甲、乙 (丙、丁), with an attribution under each.
- 2–3 items per 題組 (up to 5 for a rich text), each testing a different 目標: e.g. B1 detail → B2 inference → B3 application or B4 form.
- **Application items** are the modern signature: an app, game, exhibition, lesson, itinerary or citation task that applies the text (112-17, 113-15, 114-8, 114-31, 115-13).
- **Non-continuous material**: tables, right-hand boxes (右框) and simple diagrams. In text output, render tables in Markdown and describe any image in words.

## 5. 混合題 (第貳部分, default 24分 in 1 題組)

```
第貳部分、混合題或非選擇題（占 24 分）
說明：本部分共有1題組，選擇題每題2分，非選擇題配分標於題末。……非選擇題請由左而右橫式書寫。

32-36為題組。閱讀甲、乙、丙文，回答 32-36 題。
（甲：概念性文本；乙、丙：可套用概念的文學作品或真實材料）
32. 請依據甲文，回答下列問題：
（1）……？（占 2 分，作答字數：10字以內。）
（2）……？（占 4 分，作答字數：30字以內。）
33. ……（占 2 分，單選題）
……
```
- Design around **one concept** from 甲 applied to the other texts (回憶 113; 概念框架 114; 女性聲音 115).
- Non-choice sub-items: **2分** = locate or copy a term or phrase (one right answer); **4分** = explain a reason, apply the concept, or answer a two-part 「基於……，因此……」 question. Give a 作答字數 limit (10/15/20/30/40字).
- Include 1–2 單選 (2分) for ①② or ①②③ 研判 or 最適當的解讀.
- Total 24 = e.g. 非 6 + 非 6 + 單 2 + 單 2 + 非 6, or 非 6 + 非 6 + 非 8 + 單 2 + 單 2. Check that the sum is right.
- For each 非選 sub-item, write a **滿分參考答案** (with 「或：」 alternatives) and a 評分原則 in the official tiers (`grading.md`).

## 6. Output per item

題目 → separator → 參考答案 → 測驗目標 → 解析 (why the key is right and why each distractor is wrong; for 字音／字義 give every option's reading or meaning, as the official 試題解析 does). Add 評分原則 for 非選. Label everything **GSAT-Tutor 模擬題**.

## 7. Self-check before shipping

- [ ] Each item has 測驗目標 code(s) and stays within 部定必修.
- [ ] Quotations are verbatim and correctly attributed, or labelled 自編. No invented classics.
- [ ] 單選: 4 options, exactly one defensible answer. 多選: 5 options, each clearly true or false, at least one true.
- [ ] 字音 items: verify every reading (注音). 字形 items: exactly one fully correct sentence. 字義 items: give each meaning.
- [ ] ①② items: the key distinguishes 不符合 from 無法判斷 correctly.
- [ ] 混合題 points add up; every 非選 has 參考答案 and 評分原則; 字數 limits are realistic for the answer.
- [ ] 文言 share and topic mix follow `trends.md` §5 for full papers.
