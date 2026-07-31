"""repair-content 歷史資料修復測試。所有測試以注入 fetcher 避免真實 HTTP。"""

from __future__ import annotations

import html as _html
import json

import pytest

from src.collectors.hf_papers import looks_unspaced
from src.repair import repair_all

BROKEN = "LLMtrainingisshiftingfrommanualdesignandannotationtointeractiondrivenselfevolution" * 2
FIXED = "LLM training is shifting from manual design and annotation to interaction driven self evolution. " * 2
ARXIV_TEXT = "This paper studies interaction driven self evolution of language models in depth. " * 2

# 帶得出 arxiv_id 的 HF URL（_ARXIV_ID_RE 要求小數點後 4-5 位；`2607.1` 抽不出來）
HF_URL = "https://huggingface.co/papers/2607.12345"

# 真實 data/raw 樣本——不是自己編的字串。looks_unspaced() 的門檻很窄
# （space_ratio < 0.05），隨手編的 URL 字串很容易落在門檻外而讓測試變成空砲，
# 這正是本測試上一版的 bug。每個樣本都在測試裡先斷言前置條件成立。
REDDIT_UNSPACED = (
    "Blog post: [https://qwen.ai/blog?id=qwen3.6](https://qwen.ai/blog?id=qwen3.6)\n\n"
    "From Chujie Zheng on 𝕏: [https://x.com/ChujieZheng/status/2039560126047359394]"
    "(https://x.com/ChujieZheng/status/2039560126047359394)"
)  # data/raw/2026-04-02.json — len 211, space_ratio 0.0332
HN_UNSPACED = (
    "https:&#x2F;&#x2F;x.com&#x2F;karpathy&#x2F;status&#x2F;2040470801506541998   "
    "https:&#x2F;&#x2F;xcancel.com&#x2F;karpathy&#x2F;status&#x2F;2040470801506541998"
)  # data/raw/2026-04-05.json — len 157, space_ratio 0.0191


def _write(path, obj):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(obj, ensure_ascii=False), encoding="utf-8")


def _boom(*_args, **_kwargs):
    """任何被呼叫就代表測試預期外的連網／重抓發生了。"""
    raise AssertionError("不應該被呼叫")


@pytest.fixture
def repo(tmp_path, monkeypatch):
    """在 tmp_path 造一個迷你 repo 結構並切換 cwd。"""
    monkeypatch.chdir(tmp_path)
    return tmp_path


def test_refetches_broken_hf_abstract(repo):
    _write(repo / "data/raw/2026-07-27.json", [
        {"source": "hf_papers", "source_name": "HuggingFace Daily Papers",
         "title": "T", "url": HF_URL,
         "abstract": BROKEN, "published_date": "2026-07-27"},
    ])
    res = repair_all(fetcher=lambda url: FIXED, arxiv_fetcher=_boom)
    assert res["hf_refetched"] == 1
    data = json.loads((repo / "data/raw/2026-07-27.json").read_text(encoding="utf-8"))
    assert data[0]["abstract"] == FIXED


# ── HF 重抓的三條路徑（設計 spec §6：論文頁 → arXiv fallback → 保留原值）──────

def test_falls_back_to_arxiv_when_page_fetch_fails(repo):
    """論文頁抓不到（HF 掛掉／被限流）→ 改走 arXiv。"""
    _write(repo / "data/raw/2026-07-27.json", [
        {"source": "hf_papers", "source_name": "HF", "title": "T", "url": HF_URL,
         "abstract": BROKEN, "published_date": "2026-07-27"},
    ])
    seen = []
    res = repair_all(
        fetcher=lambda url: "",
        arxiv_fetcher=lambda aid: seen.append(aid) or ARXIV_TEXT,
    )
    assert seen == ["2607.12345"]
    assert res["hf_refetched"] == 1 and res["hf_failed"] == 0
    data = json.loads((repo / "data/raw/2026-07-27.json").read_text(encoding="utf-8"))
    assert data[0]["abstract"] == ARXIV_TEXT


def test_falls_back_to_arxiv_when_page_result_still_broken(repo):
    """論文頁有回應但內容仍是黏字 → 不可採用，改走 arXiv。"""
    _write(repo / "data/raw/2026-07-27.json", [
        {"source": "hf_papers", "source_name": "HF", "title": "T", "url": HF_URL,
         "abstract": BROKEN, "published_date": "2026-07-27"},
    ])
    res = repair_all(fetcher=lambda url: BROKEN, arxiv_fetcher=lambda aid: ARXIV_TEXT)
    assert res["hf_refetched"] == 1
    data = json.loads((repo / "data/raw/2026-07-27.json").read_text(encoding="utf-8"))
    assert data[0]["abstract"] == ARXIV_TEXT


def test_keeps_original_when_refetch_fails(repo):
    """論文頁與 arXiv 皆失敗 → 保留原值，計 hf_failed。"""
    _write(repo / "data/raw/2026-07-27.json", [
        {"source": "hf_papers", "source_name": "HF", "title": "T", "url": HF_URL,
         "abstract": BROKEN, "published_date": "2026-07-27"},
    ])
    res = repair_all(fetcher=lambda url: "", arxiv_fetcher=lambda aid: "")
    assert res["hf_refetched"] == 0 and res["hf_failed"] == 1
    data = json.loads((repo / "data/raw/2026-07-27.json").read_text(encoding="utf-8"))
    assert data[0]["abstract"] == BROKEN


def test_arxiv_result_still_broken_keeps_original(repo):
    """arXiv 回來的也是黏字 → 一樣不採用。"""
    _write(repo / "data/raw/2026-07-27.json", [
        {"source": "hf_papers", "source_name": "HF", "title": "T", "url": HF_URL,
         "abstract": BROKEN, "published_date": "2026-07-27"},
    ])
    res = repair_all(fetcher=lambda url: "", arxiv_fetcher=lambda aid: BROKEN)
    assert res["hf_refetched"] == 0 and res["hf_failed"] == 1


def test_injected_fetcher_never_builds_real_http_client(repo, monkeypatch):
    """注入 fetcher 但沒注入 arxiv_fetcher 時，不得偷偷建真的 arXiv client。"""
    import src.repair as repair_mod

    monkeypatch.setattr(repair_mod, "_build_default_fetchers", _boom)
    _write(repo / "data/raw/2026-07-27.json", [
        {"source": "hf_papers", "source_name": "HF", "title": "T", "url": HF_URL,
         "abstract": BROKEN, "published_date": "2026-07-27"},
    ])
    res = repair_all(fetcher=lambda url: "")  # 只注入一半
    assert res["hf_failed"] == 1  # arXiv 退化成 no-op，不連網


def test_default_fetchers_throttle_before_each_request(monkeypatch):
    """生產路徑每次 HTTP 前都要 sleep，且沿用 collector 的既有節流常數。"""
    import src.collectors.hf_papers as hf
    import src.repair as repair_mod

    sleeps: list[float] = []
    monkeypatch.setattr(repair_mod.time, "sleep", lambda s: sleeps.append(s))
    monkeypatch.setattr("src.utils.get_http_client", lambda: object())
    monkeypatch.setattr(repair_mod, "fetch_paper_abstract", lambda client, url: "page")
    monkeypatch.setattr(repair_mod, "_fetch_arxiv_abstract", lambda aid, client: "arxiv")

    fetch_hf, fetch_arxiv = repair_mod._build_default_fetchers()
    assert fetch_hf("https://example.com") == "page"
    assert fetch_arxiv("2607.12345") == "arxiv"

    assert sleeps == [hf._ENRICH_DELAY_SECONDS, hf._ENRICH_DELAY_SECONDS]
    assert repair_mod._ENRICH_DELAY_SECONDS is hf._ENRICH_DELAY_SECONDS  # 不得另立常數


# ── source 限定（第一號硬約束）────────────────────────────────

@pytest.mark.parametrize("source,abstract", [
    ("hackernews", HN_UNSPACED),
    ("reddit", REDDIT_UNSPACED),
])
def test_does_not_touch_non_hf_unspaced_text(repo, source, abstract):
    """HN／reddit 留言是整串 URL，空白天生就少——不得被當成破損重抓。

    真實 data/raw 有 hackernews 26 筆、reddit 8 筆會命中 looks_unspaced()。
    少了 source 限定，這批會拿 fetch_paper_abstract 去抓 gist 頁與圖片 URL，
    把回來的任意 <p> 寫進真實 abstract —— 是寫壞資料，不是修不完。
    """
    # 前置條件：樣本必須真的命中判定式，否則本測試等於沒測到東西
    assert looks_unspaced(abstract), "fixture 必須命中 looks_unspaced()，否則此測試是空砲"

    _write(repo / "data/raw/2026-07-27.json", [
        {"source": source, "source_name": source, "title": "T",
         "url": "https://news.ycombinator.com/item?id=1",
         "abstract": abstract, "published_date": "2026-07-27"},
    ])
    res = repair_all(fetcher=_boom, arxiv_fetcher=_boom)
    assert res["hf_refetched"] == 0 and res["hf_failed"] == 0
    data = json.loads((repo / "data/raw/2026-07-27.json").read_text(encoding="utf-8"))
    # 內容只允許被 entity 解碼改動，不得被重抓覆蓋
    assert data[0]["abstract"] == _html.unescape(abstract)


# ── entity 解碼 ──────────────────────────────────────────────

def test_decodes_entities_across_sources(repo):
    _write(repo / "data/raw/2026-07-27.json", [
        {"source": "rss", "source_name": "The Verge AI",
         "title": "Sam Altman&#8217;s orb", "url": "https://example.com/a",
         "abstract": "a &amp; b", "tags": ["AI &amp; ML"], "published_date": "2026-07-27"},
    ])
    res = repair_all(fetcher=_boom, arxiv_fetcher=_boom)
    assert res["entities_fixed"] == 3  # title + abstract + 1 tag
    data = json.loads((repo / "data/raw/2026-07-27.json").read_text(encoding="utf-8"))
    assert data[0]["title"] == "Sam Altman’s orb"
    assert data[0]["abstract"] == "a & b"
    assert data[0]["tags"] == ["AI & ML"]


def test_syncs_lists_hf_abstract(repo):
    _write(repo / "data/raw/2026-07-27.json", [
        {"source": "hf_papers", "source_name": "HF", "title": "T", "url": HF_URL,
         "abstract": BROKEN, "published_date": "2026-07-27"},
    ])
    _write(repo / "output/lists/2026-07-27.json", {
        "date": "2026-07-27",
        "papers": {"hf": [{"slug": "t", "title": "T", "url": HF_URL,
                           "abstract": BROKEN}], "others": []},
        "github": [],
    })
    repair_all(fetcher=lambda url: FIXED, arxiv_fetcher=_boom)
    lists = json.loads((repo / "output/lists/2026-07-27.json").read_text(encoding="utf-8"))
    assert lists["papers"]["hf"][0]["abstract"] == FIXED


