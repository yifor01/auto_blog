"""Pipeline 編排邏輯測試（checkpoint / force / supplement 增量）。"""

from __future__ import annotations

import json
from datetime import date
from unittest.mock import MagicMock, patch

import pytest

from src import pipeline
from src.models import ContentItem, ScoredItem, SourceType


# ──────────────────────────────────────────────────────────
# Helpers
# ──────────────────────────────────────────────────────────

def _item(url: str, source: SourceType = SourceType.ARXIV, title: str = "T") -> ContentItem:
    return ContentItem(
        source=source,
        source_name=source.value,
        title=title,
        url=url,
        published_date=date(2026, 1, 1),
    )


def _scored(item: ContentItem, rule: float = 30.0, llm: float = 50.0) -> ScoredItem:
    return ScoredItem(item=item, rule_score=rule, llm_score=llm)


class _FakeCollector:
    """最小 collector stub：name + collect()。"""

    def __init__(self, name: str, items: list[ContentItem]):
        self.name = name
        self._items = items

    def collect(self, target_date):
        return self._items


def _min_config() -> dict:
    return {
        "dedup": {"lookback_days": 0},
        "scoring": {"final_top_k": 30},
    }


# ──────────────────────────────────────────────────────────
# Checkpoint：raw 存在 → 跳過收集
# ──────────────────────────────────────────────────────────

class TestCollectCheckpoint:
    def test_skips_collection_when_raw_exists(self, tmp_path):
        d = date(2026, 1, 1)
        raw_path = tmp_path / f"{d.isoformat()}.json"
        cached = [_item("https://example.com/a").model_dump(mode="json")]
        raw_path.write_text(json.dumps(cached), encoding="utf-8")

        get_collectors = MagicMock()
        with patch.object(pipeline, "RAW_DIR", tmp_path), \
             patch.object(pipeline, "get_collectors", get_collectors):
            result = pipeline.collect_items(d)

        # collectors 不應被建立（使用快取）
        get_collectors.assert_not_called()
        assert len(result) == 1
        assert result[0].url == "https://example.com/a"

    def test_runs_collectors_when_no_raw(self, tmp_path, monkeypatch):
        d = date(2026, 1, 1)
        new_items = [_item("https://example.com/new")]
        collector = _FakeCollector("arxiv", new_items)

        with patch.object(pipeline, "RAW_DIR", tmp_path), \
             patch.object(pipeline, "HEALTH_DIR", tmp_path), \
             patch.object(pipeline, "get_collectors", return_value=[collector]), \
             patch.object(pipeline, "load_config", return_value=_min_config()):
            result = pipeline.collect_items(d)

        assert len(result) == 1
        assert result[0].url == "https://example.com/new"
        # raw 已寫入
        assert (tmp_path / f"{d.isoformat()}.json").exists()

    def test_empty_collection_not_cached(self, tmp_path):
        """所有 collector 回空（多半是 transient 失敗）時不應寫 raw cache，
        避免 [] 被 checkpoint 永久卡住。"""
        d = date(2026, 1, 1)
        collector = _FakeCollector("arxiv", [])
        raw_dir = tmp_path / "raw"
        health_dir = tmp_path / "health"
        raw_dir.mkdir()
        health_dir.mkdir()

        with patch.object(pipeline, "RAW_DIR", raw_dir), \
             patch.object(pipeline, "HEALTH_DIR", health_dir), \
             patch.object(pipeline, "get_collectors", return_value=[collector]), \
             patch.object(pipeline, "load_config", return_value=_min_config()):
            result = pipeline.collect_items(d)

        assert result == []
        assert not (raw_dir / f"{d.isoformat()}.json").exists()


# ──────────────────────────────────────────────────────────
# Score checkpoint：scored 存在 → 跳過篩選
# ──────────────────────────────────────────────────────────

