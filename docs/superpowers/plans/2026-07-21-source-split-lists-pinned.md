# 清單型來源拆分 + Pinned 置頂 Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** 將 github / hf_papers / arxiv / chatpaper / semantic_scholar 五個來源退出評分 pipeline，改為零 LLM 的每日清單（`output/lists/{date}.json`），兩個 GUI 各加 Trending / Papers 分頁；頂尖 AI 公司官方 blog 免評分直接生成並置頂。

**Architecture:** 新模組 `src/lists.py`（清單建構）與 `src/pinned.py`（置頂挑選）為純選擇邏輯 + 薄 IO；pipeline 在 collect 後呼叫 lists stage、在 score 前排除清單/置頂來源、在 generate 前先生成 pinned 文章。兩個 GUI 讀同一份 lists JSON。

**Tech Stack:** Python 3 / Pydantic v2 / Typer / FastAPI + Jinja2（Web Monitor）、Astro 5 + TypeScript（靜態站）、pytest。

**Spec:** `docs/superpowers/specs/2026-07-21-source-split-lists-pinned-design.md`

## Global Constraints

- 繁體中文輸出；Python 註解風格比照既有檔案（精簡、講 why）
- `tests/` 不進 repo（.gitignore 排除），只存在本地；pytest 執行方式 `source .venv/bin/activate && pytest tests/...`
- 既往不究：不回填歷史日期 lists 檔；無 lists 檔的日期 GUI 隱藏對應 tab / 不顯示
- lists stage 零 LLM；pinned 生成走現有 generation chain
- `LIST_SOURCES = {GITHUB, HF_PAPERS, ARXIV, CHATPAPER, SEMANTIC_SCHOLAR}`
- lists 預設值：`github_top_k: 10`、`hf_top_k: 10`、`other_papers_limit: 30`；pinned 預設 `pinned_daily_limit: 5`
- 缺失 raw_metadata 數值欄位（stars_today / upvotes / citation_count）以 0 處理
- commit message 格式 `<type>: <description>`；多行訊息用 `git commit -F <file>`

---

### Task 1: `src/lists.py` — 清單建構模組

**Files:**
- Modify: `src/utils.py:31-38`（加 `LISTS_DIR`）
- Create: `src/lists.py`
- Test: `tests/test_lists.py`

**Interfaces:**
- Consumes: `src/utils.py` 的 `save_json / load_config / slugify / console`；`src/models.py` 的 `ContentItem / SourceType`
- Produces:
  - `LIST_SOURCES: set[SourceType]`、`PAPER_SOURCES: set[SourceType]`
  - `get_lists_path(d: date) -> Path`
  - `build_day_lists(items: list[ContentItem], target_date: date, config: dict | None = None) -> dict`（純函式，回傳 lists dict）
  - `build_lists(items: list[ContentItem], target_date: date, force: bool = False) -> dict | None`（含 checkpoint 的 IO 包裝；已存在且非 force 回 None）

- [ ] **Step 1: 在 `src/utils.py` 加 `LISTS_DIR`**

在 `BLOGS_DIR = OUTPUT_DIR / "blogs"`（`src/utils.py:36`）之後加：

```python
LISTS_DIR = OUTPUT_DIR / "lists"
```

並把 `LISTS_DIR` 加進下一行的 mkdir 迴圈清單（`for d in [RAW_DIR, ..., BLOGS_DIR, LISTS_DIR]:`）。

- [ ] **Step 2: 寫失敗測試 `tests/test_lists.py`**

```python
"""src/lists.py 清單建構測試。"""
from datetime import date

import pytest

from src.lists import LIST_SOURCES, build_day_lists, build_lists, get_lists_path
from src.models import ContentItem, SourceType

D = date(2026, 7, 21)


def _item(source, title, **meta):
    return ContentItem(
        source=source,
        source_name=source.value,
        title=title,
        url=f"https://example.com/{title.replace('/', '-')}",
        abstract="some abstract " * 5,
        published_date=D,
        raw_metadata=meta,
    )


CFG = {"lists": {"github_top_k": 2, "hf_top_k": 2, "other_papers_limit": 3}}


def test_list_sources_membership():
    assert LIST_SOURCES == {
        SourceType.GITHUB, SourceType.HF_PAPERS, SourceType.ARXIV,
        SourceType.CHATPAPER, SourceType.SEMANTIC_SCHOLAR,
    }


def test_github_sorted_by_stars_and_truncated():
    items = [
        _item(SourceType.GITHUB, "a/low", stars_today=5),
        _item(SourceType.GITHUB, "b/high", stars_today=500),
        _item(SourceType.GITHUB, "c/mid", stars_today=50),
    ]
    result = build_day_lists(items, D, CFG)
    assert [e["title"] for e in result["github"]] == ["b/high", "c/mid"]
    assert result["github"][0]["stars_today"] == 500
    assert result["github"][0]["slug"]  # slug 供詳情頁路由


def test_hf_sorted_by_upvotes():
    items = [
        _item(SourceType.HF_PAPERS, "paper low", upvotes=1, arxiv_id="2607.00001"),
        _item(SourceType.HF_PAPERS, "paper high", upvotes=99, arxiv_id="2607.00002"),
    ]
    result = build_day_lists(items, D, CFG)
    assert [e["title"] for e in result["papers"]["hf"]] == ["paper high", "paper low"]


def test_others_merged_sorted_truncated():
    items = [
        _item(SourceType.ARXIV, "arxiv paper", arxiv_id="2607.10001"),
        _item(SourceType.CHATPAPER, "chatpaper paper", arxiv_id="2607.10002"),
        _item(SourceType.SEMANTIC_SCHOLAR, "ss cited", arxiv_id="2607.10003", citation_count=42),
        _item(SourceType.SEMANTIC_SCHOLAR, "ss extra", arxiv_id="2607.10004", citation_count=7),
    ]
    result = build_day_lists(items, D, CFG)
    others = result["papers"]["others"]
    assert len(others) == 3  # other_papers_limit=3 截斷
    assert others[0]["title"] == "ss cited"  # citation_count 最高排最前


def test_missing_metadata_defaults_to_zero():
    items = [_item(SourceType.GITHUB, "a/nometa")]
    result = build_day_lists(items, D, CFG)
    assert result["github"][0]["stars_today"] == 0


def test_non_list_sources_excluded():
    items = [_item(SourceType.RSS, "some news")]
    result = build_day_lists(items, D, CFG)
    assert result["github"] == []
    assert result["papers"]["hf"] == []
    assert result["papers"]["others"] == []


def test_build_lists_checkpoint(tmp_path, monkeypatch):
    import src.lists as lists_mod
    monkeypatch.setattr(lists_mod, "LISTS_DIR", tmp_path)
    items = [_item(SourceType.GITHUB, "a/repo", stars_today=10)]
    first = build_lists(items, D)
    assert first is not None
    assert get_lists_path(D).exists() is False or True  # path 用 patched dir 驗證於下行
    assert (tmp_path / "2026-07-21.json").exists()
    # 已存在 → 跳過
    assert build_lists(items, D) is None
    # force → 重建
    assert build_lists(items, D, force=True) is not None
```

- [ ] **Step 3: 跑測試確認失敗**

Run: `source .venv/bin/activate && pytest tests/test_lists.py -v`
Expected: FAIL（`ModuleNotFoundError: No module named 'src.lists'`）

- [ ] **Step 4: 實作 `src/lists.py`**

