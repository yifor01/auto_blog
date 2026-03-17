# Auto Post Blog 🤖📝

[![Python 3.11+](https://img.shields.io/badge/python-3.11+-blue.svg)](https://www.python.org/downloads/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.115+-00a393.svg)](https://fastapi.tiangolo.com)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

**Auto Post Blog** 是一個自動化的 AI 資訊聚合與內容生成系統。每天自動從 9 個前沿資料源（arXiv、HuggingFace、GitHub、Tech Blogs、RSS、Hacker News、Reddit、NewsAPI、ChatPaper）收集最新的生成式 AI 論文與新聞，透過 Rule-based 與 LLM 雙層價值篩選機制，產出高品質的繁體中文「部落格貼文草稿」與「每日精選摘要」。配備完整的 Web Dashboard 供監控、搜尋、收藏與內容管理。支援多 API key round-robin 輪替，scoring 與 blog 生成可使用不同模型。

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
  - 精選 AI Tech Blogs — Karpathy、Simon Willison、Eugene Yan、Latent Space 等
  - 主流科技媒體 RSS Feeds — TechCrunch、OpenAI、Google Research、VentureBeat、MarkTechPost 等
  - Hacker News — Algolia API，依 upvotes 篩選 AI 熱門討論
  - Reddit — r/LocalLLaMA、r/MachineLearning
  - NewsAPI — 主流科技新聞聚合
- **🖥️ 現代化 Web Dashboard**：
  - Dark / Light 主題切換
  - **Dashboard 戰情室**：7 天互動式卡片、趨勢 sparkline、來源分布 mini chart、最近 Blog 文章快速回顧
  - **Dashboard 快速行動**：Top Items 直連內部素材頁，有 Blog 的文章顯示紫色 Article badge 一鍵直達
  - **Pipeline 控制台**：GitLab CI/CD 風格 stage pills（running / done / failed / cancelled），支援逐 stage 重跑、強制停止、即時 log 串流（SSE）
  - **素材庫**：合併 posts + notes，全文搜尋、來源/分數/日期篩選、Article pill 一鍵直連精選 Blog
  - **書籤 & Kanban 待寫清單**：三欄拖曳（已收藏→已完成→已發布），已收藏欄完整卡片（摘要+LLM 評語+tags），已完成/已發布精簡顯示可捲動
  - **Day Detail 單篇收藏**：點擊 ☆ 星號即可加入待寫清單
  - **主題聚合**：8 個 topic cluster + 14 天趨勢 sparkline
  - **每日摘要**：模板式生成（不需 LLM），Top Picks + Worth Watching
  - **精選 Blog**：人工策展的精選文章（FB 格式），底部導航可快速跳轉至評分詳情或日詳情做 fact-check
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
    LLMScore --> |Scored JSON| DigestGen

    PostGen --> |Markdown| output/posts
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

複製範例設定檔並填入您的 API Key（專案使用 aihubmix.com 免費模型，支援 4 key round-robin）：

```bash
cp .env.example .env
# 編輯 .env 填入：
#   AIHUBMIX_API_KEY_1 ~ AIHUBMIX_API_KEY_4（至少一組必要）
#   NEWSAPI_KEY（選用，啟用 NewsAPI collector 需要）
```

### 3. 微調配置 (Optional)

編輯 `config.yaml` 調整偏好設定，或啟動 Web 後在 `/settings` 頁面直接修改：

- **LLM 模型**（Scoring: `gpt-4.1-free`、Blog 生成: `gpt-4o-free`，可在 Settings 頁面切換）
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

# 強制清除快取重跑（保留舊 posts，新 top-K 覆寫同名舊文）
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

## 📋 撰寫員每日工作流 (Writer's Daily Workflow)

Web Dashboard 的設計目標是讓「打開 Dashboard → 決定寫什麼 → 完成文章」的路徑盡可能短。以下是推薦的每日操作手順：

### Step 1：總覽 — Dashboard (`/dashboard`)

啟動 Web 後，Pipeline 會自動在背景執行當天的收集與評分。Dashboard 頁面提供：

- **今日精選 Top 3** + **本週 Top 10**：每篇標題直連內部素材頁，旁邊有 ↗ 外部連結可快速開啟原文
- **紫色 Article badge**：已有精選 Blog 的文章會顯示紫色 `Article` 標記，點擊直達 Blog 閱讀頁面；沒有 badge 的高分文章就是「還沒寫的」候選題材
- **最近 Blog 文章**：頁面底部列出最近 5 篇已產出的 Blog，方便回顧

> **操作**：掃一眼 Top 10，找到沒有 Article badge 的高分文章 → 點標題進入素材頁

### Step 2：選題 — 素材頁 (`/material/{date}/{index}`)

素材詳情頁提供 5D 雷達圖、LLM 評語、原文摘要，幫助判斷一篇文章是否值得撰寫。

> **操作**：覺得值得寫 → 點擊 ☆ 收藏加入待寫清單

### Step 3：決定優先級 — 待寫清單 (`/queue`)

Kanban 三欄（已收藏 → 已完成 → 已發布），拖曳卡片即可切換狀態。

每張卡片顯示：
- **LLM 評語**：不用離開 Queue 就能回顧「為什麼這篇值得寫」
- **原文 ↗ 連結**：一鍵開啟原始論文/文章
- **分數 badge**、來源、日期、tags

> **操作**：看 LLM 評語決定今天先寫哪篇 → 拖到「已完成」

### Step 4：撰寫與 Fact-check

撰寫時可隨時在以下頁面間跳轉：

| 需求 | 前往 | 操作 |
|------|------|------|
| 查看原文 | 卡片上的 ↗ 連結 | 新分頁開啟 |
| 查看 LLM 評分細節 | 素材頁 `/material/{date}/{index}` | 點卡片標題 |
| 查看全天文章分布 | Day Detail `/day/{date}` | 從素材頁麵包屑導航 |

### Step 5：發布後回顧 — Blog View (`/blog/{date}/{slug}`)

精選 Blog 閱讀頁底部提供三個導航連結：

- **返回 Blog 列表** → `/blogs`
- **查看評分詳情** → `/material/{date}/{index}`（核對分數、原文做 fact-check）
- **查看日詳情** → `/day/{date}`

### 素材庫快速篩選 (`/materials`)

素材庫提供多維度篩選，適合更系統性地瀏覽：

- **來源篩選**：下拉選單或標題搜尋
- **Tag 篩選**：LLM / Agent / RAG / Fine-tuning 等快速 chip
- **產出篩選**：「有 Blog」「有 Note」「有 Article」chip 快速過濾
- **Article pill**：紫色可點擊直連 Blog，灰色表示尚無 Blog — 一眼區分已寫/未寫

### 工作流速查表

| 場景 | 起點 | 操作 | 到達 |
|------|------|------|------|
| 找今天值得寫的文章 | Dashboard | 點擊無 Article badge 的高分標題 | 素材頁 |
| 閱讀已有的 Blog | Dashboard | 點擊紫色 Article badge | Blog View |
| 收藏高分文章 | Day Detail | 點擊 ☆ 星號收藏 | Queue |
| 決定今天先寫哪篇 | Queue | 看 LLM 評語 + 分數 | 拖到「已完成」|
| Blog 發布後做 fact-check | Blog View | 點「查看評分詳情」 | 素材頁 |
| 查看哪些文章還沒寫 | 素材庫 | 反選「有 Article」filter | 未寫文章清單 |

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

Web server 啟動時會自動觸發當天的 pipeline（`force=False`，checkpoint 機制保護不重跑已完成階段）。若需透過 cron 排程 CLI 執行：

```bash
# 範例：每日早上 10:00 執行完整 pipeline（配合 HuggingFace Daily Papers 更新時區）
0 10 * * * cd /path/to/auto_post_blog && .venv/bin/python -m src.cli run >> logs/cron.log 2>&1
```

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
│   ├── notes/           # 歷史 AI 筆記（pipeline 不再生成，保留供瀏覽）
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
