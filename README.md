# GSAT-Tutor

學科能力測驗（學測）家教插件，提供 Claude 與 OpenAI 共用的五科技能。以大考中心〈考試說明〉為最高依據，並以參考試卷、試辦考試與 111–115 學測試題為趨勢參考。

A portable skills-only plugin for Taiwan's General Scholastic Ability Test (GSAT), with shared skills for Claude and OpenAI hosts. Anchored to official CEEC exam guidelines and calibrated on the 111–115 past papers. Independent of CEEC, OpenAI, Anthropic, universities, and government agencies.

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

## Use with ChatGPT on iPhone / iPad / Web

**此 repository 已準備可上傳的套件格式；本文件不宣稱 GSAT-Tutor 已在公開目錄上架。**
維護者仍須在 OpenAI 的 universal Plugin Directory 完成提交、審核通過與發布。
GitHub push 或本機安裝不會完成此步驟，這也不是 Custom GPT／GPT Store。

正式發布後，在支援 Plugins 的 ChatGPT 網頁、iPhone 或 iPad 版本中：

1. 開啟 ChatGPT，進入 **Plugins**。
2. 搜尋 **GSAT-Tutor**，開啟詳情並安裝。
3. 開啟對話，選取插件或使用起始提示。

此路徑不需要 clone GitHub，也不需要手動加入 Claude marketplace。
是否可見仍受帳號、地區、組織設定及客戶端支援影響；發布後須逐一實測。

## Use with ChatGPT Desktop / Codex locally

既有本機市集流程保留，與公開目錄發布互相獨立。
`.claude-plugin/marketplace.json` 仍是原本的相容市集，名稱為
`gsat-tutor-marketplace`，唯一插件來源為 repository root (`source: "./"`)。
ChatGPT Desktop 支援此 legacy-compatible catalog，詳見
[OpenAI 套件文件](https://developers.openai.com/plugins/build/plugins)。

### ChatGPT Desktop

1. 在支援本機市集的 ChatGPT 桌面版本，進入 **Plugins → Add → Add marketplace**。
2. 貼上 `https://github.com/Samson-Ho/GSAT-Tutor`，依提示載入。
3. 在 **gsat-tutor-marketplace** 找到 **GSAT-Tutor 學測家教** 並安裝。
4. 開啟新對話，選取插件或輸入 `@GSAT-Tutor`。

不要將桌面版「加入 GitHub 市集」當成 iPhone／iPad／Web 的公開安裝流程。

### Codex

```sh
codex plugin marketplace add Samson-Ho/GSAT-Tutor
codex plugin add gsat-tutor@gsat-tutor-marketplace
```

## Use with Claude Code

原有 GitHub marketplace 安裝指令不變，無須遷移到 OpenAI：

```sh
/plugin marketplace add Samson-Ho/GSAT-Tutor
/plugin install gsat-tutor@gsat-tutor-marketplace
```

### Claude App
1. 在 [claude.ai](https://claude.ai) 網頁或 Claude 桌面版打開 **Customize › Plugins**。
2. 點 **Add › Add marketplace › Add from a repository**，貼上 `Samson-Ho/GSAT-Tutor`（或 `https://github.com/Samson-Ho/GSAT-Tutor`）。
3. 同步完成後，在 **Discover** 找到 **GSAT-Tutor 學測家教**，點 **Add**。

插件裝在你的帳號上，之後在手機與 iPad 的 Claude App 對話中也能直接使用；使用對話框左側加號，選擇plugin中的 GSAT-Tutor 即可觸發。（新增插件的步驟請在網頁或桌面版完成。）

## For maintainers: publish to OpenAI

完整步驟見 [OpenAI submission guide](https://github.com/Samson-Ho/GSAT-Tutor/blob/main/docs/OPENAI_SUBMISSION.md)
（repository 內的 `docs/OPENAI_SUBMISSION.md`）。先在開發環境安裝 `requirements-dev.txt`，再執行：

```sh
python3 scripts/validate_plugin.py
python3 -m unittest discover -s tests -v
python3 scripts/build_openai_plugin.py
```

產物：`dist/gsat-tutor-openai-1.2.0.zip`（不提交到 Git）。
根目錄 `plugin.json` 為 OpenAI 可攜式入口；OpenAI metadata 放在
`extensions.com.openai`。不需要新增 `.codex-plugin/plugin.json` 或另一份 marketplace。
五科技能共用，核心家教不需要本機 shell、Python、MCP、OAuth 或後端；
英文詞彙 script 和 PDF 轉換工具僅為可選的本機輔助。
無法讀取原題圖像或完整評分原則時，請提供相關片段，評分會清楚標示估計。

隱私與支援：[PRIVACY.md](PRIVACY.md)、[SUPPORT.md](SUPPORT.md)。
維護者須先公開隱私政策並確認可存取，再把實際 HTTPS URL 填入 listing。
送審、身分驗證、政策聲明、審核與發布均由維護者在 OpenAI dashboard 完成。

## 結構
每個科目是一個獨立的 skill，內容互不影響：

```
GSAT-Tutor/
├── plugin.json                  # OpenAI portable manifest（含 extensions.com.openai）
├── assets/icon.png              # 原創 listing / composer 圖示
├── docs/OPENAI_SUBMISSION.md     # 維護者發布指南
├── scripts/                     # 驗證與可重現 ZIP 建置（開發用）
├── PRIVACY.md
├── SUPPORT.md
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
本專案的程式與文件（manifests、原創圖示、scripts、tests、`skills/*/SKILL.md`、`skills/*/references/`、`evals/`、README 及專案文件；下列例外除外）採用 [GNU General Public License v3.0](LICENSE) 授權。

`skills/*/assets/papers/` 內的大考中心 PDF 與 `skills/gsat-english/references/vocabulary.md`（參考詞彙表轉錄）**不適用** GPL-3.0，著作權仍屬財團法人大學入學考試中心基金會，僅供非營利目的使用（見上方「資料來源與著作權」）。

The code and documentation are licensed under GPL-3.0. The CEEC PDFs in `skills/*/assets/papers/` and the transcribed CEEC vocabulary list (`skills/gsat-english/references/vocabulary.md`) are excluded: they remain © 大學入學考試中心 and are redistributed for non-commercial use only.