def test_fixes_post_frontmatter_title_only(repo):
    """posts 走字串切片而非 save_json，對應的不變量是「除 title 值外逐字元不變」。

    why full-file 比對而非 `in` 斷言：substring 斷言擋不住「順手動到別處」的
    改動（掉尾端換行、改用 text.replace() 連 body 一起換）。這條路徑沒有
    save_json 那種正規格式可比，唯一等價的防線就是整檔比對預期輸出。
    """
    p = repo / "output/posts/2026-07-27_x.md"
    p.parent.mkdir(parents=True, exist_ok=True)
    original = (
        '---\ntitle: "Sam Altman&#8217;s orb"\nurl: https://example.com/a\n---\n\n'
        "本文提到 &amp; 這個符號應該保持原樣。\n"
    )
    p.write_text(original, encoding="utf-8")

    repair_all(fetcher=_boom, arxiv_fetcher=_boom)

    expected = original.replace('"Sam Altman&#8217;s orb"', '"Sam Altman’s orb"')
    written = p.read_text(encoding="utf-8")
    assert written == expected, "只有 title 值可以變，其餘逐字元不變"
    # body 的 &amp; 是 LLM 生成內容，可能是字面意義，必須原樣保留。
    # 斷言對象一定要是**實際讀回的檔案內容**——對 `expected`（測試自己 replace 出來的）
    # 斷言是恆真式，看起來在驗 body、其實什麼都沒驗。
    assert "本文提到 &amp; 這個符號應該保持原樣。\n" in written


# ── dry-run ─────────────────────────────────────────────────

def test_dry_run_writes_nothing(repo):
    """三條寫檔路徑（raw / lists / posts）都必須被 dry-run 擋下。"""
    raw = repo / "data/raw/2026-07-27.json"
    _write(raw, [
        {"source": "rss", "source_name": "R", "title": "A&#8217;s",
         "url": "https://example.com/a", "abstract": "", "published_date": "2026-07-27"},
    ])
    lists = repo / "output/lists/2026-07-27.json"
    _write(lists, {
        "date": "2026-07-27",
        "papers": {"hf": [{"slug": "t", "title": "B&#8217;s", "url": HF_URL,
                           "abstract": "x &amp; y"}], "others": []},
        "github": [],
    })
    post = repo / "output/posts/2026-07-27_x.md"
    post.parent.mkdir(parents=True, exist_ok=True)
    post.write_text('---\ntitle: "C&#8217;s orb"\n---\n\nbody\n', encoding="utf-8")

    before = {p: p.read_text(encoding="utf-8") for p in (raw, lists, post)}
    res = repair_all(dry_run=True, fetcher=_boom, arxiv_fetcher=_boom)

    assert res["entities_fixed"] == 4  # raw title + lists title + lists abstract + post title
    assert res["files_written"] == 0
    for p, text in before.items():
        assert p.read_text(encoding="utf-8") == text, f"dry-run 不該寫 {p}"


def test_dry_run_makes_no_http_requests(repo):
    """dry-run 只清點候選數，絕不重抓——否則「先預覽再實跑」會讓請求數翻倍。"""
    _write(repo / "data/raw/2026-07-27.json", [
        {"source": "hf_papers", "source_name": "HF", "title": "T", "url": HF_URL,
         "abstract": BROKEN, "published_date": "2026-07-27"},
    ])
    res = repair_all(dry_run=True, fetcher=_boom, arxiv_fetcher=_boom)
    assert res["hf_candidates"] == 1
    assert res["hf_refetched"] == 0 and res["hf_failed"] == 0
    data = json.loads((repo / "data/raw/2026-07-27.json").read_text(encoding="utf-8"))
    assert data[0]["abstract"] == BROKEN


def test_dry_run_never_builds_real_http_client(repo, monkeypatch):
    """dry-run 連 client 都不該建（完全不連網）。"""
    import src.repair as repair_mod

    monkeypatch.setattr(repair_mod, "_build_default_fetchers", _boom)
    _write(repo / "data/raw/2026-07-27.json", [
        {"source": "hf_papers", "source_name": "HF", "title": "T", "url": HF_URL,
         "abstract": BROKEN, "published_date": "2026-07-27"},
    ])
    res = repair_all(dry_run=True)  # 完全不注入
    assert res["hf_candidates"] == 1 and res["files_written"] == 0


# ── 寫檔格式與不寫檔 ─────────────────────────────────────────

def test_writes_in_save_json_format(repo):
    """寫回一律走 save_json（indent=2 / ensure_ascii=False），格式一走樣就是全檔假 diff。

    **三個 JSON 寫入點（data/raw、data/scored、output/lists）都要驗**——只驗其中
    一個，其他換成無 indent 的 json.dumps 也不會被抓到（本測試上一版的缺口）。
    """
    raw = repo / "data/raw/2026-07-27.json"
    _write(raw, [
        {"source": "rss", "source_name": "R", "title": "A&#8217;s 中文標題",
         "url": "https://example.com/a", "abstract": "", "published_date": "2026-07-27"},
    ])
    scored = repo / "data/scored/2026-07-27.json"
    _write(scored, [
        {"item": {"source": "rss", "source_name": "R", "title": "C&#8217;s 中文標題",
                  "url": "https://example.com/c", "abstract": "",
                  "published_date": "2026-07-27"},
         "rule_score": 30.0, "llm_score": 70.0},
    ])
    lists = repo / "output/lists/2026-07-27.json"
    _write(lists, {
        "date": "2026-07-27",
        "papers": {"hf": [], "others": [
            {"slug": "b", "title": "B&#8217;s 中文標題", "url": "https://example.com/b",
             "abstract": "x &amp; y"},
        ]},
        "github": [],
    })

    res = repair_all(fetcher=_boom, arxiv_fetcher=_boom)
    assert res["files_written"] == 3  # raw + scored + lists 三個寫入點都被觸發

    for path in (raw, scored, lists):
        text = path.read_text(encoding="utf-8")
        canonical = json.dumps(json.loads(text), ensure_ascii=False, indent=2, default=str)
        assert text == canonical, f"{path} 必須與 save_json 的正規格式逐字元相同"
        assert "中文標題" in text  # ensure_ascii=False：中文不得被跳脫成 \uXXXX


def test_no_changes_means_no_write(repo):
    raw = repo / "data/raw/2026-07-27.json"
    _write(raw, [
        {"source": "rss", "source_name": "R", "title": "clean",
         "url": "https://example.com/a", "abstract": "clean", "published_date": "2026-07-27"},
    ])
    mtime_before = raw.stat().st_mtime_ns
    res = repair_all(fetcher=_boom, arxiv_fetcher=_boom)
    assert res["files_written"] == 0
    assert raw.stat().st_mtime_ns == mtime_before


def test_days_filter_skips_older_files(repo):
    old = repo / "data/raw/2020-01-01.json"
    _write(old, [
        {"source": "rss", "source_name": "R", "title": "A&#8217;s",
         "url": "https://example.com/a", "abstract": "", "published_date": "2020-01-01"},
    ])
    res = repair_all(days=30, fetcher=_boom, arxiv_fetcher=_boom)
    assert res["entities_fixed"] == 0


# ══════════════════════════════════════════════════════════
# data/scored 依 data/raw 對齊 Layer A 欄位
# ══════════════════════════════════════════════════════════

def _scored_rec(url, title="T", abstract="A", tags=None, **extra):
    """一筆 data/scored 記錄。評分欄位刻意給滿，方便驗證它們不被動到。"""
    rec = {
        "item": {"source": "rss", "source_name": "R", "title": title, "url": url,
                 "abstract": abstract, "published_date": "2026-07-27",
                 "tags": list(tags or [])},
        "rule_score": 25.0, "rule_reasons": ["機構加分"],
        "llm_score": 72.0, "llm_reason": "很有價值",
        "novelty": 15.0, "impact": 16.0, "trending": 14.0,
        "practicality": 13.0, "blog_worthiness": 14.0,
    }
    rec.update(extra)
    return rec


def test_backfills_scored_layer_a_fields_from_raw(repo):
    """scored 的 title/abstract/tags 一律以同日 raw 為準。

    實測全庫 2712 筆有 69 筆與 raw 不一致（17 筆未解碼 entity、52 筆 abstract
    空白被吃掉），讀取端改成無損還原後就成了使用者可見的回歸。
    """
    url = "https://example.com/a"
    _write(repo / "data/raw/2026-07-27.json", [
        {"source": "rss", "source_name": "R", "title": "Sam Altman’s orb", "url": url,
         "abstract": "完整的  雙空格摘要", "tags": ["AI & ML"],
         "published_date": "2026-07-27"},
    ])
    _write(repo / "data/scored/2026-07-27.json", [
        _scored_rec(url, title="Sam Altman&#8217;s orb",
                    abstract="完整的 雙空格摘要", tags=["AI &amp; ML"]),
    ])

    res = repair_all(fetcher=_boom, arxiv_fetcher=_boom)
    assert res["scored_backfilled"] == 3  # title + abstract + tags

    rec = json.loads((repo / "data/scored/2026-07-27.json").read_text(encoding="utf-8"))[0]
    assert rec["item"]["title"] == "Sam Altman’s orb"
    assert rec["item"]["abstract"] == "完整的  雙空格摘要"  # 空白逐字比照 raw
    assert rec["item"]["tags"] == ["AI & ML"]


def test_scored_backfill_never_touches_score_fields(repo):
    """只覆寫 Layer A 三欄，評分欄位逐一保持原值。"""
    url = "https://example.com/a"
    _write(repo / "data/raw/2026-07-27.json", [
        {"source": "rss", "source_name": "R", "title": "乾淨標題", "url": url,
         "abstract": "乾淨摘要", "published_date": "2026-07-27"},
    ])
    original = _scored_rec(url, title="髒 &amp; 標題", abstract="髒摘要")
    _write(repo / "data/scored/2026-07-27.json", [original])

    repair_all(fetcher=_boom, arxiv_fetcher=_boom)

    rec = json.loads((repo / "data/scored/2026-07-27.json").read_text(encoding="utf-8"))[0]
    for field in ("rule_score", "rule_reasons", "llm_score", "llm_reason",
                  "novelty", "impact", "trending", "practicality", "blog_worthiness"):
        assert rec[field] == original[field], f"{field} 不得被修復流程改動"
    assert rec["item"]["title"] == "乾淨標題"  # 前提：這筆確實被回補過


@pytest.mark.parametrize("raw_url,scored_url", [
    ("http://example.com/a/", "https://example.com/a"),  # 髒的在 raw 側（建表要正規化）
    ("https://example.com/a", "http://example.com/a/"),  # 髒的在 scored 側（查表要正規化）
])
def test_scored_backfill_matches_by_normalized_url(repo, raw_url, scored_url):
    """配對走 normalize_url_light：scheme / 尾斜線差異不得讓配對失敗。

    **兩個方向都要測**：只測其中一邊的話，把另一邊的 normalize 拿掉照樣全綠
    （實測 mutation SURVIVED）——建表與查表是兩個獨立的施力點。
    """
    _write(repo / "data/raw/2026-07-27.json", [
        {"source": "rss", "source_name": "R", "title": "正確標題",
         "url": raw_url, "abstract": "x", "published_date": "2026-07-27"},
    ])
    _write(repo / "data/scored/2026-07-27.json", [
        _scored_rec(scored_url, title="舊標題", abstract="x"),
    ])

    res = repair_all(fetcher=_boom, arxiv_fetcher=_boom)
    assert res["scored_backfilled"] == 1
    rec = json.loads((repo / "data/scored/2026-07-27.json").read_text(encoding="utf-8"))[0]
    assert rec["item"]["title"] == "正確標題"


