# Auto Post Blog 🤖📝

[![Python 3.11+](https://img.shields.io/badge/python-3.11+-blue.svg)](https://www.python.org/downloads/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.115+-00a393.svg)](https://fastapi.tiangolo.com)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

**Auto Post Blog** 是一個自動化的 AI 資訊聚合與內容生成系統。每天自動從 9 個前沿資料源（arXiv、HuggingFace、GitHub、Tech Blogs、RSS、Hacker News、Reddit、NewsAPI、ChatPaper）收集最新的生成式 AI 論文與新聞，透過 Rule-based 與 LLM 雙層價值篩選機制，產出高品質的繁體中文「部落格貼文草稿」、「個人 AI 筆記」與「每日精選摘要」。配備完整的 Web Dashboard 供監控、搜尋、收藏與內容管理。

---

## ✨ 核心特色 (Core Features)

- **🔄 全自動化 Pipeline**：收集 (Collect) → 評分 (Score) → 生成 (Generate)，支援排程全自動執行、斷點續做、Web 啟動時自動觸發。
- **🧠 雙層篩選機制**：
  - _Rule-based 預篩_：自動識別頂流研究機構（word boundary 精確匹配）、熱門話題關鍵字與社群指標（GitHub Stars、HF Upvotes）。
  - _LLM 深度評分_：透過大語言模型就「新穎性、影響力、話題性、實用性、部落格適合度」五大維度進行深度計分。
- **📊 跨來源去重**：內建 7 天滑動窗口的 URL 與 Arxiv ID 歷史比對，避免同一篇論文或新聞重複出現。
- **🌐 9 大資料源**：
  - arXiv / ChatPaper API — 每日最新 AI 論文
  - HuggingFace Daily Papers — 社群投票熱門論文
  - GitHub Trending — AI 相關熱門開源專案
  - 精選 AI Tech Blogs — Karpathy、Simon Willison 等
  - 主流科技媒體 RSS Feeds — TechCrunch、OpenAI、Anthropic、Google Research 等
  - Hacker News — Algolia API，依 upvotes 篩選 AI 熱門討論
  - Reddit — r/LocalLLaMA、r/MachineLearning
  - NewsAPI — 主流科技新聞聚合
- **🖥️ 現代化 Web Dashboard**：
  - Dark / Light 主題切換
  - **Dashboard 戰情室**：7 天互動式卡片、趨勢 sparkline、來源分布 mini chart
  - **Pipeline 控制台**：GitLab CI/CD 風格 stage pills（running / done / failed / cancelled），支援逐 stage 重跑、強制停止、即時 log 串流（SSE）
  - **素材庫**：合併 posts + notes，全文搜尋、來源/分數/日期篩選
  - **書籤 & Kanban 待寫清單**：四欄拖曳（已收藏→撰寫中→已完成→已發布），卡片含摘要預覽、Blog Draft badge、tags
  - **主題聚合**：8 個 topic cluster + 14 天趨勢 sparkline
  - **每日摘要**：模板式生成（不需 LLM），Top Picks + Worth Watching
  - **精選 Blog**：人工策展的精選文章（FB 格式）
  - **Settings 頁面**：Web UI 直接調整 LLM、評分、Collectors 所有參數，即時生效
  - **評分列表篩選**：Chip 式來源篩選器，即時過濾

## 🏗️ 系統架構 (Architecture)

```mermaid
graph TD;
    subgraph Data Sources
        Arxiv[arXiv API]
        CP[ChatPaper API]
        HF[HuggingFace Papers]
        GH[GitHub Trending]
        RSS[RSS Feeds]
        Blog[Tech Blogs]
        HN[Hacker News]
        Reddit[Reddit]
        News[NewsAPI]
    end

    subgraph Collection Layer
        Collect[BaseCollector x9]
        Dedup[Single-day + Cross-day Dedup]
    end

    subgraph Scoring Layer
        RuleEngine[Rule-based Pre-filter]
        LLMScore[LLM 5D Scoring]
    end

    subgraph Generation Layer
        PostGen[Blog Post Generator]
        NoteGen[AI Note Generator]
        DigestGen[Daily Digest]
    end

    Arxiv --> Collect
    CP --> Collect
    HF --> Collect
    GH --> Collect
    RSS --> Collect
    Blog --> Collect
    HN --> Collect
    Reddit --> Collect
    News --> Collect

    Collect --> Dedup
    Dedup --> |Raw JSON| RuleEngine
    RuleEngine --> |Top K| LLMScore
    LLMScore --> |Scored JSON| PostGen
    LLMScore --> |Scored JSON| NoteGen
    LLMScore --> |Scored JSON| DigestGen

    PostGen --> |Markdown| output/posts
    NoteGen --> |Markdown| output/notes
    DigestGen --> |Markdown| output/digests
```

---

## 🚀 快速開始 (Quick Start)

### 1. 環境安裝

```bash
# 建立並啟動虛擬環境
python3 -m venv .venv
source .venv/bin/activate

# 安裝核心依賴（含 Web 介面）
pip install -e '.[web]'
```

### 2. 環境變數設定

複製範例設定檔並填入您的 API Key（專案預設使用 OpenRouter 取用外部 LLM）：

```bash
cp .env.example .env
# 編輯 .env 填入：
#   OPENROUTER_API_KEY（必要）
#   NEWSAPI_KEY（選用，啟用 NewsAPI collector 需要）
```

### 3. 微調配置 (Optional)

編輯 `config.yaml` 調整偏好設定，或啟動 Web 後在 `/settings` 頁面直接修改：

- **LLM 模型**（預設 `deepseek/deepseek-r1-0528:free`，可在 Settings 頁面切換）
- **收集器開關**（視需求開關各資料源）
- **評分權重與閾值**
- **去重回看天數** (`dedup.lookback_days`)
- **資料保留天數** (`retention_days`)

---

## 💻 終端機指令 (CLI Usage)

Auto Post Blog 提供完整的命令列介面（基於 Typer），所有核心功能皆可獨立使用。

### 完整執行

```bash
# 完整跑一次：收集 → 篩選 → 生成
python -m src.cli run

# 模擬執行（只收集+評分，不呼叫 LLM 產文）
python -m src.cli run --dry-run

# 指定處理歷史日期
python -m src.cli run --date 2026-02-23

# 強制清除所有快取重跑（含 posts/notes/prompts）
python -m src.cli run --force
```

### 分段執行與管理

```bash
python -m src.cli collect              # 僅執行資料收集
python -m src.cli score                # 僅執行價值評分
python -m src.cli generate --top-k 3  # 僅將最高分的 3 筆生成文章
python -m src.cli summary              # 檢視當日爬取與評分的分佈摘要
python -m src.cli status               # 檢視最近 7 天執行狀態
python -m src.cli list --days 7        # 列出最近 7 天產出的文章清單
python -m src.cli show output/posts/2026-02-28_slug.md  # 在終端機預覽文章
python -m src.cli clean --keep-days 30  # 清理 30 天前的過期資料
python -m src.cli catchup --days 7     # 補跑最近 N 天中遺漏的日期
```

### 每日摘要

```bash
python -m src.cli digest               # 生成今日精選摘要（不需 LLM）
python -m src.cli digest --date 2026-02-28  # 指定日期
```

### 啟動 Web 監控介面

```bash
# 啟動 FastAPI Server（預設 port 8555，啟動時自動觸發當天 pipeline）
python -m src.cli web
```

瀏覽器開啟 `http://127.0.0.1:8555/dashboard` 即可進入系統戰情室。

---

## ⚙️ 動態設定（Settings UI）

啟動 Web server 後，前往 `http://127.0.0.1:8555/settings` 即可在瀏覽器中即時調整所有參數：

| 區塊 | 可調整項目 |
|------|-----------|
| 🤖 LLM 設定 | API Key、Base URL、主力/備援模型、Max Tokens、Request Delay |
| 📊 評分參數 | Rule 門檻、LLM Top-K、Final Top-K、HF Upvote/GitHub Stars 閾值 |
| 🔧 Pipeline 參數 | 去重回看天數、資料保留天數 |
| 🔌 Collector 設定 | 各資料源開關（arXiv、HF Papers、ChatPaper、RSS、Blogs、GitHub、Hacker News、Reddit、NewsAPI）及各自的收集數量與查詢參數 |

所有設定儲存後**即時生效**，下次執行 pipeline 時自動採用新設定。

---

## ⏱️ 自動化排程 (Cron Setup)

系統內建排程腳本，可輕易整合進 Linux 系統排程，實現「每天起床就有整理好的前沿 AI 資訊」。

```bash
chmod +x setup_cron.sh
./setup_cron.sh
```

_註：預設排程設定為每日早上 10:00 執行（配合 HuggingFace Daily Papers 的更新時區）。_

---

## 📂 目錄與輸出結構

Pipeline 產生的所有資料皆按模組劃分，方便溯源與二次開發：

```text
├── data/
│   ├── raw/             # 每日收集的原始資料快取 (JSON)
│   ├── scored/          # 經由 Rule 與 LLM 評分後的結果清單
│   ├── bookmarks.json   # 書籤/收藏清單（含 writing queue 狀態）
│   ├── feedback/        # Web UI 上使用者給予的品質回饋記錄
│   └── health/          # 各 Collector 的爬取成功率與耗時數據
├── output/
│   ├── posts/           # 繁體中文部落格草稿 (Markdown + YAML Frontmatter)
│   ├── notes/           # 條列式重點摘錄的個人 AI 筆記
│   ├── digests/         # 每日精選摘要（模板式，不需 LLM）
│   ├── blogs/           # 精選 Blog 文章（人工策展，FB 格式）
│   └── prompts/         # 產文時送給 LLM 的完整 Prompt 紀錄（Debug 用）
└── logs/
    └── {date}.log       # Web UI 觸發的 pipeline 執行日誌
```

---

## 🛠️ 開發與貢獻

本專案使用 `pytest` 確保核心模組的正確性：

```bash
# 執行所有單元與整合測試（146 tests）
pytest tests/ -v
```

歡迎任何 Issue 回報或 Pull Request！如果這個專案對您追蹤 AI 領域的發展有幫助，請不要吝嗇給予一顆 ⭐️。
