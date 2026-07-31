"""Tests for abstract quality gate in blog post generator."""
import pytest
from unittest.mock import MagicMock, patch
from datetime import date, datetime
from src.generators.blog_post import generate_and_save_posts, save_blog_post
from src.models import ContentItem, GeneratedContent, ScoredItem, SourceType


def _make_scored_item(abstract: str) -> ScoredItem:
    item = ContentItem(
        source=SourceType.BLOG,
        source_name="Test Blog",
        title="Test Article",
        url="https://example.com/test",
        authors=["Author"],
        abstract=abstract,
        published_date=date.today(),
        tags=["test"],
    )
    return ScoredItem(item=item, rule_score=80.0, llm_score=70.0)


def test_short_abstract_skips_generation():
    """abstract < 100 字元應跳過生成，回傳空 list。"""
    item = _make_scored_item("Short abstract.")  # < 100 chars
    with patch("src.generators.blog_post.generate_blog_post") as mock_gen:
        result = generate_and_save_posts([item], target_date=date.today())
        mock_gen.assert_not_called()
    assert result == []


def test_sufficient_abstract_generates():
    """abstract >= 100 字元應正常生成。"""
    long_abstract = "B" * 150  # 150 chars, >= 100
    item = _make_scored_item(long_abstract)
    mock_content = MagicMock()
    mock_content.source_item = item
    mock_content.content = "Generated blog post"
    mock_content.prompt_used = "prompt"
    mock_content.model_used = "test-model"
    mock_content.generated_at = datetime.now()
    with patch("src.generators.blog_post.load_config", return_value={"llm": {"request_delay_seconds": 0}}):
        with patch("src.generators.blog_post.generate_blog_post", return_value=mock_content):
            with patch("src.generators.blog_post.save_blog_post", return_value="/fake/path.md") as mock_save:
                result = generate_and_save_posts([item], target_date=date.today())
                mock_save.assert_called_once()
    assert result == ["/fake/path.md"]


# ── P0-2: 空文章 guard ────────────────────────────────────────────────────────

def _gen_with_content(content: str) -> GeneratedContent:
    item = _make_scored_item("A" * 150)
    return GeneratedContent(
        source_item=item,
        content=content,
        prompt_used="prompt",
        model_used="test-model",
        content_type="blog_post",
    )


@pytest.mark.parametrize("empty", ["", "   \n  \t "])
def test_save_blog_post_refuses_empty_content(empty, tmp_path, monkeypatch):
    """llm_chat 回空字串時，save_blog_post 應 raise ValueError，不寫出空文章。"""
    import src.generators.blog_post as bp
    monkeypatch.setattr(bp, "POSTS_DIR", tmp_path)
    monkeypatch.setattr(bp, "PROMPTS_DIR", tmp_path)
    with pytest.raises(ValueError, match="empty post"):
        save_blog_post(_gen_with_content(empty), target_date=date(2026, 2, 26))
    # 不應留下任何檔案
    assert list(tmp_path.glob("*.md")) == []


def test_empty_generation_skipped_batch_continues():
    """一篇生成空內容（guard raise）被 per-item try/except 跳過，不中斷整批。"""
    good = _make_scored_item("G" * 150)
    bad = _make_scored_item("B" * 150)

    def fake_save(gen, target_date=None, pinned=False):
        if not gen.content.strip():
            raise ValueError("refuse to write empty post: x")
        return "/fake/good.md"

    with patch("src.generators.blog_post.load_config", return_value={"llm": {"request_delay_seconds": 0}}):
        with patch("src.generators.blog_post.generate_blog_post",
                   side_effect=[_gen_with_content(""), _gen_with_content("real content")]):
            with patch("src.generators.blog_post.save_blog_post", side_effect=fake_save):
                result = generate_and_save_posts([bad, good], target_date=date.today())
    # 空的被跳過，好的仍寫出
    assert result == ["/fake/good.md"]


# ── P1-2: generation_model 取值不應 eager KeyError ────────────────────────────

def test_generate_blog_post_model_no_keyerror_when_legacy_keys_absent():
    """清掉 legacy 單數 model/generation_model key 後，仍能從 generation_models chain
    取得 model，不應 KeyError。"""
    from src.generators.blog_post import generate_blog_post

    item = _make_scored_item("A" * 150)
    cfg = {"llm": {"generation_models": ["chain/model-1", "chain/model-2"]}}  # 無 model / generation_model
    with patch("src.generators.blog_post.load_config", return_value=cfg):
        with patch("src.generators.blog_post.llm_chat", return_value="content") as mock_chat:
            gen = generate_blog_post(item)
    assert gen.model_used == "chain/model-1"
    assert mock_chat.call_args.kwargs["model"] == "chain/model-1"


def test_generate_blog_post_prefers_singular_generation_model():
    """有 legacy generation_model 時優先採用（行為相容）。"""
    from src.generators.blog_post import generate_blog_post

    item = _make_scored_item("A" * 150)
    cfg = {"llm": {"generation_model": "legacy/gen", "generation_models": ["chain/m1"], "model": "legacy/m"}}
    with patch("src.generators.blog_post.load_config", return_value=cfg):
        with patch("src.generators.blog_post.llm_chat", return_value="content"):
            gen = generate_blog_post(item)
    assert gen.model_used == "legacy/gen"
