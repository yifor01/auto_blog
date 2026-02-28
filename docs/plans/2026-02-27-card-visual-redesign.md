# 設計文件：部落格 & AI 筆記卡片視覺重構

**日期**：2026-02-27
**範疇**：posts_list.html、notes_list.html、day_detail.html、data_service.py

---

## 目標

1. 卡片顯示 5D 分數條 + 總分 + 來源 chip（如 item_detail 版面）
2. 利用 feedback 狀態 & 日期分組避免密集感
3. 預設快速 tag 搜尋 chips

---

## 架構決策

採用 **Eager cross-reference + client-side filter** 方案：
- 後端在 `list_all_posts/notes` 時讀取 `data/scored/{date}.json`，以 title 匹配取得 5D 分數
- 同一 date 的 scored JSON 只讀一次（per-request dict cache）
- 搜尋/篩選/tag filter 全部 client-side，不增加 API call

---

## 資料層（data_service.py）

### 新增函數

**`_load_scored_for_date(date_str: str) -> dict[str, dict]`**
- 讀取 `data/scored/{date_str}.json`
- 回傳 `{title: scored_item_dict}` 便於 O(1) 查找

**`_enrich_with_scored(item: dict) -> dict`**
- 根據 item 的 `date_str` + `title` 查 scored dict
- 填入：`novelty`, `impact`, `trending`, `practicality`, `blog_worthiness`, `rule_score`, `llm_score`, `source_name`, `llm_reason`
- 找不到時各欄位留 `None`

**`get_all_feedback() -> dict[str, str]`**
- 掃描 `data/feedback/*.json`
- 回傳 `{"2026-02-27_slug": "good", ...}`

### 修改函數

`list_all_posts()` / `list_all_notes()`：每個 item 加入 `_enrich_with_scored` 結果 + feedback 值

---

## UI 設計

### posts_list.html / notes_list.html

**版面結構**：
```
[搜尋框]  [排序▾]                          共 N 篇 · M 天

[全部] [LLM] [Agent] [RAG] [Fine-tuning] [Multimodal]
[安全] [小模型] [推理] [Anthropic] [OpenAI] [Meta] [開源]

📅 2026-02-27  10 篇
┌──────────────────────┐ ┌──────────────────────┐
│ [ArXiv]       👍 好  │ │ [HuggingFace]  (未評) │
│ 標題 xxxxxxxxxxxxxxx │ │ 標題 xxxxxxxxxxxxxxx  │
│ 摘要 xxx...          │ │ 摘要 xxx...           │
│ 新穎性 ▓▓▓▓▓  16     │ │ 新穎性 ▓▓▓    12      │
│ 話題性 ▓▓▓▓   15     │ │ 話題性 ▓▓      8      │
│ 實用性 ▓▓▓    14     │ │ 實用性 ▓▓▓▓   15      │
│ 🏷 LLM  Agent        │ │ 🏷 RAG                │
│ ⭐113  ⏱5分 · 800字  │ │ ⭐89   ⏱3分 · 600字   │
└──────────────────────┘ └──────────────────────┘

📅 2026-02-26  5 篇
...
```

### Feedback 著色規則

| 狀態 | 左邊框 | 背景 tint | 右上角 badge |
|------|--------|-----------|-------------|
| good | 3px #34d399 | rgba(52,211,153,0.05) | 👍 好 |
| bad | 3px #f87171 | rgba(248,113,113,0.05) | 👎 差 |
| normal | 3px #475569 | 無 | ─ 普通 |
| 未評 | 1px var(--br) | 無 | 無 |

### 快速 tag 預設清單

`LLM`、`Agent`、`RAG`、`Fine-tuning`、`Multimodal`、`安全`、`小模型`、`推理`、`Anthropic`、`OpenAI`、`Meta`、`開源`

Tag chip 點擊 → toggle active → 多選為 AND 交集。搜尋框與 tag 可同時使用。

### day_detail.html mini-card

- 加入 feedback 著色（green/red/gray 左邊框）
- 加入 3 條緊湊 mini bar（高度 3px）：新穎性、話題性、實用性
- 需在 `day_detail` 路由傳入 `feedback_map`（由 `get_all_feedback()` 篩選出當日）

---

## 受影響檔案

| 檔案 | 修改類型 |
|------|---------|
| `src/web/data_service.py` | 新增 3 個函數，修改 list_all_posts/notes |
| `src/web/app.py` | day_detail 路由加入 feedback_map |
| `src/web/templates/posts_list.html` | 完全重寫 |
| `src/web/templates/notes_list.html` | 完全重寫 |
| `src/web/templates/day_detail.html` | mini-card 加入 5D bars + feedback |

---

## 驗證計畫

1. `python3 -c "from src.web import data_service as ds; print(ds.list_all_posts()[0])"` — 確認 5D 欄位存在
2. 啟動 `python -m src.cli web`，訪問 `/posts` — 確認日期分組、5D bars、feedback 著色、tag filter
3. 訪問 `/day/2026-02-27` — 確認 mini-card feedback 著色
4. 邊界條件：無 scored 資料 → 不顯示 5D bars；無 feedback → 不顯示 badge
