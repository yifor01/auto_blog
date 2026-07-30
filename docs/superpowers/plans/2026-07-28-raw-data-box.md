# 摘要頁面「原始資料」展開 box — 實作計畫

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** 在 Astro `/daily/<id>` 與 Web Monitor `/post/<date>/<slug>` 的正文後加一個可展開的「原始資料」box，並修復會在 box 裡露出來的兩批髒資料（HF 摘要黏字、HTML entity 未解碼）。

**Architecture:** 靜態站用原生 `<details>`、零 JavaScript，資料在 build 時由新模組 `web/src/raw.ts` 從 `data/raw` 直讀（不走 `data/scored`，因為 pinned 文不在 scored）。Monitor 端由 `data_service.get_raw_by_url()` 提供同一份欄位。髒資料修復收斂成一支 `repair-content` CLI，一次改完 `data/raw`、`output/lists`、`output/posts` 三處。

**Tech Stack:** Python 3 / Pydantic v2 / Typer / pytest；Astro 5 / TypeScript；Jinja2（Monitor 端）

**Spec:** `docs/superpowers/specs/2026-07-28-raw-data-box-design.md`

## Global Constraints

- 所有使用者可見文字為**繁體中文**
- Astro box 必須**零 JavaScript**（原生 `<details>`）
- 黏字判定式**必須限定 `source == "hf_papers"`**——實測 `hackernews`(26) / `reddit`(8) 會誤判
- `html.unescape()` 必須在 `to_traditional()` **之前**執行
- URL 比對用**輕量正規化**（去尾斜線 + `http:`→`https:`），**不要**用 `src/utils.py` 的 `normalize_url()`——那支是為去重設計的、會動 query 與 `www.`。post frontmatter 的 `url` 就是 `ContentItem.url` 原值（`src/generators/blog_post.py:301`），輕量正規化已足夠
- 修復 CLI 無任何項目變更則**不寫檔**（比照 `src/backfill.py`）
- 測試中**不得發出真實 HTTP 請求**——抓取函式一律以參數注入
- `web/` 目前**沒有** TS 測試框架（`enrich.ts` 也沒有測試）。不為此引入 vitest；TS 端以 `npm run build` + 實際開頁面驗證
  （**2026-07-31 已推翻**：`e77f802` 於 `web/` 引入 vitest + happy-dom，使用者追認。此條為本計畫執行當下的約束，保留不改）
- Commit message 格式：`<type>: <description>`，type ∈ feat/fix/refactor/docs/test/chore
- **不得改動 `output/posts/` 的檔名**。`sam-altman8217s-orb` 這種被 entity 污染的 slug 就是 Astro 的頁面 id，改名等於改 URL、打斷既有連結與 `apb-read` localStorage 記錄。只修 frontmatter 的顯示標題
- **不得解碼 post body**。body 是 LLM 生成的 markdown，程式碼區塊裡的 `&amp;` 可能是字面意義。實測 4 篇受影響檔案的 entity 全部只在 `title:` 行
- 資料寫回一律用 `src/utils.py` 的 `save_json()`，不要自寫 `json.dump`——格式（`indent=2, ensure_ascii=False, default=str`）一有出入就會產生全檔假 diff
- Commit 切分比 spec §9 更細（每個 task 一個），語意分組不變：Task 1-3 為 `fix`、Task 4-6 為 `feat`、Task 7 為獨立的 `chore` 資料 diff

---

## File Structure

| 檔案 | 動作 | 責任 |
|---|---|---|
| `src/collectors/hf_papers.py` | Modify | 抽出 `fetch_paper_abstract()`；新增 `looks_unspaced()`；修正 arXiv fallback 觸發條件 |
| `src/models.py` | Modify | `ContentItem` validator 加 `html.unescape()` |
| `src/repair.py` | Create | 歷史資料修復核心邏輯（純函式 + 注入式抓取） |
| `src/cli.py` | Modify | `repair-content` 指令（薄層） |
| `web/src/raw.ts` | Create | build 時讀 `data/raw`，回傳 `Map<normUrl, RawItem>` |
| `web/src/pages/daily/[slug].astro` | Modify | 渲染 `<details>` box |
| `src/web/data_service.py` | Modify | `get_raw_by_url()` |
| `src/web/app.py` | Modify | `post_view` route 傳 `raw_item` |
| `src/web/templates/post_view.html` | Modify | 渲染 box（`{% if raw_item %}` 包住） |
| `tests/test_collectors/test_hf_papers_enrichment.py` | Modify | `looks_unspaced()` 測試 |
| `tests/test_models.py` | Modify | entity 解碼測試 |
| `tests/test_repair.py` | Create | 修復邏輯測試 |
| `tests/test_web/test_data_service_raw.py` | Create | `get_raw_by_url()` 測試 |

執行順序：先修髒資料的**程式碼**（Task 1-3），再做 box（Task 4-6），最後**跑**修復產生資料 diff（Task 7），端對端驗證收尾（Task 8）。

---

### Task 1: HF collector — 抽出抓取函式 + 黏字判定 + 修正 fallback 條件

**Files:**
- Modify: `src/collectors/hf_papers.py:184-223`
- Test: `tests/test_collectors/test_hf_papers_enrichment.py`

**Interfaces:**
- Produces:
  - `looks_unspaced(text: str) -> bool` — Task 3 用來篩修復目標
  - `fetch_paper_abstract(client, paper_url: str) -> str` — Task 3 用來重抓，失敗回 `""`
  - 既有的 `_fetch_arxiv_abstract(arxiv_id: str, client) -> str` 維持不變，Task 3 直接用

- [ ] **Step 1: 寫失敗的測試**

加到 `tests/test_collectors/test_hf_papers_enrichment.py` 末尾：

```python
from src.collectors.hf_papers import looks_unspaced


class TestLooksUnspaced:
    def test_detects_stripped_whitespace(self):
        # 實測破損樣本：get_text(strip=True) 把節點間空白全吃掉
        broken = "LLMtrainingisshiftingfrommanualdesignandannotationtointeractiondrivenselfevolution" * 2
        assert looks_unspaced(broken) is True

    def test_normal_english_abstract_is_fine(self):
        ok = (
            "LLM training is shifting from manual design and annotation to "
            "interaction-driven self-evolution. However, existing methods face a dilemma."
        )
        assert looks_unspaced(ok) is False

    def test_flags_broken_text_containing_slashes(self):
        # 真實破損樣本有 59/192 含 "/"（and/or、Hand-Object），不得被排除
        broken = "Hand-ObjectInteraction(HOI)synthesisisacornerstoneforanimationproductionand/orembodiedAI." * 2
        assert looks_unspaced(broken) is True

    def test_chinese_abstract_not_flagged(self):
        # 中文幾乎沒有空白，必須靠 ASCII 比例擋掉
        zh = "本文提出一種新的大型語言模型訓練方法，透過技能自我對弈提升模型能力邊界。" * 4
        assert looks_unspaced(zh) is False

    def test_short_text_not_flagged(self):
        assert looks_unspaced("short") is False

    def test_empty_string_not_flagged(self):
        assert looks_unspaced("") is False
```