def test_scored_backfill_only_uses_same_day_raw(repo):
    """配對限定同日 raw——跨日同 URL 不得被拿來覆寫。"""
    url = "https://example.com/a"
    _write(repo / "data/raw/2026-07-26.json", [
        {"source": "rss", "source_name": "R", "title": "前一天的標題", "url": url,
         "abstract": "x", "published_date": "2026-07-26"},
    ])
    _write(repo / "data/scored/2026-07-27.json", [_scored_rec(url, title="當天標題")])

    res = repair_all(fetcher=_boom, arxiv_fetcher=_boom)
    assert res["scored_backfilled"] == 0
    rec = json.loads((repo / "data/scored/2026-07-27.json").read_text(encoding="utf-8"))[0]
    assert rec["item"]["title"] == "當天標題"


def test_scored_record_without_raw_counterpart_is_still_cleaned(repo):
    """配對不到 raw（實測 0 筆，但不可整筆放生）→ 仍要自行清洗。"""
    _write(repo / "data/scored/2026-07-27.json", [
        _scored_rec("https://example.com/nope", title="A&#8217;s orb",
                    abstract="访谈｜Codex 团队"),
    ])
    res = repair_all(fetcher=_boom, arxiv_fetcher=_boom)
    assert res["scored_backfilled"] == 0
    assert res["entities_fixed"] == 1 and res["simplified_converted"] == 1

    rec = json.loads((repo / "data/scored/2026-07-27.json").read_text(encoding="utf-8"))[0]
    assert rec["item"]["title"] == "A’s orb"
    assert rec["item"]["abstract"] == "訪談｜Codex 團隊"


def test_scored_copies_repaired_raw_not_stale_raw(repo):
    """順序不變量：raw 先修乾淨，scored 才抄——抄到髒 raw 等於把髒資料擴散。"""
    url = "https://example.com/a"
    _write(repo / "data/raw/2026-07-27.json", [
        {"source": "rss", "source_name": "R", "title": "访谈&#8217;s 团队", "url": url,
         "abstract": "x", "published_date": "2026-07-27"},
    ])
    _write(repo / "data/scored/2026-07-27.json", [_scored_rec(url, title="舊標題")])

    repair_all(fetcher=_boom, arxiv_fetcher=_boom)

    raw = json.loads((repo / "data/raw/2026-07-27.json").read_text(encoding="utf-8"))[0]
    rec = json.loads((repo / "data/scored/2026-07-27.json").read_text(encoding="utf-8"))[0]
    assert raw["title"] == "訪談’s 團隊"
    assert rec["item"]["title"] == raw["title"], "scored 必須等於修完的 raw，不是修之前的"


def test_scored_backfill_does_not_alias_raw_tags_list(repo):
    """tags 要複製再塞：共用同一個 list 物件會讓日後任一端的原地修改污染另一端。"""
    url = "https://example.com/a"
    _write(repo / "data/raw/2026-07-27.json", [
        {"source": "rss", "source_name": "R", "title": "T", "url": url, "abstract": "x",
         "tags": ["AI &amp; ML"], "published_date": "2026-07-27"},
    ])
    _write(repo / "data/scored/2026-07-27.json", [_scored_rec(url, tags=["舊標籤"])])

    import src.repair as repair_mod

    # aliasing 寫檔之後就看不出來了（JSON 沒有物件同一性），必須攔在寫檔當下
    saved: dict[str, object] = {}
    real_save = repair_mod.save_json

    def capture_save(data, path):
        saved[path.parent.name] = data
        real_save(data, path)

    monkey = pytest.MonkeyPatch()
    monkey.setattr(repair_mod, "save_json", capture_save)
    try:
        repair_all(fetcher=_boom, arxiv_fetcher=_boom)
    finally:
        monkey.undo()

    raw_tags = saved["raw"][0]["tags"]
    scored_tags = saved["scored"][0]["item"]["tags"]
    assert raw_tags == scored_tags == ["AI & ML"]
    assert scored_tags is not raw_tags, "必須是複製品，不得共用同一個 list 物件"


# ══════════════════════════════════════════════════════════
# 媒體標記回補（四個寫入點都要驗）
# ══════════════════════════════════════════════════════════

# 真實樣本：量子位每篇 abstract 開頭都掛著這段（實測 data/raw 命中 309 筆）
QBIT_TAG = (
    '< img id="wx_img" src="https://www.qbitai.com/wp-content/uploads/imgs/logo.png" '
    'width="600">'
)
QBIT_MEDIA = QBIT_TAG + "量子位 | 公眾號 QbitAI"
QBIT_CLEAN = "量子位 | 公眾號 QbitAI"


def test_media_strip_uses_shared_implementation():
    """必須 import models.strip_media_tags，不得另複製一份實作。"""
    import src.models as models
    import src.repair as repair_mod

    assert repair_mod.strip_media_tags is models.strip_media_tags


def test_strips_media_tags_in_raw(repo):
    _write(repo / "data/raw/2026-07-27.json", [
        {"source": "rss", "source_name": "量子位", "title": "T",
         "url": "https://example.com/a", "abstract": QBIT_MEDIA,
         "published_date": "2026-07-27"},
    ])
    res = repair_all(fetcher=_boom, arxiv_fetcher=_boom)
    assert res["media_stripped"] == 1
    data = json.loads((repo / "data/raw/2026-07-27.json").read_text(encoding="utf-8"))
    assert data[0]["abstract"] == QBIT_CLEAN


def test_strips_media_tags_in_scored(repo):
    """實測 data/scored 有 35 個 abstract 帶媒體標記。"""
    _write(repo / "data/scored/2026-07-27.json", [
        _scored_rec("https://example.com/a", abstract=QBIT_MEDIA),
    ])
    res = repair_all(fetcher=_boom, arxiv_fetcher=_boom)
    assert res["media_stripped"] == 1
    rec = json.loads((repo / "data/scored/2026-07-27.json").read_text(encoding="utf-8"))[0]
    assert rec["item"]["abstract"] == QBIT_CLEAN


def test_strips_media_tags_in_lists(repo):
    """實測 output/lists 目前 0 筆命中，但這條路徑上一版根本沒掃過。"""
    _write(repo / "output/lists/2026-07-27.json", {
        "date": "2026-07-27",
        "papers": {"hf": [], "others": [
            {"slug": "b", "title": "T", "url": "https://example.com/b",
             "abstract": QBIT_MEDIA},
        ]},
        "github": [],
    })
    res = repair_all(fetcher=_boom, arxiv_fetcher=_boom)
    assert res["media_stripped"] == 1
    doc = json.loads((repo / "output/lists/2026-07-27.json").read_text(encoding="utf-8"))
    assert doc["papers"]["others"][0]["abstract"] == QBIT_CLEAN


def test_strips_media_tags_in_post_title_only(repo):
    """實測 output/posts 目前 0 篇 title 帶媒體標記，但這條路徑上一版沒掃過。

    標記刻意放在標題中段而非開頭：frontmatter 的 title 值含引號，開頭剝除後
    `strip_media_tags()` 的 `.strip()` 收不到引號內側的空白（`" 量子位…"`），
    那是既有函式的行為而非本測試要釘的東西。
    """
    p = repo / "output/posts/2026-07-27_x.md"
    p.parent.mkdir(parents=True, exist_ok=True)
    body_tag = '<img src="https://example.com/fig.png">'
    dirty_title = f'量子位{QBIT_TAG}報導'
    original = f'---\ntitle: "{dirty_title}"\n---\n\n正文的 {body_tag} 不得被剝除。\n'
    p.write_text(original, encoding="utf-8")

    res = repair_all(fetcher=_boom, arxiv_fetcher=_boom)
    assert res["media_stripped"] == 1
    expected = original.replace(dirty_title, "量子位 報導")
    written = p.read_text(encoding="utf-8")
    assert written == expected, "只有 title 值可以變，其餘逐字元不變"
    assert body_tag in written, "正文的媒體標記必須原封不動（要對實際檔案內容斷言）"


# ══════════════════════════════════════════════════════════
# 簡→繁（四個寫入點 + 兩道守門）
# ══════════════════════════════════════════════════════════

# 真實樣本：data/raw/2026-04-07.json 的 ChatPaper title
SIMPLIFIED = "访谈｜Codex 团队如何用自己的产品构建产品"
TRADITIONAL = "訪談｜Codex 團隊如何用自己的產品構建產品"

# 已是繁體、但 OpenCC 詞組規則會誤觸發的真實樣本（皆取自 data/raw）
#   說明了 → 說明瞭（明了→明瞭）、裡面包括 → 裡麵包括（面包→麵包）
TRAD_TRAPS = [
    "但也說明了一件事：智慧體不只會埋頭幹活",
    "這是一套用於AI計算的模組化資料中心硬體系統，裡面包括計算機伺服器",
]


def test_converts_simplified_in_raw(repo):
    _write(repo / "data/raw/2026-07-27.json", [
        {"source": "chatpaper", "source_name": "ChatPaper", "title": SIMPLIFIED,
         "url": "https://example.com/a", "abstract": SIMPLIFIED,
         "tags": [SIMPLIFIED], "published_date": "2026-07-27"},
    ])
    res = repair_all(fetcher=_boom, arxiv_fetcher=_boom)
    assert res["simplified_converted"] == 3  # title + abstract + 1 tag
    data = json.loads((repo / "data/raw/2026-07-27.json").read_text(encoding="utf-8"))
    assert data[0]["title"] == TRADITIONAL
    assert data[0]["abstract"] == TRADITIONAL
    assert data[0]["tags"] == [TRADITIONAL]


def test_converts_simplified_in_scored(repo):
    _write(repo / "data/scored/2026-07-27.json", [
        _scored_rec("https://example.com/a", title=SIMPLIFIED, abstract=SIMPLIFIED),
    ])
    res = repair_all(fetcher=_boom, arxiv_fetcher=_boom)
    assert res["simplified_converted"] == 2
    rec = json.loads((repo / "data/scored/2026-07-27.json").read_text(encoding="utf-8"))[0]
    assert rec["item"]["title"] == TRADITIONAL


def test_converts_simplified_in_lists(repo):
    _write(repo / "output/lists/2026-07-27.json", {
        "date": "2026-07-27",
        "papers": {"hf": [{"slug": "b", "title": SIMPLIFIED,
                           "url": "https://example.com/b", "abstract": SIMPLIFIED}],
                   "others": []},
        "github": [],
    })
    res = repair_all(fetcher=_boom, arxiv_fetcher=_boom)
    assert res["simplified_converted"] == 2
    doc = json.loads((repo / "output/lists/2026-07-27.json").read_text(encoding="utf-8"))
    assert doc["papers"]["hf"][0]["title"] == TRADITIONAL


def test_converts_simplified_in_post_title_only(repo):
    """實測 output/posts 有 11 篇 frontmatter title 仍是簡體。"""
    p = repo / "output/posts/2026-07-27_x.md"
    p.parent.mkdir(parents=True, exist_ok=True)
    original = f'---\ntitle: "{SIMPLIFIED}"\n---\n\n正文的 {SIMPLIFIED} 不得被轉換。\n'
    p.write_text(original, encoding="utf-8")

    res = repair_all(fetcher=_boom, arxiv_fetcher=_boom)
    assert res["simplified_converted"] == 1
    expected = original.replace(f'"{SIMPLIFIED}"', f'"{TRADITIONAL}"')
    written = p.read_text(encoding="utf-8")
    assert written == expected, "只有 title 值可以變，其餘逐字元不變"
    assert f"正文的 {SIMPLIFIED} 不得被轉換。" in written, "正文簡體必須留著（對實際檔案斷言）"


