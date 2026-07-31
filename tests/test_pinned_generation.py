"""Pinned 生成整合測試。"""
from datetime import date, datetime

import yaml

from src.models import ContentItem, GeneratedContent, SourceType
from src.pinned import to_pinned_scored

D = date(2026, 7, 21)


def _gen(title="OpenAI ships GPT-6"):
    item = ContentItem(
        source=SourceType.RSS, source_name="OpenAI Blog", title=title,
        url="https://openai.com/blog/gpt-6", abstract="x" * 200,
        published_date=D, organization="OpenAI",
    )
    return GeneratedContent(
        source_item=to_pinned_scored(item), content="📌 內容", prompt_used="p",
        model_used="m", generated_at=datetime(2026, 7, 21, 3, 0),
    )


def test_save_blog_post_pinned_frontmatter(tmp_path, monkeypatch):
    import src.generators.blog_post as bp

    monkeypatch.setattr(bp, "POSTS_DIR", tmp_path)
    monkeypatch.setattr(bp, "PROMPTS_DIR", tmp_path)
    path = bp.save_blog_post(_gen(), D, pinned=True)
    fm = yaml.safe_load(open(path).read().split("---")[1])
    assert fm["pinned"] is True
    assert "score" not in fm  # 置頂文沒有評分，不寫誤導性的 0 分


def test_save_blog_post_normal_no_pinned_key(tmp_path, monkeypatch):
    import src.generators.blog_post as bp

    monkeypatch.setattr(bp, "POSTS_DIR", tmp_path)
    monkeypatch.setattr(bp, "PROMPTS_DIR", tmp_path)
    path = bp.save_blog_post(_gen(), D)  # pinned 預設 False
    fm = yaml.safe_load(open(path).read().split("---")[1])
    assert "pinned" not in fm
    assert fm["score"] == 0


def test_generate_posts_runs_pinned_first(tmp_path, monkeypatch):
    from src import pipeline
    from src.models import ScoredItem

    d = D
    raw_item = {
        "source": "rss", "source_name": "OpenAI Blog", "title": "GPT-6",
        "url": "https://openai.com/blog/gpt-6", "abstract": "x" * 200,
        "published_date": d.isoformat(), "organization": "OpenAI",
    }
    raw_path = tmp_path / f"{d.isoformat()}.json"
    import json
    raw_path.write_text(json.dumps([raw_item]))
    monkeypatch.setattr(pipeline, "get_raw_path", lambda dd: raw_path)
    monkeypatch.setattr(pipeline, "POSTS_DIR", tmp_path)  # checkpoint 檢查用

    calls = []

    def fake_generate(items, target_date=None, pinned=False):
        calls.append((pinned, [it.item.title for it in items]))
        return [f"/fake/{it.item.title}.md" for it in items]

    import src.generators.blog_post as bp
    monkeypatch.setattr(bp, "generate_and_save_posts", fake_generate)

    paths = pipeline.generate_posts([], d)
    assert calls[0][0] is True          # pinned 批先跑
    assert calls[0][1] == ["GPT-6"]
    assert len(paths) == 1


def test_score_items_excludes_pinned(tmp_path, monkeypatch):
    from src import pipeline
    from src.models import ContentItem

    monkeypatch.setattr(pipeline, "get_scored_path", lambda d: tmp_path / f"{d}.json")
    received = {}
    monkeypatch.setattr(
        pipeline, "batch_rule_score",
        lambda items, config: received.update(items=items) or [],
    )
    monkeypatch.setattr(pipeline, "batch_llm_score", lambda items, config: [])
    monkeypatch.setattr(
        pipeline, "load_config",
        lambda: {"pinned_organizations": ["OpenAI"], "pinned_daily_limit": 5, "scoring": {}},
    )

    pinned_item = ContentItem(
        source=SourceType.RSS, source_name="OpenAI Blog", title="GPT-6",
        url="https://openai.com/blog/gpt-6", abstract="x" * 200,
        published_date=D, organization="OpenAI",
    )
    normal = ContentItem(
        source=SourceType.RSS, source_name="TechCrunch AI", title="other news",
        url="https://example.com/news", abstract="x" * 200, published_date=D,
    )
    pipeline.score_items([pinned_item, normal], D)
    assert [it.title for it in received["items"]] == ["other news"]