- [ ] **Step 2: 跑測試確認失敗**

Run: `pytest tests/test_collectors/test_hf_papers_enrichment.py -v -k LooksUnspaced`
Expected: FAIL — `ImportError: cannot import name 'looks_unspaced'`

- [ ] **Step 3: 實作 `looks_unspaced()`**

加到 `src/collectors/hf_papers.py`（放在 `_fetch_arxiv_abstract` 之前）：

```python
def looks_unspaced(text: str) -> bool:
    """判斷 abstract 是否為「空白被吃掉」的破損字串。

    HF 論文頁把 abstract 拆成大量 text node，舊版用 get_text(strip=True)
    解析會把節點間空白全部吃掉，整段變成一個無空白長字串。

    why ASCII 比例門檻：中文摘要天生幾乎沒有空白，單看空白比會誤判。

    why 不加「含 URL 就排除」的防呆：URL 堆疊的 HN 留言確實也會命中空白比
    門檻（實測 hackernews 26 筆 / reddit 8 筆），但用 "/" 或 "http" 排除會
    連帶誤殺 59/192 筆真實破損樣本（and/or、Hand-Object 都含 "/"）。
    正確的防線是**呼叫端限定 source == hf_papers** —— 兩個呼叫點
    （本檔的 arXiv fallback、src/repair.py）都在 HF 脈絡內，而 HF abstract
    一律為英文散文。本函式對其他來源不保證正確，不可挪作通用判定。
    """
    if len(text) < 100:
        return False
    if sum(c.isascii() for c in text) / len(text) <= 0.9:
        return False
    return text.count(" ") / len(text) < 0.05
```

- [ ] **Step 4: 跑測試確認通過**

Run: `pytest tests/test_collectors/test_hf_papers_enrichment.py -v -k LooksUnspaced`
Expected: 6 passed

- [ ] **Step 5: 抽出 `fetch_paper_abstract()`**

在 `src/collectors/hf_papers.py` 新增（放在 `looks_unspaced` 之後）：

```python
def fetch_paper_abstract(client, paper_url: str) -> str:
    """抓取 HF 論文頁的 abstract 原文；失敗回空字串。

    why " ".join(get_text().split())：HF 論文頁的 abstract 被拆成逐字元
    text node，get_text(strip=True) 會把節點間空白全部吃掉，get_text(" ")
    則會變成每字元間插空白 —— 只能先取原文再正規化空白。
    """
    try:
        resp = client.get(paper_url)
        if resp.status_code != 200:
            _logger.warning(
                "Non-200 fetching HF paper page, skipping enrichment",
                extra={"url": paper_url, "status_code": resp.status_code},
            )
            return ""
        soup = BeautifulSoup(resp.text, "html.parser")
        for p in soup.select("p"):
            text = " ".join(p.get_text().split())
            if len(text) > 100:  # 通常 abstract 都比較長
                return text
    except Exception as e:
        _logger.debug(
            "Failed to fetch HF paper abstract",
            extra={"url": paper_url, "error": str(e)},
        )
    return ""
```

- [ ] **Step 6: 改 `collect()` 改用新函式並修正 fallback 條件**

把 `src/collectors/hf_papers.py:184-223` 那整段（從 `# 修改為去論文單獨頁面抓取 abstract` 到 arXiv enrichment 結束）替換成：

```python
                abstract = fetch_paper_abstract(client, paper_url)

                # 如果還是抓不到，我們預設為標題
                if not abstract:
                    abstract = f"AI Paper from HuggingFace Daily Papers: {title}"

                # arXiv abstract enrichment
                # why 加 looks_unspaced：破損字串很長，只看 len < 100 會直接
                # 繞過補救而靜默通過（2026-04~07 共 192 筆就是這樣漏掉的）
                arxiv_id = _extract_arxiv_id(paper_url)
                if (len(abstract.strip()) < 100 or looks_unspaced(abstract)) and arxiv_id:
                    _logger.debug("Attempting arXiv enrichment", extra={"arxiv_id": arxiv_id})
                    arxiv_abstract = _fetch_arxiv_abstract(arxiv_id, client)
                    if arxiv_abstract:
                        abstract = arxiv_abstract
                        _logger.info(
                            "arXiv enrichment succeeded",
                            extra={"arxiv_id": arxiv_id, "abstract_len": len(abstract)},
                        )
                    else:
                        _logger.warning(
                            "arXiv enrichment failed, keeping fallback",
                            extra={"arxiv_id": arxiv_id},
                        )
```

- [ ] **Step 7: 跑整個 collector 測試確認沒有回歸**

Run: `pytest tests/test_collectors/ -v`
Expected: all passed（原有 HF enrichment 測試必須仍通過——若它們直接 patch 了舊的 inline 抓取路徑，改成 patch `fetch_paper_abstract`）

- [ ] **Step 8: Commit**

```bash
git add src/collectors/hf_papers.py tests/test_collectors/test_hf_papers_enrichment.py
git commit -m "fix: HF abstract 黏字偵測 + arXiv fallback 不再被長破損字串繞過"
```

---

### Task 2: `ContentItem` 解碼 HTML entity

**Files:**
- Modify: `src/models.py:40-58`
- Test: `tests/test_models.py`

**Interfaces:**
- Consumes: 無
- Produces: `ContentItem(title=..., abstract=..., tags=[...])` 建構後 entity 已解碼且已轉繁

- [ ] **Step 1: 寫失敗的測試**

加到 `tests/test_models.py` 末尾：

```python
class TestHtmlEntityDecoding:
    def _item(self, **kw):
        from datetime import date as _date

        from src.models import ContentItem, SourceType

        base = dict(
            source=SourceType.RSS,
            title="t",
            url="https://example.com/a",
            published_date=_date(2026, 7, 28),
        )
        base.update(kw)
        return ContentItem(**base)

    def test_decodes_numeric_entity_in_title(self):
        # 實測：output/posts 有 4 篇 frontmatter title 帶著 &#8217;
        assert self._item(title="Sam Altman&#8217;s orb").title == "Sam Altman’s orb"

    def test_decodes_hex_entity_in_abstract(self):
        # 實測：hackernews abstract 269 筆帶 &#x2F;
        got = self._item(abstract="https:&#x2F;&#x2F;x.com&#x2F;a").abstract
        assert got == "https://x.com/a"

    def test_decodes_named_entities(self):
        assert self._item(abstract="a &amp; b &gt; c").abstract == "a & b > c"

    def test_decodes_entity_in_tags(self):
        assert self._item(tags=["AI &amp; ML"]).tags == ["AI & ML"]

    def test_idempotent_on_clean_text(self):
        clean = "No entities here at all."
        assert self._item(abstract=clean).abstract == clean

    def test_decode_runs_before_opencc(self):
        # 簡體 + entity 混合：解碼後才轉繁，兩者都要生效
        got = self._item(title="开源模型&#8217;s 发布").title
        assert "&#" not in got
        assert "開源" in got and "發布" in got
```

