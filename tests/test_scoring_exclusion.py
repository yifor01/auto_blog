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
