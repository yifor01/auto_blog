# 設計：清單型來源拆分（Trending / Papers）+ 頂尖 AI 公司 blog 置頂

- 日期：2026-07-21
- 狀態：已核准（brainstorming 完成）

## 背景與目標

GitHub Trending 與 paper 類來源和一般新聞混在同一條評分 pipeline，造成：

1. 閱讀混亂 — trending repo 和新聞文章性質不同，混排難讀
2. 評分無意義 — LLM 拿不到論文全文 / repo 內容，5D 評分不可靠
3. 浪費 LLM 額度 — 這些項目佔掉 scoring / generation 呼叫

另外，頂尖 AI 公司（OpenAI/Anthropic/Google/DeepSeek 等）的官方 blog 是最重要的內容，
但受 LLM 評分波動影響，可能沒進 top-K 而漏掉。

**目標**：

- `github`、`hf_papers`、`arxiv`、`chatpaper`、`semantic_scholar` 五個來源退出評分
  pipeline，改為每日「清單」呈現（免 LLM，用天然訊號排序）
- 兩個 GUI（Astro 靜態站為主、Web Monitor 為輔）各加 Trending / Papers 分頁
- 頂尖 AI 公司官方 blog 當天發布 → 免評分直接生成文章並置頂
- 既往不究：不回填舊日期資料

## 1. Pipeline / 資料流

### 1.1 LIST_SOURCES 常數

`src/pipeline.py` 定義：

```python
LIST_SOURCES = {SourceType.GITHUB, SourceType.HF_PAPERS, SourceType.ARXIV,
                SourceType.CHATPAPER, SourceType.SEMANTIC_SCHOLAR}
```

### 1.2 Collect 階段（不動）

所有 collector 照舊收集進 `data/raw/{date}.json`；單日去重、跨日去重、
`--supplement` 補收、checkpoint 機制完全不變。

### 1.3 新增 lists stage（零 LLM）

collect 之後、score 之前執行 `build_lists(items, target_date)`，
輸出 `output/lists/{date}.json`：

```json
{
  "date": "2026-07-21",
  "github": [
    {"title": "owner/repo", "url": "...", "abstract": "...",
     "stars_today": 512, "language": "Python"}
  ],
  "papers": {
    "hf": [
      {"title": "...", "url": "...", "abstract": "...",
       "upvotes": 42, "arxiv_id": "2507.12345"}
    ],
    "others": [
      {"title": "...", "url": "...", "abstract": "...",
       "source": "arxiv", "source_name": "arXiv",
       "citation_count": 0, "published_date": "2026-07-21"}
    ]
  }
}
```

- `github`：`stars_today` 降冪，取 top `lists.github_top_k`（預設 10）
- `papers.hf`：`upvotes` 降冪，取 top `lists.hf_top_k`（預設 10）
- `papers.others`：arxiv + chatpaper + semantic_scholar 合併
  （彼此已在 collect 去重階段以 arxiv_id 互相去重），
  `citation_count` 降冪 → `published_date` 降冪，上限 `lists.other_papers_limit`（預設 30）
- 簡→繁：ContentItem 建構端 Layer A 已處理，lists 直接 dump
- **去重順序調整**：單日去重「先收集者留」，現行順序 arXiv 在 HF Papers 之前，
  同論文會留 arxiv 版而丟失 upvotes 訊號、造成 HF top 10 缺項。
  `get_collectors()` 將 `HFPapersCollector` 移到 `ArxivCollector` 之前
  （upvotes 是 papers 清單的主要排序訊號，優先保留 HF 版本）
- Checkpoint：lists 檔已存在即跳過；`--force` 一併刪除
- 某來源當日收集失敗 → 該欄位空陣列照寫，不視為錯誤

### 1.4 評分階段排除

- `score_items` / `score_incremental` 進入 rule scoring 前先過濾掉
  `item.source in LIST_SOURCES`
- 移除 `scoring/rules.py` 的 hf_papers 加分（+15/+10）與 github stars 加分（+15/+10）區塊
- 移除 `config.yaml` 的 `hf_upvote_bonus_threshold`、`github_stars_high`、
  `github_stars_medium`（及讀取端）

### 1.5 Pinned 機制（頂尖 AI 公司 blog 免評分生成）

生成階段之前：

1. 從 raw items 篩選：`source in {RSS, BLOG}` 且 `organization` 命中
   `pinned_organizations`（word-boundary 比對，沿用 `_match_institution` 風格）
   且 `published_date == target_date`
2. 命中項目包成 pseudo-ScoredItem：5D 分數以 0 填充、
   `llm_reason = "📌 頂尖 AI 公司官方發布"`、`rule_reasons = ["pinned"]`