- [ ] **Step 2: 跑測試確認失敗**

Run: `pytest tests/test_models.py -v -k HtmlEntityDecoding`
Expected: FAIL — title 仍是 `Sam Altman&#8217;s orb`

- [ ] **Step 3: 改 validator**

`src/models.py` 頂部 import 區加 `import html`，然後改兩個 validator：

```python
    @field_validator("title", "abstract")
    @classmethod
    def _normalize_to_traditional(cls, v: str) -> str:
        """Layer A：來源端 HTML entity 解碼 + 簡→繁。量子位 / ChatPaper 等
        中國 source 的簡體 title/abstract 在建構時就轉繁，一改全下游受惠
        （raw/scored JSON、blog frontmatter title、digest、web UI）。
        對英文/繁中為冪等。

        why 先 unescape 再轉繁：&#8217; 解碼後是 ASCII 標點，OpenCC 不動它；
        反過來則是拿未解碼的髒字串餵 OpenCC。RSS 有 58 筆 title、
        hackernews 有 269 筆 abstract 帶著未解碼 entity。
        """
        # 區域 import 避免 utils <-> models 潛在循環依賴
        from src.utils import to_traditional

        return to_traditional(html.unescape(v))

    @field_validator("tags")
    @classmethod
    def _normalize_tags_to_traditional(cls, v: list[str]) -> list[str]:
        """tags 同樣走 Layer A。漏掉這個，網站的 tag chip 會直接顯示
        簡體（资讯 / 开源 / 科大讯飞），且 tag 篩選會把簡繁當成兩個不同標籤。"""
        from src.utils import to_traditional

        return [to_traditional(html.unescape(t)) for t in v]
```

- [ ] **Step 4: 跑測試確認通過**

Run: `pytest tests/test_models.py -v -k HtmlEntityDecoding`
Expected: 6 passed

- [ ] **Step 5: 跑全套確認沒有回歸**

Run: `pytest tests/ -q`
Expected: all passed（特別注意 `test_to_traditional.py`、`test_dedup.py`）

- [ ] **Step 6: Commit**

```bash
git add src/models.py tests/test_models.py
git commit -m "fix: ContentItem 建構時解碼 HTML entity（先解碼再轉繁）"
```

---

### Task 3: `repair-content` 修復模組 + CLI

**Files:**
- Create: `src/repair.py`
- Modify: `src/cli.py`（新增 command）
- Test: `tests/test_repair.py`

**Interfaces:**
- Consumes: `looks_unspaced(text) -> bool`、`fetch_paper_abstract(client, url) -> str`（Task 1）
- Produces:
  - `repair_all(days: int | None = None, dry_run: bool = False, fetcher: Callable[[str], str] | None = None) -> dict`
  - 回傳 `{"hf_refetched": int, "hf_failed": int, "entities_fixed": int, "files_written": int}`
  - `fetcher(url) -> str`：注入點，`None` 時建立真實 HTTP client。測試一律注入 stub

- [ ] **Step 1: 寫失敗的測試**

建立 `tests/test_repair.py`：

```python
"""repair-content 歷史資料修復測試。所有測試以注入 fetcher 避免真實 HTTP。"""

from __future__ import annotations

import json

import pytest

from src.repair import repair_all

BROKEN = "LLMtrainingisshiftingfrommanualdesignandannotationtointeractiondrivenselfevolution" * 2
FIXED = "LLM training is shifting from manual design and annotation to interaction driven self evolution. " * 2


def _write(path, obj):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(obj, ensure_ascii=False), encoding="utf-8")


@pytest.fixture
def repo(tmp_path, monkeypatch):
    """在 tmp_path 造一個迷你 repo 結構並切換 cwd。"""
    monkeypatch.chdir(tmp_path)
    return tmp_path


def test_refetches_broken_hf_abstract(repo):
    _write(repo / "data/raw/2026-07-27.json", [
        {"source": "hf_papers", "source_name": "HuggingFace Daily Papers",
         "title": "T", "url": "https://huggingface.co/papers/2607.1",
         "abstract": BROKEN, "published_date": "2026-07-27"},
    ])
    res = repair_all(fetcher=lambda url: FIXED)
    assert res["hf_refetched"] == 1
    data = json.loads((repo / "data/raw/2026-07-27.json").read_text(encoding="utf-8"))
    assert data[0]["abstract"] == FIXED


def test_keeps_original_when_refetch_fails(repo):
    _write(repo / "data/raw/2026-07-27.json", [
        {"source": "hf_papers", "source_name": "HF", "title": "T",
         "url": "https://huggingface.co/papers/2607.1",
         "abstract": BROKEN, "published_date": "2026-07-27"},
    ])
    res = repair_all(fetcher=lambda url: "")
    assert res["hf_refetched"] == 0 and res["hf_failed"] == 1
    data = json.loads((repo / "data/raw/2026-07-27.json").read_text(encoding="utf-8"))
    assert data[0]["abstract"] == BROKEN


def test_does_not_touch_non_hf_unspaced_text(repo):
    """HN 留言是整串 URL，空白天生就少——不得被當成破損重抓。"""
    hn = "https://x.com/a/status/1   https://x.com/b/status/2" * 4
    _write(repo / "data/raw/2026-07-27.json", [
        {"source": "hackernews", "source_name": "Hacker News", "title": "T",
         "url": "https://news.ycombinator.com/item?id=1",
         "abstract": hn, "published_date": "2026-07-27"},
    ])
    called = []
    res = repair_all(fetcher=lambda url: called.append(url) or FIXED)
    assert called == [] and res["hf_refetched"] == 0


def test_decodes_entities_across_sources(repo):
    _write(repo / "data/raw/2026-07-27.json", [
        {"source": "rss", "source_name": "The Verge AI",
         "title": "Sam Altman&#8217;s orb", "url": "https://example.com/a",
         "abstract": "a &amp; b", "tags": ["AI &amp; ML"], "published_date": "2026-07-27"},
    ])
    res = repair_all(fetcher=lambda url: FIXED)
    assert res["entities_fixed"] == 3  # title + abstract + 1 tag
    data = json.loads((repo / "data/raw/2026-07-27.json").read_text(encoding="utf-8"))
    assert data[0]["title"] == "Sam Altman’s orb"
    assert data[0]["abstract"] == "a & b"
    assert data[0]["tags"] == ["AI & ML"]


def test_syncs_lists_hf_abstract(repo):
    _write(repo / "data/raw/2026-07-27.json", [
        {"source": "hf_papers", "source_name": "HF", "title": "T",
         "url": "https://huggingface.co/papers/2607.1",
         "abstract": BROKEN, "published_date": "2026-07-27"},
    ])
    _write(repo / "output/lists/2026-07-27.json", {
        "date": "2026-07-27",
        "papers": {"hf": [{"slug": "t", "title": "T",
                           "url": "https://huggingface.co/papers/2607.1",
                           "abstract": BROKEN}], "others": []},
        "github": [],
    })
    repair_all(fetcher=lambda url: FIXED)
    lists = json.loads((repo / "output/lists/2026-07-27.json").read_text(encoding="utf-8"))
    assert lists["papers"]["hf"][0]["abstract"] == FIXED


def test_fixes_post_frontmatter_title_only(repo):
    p = repo / "output/posts/2026-07-27_x.md"
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(
        '---\ntitle: "Sam Altman&#8217;s orb"\nurl: https://example.com/a\n---\n\n'
        "本文提到 &amp; 這個符號應該保持原樣。\n",
        encoding="utf-8",
    )
    repair_all(fetcher=lambda url: FIXED)
    out = p.read_text(encoding="utf-8")
    assert 'title: "Sam Altman’s orb"' in out
    assert "本文提到 &amp; 這個符號應該保持原樣。" in out  # body 不動


def test_dry_run_writes_nothing(repo):
    raw = repo / "data/raw/2026-07-27.json"
    _write(raw, [
        {"source": "rss", "source_name": "R", "title": "A&#8217;s",
         "url": "https://example.com/a", "abstract": "", "published_date": "2026-07-27"},
    ])
    before = raw.read_text(encoding="utf-8")
    res = repair_all(dry_run=True, fetcher=lambda url: FIXED)
    assert res["entities_fixed"] == 1
    assert res["files_written"] == 0
    assert raw.read_text(encoding="utf-8") == before


def test_no_changes_means_no_write(repo):
    raw = repo / "data/raw/2026-07-27.json"
    _write(raw, [
        {"source": "rss", "source_name": "R", "title": "clean",
         "url": "https://example.com/a", "abstract": "clean", "published_date": "2026-07-27"},
    ])
    mtime_before = raw.stat().st_mtime_ns
    res = repair_all(fetcher=lambda url: FIXED)
    assert res["files_written"] == 0
    assert raw.stat().st_mtime_ns == mtime_before


def test_days_filter_skips_older_files(repo):
    old = repo / "data/raw/2020-01-01.json"
    _write(old, [
        {"source": "rss", "source_name": "R", "title": "A&#8217;s",
         "url": "https://example.com/a", "abstract": "", "published_date": "2020-01-01"},
    ])
    res = repair_all(days=30, fetcher=lambda url: FIXED)
    assert res["entities_fixed"] == 0
```

