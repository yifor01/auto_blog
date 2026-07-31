"""src/backfill.py 隔日補票測試。"""
import json
from datetime import date
from unittest.mock import patch

import pytest

from src import backfill
from src.models import ContentItem, SourceType

D = date(2026, 7, 24)


def _hf(title: str, upvotes: int, paper_id: str) -> ContentItem:
    url = f"https://huggingface.co/papers/{paper_id}"
    return ContentItem(
        source=SourceType.HF_PAPERS,
        source_name="HuggingFace Daily Papers",
        title=title,
        url=url,
        abstract="some abstract " * 10,
        published_date=D,
        raw_metadata={"upvotes": upvotes, "hf_url": url, "arxiv_id": paper_id},
    )


def _github(title: str, stars: int) -> ContentItem:
    return ContentItem(
        source=SourceType.GITHUB,
        source_name="GitHub Trending",
        title=title,
        url=f"https://github.com/{title}",
        abstract="repo description " * 5,
        published_date=D,
        raw_metadata={"stars_today": stars},
    )


@pytest.fixture
def workspace(tmp_path, monkeypatch):
    """把 raw / lists 目錄導到 tmp，避免動到真實資料。"""
    raw_dir = tmp_path / "raw"
    lists_dir = tmp_path / "lists"
    raw_dir.mkdir()
    lists_dir.mkdir()
    monkeypatch.setattr(backfill, "RAW_DIR", raw_dir)
    monkeypatch.setattr("src.lists.LISTS_DIR", lists_dir)
    # backfill 在 pytest 下預設完全不動作（防止誤打真實 HF / 改真實 data/raw），
    # 這裡目錄已導到 tmp、fetch_upvotes 也都有 mock，才明確解除該保險
    monkeypatch.setenv("AUTOPB_ALLOW_BACKFILL_IN_TESTS", "1")
    return raw_dir, lists_dir


def _seed(raw_dir, lists_dir, items):
    from src.lists import build_day_lists

    (raw_dir / f"{D.isoformat()}.json").write_text(
        json.dumps([i.model_dump(mode="json") for i in items], ensure_ascii=False, default=str)
    )
    (lists_dir / f"{D.isoformat()}.json").write_text(
        json.dumps(build_day_lists(items, D), ensure_ascii=False)
    )


def test_backfill_updates_votes_and_reorders(workspace):
    """票數回補後，lists 的 hf 段必須依新票數重排。"""
    raw_dir, lists_dir = workspace
    items = [
        _hf("paper A", 0, "2607.00001"),
        _hf("paper B", 0, "2607.00002"),
        _github("org/repo", 100),
    ]
    _seed(raw_dir, lists_dir, items)

    votes = {
        "https://huggingface.co/papers/2607.00001": 12,
        "https://huggingface.co/papers/2607.00002": 144,
    }
    with patch.object(backfill, "fetch_upvotes", return_value=votes):
        stats = backfill.backfill_hf_upvotes(D, quiet=True)

    assert stats["updated"] == 2
    assert stats["changed"] == 2
    assert stats["max_delta"] == 144

    lists_data = json.loads((lists_dir / f"{D.isoformat()}.json").read_text())
    hf = lists_data["papers"]["hf"]
    assert [e["title"] for e in hf] == ["paper B", "paper A"]  # 依新票數重排
    assert [e["upvotes"] for e in hf] == [144, 12]
    assert len(lists_data["github"]) == 1  # 其他來源不受影響

    raw_data = json.loads((raw_dir / f"{D.isoformat()}.json").read_text())
    hf_raw = {r["title"]: r["raw_metadata"]["upvotes"] for r in raw_data if r["source"] == "hf_papers"}
    assert hf_raw == {"paper A": 12, "paper B": 144}


def test_backfill_is_noop_under_pytest_by_default(tmp_path, monkeypatch):
    """沒有明確解除保險時，pytest 下絕不打網路、不碰檔案。"""
    monkeypatch.setattr(backfill, "RAW_DIR", tmp_path)
    monkeypatch.delenv("AUTOPB_ALLOW_BACKFILL_IN_TESTS", raising=False)

    def _boom(*_a, **_kw):
        raise AssertionError("fetch_upvotes 不該在測試中被呼叫")

    with patch.object(backfill, "fetch_upvotes", side_effect=_boom):
        stats = backfill.backfill_hf_upvotes(D, quiet=True)
    assert stats["updated"] == 0


def test_backfill_no_raw_file_is_noop(workspace):
    """該日沒跑過 pipeline 時安靜跳過，不可拋例外。"""
    stats = backfill.backfill_hf_upvotes(D, quiet=True)
    assert stats["updated"] == 0 and stats["changed"] == 0


def test_backfill_empty_votes_leaves_data_untouched(workspace):
    """抓不到票數（日期轉址 / 網路失敗）時完全不動既有資料。"""
    raw_dir, lists_dir = workspace
    _seed(raw_dir, lists_dir, [_hf("paper A", 7, "2607.00001")])
    before = (raw_dir / f"{D.isoformat()}.json").read_text()

    with patch.object(backfill, "fetch_upvotes", return_value={}):
        stats = backfill.backfill_hf_upvotes(D, quiet=True)

    assert stats["changed"] == 0
    assert (raw_dir / f"{D.isoformat()}.json").read_text() == before