@pytest.mark.parametrize("body", [
    # 正文的程式碼區塊在示範 YAML frontmatter 寫法
    "```yaml\ntitle: 访谈｜Codex 团队\n```\n",
    # 正文直接有一行以 title: 開頭
    "title: 访谈｜Codex 团队\n",
])
def test_only_frontmatter_title_line_is_considered(repo, body):
    """`title:` 的搜尋範圍限定在開頭的 `---` … `---` 區塊內。

    只靠 `re.MULTILINE` + `search()` 的話會咬到**全檔第一個行首 `title:`**；
    frontmatter 沒有 title 時，正文（尤其是示範 YAML 的程式碼區塊）那一行就會被
    當成 frontmatter 改掉。實測 2757 篇 post 目前 0 篇會踩到，這是廉價保險。
    """
    p = repo / "output/posts/2026-07-27_x.md"
    p.parent.mkdir(parents=True, exist_ok=True)
    original = f"---\ndate: 2026-07-27\nsource: rss\n---\n\n{body}"
    p.write_text(original, encoding="utf-8")

    res = repair_all(fetcher=_boom, arxiv_fetcher=_boom)
    assert res["simplified_converted"] == 0 and res["files_written"] == 0
    assert p.read_text(encoding="utf-8") == original


def test_post_without_frontmatter_is_skipped(repo):
    """整篇沒有 frontmatter → 一個字都不動。"""
    p = repo / "output/posts/2026-07-27_x.md"
    p.parent.mkdir(parents=True, exist_ok=True)
    original = f"title: {SIMPLIFIED}\n\n正文\n"
    p.write_text(original, encoding="utf-8")

    res = repair_all(fetcher=_boom, arxiv_fetcher=_boom)
    assert res["files_written"] == 0
    assert p.read_text(encoding="utf-8") == original


def test_post_body_untouched_when_title_repeats_in_body(repo):
    """title 值未加引號、且正文出現同一段文字時，只准改 frontmatter 那一行。

    這條專擋 `text.replace(舊title, 新title)` 的寫法。實測 output/posts 確實有
    未加引號的 frontmatter title（`title: 为啥 Codex 还不推出类似...`），全檔
    replace 會連正文一起改——而正文是 LLM 生成內容，一律不動。
    先前只有「title 加引號」的測試，引號讓 replace 剛好對不上正文，
    這個 mutation 因此 SURVIVED。
    """
    p = repo / "output/posts/2026-07-27_x.md"
    p.parent.mkdir(parents=True, exist_ok=True)
    original = (
        f"---\ntitle: {SIMPLIFIED}\ndate: 2026-07-27\n---\n\n"
        f"本文標題是「{SIMPLIFIED}」，正文不得被轉換。\n"
    )
    p.write_text(original, encoding="utf-8")

    res = repair_all(fetcher=_boom, arxiv_fetcher=_boom)
    assert res["simplified_converted"] == 1

    expected = (
        f"---\ntitle: {TRADITIONAL}\ndate: 2026-07-27\n---\n\n"
        f"本文標題是「{SIMPLIFIED}」，正文不得被轉換。\n"
    )
    assert p.read_text(encoding="utf-8") == expected


@pytest.mark.parametrize("text", TRAD_TRAPS)
def test_does_not_convert_already_traditional_text(repo, text):
    """守門一：欄位裡沒有任何「單字元層級就會被改寫」的字，就完全不碰。

    少了這道門，s2tw 的詞組規則會把已是繁體的欄位改壞（說明了→說明瞭、
    裡面包括→裡麵包括）。實測 data/raw 有 37 個純繁體欄位會這樣被誤改。
    注意這兩個樣本靠的是 `了` / `面` **單字元不會被改**（`s2tw('了')=='了'`）；
    `里` / `干` / `托` 單字元就會變，不屬於這一類——見
    `test_traditional_gan_tuo_are_not_simplified_evidence`。
    """
    from src.utils import to_traditional_shape_only

    # 前提：不擋的話這段真的會被改，否則本測試是空砲
    assert to_traditional_shape_only(text) != text

    _write(repo / "data/raw/2026-07-27.json", [
        {"source": "rss", "source_name": "量子位", "title": text,
         "url": "https://example.com/a", "abstract": text,
         "published_date": "2026-07-27"},
    ])
    res = repair_all(fetcher=_boom, arxiv_fetcher=_boom)
    assert res["simplified_converted"] == 0 and res["files_written"] == 0
    data = json.loads((repo / "data/raw/2026-07-27.json").read_text(encoding="utf-8"))
    assert data[0]["title"] == text and data[0]["abstract"] == text


@pytest.mark.parametrize("text,wrong", [
    # 全部取自 data/raw 的真實純繁體量子位摘要
    ("政策給的八字要求是「最小干預、利舊複用」", "幹預"),
    ("適用於可以並行處理、互不干擾的子任務", "幹擾"),
    ("支援自定義主題顏色、代理組/托盤圖示", "託盤"),
    ("上海安托資訊科技有限公司總經理於永峰", "安託"),
])
def test_traditional_gan_tuo_are_not_simplified_evidence(repo, text, wrong):
    """`干` / `托` 不得被當成「這個欄位含簡體」的證據。

    這兩個字在台灣繁體是天天出現的正常用字（干擾 / 干預、托盤 / 委托），但
    `s2tw('干')=='幹'`、`s2tw('托')=='託'`——把它們當簡體證據，等於讓一整個純繁體
    欄位過門、接著被詞組規則改壞。實測 data/raw 有 11 個純繁體欄位唯一觸發條件
    就是這兩個字，落地結果是 `干預`→`幹預`、`托盤`→`託盤`、`安托`→`安託`，全錯。
    """
    from src.utils import to_traditional_shape_only

    # 前提：這段真的是「不排除就會被改壞」，否則本測試是空砲
    assert wrong in to_traditional_shape_only(text)

    _write(repo / "data/raw/2026-07-27.json", [
        {"source": "rss", "source_name": "量子位", "title": text,
         "url": "https://example.com/a", "abstract": text,
         "published_date": "2026-07-27"},
    ])
    res = repair_all(fetcher=_boom, arxiv_fetcher=_boom)
    assert res["simplified_converted"] == 0 and res["files_written"] == 0
    data = json.loads((repo / "data/raw/2026-07-27.json").read_text(encoding="utf-8"))
    assert data[0]["title"] == text and wrong not in data[0]["title"]


@pytest.mark.parametrize("text,expected", [
    # 欄位裡還有別的簡體字撐著 gate → 照樣過門，`干扰` 一輪就到不動點
    ("适用于可以并行处理、互不干扰的子任务", "適用於可以並行處理、互不干擾的子任務"),
    # **完整重現生產環境的兩輪機制**（取自 data/raw/2026-04-05.json#12）：第一輪
    # `托盘`→`托盤`（對），但 `佣金` 的 `佣` 沒被轉掉、仍是 evidence，於是第二輪把
    # 已經是繁體的整段又餵一次 → `托盤`→`託盤`（錯），最後由 `_VARIANT_FIXES` 修回。
    # 舊版 fixture 是截斷過的（沒有 `佣`），一輪就到不動點，於是「托盘→托盤 轉得對」
    # 這句宣稱在生產環境被 6 個 `託盤` 打臉而測試照樣全綠。
    # 期望值是 s2tw（無詞庫）的結果：`支持` / `图标→圖標` 不會變成 `支援` / `圖示`。
    ("支持自定义主题颜色、代理组/托盘图标，佣金",
     "支持自定義主題顏色、代理組/托盤圖標，佣金"),
])
def test_gan_tuo_still_converted_when_field_is_really_simplified(repo, text, expected):
    """排除集只影響「要不要過門」，不影響過門後 OpenCC 怎麼轉。

    真簡體欄位裡有大量其他簡體字撐著 gate，`干扰`→`干擾`、`托盘`→`托盤`
    最終都拿得到正確結果——這正是排除 `干`/`托` 不會造成損失的原因。
    **注意第二筆的正確性來自 `_VARIANT_FIXES` 而非守門**（守門是欄位層級的准入
    測試，管不到 OpenCC 進去之後挑哪個分支）。
    """
    _write(repo / "data/raw/2026-07-27.json", [
        {"source": "chatpaper", "source_name": "C", "title": text,
         "url": "https://example.com/a", "abstract": "x",
         "published_date": "2026-07-27"},
    ])
    repair_all(fetcher=_boom, arxiv_fetcher=_boom)
    data = json.loads((repo / "data/raw/2026-07-27.json").read_text(encoding="utf-8"))
    assert data[0]["title"] == expected


def test_does_not_convert_fields_with_control_chars(repo):
    """守門二：含控制字元的欄位不碰——OpenCC 遇 NUL 會靜默截斷。

    實測 data/raw 有 17 個 abstract 是被當文字存進來的 PNG/JPEG 位元組，
    其中 14 個轉完長度掉到不足一成（1543 字 → 7 字）。
    """
    from src.utils import to_traditional_shape_only

    junk = "简体\x00测试内容" * 3
    assert len(to_traditional_shape_only(junk)) < len(junk)  # 前提：真的會被截斷

    _write(repo / "data/raw/2026-07-27.json", [
        {"source": "rss", "source_name": "R", "title": "T",
         "url": "https://example.com/a", "abstract": junk,
         "published_date": "2026-07-27"},
    ])
    res = repair_all(fetcher=_boom, arxiv_fetcher=_boom)
    assert res["simplified_converted"] == 0 and res["files_written"] == 0
    data = json.loads((repo / "data/raw/2026-07-27.json").read_text(encoding="utf-8"))
    assert data[0]["abstract"] == junk


def test_converges_context_sensitive_conversion(repo):
    """OpenCC 詞組規則吃上下文，第一輪轉完上下文就變了、第二輪還會再動一次。

    `糊里糊涂` →（1）`糊里糊塗` →（2）`糊裡糊塗`。排除 `干`/`托` 之後全庫仍有
    10 個欄位是這種兩輪才穩定的。轉一次就收工的話，下次跑 repair-content 又會
    再變一格——正是本專案一路在修的「每跑一次漂一格」。
    """
    from src.utils import to_traditional_shape_only

    # why 不用 `互不干扰`：`干` 已列入 `_NOT_SIMPLIFIED_EVIDENCE`，它的第一輪結果
    # 已經是不動點（那正是排除集要的效果），拿它測收斂等於空砲。
    unstable = "很大一部分公司，其实是糊里糊涂就成功了的"
    once = to_traditional_shape_only(unstable)
    # 前提：這段真的是「轉一次還不穩定」，否則本測試測不到收斂
    assert to_traditional_shape_only(once) != once

    _write(repo / "data/raw/2026-07-27.json", [
        {"source": "chatpaper", "source_name": "C", "title": "T",
         "url": "https://example.com/a", "abstract": unstable,
         "published_date": "2026-07-27"},
    ])
    repair_all(fetcher=_boom, arxiv_fetcher=_boom)
    stored = json.loads(
        (repo / "data/raw/2026-07-27.json").read_text(encoding="utf-8")
    )[0]["abstract"]
    assert stored == to_traditional_shape_only(once), "必須寫入不動點而非第一輪結果"

    # 再跑一次不得再動（真正要守的不變量）
    res = repair_all(fetcher=_boom, arxiv_fetcher=_boom)
    assert res["files_written"] == 0 and res["simplified_converted"] == 0