# ──────────────────────────────────────────────────────────
# Finding 1：評分為零時 pinned 仍須生成（不被 `if not top_items` guard block）
# spec §5：pinned / 一般生成互不 block
# ──────────────────────────────────────────────────────────

def _one_item():
    return [
        ContentItem(
            source=SourceType.RSS, source_name="RSS", title="some news",
            url="https://example.com/x", abstract="y" * 200, published_date=D,
        )
    ]


def test_run_pipeline_generates_pinned_when_scoring_empty(monkeypatch):
    """run_pipeline 路徑：score_items 回 [] 時，仍須呼叫 _generate_pinned_posts。"""
    from src import pipeline

    calls = {"pinned": 0}
    monkeypatch.setattr(pipeline, "get_pipeline_state", lambda d: "pending")
    monkeypatch.setattr(pipeline, "collect_items", lambda target_date=None: _one_item())
    monkeypatch.setattr(pipeline, "build_lists", lambda i, td, force=False: None)
    monkeypatch.setattr(pipeline, "score_items", lambda items, d: [])
    monkeypatch.setattr(
        pipeline, "_generate_pinned_posts",
        lambda d: calls.__setitem__("pinned", calls["pinned"] + 1) or [],
    )
    monkeypatch.setattr(
        pipeline, "generate_posts",
        lambda *a, **k: (_ for _ in ()).throw(AssertionError("top_items 空時不該生成一般 posts")),
    )

    pipeline.run_pipeline(D)
    assert calls["pinned"] == 1


def test_run_supplement_generates_pinned_when_scoring_empty(monkeypatch):
    """run_supplement 路徑：score 回 [] 時 pinned 仍生成（在 changed/has_posts gate 之外）。"""
    from src import pipeline

    calls = {"pinned": 0}
    monkeypatch.setattr(pipeline, "supplement_items", lambda d: (_one_item(), True))
    monkeypatch.setattr(pipeline, "build_lists", lambda i, td, force=False: None)
    monkeypatch.setattr(pipeline, "score_incremental", lambda items, d: [])
    monkeypatch.setattr(pipeline, "score_items", lambda items, d: [])
    monkeypatch.setattr(
        pipeline, "_generate_pinned_posts",
        lambda d: calls.__setitem__("pinned", calls["pinned"] + 1) or [],
    )
    monkeypatch.setattr(
        pipeline, "generate_posts",
        lambda *a, **k: (_ for _ in ()).throw(AssertionError("top_items 空時不該生成一般 posts")),
    )

    pipeline.run_supplement(D)
    assert calls["pinned"] == 1


def test_run_catchup_generates_pinned_when_scoring_empty(monkeypatch):
    """run_catchup 路徑：score 回 [] 時 pinned 仍生成。"""
    from src import pipeline

    calls = {"pinned": 0}
    monkeypatch.setattr(pipeline, "get_pipeline_state", lambda d: "pending")
    monkeypatch.setattr(pipeline, "collect_items", lambda target_date=None: _one_item())
    monkeypatch.setattr(pipeline, "build_lists", lambda i, td, force=False: None)
    monkeypatch.setattr(pipeline, "score_items", lambda items, d: [])
    monkeypatch.setattr(
        pipeline, "_generate_pinned_posts",
        lambda d: calls.__setitem__("pinned", calls["pinned"] + 1) or [],
    )
    monkeypatch.setattr(
        pipeline, "generate_posts",
        lambda *a, **k: (_ for _ in ()).throw(AssertionError("top_items 空時不該生成一般 posts")),
    )

    pipeline.run_catchup(days=1)
    assert calls["pinned"] >= 1


def test_run_catchup_dry_run_skips_pinned(monkeypatch):
    """dry_run 下不生成任何內容（含 pinned）。"""
    from src import pipeline

    calls = {"pinned": 0}
    monkeypatch.setattr(pipeline, "get_pipeline_state", lambda d: "pending")
    monkeypatch.setattr(pipeline, "collect_items", lambda target_date=None: _one_item())
    monkeypatch.setattr(pipeline, "build_lists", lambda i, td, force=False: None)
    monkeypatch.setattr(pipeline, "score_items", lambda items, d: [])
    monkeypatch.setattr(
        pipeline, "_generate_pinned_posts",
        lambda d: calls.__setitem__("pinned", calls["pinned"] + 1) or [],
    )

    pipeline.run_catchup(days=1, dry_run=True)
    assert calls["pinned"] == 0