class TestScoreCheckpoint:
    def test_skips_scoring_when_scored_exists(self, tmp_path):
        d = date(2026, 1, 1)
        scored_path = tmp_path / f"{d.isoformat()}.json"
        si = _scored(_item("https://example.com/a"))
        scored_path.write_text(json.dumps([si.model_dump(mode="json")]), encoding="utf-8")

        rule = MagicMock()
        llm = MagicMock()
        with patch.object(pipeline, "SCORED_DIR", tmp_path), \
             patch.object(pipeline, "batch_rule_score", rule), \
             patch.object(pipeline, "batch_llm_score", llm):
            result = pipeline.score_items([_item("https://example.com/a")], d)

        rule.assert_not_called()
        llm.assert_not_called()
        assert len(result) == 1

    def test_empty_scoring_not_cached(self, tmp_path):
        """評分結果為空（LLM 全數失敗等 transient）時不應寫 scored cache。"""
        d = date(2026, 1, 1)
        rule = MagicMock(return_value=[])
        llm = MagicMock(return_value=[])
        with patch.object(pipeline, "SCORED_DIR", tmp_path), \
             patch.object(pipeline, "load_config", return_value=_min_config()), \
             patch.object(pipeline, "batch_rule_score", rule), \
             patch.object(pipeline, "batch_llm_score", llm):
            result = pipeline.score_items([_item("https://example.com/a")], d)

        assert result == []
        assert not (tmp_path / f"{d.isoformat()}.json").exists()


# ──────────────────────────────────────────────────────────
# Force：清除 raw/scored + prompts，保留 posts
# ──────────────────────────────────────────────────────────

class TestForceClear:
    def test_force_clears_caches_keeps_posts(self, tmp_path):
        d = date(2026, 1, 1)
        prefix = d.isoformat()

        raw_dir = tmp_path / "raw"
        scored_dir = tmp_path / "scored"
        posts_dir = tmp_path / "posts"
        prompts_dir = tmp_path / "prompts"
        for p in (raw_dir, scored_dir, posts_dir, prompts_dir):
            p.mkdir()

        raw_file = raw_dir / f"{prefix}.json"
        scored_file = scored_dir / f"{prefix}.json"
        post_file = posts_dir / f"{prefix}_x.md"
        prompt_file = prompts_dir / f"{prefix}_x_prompt.md"
        raw_file.write_text("[]", encoding="utf-8")
        scored_file.write_text("[]", encoding="utf-8")
        post_file.write_text("post", encoding="utf-8")
        prompt_file.write_text("prompt", encoding="utf-8")

        with patch.object(pipeline, "RAW_DIR", raw_dir), \
             patch.object(pipeline, "SCORED_DIR", scored_dir), \
             patch.object(pipeline, "POSTS_DIR", posts_dir), \
             patch.object(pipeline, "PROMPTS_DIR", prompts_dir), \
             patch.object(pipeline, "collect_items", return_value=[]):
            pipeline.run_pipeline(d, force=True)

        # raw/scored/prompt 被清除，post 保留
        assert not raw_file.exists()
        assert not scored_file.exists()
        assert not prompt_file.exists()
        assert post_file.exists()


# ──────────────────────────────────────────────────────────
# Supplement：補收缺失 source + 增量合併
# ──────────────────────────────────────────────────────────

