# 數A — Item Writing Spec

Follow this exactly when generating 數A practice items. The goal: an item a 大考中心 reviewer would accept as 學測-style. That means in scope, unambiguous, solvable by hand with the formula sheet, and formatted like the real paper.

## 1. Universal rules
- **Scope**: every item maps to one or more codes in `scope.md`; no ※ content; respect the 備註 limits (no 兩圓關係, no 3×3 inverse computation, no 綜合除法 by ax−b, …). No 微積分, 圓錐曲線, e/ln.
- **No calculator**: numbers must be hand-friendly. Allowed approximations are only those on the formula sheet: √2, √3, √5, √6, π, log 2, log 3, log 5, log 7.
- **Unambiguous**: one defensible reading of the stem; define any non-standard notation in the stem (as 115-2 defines [a]).
- **Figures**: real items say 「如圖」 with a 示意圖. In text output, either give all needed data in words or coordinates so no figure is required, or include a simple ASCII or SVG sketch plus the sentence 「附圖為示意圖」.
- **Language**: 繁體中文, official phrasing. Typical stems: 「試問…為下列哪一個選項？」「試選出正確的選項。」「則…＝○。（化為最簡分數）」.

## 2. 單選題 (5分)
```
1. ［題幹］試問…為下列哪一個選項？
(1) …　(2) …　(3) …　(4) …　(5) …
```
- Exactly five options (1)–(5), exactly one correct, in increasing numeric order when numeric.
- Distractors come from real mistakes: a sign error, a forgotten case, the wrong formula (e.g. averaging rates), the reciprocal, an off-by-one in counting.

## 3. 多選題 (5分)
```
7. ［題幹］試選出正確的選項。
(1) …
(2) …
(3) …
(4) …
(5) …
```
- Five statements, **at least one** correct; any number from 1 to 5 may be correct. 111–115 answers range from 1 correct (113-9) to 4 correct (114-12); 2 or 3 is most common.
- Each option must be decidable as definitely true or definitely false. Avoid "可能" unless the stem makes possibility the question (e.g. 「試選出…可能的關係式」 in 參考-11, 「試選出不可能是…之選項」 in 111-12).
- Write options that test **different** facets: computation, a property, a boundary case, a converse, a "must vs may" distinction.
- Don't tell the number of correct options. (That is a 自然 convention; 數A never says 應選 n 項.)

## 4. 選填題 (5分, all-or-nothing)
- The answer is entered digit by digit into numbered slots: ○13-1, ○13-2, … Each slot holds one of − ± 0–9.
- Show the answer format in the stem with slot markers, e.g.
  - integer: 「則 n ＝ ○13-1 ○13-2」 (two-digit answer)
  - fraction: 「機率為 ○14-1 ／ ○14-2 ○14-3（化為最簡分數）」, meaning a one-digit numerator over a two-digit denominator
  - radical: 「BC ＝ ○16-1 √○16-2（化為最簡根式）」
  - negative: put a slot where the sign goes, e.g. 「a ＝ ○14-1 ○14-2」 with answer −3 entered as −, 3
  - coordinates/ordered pair: 「(○13-1 ○13-2, ○13-3)」
- Always state 「（化為最簡分數）」 or 「（化為最簡根式）」 when relevant. The answer must fit the slots exactly in simplest form, so the slot count is part of the item design: check it.
- Keep values small enough to avoid arithmetic grind; difficulty should come from the idea.

## 5. 混合題組 (18–20, 15分)
```
第貳部分、混合題或非選擇題（占15分）
說明：本部分共有1題組，單選題每題3分，非選擇題配分標於題末。限在答題卷標示題號的作答區內作答。選擇（填）題與「非選擇題作圖部分」使用2B鉛筆作答…非選擇題請由左而右橫式書寫，作答時必須寫出計算過程或理由，否則將酌予扣分。

18-20題為題組
［共同情境／已知條件］
18. …（單選題，3分）
(1) … (2) … (3) … (4) … (5) …
19. …（非選擇題，6分）  ← or 4分
20. （承19題）…（非選擇題，6分）  ← or 8分
```
- 18 is a scaffold: a quick computation that hands over a key quantity used in 19 and 20.
- At least one of 19/20 asks for **說明／證明** (「試說明…」「試證明…」), not only a number.
- 20 may have two asks (e.g. 「試求…的範圍，並求…的最小值」); split the rubric accordingly.
- Prefer geometry, vectors, space or matrix contexts, as in 111–115 (see `trends.md` §4).
- If drawing is required (作圖), say what must be drawn and that it goes in the 作圖區.

## 6. Answer key and 詳解 format
Mirror the 參考試卷 試題解析 format:
```
試題編號：16
參考答案：3√2
學習內容：G-10-7 三角比的性質
測驗目標：評量正弦與餘弦定理的應用（主要：程序性知識）
試題解析：
1. …
2. …
（若有不合之解，須說明排除理由）
```
- 測驗目標: name one of the six (概念性知識／程序性知識／閱讀與表達／連結能力／推理能力／解決問題) and add a short description like the official 「評量…」.
- For 多選, explain every option, including why each wrong one is wrong.
- For 非選, also give a 評分原則 (see `grading.md` §3).
- Mention an alternative method when one exists (official 解析 often show 【解法一】【解法二】).

## 7. Self-check before showing any item
1. Scope: codes listed? Any ※ or excluded 備註 content? Remove it.
2. Solved twice by two different routes (or verified numerically with code if available)?
3. 單選: exactly one correct option? 多選: each option's truth value certain?
4. 選填: answer fits the slot format exactly, in simplest form?
5. Hand-computable without a calculator, using only formula-sheet constants?
6. Stem complete: no figure-only information, units given, notation defined?
7. Distractors plausible and tied to specific misconceptions?
8. Difficulty matches the request and the slot position (see `trends.md` §6)?
9. Labelled as GSAT-Tutor 模擬題?