```python
"""清單型來源（GitHub Trending / Papers）每日清單建構。

這五個來源 LLM 拿不到全文、評分不可靠，退出評分 pipeline，
改用天然訊號（stars_today / upvotes / citation_count）排序成每日清單，
輸出 output/lists/{date}.json 供 Astro 靜態站與 Web Monitor 共用。零 LLM。
"""

from __future__ import annotations

from datetime import date
from pathlib import Path

from src.logger import get_logger
from src.models import ContentItem, SourceType
from src.utils import LISTS_DIR, console, load_config, save_json, slugify

_logger = get_logger("lists")

LIST_SOURCES = {
    SourceType.GITHUB,
    SourceType.HF_PAPERS,
    SourceType.ARXIV,
    SourceType.CHATPAPER,
    SourceType.SEMANTIC_SCHOLAR,
}

PAPER_SOURCES = {SourceType.ARXIV, SourceType.CHATPAPER, SourceType.SEMANTIC_SCHOLAR}


def get_lists_path(d: date) -> Path:
    return LISTS_DIR / f"{d.isoformat()}.json"


def _int_meta(item: ContentItem, key: str) -> int:
    try:
        return int(item.raw_metadata.get(key) or 0)
    except (TypeError, ValueError):
        return 0


def _github_entry(it: ContentItem) -> dict:
    return {
        "title": it.title,
        "slug": slugify(it.title),
        "url": it.url,
        "abstract": it.abstract,
        "stars_today": _int_meta(it, "stars_today"),
        "language": it.raw_metadata.get("language", ""),
    }


def _hf_entry(it: ContentItem) -> dict:
    return {
        "title": it.title,
        "slug": slugify(it.title),
        "url": it.url,
        "abstract": it.abstract,
        "upvotes": _int_meta(it, "upvotes"),
        "arxiv_id": it.raw_metadata.get("arxiv_id", ""),
        "authors": it.authors,
    }


def _other_entry(it: ContentItem) -> dict:
    return {
        "title": it.title,
        "slug": slugify(it.title),
        "url": it.url,
        "abstract": it.abstract,
        "source": it.source.value,
        "source_name": it.source_name,
        "citation_count": _int_meta(it, "citation_count"),
        "published_date": it.published_date.isoformat(),
        "authors": it.authors,
    }


def build_day_lists(
    items: list[ContentItem], target_date: date, config: dict | None = None
) -> dict:
    """純函式：從當日 items 篩出清單來源，排序＋截斷成 lists dict（不做 IO）。"""
    config = config or load_config()
    lists_cfg = config.get("lists", {})
    github_top_k = lists_cfg.get("github_top_k", 10)
    hf_top_k = lists_cfg.get("hf_top_k", 10)
    others_limit = lists_cfg.get("other_papers_limit", 30)

    github = sorted(
        (it for it in items if it.source == SourceType.GITHUB),
        key=lambda it: _int_meta(it, "stars_today"),
        reverse=True,
    )[:github_top_k]
    hf = sorted(
        (it for it in items if it.source == SourceType.HF_PAPERS),
        key=lambda it: _int_meta(it, "upvotes"),
        reverse=True,
    )[:hf_top_k]
    others = sorted(
        (it for it in items if it.source in PAPER_SOURCES),
        key=lambda it: (_int_meta(it, "citation_count"), it.published_date.isoformat()),
        reverse=True,
    )[:others_limit]

    return {
        "date": target_date.isoformat(),
        "github": [_github_entry(it) for it in github],
        "papers": {
            "hf": [_hf_entry(it) for it in hf],
            "others": [_other_entry(it) for it in others],
        },
    }


def build_lists(
    items: list[ContentItem], target_date: date, force: bool = False
) -> dict | None:
    """建構並寫入 output/lists/{date}.json。已存在且非 force → 跳過（checkpoint）。"""
    path = get_lists_path(target_date)
    if path.exists() and not force:
        return None
    data = build_day_lists(items, target_date)
    save_json(data, path)
    _logger.info(
        "Lists saved",
        extra={
            "date": str(target_date),
            "github": len(data["github"]),
            "hf": len(data["papers"]["hf"]),
            "others": len(data["papers"]["others"]),
        },
    )
    console.print(
        f"📋 Lists saved: {path.name} "
        f"(github {len(data['github'])} / hf {len(data['papers']['hf'])} "
        f"/ others {len(data['papers']['others'])})"
    )
    return data
```

注意：`build_lists` 內對 `LISTS_DIR` 的引用要透過 module attribute 供測試 monkeypatch —— `get_lists_path` 已滿足（讀模組層變數）。若測試失敗於 path patch，改 `monkeypatch.setattr("src.lists.LISTS_DIR", tmp_path)` 寫法。

- [ ] **Step 5: 跑測試確認通過**

Run: `pytest tests/test_lists.py -v`
Expected: 全部 PASS

- [ ] **Step 6: Commit**

```bash
git add src/lists.py src/utils.py
git commit -m "feat: lists 模組 — 清單型來源每日清單建構（零 LLM）"
```

---

### Task 2: Pipeline 整合 lists stage + collector 順序調整

**Files:**
- Modify: `src/pipeline.py`（`get_collectors` 順序、`run_pipeline` / `run_supplement` / `run_collect` / `run_catchup` 加 build_lists、`--force` 清除 lists 檔）
- Test: `tests/test_pipeline_lists.py`

**Interfaces:**
- Consumes: Task 1 的 `build_lists(items, target_date, force=False)`、`get_lists_path(d)`
- Produces: pipeline 各入口在 collect 後保證 lists 檔產出

- [ ] **Step 1: 寫失敗測試 `tests/test_pipeline_lists.py`**

```python
"""Pipeline 的 lists stage 整合與 collector 順序測試。"""
from datetime import date


def test_hf_collector_before_arxiv():
    """單日去重「先收集者留」：HF 需在 arXiv 前，同論文才保得住 upvotes 訊號。"""
    from src.pipeline import get_collectors

    names = [c.name for c in get_collectors()]
    assert names.index("hf_papers") < names.index("arxiv")


def test_run_collect_builds_lists(tmp_path, monkeypatch):
    from src import pipeline
    from src.models import ContentItem, SourceType

    d = date(2026, 7, 21)
    items = [
        ContentItem(
            source=SourceType.GITHUB, source_name="GitHub Trending",
            title="a/repo", url="https://github.com/a/repo",
            abstract="desc", published_date=d,
            raw_metadata={"stars_today": 10},
        )
    ]
    calls = {}
    monkeypatch.setattr(pipeline, "collect_items", lambda target_date=None: items)
    monkeypatch.setattr(
        pipeline, "build_lists",
        lambda i, td, force=False: calls.update(items=i, date=td, force=force),
    )
    pipeline.run_collect(d)
    assert calls["date"] == d
    assert calls["items"] == items
```

- [ ] **Step 2: 跑測試確認失敗**

Run: `pytest tests/test_pipeline_lists.py -v`
Expected: FAIL（順序不符 / `pipeline` 無 `build_lists` 屬性）

- [ ] **Step 3: 修改 `src/pipeline.py`**

3a. import 區（`from src.scoring.rules import ...` 之前）加：

```python
from src.lists import LIST_SOURCES, build_lists, get_lists_path
```

3b. `get_collectors()` 內把 `HFPapersCollector(),` 移到 `ArxivCollector(),` 之前，並加註解：

```python
    return [
        # HF 在 arXiv 前：單日去重「先收集者留」，同論文優先保留帶 upvotes 的 HF 版
        HFPapersCollector(),
        ArxivCollector(),
        ChatPaperCollector(),
        RSSCollector(),
        ...
```

3c. `run_pipeline` 的 `--force` 清除清單（`for p in [get_raw_path(d), get_scored_path(d)]:` 改成）：

```python
        for p in [get_raw_path(d), get_scored_path(d), get_lists_path(d)]:
```

3d. `run_pipeline` collect stage 結束後（`if not items:` 判斷之後、score stage 之前）加：

```python
    build_lists(items, d)
```

3e. `run_supplement` 在 collect stage 結束後（`if not items:` 判斷之後）加：

```python
    build_lists(items, d, force=changed)  # 補收有新項目時重建清單
```

3f. `run_collect` 在 `collect_items(d)` 取得 items 後、return 前加：

```python
    if items:
        build_lists(items, d, force=force)
```

3g. `run_catchup` 迴圈內 `collect_items(d)` 之後、`if not items: continue` 之後加：

```python
            build_lists(items, d)
```

- [ ] **Step 4: 跑測試確認通過**

Run: `pytest tests/test_pipeline_lists.py -v && pytest tests/ -x -q`
Expected: 新測試 PASS，既有測試不壞（若既有測試斷言 collector 順序需同步修正）

- [ ] **Step 5: Commit**

```bash
git add src/pipeline.py
git commit -m "feat: pipeline 整合 lists stage；HF collector 移到 arXiv 前保住 upvotes"
```

---

### Task 3: 評分排除清單來源 + rules/config 清理

**Files:**
- Modify: `src/pipeline.py`（`score_items` / `score_incremental` 過濾）
- Modify: `src/scoring/rules.py`（移除 hf/github 加分區塊）
- Modify: `config.yaml`（移除失效 keys、加 `lists` 區塊）
- Test: `tests/test_scoring_exclusion.py`

