# 卡片視覺重構 Implementation Plan

> **For Claude:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task.

**Goal:** 把 posts/notes 列表頁升級為「日期分組 + 5D 分數條 + Feedback 著色 + 快速 Tag 篩選」的完整視覺體驗。

**Architecture:** 後端 data_service.py 新增 scored JSON 跨查與 feedback 聚合，把所有欄位預填入 list 函數回傳值。前端純 client-side 篩選（搜尋框 + tag chips + 排序），不增加 API call。

**Tech Stack:** Python 3.11+、Jinja2、Vanilla JS（無框架）、CSS Variables（已定義在 base.html）

---

## 背景知識

**Frontmatter 格式**（posts & notes 相同）：
```yaml
title: "SWE-Protégé: ..."
source: GitHub Trending
url: https://...
score: 113
model: arcee-ai/trinity-large-preview:free
generated_at: 2026-02-26T20:07:19.952143
```

**Scored JSON** 位於 `data/scored/{date}.json`，每筆含 `ScoredItem` 的 `novelty`, `impact`, `trending`, `practicality`, `blog_worthiness`, `rule_score`, `llm_score`。

**Feedback JSON** 位於 `data/feedback/{date}.json`，格式 `{"slug": "good"|"normal"|"bad"}`。

**關鍵 CSS 變數**（定義在 base.html）：
- 顏色：`--ag`（綠）, `--ac`（青）, `--ar`（紅）, `--ay`（黃）, `--av`（紫）
- 文字：`--t1`~`--t6`（由亮到暗）
- 背景：`--bg-c`（卡片背景）, `--br`（邊框）

---

## Task 1：data_service.py 擴充

**Files:**
- Modify: `src/web/data_service.py`
- Test: `tests/test_data_service_enrich.py` (新建)

### Step 1：寫失敗測試

新建 `tests/test_data_service_enrich.py`：

