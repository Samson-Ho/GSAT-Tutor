# 國寫 — Task Writing Spec

Follow this when generating 國寫 practice tasks or mock papers. Aim for a task a 大考中心 reviewer would accept: reading-and-writing combined, a concrete task, no specialist knowledge, gradable with a 三等六級 rubric.

## 1. Universal rules

- **Two 大題, two abilities**: 第一大題 tests 知性的統整判斷; 第二大題 tests 情意的感受抒發. Don't mix them: an opinion essay is 知性, a personal-experience essay is 情意.
- **Material**: 「試題素材上限設為 800 字」. Text, 圖表, 圖片 or 照片. Cross-field topics are welcome (人文、社會、自然), but 「不涉及艱深或專業的學科知識」. Every concept the task uses must be explained inside the material.
- **Write original material, or adapt it with a clear attribution** (「改寫自……」 as the real papers do). Never present invented quotations as real ones by real people. If you write a passage yourself, label it 「GSAT-Tutor 自編素材」.
- **Give a concrete writing task**: name the title (「請以『……』為題」) and list the required content components (2–3) in the prompt. The rubric will grade exactly those components.
- **Set limits explicitly**: 問題（一） 「文長限 80 字以內（至多 4 行）」; 問題（二） 「文長限 400 字以內（至多 19 行）」; 情意 「文長不限」 (one answer-sheet side = 38 行 × 22 格).
- **Language**: 繁體中文, official phrasing. Typical verbs: 依據上文，說明／歸納／分析／比較; 請寫一篇短文，舉例說明你對……的看法; 闡述……的正、負面影響; 表明你贊成或反對，並提出理由; 結合生活經驗或見聞，書寫你的感思與體悟.

## 2. 第一大題（知性）template — default since 111

```
一、
（素材：一或兩篇短文，可含圖表；合計 ≤ 800 字；標明出處或「GSAT-Tutor 自編素材」）

請分項回答以下問題。
問題（一）：依據上文，說明……（2–3 個可由文本找到的要素）。文長限 80 字以內（至多 4 行）。（占 4 分）
問題（二）：……（延伸到生活或社會：舉例＋看法／正負面影響／比較並說明傾向／贊成或反對並說明理由／提出對策）。
            文長限 400 字以內（至多 19 行）。（占 21 分）
```

Design checks:
- 問題（一） must have a **determinate answer in the material**, so a reader can list the 參考答案要點. Questions that only invite opinion don't belong here.
- 問題（二） must **use the material's concept** and still need the student's own thinking. Avoid prompts answerable by restating the material.
- Prefer two required components in 問題（二） (e.g. 「舉例說明……，並提出你的看法」). Three is the maximum.
- Balanced issues only. Where a position is asked for, both sides must be defensible (a 鄰避／被遺忘權 kind of issue, not a moral no-brainer).

## 3. 第二大題（情意）template — default since 111

```
二、
（素材：散文片段／詩／科普短文／圖像，提供一個意象或隱喻；≤ 800 字）

（承接素材的一兩句引導）請以「……」為題，寫一篇文章，結合生活經驗或見聞，
書寫……（1–3 項內容要求，例如：原因、轉變、體悟）。文長不限。（占 25 分）
```

Design checks:
- The title must be **open enough for every student** to have an experience to write about: no special backgrounds, no trauma prompts, nothing that disadvantages students without particular resources.
- The material should offer a **transferable image** (縫隙、52赫茲、氣味、隔閡) that rewards turning the literal into the personal.
- State the content components when the task needs structure (115: 原因＋換位思考＋回應). Leave them out for imaginative prompts (114: 抒發想像).

## 4. Variant formats (參考試卷; use when asked for 變化題型)

| Variant | Template | Rubric note |
|---|---|---|
| 知性 25分 with 自訂題目 (漫畫解讀) | 解讀圖像寓意＋闡述看法，請自訂題目（須與寓意相關），文長限 500 字以內（至多 23 行） | 未訂定題目至多 B+（17分） |
| 情意 7+18 | 問題（一） 文本分析 100–150 字（至多 5–7 行）7分; 問題（二） 以……為題的抒情文 18分 | 18分 bands A+ 18–16 … C 3–1 |
| 情意 narrative from a picture (炙艾圖) | 觀察畫面細節，想像情境，以畫中人物寫故事，須有角色、對白、情節 | 缺三要素至多 B+（17分） |
| 情意 4+21 (卷三 籠中鳥) | 問題（一） 比較兩文意象 80 字; 問題（二） 相似經驗與感受 | 21分 bands |

## 5. Answer key and rubric (always included)

For each generated task, provide:
1. **測驗目標** (`scope.md` §2), e.g. 「知性的統整判斷能力：1. 解讀分析 2. 思辨見解」.
2. **問題（一） 參考答案要點**, plus one model answer of ≤80字.
3. **評分原則** in official table form (`grading.md` §3), naming the required components in each tier, with standing deductions and any 特殊評分原則.
4. Optional, on request: **寫作提示** for students (審題要點, 可用材料, 結構建議), or a **示範文** labelled 「GSAT-Tutor 示範文（非官方）」. Keep a model essay at a realistic length (問題（二） ≤400字; 情意 600–800字), and don't make it impossibly polished.

## 6. Self-check before shipping

- [ ] Material ≤ 800 字; no specialist knowledge needed; sources attributed or labelled 自編.
- [ ] 第一大題 tests reading → analysis → own view; 第二大題 tests experience → feeling → insight.
- [ ] Every prompt has a title or clear task, required components, a length limit and point values (4/21/25 by default).
- [ ] 問題（一） has a determinate answer, and the 參考答案要點 is listed.
- [ ] The rubric's tiers mention every required component, and the bands add up correctly.
- [ ] Topic is fair to all students; no sensitive personal disclosures required.
- [ ] Labelled 「GSAT-Tutor 模擬題」.