**Interfaces:**
- Consumes: Task 1 的 `LIST_SOURCES`
- Produces: `score_items` / `score_incremental` 進場先剔除 `item.source in LIST_SOURCES`（pinned 剔除由 Task 5 加入同一位置）

- [ ] **Step 1: 寫失敗測試**

```python
"""評分階段排除清單來源。"""
from datetime import date

from src.models import ContentItem, SourceType

D = date(2026, 7, 21)


def _item(source, title):
    return ContentItem(
        source=source, source_name=source.value, title=title,
        url=f"https://example.com/{title}", abstract="x" * 200, published_date=D,
    )


def test_score_items_excludes_list_sources(tmp_path, monkeypatch):
    from src import pipeline

    monkeypatch.setattr(pipeline, "SCORED_DIR", tmp_path)
    received = {}

    def fake_rule_score(items, config):
        received["items"] = items
        return []

    monkeypatch.setattr(pipeline, "batch_rule_score", fake_rule_score)
    monkeypatch.setattr(pipeline, "batch_llm_score", lambda items, config: [])

    items = [
        _item(SourceType.GITHUB, "a-repo"),
        _item(SourceType.ARXIV, "paper"),
        _item(SourceType.RSS, "news"),
    ]
    pipeline.score_items(items, D)
    assert [it.title for it in received["items"]] == ["news"]


def test_rule_score_no_hf_github_bonus():
    from src.scoring.rules import rule_score

    it = _item(SourceType.HF_PAPERS, "some paper")
    it.raw_metadata["upvotes"] = 999
    scored = rule_score(it, {"scoring": {}})
    assert not any("HuggingFace" in r for r in scored.rule_reasons)
```

注意：`score_items` 內部用 `get_scored_path`，其引用 `SCORED_DIR`；若 monkeypatch `SCORED_DIR` 無效（函式綁定原模組變數），改 patch `pipeline.get_scored_path` 為 `lambda d: tmp_path / f"{d}.json"`。

- [ ] **Step 2: 跑測試確認失敗**

Run: `pytest tests/test_scoring_exclusion.py -v`
Expected: FAIL（github/arxiv 未被排除；HF bonus 仍在）

- [ ] **Step 3: `src/pipeline.py` 評分過濾**

`score_items` 在 `console.rule("[bold blue]🔍 篩選階段[/bold blue]")` 之後、`rule_passed = ...` 之前加：

```python
    # 清單來源不評分（拿不到全文，評分不可靠；已由 lists stage 呈現）
    before = len(items)
    items = [it for it in items if it.source not in LIST_SOURCES]
    if before != len(items):
        console.print(f"[dim]📋 清單來源不評分: {before} → {len(items)} items[/dim]")
```

`score_incremental` 在 `new_items = [...]` 計算之後加同樣過濾：

```python
    new_items = [it for it in new_items if it.source not in LIST_SOURCES]
```

- [ ] **Step 4: `src/scoring/rules.py` 清理**

- 刪除區塊 3（HF Daily Papers 收錄加分，`if item.source.value == "hf_papers":` 整段）
- 刪除區塊 4（GitHub stars 加分，`if item.source.value == "github":` 整段）
- 刪除對應變數讀取：`hf_upvote_threshold`、`github_stars_high`、`github_stars_medium` 三行
- 摘要過短懲罰的排除 tuple `("github", "blog", "reddit")` 改為 `("blog", "reddit")`
- 區塊編號註解順移（原 5→3、6→4…），維持可讀性

- [ ] **Step 5: `config.yaml` 清理與新增**

- `scoring:` 區塊刪除 `hf_upvote_bonus_threshold`、`github_stars_high`、`github_stars_medium`
- `source_weights:` 刪除 `arxiv` / `chatpaper` / `hf_papers` / `github` / `semantic_scholar` 五行（不再進評分）
- 頂層（`dedup:` 之前）加：

```yaml
lists:                       # 清單型來源（不評分，天然訊號排序）
  github_top_k: 10
  hf_top_k: 10
  other_papers_limit: 30
```

- 執行 `grep -rn "hf_upvote_bonus_threshold\|github_stars_high\|github_stars_medium" src/ web/ --include="*.py" --include="*.html"`，清掉殘留讀取端（`src/web/config_manager.py` 或 settings 模板若有引用一併移除）

- [ ] **Step 6: 跑測試確認通過**

Run: `pytest tests/test_scoring_exclusion.py -v && pytest tests/ -x -q`
Expected: 新測試 PASS；既有 rules 測試若斷言 hf/github 加分需同步刪除該測試案例

- [ ] **Step 7: Commit**

```bash
git add src/pipeline.py src/scoring/rules.py config.yaml
git commit -m "feat: 評分排除清單來源；移除 hf/github 規則加分與失效 config"
```

---

### Task 4: `src/pinned.py` — 置頂挑選模組 + config

**Files:**
- Create: `src/pinned.py`
- Modify: `config.yaml`（加 `pinned_organizations` / `pinned_daily_limit`）
- Test: `tests/test_pinned.py`

**Interfaces:**
- Consumes: `src/models.py` 的 `ContentItem / ScoredItem / SourceType`
- Produces:
  - `select_pinned(items: list[ContentItem], target_date: date, config: dict) -> list[ContentItem]`
  - `to_pinned_scored(item: ContentItem) -> ScoredItem`（rule_reasons 含 `"pinned"`、llm_reason 為置頂說明）
  - `PINNED_WINDOW_DAYS = 1`

- [ ] **Step 1: 寫失敗測試 `tests/test_pinned.py`**

```python
"""頂尖 AI 公司官方 blog 置頂挑選測試。"""
from datetime import date, timedelta

from src.models import ContentItem, SourceType
from src.pinned import select_pinned, to_pinned_scored

D = date(2026, 7, 21)
CFG = {"pinned_organizations": ["OpenAI", "Anthropic", "Google"], "pinned_daily_limit": 2}


def _item(org, title, source=SourceType.RSS, pub=D):
    return ContentItem(
        source=source, source_name="RSS", title=title,
        url=f"https://example.com/{title}", abstract="x" * 200,
        published_date=pub, organization=org,
    )


def test_hit_org_selected():
    items = [_item("OpenAI", "gpt-6"), _item("", "random news")]
    assert [it.title for it in select_pinned(items, D, CFG)] == ["gpt-6"]


def test_org_substring_match():
    # config "Google" 需命中 organization "Google DeepMind"
    items = [_item("Google DeepMind", "gemini-4")]
    assert len(select_pinned(items, D, CFG)) == 1


def test_daily_limit():
    items = [_item("OpenAI", f"post-{i}") for i in range(4)]
    assert len(select_pinned(items, D, CFG)) == 2


def test_date_window():
    ok = _item("OpenAI", "yesterday", pub=D - timedelta(days=1))   # UTC 時差容忍
    stale = _item("OpenAI", "old", pub=D - timedelta(days=3))
    got = select_pinned([ok, stale], D, CFG)
    assert [it.title for it in got] == ["yesterday"]


def test_non_blog_source_excluded():
    items = [_item("OpenAI", "hn item", source=SourceType.HACKERNEWS)]
    assert select_pinned(items, D, CFG) == []


def test_to_pinned_scored():
    scored = to_pinned_scored(_item("OpenAI", "gpt-6"))
    assert "pinned" in scored.rule_reasons
    assert scored.total_score == 0
    assert "官方發布" in scored.llm_reason
```

- [ ] **Step 2: 跑測試確認失敗**

Run: `pytest tests/test_pinned.py -v`
Expected: FAIL（`No module named 'src.pinned'`）

- [ ] **Step 3: 實作 `src/pinned.py`**