```python
"""測試 data_service 的 scored 跨查與 feedback 聚合功能。"""
from __future__ import annotations

import json
from pathlib import Path

import pytest


@pytest.fixture
def tmp_project(tmp_path):
    """建立最小化的 output/posts、data/scored、data/feedback 目錄結構。"""
    posts_dir = tmp_path / "output" / "posts"
    notes_dir = tmp_path / "output" / "notes"
    scored_dir = tmp_path / "data" / "scored"
    feedback_dir = tmp_path / "data" / "feedback"
    for d in [posts_dir, notes_dir, scored_dir, feedback_dir]:
        d.mkdir(parents=True)

    # 一篇 post
    post = posts_dir / "2026-02-27_test-paper.md"
    post.write_text(
        "---\ntitle: \"Test Paper\"\nsource: arXiv\nurl: https://example.com\n"
        "score: 95\nmodel: test\ngenerated_at: 2026-02-27T10:00:00\n---\n\n"
        "Body text here for word count. " * 50,
        encoding="utf-8",
    )

    # 對應的 scored JSON
    scored = [
        {
            "item": {
                "source": "arxiv",
                "source_name": "arXiv",
                "title": "Test Paper",
                "url": "https://example.com",
                "authors": [],
                "abstract": "",
                "published_date": "2026-02-27",
                "organization": "",
                "raw_metadata": {},
            },
            "rule_score": 45.0,
            "rule_reasons": [],
            "llm_score": 50.0,
            "llm_reason": "Good paper",
            "novelty": 18.0,
            "impact": 16.0,
            "trending": 15.0,
            "practicality": 14.0,
            "blog_worthiness": 17.0,
        }
    ]
    (scored_dir / "2026-02-27.json").write_text(
        json.dumps(scored), encoding="utf-8"
    )

    # feedback
    (feedback_dir / "2026-02-27.json").write_text(
        json.dumps({"test-paper": "good"}), encoding="utf-8"
    )

    return {
        "root": tmp_path,
        "posts_dir": posts_dir,
        "notes_dir": notes_dir,
        "scored_dir": scored_dir,
        "feedback_dir": feedback_dir,
    }


def test_load_scored_for_date_returns_title_keyed_dict(tmp_project, monkeypatch):
    """_load_scored_for_date 應回傳以 title 為 key 的 dict。"""
    import src.web.data_service as ds
    monkeypatch.setattr(ds, "SCORED_DIR", tmp_project["scored_dir"])
    monkeypatch.setattr(ds, "_scored_cache", {})

    result = ds._load_scored_for_date("2026-02-27")

    assert "Test Paper" in result
    assert result["Test Paper"]["novelty"] == 18.0
    assert result["Test Paper"]["impact"] == 16.0
    assert result["Test Paper"]["llm_score"] == 50.0


def test_load_scored_for_date_missing_returns_empty(tmp_project, monkeypatch):
    """日期不存在時回傳空 dict，不拋例外。"""
    import src.web.data_service as ds
    monkeypatch.setattr(ds, "SCORED_DIR", tmp_project["scored_dir"])
    monkeypatch.setattr(ds, "_scored_cache", {})

    result = ds._load_scored_for_date("2099-01-01")
    assert result == {}


def test_enrich_with_scored_fills_5d(tmp_project, monkeypatch):
    """_enrich_with_scored 應填入 5D 分數。"""
    import src.web.data_service as ds
    monkeypatch.setattr(ds, "SCORED_DIR", tmp_project["scored_dir"])
    monkeypatch.setattr(ds, "_scored_cache", {})

    item = {"date_str": "2026-02-27", "title": "Test Paper", "slug": "test-paper"}
    enriched = ds._enrich_with_scored(item)

    assert enriched["novelty"] == 18.0
    assert enriched["trending"] == 15.0
    assert enriched["llm_score"] == 50.0
    assert enriched["source_name"] == "arXiv"


def test_enrich_with_scored_no_match_returns_unchanged(tmp_project, monkeypatch):
    """找不到對應項目時，原 item 不受影響。"""
    import src.web.data_service as ds
    monkeypatch.setattr(ds, "SCORED_DIR", tmp_project["scored_dir"])
    monkeypatch.setattr(ds, "_scored_cache", {})

    item = {"date_str": "2026-02-27", "title": "Non-existent Paper", "slug": "none"}
    enriched = ds._enrich_with_scored(item)

    assert enriched.get("novelty") is None
    assert enriched["title"] == "Non-existent Paper"


def test_get_all_feedback_returns_flat_map(tmp_project, monkeypatch):
    """get_all_feedback 應回傳 {date_slug: rating} 格式。"""
    import src.web.data_service as ds
    monkeypatch.setattr(ds, "FEEDBACK_DIR", tmp_project["feedback_dir"])

    result = ds.get_all_feedback()

    assert result["2026-02-27_test-paper"] == "good"


def test_list_all_posts_includes_feedback_and_5d(tmp_project, monkeypatch):
    """list_all_posts 回傳項目應含 feedback 與 5D 分數。"""
    import src.web.data_service as ds
    monkeypatch.setattr(ds, "POSTS_DIR", tmp_project["posts_dir"])
    monkeypatch.setattr(ds, "SCORED_DIR", tmp_project["scored_dir"])
    monkeypatch.setattr(ds, "FEEDBACK_DIR", tmp_project["feedback_dir"])
    monkeypatch.setattr(ds, "_scored_cache", {})

    posts = ds.list_all_posts()

    assert len(posts) == 1
    p = posts[0]
    assert p["feedback"] == "good"
    assert p["novelty"] == 18.0
    assert p["fm_score"] == 95.0
    assert p["source_fm"] == "arXiv"
```

### Step 2：確認測試失敗

```bash
cd /home/yifor/auto_post_blog && source .venv/bin/activate
pytest tests/test_data_service_enrich.py -v 2>&1 | head -40
```
預期：全部 FAIL（函數尚未存在）

### Step 3：實作 data_service.py 變更

**3-A：`_extract_content_meta` 加入 `fm_score` 和 `source_fm` 欄位**

找到現有函數，在 `return {...}` 中新增兩個欄位：

```python
# 在 fm 解析之後加入：
score_raw = fm.get("score")
try:
    fm_score = float(score_raw) if score_raw is not None else None
except (TypeError, ValueError):
    fm_score = None
source_fm = fm.get("source") or ""

# return dict 加入：
    "fm_score": fm_score,
    "source_fm": source_fm,
```

**3-B：在 `get_sidebar_stats()` 上方加入 module-level cache 與 3 個新函數**