def test_non_converging_field_is_left_untouched(repo, monkeypatch):
    """收斂上限用完仍在跳動 → 整個欄位不動（不寫入一個注定會再漂的值）。"""
    import src.repair as repair_mod

    # 造一個永遠在兩個值之間跳動的轉換器
    flip = {"訪A": "訪B", "訪B": "訪A"}
    monkeypatch.setattr(repair_mod, "_convert_once", lambda t: flip.get(t, t))

    _write(repo / "data/raw/2026-07-27.json", [
        {"source": "chatpaper", "source_name": "C", "title": "訪A",
         "url": "https://example.com/a", "abstract": "x",
         "published_date": "2026-07-27"},
    ])
    res = repair_all(fetcher=_boom, arxiv_fetcher=_boom)
    assert res["simplified_converted"] == 0 and res["files_written"] == 0
    data = json.loads((repo / "data/raw/2026-07-27.json").read_text(encoding="utf-8"))
    assert data[0]["title"] == "訪A"


def test_conversion_is_idempotent_on_repaired_data(repo):
    """跑第二次不得再改動任何東西（否則就是 s2twp 那種漂移又回來了）。"""
    _write(repo / "data/raw/2026-07-27.json", [
        {"source": "chatpaper", "source_name": "C", "title": SIMPLIFIED,
         "url": "https://example.com/a", "abstract": QBIT_MEDIA + SIMPLIFIED,
         "published_date": "2026-07-27"},
    ])
    repair_all(fetcher=_boom, arxiv_fetcher=_boom)
    first = (repo / "data/raw/2026-07-27.json").read_text(encoding="utf-8")

    res = repair_all(fetcher=_boom, arxiv_fetcher=_boom)
    assert res["files_written"] == 0
    assert (repo / "data/raw/2026-07-27.json").read_text(encoding="utf-8") == first


# ══════════════════════════════════════════════════════════
# dry-run 涵蓋新增的四類修復
# ══════════════════════════════════════════════════════════

def test_dry_run_counts_new_repairs_without_writing(repo):
    """四個寫入點 × 新增修復類型都要被 dry-run 擋下，但候選數照算。"""
    url = "https://example.com/a"
    raw = repo / "data/raw/2026-07-27.json"
    _write(raw, [
        {"source": "rss", "source_name": "量子位", "title": SIMPLIFIED, "url": url,
         "abstract": QBIT_MEDIA, "published_date": "2026-07-27"},
    ])
    scored = repo / "data/scored/2026-07-27.json"
    _write(scored, [_scored_rec(url, title="舊標題", abstract=QBIT_MEDIA)])
    lists = repo / "output/lists/2026-07-27.json"
    _write(lists, {
        "date": "2026-07-27",
        "papers": {"hf": [], "others": [
            {"slug": "b", "title": SIMPLIFIED, "url": "https://example.com/b",
             "abstract": QBIT_MEDIA},
        ]},
        "github": [],
    })
    post = repo / "output/posts/2026-07-27_x.md"
    post.parent.mkdir(parents=True, exist_ok=True)
    post.write_text(f'---\ntitle: "{SIMPLIFIED}"\n---\n\nbody\n', encoding="utf-8")

    before = {p: p.read_text(encoding="utf-8") for p in (raw, scored, lists, post)}
    res = repair_all(dry_run=True, fetcher=_boom, arxiv_fetcher=_boom)

    assert res["files_written"] == 0
    assert res["simplified_converted"] == 3   # raw title + lists title + post title
    # scored 的 abstract 是被「已剝乾淨的 raw」覆寫掉的，不會再自己剝一次——
    # 這正是 raw 先修、scored 後抄的順序在 dry-run 下也成立的證據
    assert res["media_stripped"] == 2         # raw + lists 的 abstract
    assert res["scored_backfilled"] == 2      # title + abstract 對齊 raw
    for p, text in before.items():
        assert p.read_text(encoding="utf-8") == text, f"dry-run 不該寫 {p}"


def test_days_filter_skips_older_scored_files(repo):
    """--days 對 data/scored 一樣生效。"""
    _write(repo / "data/scored/2020-01-01.json", [
        _scored_rec("https://example.com/a", title="A&#8217;s"),
    ])
    res = repair_all(days=30, fetcher=_boom, arxiv_fetcher=_boom)
    assert res["entities_fixed"] == 0 and res["files_written"] == 0


# ══════════════════════════════════════════════════════════
# _VARIANT_FIXES：OpenCC 一簡對多繁挑錯分支的修正表
# ══════════════════════════════════════════════════════════
#
# 為什麼守門調整取代不了這張表：守門是**欄位層級的准入測試**，只能決定「這個欄位
# 要不要進轉換器」，管不到「進去之後 OpenCC 挑哪個繁體」。實測全語料 85601 個欄位，
# 加了 `_NOT_SIMPLIFIED_EVIDENCE` 之後仍有 39 處錯誤落地，分兩類：
#   ① 守門失效：欄位靠**別的**合法繁體字（云/里/台/范/卷/合）過門，純繁體被改壞
#   ② OpenCC 消歧錯誤：欄位確實整段簡體、該轉，但挑錯分支
# 繼續擴大排除集治不了②，且已實測不可行（`里` 會讓 22 個真簡體欄位整個不轉）。

# 每個條目一筆：(表的 key, 收斂後的錯誤文字, 修正後應得到的文字)。
# 文字全部取自真實語料的實際上下文——脈絡是從**全語料的全部出現位置**枚舉出來的，
# 不是抽樣，所以「加長 key」不會損失覆蓋率。
VARIANT_CASES = [
    # ① 守門失效：純繁體被詞組規則改壞
    ("過濾幹擾", "讓模型也能過濾幹擾、只留音色", "讓模型也能過濾干擾、只留音色"),
    ("受到幹擾", "駕駛員視線明顯受到幹擾的情況下", "駕駛員視線明顯受到干擾的情況下"),
    ("一次幹預", "研究者接著做了一次幹預實驗", "研究者接著做了一次干預實驗"),
    ("人工幹預", "或者停下來等人工幹預重新校準", "或者停下來等人工干預重新校準"),
    # 這筆是存檔裡既有的汙染（非本 pass 造成），但欄位會被轉換 ⇒ 順手修掉
    ("接管幹預", "一旦有人進入危險區域，再立即接管幹預。",
     "一旦有人進入危險區域，再立即接管干預。"),
    ("臺積電", "A0版晶片已從臺積電N4P工藝流片回片", "A0版晶片已從台積電N4P工藝流片回片"),
    ("穀底", "Meta員工士氣跌至20年穀底", "Meta員工士氣跌至20年谷底"),
    # 注意期望值連 `庫裡安`→`庫里安` 一起修——舊版把 `庫裡安` 當成正確輸出寫死在
    # 斷言裡，等於用測試把一個錯字釘成規格（round 4 才發現）
    ("託馬斯", "Google Cloud 的 CEO 託馬斯·庫裡安", "Google Cloud 的 CEO 托馬斯·庫里安"),
    ("藍色遊標", "Lion X基金、藍色遊標、CloudAlpha", "Lion X基金、藍色游標、CloudAlpha"),
    ("/遊資", "（+政策分析師/遊資追蹤/解禁監控）", "（+政策分析師/游資追蹤/解禁監控）"),
    # ② OpenCC 消歧錯誤：整段簡體該轉，但挑錯分支
    ("/託盤", "代理組/託盤圖標以及 CSS Injection", "代理組/托盤圖標以及 CSS Injection"),
    ("金屬託盤", "抱著一塊大金屬託盤走進來", "抱著一塊大金屬托盤走進來"),
    ("載物託盤", "UV清潔裝置、載物託盤，軟體層", "UV清潔裝置、載物托盤，軟體層"),
    ("不復雜", "後端邏輯為主、界面不復雜的產品", "後端邏輯為主、界面不複雜的產品"),
    ("更復雜", "可以完成更長、更復雜的任務", "可以完成更長、更複雜的任務"),
    ("執行復雜", "理解任務和執行復雜指令的能力", "理解任務和執行複雜指令的能力"),
    ("證明瞭太多", "走到今天這一步已經證明瞭太多東西", "走到今天這一步已經證明了太多東西"),
    ("說明瞭一件", "場景很輕鬆，但也說明瞭一件事", "場景很輕鬆，但也說明了一件事"),
    ("目睹瞭如今", "他曾在第一線親眼目睹瞭如今軟件項目", "他曾在第一線親眼目睹了如今軟件項目"),
    ("一齣來", "這個建議一齣來，連人類化學家都震驚了", "這個建議一出來，連人類化學家都震驚了"),
    ("搞定併發布", "現在創始人自己就能搞定併發布。", "現在創始人自己就能搞定並發布。"),
    ("乾的就是", "大語言模型乾的就是這件事", "大語言模型幹的就是這件事"),
    ("乾的是", "Applied AI乾的是更“下沉”的活", "Applied AI幹的是更“下沉”的活"),
    ("該乾的活", "這正是一個優秀文案該乾的活", "這正是一個優秀文案該幹的活"),
    ("它乾的活", "半年前，它乾的活兒還是站在自攻螺母工站", "半年前，它幹的活兒還是站在自攻螺母工站"),
    ("不是隻寫", "想驗證能參與整本小說生產，而不是隻寫單段文案",
     "想驗證能參與整本小說生產，而不是只寫單段文案"),
    ("不是隻面", "它不是隻面向閒聊的聊天框", "它不是只面向閒聊的聊天框"),
    ("不是隻在", "也不是隻在本地終端裡運行的 CLI 工具",
     "也不是只在本地終端裡運行的 CLI 工具"),
    ("不是隻返", "它不是隻返回一段回答", "它不是只返回一段回答"),
    ("這隻會營造", "沒定義清楚什麼，這隻會營造出一種虛假繁榮",
     "沒定義清楚什麼，這只會營造出一種虛假繁榮"),
    # ③ fix round 4：第一順位挑錯（round 3 的掃描法結構上看不到）
    ("合並請求", "自動化測試、提交 PR（代碼提交合並請求）。",
     "自動化測試、提交 PR（代碼提交合併請求）。"),
    ("在籤什麼", "那時候我完全不知道自己在籤什麼。", "那時候我完全不知道自己在簽什麼。"),
    ("一起籤的", "旁邊一起籤的還有 Andrej", "旁邊一起簽的還有 Andrej"),
    ("·庫裡安", "CEO 托馬斯·庫裡安（Thomas Kurian）",
     "CEO 托馬斯·庫里安（Thomas Kurian）"),
    # ④ fix round 3 用 target-side 掃描新抓到的（前兩輪的黑名單看不到）
    ("曆史", "宣佈了這家公司 27 年曆史上最激進的一次架構轉型",
     "宣佈了這家公司 27 年歷史上最激進的一次架構轉型"),
    ("總檯", "魔法原子作為總檯《2026年春節聯歡晚會》",
     "魔法原子作為總臺《2026年春節聯歡晚會》"),
    ("聯閤", "剛剛，阿里達摩院聯閤中國人民大學", "剛剛，阿里達摩院聯合中國人民大學"),
    ("係統化", "幫助你係統化學習如何使用多智能體", "幫助你系統化學習如何使用多智能體"),
    ("剋制", "這可能是產品上有意為之的剋制", "這可能是產品上有意為之的克制"),
    ("死衚衕", "這種循環很容易陷入“死衚衕”", "這種循環很容易陷入“死胡同”"),
    ("揹負", "這對於揹負著繁重生活壓力的人", "這對於背負著繁重生活壓力的人"),
    # ⑤ 2026-07-31 巡邏候選，經「≥2 篇脈絡 + 教育部辭典核對 + 反例掃描」三道閘門
    # 發（發生）被挑成髮（頭髮）：OpenCC 把「结发」當成「結髮」詞組。
    # 帶左錨定，否則會弄壞「頭髮生長」
    ("總結髮生", "定期檢查網站和儀表盤，總結髮生了什麼變化。",
     "定期檢查網站和儀表盤，總結發生了什麼變化。"),
    ("總髮生", "為什麼最有價值的AI討論總髮生在知乎？",
     "為什麼最有價值的AI討論總發生在知乎？"),
    # 注（投資加碼，同賭注）被挑成註（註解）。全語料 17 筆脈絡皆為投資，
    # 但「加註說明」是合法用法，故一律帶左錨定
    ("共同加註", "產業與全球資本共同加註，愛詩科技完成29.8億元C輪融資",
     "產業與全球資本共同加注，愛詩科技完成29.8億元C輪融資"),
    ("持續加註", "老股東普華資本、誠通科創基金持續加註，藍湖資本",
     "老股東普華資本、誠通科創基金持續加注，藍湖資本"),
    ("資本加註", "獲得資本加註，身價暴漲，甚至晉升百億估值",
     "獲得資本加注，身價暴漲，甚至晉升百億估值"),
    ("輪加註", "悉數在列，小米戰投更是連續三輪加註。",
     "悉數在列，小米戰投更是連續三輪加注。"),
    ("重磅加註", "本輪領投方的重磅加註，看重的不僅僅是普通財務回報",
     "本輪領投方的重磅加注，看重的不僅僅是普通財務回報"),
    ("超額加註", "尚頎資本、蔚來資本等都在本輪超額加註。",
     "尚頎資本、蔚來資本等都在本輪超額加注。"),
]