class TestSupplementItems:
    def test_no_missing_returns_cached_unchanged(self, tmp_path):
        d = date(2026, 1, 1)
        raw_path = tmp_path / f"{d.isoformat()}.json"
        existing = [_item("https://e.com/a", SourceType.ARXIV).model_dump(mode="json")]
        raw_path.write_text(json.dumps(existing), encoding="utf-8")

        # 所有 collector 的 source 都已存在 → 用一個只含 arxiv 的 map
        with patch.object(pipeline, "RAW_DIR", tmp_path), \
             patch.object(pipeline, "get_collectors",
                          return_value=[_FakeCollector("arxiv", [])]), \
             patch.dict(pipeline.COLLECTOR_SOURCE_MAP,
                        {"arxiv": SourceType.ARXIV}, clear=True):
            items, changed = pipeline.supplement_items(d)

        assert changed is False
        assert len(items) == 1

    def test_missing_source_collects_and_merges(self, tmp_path):
        d = date(2026, 1, 1)
        raw_path = tmp_path / f"{d.isoformat()}.json"
        existing = [_item("https://e.com/a", SourceType.ARXIV).model_dump(mode="json")]
        raw_path.write_text(json.dumps(existing), encoding="utf-8")

        rss_item = _item("https://e.com/rss", SourceType.RSS, title="rss")
        collectors = [
            _FakeCollector("arxiv", []),
            _FakeCollector("rss", [rss_item]),
        ]

        with patch.object(pipeline, "RAW_DIR", tmp_path), \
             patch.object(pipeline, "get_collectors", return_value=collectors), \
             patch.object(pipeline, "load_config", return_value=_min_config()), \
             patch.dict(pipeline.COLLECTOR_SOURCE_MAP,
                        {"arxiv": SourceType.ARXIV, "rss": SourceType.RSS}, clear=True):
            items, changed = pipeline.supplement_items(d)

        assert changed is True
        urls = {it.url for it in items}
        assert urls == {"https://e.com/a", "https://e.com/rss"}
        # raw 已覆寫含新項目
        saved = json.loads(raw_path.read_text(encoding="utf-8"))
        assert len(saved) == 2

    def test_existing_items_written_back_verbatim(self, tmp_path):
        """既有項目必須寫回原始 dict，不得經 ContentItem 重新序列化。

        存檔裡的「這個文件的參數設定」是 Layer A 已轉繁的成品，s2twp 對它
        不冪等（再套一次會變「這個檔案的參數設定」）。--supplement 每次補收
        都重寫整份 raw，用 model_dump() 等於讓歷史欄位每跑一次漂一次。
        """
        from src.utils import to_traditional

        drifting = "這個文件的參數設定"
        assert to_traditional(drifting) != drifting, "測試前提失效：這串已經冪等了"

        d = date(2026, 1, 1)
        raw_path = tmp_path / f"{d.isoformat()}.json"
        existing = _item("https://e.com/a", SourceType.ARXIV).model_dump(mode="json")
        existing["title"] = drifting
        existing["abstract"] = drifting * 3
        existing["tags"] = [drifting]
        # 舊 schema 留下的欄位：ContentItem 會忽略它、model_dump() 會靜默丟掉它。
        # 有了它，這筆測試才同時守住「寫回用原始 dict」（而不只是「文字沒漂」——
        # 後者現在已由 item_from_raw 保證，寫回改用 model_dump() 也照樣過）。
        existing["legacy_field"] = "must survive"
        raw_path.write_text(json.dumps([existing], ensure_ascii=False), encoding="utf-8")

        rss_item = _item("https://e.com/rss", SourceType.RSS, title="rss")
        collectors = [
            _FakeCollector("arxiv", []),
            _FakeCollector("rss", [rss_item]),
        ]

        with patch.object(pipeline, "RAW_DIR", tmp_path), \
             patch.object(pipeline, "get_collectors", return_value=collectors), \
             patch.object(pipeline, "load_config", return_value=_min_config()), \
             patch.dict(pipeline.COLLECTOR_SOURCE_MAP,
                        {"arxiv": SourceType.ARXIV, "rss": SourceType.RSS}, clear=True):
            _items, changed = pipeline.supplement_items(d)

        assert changed is True
        saved = json.loads(raw_path.read_text(encoding="utf-8"))
        assert len(saved) == 2
        # 既有項目逐字不變；新收項目才是序列化產物
        assert saved[0] == existing
        assert saved[1]["url"] == "https://e.com/rss"

    def test_cross_day_dedup_keeps_raw_dict_alignment(self, tmp_path):
        """跨日去重同時篩掉 dict 與 ContentItem，兩邊索引不得錯位。

        `keep` 的文字刻意用會漂移的字串，讓這一筆同時守住兩個性質：
        索引沒錯位（留下的是 keep 不是 drop）、且留下的內容逐字保留。
        """
        from src.utils import to_traditional

        drifting = "這個文件的參數設定"
        assert to_traditional(drifting) != drifting, "測試前提失效：這串已經冪等了"

        d = date(2026, 1, 1)
        raw_path = tmp_path / f"{d.isoformat()}.json"
        keep = _item("https://e.com/keep", SourceType.ARXIV, title="keep").model_dump(mode="json")
        keep["title"] = drifting
        keep["abstract"] = drifting * 2
        keep["tags"] = [drifting]
        keep["legacy_field"] = "must survive"
        drop = _item("https://e.com/drop", SourceType.ARXIV, title="drop").model_dump(mode="json")
        raw_path.write_text(json.dumps([drop, keep], ensure_ascii=False), encoding="utf-8")

        rss_item = _item("https://e.com/rss", SourceType.RSS, title="rss")
        collectors = [
            _FakeCollector("arxiv", []),
            _FakeCollector("rss", [rss_item]),
        ]
        config = {"dedup": {"lookback_days": 7}, "scoring": {"final_top_k": 30}}

        with patch.object(pipeline, "RAW_DIR", tmp_path), \
             patch.object(pipeline, "get_collectors", return_value=collectors), \
             patch.object(pipeline, "load_config", return_value=config), \
             patch.object(pipeline, "get_seen_urls",
                          return_value={"https://e.com/drop"}), \
             patch.dict(pipeline.COLLECTOR_SOURCE_MAP,
                        {"arxiv": SourceType.ARXIV, "rss": SourceType.RSS}, clear=True):
            items, _changed = pipeline.supplement_items(d)

        saved = json.loads(raw_path.read_text(encoding="utf-8"))
        assert [s["url"] for s in saved] == ["https://e.com/keep", "https://e.com/rss"]
        assert [it.url for it in items] == ["https://e.com/keep", "https://e.com/rss"]
        assert saved[0] == keep

    def test_falls_back_to_full_collect_when_no_raw(self, tmp_path):
        d = date(2026, 1, 1)
        collect = MagicMock(return_value=[_item("https://e.com/x")])
        with patch.object(pipeline, "RAW_DIR", tmp_path), \
             patch.object(pipeline, "collect_items", collect):
            items, changed = pipeline.supplement_items(d)

        collect.assert_called_once()
        assert changed is True
        assert len(items) == 1


