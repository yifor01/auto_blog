"""data_service 讀 data/scored 的 9 個呼叫點：一律無損還原。

`scored_from_raw()` 本身的單元測試在 tests/test_models.py::TestScoredFromRaw；
這裡守的是「每個呼叫點都真的走了它」。退回 `ScoredItem(**rec)` 是完全靜默的
（內嵌的 `item: ContentItem` 會再跑一次 Layer A 的 s2twp），而本模組每一頁都是
給人看的文字——素材庫列表、搜尋結果、主題頁與同頁直接讀 data/raw 的
「原始資料 box」並列時，同一段文字會顯示不一致。
"""

from __future__ import annotations

import json
from datetime import date, timedelta

import pytest

DRIFTING = "這個文件的參數設定"  # s2twp 再套一次 → 這個檔案的參數設定
DRIFTING_TAG = "高性價比"        # → 高價效比

TODAY = date.today()


def _rec(url: str = "https://example.com/a", pub: date | None = None) -> dict:
    return {
        "item": {
            "source": "rss",
            "source_name": "TechCrunch AI",
            "title": DRIFTING,
            "url": url,
            "authors": ["Alice"],
            "abstract": DRIFTING * 3,
            "published_date": (pub or TODAY).isoformat(),
            "tags": [DRIFTING_TAG, DRIFTING],
            "organization": "OpenAI",
            "raw_metadata": {},
        },
        "rule_score": 30.0,
        "rule_reasons": [],
        "llm_score": 60.0,
        "llm_reason": "ok",
        "novelty": 12.0, "impact": 12.0, "trending": 12.0,
        "practicality": 12.0, "blog_worthiness": 12.0,
    }


@pytest.fixture
def ds(tmp_path, monkeypatch):
    """把 data_service 的所有目錄常數導向 tmp，並清掉 module-level cache。

    why monkeypatch.setattr 而非 chdir：這些常數是由 PROJECT_ROOT 推導的絕對
    路徑，換 cwd 只會讓測試讀到專案真實的 data/ 與 output/。
    """
    from src.web import data_service

    dirs = {}
    for name in ("SCORED_DIR", "RAW_DIR", "POSTS_DIR", "NOTES_DIR",
                 "BLOGS_DIR", "HEALTH_DIR", "LISTS_DIR", "DIGESTS_DIR"):
        p = tmp_path / name.lower()
        p.mkdir()
        dirs[name] = p
        monkeypatch.setattr(data_service, name, p)

    (dirs["SCORED_DIR"] / f"{TODAY.isoformat()}.json").write_text(
        json.dumps([_rec()], ensure_ascii=False), encoding="utf-8"
    )
    # 搜尋索引與 scored cache 是 module-level 全域，跨測試會殘留
    monkeypatch.setattr(data_service, "_search_index", [])
    monkeypatch.setattr(data_service, "_search_built_at", 0)
    data_service._scored_cache.clear()
    yield data_service
    data_service._scored_cache.clear()


def _assert_verbatim(d: dict) -> None:
    assert d["title"] == DRIFTING, f"title 漂移: {d['title']!r}"
    assert d["tags"] == [DRIFTING_TAG, DRIFTING], f"tags 漂移: {d['tags']!r}"


def test_premise_strings_really_drift():
    """測試前提：這兩串在 s2twp 下不冪等。前提失效要立刻自曝，而非靜默常綠。"""
    from src.utils import to_traditional

    assert to_traditional(DRIFTING) != DRIFTING
    assert to_traditional(DRIFTING_TAG) != DRIFTING_TAG


def test_get_week_top_items(ds):
    """首頁本週精選卡片。"""
    items = ds.get_week_top_items(days=7, top_k=5)
    assert len(items) == 1
    _assert_verbatim(items[0])
    assert items[0]["abstract"] == DRIFTING * 3


def test_get_day_items(ds):
    """Day Detail 的已評分列表。"""
    items = ds.get_day_items(TODAY)
    assert len(items) == 1
    _assert_verbatim(items[0])
    assert items[0]["abstract"] == DRIFTING * 3


def test_get_all_day_items(ds):
    """素材庫列表（raw + scored 合併）——reviewer 實測 AGREE? False 的那一頁。

    同一筆資料在 raw 與 scored 各存一份、內容一致；scored 側若多套一次 s2twp，
    列表顯示的 title 就會與詳情頁「原始資料 box」（直接讀 raw）打架。
    """
    raw_rec = dict(_rec()["item"])
    (ds.RAW_DIR / f"{TODAY.isoformat()}.json").write_text(
        json.dumps([raw_rec], ensure_ascii=False), encoding="utf-8"
    )
    items = ds.get_all_day_items(TODAY)
    assert len(items) == 1
    assert items[0]["scored"] is True
    _assert_verbatim(items[0])


def test_get_item_detail(ds):
    """詳情頁本體。"""
    detail = ds.get_item_detail(TODAY, 0)
    assert detail is not None
    _assert_verbatim(detail)
    assert detail["abstract"] == DRIFTING * 3


def test_load_scored_for_date(ds):
    """post 詳情頁的評分跨查——以 title 為 key，漂移會直接查不到而靜默掉分數。"""
    got = ds._load_scored_for_date(TODAY.isoformat())
    assert DRIFTING in got, f"key 漂移: {list(got)!r}"


def test_list_all_materials(ds):
    """素材庫全量掃描。"""
    items = ds.list_all_materials(days=7)
    assert len(items) == 1
    _assert_verbatim(items[0])
    assert items[0]["abstract"] == DRIFTING * 3


def test_build_search_index(ds):
    """搜尋索引：title/tags 進索引，也進分詞後的 _tokens。"""
    ds.build_search_index()
    assert len(ds._search_index) == 1
    _assert_verbatim(ds._search_index[0])


def test_cluster_topics(ds, monkeypatch):
    """主題瀏覽頁。"""
    monkeypatch.setattr(
        "src.utils.load_config",
        lambda: {"topic_clusters": {"參數": ["參數設定"]}},
    )
    got = ds.cluster_topics(days=7)
    assert len(got["topics"]["參數"]) == 1, "關鍵字匹配落空——searchable 內容已漂"
    _assert_verbatim(got["topics"]["參數"][0])


def test_get_dashboard_charts_uses_the_lossless_reader(ds, monkeypatch):
    """Dashboard 圖表只吐數字與 source_name，Layer A 欄位不出現在輸出裡。

    也就是說這個呼叫點退回 ScoredItem(**rec) 在行為上「看不出來」——只能直接
    釘住它呼叫了 scored_from_raw()。留著它是為了維持單一讀取路徑：一旦這裡
    退化，下一個照抄這段寫法的人就會把漂移帶進會顯示文字的地方。
    """
    calls = []
    real = ds.scored_from_raw
    monkeypatch.setattr(ds, "scored_from_raw",
                        lambda rec: (calls.append(rec), real(rec))[1])
    charts = ds.get_dashboard_charts(days=7)
    assert charts["source_data"] == [1]  # 前提：真的讀到了那筆資料
    assert calls, "get_dashboard_charts 沒走 scored_from_raw()"