@pytest.mark.parametrize("key,wrong,right", VARIANT_CASES)
def test_variant_fix_entry(key, wrong, right):
    """每一條修正表條目都要有自己的測試（拿掉該條就會 FAIL）。"""
    from src.utils import _apply_variant_fixes

    assert _apply_variant_fixes(wrong) == right


def test_every_variant_fix_entry_has_a_test():
    """修正表與測試案例必須逐條對齊——新增條目卻沒補測試會在這裡失敗。

    這條擋的是「表越加越長、但只有前幾條真的被驗過」。

    表已於 2026-07-31 搬到 `src/utils.py`（Layer A 與 repair 共用），這裡跟著改
    import 來源；對齊關係本身不變。
    """
    from src.utils import _VARIANT_FIXES

    tested = {c[0] for c in VARIANT_CASES}
    assert tested == set(_VARIANT_FIXES), (
        "VARIANT_CASES 與 _VARIANT_FIXES 不一致：\n"
        f"  表有測試沒有：{set(_VARIANT_FIXES) - tested}\n"
        f"  測試有表沒有：{tested - set(_VARIANT_FIXES)}"
    )


@pytest.mark.parametrize("text", [
    # ── 這些是**正確**的台灣繁體，刻意不收進表裡——收了反而是製造錯誤 ──
    "讓使用者快速瞭解專案結構",       # 瞭解
    "資料一目瞭然",                   # 教育部標準寫法
    "其實是糊裡糊塗就成功了的",
    "產率超過30%的反應佔比",
    "生成模型捲到飛起",
    "跨平臺兼容",
    "多個 Agent 同時幹活的時候",     # 幹活 = 做事，正確
    "把果醬抹到麵包上",
    "奇蹟般地活了下來",
    "沒問題，老闆",
    "英語肌肉記憶鍛鍊軟件",
    "接入資料庫、日曆、程式碼倉庫",   # 日曆 正確；`曆史→歷史` 不會誤傷
    "難度係數拉滿",                   # 係數 正確；`係統化→系統化` 不會誤傷
    # ── 修正表**不得**誤傷的字串：每條都對應表裡一個刻意加長的 key ──
    "工程師正在修復雜湊表的碰撞問題",   # 擋 復雜（雜湊=hash，台灣術語）
    "系統會自動恢復雜亂的狀態",         # 擋 復雜
    "這份文件說明瞭解決方案的取捨",     # 擋 說明瞭（瞭解 是正確用法）
    "實驗證明瞭解這個機制很重要",       # 擋 證明瞭
    "這張表是關係統計資料的來源",       # 擋 係統化
    "他是團隊骨幹擾動了整個進度",       # 擋 幹擾（語料裡確實有「骨幹」）
    "公司骨幹預備隊已經就位",           # 擋 幹預
    "把衣服曬乾的活兒交給機器",         # 擋 乾的活
    "委託盤與信託盤是兩回事",           # 擋 託盤
    "旅遊標籤與旅遊資訊分開存放",       # 擋 遊標 / 遊資
    "支援企業高併發、7*24 技術支持",   # 擋 併發布
    "一隻在樹上的鳥",                   # 擋 隻在
    "這隻會飛的鳥很罕見",               # 擋 這隻會（收窄成 這隻會營造 之後才擋得住）
    "他是這隻鳥的主人",
    "標籤生成與標籤嵌入",               # 擋 在籤什麼 / 一起籤的（籤 在標籤裡是對的）
    "這裡安裝好之後就能用",             # 擋 庫裡安（`裡安` 在一般句子裡是對的）
    "資料庫裡安放著索引",               # 同上：只有音譯名 `庫裡安` 才錯
    "合並發症一起處理",                 # 擋 合並請求 的過度一般化
])
def test_variant_fixes_leave_correct_text_alone(text):
    """修正表對正確文字必須是 no-op（逐字元不變）。

    後半段每一條都是「如果某個 key 沒有帶脈絡就會被改壞」的實例——
    這組測試就是那些 key 為什麼要加長的理由，也是 mutation 殺得掉它們的原因。
    """
    from src.repair import _apply_variant_fixes

    assert _apply_variant_fixes(text) == text


def test_variant_fixes_only_applied_to_converted_fields(repo):
    """守門擋下的欄位連修正表都不套——「沒過門就原封不動」是不變量。

    純繁體欄位裡若剛好有 `復雜` 這種字，那是既有資料的問題，不歸簡→繁 pass 管；
    在這裡順手改會讓「這個 pass 只碰它轉過的欄位」這條保證破功。
    """
    # fixture 必須含**現行**的 key：round 3 把 key 從裸的 `復雜` 收窄成
    # `不復雜`/`更復雜`/`執行復雜` 之後，舊 fixture（只有裸 `復雜`）就再也命中不了，
    # 這條 guard 於是靜默失效——實測「把 _apply_variant_fixes 搬進收斂迴圈內」
    # 的 mutation 會 SURVIVED，而它對真實資料有 26 個欄位輸出不同（非等價突變）。
    #
    # fixture 還必須是**只在 `_VARIANT_FIXES` 裡、不在 `_TYPO_FIXES` 裡**的 key：
    # 後者是無守門 pass，會把 `更復雜`（舊 fixture）修掉而讓本測試測不到守門。
    # `人工幹預` 在現行語料 0 次出現，故沒有收進 `_TYPO_FIXES`，正好當守門的探針。
    text = "這段是純繁體，裡面提到人工幹預四個字"  # 無任何簡體字 → 不過門
    from src.utils import to_traditional_shape_only

    assert to_traditional_shape_only(text) == text  # 前提：OpenCC 本身也不動它

    _write(repo / "data/raw/2026-07-27.json", [
        {"source": "rss", "source_name": "R", "title": text,
         "url": "https://example.com/a", "abstract": text,
         "published_date": "2026-07-27"},
    ])
    res = repair_all(fetcher=_boom, arxiv_fetcher=_boom)
    assert res["files_written"] == 0
    data = json.loads((repo / "data/raw/2026-07-27.json").read_text(encoding="utf-8"))
    assert data[0]["title"] == text


def test_variant_fixes_run_after_convergence_end_to_end(repo):
    """端到端：兩輪收斂造出 `託盤`，修正表在迴圈後把它修回 `托盤`。

    這是生產環境真實機制的最小重現（data/raw/2026-04-05.json#12）：
    第一輪 `托盘`→`托盤`（對），但 `佣金` 的 `佣` 仍是 evidence，第二輪把已經
    是繁體的整段再餵一次 → `託盤`（錯），最後由修正表導回。
    """
    import src.repair as repair_mod

    dirty = "代理组/托盘图标，佣金"
    # 前提：收斂後（套表前）確實是錯的，否則本測試測不到修正表
    mid = dirty
    for _ in range(5):
        nxt = repair_mod._convert_once(mid)
        if nxt == mid:
            break
        mid = nxt
    assert "託盤" in mid, "前提不成立：收斂後應該出現錯誤的 託盤"

    _write(repo / "data/raw/2026-07-27.json", [
        {"source": "chatpaper", "source_name": "C", "title": dirty,
         "url": "https://example.com/a", "abstract": "x",
         "published_date": "2026-07-27"},
    ])
    repair_all(fetcher=_boom, arxiv_fetcher=_boom)
    data = json.loads((repo / "data/raw/2026-07-27.json").read_text(encoding="utf-8"))
    assert data[0]["title"] == "代理組/托盤圖標，佣金"

    # 且仍然冪等
    res = repair_all(fetcher=_boom, arxiv_fetcher=_boom)
    assert res["files_written"] == 0


# ══════════════════════════════════════════════════════════
# _TYPO_FIXES：無守門的既有錯字修正表
# ══════════════════════════════════════════════════════════
#
# 與 `_VARIANT_FIXES` 的差別（合併兩張表會同時弄壞兩邊，理由見 repair.py 的表頭）：
#   - `_VARIANT_FIXES` 只套在**本 pass 真的轉換過**的欄位（約 800 個），修的是
#     OpenCC 一簡對多繁挑錯分支，也就是**本 pass 自己造成**的錯。
#   - `_TYPO_FIXES` 對全部 88361 個欄位無條件套用，修的是存檔裡**既有**的錯字。
#     這些錯字絕大多數落在純繁體欄位——守門永遠擋著，跑不跑 repair 都一樣。
#
# 因為會碰到從沒被動過的正常文字，安全門檻高得多：每一條都對全語料掃過、
# 逐處人工判讀（114 處改動 / 87 個相異脈絡，0 誤傷）。