```python
# Module-level scored cache（per process，不跨重啟）
_scored_cache: dict[str, dict[str, dict]] = {}


def _load_scored_for_date(date_str: str) -> dict[str, dict]:
    """讀取指定日期的 scored JSON，以 title 為 key（module-level cache）。"""
    if date_str in _scored_cache:
        return _scored_cache[date_str]
    try:
        d = date.fromisoformat(date_str)
    except ValueError:
        _scored_cache[date_str] = {}
        return {}
    path = _get_scored_path(d)
    if not path.exists():
        _scored_cache[date_str] = {}
        return {}
    data = load_json(path)
    result: dict[str, dict] = {}
    if isinstance(data, list):
        for raw in data:
            try:
                item = ScoredItem(**raw)
                result[item.item.title] = {
                    "novelty": item.novelty,
                    "impact": item.impact,
                    "trending": item.trending,
                    "practicality": item.practicality,
                    "blog_worthiness": item.blog_worthiness,
                    "rule_score": item.rule_score,
                    "llm_score": item.llm_score,
                    "source_name": item.item.source_name,
                    "llm_reason": item.llm_reason,
                }
            except Exception:
                continue
    _scored_cache[date_str] = result
    return result


def _enrich_with_scored(item: dict) -> dict:
    """根據 date_str + title 跨查 scored JSON，填入 5D 分數等欄位。"""
    date_str = item.get("date_str", "")
    title = item.get("title", "")
    if not date_str or not title:
        return item
    scored_map = _load_scored_for_date(date_str)
    scored = scored_map.get(title)
    if not scored:
        # 5D 欄位全部設 None，確保模板可以判斷
        return {
            **item,
            "novelty": None,
            "impact": None,
            "trending": None,
            "practicality": None,
            "blog_worthiness": None,
            "rule_score": None,
            "llm_score": None,
            "source_name": item.get("source_fm", ""),
            "llm_reason": None,
        }
    return {**item, **scored}


def get_all_feedback() -> dict[str, str]:
    """回傳所有 feedback，格式：{date_str_slug: rating}。"""
    result: dict[str, str] = {}
    for path in FEEDBACK_DIR.glob("*.json"):
        date_str = path.stem
        data = load_json(path)
        if isinstance(data, dict):
            for slug, rating in data.items():
                result[f"{date_str}_{slug}"] = rating
    return result
```

**3-C：更新 `list_posts`, `list_notes`, `list_all_posts`, `list_all_notes`**

每個函數在 `result.append(...)` 前加入 enrichment + feedback：

```python
# list_posts：
def list_posts(date_str: str) -> list[dict]:
    result = []
    feedback_map = get_all_feedback()
    for f in sorted(POSTS_DIR.glob(f"{date_str}*.md")):
        slug = f.stem[len(date_str) + 1 :] if f.stem.startswith(date_str) else f.stem
        meta = _extract_content_meta(f)
        item = {"slug": slug, "filename": f.name, "date_str": date_str, **meta}
        item = _enrich_with_scored(item)
        item["feedback"] = feedback_map.get(f"{date_str}_{slug}")
        result.append(item)
    return result

# list_notes：同上，改 NOTES_DIR

# list_all_posts：
def list_all_posts() -> list[dict]:
    result = []
    feedback_map = get_all_feedback()
    for f in POSTS_DIR.glob("*.md"):
        parts = f.stem.split("_", 1)
        if len(parts) >= 1:
            date_str = parts[0]
            if len(date_str) == 10 and date_str.count("-") == 2:
                slug = parts[1] if len(parts) > 1 else f.stem
                meta = _extract_content_meta(f)
                item = {"date_str": date_str, "slug": slug, "filename": f.name, **meta}
                item = _enrich_with_scored(item)
                item["feedback"] = feedback_map.get(f"{date_str}_{slug}")
                result.append(item)
    return sorted(result, key=lambda x: (x["date_str"], x["slug"]), reverse=True)

# list_all_notes：同上，改 NOTES_DIR
```

### Step 4：跑測試確認通過

```bash
pytest tests/test_data_service_enrich.py -v
```
預期：全部 PASS

### Step 5：快速 smoke test

```bash
python3 -c "
from src.web import data_service as ds
posts = ds.list_all_posts()
p = posts[0]
print('keys:', [k for k in p.keys()])
print('feedback:', p.get('feedback'))
print('novelty:', p.get('novelty'))
print('fm_score:', p.get('fm_score'))
print('source_fm:', p.get('source_fm'))
"
```

### Step 6：Commit

```bash
git add src/web/data_service.py tests/test_data_service_enrich.py
git commit -m "feat: enrich posts/notes with 5D scores, feedback, and frontmatter score"
```

---

## Task 2：posts_list.html 完全重寫

**Files:**
- Modify: `src/web/templates/posts_list.html`

### Step 1：確認資料欄位可用

```bash
python3 -c "
from src.web import data_service as ds
p = ds.list_all_posts()[0]
print('novelty:', p.get('novelty'))
print('source_name:', p.get('source_name'))
print('fm_score:', p.get('fm_score'))
print('feedback:', p.get('feedback'))
"
```