- [ ] **Step 2: 跑測試確認失敗**

Run: `pytest tests/test_repair.py -v`
Expected: FAIL — `ModuleNotFoundError: No module named 'src.repair'`

- [ ] **Step 3: 實作 `src/repair.py`**

```python
"""歷史資料修復：HF 摘要黏字重抓 + 跨來源 HTML entity 解碼。

why 合併成一支：兩種修復都要翻 data/raw、output/lists、output/posts 同一批
檔案，分兩支等於把每個檔案改兩遍、產生兩次巨量 diff。

修復目標與判定依據見 docs/superpowers/specs/2026-07-28-raw-data-box-design.md
"""

from __future__ import annotations

import html
import json
import re
from collections.abc import Callable
from datetime import date, timedelta
from pathlib import Path

from src.collectors.hf_papers import fetch_paper_abstract, looks_unspaced
from src.logger import get_logger
from src.utils import save_json

_logger = get_logger(__name__)

_RAW_DIR = Path("data/raw")
_LISTS_DIR = Path("output/lists")
_POSTS_DIR = Path("output/posts")

_DATE_RE = re.compile(r"^(\d{4}-\d{2}-\d{2})")
# 只吃 frontmatter 的 title 行；body 不動（可能含程式碼區塊裡字面意義的 &amp;）
_TITLE_LINE_RE = re.compile(r'^title:[ \t]*(.*)$', re.MULTILINE)


def _norm_url(url: str) -> str:
    """輕量 URL 正規化，與 web/src/enrich.ts 的 normalizeUrl 行為一致。

    why 不用 utils.normalize_url：那支為去重設計，會排序 query、去 www.，
    比對兩端來源相同（皆為 ContentItem.url 原值）時只會徒增不一致風險。
    """
    if not url:
        return ""
    return url.strip().rstrip("/").replace("http:", "https:", 1)


def _within_days(path: Path, days: int | None) -> bool:
    if days is None:
        return True
    m = _DATE_RE.match(path.stem)
    if not m:
        return False
    return date.fromisoformat(m.group(1)) >= date.today() - timedelta(days=days)


def _unescape_field(value):
    """回傳 (新值, 修正筆數)。字串與字串陣列都處理。"""
    if isinstance(value, str):
        new = html.unescape(value)
        return new, int(new != value)
    if isinstance(value, list):
        out, n = [], 0
        for v in value:
            nv, c = _unescape_field(v)
            out.append(nv)
            n += c
        return out, n
    return value, 0


def repair_all(
    days: int | None = None,
    dry_run: bool = False,
    fetcher: Callable[[str], str] | None = None,
) -> dict:
    """修復歷史資料。fetcher 為注入點（測試必須注入，避免真實 HTTP）。"""
    stats = {"hf_refetched": 0, "hf_failed": 0, "entities_fixed": 0, "files_written": 0}
    fetched: dict[str, str] = {}  # normUrl -> 修好的 abstract，供 lists 同步

    if fetcher is None:
        from src.utils import get_http_client

        client = get_http_client()
        fetcher = lambda url: fetch_paper_abstract(client, url)  # noqa: E731

    # ── data/raw ──────────────────────────────────────────
    for path in sorted(_RAW_DIR.glob("*.json")) if _RAW_DIR.exists() else []:
        if not _within_days(path, days):
            continue
        try:
            items = json.loads(path.read_text(encoding="utf-8"))
        except Exception:
            _logger.warning("Skipping unreadable raw file", extra={"path": str(path)})
            continue
        if not isinstance(items, list):
            continue

        changed = False
        for it in items:
            if not isinstance(it, dict):
                continue
            # 1) HF 黏字重抓
            if it.get("source") == "hf_papers" and looks_unspaced(it.get("abstract") or ""):
                new_abs = fetcher(it.get("url", ""))
                if new_abs and not looks_unspaced(new_abs):
                    it["abstract"] = new_abs
                    fetched[_norm_url(it.get("url", ""))] = new_abs
                    stats["hf_refetched"] += 1
                    changed = True
                else:
                    stats["hf_failed"] += 1
                    _logger.warning("HF abstract refetch failed", extra={"url": it.get("url")})
            # 2) entity 解碼
            for field in ("title", "abstract", "tags"):
                if field not in it:
                    continue
                new_val, n = _unescape_field(it[field])
                if n:
                    it[field] = new_val
                    stats["entities_fixed"] += n
                    changed = True

        if changed and not dry_run:
            save_json(items, path)
            stats["files_written"] += 1

    # ── output/lists ──────────────────────────────────────
    for path in sorted(_LISTS_DIR.glob("*.json")) if _LISTS_DIR.exists() else []:
        if not _within_days(path, days):
            continue
        try:
            doc = json.loads(path.read_text(encoding="utf-8"))
        except Exception:
            continue
        if not isinstance(doc, dict):
            continue

        changed = False
        buckets = [doc.get("github") or []]
        papers = doc.get("papers") or {}
        buckets += [papers.get("hf") or [], papers.get("others") or []]
        for entries in buckets:
            for e in entries:
                if not isinstance(e, dict):
                    continue
                repaired = fetched.get(_norm_url(e.get("url", "")))
                if repaired and e.get("abstract") != repaired:
                    e["abstract"] = repaired
                    changed = True
                for field in ("title", "abstract"):
                    if field not in e:
                        continue
                    new_val, n = _unescape_field(e[field])
                    if n:
                        e[field] = new_val
                        stats["entities_fixed"] += n
                        changed = True

        if changed and not dry_run:
            save_json(doc, path)
            stats["files_written"] += 1

    # ── output/posts（只動 frontmatter title 行）─────────────
    for path in sorted(_POSTS_DIR.glob("*.md")) if _POSTS_DIR.exists() else []:
        if not _within_days(path, days):
            continue
        text = path.read_text(encoding="utf-8")
        m = _TITLE_LINE_RE.search(text)
        if not m:
            continue
        new_title, n = _unescape_field(m.group(1))
        if not n:
            continue
        stats["entities_fixed"] += n
        if not dry_run:
            path.write_text(
                text[: m.start(1)] + new_title + text[m.end(1) :], encoding="utf-8"
            )
            stats["files_written"] += 1

    return stats
```