3. 直接送生成（走現有 blog_post generator），frontmatter 加 `pinned: true`
4. 每日上限 `pinned_daily_limit`（預設 5）篇，超過依 published_date 新→舊取前 5
5. 命中項目**從評分 pool 移除**，避免同一篇既 pinned 又走評分重複生成
6. Pinned 生成同樣逐篇 checkpoint（已有同名 post 跳過）

## 2. Config 新增（`config.yaml`）

```yaml
pinned_organizations:   # 頂尖 AI 公司清單（官方 blog 免評分置頂）
  - OpenAI
  - Anthropic
  - Google
  - DeepSeek
  - 智譜        # GLM / Zhipu
  - Moonshot    # Kimi
  - MiniMax
  - Meta
  - xAI
  - Mistral
pinned_daily_limit: 5

lists:
  github_top_k: 10
  hf_top_k: 10
  other_papers_limit: 30
```

拼法須與 `_helpers.py` 機構對照表（`infer_organization`）輸出一致。

## 3. GUI

### 3.1 Astro 靜態站（`web/`，主要介面）

- `Nav.astro` 加兩個 tab：`🔥 Trending`（`/trending`）、`📄 Papers`（`/papers`）
- 兩頁皆：按日分組（只 build 近 30 天，比照首頁），每日一節，
  節內清單卡片（標題 / 簡介 / 天然訊號 badge：stars_today、upvotes、citation）
- 詳情頁：`/trending/<slug>`、`/papers/<slug>`（比照現有 `/daily/[slug]` pattern），
  內容直接呈現爬蟲已抓到的資料——標題、完整 abstract、metadata badge
  （stars_today / upvotes / citation / language / authors）、原文外連按鈕；
  **不做額外爬取或 LLM 加工**，有什麼放什麼
- 資料來源：`import.meta.glob` 直讀 `output/lists/*.json`，不進 content collection
- `⚡ 每日自動` 首頁：frontmatter `pinned: true` 的文章置頂 + 📌 badge
- Papers 頁 others 區塊預設折疊（HF top 10 為主清單）
- 某日無 lists 檔（歷史日期）→ 該日不顯示；當日空陣列 → 顯示「今日無資料」

### 3.2 Web Monitor（`src/web/`）

- `data_service.py` 加 `get_day_lists(date) -> dict | None`（讀 lists JSON，無檔回 None）
- Day Detail 頁加「🔥 Trending」「📄 Papers」分頁（與現有評分列表並列 tab）；
  無 lists 檔的舊日期隱藏這兩個 tab
- 分頁內卡片可展開完整 abstract（`<details>` 式，本機頁面不另做詳情頁）
- Dashboard / Day Detail 對 pinned 文章置頂顯示 + 📌 標記
- 其他頁面（素材庫 / 主題 / 書籤）不動：LIST_SOURCES 項目不再出現在 scored 資料中，
  自然從這些頁面消失（舊資料照舊顯示，既往不究）

## 4. CI/CD 與相容性

- `output/lists/` 進 repo：daily-pipeline workflow 的 commit 範圍已含 `output/`，
  確認不在排除清單（現排除僅 `output/notes/`、`output/prompts/`）即可
- 不回填歷史日期的 lists 檔
- 檢查 `src/generators/digest.py`：若模板引用 github / hf_papers 項目，
  同步改為排除 LIST_SOURCES（避免與新 tab 內容重複）；digest 定位維持「當日精選摘要」

## 5. 錯誤處理

- lists stage 對缺失 `raw_metadata` 欄位（stars_today / upvotes / citation_count）
  以 0 處理，不炸
- pinned 生成失敗（LLM chain 全掛）→ 記 log、不 block 後續評分項生成
- Web Monitor lists 檔 JSON 損毀 → `get_day_lists` 回 None、tab 隱藏（log warning）

## 6. 測試

pytest（`tests/`，不進 repo）：

- `build_lists`：排序正確、截斷上限、缺 metadata 欄位、空來源空陣列、繁化透傳
- pinned 挑選：organization 命中 / 未命中、每日上限、從評分 pool 移除、
  非當日發布不 pin
- 評分排除：LIST_SOURCES 項目不進 rule/LLM scoring
- `get_day_lists`：正常讀取 / 無檔 / 損毀 JSON
- rules.py：hf/github 加分移除後其餘規則不受影響

Astro 端：`npm run build` 成功 + 本地 preview 驗證 Trending / Papers 頁與 pinned 置頂。

End-to-end：`python -m src.cli run --date <近日> --force`（或 dry-run + 手動 lists）
確認 lists 檔產出、scored 不含 LIST_SOURCES、pinned 文章生成。

## 7. 不做的事（YAGNI）

- 詳情頁的額外爬取 / LLM 加工（只呈現 collect 階段已抓到的內容）
- 歷史資料回填
- lists 項目的書籤 / 素材庫整合（想深入寫某篇 → 人工加入精選 blogs 流程）
- LLM 對 lists 項目的任何處理（摘要翻譯等）——abstract 原樣呈現
