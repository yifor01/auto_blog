# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

自動收集 GenAI 前沿論文與新聞 → 價值篩選 → 產出部落格貼文的 Python CLI pipeline。
使用 Typer 作為 CLI 框架，透過 OpenRouter API 進行 LLM 評分與內容生成。

## Commands

```bash
# Setup
python3 -m venv .venv && source .venv/bin/activate
pip install -e .
cp .env.example .env  # 填入 OPENROUTER_API_KEY

# Run pipeline
python -m src.cli run                    # 完整 pipeline（收集→評分→生成）
python -m src.cli run --dry-run          # 只收集+評分，不生成
python -m src.cli run --date 2026-02-23  # 指定日期
python -m src.cli run --force            # 清除所有快取+輸出重跑（含 posts/notes/prompts）

# Individual steps
python -m src.cli collect                # 只收集
python -m src.cli score                  # 只評分
python -m src.cli generate --top-k 3    # 只生成（預設使用 config final_top_k）
python -m src.cli summary                # 檢視評分摘要
python -m src.cli status                 # 檢視 7 天狀態
python -m src.cli catchup --days 7      # 補跑遺漏天數

# Content browsing
python -m src.cli list                   # 列出最近 7 天所有生成文章
python -m src.cli list --days 30 --type post   # 只看 blog posts
python -m src.cli show output/posts/2026-02-26_xxx.md  # 在終端機渲染文章

# Digest（每日摘要，不需 LLM）
python -m src.cli digest                 # 生成今日精選摘要
python -m src.cli digest --date 2026-02-28  # 指定日期

# Maintenance
python -m src.cli clean --keep-days 30  # 清理 30 天前的資料
python -m src.cli clean --before 2026-01-01 --dry-run  # 預覽清理

# Web monitor
python -m src.cli web                    # 啟動監控網頁 http://127.0.0.1:8080

# Installed command alias
autopb run

# Testing
pytest tests/                            # 116 tests
```

## Architecture

```
Collection (7 collectors) → Single-day Dedup → Cross-day Dedup → Rule Score → LLM Score → Top-K → Generate
```

**Pipeline 有 checkpoint 機制**：每個階段結果快取為 JSON，中斷後可續跑。

### Key Layers

| Layer | Directory | Purpose |
|-------|-----------|---------|
| CLI 入口 | `src/cli.py` | Typer 指令、pipeline 編排、checkpoint 管理 |
| Logger | `src/logger.py` | 雙模式日誌：`JsonFormatter`、`setup_logging()`、`get_logger()`；`AUTOPB_LOG_FORMAT=json` 切換 JSON lines 模式 |
| Models | `src/models.py` | Pydantic models：`ContentItem`, `ScoredItem`, `SourceType` |
| Utilities | `src/utils.py` | Config 讀取、HTTP client、LLM 呼叫、IO helpers、跨日去重 |
| Collectors | `src/collectors/` | 7 個資料源收集器，繼承 `BaseCollector` |
| Scoring | `src/scoring/` | `rules.py` 規則預篩 + `scorer.py` LLM 深度評分（CLI 模式含 Rich 進度條，JSON 模式自動停用） |
| Generators | `src/generators/` | `blog_post.py` 部落格文 + `note.py` AI 筆記 + `digest.py` 每日摘要（均含 YAML frontmatter） |
| Web | `src/web/` | FastAPI 監控介面、素材庫、搜尋、書籤、主題瀏覽、每日摘要 |

### Data Sources (Collectors)

arXiv、ChatPaper、HuggingFace Daily Papers、RSS feeds（TechCrunch, OpenAI, Anthropic 等）、AI 部落格、GitHub Trending、Hacker News（Algolia API）

### Scoring Pipeline

1. **Rule-based**（`scoring/rules.py`）：機構加分（word boundary 匹配）、關鍵字加分、HF upvote 加分，門檻 25 分
2. **LLM-based**（`scoring/scorer.py`）：5 維度各 0-20 分（新穎性、影響力、**話題性**、**實用性**、部落格適合度）

`ScoredItem` 欄位：`novelty`, `impact`, `trending`（舊版 JSON 的 `relevance` 自動對應）, `practicality`, `blog_worthiness`

### Data Flow

- `data/raw/{date}.json` — 去重後原始資料（含跨日去重）
- `data/scored/{date}.json` — 評分後資料（5D LLM scores 全部儲存）
- `data/bookmarks.json` — 書籤/收藏清單（status: bookmarked/writing/written/published）
- `output/posts/{date}_{slug}.md` — 生成的部落格文（含 YAML frontmatter）
- `output/notes/{date}_{slug}.md` — 生成的 AI 筆記（含 YAML frontmatter）
- `output/digests/{date}.md` — 每日精選摘要（模板式，不需 LLM）
- `output/prompts/{date}_{slug}_prompt.md` — 完整 prompt（稽核用）
- `logs/{date}.log` — Web UI 觸發的 pipeline 執行日誌