# ──────────────────────────────────────────────────────────
# 增量評分：只評新項目，與既有 scored 合併排名
# ──────────────────────────────────────────────────────────

class TestScoreIncremental:
    def test_no_existing_scored_falls_back_to_full(self, tmp_path):
        d = date(2026, 1, 1)
        full = MagicMock(return_value=[_scored(_item("https://e.com/a"))])
        with patch.object(pipeline, "SCORED_DIR", tmp_path), \
             patch.object(pipeline, "score_items", full):
            result = pipeline.score_incremental([_item("https://e.com/a")], d)

        full.assert_called_once()
        assert len(result) == 1

    def test_no_new_items_returns_existing(self, tmp_path):
        d = date(2026, 1, 1)
        scored_path = tmp_path / f"{d.isoformat()}.json"
        existing = _scored(_item("https://e.com/a"))
        scored_path.write_text(json.dumps([existing.model_dump(mode="json")]), encoding="utf-8")

        rule = MagicMock()
        with patch.object(pipeline, "SCORED_DIR", tmp_path), \
             patch.object(pipeline, "batch_rule_score", rule):
            result = pipeline.score_incremental([_item("https://e.com/a")], d)

        rule.assert_not_called()
        assert len(result) == 1

    def test_new_items_scored_and_merged(self, tmp_path):
        d = date(2026, 1, 1)
        scored_path = tmp_path / f"{d.isoformat()}.json"
        old = _scored(_item("https://e.com/old"), rule=10, llm=10)  # total 20
        scored_path.write_text(json.dumps([old.model_dump(mode="json")]), encoding="utf-8")

        # 用非清單來源（RSS）：清單來源會被 score_incremental 過濾掉不評分
        new_item = _item("https://e.com/new", source=SourceType.RSS, title="new")
        new_scored = _scored(new_item, rule=40, llm=40)  # total 80

        with patch.object(pipeline, "SCORED_DIR", tmp_path), \
             patch.object(pipeline, "load_config", return_value=_min_config()), \
             patch.object(pipeline, "batch_rule_score", return_value=[new_scored]), \
             patch.object(pipeline, "batch_llm_score", return_value=[new_scored]):
            result = pipeline.score_incremental(
                [_item("https://e.com/old"), new_item], d
            )

        # 合併後依 total_score 排序，新項目分數高排前面
        assert len(result) == 2
        assert result[0].item.url == "https://e.com/new"
        saved = json.loads(scored_path.read_text(encoding="utf-8"))
        assert len(saved) == 2