```python
"""頂尖 AI 公司官方 blog 免評分置頂挑選。

命中 config `pinned_organizations` 的 RSS/blog 來源當天（±1 天，容忍 UTC 時差）
發布項目，繞過評分直接生成，frontmatter 標 pinned。挑選為純函式、確定性，
score 階段（排除 pool）與 generate 階段（挑生成對象）呼叫同一份邏輯保持一致。
"""

from __future__ import annotations

from datetime import date

from src.models import ContentItem, ScoredItem, SourceType

# 允許前一天發布：pipeline 於 UTC 18:00 跑當日，官方 blog 常在收集時間之後發布、
# 隔天才進 raw，嚴格 == target_date 會漏掉大半
PINNED_WINDOW_DAYS = 1

PINNED_LLM_REASON = "📌 頂尖 AI 公司官方發布"


def _org_hit(org: str, pinned_orgs: list[str]) -> bool:
    if not org:
        return False
    org_lower = org.lower()
    return any(p.lower() in org_lower for p in pinned_orgs)


def select_pinned(
    items: list[ContentItem], target_date: date, config: dict
) -> list[ContentItem]:
    """挑出應置頂生成的官方 blog 項目（依日期新→舊，上限 pinned_daily_limit）。"""
    pinned_orgs = config.get("pinned_organizations", [])
    limit = config.get("pinned_daily_limit", 5)
    if not pinned_orgs:
        return []

    hits = [
        it
        for it in items
        if it.source in (SourceType.RSS, SourceType.BLOG)
        and abs((target_date - it.published_date).days) <= PINNED_WINDOW_DAYS
        and _org_hit(it.organization, pinned_orgs)
    ]
    hits.sort(key=lambda it: it.published_date, reverse=True)
    return hits[:limit]


def to_pinned_scored(item: ContentItem) -> ScoredItem:
    """包成 pseudo-ScoredItem 走現有 generator（分數 0、理由標明置頂）。"""
    return ScoredItem(item=item, rule_score=0.0, rule_reasons=["pinned"], llm_reason=PINNED_LLM_REASON)
```

- [ ] **Step 4: `config.yaml` 加置頂設定**

頂層 `lists:` 區塊之前加（拼法對齊 `src/collectors/_helpers.py` 的 `_NAME_TO_ORG` / `_DOMAIN_TO_ORG` 輸出值；智譜/Moonshot/MiniMax 目前無對應 feed，先佔位供未來 feed 啟用）：

```yaml
pinned_organizations:        # 頂尖 AI 公司官方 blog 免評分置頂（比對 ContentItem.organization）
  - OpenAI
  - Anthropic
  - Google                   # 同時命中 Google / Google DeepMind
  - DeepSeek
  - Meta                     # 同時命中 Meta AI
  - xAI
  - Mistral
  - Zhipu AI                 # 智譜 GLM（暫無 feed，佔位）
  - Moonshot AI              # Kimi（暫無 feed，佔位）
  - MiniMax                  # （暫無 feed，佔位）
pinned_daily_limit: 5
```

- [ ] **Step 5: 跑測試確認通過**

Run: `pytest tests/test_pinned.py -v`
Expected: 全部 PASS

- [ ] **Step 6: Commit**

```bash
git add src/pinned.py config.yaml
git commit -m "feat: pinned 模組 — 頂尖 AI 公司官方 blog 置頂挑選"
```

---

### Task 5: Pinned 生成整合（generator frontmatter + pipeline）

**Files:**
- Modify: `src/generators/blog_post.py`（`save_blog_post` / `generate_and_save_posts` 加 `pinned` 參數）
- Modify: `src/pipeline.py`（`generate_posts` 前置 pinned 生成；`score_items` / `score_incremental` 剔除 pinned）
- Test: `tests/test_pinned_generation.py`

**Interfaces:**
- Consumes: Task 4 的 `select_pinned` / `to_pinned_scored`
- Produces:
  - `save_blog_post(gen, target_date=None, pinned=False) -> str`（pinned 時 frontmatter 加 `pinned: true`、不寫 `score`）
  - `generate_and_save_posts(items, target_date=None, pinned=False) -> list[str]`
  - `pipeline.generate_posts(top_items, target_date=None)` 內部先生成 pinned 再生成 top-K

- [ ] **Step 1: 寫失敗測試 `tests/test_pinned_generation.py`**

```python
"""Pinned 生成整合測試。"""
from datetime import date, datetime

import yaml

from src.models import ContentItem, GeneratedContent, SourceType
from src.pinned import to_pinned_scored

D = date(2026, 7, 21)


def _gen(title="OpenAI ships GPT-6"):
    item = ContentItem(
        source=SourceType.RSS, source_name="OpenAI Blog", title=title,
        url="https://openai.com/blog/gpt-6", abstract="x" * 200,
        published_date=D, organization="OpenAI",
    )
    return GeneratedContent(
        source_item=to_pinned_scored(item), content="📌 內容", prompt_used="p",
        model_used="m", generated_at=datetime(2026, 7, 21, 3, 0),
    )


def test_save_blog_post_pinned_frontmatter(tmp_path, monkeypatch):
    import src.generators.blog_post as bp

    monkeypatch.setattr(bp, "POSTS_DIR", tmp_path)
    monkeypatch.setattr(bp, "PROMPTS_DIR", tmp_path)
    path = bp.save_blog_post(_gen(), D, pinned=True)
    fm = yaml.safe_load(open(path).read().split("---")[1])
    assert fm["pinned"] is True
    assert "score" not in fm  # 置頂文沒有評分，不寫誤導性的 0 分


def test_save_blog_post_normal_no_pinned_key(tmp_path, monkeypatch):
    import src.generators.blog_post as bp

    monkeypatch.setattr(bp, "POSTS_DIR", tmp_path)
    monkeypatch.setattr(bp, "PROMPTS_DIR", tmp_path)
    path = bp.save_blog_post(_gen(), D)  # pinned 預設 False
    fm = yaml.safe_load(open(path).read().split("---")[1])
    assert "pinned" not in fm
    assert fm["score"] == 0


def test_generate_posts_runs_pinned_first(tmp_path, monkeypatch):
    from src import pipeline
    from src.models import ScoredItem

    d = D
    raw_item = {
        "source": "rss", "source_name": "OpenAI Blog", "title": "GPT-6",
        "url": "https://openai.com/blog/gpt-6", "abstract": "x" * 200,
        "published_date": d.isoformat(), "organization": "OpenAI",
    }
    raw_path = tmp_path / f"{d.isoformat()}.json"
    import json
    raw_path.write_text(json.dumps([raw_item]))
    monkeypatch.setattr(pipeline, "get_raw_path", lambda dd: raw_path)
    monkeypatch.setattr(pipeline, "POSTS_DIR", tmp_path)  # checkpoint 檢查用

    calls = []

    def fake_generate(items, target_date=None, pinned=False):
        calls.append((pinned, [it.item.title for it in items]))
        return [f"/fake/{it.item.title}.md" for it in items]

    import src.generators.blog_post as bp
    monkeypatch.setattr(bp, "generate_and_save_posts", fake_generate)

    paths = pipeline.generate_posts([], d)
    assert calls[0][0] is True          # pinned 批先跑
    assert calls[0][1] == ["GPT-6"]
    assert len(paths) == 1


def test_score_items_excludes_pinned(tmp_path, monkeypatch):
    from src import pipeline
    from src.models import ContentItem

    monkeypatch.setattr(pipeline, "get_scored_path", lambda d: tmp_path / f"{d}.json")
    received = {}
    monkeypatch.setattr(
        pipeline, "batch_rule_score",
        lambda items, config: received.update(items=items) or [],
    )
    monkeypatch.setattr(pipeline, "batch_llm_score", lambda items, config: [])
    monkeypatch.setattr(
        pipeline, "load_config",
        lambda: {"pinned_organizations": ["OpenAI"], "pinned_daily_limit": 5, "scoring": {}},
    )

    pinned_item = ContentItem(
        source=SourceType.RSS, source_name="OpenAI Blog", title="GPT-6",
        url="https://openai.com/blog/gpt-6", abstract="x" * 200,
        published_date=D, organization="OpenAI",
    )
    normal = ContentItem(
        source=SourceType.RSS, source_name="TechCrunch AI", title="other news",
        url="https://example.com/news", abstract="x" * 200, published_date=D,
    )
    pipeline.score_items([pinned_item, normal], D)
    assert [it.title for it in received["items"]] == ["other news"]
```

- [ ] **Step 2: 跑測試確認失敗**

Run: `pytest tests/test_pinned_generation.py -v`
Expected: FAIL（`save_blog_post` 不收 `pinned` 參數等）

- [ ] **Step 3: 修改 `src/generators/blog_post.py`**

3a. `save_blog_post` 簽名改 `def save_blog_post(gen: GeneratedContent, target_date: date | None = None, pinned: bool = False) -> str:`，frontmatter 組裝改為：