# (表的 key, 真實語料脈絡, 修正後應得到的文字)
TYPO_CASES = [
    # ── 干 / 幹 ──
    ("幹預路徑", "而是能沿因果鏈定位病因，並推演多條幹預路徑", "而是能沿因果鏈定位病因，並推演多條干預路徑"),
    ("幹預效果", "事前不可驗證：幹預效果無法提前推演", "事前不可驗證：干預效果無法提前推演"),
    ("幹預後果", "包含因果機制、時序演化與幹預後果的世界圖景", "包含因果機制、時序演化與干預後果的世界圖景"),
    ("是幹預，", "第二級是幹預，回答“主動改變一個變數後會發生什麼”", "第二級是干預，回答“主動改變一個變數後會發生什麼”"),
    ("主動幹預", "限制下水人數等主動幹預會產生什麼結果", "限制下水人數等主動干預會產生什麼結果"),
    ("匹配幹擾", "有效降低透明材質帶來的匹配幹擾", "有效降低透明材質帶來的匹配干擾"),
    ("抗幹擾", "保持了與Picking同等級的閉環抗幹擾能力", "保持了與Picking同等級的閉環抗干擾能力"),
    ("伸手幹擾", "我問現場工作人員：能不能伸手幹擾一下？", "我問現場工作人員：能不能伸手干擾一下？"),
    ("多人幹擾", "第二種是多人幹擾。周圍幾個人同時移動", "第二種是多人干擾。周圍幾個人同時移動"),
    # ── 復 / 複 ──
    ("更復雜", "它面對的還不是普通軟體工程，而是更復雜的物理AI", "它面對的還不是普通軟體工程，而是更複雜的物理AI"),
    ("不復雜", "甚至Skill部署也不復雜，點一下「使用」就能行", "甚至Skill部署也不複雜，點一下「使用」就能行"),
    ("執行復雜", "學會動作間的時序銜接，執行復雜裝配這類長序列動作時", "學會動作間的時序銜接，執行複雜裝配這類長序列動作時"),
    ("進行復雜", "同樣是進行復雜連續的家務實操", "同樣是進行複雜連續的家務實操"),
    ("展開復雜", "需要針對不同的p分別展開復雜分析", "需要針對不同的p分別展開複雜分析"),
    # ── 併 / 並 ──
    ("併發布", "儀電智算牽頭成立“智算系統架構聯盟”併發布《超節點系統架構規範》",
     "儀電智算牽頭成立“智算系統架構聯盟”並發布《超節點系統架構規範》"),
    ("併發起搭子", "百度搭子此次升級個人版、釋出企業版併發起搭子聯盟", "百度搭子此次升級個人版、釋出企業版並發起搭子聯盟"),
    ("併發揮", "字底盤與高通智慧體AI執行環境結合，併發揮各家生態企業", "字底盤與高通智慧體AI執行環境結合，並發揮各家生態企業"),
    ("，併產生", "生命科學領域，世界模型能否真正落地，併產生實質價值？", "生命科學領域，世界模型能否真正落地，並產生實質價值？"),
    ("併入圍", "“垂類大模型”雙核心板塊收錄，併入圍中國AI商業落地應用價值Top5",
     "“垂類大模型”雙核心板塊收錄，並入圍中國AI商業落地應用價值Top5"),
    ("精簡併穩定", "Boz的應對策略是精簡併穩定組織架構", "Boz的應對策略是精簡並穩定組織架構"),
    ("，併為", "將數學方法嚴格應用於物理學，併為物理學建立數學公理體系",
     "將數學方法嚴格應用於物理學，並為物理學建立數學公理體系"),
    ("，併成為", "這一概念正逐步獲得行業驗證，併成為衡量智慧體應用深度與價值產出的重要指標",
     "這一概念正逐步獲得行業驗證，並成為衡量智慧體應用深度與價值產出的重要指標"),
    ("，併成立", "開潤股份與小米達成合作，併成立了自有箱包品牌「90分」",
     "開潤股份與小米達成合作，並成立了自有箱包品牌「90分」"),
    # ── 係 / 系 ──
    ("係統化", "體與大模型股票分析學習平臺。幫助你係統化學習如何使用多智慧體交易框架",
     "體與大模型股票分析學習平臺。幫助你系統化學習如何使用多智慧體交易框架"),
    ("係統論證", "VisualSkill²等近期學術工作已係統論證了這一方向", "VisualSkill²等近期學術工作已系統論證了這一方向"),
    ("係統電氣", "工作超過8年，曾參與iPhone相關係統電氣工程專案", "工作超過8年，曾參與iPhone相關系統電氣工程專案"),
    # ── 瞭 / 了 ──
    ("指明瞭靶子", "還是靠表面模式蒙對了？這為後續的訓練指明瞭靶子", "還是靠表面模式蒙對了？這為後續的訓練指明了靶子"),
    ("指明瞭方向", "也為產業智慧化、高階化發展指明瞭方向", "也為產業智慧化、高階化發展指明了方向"),
    ("鮮明瞭：", "它過去留給大家的印象太鮮明瞭：便宜", "它過去留給大家的印象太鮮明了：便宜"),
    ("證明瞭向", "Zeilinger院士特別指出:“團隊證明瞭向變分量子電路中注入",
     "Zeilinger院士特別指出:“團隊證明了向變分量子電路中注入"),
    ("證明瞭三維", "用127頁論文成功證明瞭三維情況下（n=3）的掛谷集猜想",
     "用127頁論文成功證明了三維情況下（n=3）的掛谷集猜想"),
    # ── 隻 / 只 ──
    ("大多隻是", "但是，這些資訊大多隻是以日誌形式被儲存下來", "但是，這些資訊大多只是以日誌形式被儲存下來"),
    ("不是隻會", "企業需要的並不是隻會依照現有資料來生成內容的AI工具",
     "企業需要的並不是只會依照現有資料來生成內容的AI工具"),
    ("不是隻做", "更具體地說，它不是隻做一個觸覺模型或硬體", "更具體地說，它不是只做一個觸覺模型或硬體"),
    ("不是隻問", "會觸發“多模型融合”機制。它不是隻問一個模型", "會觸發“多模型融合”機制。它不是只問一個模型"),
    ("不是隻能", "它證明擴散模型並不是隻能停留在小參數實驗階段", "它證明擴散模型並不是只能停留在小參數實驗階段"),
    ("而是隻持有", "GPU不再完整持有所有expert，而是隻持有其中一部分引數",
     "GPU不再完整持有所有expert，而是只持有其中一部分引數"),
    ("而是隻保留", "不再死記硬背前面已經抄寫過的內容，而是隻保留當前工作需要的資訊",
     "不再死記硬背前面已經抄寫過的內容，而是只保留當前工作需要的資訊"),
    ("而是隻執行", "模型不會一次性執行完整動作序列，而是隻執行第一段動作",
     "模型不會一次性執行完整動作序列，而是只執行第一段動作"),
    ("是隻描述", "它的核心思路是隻描述化學過程，把幾何計算交給程式完成",
     "它的核心思路是只描述化學過程，把幾何計算交給程式完成"),
    ("是隻更新", "一是使用stop-gradient；二是隻更新少量引數", "一是使用stop-gradient；二是只更新少量引數"),
    ("沒有隻盯", "沒有圍著單一工具橫向擴功能，也沒有隻盯著一個爆款產品吃紅利",
     "沒有圍著單一工具橫向擴功能，也沒有只盯著一個爆款產品吃紅利"),
    ("許多隻有", "許多隻有在特定擾動條件下才顯現的關鍵生物學規律",
     "許多只有在特定擾動條件下才顯現的關鍵生物學規律"),
    ("很多隻展示", "和很多隻展示單點能力的機器人不同，D7被放在真實場景",
     "和很多只展示單點能力的機器人不同，D7被放在真實場景"),
    # ── 其他歧義組的低頻錯字 ──
    ("曆史", "既不用反覆重算曆史，也不會因為影片變長而失憶", "既不用反覆重算歷史，也不會因為影片變長而失憶"),
    ("衚衕", "「PHEW」出現在它終於繞過一個死衚衕的時候", "「PHEW」出現在它終於繞過一個死胡同的時候"),
    ("穀底", "技術推進比預期慢、員工士氣跌到20年穀底", "技術推進比預期慢、員工士氣跌到20年谷底"),
    ("穀歌", "Character.AI，2024年穀歌花了27億美元把他買了回去",
     "Character.AI，2024年谷歌花了27億美元把他買了回去"),
    ("剋制", "其實從這輪融資額看，對比同行也比較剋制", "其實從這輪融資額看，對比同行也比較克制"),
    ("聯閤", "打造多模態智慧體vivago R1，聯閤中科類腦等機構組建",
     "打造多模態智慧體vivago R1，聯合中科類腦等機構組建"),
    ("詆譭", "公示了一批惡意造謠、抹黑詆譭品牌的自媒體侵權判決", "公示了一批惡意造謠、抹黑詆毀品牌的自媒體侵權判決"),
    ("孃胎", "VLA模型不僅要“眼光放長遠”，還得從孃胎裡就是具身的！",
     "VLA模型不僅要“眼光放長遠”，還得從娘胎裡就是具身的！"),
    ("一齣，", "營收指引高達約500億美元。 財報一齣，市場瞬間被點燃",
     "營收指引高達約500億美元。 財報一出，市場瞬間被點燃"),
    ("一齣來", "恰恰是追不動了。 訊息一齣來，X上幾乎刷成了送別現場",
     "恰恰是追不動了。 訊息一出來，X上幾乎刷成了送別現場"),
    ("一箇", "全球最大的AI開源社群抱抱臉突然給一箇中國模型開了“專屬VIP通道”",
     "全球最大的AI開源社群抱抱臉突然給一個中國模型開了“專屬VIP通道”"),
    ("几乎", "傳聞一度甚囂塵上，極石几乎算得上在夾縫中生存", "傳聞一度甚囂塵上，極石幾乎算得上在夾縫中生存"),
    ("7天后", "再逐段複製貼上。 大約7天后，她做出了一個完整的iOS應用",
     "再逐段複製貼上。 大約7天後，她做出了一個完整的iOS應用"),
    ("傢俬人", "拉上一批老同事、老朋友，做了一傢俬人健康機器人公司",
     "拉上一批老同事、老朋友，做了一家私人健康機器人公司"),
    ("人傢俬聊", "來訓練AI。 結果把人傢俬聊記錄、績效資料弄得滿公司亂飛",
     "來訓練AI。 結果把人家私聊記錄、績效資料弄得滿公司亂飛"),
    ("檔案類與相關字型", "安裝 texlive、ElegantBook 檔案類與相關字型後，執行 cd book",
     "安裝 texlive、ElegantBook 文件類與相關字型後，執行 cd book"),
    # 2026-07-31 巡邏候選的無守門副本（脈絡與 VARIANT_CASES 同源，皆取自真實語料）
    ("總結髮生", "定期檢查網站和儀表盤，總結髮生了什麼變化。",
     "定期檢查網站和儀表盤，總結發生了什麼變化。"),
    ("總髮生", "為什麼最有價值的AI討論總髮生在知乎？",
     "為什麼最有價值的AI討論總發生在知乎？"),
    ("共同加註", "產業與全球資本共同加註，愛詩科技完成29.8億元C輪融資",
     "產業與全球資本共同加注，愛詩科技完成29.8億元C輪融資"),
    ("持續加註", "老股東普華資本、誠通科創基金持續加註，藍湖資本",
     "老股東普華資本、誠通科創基金持續加注，藍湖資本"),
    ("資本加註", "獲得資本加註，身價暴漲，甚至晉升百億估值",
     "獲得資本加注，身價暴漲，甚至晉升百億估值"),
    ("輪加註", "悉數在列，小米戰投更是連續三輪加註。",
     "悉數在列，小米戰投更是連續三輪加注。"),
    ("重磅加註", "本輪領投方的重磅加註，看重的不僅僅是普通財務回報",
     "本輪領投方的重磅加注，看重的不僅僅是普通財務回報"),
    ("超額加註", "尚頎資本、蔚來資本等都在本輪超額加註。",
     "尚頎資本、蔚來資本等都在本輪超額加注。"),
]


