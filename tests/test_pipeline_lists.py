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
