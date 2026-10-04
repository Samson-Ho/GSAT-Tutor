# 自然 — Item Writing Spec

Follow this exactly when generating 自然 practice items. The goal: an item a 大考中心 reviewer would accept as 學測-style. That means 必修 scope, a 素養 context, data the student can read, and unambiguous answers.

## 1. Universal rules
- **Scope**: each item maps to 學習內容 codes in `scope.md` (and/or 探究與實作 items). Anything beyond 必修 must be fully supplied in the stem (a formula, a definition, a constant), and the item must test reasoning with it, not prior knowledge of it.
- **Constants and data in the stem**: give h, c, e, g, atomic masses, densities, conversion factors (1 eV = 1.6×10⁻¹⁹ J, 1 度 = 1 kWh = 3.6×10⁶ J) as needed. No formula sheet exists.
- **Numbers by hand**: choose values that make the arithmetic clean or order-of-magnitude.
- **Figures and tables**: real items lean heavily on figures. In text output:
  - prefer **Markdown tables** for data (as in 表1 / 表2 of real papers);
  - for graphs, either give the data table plus a short description ("圖1為…隨…的變化"), or a simple ASCII/SVG sketch labelled 「示意圖」;
  - every quantity a student needs must be readable from what you provide.
- **Numbering in Chinese style**: 圖1, 表1; 題組 header 「37-39題為題組」.
- **Language**: 繁體中文, official phrasing. Typical stems: 「下列敘述哪些正確？（應選2項）」「下列何者正確？」「下列何者錯誤？」「最可能的原因為何？」.

## 2. 單選題 (2分)
```
5. ［情境或題幹］下列何者正確？
(A) …
(B) …
(C) …
(D) …
(E) …
```
- Five options (A)–(E), exactly one correct.
- Negative stems (錯誤／不正確／最不可能) are fine, but put the negative word in the stem and make it obvious (real papers bold it).
- Combination format is allowed: 「下列甲～戊的敘述，正確的為何？ (A)甲乙 (B)乙丙 …」 or 「(A)只有甲 (B)只有乙 … (G)甲乙丙均正確」.

## 3. 多選題 (2分)
```
6. ［題幹］下列哪些選項正確？（應選2項）
(A) …
(B) …
(C) …
(D) …
(E) …
```
- **Always state 「（應選 n 項）」**, with n = 2 or 3 (occasionally 4). The answer key must contain exactly n options.
- Composite forms, when the content has two or three dimensions:
  - 「（應選2項，A至C選1項、D至F選1項）」 with (A)–(F) in two groups;
  - 「（應選3項，甲、乙、丙三欄各選1項）」 laid out as a 3-column table.
- Each option independently and definitely true or false; avoid compound options where one half is true and the other false, unless that is the deliberate trap.

## 4. 題組 (Part 2) and mini-groups (Part 1)
```
37-40題為題組
［文本 200–600 字：情境、研究背景、實驗步驟或數據；圖/表編號］
37. …（應選2項）（2分）  ← Part 2 選擇 items show （2分）
38. …（2分）
39. ［非選擇題］…（4分）
40. …
```
- Part 2 題組: 3–6 items; at least one 非選 (2 or 4 分); point values in parentheses at the end of each item.
- A good 題組 progresses: (1) read and understand the text or data → (2) apply a concept → (3) analyse or infer (探究) → (4) express or justify (非選).
- **Cross-discipline** where natural: e.g. a Doppler blood-flow device (物＋生), lake-core lead isotopes (物＋地), photocatalysts (物＋化), enzyme kinetics (化＋生).
- Hooks: a recent Nobel Prize, a current event, a Taiwan context, a classroom 探究與實作 experiment. Keep the facts in the passage accurate; if unsure of a real-world detail, make the scenario explicitly hypothetical ("假設…").
- Part 1 mini-groups (2 questions sharing a stem) follow the same header style, e.g. 「11-12題為題組」.

## 5. 非選擇題 designs (pick formats from `trends.md` §4)
- State exactly what to produce and any constraints: 「（限30字以內）」「須寫出計算過程」「係數以最簡整數表示」「請標出兩坐標軸的名稱與單位」.
- For **作圖**, specify the axes or the grid the answer sheet provides, which points to plot, and whether a trend line or extrapolation is required.
- For **說明**, make the expected reasoning chain short and checkable (2–3 key ideas), so a rubric can score it.
- For **計算**, design so the 列式 and the 答案 can be scored separately.
- For a **table to fill** (變因、預期現象), give the column headers and pre-fill some cells as in 113-43.

## 6. Answer key and 詳解 format
Mirror the official 參考試卷／試辦 試題解析:
```
試題編號：38
參考答案：(B)(E)
測驗內容：必修物理 PKa-Vc-2 定性介紹都卜勒效應及其應用。
測驗目標：2c.根據文本、數據、式子或圖表等資料作解釋、比較、推論、延伸或歸納
          3b.根據科學定律、模型，解釋日常生活現象或科學探究情境
學習表現：探究能力－問題解決 pa-Vc-2（可省略）
試題解析：
1. 本題測驗考生…
2. 各選項說明如下：
(A) …（錯誤原因）
(B) …
3. 綜合上述分析，本題正確答案為(B)(E)。
```
- For every 選擇題, explain each option.
- For 非選, give 滿分參考答案 + 評分原則 (`grading.md` §3).

## 7. Self-check before showing any item
1. Codes listed; content within 必修, or anything else fully supplied in the stem?
2. 多選: does the answer contain exactly the stated 應選 n 項?
3. Every option's truth value is certain from 必修 knowledge plus the stem?
4. Data and figures contain everything needed; units given; numbers hand-friendly?
5. Answer solved twice (or computed with code if available)?
6. Real-world facts in the passage accurate, or the scenario marked hypothetical?
7. 非選 rubric scorable (independent points, clear acceptable answers, tolerance ranges for graph reading)?
8. Labelled as GSAT-Tutor 模擬題?