### Step 2：重寫 posts_list.html

以下是完整模板：

```html
{% extends "base.html" %}
{% block title %}所有部落格文 — Auto Post Blog Monitor{% endblock %}

{% block page_title %}
<nav style="display:flex; align-items:center; gap:8px; font-size:13.5px;">
  <a href="/dashboard" class="link-muted">Dashboard</a>
  <span style="color:var(--t6);">/</span>
  <span style="color:var(--t1); font-weight:600;">📝 所有部落格文</span>
</nav>
{% endblock %}

{% block content %}
<style>
/* ── 篩選列 ── */
.filter-bar {
  display: flex; gap: 10px; align-items: center; flex-wrap: wrap;
  margin-bottom: 14px;
}
.filter-input {
  flex: 1; min-width: 200px; padding: 8px 14px;
  background: var(--bg-c); border: 1px solid var(--br2); border-radius: 9px;
  font-size: 13px; color: var(--t1); outline: none; transition: border-color 0.13s;
}
.filter-input:focus { border-color: var(--ag); }
.filter-input::placeholder { color: var(--t5); }
.filter-select {
  padding: 8px 12px; background: var(--bg-c);
  border: 1px solid var(--br2); border-radius: 9px;
  font-size: 12.5px; color: var(--t3); cursor: pointer; outline: none;
}
.count-label { font-size: 12px; color: var(--t5); margin-left: auto; white-space: nowrap; }

/* ── 快速 tag chips ── */
.quick-tags {
  display: flex; flex-wrap: wrap; gap: 7px; margin-bottom: 20px;
}
.qtag {
  font-size: 11.5px; padding: 4px 10px; border-radius: 20px; cursor: pointer;
  background: var(--bg-hv); color: var(--t3); border: 1px solid var(--br3);
  transition: all 0.12s; user-select: none;
}
.qtag:hover { background: var(--bg-in); color: var(--t2); }
.qtag.active {
  background: rgba(52,211,153,0.15); color: var(--ag);
  border-color: rgba(52,211,153,0.35); font-weight: 600;
}

/* ── 日期分組 ── */
.date-group { margin-bottom: 28px; }
.date-header {
  display: flex; align-items: center; gap: 10px;
  margin-bottom: 12px; padding-bottom: 8px; border-bottom: 1px solid var(--br3);
}
.date-label {
  font-size: 13px; font-weight: 600; color: var(--t2);
  font-family: 'JetBrains Mono', monospace;
}
.date-count { font-size: 11.5px; color: var(--t5); }

/* ── 卡片格 ── */
.content-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(290px, 1fr));
  gap: 14px;
}

/* ── 內容卡片 ── */
.content-card {
  background: var(--bg-c); border: 1px solid var(--br);
  border-left-width: 3px; border-radius: 12px;
  transition: transform 0.15s, box-shadow 0.15s;
  cursor: pointer; display: flex; flex-direction: column;
  text-decoration: none;
}
.content-card:hover {
  transform: translateY(-2px);
  box-shadow: 0 8px 24px rgba(0,0,0,0.25);
}
/* Feedback 著色 */
.cc-good  { border-left-color: var(--ag); background-color: rgba(52,211,153,0.04); }
.cc-bad   { border-left-color: var(--ar); background-color: rgba(248,113,113,0.04); }
.cc-normal { border-left-color: var(--t5); }
.cc-unrated { border-left-color: var(--br2); }

.cc-header {
  padding: 12px 14px 0;
  display: flex; align-items: center; justify-content: space-between;
}
.cc-source {
  font-size: 10.5px; padding: 2px 7px; border-radius: 4px;
  background: var(--bg-in); color: var(--t4);
  font-family: 'JetBrains Mono', monospace; white-space: nowrap;
  overflow: hidden; text-overflow: ellipsis; max-width: 120px;
}
.cc-feedback-badge {
  font-size: 10.5px; padding: 2px 7px; border-radius: 4px; font-weight: 600;
}
.cc-feedback-good  { background: rgba(52,211,153,0.12); color: var(--ag); }
.cc-feedback-bad   { background: rgba(248,113,113,0.12); color: var(--ar); }
.cc-feedback-normal { background: var(--bg-in); color: var(--t5); }

.cc-body { padding: 10px 14px 8px; flex: 1; display: flex; flex-direction: column; gap: 6px; }
.cc-title {
  font-size: 13.5px; font-weight: 600; color: var(--t1); line-height: 1.4;
}
.cc-excerpt {
  font-size: 12px; color: var(--t4); line-height: 1.5;
  display: -webkit-box; -webkit-line-clamp: 2; -webkit-box-orient: vertical; overflow: hidden;
}

/* ── 5D mini bars ── */
.cc-5d { display: flex; flex-direction: column; gap: 5px; margin-top: 4px; }
.mini-bar-row {
  display: flex; align-items: center; gap: 6px;
}
.mini-bar-label { font-size: 10px; color: var(--t5); width: 42px; flex-shrink: 0; }
.mini-bar-track {
  flex: 1; height: 4px; background: var(--bg-in); border-radius: 3px; overflow: hidden;
}
.mini-bar-fill { height: 100%; border-radius: 3px; transition: width 0.6s ease; }
.mini-bar-val { font-size: 10px; color: var(--t4); width: 18px; text-align: right; }

/* ── 標籤 & Footer ── */
.cc-tags {
  padding: 6px 14px; display: flex; gap: 5px; flex-wrap: wrap; align-items: center;
}
.tag-chip-g {
  font-size: 10px; padding: 2px 6px; border-radius: 4px;
  background: rgba(52,211,153,0.1); color: var(--ag);
  border: 1px solid rgba(52,211,153,0.2);
}
.cc-footer {
  padding: 8px 14px 12px;
  border-top: 1px solid var(--br4);
  display: flex; align-items: center; justify-content: space-between;
}
.cc-score {
  display: inline-flex; align-items: center; gap: 4px;
  font-size: 11.5px; font-weight: 700;
  background: var(--av-d); color: var(--av);
  border: 1px solid var(--av-b); border-radius: 99px;
  padding: 2px 9px;
}
.cc-meta { font-size: 11px; color: var(--t5); }
</style>

<!-- 頁面標題 -->
<div style="margin-bottom:18px;">
  <h2 style="font-size:20px; font-weight:700; color:var(--ag); margin:0 0 4px;">📝 部落格文庫</h2>
  <p style="font-size:13px; color:var(--t4); margin:0;">
    共 {{ posts|length }} 篇文章
    {%- set unique_dates = posts | map(attribute='date_str') | unique | list %}
    · 來自 {{ unique_dates|length }} 天
  </p>
</div>

<!-- 篩選列 -->
<div class="filter-bar">
  <input type="text" id="search-input" class="filter-input"
    placeholder="🔍 搜尋標題或標籤..." oninput="filterCards()" />
  <select id="sort-select" class="filter-select" onchange="rebuildGroups()">
    <option value="newest">最新優先</option>
    <option value="oldest">最早優先</option>
  </select>
  <span class="count-label" id="count-label">{{ posts|length }} 篇</span>
</div>

<!-- 快速 tag chips -->
<div class="quick-tags" id="quick-tags">
  <span class="qtag active" onclick="toggleTag(this,'')">全部</span>
  {% for tag in ['LLM','Agent','RAG','Fine-tuning','Multimodal','安全','小模型','推理','Anthropic','OpenAI','Meta','開源'] %}
  <span class="qtag" onclick="toggleTag(this,'{{ tag }}')">{{ tag }}</span>
  {% endfor %}
</div>

{% if not posts %}
<!-- 空狀態 -->
<div class="card" style="padding:48px; text-align:center;">
  <div style="font-size:32px; margin-bottom:12px;">📭</div>
  <p style="color:var(--t4); font-size:14px; margin:0;">目前尚無部落格文章</p>
</div>
{% else %}

<!-- 日期分組 -->
{% for date_str, date_items in posts | groupby('date_str') | list | reverse %}
<div class="date-group" id="group-{{ date_str }}" data-date="{{ date_str }}">
  <div class="date-header">
    <span class="date-label">📅 {{ date_str }}</span>
    <span class="date-count" id="gc-{{ date_str }}">{{ date_items | list | length }} 篇</span>
  </div>
  <div class="content-grid">
    {% for p in date_items %}
    {%- set fb = p.feedback or '' -%}
    {%- set fb_class = 'cc-' + fb if fb else 'cc-unrated' -%}
    <a href="/post/{{ p.date_str }}/{{ p.slug }}"
       class="content-card {{ fb_class }}"
       data-date="{{ p.date_str }}"
       data-title="{{ (p.title or p.slug) | lower }}"
       data-tags="{{ (p.tags or []) | join(' ') | lower }} {{ (p.source_name or p.source_fm or '') | lower }}">

      <!-- Header: source + feedback -->
      <div class="cc-header">
        <span class="cc-source">{{ p.source_name or p.source_fm or '—' }}</span>
        {% if fb %}
        <span class="cc-feedback-badge cc-feedback-{{ fb }}">
          {% if fb == 'good' %}👍 好{% elif fb == 'bad' %}👎 差{% else %}─ 普通{% endif %}
        </span>
        {% endif %}
      </div>

      <!-- Title + Excerpt -->
      <div class="cc-body">
        <div class="cc-title">{{ p.title or p.slug }}</div>
        {% if p.excerpt %}
        <div class="cc-excerpt">{{ p.excerpt }}</div>
        {% endif %}

        <!-- 5D mini bars（只在有資料時顯示） -->
        {% if p.novelty is not none %}
        <div class="cc-5d">
          {% set dims5 = [
            ('新穎性', p.novelty,         '#a78bfa'),
            ('影響力', p.impact,           '#fb923c'),
            ('話題性', p.trending,         '#34d399'),
            ('實用性', p.practicality,     '#f59e0b'),
            ('適合度', p.blog_worthiness,  '#22d3ee'),
          ] %}
          {% for label, val, color in dims5 %}
          {% if val is not none %}
          <div class="mini-bar-row">
            <span class="mini-bar-label">{{ label }}</span>
            <div class="mini-bar-track">
              <div class="mini-bar-fill"
                   style="width:{{ (val / 20 * 100)|int }}%; background:{{ color }};"></div>
            </div>
            <span class="mini-bar-val">{{ val|int }}</span>
          </div>
          {% endif %}
          {% endfor %}
        </div>
        {% endif %}
      </div>

      <!-- Tags -->
      {% if p.tags %}
      <div class="cc-tags">
        {% for tag in p.tags[:4] %}
        <span class="tag-chip-g">{{ tag }}</span>
        {% endfor %}
      </div>
      {% endif %}

      <!-- Footer: score + reading time -->
      <div class="cc-footer">
        <span class="cc-score">⭐ {{ (p.fm_score or ((p.rule_score or 0) + (p.llm_score or 0)))|int }}</span>
        <span class="cc-meta">⏱ {{ p.reading_time_min }}分 · {{ p.word_count }}字</span>
      </div>
    </a>
    {% endfor %}
  </div>
</div>
{% endfor %}

<!-- 空搜尋結果 -->
<div id="empty-search" style="display:none; padding:48px; text-align:center;">
  <div style="font-size:32px; margin-bottom:12px;">🔍</div>
  <p style="color:var(--t4); font-size:14px; margin:0;">找不到符合條件的文章</p>
</div>
{% endif %}

{% endblock %}

{% block scripts %}
<script>
var allCards = null;
var activeTag = '';

function initCards() {
  allCards = Array.from(document.querySelectorAll('.content-card[data-date]'));
}

function toggleTag(btn, tagName) {
  activeTag = (activeTag === tagName) ? '' : tagName;
  document.querySelectorAll('.qtag').forEach(function(el) {
    el.classList.toggle('active', el.dataset.tag === activeTag ||
      (activeTag === '' && el.dataset.tag === ''));
  });
  // mark 'all' chip active when no tag
  document.querySelectorAll('.qtag').forEach(function(el) {
    var isAll = el.textContent.trim() === '全部';
    if (isAll) el.classList.toggle('active', activeTag === '');
  });
  filterCards();
}

function filterCards() {
  if (!allCards) initCards();
  var query = document.getElementById('search-input').value.toLowerCase().trim();

  var total = 0;
  allCards.forEach(function(card) {
    var combined = (card.dataset.title || '') + ' ' + (card.dataset.tags || '');
    var queryMatch = !query || combined.indexOf(query) >= 0;
    var tagMatch = !activeTag || combined.indexOf(activeTag.toLowerCase()) >= 0;
    var show = queryMatch && tagMatch;
    card.style.display = show ? '' : 'none';
    if (show) total++;
  });

  // 更新每個 date-group 的計數與可見性
  document.querySelectorAll('.date-group').forEach(function(group) {
    var date = group.dataset.date;
    var visible = Array.from(group.querySelectorAll('.content-card'))
                       .filter(function(c){ return c.style.display !== 'none'; });
    group.style.display = visible.length > 0 ? '' : 'none';
    var countEl = document.getElementById('gc-' + date);
    if (countEl) countEl.textContent = visible.length + ' 篇';
  });

  document.getElementById('count-label').textContent = total + ' 篇';
  var empty = document.getElementById('empty-search');
  if (empty) empty.style.display = total === 0 ? 'block' : 'none';
}

function rebuildGroups() {
  // 排序只影響 group 的順序，不重新渲染
  var sort = document.getElementById('sort-select').value;
  var container = document.querySelector('.page-main') ||
                  document.getElementById('cards-container');
  var groups = Array.from(document.querySelectorAll('.date-group'));
  groups.sort(function(a, b) {
    var da = a.dataset.date, db = b.dataset.date;
    return sort === 'newest' ? (db > da ? 1 : -1) : (da > db ? 1 : -1);
  });
  // 重新插入到 DOM（保持在 empty-search 之前）
  var anchor = document.getElementById('empty-search');
  groups.forEach(function(g) {
    anchor.parentNode.insertBefore(g, anchor);
  });
}

// 為 qtag 設定 data-tag attribute（方便判斷 active 狀態）
document.querySelectorAll('.qtag').forEach(function(el) {
  var text = el.textContent.trim();
  el.dataset.tag = text === '全部' ? '' : text;
});
</script>
{% endblock %}
```