```python
    frontmatter = {
        "title": gen.source_item.item.title,
        "source": gen.source_item.item.source_name,
        "url": gen.source_item.item.url,
        "model": gen.model_used,
        "generated_at": gen.generated_at.isoformat(),
    }
    if pinned:
        # 置頂文沒有評分：不寫 score（0 分會誤導），改標 pinned 供兩個 GUI 置頂
        frontmatter["pinned"] = True
    else:
        frontmatter["score"] = round(gen.source_item.total_score)
```

（key 順序調整後記得 `score` 放 `url` 之後、`model` 之前也可，維持既有欄位序即可。）

3b. `generate_and_save_posts` 簽名改 `def generate_and_save_posts(items: list[ScoredItem], target_date: date | None = None, pinned: bool = False) -> list[str]:`，內部 `save_blog_post(gen, target_date)` 改 `save_blog_post(gen, target_date, pinned=pinned)`。

- [ ] **Step 4: 修改 `src/pipeline.py`**

4a. import 加：

```python
from src.pinned import select_pinned, to_pinned_scored
```

4b. `score_items` 的清單來源過濾（Task 3 加的那段）擴充 pinned 剔除，整段改為：

```python
    # 清單來源不評分；pinned 官方 blog 繞過評分直接生成（generate 階段處理）
    pinned_keys = {it.dedup_key() for it in select_pinned(items, target_date, config)}
    before = len(items)
    items = [
        it for it in items
        if it.source not in LIST_SOURCES and it.dedup_key() not in pinned_keys
    ]
    if before != len(items):
        console.print(f"[dim]📋 清單/置頂來源不評分: {before} → {len(items)} items[/dim]")
```

（此段需在 `config = load_config()` 之後。）`score_incremental` 的 new_items 過濾同樣擴充：

```python
    config = load_config()
    pinned_keys = {it.dedup_key() for it in select_pinned(all_items, target_date, config)}
    new_items = [
        it for it in new_items
        if it.source not in LIST_SOURCES and it.dedup_key() not in pinned_keys
    ]
```

（`score_incremental` 原本在過濾後才 `config = load_config()`，把該行上移避免重複。）

4c. `generate_posts` 改為：

```python
def generate_posts(top_items: list[ScoredItem], target_date: date | None = None) -> list[str]:
    """生成 blog posts：先置頂官方 blog（免評分），再生成評分 top-K。"""
    from src.generators.blog_post import generate_and_save_posts

    target_date = target_date or date.today()

    console.rule("[bold blue]✍️ 生成階段[/bold blue]")

    pinned_paths = _generate_pinned_posts(target_date)
    paths = generate_and_save_posts(top_items, target_date)
    return pinned_paths + paths


def _generate_pinned_posts(target_date: date) -> list[str]:
    """頂尖 AI 公司官方 blog 免評分直接生成（逐篇 checkpoint：已有同名 post 跳過）。"""
    from src.generators.blog_post import generate_and_save_posts
    from src.utils import slugify

    raw_path = get_raw_path(target_date)
    if not raw_path.exists():
        return []

    config = load_config()
    items = [ContentItem(**r) for r in load_json(raw_path)]
    todo = []
    for it in select_pinned(items, target_date, config):
        post_path = POSTS_DIR / f"{target_date.isoformat()}_{slugify(it.title)}.md"
        if post_path.exists():
            continue
        todo.append(to_pinned_scored(it))

    if not todo:
        return []

    console.print(f"[bold]📌 置頂生成: {len(todo)} 篇頂尖 AI 公司官方發布[/bold]")
    paths = generate_and_save_posts(todo, target_date, pinned=True)
    if len(paths) < len(todo):
        _logger.warning(
            "部分置頂文章生成失敗",
            extra={"expected": len(todo), "generated": len(paths)},
        )
    return paths
```

（`slugify` 若 utils 已 import 於檔頭則不需區域 import；`POSTS_DIR` 已在 import 清單。）

- [ ] **Step 5: 跑測試確認通過**

Run: `pytest tests/test_pinned_generation.py tests/test_scoring_exclusion.py -v && pytest tests/ -x -q`
Expected: 全部 PASS

- [ ] **Step 6: Commit**

```bash
git add src/generators/blog_post.py src/pipeline.py
git commit -m "feat: pinned 官方 blog 免評分直接生成，frontmatter 標 pinned"
```

---

### Task 6: Web Monitor — get_day_lists + Day Detail 分頁

**Files:**
- Modify: `src/web/data_service.py`（加 `get_day_lists`）
- Modify: `src/web/app.py`（`/day/{date_str}` 路由傳入 lists）
- Modify: `src/web/templates/day_detail.html`（tab bar + Trending / Papers 區塊）
- Test: `tests/test_web_lists.py`

**Interfaces:**
- Consumes: Task 1 的 lists JSON 格式（`{date, github[], papers:{hf[], others[]}}`）
- Produces: `get_day_lists(d: date) -> dict | None`（無檔 / 損毀 / 非 dict 皆回 None）

- [ ] **Step 1: 寫失敗測試 `tests/test_web_lists.py`**

```python
"""Web data_service 的 lists 讀取測試。"""
from datetime import date

from src.web import data_service

D = date(2026, 7, 21)


def test_get_day_lists_missing_returns_none(tmp_path, monkeypatch):
    monkeypatch.setattr(data_service, "LISTS_DIR", tmp_path)
    assert data_service.get_day_lists(D) is None


def test_get_day_lists_reads_json(tmp_path, monkeypatch):
    monkeypatch.setattr(data_service, "LISTS_DIR", tmp_path)
    (tmp_path / "2026-07-21.json").write_text(
        '{"date": "2026-07-21", "github": [], "papers": {"hf": [], "others": []}}'
    )
    data = data_service.get_day_lists(D)
    assert data["date"] == "2026-07-21"


def test_get_day_lists_corrupt_returns_none(tmp_path, monkeypatch):
    monkeypatch.setattr(data_service, "LISTS_DIR", tmp_path)
    (tmp_path / "2026-07-21.json").write_text("{not valid json")
    assert data_service.get_day_lists(D) is None
```

- [ ] **Step 2: 跑測試確認失敗**

Run: `pytest tests/test_web_lists.py -v`
Expected: FAIL（`data_service` 無 `get_day_lists` / `LISTS_DIR`）

- [ ] **Step 3: `src/web/data_service.py` 加函式**

import 區把 `LISTS_DIR` 加進既有 `from src.utils import ...`；在 `get_day_raw_items` 之後加：

```python
def get_day_lists(d: date) -> dict | None:
    """讀取當日清單檔（Trending / Papers）。無檔、損毀、格式不符皆回 None（tab 隱藏）。"""
    path = LISTS_DIR / f"{d.isoformat()}.json"
    if not path.exists():
        return None
    try:
        data = load_json(path)
    except Exception as e:
        _logger.warning("Lists 檔讀取失敗", extra={"date": str(d), "error": str(e)})
        return None
    return data if isinstance(data, dict) else None
```

（若模組頂端 logger 名稱不同，沿用該檔既有 logger 變數。）

- [ ] **Step 4: `src/web/app.py` day 路由傳入 lists**

`/day/{date_str}` 路由（`app.py:182` 附近）的 template context dict 加一行：

```python
        "lists": data_service.get_day_lists(d),
```

- [ ] **Step 5: `src/web/templates/day_detail.html` 加分頁**

5a. 在「收集文章」section（`<!-- Scored items (card-style list) -->`）之前插入 tab bar：

```html
{% if lists %}
<div class="day-tabs" id="day-tabs">
  <button class="day-tab day-tab-active" data-tab="scored" onclick="switchDayTab(this)">📊 評分文章</button>
  <button class="day-tab" data-tab="trending" onclick="switchDayTab(this)">🔥 Trending <span class="sf-count">{{ lists.github|length }}</span></button>
  <button class="day-tab" data-tab="papers" onclick="switchDayTab(this)">📄 Papers <span class="sf-count">{{ lists.papers.hf|length + lists.papers.others|length }}</span></button>
</div>
{% endif %}
```

5b. 把既有整個「收集文章」`<section>` 包進 `<div id="day-tab-scored">`；其後加兩個預設隱藏的區塊：

