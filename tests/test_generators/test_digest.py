"""測試每日摘要生成器（模板式，不需 LLM）。"""
from __future__ import annotations

from datetime import date

from src.generators.digest import generate_digest, generate_and_save_digest
from src.models import ContentItem, ScoredItem, SourceType


def _scored(title: str, total: float, source_name: str = "arXiv") -> ScoredItem:
    item = ContentItem(
        source=SourceType.ARXIV,
        source_name=source_name,
        title=title,
        url=f"https://arxiv.org/abs/{abs(hash(title)) % 100000}",
        authors=["Alice"],
        abstract="An abstract. " * 30,
        published_date=date(2026, 2, 26),
        tags=["agent"],
    )
    # total_score = rule_score + llm_score；rule 設 0、用 llm_score 直接控制總分落點
    return ScoredItem(item=item, rule_score=0.0, rule_reasons=[], llm_score=total,
                      llm_reason="值得一讀")


def test_digest_splits_top_picks_and_worth_watching():
    items = [_scored("High", 90), _scored("Mid", 50)]
    md = generate_digest(items, date(2026, 2, 26))

    assert "# 每日精選摘要 — 2026-02-26" in md
    assert "## Top Picks" in md
    assert "High" in md
    assert "## Worth Watching" in md
    assert "Mid" in md


def test_digest_empty_top_picks_message():
    md = generate_digest([_scored("OnlyMid", 40)], date(2026, 2, 26))
    assert "今日無分數超過 80 的 Top Pick" in md


def test_digest_quick_stats_counts():
    items = [_scored("A", 90), _scored("B", 85), _scored("C", 30)]
    md = generate_digest(items, date(2026, 2, 26))
    # 3 筆素材、2 筆 Top Picks (>80)
    assert "| 評分素材總數 | 3 |" in md
    assert "| Top Picks (>80) | 2 |" in md


def test_digest_handles_empty_items():
    md = generate_digest([], date(2026, 2, 26))
    assert "| 評分素材總數 | 0 |" in md
    assert "今日無分數超過 80 的 Top Pick" in md


def test_generate_and_save_digest_writes_file(tmp_path, monkeypatch):
    import src.generators.digest as digest_mod

    monkeypatch.setattr(digest_mod, "DIGESTS_DIR", tmp_path)
    path = generate_and_save_digest([_scored("X", 90)], date(2026, 2, 26))
    assert path.exists()
    assert path.name == "2026-02-26.md"
    assert "X" in path.read_text(encoding="utf-8")