- [ ] **Step 4: 跑測試確認通過**

Run: `pytest tests/test_repair.py -v`
Expected: 9 passed

- [ ] **Step 5: 加 CLI 指令**

在 `src/cli.py` 的 `backfill_votes` 之後插入：

```python
@app.command(name="repair-content")
def repair_content(
    days: int = typer.Option(None, "--days", "-n", help="只修最近 N 天（預設全期）"),
    dry_run: bool = typer.Option(False, "--dry-run", help="只報告不寫檔"),
):
    """修復歷史資料：HF 摘要黏字重抓 + 跨來源 HTML entity 解碼。"""
    from src.repair import repair_all

    stats = repair_all(days=days, dry_run=dry_run)
    console.print(
        f"HF 重抓成功 [green]{stats['hf_refetched']}[/green] / "
        f"失敗 [yellow]{stats['hf_failed']}[/yellow]，"
        f"entity 修正 [green]{stats['entities_fixed']}[/green] 處，"
        f"寫入 [bold]{stats['files_written']}[/bold] 個檔案"
    )
    if dry_run:
        console.print("[yellow]--dry-run：未寫入任何檔案[/yellow]")
```

- [ ] **Step 6: 驗證 CLI 可用（dry-run，不改檔）**

Run: `python -m src.cli repair-content --days 3 --dry-run`
Expected: 印出統計，且 `git status --porcelain data/ output/` 為空

- [ ] **Step 7: Commit**

```bash
git add src/repair.py src/cli.py tests/test_repair.py
git commit -m "fix: 新增 repair-content 修復 HF 摘要黏字與 HTML entity"
```

---

### Task 4: `web/src/raw.ts` — build 時讀取原始資料

**Files:**
- Create: `web/src/raw.ts`

**Interfaces:**
- Consumes: `normalizeUrl(url)` from `web/src/enrich.ts`、`RECENT_DAYS` from `web/src/utils.ts`
- Produces:
  - `export interface RawItem { title, abstract, authors, organization, tags, sourceName, url, collectedDate, signals }`
  - `signals: { label: string; value: number }[]`
  - `export function loadRaw(): Map<string, RawItem>`（key 為 `normalizeUrl(url)`）

- [ ] **Step 1: 建立 `web/src/raw.ts`**

```ts
import fs from 'node:fs';
import path from 'node:path';
import { normalizeUrl } from './enrich';
import { RECENT_DAYS } from './utils';

// 從 data/raw/{date}.json 讀取來源原始資料，供詳情頁的「原始資料」box 使用。
// why 不共用 enrich.ts（data/scored）：pinned 文免評分、不在 scored 裡，
// 實測近 200 篇 posts 有 10 篇會查無資料；raw 則 200/200 全中。
// raw JSON 不在 web/ 內，故用 fs 直讀（cwd = web/，與 content.config.ts 的 glob base 同基準）。

export interface RawItem {
  title: string;
  abstract: string;
  authors: string[];
  organization: string;
  tags: string[];
  sourceName: string;
  url: string;
  collectedDate: string; // YYYY-MM-DD
  signals: { label: string; value: number }[];
}

// raw_metadata 中值得展示的天然訊號；沒有或為 0 的不顯示
const SIGNAL_LABELS: [string, string][] = [
  ['upvotes', '👍 upvotes'],
  ['stars_today', '⭐ stars today'],
  ['points', 'HN points'],
  ['num_comments', 'HN 留言'],
  ['citation_count', '📖 citations'],
];

function toSignals(meta: unknown): { label: string; value: number }[] {
  if (!meta || typeof meta !== 'object') return [];
  const m = meta as Record<string, unknown>;
  const out: { label: string; value: number }[] = [];
  for (const [key, label] of SIGNAL_LABELS) {
    const v = Number(m[key]);
    if (Number.isFinite(v) && v > 0) out.push({ label, value: v });
  }
  return out;
}

let cache: Map<string, RawItem> | null = null;

export function loadRaw(): Map<string, RawItem> {
  // dev server 是長駐進程，快取會看不到 pipeline 新寫入的 raw JSON；只在 build 時快取
  if (import.meta.env?.DEV) cache = null;
  if (cache) return cache;

  const map = new Map<string, RawItem>();
  const dir = path.resolve(process.cwd(), '../data/raw');
  let files: string[] = [];
  try {
    files = fs.readdirSync(dir).filter((f) => f.endsWith('.json'));
  } catch {
    cache = map;
    return map; // 沒有 raw 資料時優雅降級
  }

  // 詳情頁只 build 近 RECENT_DAYS 天，多讀的檔案純屬浪費 build 時間
  const cutoff = new Date(Date.now() - RECENT_DAYS * 86400_000).toISOString().slice(0, 10);

  for (const file of files) {
    const day = file.slice(0, 10);
    if (day < cutoff) continue;
    let parsed: unknown;
    try {
      parsed = JSON.parse(fs.readFileSync(path.join(dir, file), 'utf-8'));
    } catch {
      continue;
    }
    if (!Array.isArray(parsed)) continue;
    for (const it of parsed) {
      const url = normalizeUrl(it?.url);
      if (!url) continue;
      map.set(url, {
        title: it.title ?? '',
        abstract: it.abstract ?? '',
        authors: Array.isArray(it.authors) ? it.authors : [],
        organization: it.organization ?? '',
        tags: Array.isArray(it.tags) ? it.tags.filter((t: unknown) => typeof t === 'string') : [],
        sourceName: it.source_name ?? '',
        url: it.url ?? '',
        collectedDate: day,
        signals: toSignals(it.raw_metadata),
      });
    }
  }

  cache = map;
  return map;
}
```