@pytest.mark.parametrize("key,wrong,right", TYPO_CASES)
def test_typo_fix_entry(key, wrong, right):
    """每一條錯字修正表條目都要有自己的測試（拿掉該條就會 FAIL）。"""
    from src.repair import _apply_typo_fixes

    assert _apply_typo_fixes(wrong) == right


def test_every_typo_fix_entry_has_a_test():
    """錯字表與測試案例必須逐條對齊——新增條目卻沒補測試會在這裡失敗。"""
    from src.repair import _TYPO_FIXES

    tested = {c[0] for c in TYPO_CASES}
    assert tested == set(_TYPO_FIXES), (
        "TYPO_CASES 與 _TYPO_FIXES 不一致：\n"
        f"  表有測試沒有：{set(_TYPO_FIXES) - tested}\n"
        f"  測試有表沒有：{tested - set(_TYPO_FIXES)}"
    )


@pytest.mark.parametrize("text", [
    # ── 每一條都是「某個 key 若不帶脈絡就會被改壞」的實例 ──
    "他是團隊骨幹擾動了整個進度",         # 擋 幹擾（骨幹 backbone + 擾動 perturbation）
    "公司骨幹預備隊已經就位",             # 擋 幹預
    "多個 Agent 同時幹活的時候",         # 幹活／幹嘛／軀幹／幹線 都是正確用法
    "把上肢、軀幹和頭部也基本固定住",
    "廣袤的公路幹線上，這件事才剛開始",
    "工程師正在修復雜湊表的碰撞問題",     # 擋 復雜（雜湊 = hash，台灣術語）
    "系統會自動恢復雜亂的狀態",           # 擋 復雜
    "把兩個分支合併成一個版本",           # 擋 ，併成為／，併成立
    "支援企業高併發、7*24 技術支持",     # 擋 併發布／併發揮
    # fix round 1：這兩組證明「右錨定到後面那個動詞」對 併 不是萬用解——
    # 碰撞對象是 `合併`/`兼併`（前綴）或 concurrency 的 `併發`＋`起X` 時，
    # 往右延長並不消歧，必須改成逗號錨定或把產品名收進 key。
    "兩家公司合併產生的綜效相當可觀",      # 擋 併產生（碰撞對象是 合併，不是 併發）
    "業務兼併產生新的營運模式",            # 擋 併產生
    "系統的併發起始時間必須對齊",          # 擋 併發起（起 會接在 concurrency 的 併發 後）
    "併發起點的選擇影響吞吐量",            # 擋 併發起
    "整個團隊併入 Meta 的超級智慧實驗室",  # 併入 是正確用法（擋 併入圍 的過度一般化）
    "施工週期和併網審批上都要時間",        # 併網 正確
    "在招崗位一併取消",                    # 一併 正確
    "這張表是關係統計資料的來源",          # 擋 係統化
    "難度係數拉滿了",                      # 係數 正確
    "這份文件說明瞭解決方案的取捨",        # 擋 指明瞭／證明瞭（瞭解 正確）
    "誰高誰低一目瞭然",                    # 一目瞭然 正確
    "讓使用者快速瞭解專案結構",
    "一隻會飛的鳥很罕見",                  # 擋 不是隻會
    "一隻有毒的蜘蛛爬過桌面",              # 擋 許多隻有
    "兩隻貓裡，一隻是黑的",                # 擋 大多隻是
    "他不是隻身一人前往",                  # 擋「而是隻/不是隻」若不帶動詞就會誤傷
    "展示時只用一隻手，實際作業時用到了兩隻手",
    "多隻“靈貓”協同響應",
    "接入資料庫、日曆、程式碼倉庫",        # 擋 曆史（日曆 正確）
    "農曆新年前後的曆法換算",
    "上個月的天后宮參拜人數",              # 擋 7天后（天后 正確）
    "第 17 天后勤補給才到",                # 同上：只有 `7天后` 這個實例被收
    "客廳的傢俱和傢伙什都搬走了",          # 擋 傢俬人（傢俱／傢伙 正確）
    "好傢伙，果然都是老朋友",
    "新動作，箇中意味值得玩味",            # 擋 一箇（箇中 正確）
    "這個檔案類型不支援上傳",              # 擋 檔案類（檔案類型 正確）
    "資料庫檔案類別繁多",
    "研究團隊要演出一齣好戲",              # 擋 一齣（戲曲量詞 正確）
    "五穀雜糧與稻穀收成",                  # 擋 穀底／穀歌
    "相生相剋的五行理論",                  # 擋 剋制
    "案几上放著一本書",                    # 擋 几乎
])
def test_typo_fixes_leave_correct_text_alone(text):
    """錯字表對正確文字必須是 no-op（逐字元不變）。

    這組就是每個 key 為什麼要帶脈絡的理由，也是 mutation 殺得掉那些脈絡的原因。
    """
    from src.repair import _apply_typo_fixes

    assert _apply_typo_fixes(text) == text


def test_typo_fixes_are_idempotent_by_construction():
    """表的 value 不得含任何 key ⇒ 套第二次必為 no-op。

    這條是冪等性的**建構層保證**，比端到端跑兩次更強：新增條目時若不小心造出
    A→B、B→C 的鏈（或 A→B、B→A 的環），這裡立刻失敗。
    """
    from src.repair import _TYPO_FIXES, _apply_typo_fixes

    for wrong, right in _TYPO_FIXES.items():
        assert _apply_typo_fixes(right) == right, f"{wrong!r}→{right!r} 的輸出還會再被改"


def test_typo_fixes_apply_without_the_simplified_gate(repo):
    """核心不變量：純繁體欄位（守門必擋）裡的既有錯字也要被修掉。

    這正是本表存在的唯一理由——`_VARIANT_FIXES` 只碰轉換過的欄位，對這種欄位
    永遠無效。把 `_apply_typo_fixes` 移到守門後面（或併進 `_VARIANT_FIXES`）
    就會在這裡 FAIL。
    """
    from src.utils import to_traditional_shape_only

    text = "這段是純繁體，只有一個更復雜的錯字"
    # 前提：這個欄位確實不含簡體字、守門一定擋下（否則測不到「無守門」）
    assert to_traditional_shape_only(text) == text

    _write(repo / "data/raw/2026-07-27.json", [
        {"source": "rss", "source_name": "R", "title": text,
         "url": "https://example.com/a", "abstract": "x",
         "published_date": "2026-07-27"},
    ])
    res = repair_all(fetcher=_boom, arxiv_fetcher=_boom)
    assert res["simplified_converted"] == 0, "前提：這個欄位不該進轉換器"
    assert res["typos_fixed"] == 1
    data = json.loads((repo / "data/raw/2026-07-27.json").read_text(encoding="utf-8"))
    assert data[0]["title"] == "這段是純繁體，只有一個更複雜的錯字"

    # 再跑一次不得再動
    again = repair_all(fetcher=_boom, arxiv_fetcher=_boom)
    assert again["files_written"] == 0 and again["typos_fixed"] == 0


def test_typo_fixes_reach_all_four_writers(repo):
    """raw / scored / lists / post frontmatter title 四個寫入點都要套到。"""
    url = "https://example.com/a"
    text = "報告指出這比想像中更復雜"
    fixed = "報告指出這比想像中更複雜"

    _write(repo / "data/raw/2026-07-27.json", [
        {"source": "rss", "source_name": "R", "title": text, "url": url,
         "abstract": "x", "published_date": "2026-07-27"},
    ])
    _write(repo / "data/scored/2026-07-27.json",
           [_scored_rec("https://example.com/b", title=text, abstract=text)])
    _write(repo / "output/lists/2026-07-27.json", {
        "date": "2026-07-27", "github": [],
        "papers": {"hf": [], "others": [
            {"slug": "c", "title": text, "url": "https://example.com/c", "abstract": "y"},
        ]},
    })
    post = repo / "output/posts/2026-07-27_x.md"
    post.parent.mkdir(parents=True, exist_ok=True)
    post.write_text(f'---\ntitle: "{text}"\n---\n\n{text}\n', encoding="utf-8")

    repair_all(fetcher=_boom, arxiv_fetcher=_boom)

    assert json.loads((repo / "data/raw/2026-07-27.json").read_text(encoding="utf-8"))[0]["title"] == fixed
    scored = json.loads((repo / "data/scored/2026-07-27.json").read_text(encoding="utf-8"))[0]["item"]
    assert scored["title"] == fixed and scored["abstract"] == fixed
    lists = json.loads((repo / "output/lists/2026-07-27.json").read_text(encoding="utf-8"))
    assert lists["papers"]["others"][0]["title"] == fixed
    body = post.read_text(encoding="utf-8")
    assert f'title: "{fixed}"' in body
    assert f"\n\n{text}\n" in body, "post body 不得被動到"


def test_typo_fixes_counted_but_not_written_in_dry_run(repo):
    """--dry-run 照算候選數，但不寫檔、不連網。"""
    raw = repo / "data/raw/2026-07-27.json"
    _write(raw, [
        {"source": "rss", "source_name": "R", "title": "更復雜的任務",
         "url": "https://example.com/a", "abstract": "死衚衕", "published_date": "2026-07-27"},
    ])
    before = raw.read_text(encoding="utf-8")
    res = repair_all(dry_run=True, fetcher=_boom, arxiv_fetcher=_boom)
    assert res["typos_fixed"] == 2 and res["files_written"] == 0
    assert raw.read_text(encoding="utf-8") == before


def test_typo_fixes_run_after_conversion(repo):
    """順序不變量：錯字表必須在簡→繁**之後**跑。

    `幹擾` 是 OpenCC 從簡體 `干扰` 收斂出來的結果；若錯字表跑在轉換之前，
    它看到的還是 `干扰`，修完又被 OpenCC 改回 `幹擾`，落地就是錯的。
    """
    _write(repo / "data/raw/2026-07-27.json", [
        {"source": "chatpaper", "source_name": "C", "title": "抱抱脸",
         "url": "https://example.com/a",
         "abstract": "第二种是多人干扰。周围几个人同时移动、交叉甚至交换位置",
         "published_date": "2026-07-27"},
    ])
    repair_all(fetcher=_boom, arxiv_fetcher=_boom)
    stored = json.loads((repo / "data/raw/2026-07-27.json").read_text(encoding="utf-8"))[0]
    assert "多人干擾" in stored["abstract"], stored["abstract"]

    res = repair_all(fetcher=_boom, arxiv_fetcher=_boom)
    assert res["files_written"] == 0, "轉換 ↔ 錯字表之間不得來回震盪"