```html
{% if lists %}
<div id="day-tab-trending" hidden>
  <section>
    <h3 class="section-title-sm">🔥 GitHub Trending Top {{ lists.github|length }}</h3>
    {% if lists.github %}
    <div class="card" style="overflow:hidden;">
      {% for e in lists.github %}
      <details class="list-item">
        <summary>
          <span class="li-rank">{{ loop.index }}</span>
          <span class="li-title">{{ e.title }}</span>
          <span class="li-badges">
            <span class="li-badge">⭐ +{{ e.stars_today }} today</span>
            {% if e.language %}<span class="li-badge">{{ e.language }}</span>{% endif %}
          </span>
        </summary>
        <div class="li-body">
          <p>{{ e.abstract or "（無簡介）" }}</p>
          <a href="{{ e.url }}" target="_blank" rel="noopener">前往 GitHub ↗</a>
        </div>
      </details>
      {% endfor %}
    </div>
    {% else %}<p class="empty-note">今日無資料</p>{% endif %}
  </section>
</div>

<div id="day-tab-papers" hidden>
  <section>
    <h3 class="section-title-sm">📄 HuggingFace Daily Papers Top {{ lists.papers.hf|length }}</h3>
    {% if lists.papers.hf %}
    <div class="card" style="overflow:hidden;">
      {% for e in lists.papers.hf %}
      <details class="list-item">
        <summary>
          <span class="li-rank">{{ loop.index }}</span>
          <span class="li-title">{{ e.title }}</span>
          <span class="li-badges"><span class="li-badge">👍 {{ e.upvotes }}</span></span>
        </summary>
        <div class="li-body">
          <p>{{ e.abstract or "（無摘要）" }}</p>
          <a href="{{ e.url }}" target="_blank" rel="noopener">前往 HF ↗</a>
        </div>
      </details>
      {% endfor %}
    </div>
    {% else %}<p class="empty-note">今日無資料</p>{% endif %}

    {% if lists.papers.others %}
    <h3 class="section-title-sm" style="margin-top:16px;">更多論文（{{ lists.papers.others|length }}）</h3>
    <div class="card" style="overflow:hidden;">
      {% for e in lists.papers.others %}
      <details class="list-item">
        <summary>
          <span class="li-rank">{{ loop.index }}</span>
          <span class="li-title">{{ e.title }}</span>
          <span class="li-badges">
            <span class="li-badge">{{ e.source_name }}</span>
            {% if e.citation_count %}<span class="li-badge">📖 {{ e.citation_count }}</span>{% endif %}
          </span>
        </summary>
        <div class="li-body">
          <p>{{ e.abstract or "（無摘要）" }}</p>
          <a href="{{ e.url }}" target="_blank" rel="noopener">前往原文 ↗</a>
        </div>
      </details>
      {% endfor %}
    </div>
    {% endif %}
  </section>
</div>
{% endif %}
```

5c. 頁尾 script 區加切換函式，`<style>` 區加樣式（沿用該模板既有 CSS 變數 `--t4`/`--br2`/`--ay` 等命名風格）：

```html
<script>
function switchDayTab(btn) {
  document.querySelectorAll('.day-tab').forEach(b => b.classList.remove('day-tab-active'));
  btn.classList.add('day-tab-active');
  ['scored', 'trending', 'papers'].forEach(name => {
    const el = document.getElementById('day-tab-' + name);
    if (el) el.hidden = (name !== btn.dataset.tab);
  });
}
</script>
<style>
.day-tabs { display:flex; gap:6px; margin:14px 0 10px; border-bottom:1px solid var(--br2); }
.day-tab { background:none; border:none; border-bottom:2px solid transparent; padding:6px 12px;
  color:var(--t4); font-size:13px; cursor:pointer; }
.day-tab-active { color:var(--ab); border-bottom-color:var(--ab); font-weight:600; }
.list-item summary { display:flex; align-items:center; gap:10px; padding:10px 18px;
  cursor:pointer; list-style:none; }
.list-item summary::-webkit-details-marker { display:none; }
.list-item + .list-item { border-top:1px solid var(--br2); }
.li-rank { color:var(--t5); font-size:12px; min-width:20px; }
.li-title { flex:1; font-size:13.5px; }
.li-badges { display:flex; gap:6px; flex-shrink:0; }
.li-badge { font-size:11px; color:var(--t4); border:1px solid var(--br2);
  border-radius:5px; padding:0 6px; }
.li-body { padding:4px 18px 12px 48px; font-size:13px; color:var(--t3); line-height:1.6; }
.empty-note { color:var(--t5); font-size:13px; padding:12px 0; }
</style>
```

（實作時對照模板實際的 CSS 變數名，不存在的變數換成該檔已用的等價色票。）

- [ ] **Step 6: 跑測試 + 手動驗證**

Run: `pytest tests/test_web_lists.py -v`
Expected: PASS

手動驗證：`python -m src.cli web` → 開 `http://127.0.0.1:8555/day/<有 lists 檔的日期>`：
- 三個 tab 可切換；Trending/Papers 卡片可展開 abstract；外連正常
- 開一個舊日期（無 lists 檔）：tab bar 不出現、原評分列表照常

- [ ] **Step 7: Commit**

```bash
git add src/web/data_service.py src/web/app.py src/web/templates/day_detail.html
git commit -m "feat: Web Monitor Day Detail 加 Trending/Papers 分頁"
```

---

### Task 7: Astro — lists 載入 + Trending 頁（列表＋詳情）

**Files:**
- Create: `web/src/lists.ts`
- Modify: `web/src/components/Nav.astro`
- Create: `web/src/pages/trending/index.astro`
- Create: `web/src/pages/trending/[slug].astro`

**Interfaces:**
- Consumes: `output/lists/*.json`（Task 1 格式）、`web/src/utils.ts` 的 `recentCutoff / RECENT_DAYS`
- Produces:
  - `lists.ts`：`interface DayLists`、`loadLists(): DayLists[]`（近 30 天、日期新→舊）
  - Nav `active` type 擴充為 `'curated' | 'daily' | 'trending' | 'papers'`
  - 詳情頁路由 `/trending/{date}_{slug}`

- [ ] **Step 1: 寫 `web/src/lists.ts`**

```ts
import { RECENT_DAYS, recentCutoff } from './utils';

export interface GithubEntry {
  title: string;
  slug: string;
  url: string;
  abstract: string;
  stars_today: number;
  language: string;
}

export interface HfEntry {
  title: string;
  slug: string;
  url: string;
  abstract: string;
  upvotes: number;
  arxiv_id: string;
  authors: string[];
}

export interface OtherEntry {
  title: string;
  slug: string;
  url: string;
  abstract: string;
  source: string;
  source_name: string;
  citation_count: number;
  published_date: string;
  authors: string[];
}

export interface DayLists {
  date: string;
  github: GithubEntry[];
  papers: { hf: HfEntry[]; others: OtherEntry[] };
}

// build 時直讀 pipeline 產出的 lists JSON（與 posts 同策略：近 N 天）
const modules = import.meta.glob<DayLists>('../../output/lists/*.json', {
  eager: true,
  import: 'default',
});

export function loadLists(days = RECENT_DAYS): DayLists[] {
  const cutoff = recentCutoff(days);
  return Object.values(modules)
    .filter((d) => new Date(`${d.date}T00:00:00Z`) >= cutoff)
    .sort((a, b) => b.date.localeCompare(a.date));
}
```

- [ ] **Step 2: `Nav.astro` 加 tab**

Props 型別改 `active: 'curated' | 'daily' | 'trending' | 'papers';`，nav 內加：

```astro
  <a href="/trending" class:list={['tab', { active: active === 'trending' }]}>
    🔥 Trending
  </a>
  <a href="/papers" class:list={['tab', { active: active === 'papers' }]}>
    📄 Papers
  </a>
```

- [ ] **Step 3: `web/src/pages/trending/index.astro`**