- [ ] **Step 2: 驗證能編譯且真的讀到資料**

Run:
```bash
cd web && npx astro check 2>&1 | tail -5
```
Expected: 0 errors（若 `astro check` 未安裝依賴則跳過，改由 Task 5 的 build 驗證）

- [ ] **Step 3: Commit**

```bash
git add web/src/raw.ts
git commit -m "feat: 新增 loadRaw() 於 build 時讀取來源原始資料"
```

---

### Task 5: Astro `/daily/<id>` 渲染原始資料 box

**Files:**
- Modify: `web/src/pages/daily/[slug].astro`

**Interfaces:**
- Consumes: `loadRaw()`、`RawItem`（Task 4）

- [ ] **Step 1: 在 `getStaticPaths()` 取得 raw item**

改 `web/src/pages/daily/[slug].astro` 的 frontmatter 區：

import 區加一行：
```ts
import { loadRaw } from '../../raw';
```

`getStaticPaths()` 內，在 `const enrichMap = loadEnrichment();` 下面加：
```ts
  const rawMap = loadRaw();
```

`return recent.map(...)` 內，在 `const e = ...` 下面加：
```ts
    const raw = rawMap.get(normalizeUrl(post.data.url)) ?? null;
```

`props` 物件加一個欄位：
```ts
        raw,
```

最後把 props 解構那行改成：
```ts
const { post, enrich, newer, older, related, raw } = Astro.props;
```

- [ ] **Step 2: 插入 `<details>` box**

在 `<div class="prose"><Content /></div>` 之後、`post.data.model &&` 那段之前插入：

```astro
    {
      raw && (
        <details class="raw-box">
          <summary>
            <span class="raw-caret" aria-hidden="true">▸</span>
            原始資料
            <span class="raw-hint">{raw.sourceName} · 收集於 {raw.collectedDate}</span>
          </summary>
          <div class="raw-body">
            <dl class="raw-meta">
              <dt>來源原標題</dt>
              <dd>{raw.title}</dd>
              {raw.organization && (
                <>
                  <dt>機構</dt>
                  <dd>{raw.organization}</dd>
                </>
              )}
              {raw.authors.length > 0 && (
                <>
                  <dt>作者</dt>
                  <dd>{raw.authors.join(', ')}</dd>
                </>
              )}
              {raw.tags.length > 0 && (
                <>
                  <dt>原始標籤</dt>
                  <dd>{raw.tags.join(' · ')}</dd>
                </>
              )}
              {raw.signals.length > 0 && (
                <>
                  <dt>來源訊號</dt>
                  <dd>{raw.signals.map((s) => `${s.label} ${s.value}`).join('　')}</dd>
                </>
              )}
              <dt>原始連結</dt>
              <dd>
                <a href={raw.url} target="_blank" rel="noopener">{raw.url}</a>
              </dd>
            </dl>
            <h4>摘要原文</h4>
            {raw.abstract ? (
              <p class="raw-abstract">{raw.abstract}</p>
            ) : (
              <p class="raw-none">（來源未提供摘要）</p>
            )}
          </div>
        </details>
      )
    }
```

- [ ] **Step 3: 加樣式**

在 `<style>` 區塊內、`.model-note` 規則之前插入：

```css
  .raw-box {
    margin-top: 2.5rem;
    background: var(--surface);
    border: 1px solid var(--border);
    border-radius: var(--radius);
  }
  .raw-box > summary {
    cursor: pointer;
    padding: 0.75rem 1.1rem;
    font-family: var(--mono);
    font-size: 0.82rem;
    color: var(--muted);
    list-style: none;
    display: flex;
    align-items: center;
    gap: 0.5rem;
  }
  .raw-box > summary::-webkit-details-marker {
    display: none;
  }
  .raw-box > summary:hover {
    color: var(--text);
  }
  .raw-caret {
    color: var(--accent);
    transition: transform 0.15s ease;
    display: inline-block;
  }
  .raw-box[open] .raw-caret {
    transform: rotate(90deg);
  }
  .raw-hint {
    margin-left: auto;
    color: var(--faint);
    font-size: 0.74rem;
  }
  .raw-body {
    border-top: 1px solid var(--border);
    padding: 1rem 1.1rem 1.2rem;
  }
  .raw-meta {
    display: grid;
    grid-template-columns: 6rem 1fr;
    gap: 0.35rem 0.9rem;
    margin: 0 0 1.1rem;
    font-size: 0.82rem;
  }
  .raw-meta dt {
    font-family: var(--mono);
    font-size: 0.74rem;
    color: var(--faint);
  }
  .raw-meta dd {
    margin: 0;
    color: var(--muted);
    overflow-wrap: anywhere;
  }
  .raw-body h4 {
    margin: 0 0 0.45rem;
    font-size: 0.72rem;
    text-transform: uppercase;
    letter-spacing: 0.08em;
    color: var(--faint);
  }
  .raw-abstract {
    margin: 0;
    font-size: 0.85rem;
    line-height: 1.7;
    color: var(--muted);
    white-space: pre-wrap;
  }
  .raw-none {
    margin: 0;
    font-size: 0.85rem;
    color: var(--faint);
  }
  @media (max-width: 700px) {
    .raw-meta {
      grid-template-columns: 1fr;
      gap: 0.1rem 0;
    }
    .raw-meta dd {
      margin-bottom: 0.5rem;
    }
  }
```

- [ ] **Step 4: build 並確認頁面正確**

Run:
```bash
cd web && npm run build 2>&1 | tail -20
```
Expected: build 成功、0 errors

接著確認 box 真的被渲染進去（挑一篇有 raw 的近期文章）：
```bash
cd web && grep -l 'class="raw-box"' dist/daily/*/index.html | wc -l
```
Expected: 數字 > 0

- [ ] **Step 5: Commit**

```bash
git add web/src/pages/daily/\[slug\].astro
git commit -m "feat: /daily 詳情頁加入原始資料展開 box"
```

---

### Task 6: Web Monitor 原始資料 box

**Files:**
- Modify: `src/web/data_service.py`、`src/web/app.py:277-303`、`src/web/templates/post_view.html`
- Test: `tests/test_web/test_data_service_raw.py`

**Interfaces:**
- Produces: `get_raw_by_url(date_str: str, url: str) -> dict | None`
  回傳 `{"title", "abstract", "authors", "organization", "tags", "source_name", "url", "collected_date", "signals"}`；`signals` 為 `list[tuple[str, int]]`

- [ ] **Step 1: 寫失敗的測試**

建立 `tests/test_web/test_data_service_raw.py`：

