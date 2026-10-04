# GSAT-Tutor

學科能力測驗（學測）家教插件（Claude Plugin／Agent Skill）。以大考中心〈考試說明〉為最高依據，並以參考試卷、試辦考試與 111–115 學測試題的為出題趨勢參考。

A Claude plugin (and portable Agent Skill) that tutors students for Taiwan's General Scholastic Ability Test (GSAT), anchored to the official CEEC exam guidelines and calibrated on the 111–115 past papers.

## 目前支援科目
| 科目 | 狀態 |
|---|---|
| 數學A | Done |
| 自然 | Done |
| 國綜、國寫、英文 | TBA（之後以獨立 skill 加入） |

## 功能
- **觀念講解**：依〈考試說明〉學習內容代碼講解，標示 ※／★／＃ 與備註範圍，並連結歷屆考題。
- **模擬出題**：依學測格式產生單選、多選、選填、混合題、題組或整份模擬卷，附答案、詳解、學習內容代碼與評分原則。
- **非選批改＋弱點診斷**：依大考中心評分原則批改非選擇題，將失分對應到學習內容與測驗目標，並提供讀書計畫。

## 安裝

### Claude App（網頁、桌面、手機、iPad）
需付費方案（Pro、Max、Team、Enterprise）。
1. 在 [claude.ai](https://claude.ai) 網頁或 Claude 桌面版打開 **Customize › Plugins**。
2. 點 **Add › Add marketplace › Add from a repository**，貼上 `Samson-Ho/GSAT-Tutor`（或 `https://github.com/Samson-Ho/GSAT-Tutor`）。
3. 同步完成後，在 **Discover** 找到 **GSAT-Tutor 學測家教**，點 **Add**。

插件裝在你的帳號上，之後在手機與 iPad 的 Claude App 對話中也能直接使用；直接說「幫我出一題學測數A」即可觸發。（新增插件的步驟請在網頁或桌面版完成。）

### Claude Code
```
/plugin marketplace add Samson-Ho/GSAT-Tutor
/plugin install gsat-tutor@gsat-tutor-marketplace
```

### ChatGPT
ChatGPT 無法直接從 GitHub 連結安裝，但支援相同的 SKILL.md 格式：
1. 到 [Releases](https://github.com/Samson-Ho/GSAT-Tutor/releases/latest) 下載需要的科目：`gsat-math-a-skill.zip`（數A）、`gsat-science-skill.zip`（自然）。
2. 在 ChatGPT 打開 **Skills › Create › Upload from your computer**，逐一上傳。

## 結構
每個科目是一個獨立的 skill，內容互不影響：

```
GSAT-Tutor/
├── .claude-plugin/
│   ├── plugin.json             # 插件資訊
│   └── marketplace.json        # 讓此 repo 可作為 marketplace 加入
├── skills/
│   ├── gsat-math-a/            # 數A
│   │   ├── SKILL.md
│   │   ├── references/         # scope / trends / question-index / item-writing / grading
│   │   └── assets/papers/      # 大考中心官方 PDF（考試說明、參考試卷、試辦、111–115 試題＋答案＋評分原則）
│   └── gsat-science/           # 自然（同上結構）
└── evals/                      # 測試案例
```

## 資料來源與著作權
`skills/*/assets/papers/` 內之考試說明、參考試卷、試辦考試及歷屆試題、答案與評分原則，均取自財團法人大學入學考試中心基金會（https://www.ceec.edu.tw）。


本專案為非官方、非營利的學習工具，與大考中心無隸屬關係。`references/` 中 111–115 學年度試題的學習內容分類與趨勢分析為 GSAT-Tutor 自行整理，非官方資料。GSAT-Tutor 產生的題目皆為模擬題。

## 授權 License
本專案的程式與文件（`.claude-plugin/`、`skills/*/SKILL.md`、`skills/*/references/`、`evals/`、README）採用 [GNU General Public License v3.0](LICENSE) 授權。

`skills/*/assets/papers/` 內的大考中心 PDF **不適用** GPL-3.0，著作權仍屬財團法人大學入學考試中心基金會，僅供非營利目的使用（見上方「資料來源與著作權」）。

The code and documentation are licensed under GPL-3.0. The CEEC PDFs in `skills/*/assets/papers/` are excluded: they remain © 大學入學考試中心 and are redistributed for non-commercial use only.