### Step 3：視覺驗證

```bash
python -m src.cli web
# 訪問 http://127.0.0.1:8080/posts
# 確認：日期分組、5D bars（有資料的卡片）、feedback 著色、tag chips 可點擊篩選
```

### Step 4：Commit

```bash
git add src/web/templates/posts_list.html
git commit -m "feat: redesign posts list with date groups, 5D bars, feedback colors, quick tags"
```

---

## Task 3：notes_list.html 完全重寫

**Files:**
- Modify: `src/web/templates/notes_list.html`

### Step 1：重寫（青色主題）

與 posts_list.html 結構完全相同，差異點：

| 元素 | posts（綠） | notes（青） |
|------|------------|------------|
| h2 顏色 | `var(--ag)` | `var(--ac)` |
| `.filter-input:focus` | `var(--ag)` | `var(--ac)` |
| `.qtag.active` | `rgba(52,211,153,0.15)` / `var(--ag)` | `rgba(34,211,238,0.15)` / `var(--ac)` |
| `.cc-good` border-left | `var(--ag)` | `var(--ag)`（保持綠，表示 feedback good） |
| `.tag-chip` 顏色 | `.tag-chip-g`（綠） | `.tag-chip-c`（青） |
| 連結 href | `/post/{{ n.date_str }}/{{ n.slug }}` | `/note/{{ n.date_str }}/{{ n.slug }}` |
| Jinja2 迴圈變數 | `posts` / `p` | `notes` / `n` |
| 空狀態文字 | 「尚無部落格文章」 | 「尚無 AI 筆記」 |