# ──────────────────────────────────────────────────────────
# 讀 data/raw 的呼叫點：一律無損還原（不得重複套用 Layer A 的 s2twp）
#
# item_from_raw() 本身的單元測試在 tests/test_models.py::TestItemFromRaw。
# 這裡守的是「每個讀 raw 的呼叫點都真的走了它」——退回 ContentItem(**raw)
# 是靜默的（不會拋錯、不會有 log），只有針對呼叫端的測試抓得到。
# ──────────────────────────────────────────────────────────

DRIFTING = "這個文件的參數設定"  # s2twp 再套一次 → 這個檔案的參數設定


def _drifting_raw(url: str, source: SourceType = SourceType.ARXIV, **extra) -> dict:
    rec = _item(url, source).model_dump(mode="json")
    rec["title"] = DRIFTING
    rec["abstract"] = DRIFTING * 3
    rec["tags"] = [DRIFTING]
    rec.update(extra)
    return rec


def _assert_verbatim(it) -> None:
    assert it.title == DRIFTING, f"title 漂移: {it.title!r}"
    assert it.abstract == DRIFTING * 3, f"abstract 漂移: {it.abstract!r}"
    assert it.tags == [DRIFTING], f"tags 漂移: {it.tags!r}"


class TestRawReadsAreLossless:
    def test_premise_string_really_drifts(self):
        from src.utils import to_traditional

        assert to_traditional(DRIFTING) != DRIFTING, "測試前提失效：這串已經冪等了"

    def test_collect_items_checkpoint(self, tmp_path):
        """checkpoint 續跑（raw 已存在）回傳的 items 餵給 build_lists()，不得漂。"""
        d = date(2026, 1, 1)
        (tmp_path / f"{d.isoformat()}.json").write_text(
            json.dumps([_drifting_raw("https://e.com/a")], ensure_ascii=False), encoding="utf-8"
        )
        with patch.object(pipeline, "RAW_DIR", tmp_path):
            items = pipeline.collect_items(d)
        assert len(items) == 1
        _assert_verbatim(items[0])

    def test_supplement_returned_items(self, tmp_path):
        """--supplement 回傳的既有項目會餵給 build_lists()，不得漂。"""
        d = date(2026, 1, 1)
        (tmp_path / f"{d.isoformat()}.json").write_text(
            json.dumps([_drifting_raw("https://e.com/a")], ensure_ascii=False), encoding="utf-8"
        )
        collectors = [_FakeCollector("arxiv", []), _FakeCollector("rss", [])]
        with patch.object(pipeline, "RAW_DIR", tmp_path), \
             patch.object(pipeline, "get_collectors", return_value=collectors), \
             patch.object(pipeline, "load_config", return_value=_min_config()), \
             patch.dict(pipeline.COLLECTOR_SOURCE_MAP,
                        {"arxiv": SourceType.ARXIV, "rss": SourceType.RSS}, clear=True):
            items, _changed = pipeline.supplement_items(d)
        assert len(items) == 1
        _assert_verbatim(items[0])

    def test_run_score_feeds_scorer_verbatim(self, tmp_path):
        """run_score 的產出寫進 data/scored，來源 items 不得漂。"""
        d = date(2026, 1, 1)
        (tmp_path / f"{d.isoformat()}.json").write_text(
            json.dumps([_drifting_raw("https://e.com/a")], ensure_ascii=False), encoding="utf-8"
        )
        captured = {}

        def _fake_score(items, _d):
            captured["items"] = items
            return []

        with patch.object(pipeline, "RAW_DIR", tmp_path), \
             patch.object(pipeline, "SCORED_DIR", tmp_path), \
             patch.object(pipeline, "score_items", _fake_score):
            pipeline.run_score(d)

        assert len(captured["items"]) == 1
        _assert_verbatim(captured["items"][0])

    def test_pinned_generation_uses_verbatim_title(self, tmp_path):
        """置頂文的檔名 slug 與內文都來自 item.title，不得漂。"""
        d = date(2026, 7, 21)
        rec = _drifting_raw("https://openai.com/blog/x", SourceType.RSS,
                            organization="OpenAI", published_date=d.isoformat())
        (tmp_path / f"{d.isoformat()}.json").write_text(
            json.dumps([rec], ensure_ascii=False), encoding="utf-8"
        )
        captured = {}

        def _fake_generate(todo, _d, pinned=False):
            captured["todo"] = todo
            return []

        config = {"pinned_organizations": ["OpenAI"], "pinned_daily_limit": 5}
        with patch.object(pipeline, "RAW_DIR", tmp_path), \
             patch.object(pipeline, "POSTS_DIR", tmp_path), \
             patch.object(pipeline, "load_config", return_value=config), \
             patch("src.generators.blog_post.generate_and_save_posts", _fake_generate):
            pipeline._generate_pinned_posts(d)

        assert len(captured["todo"]) == 1
        _assert_verbatim(captured["todo"][0].item)