```python
"""get_raw_by_url() 測試。"""

from __future__ import annotations

import json

import pytest


@pytest.fixture
def raw_day(tmp_path, monkeypatch):
    monkeypatch.chdir(tmp_path)
    d = tmp_path / "data/raw"
    d.mkdir(parents=True)
    (d / "2026-07-27.json").write_text(
        json.dumps([
            {"source": "hf_papers", "source_name": "HuggingFace Daily Papers",
             "title": "Skill Self-Play", "url": "https://huggingface.co/papers/2607.1",
             "authors": ["A", "B"], "abstract": "An abstract.", "tags": ["LLM"],
             "organization": "HF", "published_date": "2026-07-27",
             "raw_metadata": {"upvotes": 42, "arxiv_id": "2607.1"}},
        ], ensure_ascii=False),
        encoding="utf-8",
    )
    return tmp_path


def test_finds_item_by_exact_url(raw_day):
    from src.web.data_service import get_raw_by_url

    got = get_raw_by_url("2026-07-27", "https://huggingface.co/papers/2607.1")
    assert got is not None
    assert got["title"] == "Skill Self-Play"
    assert got["abstract"] == "An abstract."
    assert got["authors"] == ["A", "B"]
    assert got["collected_date"] == "2026-07-27"


def test_matches_despite_trailing_slash_and_scheme(raw_day):
    from src.web.data_service import get_raw_by_url

    assert get_raw_by_url("2026-07-27", "http://huggingface.co/papers/2607.1/") is not None


def test_returns_none_when_url_absent(raw_day):
    from src.web.data_service import get_raw_by_url

    assert get_raw_by_url("2026-07-27", "https://example.com/nope") is None


def test_returns_none_when_no_raw_file(raw_day):
    from src.web.data_service import get_raw_by_url

    assert get_raw_by_url("2020-01-01", "https://huggingface.co/papers/2607.1") is None


def test_exposes_only_positive_signals(raw_day):
    from src.web.data_service import get_raw_by_url

    got = get_raw_by_url("2026-07-27", "https://huggingface.co/papers/2607.1")
    assert got["signals"] == [("👍 upvotes", 42)]  # arxiv_id 非數值訊號，不列入
```

- [ ] **Step 2: 跑測試確認失敗**

Run: `pytest tests/test_web/test_data_service_raw.py -v`
Expected: FAIL — `ImportError: cannot import name 'get_raw_by_url'`

- [ ] **Step 3: 實作 `get_raw_by_url()`**

加到 `src/web/data_service.py` 的 `get_day_raw_items()` 之後：

```python
# raw_metadata 中值得展示的天然訊號；與 web/src/raw.ts 的 SIGNAL_LABELS 保持一致
_RAW_SIGNAL_LABELS = [
    ("upvotes", "👍 upvotes"),
    ("stars_today", "⭐ stars today"),
    ("points", "HN points"),
    ("num_comments", "HN 留言"),
    ("citation_count", "📖 citations"),
]


def _norm_raw_url(url: str) -> str:
    """輕量 URL 正規化，與 web/src/enrich.ts 的 normalizeUrl 一致。

    why 不用 utils.normalize_url：那支為去重設計會排序 query、去 www.；
    這裡兩端來源相同（皆為 ContentItem.url 原值），輕量比對即可。
    """
    if not url:
        return ""
    return url.strip().rstrip("/").replace("http:", "https:", 1)


def get_raw_by_url(date_str: str, url: str) -> dict | None:
    """依 URL 取回當日 raw 收集項目，供詳情頁的「原始資料」box 使用。

    why 不重用 get_day_raw_items()：那支丟掉了 organization 與 raw_metadata，
    box 需要機構與 upvotes / stars_today 等天然訊號。
    """
    target = _norm_raw_url(url)
    if not target:
        return None
    try:
        d = date.fromisoformat(date_str)
    except ValueError:
        return None
    raw_path = _get_raw_path(d)
    if not raw_path.exists():
        return None
    data = load_json(raw_path)
    if not isinstance(data, list):
        return None

    for it in data:
        if not isinstance(it, dict) or _norm_raw_url(it.get("url", "")) != target:
            continue
        meta = it.get("raw_metadata") or {}
        signals = []
        for key, label in _RAW_SIGNAL_LABELS:
            v = meta.get(key)
            if isinstance(v, (int, float)) and v > 0:
                signals.append((label, int(v)))
        return {
            "title": it.get("title", ""),
            "abstract": it.get("abstract", ""),
            "authors": it.get("authors") or [],
            "organization": it.get("organization", ""),
            "tags": it.get("tags") or [],
            "source_name": it.get("source_name", ""),
            "url": it.get("url", ""),
            "collected_date": date_str,
            "signals": signals,
        }
    return None
```

- [ ] **Step 4: 跑測試確認通過**

Run: `pytest tests/test_web/test_data_service_raw.py -v`
Expected: 5 passed

- [ ] **Step 5: route 傳入 `raw_item`**

改 `src/web/app.py` 的 `post_view`（約 277-303 行），在 `feedback = ds.get_feedback(...)` 之後加：

```python
    # why 只有 post_view 傳 raw_item：note_view 共用同一個 template，
    # 不傳就自然不渲染 box（AI 筆記沒有對應的收集來源）
    raw_item = ds.get_raw_by_url(date_str, post["frontmatter"].get("url", ""))
```

並在 `TemplateResponse` 的 context dict 加一行：
```python
            "raw_item": raw_item,
```

- [ ] **Step 6: template 渲染 box**

在 `src/web/templates/post_view.html` 的正文內容區塊之後、回饋區塊之前插入：

```html
{% if raw_item %}
<details style="margin-top:24px; border:1px solid #e2e5ea; border-radius:8px; background:#fafbfc;">
  <summary style="cursor:pointer; padding:10px 14px; font-size:13px; color:#5a6472;">
    原始資料
    <span style="float:right; color:#9aa3af; font-size:12px;">
      {{ raw_item.source_name }} · 收集於 {{ raw_item.collected_date }}
    </span>
  </summary>
  <div style="border-top:1px solid #e2e5ea; padding:14px;">
    <table style="font-size:13px; border-collapse:collapse; margin-bottom:12px;">
      <tr><td style="color:#9aa3af; padding:2px 12px 2px 0; white-space:nowrap;">來源原標題</td>
          <td>{{ raw_item.title }}</td></tr>
      {% if raw_item.organization %}
      <tr><td style="color:#9aa3af; padding:2px 12px 2px 0;">機構</td>
          <td>{{ raw_item.organization }}</td></tr>
      {% endif %}
      {% if raw_item.authors %}
      <tr><td style="color:#9aa3af; padding:2px 12px 2px 0;">作者</td>
          <td>{{ raw_item.authors | join(', ') }}</td></tr>
      {% endif %}
      {% if raw_item.tags %}
      <tr><td style="color:#9aa3af; padding:2px 12px 2px 0;">原始標籤</td>
          <td>{{ raw_item.tags | join(' · ') }}</td></tr>
      {% endif %}
      {% if raw_item.signals %}
      <tr><td style="color:#9aa3af; padding:2px 12px 2px 0;">來源訊號</td>
          <td>{% for label, value in raw_item.signals %}{{ label }} {{ value }}{% if not loop.last %}　{% endif %}{% endfor %}</td></tr>
      {% endif %}
      <tr><td style="color:#9aa3af; padding:2px 12px 2px 0;">原始連結</td>
          <td><a href="{{ raw_item.url }}" target="_blank" rel="noopener">{{ raw_item.url }}</a></td></tr>
    </table>
    <div style="color:#9aa3af; font-size:11px; letter-spacing:.06em; margin-bottom:6px;">摘要原文</div>
    {% if raw_item.abstract %}
    <p style="margin:0; font-size:13.5px; line-height:1.7; color:#4a5260; white-space:pre-wrap;">{{ raw_item.abstract }}</p>
    {% else %}
    <p style="margin:0; font-size:13.5px; color:#9aa3af;">（來源未提供摘要）</p>
    {% endif %}
  </div>
</details>
{% endif %}
```