新增 CSS 差異段（覆蓋 posts 樣式）：
```css
.filter-input:focus { border-color: var(--ac); }
.qtag.active { background: rgba(34,211,238,0.15); color: var(--ac); border-color: rgba(34,211,238,0.35); }
.tag-chip-c { font-size:10px; padding:2px 6px; border-radius:4px;
  background:rgba(34,211,238,0.1); color:var(--ac); border:1px solid rgba(34,211,238,0.2); }
```

### Step 2：Commit

```bash
git add src/web/templates/notes_list.html
git commit -m "feat: redesign notes list with date groups, 5D bars, feedback colors, quick tags (cyan theme)"
```

---

## Task 4：day_detail.html mini-card 升級

**Files:**
- Modify: `src/web/templates/day_detail.html`

`list_posts(date_str)` 和 `list_notes(date_str)` 在 Task 1 已更新，現在已包含 5D 分數與 feedback。

### Step 1：更新 posts mini-card 區塊

找到 `{% for p in posts %}` 的 `<li>` 區塊，替換為：

```html
{% for p in posts %}
<li style="margin-bottom:10px;">
  {%- set fb = p.feedback or '' -%}
  <a href="/post/{{ date_str }}/{{ p.slug }}"
     style="display:block; padding:10px 12px; border-radius:8px; text-decoration:none;
            border-left: 3px solid {% if fb == 'good' %}var(--ag){% elif fb == 'bad' %}var(--ar){% elif fb == 'normal' %}var(--t5){% else %}rgba(52,211,153,0.3){% endif %};
            background: {% if fb == 'good' %}rgba(52,211,153,0.05){% elif fb == 'bad' %}rgba(248,113,113,0.04){% else %}rgba(52,211,153,0.04){% endif %};
            border-top: 1px solid rgba(52,211,153,0.1); border-right: 1px solid rgba(52,211,153,0.1); border-bottom: 1px solid rgba(52,211,153,0.1);
            transition: background 0.13s;">

    <!-- Title + feedback -->
    <div style="display:flex; align-items:flex-start; justify-content:space-between; gap:8px; margin-bottom:4px;">
      <div style="font-size:13.5px; font-weight:600; color:var(--t1); line-height:1.4; flex:1;">
        {{ p.title or p.slug }}
      </div>
      {% if fb %}
      <span style="font-size:10px; padding:2px 7px; border-radius:4px; flex-shrink:0;
                   {% if fb == 'good' %}background:rgba(52,211,153,0.12); color:var(--ag);
                   {% elif fb == 'bad' %}background:rgba(248,113,113,0.12); color:var(--ar);
                   {% else %}background:var(--bg-in); color:var(--t5);{% endif %}">
        {% if fb == 'good' %}👍{% elif fb == 'bad' %}👎{% else %}─{% endif %}
      </span>
      {% endif %}
    </div>

    <!-- Excerpt -->
    {% if p.excerpt %}
    <div style="font-size:11.5px; color:var(--t4); margin-bottom:6px; line-height:1.45;
                overflow:hidden; display:-webkit-box; -webkit-line-clamp:1; -webkit-box-orient:vertical;">
      {{ p.excerpt }}
    </div>
    {% endif %}

    <!-- 3 mini bars（新穎性/話題性/實用性） -->
    {% if p.novelty is not none %}
    <div style="display:flex; flex-direction:column; gap:3px; margin-bottom:6px;">
      {% for label, val, color in [('新穎性', p.novelty, '#a78bfa'), ('話題性', p.trending, '#34d399'), ('實用性', p.practicality, '#f59e0b')] %}
      {% if val is not none %}
      <div style="display:flex; align-items:center; gap:5px;">
        <span style="font-size:9.5px; color:var(--t5); width:38px;">{{ label }}</span>
        <div style="flex:1; height:3px; background:var(--bg-in); border-radius:2px; overflow:hidden;">
          <div style="width:{{ (val / 20 * 100)|int }}%; height:100%; background:{{ color }}; border-radius:2px;"></div>
        </div>
        <span style="font-size:9.5px; color:var(--t4); width:16px; text-align:right;">{{ val|int }}</span>
      </div>
      {% endif %}
      {% endfor %}
    </div>
    {% endif %}

    <!-- Tags + Meta -->
    <div style="display:flex; gap:5px; align-items:center; flex-wrap:wrap;">
      {% for tag in (p.tags or [])[:3] %}
      <span style="font-size:10px; padding:2px 6px; border-radius:4px;
                   background:rgba(52,211,153,0.1); color:var(--ag); border:1px solid rgba(52,211,153,0.2);">
        {{ tag }}
      </span>
      {% endfor %}
      <span style="margin-left:auto; font-size:11px; color:var(--t5);">
        {% if p.fm_score %}⭐{{ p.fm_score|int }}  {% endif %}⏱ {{ p.reading_time_min }}分
      </span>
    </div>
  </a>
</li>
{% endfor %}
```

