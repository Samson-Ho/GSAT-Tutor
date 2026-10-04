# GSAT-Tutor

學科能力測驗（學測）家教 Agent Skill。以大考中心〈考試說明〉為最高依據，並以參考試卷、試辦考試與 111–115 學測試題的為出題趨勢參考。

An Agent Skill that tutors students for Taiwan's General Scholastic Ability Test (GSAT), anchored to the official CEEC exam guidelines and calibrated on the 111–115 past papers.

## 目前支援科目
| 科目 | 狀態 |
|---|---|
| 數學A（數A） | Done |
| 自然（物理、化學、生物、地球科學） | Done |
| 國綜、國寫、英文 | TBA |

## 功能
- **觀念講解**：依〈考試說明〉學習內容代碼講解，標示 ※／★／＃ 與備註範圍，並連結歷屆考題。
- **模擬出題**：依學測格式產生單選、多選、選填、混合題、題組或整份模擬卷，附答案、詳解、學習內容代碼與評分原則。
- **非選批改＋弱點診斷**：依大考中心評分原則批改非選擇題，將失分對應到學習內容與測驗目標，並提供讀書計畫。

## 結構
```
gsat-tutor/
├── SKILL.md                    # 路由與工作流程
├── references/
│   ├── math-a/                 # 數A：scope / trends / question-index / item-writing / grading
│   └── science/                # 自然：同上
└── assets/papers/              # 大考中心官方 PDF（考試說明、參考試卷、試辦、111–115 試題＋答案＋評分原則）
```

## 安裝
- Claude Code：將 `gsat-tutor/` 資料夾放到 `~/.claude/skills/`（個人）或專案的 `.claude/skills/`。
- Claude.ai：將資料夾打包為 `.skill` 後上傳。

## 資料來源與著作權
`assets/papers/` 內之考試說明、參考試卷、試辦考試及歷屆試題、答案與評分原則，均取自財團法人大學入學考試中心基金會（https://www.ceec.edu.tw）。


本專案為非官方、非營利的學習工具，與大考中心無隸屬關係。`references/` 中 111–115 學年度試題的學習內容分類與趨勢分析為 GSAT-Tutor 自行整理，非官方資料。GSAT-Tutor 產生的題目皆為模擬題。

## 授權 License
本專案的程式與文件（`SKILL.md`、`references/`、`evals/`、README）採用 [GNU General Public License v3.0](LICENSE) 授權。

`assets/papers/` 內的大考中心 PDF **不適用** GPL-3.0，著作權仍屬財團法人大學入學考試中心基金會，僅供非營利目的使用（見上方「資料來源與著作權」）。

The code and documentation are licensed under GPL-3.0. The CEEC PDFs in `assets/papers/` are excluded: they remain © 大學入學考試中心 and are redistributed for non-commercial use only.
