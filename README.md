# GSAT-Tutor

學科能力測驗（學測）家教插件（Claude Plugin／Agent Skill）。以大考中心〈考試說明〉為最高依據，並以參考試卷、試辦考試與 111–115 學測試題的為出題趨勢參考。

A Claude plugin (and portable Agent Skill) that tutors students for Taiwan's General Scholastic Ability Test (GSAT), anchored to the official CEEC exam guidelines and calibrated on the 111–115 past papers.

## 目前支援科目
| 科目 | 狀態 |
|---|---|
| 數學A | Done |
| 自然 | Done |
| 英文 | Done（含高中英文參考詞彙表 6,012 詞完整收錄） |
| 國綜 | Done |
| 國寫 | Done |

## 功能
- **觀念講解**：依〈考試說明〉的學習內容或測驗目標講解（數A／自然標示 ※／★／＃ 與備註範圍；國綜用 A1–B5；英文附詞彙表級數），並連結歷屆考題。
- **模擬出題**：依學測格式產生各科題型（單選、多選、選填、題組、混合題、中譯英、英文作文、國寫知性／情意題）或整份模擬卷，附答案、詳解與評分原則。
- **非選批改＋弱點診斷**：依大考中心評分原則批改非選擇題（含英文作文四項分項評分、中譯英、國寫三等六級），將失分對應到學習內容與測驗目標，並提供讀書計畫。

## 安裝

### Claude App
1. 在 [claude.ai](https://claude.ai) 網頁或 Claude 桌面版打開 **Customize › Plugins**。
2. 點 **Add › Add marketplace › Add from a repository**，貼上 `Samson-Ho/GSAT-Tutor`（或 `https://github.com/Samson-Ho/GSAT-Tutor`）。
3. 同步完成後，在 **Discover** 找到 **GSAT-Tutor 學測家教**，點 **Add**。

插件裝在你的帳號上，之後在手機與 iPad 的 Claude App 對話中也能直接使用；直接說「幫我出一題學測數A」「幫我改這篇英文作文」「這篇國寫幾級分」即可觸發。（新增插件的步驟請在網頁或桌面版完成。）

### Claude Code
```sh
/plugin marketplace add Samson-Ho/GSAT-Tutor
/plugin install gsat-tutor@gsat-tutor-marketplace
```

### ChatGPT App
1. 開啟 ChatGPT App 或 [ChatGPT 網頁版](https://chatgpt.com)，展開 **側邊欄**（手機與 iPad 請點左上角的側邊欄按鈕）。
2. 進入 **插件（Plugins）**，點 **新增（Add）› 新增市集（Add marketplace）**。
3. 在市集來源欄位貼上 GitHub 儲存庫網址：`https://github.com/Samson-Ho/GSAT-Tutor`。
4. 依畫面提示確認新增，等待市集載入。
5. 在新增的 **gsat-tutor-marketplace** 市集中找到 **GSAT-Tutor 學測家教（gsat-tutor）**，開啟插件詳情，點 **安裝（Install）** 或 **＋**。一次安裝即可取得數A、自然、英文、國綜、國寫五科技能。
6. 安裝完成後，開啟 **新對話**，輸入「請用 GSAT-Tutor 幫我出一題學測數A」「幫我改這篇英文作文」或「這篇國寫幾級分」即可開始使用。

### Codex
```sh
codex plugin marketplace add Samson-Ho/GSAT-Tutor
codex plugin add gsat-tutor@gsat-tutor-marketplace
```

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
│   ├── gsat-science/           # 自然（同上結構）
│   ├── gsat-english/           # 英文（另含 references/vocabulary.md 參考詞彙表全文、scripts/vocab_level.py 詞彙級數檢查）
│   ├── gsat-chinese/           # 國綜
│   └── gsat-chinese-writing/   # 國寫
└── evals/                      # 測試案例
```

## 資料來源與著作權
`skills/*/assets/papers/` 內之考試說明、參考試卷、試辦考試及歷屆試題、答案與評分原則，均取自財團法人大學入學考試中心基金會（https://www.ceec.edu.tw）。


本專案為非官方、非營利的學習工具，與大考中心無隸屬關係。`references/` 中 111–115 學年度試題的學習內容／測驗目標分類與趨勢分析為 GSAT-Tutor 自行整理，非官方資料。`skills/gsat-english/references/vocabulary.md` 為大考中心《高中英文參考詞彙表》（111學年度起適用）之逐條轉錄，著作權屬大考中心，同樣僅供非營利使用。GSAT-Tutor 產生的題目皆為模擬題。

## 授權 License
本專案的程式與文件（`.claude-plugin/`、`skills/*/SKILL.md`、`skills/*/references/`、`evals/`、README）採用 [GNU General Public License v3.0](LICENSE) 授權。

`skills/*/assets/papers/` 內的大考中心 PDF 與 `skills/gsat-english/references/vocabulary.md`（參考詞彙表轉錄）**不適用** GPL-3.0，著作權仍屬財團法人大學入學考試中心基金會，僅供非營利目的使用（見上方「資料來源與著作權」）。

The code and documentation are licensed under GPL-3.0. The CEEC PDFs in `skills/*/assets/papers/` and the transcribed CEEC vocabulary list (`skills/gsat-english/references/vocabulary.md`) are excluded: they remain © 大學入學考試中心 and are redistributed for non-commercial use only.