```astro
---
import Base from '../../layouts/Base.astro';
import Nav from '../../components/Nav.astro';
import { loadLists } from '../../lists';
import { formatDate, RECENT_DAYS } from '../../utils';

const days = loadLists().filter((d) => d.github.length > 0);
const weekdayFmt = new Intl.DateTimeFormat('zh-TW', { weekday: 'short', timeZone: 'UTC' });
---

<Base title="GitHub Trending — Daily AI Blog" wide>
  <Nav active="trending" />
  <p class="page-desc">每日 GitHub Trending Top 10（依當日新增 star 排序，近 {RECENT_DAYS} 天）</p>

  {days.length === 0 && <p class="empty">尚無 Trending 資料。</p>}

  {days.map((d) => (
    <section class="day-block">
      <h2 class="day-header">
        {d.date} · {weekdayFmt.format(new Date(`${d.date}T00:00:00Z`))}
        <span class="day-count">{d.github.length} repos</span>
      </h2>
      <ul class="entry-list">
        {d.github.map((e, i) => (
          <li class="entry">
            <a href={`/trending/${d.date}_${e.slug}`} class="entry-link">
              <span class="rank">{i + 1}</span>
              <div class="entry-main">
                <h3 class="entry-title">{e.title}</h3>
                {e.abstract && <p class="entry-abstract">{e.abstract.slice(0, 160)}{e.abstract.length > 160 ? '…' : ''}</p>}
              </div>
              <span class="badges">
                <span class="badge stars">⭐ +{e.stars_today}</span>
                {e.language && <span class="badge">{e.language}</span>}
              </span>
            </a>
          </li>
        ))}
      </ul>
    </section>
  ))}
</Base>

<style>
  .page-desc { color: var(--muted); font-size: 0.85rem; margin: 0 0 1.5rem; }
  .day-block { margin-bottom: 2rem; }
  .day-header { display: flex; align-items: center; gap: 0.6rem; font-family: var(--mono);
    font-size: 0.85rem; color: var(--muted); border-bottom: 1px solid var(--border);
    padding-bottom: 0.4rem; margin: 0 0 0.7rem; font-weight: 600; }
  .day-count { background: var(--surface); border-radius: 5px; padding: 0 0.4rem;
    font-size: 0.74rem; color: var(--faint); }
  .entry-list { list-style: none; margin: 0; padding: 0; display: flex;
    flex-direction: column; gap: 0.5rem; }
  .entry { border: 1px solid var(--border); border-radius: var(--radius);
    background: var(--surface); transition: border-color 0.15s ease; }
  .entry:hover { border-color: var(--accent); }
  .entry-link { display: flex; align-items: flex-start; gap: 0.8rem;
    padding: 0.75rem 1.1rem; color: inherit; }
  .rank { font-family: var(--mono); color: var(--faint); font-size: 0.8rem;
    min-width: 1.4rem; padding-top: 0.15rem; }
  .entry-main { flex: 1; min-width: 0; }
  .entry-title { margin: 0 0 0.25rem; font-size: 0.98rem; }
  .entry:hover .entry-title { color: var(--accent); }
  .entry-abstract { margin: 0; color: var(--muted); font-size: 0.82rem; line-height: 1.5; }
  .badges { display: flex; flex-direction: column; gap: 0.3rem; align-items: flex-end;
    flex-shrink: 0; }
  .badge { font-family: var(--mono); font-size: 0.72rem; color: var(--muted);
    border: 1px solid var(--border-strong); border-radius: 5px; padding: 0 0.4rem; }
  .badge.stars { color: var(--accent-2); }
  .empty { color: var(--muted); text-align: center; padding: 3rem 0; }
</style>
```

- [ ] **Step 4: `web/src/pages/trending/[slug].astro`**

```astro
---
import Base from '../../layouts/Base.astro';
import { loadLists } from '../../lists';
import { formatDate } from '../../utils';

export async function getStaticPaths() {
  return loadLists().flatMap((d) =>
    d.github.map((e) => ({
      params: { slug: `${d.date}_${e.slug}` },
      props: { entry: e, date: d.date },
    }))
  );
}

const { entry, date } = Astro.props;
---

<Base title={`${date} · ${entry.title}`} description="GitHub Trending">
  <nav class="topnav">
    <a href="/trending" class="back"><span aria-hidden="true">←</span> Trending</a>
  </nav>
  <article>
    <header class="detail-header">
      <div class="meta-row">
        <time>{formatDate(new Date(`${date}T00:00:00Z`))}</time>
        <span class="badge">⭐ +{entry.stars_today} today</span>
        {entry.language && <span class="badge">{entry.language}</span>}
      </div>
      <h1>{entry.title}</h1>
      <a class="src-link" href={entry.url} target="_blank" rel="noopener">
        🔗 {entry.url} ↗
      </a>
    </header>
    <div class="abstract">
      {entry.abstract ? <p>{entry.abstract}</p> : <p class="none">（來源未提供簡介）</p>}
    </div>
    <p class="note">內容為收集當日抓取的 repo 描述原文，完整資訊請見 GitHub 原頁。</p>
  </article>
</Base>

<style>
  .topnav { margin-bottom: 1.5rem; }
  .back { font-family: var(--mono); font-size: 0.85rem; color: var(--muted); }
  .back:hover { color: var(--accent); }
  .detail-header { border-bottom: 1px solid var(--border); padding-bottom: 1.2rem;
    margin-bottom: 1.4rem; }
  .meta-row { display: flex; gap: 0.6rem; font-family: var(--mono); font-size: 0.8rem;
    color: var(--faint); }
  .badge { border: 1px solid var(--border-strong); border-radius: 5px; padding: 0 0.4rem;
    color: var(--accent-2); }
  h1 { margin: 0.55rem 0 0.85rem; font-size: 1.6rem; }
  .src-link { font-family: var(--mono); font-size: 0.82rem; color: var(--muted);
    word-break: break-all; }
  .src-link:hover { color: var(--accent); }
  .abstract p { line-height: 1.7; }
  .none { color: var(--faint); }
  .note { margin-top: 2rem; color: var(--faint); font-size: 0.8rem; }
</style>
```

- [ ] **Step 5: Build 驗證**

Run: `cd web && npm run build`
Expected: build 成功；`dist/trending/index.html` 存在；有 lists 檔的日期產出 `dist/trending/<date>_<slug>/index.html`。若本地 `output/lists/` 還沒有任何檔案，先跑 `python -m src.cli collect` 產一份（今日）再 build。

- [ ] **Step 6: Commit**

```bash
git add web/src/lists.ts web/src/components/Nav.astro web/src/pages/trending/
git commit -m "feat: Astro Trending 分頁（每日 top 10 + 詳情頁）"
```

---

### Task 8: Astro — Papers 頁（列表＋詳情）

**Files:**
- Create: `web/src/pages/papers/index.astro`
- Create: `web/src/pages/papers/[slug].astro`

**Interfaces:**
- Consumes: Task 7 的 `loadLists()` 與 `HfEntry / OtherEntry`
- Produces: 路由 `/papers`、`/papers/{date}_{slug}`

- [ ] **Step 1: `web/src/pages/papers/index.astro`**

結構與 trending/index.astro 相同（複製後調整），差異：
- `Nav active="papers"`；標題「每日論文精選（HF Daily Papers 依社群投票排序，近 N 天）」
- 每日區塊主清單列 `d.papers.hf`（badge 用 `👍 {e.upvotes}`），連結 `/papers/${d.date}_${e.slug}`
- 主清單之後，若 `d.papers.others.length > 0`，加 `<details class="others">`（預設折疊）：

```astro
      {d.papers.others.length > 0 && (
        <details class="others">
          <summary>更多論文（arXiv / ChatPaper / Semantic Scholar，{d.papers.others.length} 篇）</summary>
          <ul class="entry-list">
            {d.papers.others.map((e, i) => (
              <li class="entry">
                <a href={`/papers/${d.date}_${e.slug}`} class="entry-link">
                  <span class="rank">{i + 1}</span>
                  <div class="entry-main">
                    <h3 class="entry-title">{e.title}</h3>
                    {e.abstract && <p class="entry-abstract">{e.abstract.slice(0, 160)}…</p>}
                  </div>
                  <span class="badges">
                    <span class="badge">{e.source_name}</span>
                    {e.citation_count > 0 && <span class="badge">📖 {e.citation_count}</span>}
                  </span>
                </a>
              </li>
            ))}
          </ul>
        </details>
      )}
```

- days filter 條件改 `d.papers.hf.length > 0 || d.papers.others.length > 0`
- `.others summary` 樣式：`font-family: var(--mono); font-size: 0.8rem; color: var(--muted); cursor: pointer; padding: 0.5rem 0;`