### Step 2：更新 notes mini-card 區塊

同上，將所有 `rgba(52,211,153,...)` 的綠色替換為 `rgba(34,211,238,...)` 青色，`var(--ag)` 替換為 `var(--ac)`，href 改為 `/note/...`。

### Step 3：移除 max-height 限制

原本兩個 card 有 `max-height: 280px; overflow-y: auto`，改為自然高度（不設 max-height）。

### Step 4：Commit

```bash
git add src/web/templates/day_detail.html
git commit -m "feat: upgrade day_detail mini-cards with feedback colors and 5D mini bars"
```

---

## Task 5：整合驗證

### Step 1：全測試套件

```bash
pytest tests/ -v --tb=short 2>&1 | tail -20
```
預期：既有測試全部 PASS，新增測試 PASS

### Step 2：啟動 web server 手動驗證

```bash
python -m src.cli web
```

**驗證清單：**
- `/posts` — 日期分組 header 正確、卡片有 5D bars（有 scored 資料的日期）、快速 tag 可篩選
- `/notes` — 青色主題、同上功能
- `/day/2026-02-27` — mini-card 有 feedback 著色、3 mini bars
- 邊界條件：點「全部」tag → 顯示所有卡片；輸入不存在關鍵字 → 顯示「找不到」提示；無 scored 資料的日期 → 不顯示 5D bars（卡片仍正常）

### Step 3：Final commit（如有雜修）

```bash
git add -p  # 選擇性加入
git commit -m "fix: post-integration visual tweaks"
```