### Key Config (`config.yaml`)

```yaml
dedup:
  lookback_days: 7          # 跨日去重回看天數（0=停用）

scoring:
  hf_upvote_bonus_threshold: 10
  github_stars_high: 100
  github_stars_medium: 50
  rule_threshold: 25
  llm_top_k: 30
  final_top_k: 10
```

## Configuration

- `config.yaml`：LLM model 設定、collector 開關、評分參數（機構清單、關鍵字、top-k 門檻、去重窗口）
- `.env`：`OPENROUTER_API_KEY`（必要）
- LLM 有 fallback model 機制，primary 失敗自動切換
- Free tier rate limiting：`request_delay_seconds` 控制請求間隔

## Conventions

- 所有輸出內容為繁體中文
- Pydantic v2 用於資料驗證
- 新 collector 需繼承 `src/collectors/base.py` 的 `BaseCollector`
- `--force` flag 清除所有快取（raw JSON、scored JSON、posts、notes、prompts）重跑
- Collectors 採 lazy init：只在 `collect`/`run` 指令實際執行時才實例化
- 日期參數統一透過 `_parse_date()` 解析，提供友善錯誤訊息
- Web pipeline log 寫入 `logs/{date}.log`，可透過 `GET /api/logs/{date}` 查看

## Web API Endpoints

| Method | Path | 說明 |
|--------|------|------|
| GET | `/dashboard` | 7 天概覽 |
| GET | `/day/{date}` | 單日詳情 |
| GET | `/item/{date}/{index}` | 單篇評分詳情（5D 雷達圖） |
| GET | `/materials` | 素材庫（合併 posts + notes，瀏覽 scored items）|
| GET | `/material/{date}/{index}` | 素材詳情（tab 切換 Blog Draft / Note）|
| GET | `/queue` | 待寫清單（Kanban 四欄，拖曳切換狀態）|
| GET | `/topics?days=30` | 主題聚合視圖（8 個 topic cluster + sparkline）|
| GET | `/digest` | 每日摘要列表 |
| GET | `/digest/{date}` | 單日摘要渲染 |
| GET | `/post/{date}/{slug}` | 部落格文渲染 |
| GET | `/note/{date}/{slug}` | AI 筆記渲染 |
| GET | `/api/search` | 素材搜尋（q, source, min_score, date_from/to, page）|
| POST | `/api/bookmark/{date}/{index}` | 收藏素材 |
| DELETE | `/api/bookmark/{date}/{index}` | 取消收藏 |
| PATCH | `/api/bookmark/{date}/{index}/status` | 更新書籤狀態 |
| GET | `/api/bookmark/{date}/{index}/check` | 檢查是否已收藏 |
| GET | `/api/bookmarks?status=` | 列出書籤 |
| GET | `/api/logs/{date}` | 查看 pipeline 執行 log |
| POST | `/api/run/{date}` | 觸發 pipeline（背景執行，重複執行回 409） |
| POST | `/api/run/{date}/force` | 強制重跑 pipeline |
| POST | `/api/run/{date}/stop` | 中止執行中的 pipeline（SIGTERM → SIGKILL） |
| POST | `/api/run/{date}/stage/{stage_name}` | 重跑單一 stage（collect/score/generate） |
| GET | `/api/logs/{date}/stage-info` | 各 stage 狀態摘要（status/elapsed/item_count） |
| GET | `/api/logs/{date}/stage/{stage_name}` | 取得特定 stage 的格式化 log（含 ts、level、msg、in_progress） |

> `/posts` 和 `/notes` 已 301 重導至 `/materials`

### Day Detail 頁面（`/day/{date}`）

- **Pipeline Stages**：GitLab 圓角膠囊（Pill）風格，3 個 `.stage-pill`（收集/評分/生成）+ `.stage-connector` 連接線/chevron，狀態色系統（done=綠、running=藍 pulse、failed=紅、cancelled=橘、pending=半透明），連接線隨上游完成變綠（CSS adjacent sibling）
- **Charts Strip**：分數分佈 + 來源佔比水平並列（grid 1fr 1fr，110px），位於 pipeline card 下方、評分列表上方
- **評分列表含「產出」欄**：`content_map`（title→Blog/Note 映射）由後端傳入，表格內嵌 Blog/Note badge 連結，不再有獨立「產出內容」區塊
- **Log Panel**：點擊 pill 展開 log，再點同一顆收合（toggle）；live log 格式 `[HH:MM:SS] [LEVEL] [source] msg (N 筆)`（UTC+8），歷史 log `ts` 欄同為 UTC+8，`msg` 包含 blog/feed 名稱與計數
- **Emoji 字體**：base.html 引入 Noto Color Emoji（Google Fonts）

### topic_clusters（`config.yaml`）

8 個預設主題：Agent、RAG、Reasoning、Vision、Training、Efficiency、Code、Safety。可在 `config.yaml` 的 `topic_clusters` 區塊自訂關鍵字。