- [ ] **Step 2: `web/src/pages/papers/[slug].astro]`**

比照 trending/[slug].astro，差異：

```astro
export async function getStaticPaths() {
  return loadLists().flatMap((d) => [
    ...d.papers.hf.map((e) => ({
      params: { slug: `${d.date}_${e.slug}` },
      props: { title: e.title, url: e.url, abstract: e.abstract, date: d.date,
               badge: `👍 ${e.upvotes} upvotes`, sourceName: 'HuggingFace Daily Papers',
               authors: e.authors },
    })),
    ...d.papers.others.map((e) => ({
      params: { slug: `${d.date}_${e.slug}` },
      props: { title: e.title, url: e.url, abstract: e.abstract, date: d.date,
               badge: e.citation_count > 0 ? `📖 ${e.citation_count} citations` : '',
               sourceName: e.source_name, authors: e.authors },
    })),
  ]);
}
```

頁面呈現：日期 + sourceName badge + badge（有值才顯示）+ 標題 + authors（有值時 `作者：{authors.slice(0, 8).join(', ')}`）+ 完整 abstract + 原文外連 + 底部註記「內容為收集當日抓取的摘要原文」。返回連結 `← Papers` 指 `/papers`。

**去重防呆**：同一天 hf 與 others 理論上不重複（collect 端已用 arxiv_id 去重），但 getStaticPaths 產生的 slug 若重複 Astro build 會炸。在 return 前加：

```ts
  const seen = new Set<string>();
  return paths.filter((p) => {
    if (seen.has(p.params.slug)) return false;
    seen.add(p.params.slug);
    return true;
  });
```

（把上面 flatMap 結果先存 `const paths = ...` 再過濾。）

- [ ] **Step 3: Build 驗證**

Run: `cd web && npm run build`
Expected: build 成功；`dist/papers/` 產出列表與詳情頁。

- [ ] **Step 4: Commit**

```bash
git add web/src/pages/papers/
git commit -m "feat: Astro Papers 分頁（HF top 10 + 更多論文折疊 + 詳情頁）"
```

---

### Task 9: Astro — 首頁 pinned 置頂

**Files:**
- Modify: `web/src/content.config.ts`（posts schema 加 `pinned`）
- Modify: `web/src/pages/index.astro`（排序 + 📌 badge）

**Interfaces:**
- Consumes: Task 5 產出的 post frontmatter `pinned: true`
- Produces: 首頁同日群組內 pinned 文章排最前 + 📌 badge

- [ ] **Step 1: `content.config.ts` posts schema 加欄位**

```ts
    pinned: z.boolean().default(false),
```

- [ ] **Step 2: `index.astro` 排序與 badge**

2a. `recent` 排序改為日期新→舊、同日 pinned 優先：

```ts
const recent = all
  .filter((p) => idDate(p.id) >= cutoff)
  .sort(
    (a, b) =>
      idDate(b.id).getTime() - idDate(a.id).getTime() ||
      Number(b.data.pinned) - Number(a.data.pinned)
  );
```

2b. `items` map 加 `pinned: p.data.pinned,`。

2c. 卡片 `post-meta` 區（`<span class="source-badge">` 之前）加：

```astro
                      {post.pinned && <span class="pin-badge">📌 置頂</span>}
```

2d. `<style>` 加：

```css
  .pin-badge {
    color: #ffce4f;
    border: 1px solid var(--border-strong);
    border-radius: 5px;
    padding: 0 0.4rem;
    font-weight: 600;
  }
```

2e. pinned 文章沒有 score（frontmatter 不寫），卡片 `post.score != null` 條件已自動略過 ★ 分數，無需額外處理；`data-score={post.score ?? 0}` 維持不動（分數排序模式下 pinned 落後屬可接受行為）。

- [ ] **Step 3: Build 驗證**

Run: `cd web && npm run build`
Expected: build 成功。若本地尚無 pinned 文章，手動造一篇假 frontmatter（`output/posts/` 加 `pinned: true` 的測試檔）確認置頂與 badge，看完刪除測試檔。

- [ ] **Step 4: Commit**

```bash
git add web/src/content.config.ts web/src/pages/index.astro
git commit -m "feat: Astro 首頁 pinned 文章置頂 + 📌 badge"
```

---

### Task 10: CI workflow + E2E 驗證 + 文件

**Files:**
- Modify: `.github/workflows/daily-pipeline.yml:61`
- Modify: `CLAUDE.md`（本地）、`CHANGELOG.md`（本地）、`docs/cicd-workflow.md`

**Interfaces:**
- Consumes: 前述全部任務
- Produces: CI commit 範圍含 `output/lists/`；文件同步

- [ ] **Step 1: workflow 加 lists 目錄**

`.github/workflows/daily-pipeline.yml:61` 的 `git add` 行改為：

```yaml
          git add data/raw/ data/scored/ data/bookmarks.json output/posts/ output/digests/ output/blogs/ output/lists/
```

- [ ] **Step 2: E2E 驗證**

```bash
source .venv/bin/activate
python -m src.cli run --date 2026-07-21 --force
```

檢查清單（逐項確認並記錄結果）：
- `output/lists/2026-07-21.json` 存在，github ≤10 / hf ≤10 / others ≤30，排序正確
- `data/scored/2026-07-21.json` 不含 `"source": "github"|"hf_papers"|"arxiv"|"chatpaper"|"semantic_scholar"`：
  `python -c "import json; d=json.load(open('data/scored/2026-07-21.json')); print({x['item']['source'] for x in d})"`
- 若當日有命中 pinned_organizations 的官方 blog：對應 post 存在且 frontmatter 有 `pinned: true`、無 `score`；若無命中，人工在 raw 塞一筆 OpenAI 測試項後跑 `python -m src.cli generate` 驗證，驗完 `--force` 清掉
- `pytest tests/ -q` 全綠
- `cd web && npm run build && npm run preview` → 檢查 `/trending`、`/papers`、首頁置頂
- `python -m src.cli web` → Day Detail 三 tab 正常

- [ ] **Step 3: 文件更新**

- `CLAUDE.md`（本地）：Architecture 表加 Lists 一列（`src/lists.py` / `src/pinned.py`）；Data Flow 加 `output/lists/{date}.json`；Key Config 更新（刪 hf/github 門檻、加 lists/pinned 區塊）；Conventions 註記「清單來源不評分不生成、pinned 免評分生成」；靜態站說明加 `/trending`、`/papers`
- `docs/cicd-workflow.md`：commit 範圍說明補 `output/lists/`
- `CHANGELOG.md`（本地）：

```markdown
## [2026-07-21]
### Changed
- github/hf_papers/arxiv/chatpaper/semantic_scholar 退出評分 pipeline，改為每日清單 output/lists/{date}.json（零 LLM，天然訊號排序）
- HF collector 移到 arXiv 前（單日去重保留 upvotes 訊號）
### Added
- 頂尖 AI 公司官方 blog 免評分直接生成 + pinned 置頂（config: pinned_organizations）
- Astro 靜態站 /trending、/papers 分頁（列表 + 詳情）；首頁 pinned 置頂
- Web Monitor Day Detail 加 Trending/Papers 分頁
```

- [ ] **Step 4: Commit**

```bash
git add .github/workflows/daily-pipeline.yml docs/cicd-workflow.md
git commit -m "ci: daily pipeline commit 範圍加 output/lists"
```

---

## Self-Review 紀錄

- **Spec coverage**：spec §1.1-1.5 → Task 1/2/3/4/5；§2 → Task 3/4；§3.1 → Task 7/8/9；§3.2 → Task 6；§4 → Task 10（digest.py 經查未特別引用 github/hf，泛用邏輯自動適應，無需修改）；§5 → Task 1（缺欄位 0）/ Task 5（pinned 失敗不 block）/ Task 6（損毀回 None）；§6 → 各 task TDD + Task 10 E2E；§7 YAGNI 遵守
- **Type consistency**：`build_lists(items, target_date, force)` / `select_pinned(items, target_date, config)` / `to_pinned_scored(item)` / `get_day_lists(d)` / `loadLists(days)` 全計畫一致；lists JSON schema（Task 1 產出 = Task 6 模板 = Task 7 interface）欄位名一致
- **known risk**：day_detail.html 的 CSS 變數名（`--ab`/`--t3` 等）以實際模板為準，實作時對照調整