- [ ] **Step 7: 跑 web 測試確認沒有回歸**

Run: `pytest tests/test_web/ -v`
Expected: all passed（含 `note_view` 相關案例——它不傳 `raw_item`，box 不應渲染）

- [ ] **Step 8: Commit**

```bash
git add src/web/data_service.py src/web/app.py src/web/templates/post_view.html tests/test_web/test_data_service_raw.py
git commit -m "feat: Web Monitor 詳情頁加入原始資料展開 box"
```

---

### Task 7: 執行修復，資料 diff 獨立 commit

**Files:**
- Modify（由 CLI 產生）：`data/raw/*.json`、`output/lists/*.json`、`output/posts/*.md`

**Interfaces:**
- Consumes: `repair-content` CLI（Task 3）

- [ ] **Step 1: 先跑 dry-run 確認規模符合預期**

Run: `python -m src.cli repair-content --dry-run`
Expected: HF 待修約 192 筆、entity 修正約 335 處。**若數字與此差距超過一個數量級就停下來查原因，不要直接寫檔。**

- [ ] **Step 2: 實際執行**

Run: `python -m src.cli repair-content`

- [ ] **Step 3: 驗證修復結果**

```bash
python3 - <<'EOF'
import json, glob
def ratio(a): return a.count(' ')/len(a) if a else 1
bad = ent = 0
import re
pat = re.compile(r'&(?:#x?[0-9a-fA-F]+|[a-zA-Z]{2,8});')
import html as _h
for f in glob.glob('data/raw/*.json'):
    for it in json.load(open(f)):
        a = it.get('abstract') or ''
        if it.get('source') == 'hf_papers' and len(a) > 100 and ratio(a) < 0.05:
            bad += 1
        for fld in ('title', 'abstract'):
            v = it.get(fld) or ''
            if pat.search(v) and _h.unescape(v) != v:
                ent += 1
print('殘留 HF 黏字:', bad, '| 殘留未解碼 entity:', ent)
EOF
grep -l '&#' output/posts/*.md | wc -l
```
Expected: 黏字殘留為抓取失敗的少數（記在 log 裡）、entity 殘留 0、`output/posts` 命中 0

- [ ] **Step 4: 確認 posts 的 body 沒被動到**

Run: `git diff --stat output/posts/ && git diff output/posts/ | grep '^[+-]' | grep -v '^[+-][+-]' | grep -v '^[+-]title:' | head`
Expected: 只有 4 個檔案、diff 僅出現在 `title:` 行（第二個指令無輸出）

- [ ] **Step 5: Commit（獨立）**

```bash
git add data/raw output/lists output/posts
git commit -m "chore: 修復歷史資料的 HF 摘要黏字與 HTML entity"
```

---

### Task 8: 端對端驗證

**Files:** 無（純驗證）

- [ ] **Step 1: 全套測試**

Run: `pytest tests/ -q`
Expected: all passed

- [ ] **Step 2: Astro build 並確認三種情境**

```bash
cd web && npm run build 2>&1 | tail -5
grep -l 'class="raw-box"' dist/daily/*/index.html | wc -l
```
Expected: build 成功；有 box 的頁面數 > 0

挑一篇 **pinned 文**（`grep -l 'pinned: true' ../output/posts/*.md | tail -1`，取近 30 天內者）確認它的 `dist/daily/<id>/index.html` 也含 `raw-box`——這是 raw-first 設計的關鍵驗證點，用 scored 會查不到。

挑一篇 **hackernews 來源**的文章，確認頁面內不含 `&#x2F;`。

- [ ] **Step 3: 用真實瀏覽器開頁面**

```bash
cd web && npm run preview -- --host 0.0.0.0
```
以 `http://$(hostname -I | awk '{print $1}'):4321/daily/<id>` 開啟（WSL2 下 `localhost` 不通）。
確認：box 預設收合、點擊展開、摘要原文換行正常、手機寬度下 meta 不擠壓。

- [ ] **Step 4: 啟動 Monitor 確認同一篇**

```bash
python -m src.cli web
```
開 `http://$(hostname -I | awk '{print $1}'):8555/post/<date>/<slug>` 確認 box 正常；再開一篇 `/note/<date>/<slug>` 確認**沒有** box。

- [ ] **Step 5: 更新 CHANGELOG**

在 `CHANGELOG.md` 最上方加：

```markdown
## [2026-07-28]
### Added
- 摘要詳情頁（Astro `/daily` 與 Web Monitor）新增「原始資料」可展開 box，顯示來源原標題、摘要原文、作者、機構、原始標籤與天然訊號
### Fixed
- `ContentItem` 建構時解碼 HTML entity，修正 RSS 標題與 HN 摘要的 `&#8217;` / `&#x2F;` 外洩
- HF 論文摘要的 arXiv fallback 不再被「空白被吃掉」的長字串繞過
- 新增 `repair-content` 指令並回補歷史資料
```

- [ ] **Step 6: Commit**

```bash
git add CHANGELOG.md
git commit -m "docs: CHANGELOG 記錄原始資料 box 與資料修復"
```

---

## 驗證缺口（實作者必須知道）

- `web/` 沒有 TS 測試框架，`loadRaw()` 沒有單元測試，只靠 Task 5/8 的 build + 實際開頁面驗證。若 build 通過但 box 沒出現，第一個要查的是 `normalizeUrl` 兩端是否對得上。
  （**2026-07-31 已推翻**：`e77f802` 引入 vitest，使用者追認；`loadRaw()` 現在可以補單元測試了。上述缺口敘述為當時實況，保留不改）
- `repair-content` 的 HF 重抓會打真實 HF 網站（約 192 次請求）。Task 3 的測試全部注入 stub，**真實抓取路徑只在 Task 7 的 dry-run 與實跑中驗證**。
- Task 7 會改動已 commit 的 `data/` 與 `output/`，且 CI 每日也會寫這些目錄。執行前先 `git pull`，避免與 Actions 產出衝突。