# ──────────────────────────────────────────────────────────
# 讀 data/scored 的呼叫點：一律無損還原
#
# scored_from_raw() 本身的單元測試在 tests/test_models.py::TestScoredFromRaw。
# 這裡守的是「每個讀 scored 的呼叫點都真的走了它」——退回 ScoredItem(**rec)
# 一樣是靜默的（ScoredItem 內嵌的 item 會再跑一次 Layer A validator）。
# ──────────────────────────────────────────────────────────

def _drifting_scored_rec(url: str, source: SourceType = SourceType.RSS, **extra) -> dict:
    rec = _scored(_item(url, source)).model_dump(mode="json")
    rec["item"]["title"] = DRIFTING
    rec["item"]["abstract"] = DRIFTING * 3
    rec["item"]["tags"] = [DRIFTING]
    rec.update(extra)
    return rec


class TestScoredReadsAreLossless:
    def test_score_items_checkpoint(self, tmp_path):
        """checkpoint 續跑（scored 已存在）直接回傳快取，這批會餵給 generate。"""
        d = date(2026, 1, 1)
        (tmp_path / f"{d.isoformat()}.json").write_text(
            json.dumps([_drifting_scored_rec("https://e.com/a")], ensure_ascii=False),
            encoding="utf-8",
        )
        with patch.object(pipeline, "SCORED_DIR", tmp_path):
            items = pipeline.score_items([], d)
        assert len(items) == 1
        _assert_verbatim(items[0].item)

    def test_run_generate_feeds_generator_verbatim(self, tmp_path):
        """run_generate 的產出寫進 output/posts，來源 items 不得漂。"""
        d = date(2026, 1, 1)
        (tmp_path / f"{d.isoformat()}.json").write_text(
            json.dumps([_drifting_scored_rec("https://e.com/a")], ensure_ascii=False),
            encoding="utf-8",
        )
        captured = {}

        def _fake_generate(items, _d):
            captured["items"] = items
            return []

        with patch.object(pipeline, "SCORED_DIR", tmp_path), \
             patch.object(pipeline, "generate_posts", _fake_generate):
            pipeline.run_generate(d)

        assert len(captured["items"]) == 1
        _assert_verbatim(captured["items"][0].item)

    def test_score_incremental_returned_items(self, tmp_path):
        """--supplement 回傳的既有項目會直接餵給 generate 階段，不得漂。"""
        d = date(2026, 1, 1)
        (tmp_path / f"{d.isoformat()}.json").write_text(
            json.dumps([_drifting_scored_rec("https://e.com/a")], ensure_ascii=False),
            encoding="utf-8",
        )
        with patch.object(pipeline, "SCORED_DIR", tmp_path), \
             patch.object(pipeline, "load_config", return_value=_min_config()):
            result = pipeline.score_incremental([_item("https://e.com/a")], d)

        assert len(result) == 1
        _assert_verbatim(result[0].item)

    def test_score_incremental_writeback_preserves_original_dict(self, tmp_path):
        """讀-改-寫：既有項目寫回 data/scored 必須是原始 dict，不能是 model_dump()。

        這是本輪最要命的一條——Web Monitor 啟動時對當天自動走 --supplement，
        開一次 dashboard 就把漂移永久固化進存檔，且逐日累積。

        誠實標註：讀取端改對之後，單獨把寫回換成 model_dump() 已經不會讓這裡的
        title 斷言失敗（model_dump 出來的就是還原後的值）。真正單獨釘住寫回的是
        下面那條 legacy relevance 測試；這條守的是「讀 + 寫同時退化」的組合，
        以及排序後 payload 與 ScoredItem 的索引不得錯位。
        """
        d = date(2026, 1, 1)
        scored_path = tmp_path / f"{d.isoformat()}.json"
        scored_path.write_text(
            json.dumps([_drifting_scored_rec("https://e.com/old", rule_score=10.0,
                                             llm_score=10.0)], ensure_ascii=False),
            encoding="utf-8",
        )
        new_item = _item("https://e.com/new", source=SourceType.RSS, title="new")
        new_scored = _scored(new_item, rule=40, llm=40)

        with patch.object(pipeline, "SCORED_DIR", tmp_path), \
             patch.object(pipeline, "load_config", return_value=_min_config()), \
             patch.object(pipeline, "batch_rule_score", return_value=[new_scored]), \
             patch.object(pipeline, "batch_llm_score", return_value=[new_scored]):
            result = pipeline.score_incremental([_item("https://e.com/old"), new_item], d)

        # 排序仍照 total_score（新項目 80 > 舊項目 20），payload 必須跟著一起搬
        assert [si.item.url for si in result] == ["https://e.com/new", "https://e.com/old"]
        saved = json.loads(scored_path.read_text(encoding="utf-8"))
        assert [rec["item"]["url"] for rec in saved] == ["https://e.com/new", "https://e.com/old"]
        old_rec = saved[1]
        assert old_rec["item"]["title"] == DRIFTING, f"寫回漂移: {old_rec['item']['title']!r}"
        assert old_rec["item"]["abstract"] == DRIFTING * 3
        assert old_rec["item"]["tags"] == [DRIFTING]

    def test_score_incremental_writeback_keeps_legacy_relevance_key(self, tmp_path):
        """沿用原始 dict 的副作用要講清楚：舊版 relevance 鍵原樣保留、不改寫成 trending。

        這是刻意的——「無損」的定義就是不動存檔既有內容，讀取端由
        scored_from_raw() 的 _migrate_relevance 負責相容。
        """
        d = date(2026, 1, 1)
        scored_path = tmp_path / f"{d.isoformat()}.json"
        rec = _drifting_scored_rec("https://e.com/old", rule_score=10.0, llm_score=10.0)
        rec["relevance"] = rec.pop("trending")
        scored_path.write_text(json.dumps([rec], ensure_ascii=False), encoding="utf-8")

        new_item = _item("https://e.com/new", source=SourceType.RSS, title="new")
        new_scored = _scored(new_item, rule=40, llm=40)
        with patch.object(pipeline, "SCORED_DIR", tmp_path), \
             patch.object(pipeline, "load_config", return_value=_min_config()), \
             patch.object(pipeline, "batch_rule_score", return_value=[new_scored]), \
             patch.object(pipeline, "batch_llm_score", return_value=[new_scored]):
            pipeline.score_incremental([_item("https://e.com/old"), new_item], d)

        saved = json.loads(scored_path.read_text(encoding="utf-8"))
        assert "relevance" in saved[1] and "trending" not in saved[1]