def test_backfill_unchanged_votes_skips_write(workspace):
    """票數沒變就不重寫檔案（避免每天產生無意義的 diff）。"""
    raw_dir, lists_dir = workspace
    _seed(raw_dir, lists_dir, [_hf("paper A", 42, "2607.00001")])
    before = (lists_dir / f"{D.isoformat()}.json").read_text()

    with patch.object(backfill, "fetch_upvotes",
                      return_value={"https://huggingface.co/papers/2607.00001": 42}):
        stats = backfill.backfill_hf_upvotes(D, quiet=True)

    assert stats["updated"] == 1 and stats["changed"] == 0
    assert (lists_dir / f"{D.isoformat()}.json").read_text() == before


def test_backfill_does_not_reapply_opencc(workspace):
    """讀-改-寫不得對已轉繁的存檔再套一次 s2twp（檔→件 那類漂移）。

    存檔裡的「這個文件的參數設定」本身就是 Layer A 轉過的成品
    （來源是簡體「这个文档的参数设置」）。s2twp 對它不冪等，再套一次會變
    「這個檔案的參數設定」——backfill 每天跑，等於每天讓歷史資料漂一次。
    """
    from src.utils import to_traditional

    drifting = "這個文件的參數設定"
    assert to_traditional(drifting) != drifting, "測試前提失效：這串已經冪等了"

    raw_dir, lists_dir = workspace
    _seed(raw_dir, lists_dir, [_hf("paper A", 0, "2607.00001")])

    raw_path = raw_dir / f"{D.isoformat()}.json"
    data = json.loads(raw_path.read_text())
    data[0]["title"] = drifting
    data[0]["abstract"] = drifting * 3
    data[0]["tags"] = [drifting]
    # 舊 schema 留下的欄位：ContentItem 會忽略它、model_dump() 會靜默丟掉它。
    # 有了它，這筆測試才同時守住「寫回用原始 dict」（而不只是「文字沒漂」——
    # 後者現在已由 item_from_raw 保證，寫回改用 model_dump() 也照樣過）。
    data[0]["legacy_field"] = "must survive"
    raw_path.write_text(json.dumps(data, ensure_ascii=False))
    before = json.loads(raw_path.read_text())

    with patch.object(backfill, "fetch_upvotes",
                      return_value={"https://huggingface.co/papers/2607.00001": 99}):
        stats = backfill.backfill_hf_upvotes(D, quiet=True)

    assert stats["changed"] == 1
    after = json.loads(raw_path.read_text())

    # upvotes 以外的欄位必須逐字不變
    expected = dict(before[0])
    expected["raw_metadata"] = {**before[0]["raw_metadata"], "upvotes": 99}
    assert after == [expected]


def test_backfill_lists_text_matches_raw_verbatim(workspace):
    """重建的 output/lists 文字必須與 data/raw 逐字一致。

    build_day_lists() 吃的是 ContentItem，若重建時多套一次 s2twp，raw 凍結後
    lists 仍會每次多漂一格 → 兩者開始有落差。而詳情頁的「原始資料 box」直接讀
    data/raw，兩處並列時同一段文字會顯示不一致。

    測資取自真實 GitHub trending abstract（近 40 天清單型來源 3375 筆中有 34 筆
    對 s2twp 非冪等，約 1%）。
    """
    from src.utils import to_traditional

    # 真實樣本：`中文文件` → `中文檔案`、`高性價比` → `高價效比`
    drifting = "Docs for AI Agents 中文文件 · 主打高性價比國產模型"
    assert to_traditional(drifting) != drifting, "測試前提失效：這串已經冪等了"

    raw_dir, lists_dir = workspace
    _seed(raw_dir, lists_dir, [_hf("paper A", 0, "2607.00001"), _github("org/repo", 100)])

    raw_path = raw_dir / f"{D.isoformat()}.json"
    data = json.loads(raw_path.read_text())
    for rec in data:
        rec["abstract"] = drifting
        rec["title"] = drifting
    raw_path.write_text(json.dumps(data, ensure_ascii=False))

    with patch.object(backfill, "fetch_upvotes",
                      return_value={"https://huggingface.co/papers/2607.00001": 99}):
        backfill.backfill_hf_upvotes(D, quiet=True)

    raw_after = json.loads(raw_path.read_text())
    lists_after = json.loads((lists_dir / f"{D.isoformat()}.json").read_text())

    # raw 本身不得漂
    assert {r["abstract"] for r in raw_after} == {drifting}
    # lists 的每個 entry 也不得漂——與 raw 逐字一致
    entries = lists_after["github"] + lists_after["papers"]["hf"] + lists_after["papers"]["others"]
    assert entries, "測試無效：lists 是空的"
    for e in entries:
        assert e["abstract"] == drifting, f"lists abstract 漂移: {e['abstract']!r}"
        assert e["title"] == drifting, f"lists title 漂移: {e['title']!r}"


def test_backfill_recent_covers_requested_days(workspace):
    """days=2 應回補基準日前兩天。"""
    seen = []
    with patch.object(backfill, "backfill_hf_upvotes", side_effect=lambda d, quiet=False: seen.append(d) or {}):
        backfill.backfill_recent(date(2026, 7, 26), days=2, quiet=True)
    assert seen == [date(2026, 7, 25), date(2026, 7, 24)]
