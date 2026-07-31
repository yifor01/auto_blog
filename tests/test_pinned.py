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
