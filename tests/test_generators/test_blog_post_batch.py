"""批次生成測試（全 mock，不叫起 claude CLI）。

設計前提：批次是**可選路徑**，config flag 關閉時既有逐篇路徑的行為必須一字不差，
且批次任何一篇出問題都要能退回逐篇——切回 OpenRouter 只需改一個 bool，不需 revert code。
"""
from datetime import date
from unittest.mock import patch

import pytest

from src.generators.blog_post import (
    BATCH_END_MARKER,
    build_batch_prompt,
    generate_and_save_posts,
    generate_posts_batch,
    parse_batch_output,
)
from src.models import ContentItem, ScoredItem, SourceType


def _item(title: str = "Test Article", abstract_len: int = 150) -> ScoredItem:
    item = ContentItem(
        source=SourceType.BLOG,
        source_name="Test Blog",
        title=title,
        url=f"https://example.com/{title.replace(' ', '-')}",
        authors=["Author"],
        abstract="A" * abstract_len,
        published_date=date.today(),
        tags=["test"],
    )
    return ScoredItem(item=item, rule_score=80.0, llm_score=70.0)


def _batch_output(*bodies: str) -> str:
    parts = [f"===POST {n}===\n{b}" for n, b in enumerate(bodies, 1)]
    return "\n".join(parts) + f"\n{BATCH_END_MARKER}\n"


# ── 解析 ──────────────────────────────────────────────────────────────────

class TestParseBatchOutput:
    def test_splits_all_posts(self):
        got = parse_batch_output(_batch_output("📌 甲\n內文甲", "📌 乙\n內文乙"), expected=2)
        assert got == {1: "📌 甲\n內文甲", 2: "📌 乙\n內文乙"}

    def test_end_marker_stripped_from_last_body(self):
        got = parse_batch_output(_batch_output("📌 只有一篇"), expected=1)
        assert BATCH_END_MARKER not in got[1]

    def test_leading_noise_discarded(self):
        """模型偶爾在第一個分隔行前寫一句「好的，以下是四篇文章」。"""
        noisy = "好的，以下是為您撰寫的文章：\n\n" + _batch_output("📌 甲")
        assert parse_batch_output(noisy, expected=1) == {1: "📌 甲"}

    def test_missing_post_simply_absent(self):
        """少寫一篇不是例外，是缺漏——回傳缺該 key，由上層 fallback。"""
        out = "===POST 1===\n📌 甲\n===POST 3===\n📌 丙\n" + BATCH_END_MARKER
        got = parse_batch_output(out, expected=3)
        assert set(got) == {1, 3}

    def test_out_of_range_index_ignored(self):
        """模型多寫一篇 POST 5（只給了 2 篇素材）不能污染對齊。"""
        out = _batch_output("📌 甲", "📌 乙").replace(BATCH_END_MARKER, "===POST 5===\n📌 幻覺\n" + BATCH_END_MARKER)
        assert set(parse_batch_output(out, expected=2)) == {1, 2}

    def test_empty_body_dropped(self):
        out = "===POST 1===\n\n===POST 2===\n📌 乙\n" + BATCH_END_MARKER
        assert set(parse_batch_output(out, expected=2)) == {2}

    @pytest.mark.parametrize("junk", ["", "完全沒有分隔符的一段話", "===POST===\n沒有編號"])
    def test_unparseable_returns_empty(self, junk):
        assert parse_batch_output(junk, expected=2) == {}


# ── prompt 組裝 ────────────────────────────────────────────────────────────

class TestBuildBatchPrompt:
    def test_contains_every_item_and_contract(self):
        items = [_item("Alpha"), _item("Beta")]
        p = build_batch_prompt(items)
        assert "Alpha" in p and "Beta" in p
        assert "### 素材 1" in p and "### 素材 2" in p
        assert "===POST 1===" in p and BATCH_END_MARKER in p

    def test_llm_reason_marked_untrusted(self):
        """選題角度是 LLM 產的，批次模式同樣不得被當事實引用。"""
        items = [_item("Alpha")]
        items[0].llm_reason = "這篇很重要"
        p = build_batch_prompt(items)
        assert "這篇很重要" in p
        assert "禁止當事實引用" in p


# ── 批次生成 ───────────────────────────────────────────────────────────────

class TestGeneratePostsBatch:
    def test_aligns_results_to_input_order(self):
        items = [_item("Alpha"), _item("Beta")]
        with patch("src.generators.blog_post.claude_code_generate",
                   return_value=_batch_output("📌 甲", "📌 乙")):
            got = generate_posts_batch(items, model="sonnet", timeout=1)
        assert [g.content for g in got] == ["📌 甲", "📌 乙"]
        assert [g.source_item.item.title for g in got] == ["Alpha", "Beta"]

    def test_missing_entry_is_none(self):
        items = [_item("Alpha"), _item("Beta")]
        with patch("src.generators.blog_post.claude_code_generate",
                   return_value="===POST 2===\n📌 乙\n" + BATCH_END_MARKER):
            got = generate_posts_batch(items, model="sonnet", timeout=1)
        assert got[0] is None
        assert got[1].content == "📌 乙"

    def test_cli_failure_all_none(self):
        items = [_item("Alpha"), _item("Beta")]
        with patch("src.generators.blog_post.claude_code_generate", return_value=""):
            got = generate_posts_batch(items, model="sonnet", timeout=1)
        assert got == [None, None]

    def test_reasoning_leak_becomes_none(self):
        """批次也要過推理外洩防線——洩漏的那篇退回 None，交給逐篇重生成。"""
        items = [_item("Alpha"), _item("Beta")]
        leak = "We need to produce a blog article about this paper."
        with patch("src.generators.blog_post.claude_code_generate",
                   return_value=_batch_output(leak, "📌 乙")):
            got = generate_posts_batch(items, model="sonnet", timeout=1)
        assert got[0] is None
        assert got[1].content == "📌 乙"

    def test_preamble_stripped(self):
        items = [_item("Alpha")]
        body = "這是一篇針對「產業新聞」型別的技術報導。\n\n📌 真正的標題\n內文"
        with patch("src.generators.blog_post.claude_code_generate",
                   return_value=_batch_output(body)):
            got = generate_posts_batch(items, model="sonnet", timeout=1)
        assert got[0].content.startswith("📌 真正的標題")

    def test_model_used_is_identifiable(self):
        """frontmatter 的 model 欄位會顯示在網站上，要看得出是哪條路徑產的。"""
        items = [_item("Alpha")]
        with patch("src.generators.blog_post.claude_code_generate",
                   return_value=_batch_output("📌 甲")):
            got = generate_posts_batch(items, model="sonnet", timeout=1)
        assert got[0].model_used == "claude-code/sonnet"

    def test_prompt_used_is_reproducible(self):
        """稽核用：存的必須是真的送出去的那份批次 prompt。"""
        items = [_item("Alpha"), _item("Beta")]
        with patch("src.generators.blog_post.claude_code_generate",
                   return_value=_batch_output("📌 甲", "📌 乙")) as m:
            got = generate_posts_batch(items, model="sonnet", timeout=1)
        sent = m.call_args.args[0]
        for g in got:
            assert sent in g.prompt_used


# ── 分流：兩種模式相容 ──────────────────────────────────────────────────────

_CFG_OFF = {"llm": {"request_delay_seconds": 0}}
_CFG_ON = {"llm": {"request_delay_seconds": 0,
                   "batch_generation": {"enabled": True, "model": "sonnet", "batch_size": 4, "timeout_seconds": 900}}}


class TestModeDispatch:
    def test_flag_absent_uses_sequential(self):
        """config 沒有 batch_generation 區段時必須走既有路徑（向後相容）。"""
        items = [_item("Alpha")]
        with patch("src.generators.blog_post.load_config", return_value=_CFG_OFF), \
             patch("src.generators.blog_post.claude_code_generate") as mock_cli, \
             patch("src.generators.blog_post.generate_blog_post") as mock_seq, \
             patch("src.generators.blog_post.save_blog_post", return_value="/p.md"):
            generate_and_save_posts(items, target_date=date.today())
        mock_cli.assert_not_called()
        mock_seq.assert_called_once()

    def test_flag_on_uses_batch(self):
        items = [_item("Alpha"), _item("Beta")]
        with patch("src.generators.blog_post.load_config", return_value=_CFG_ON), \
             patch("src.generators.blog_post.claude_code_generate",
                   return_value=_batch_output("📌 甲", "📌 乙")) as mock_cli, \
             patch("src.generators.blog_post.generate_blog_post") as mock_seq, \
             patch("src.generators.blog_post.save_blog_post", return_value="/p.md"):
            paths = generate_and_save_posts(items, target_date=date.today())
        mock_cli.assert_called_once()
        mock_seq.assert_not_called()
        assert len(paths) == 2

    def test_splits_into_batches_of_configured_size(self):
        items = [_item(f"T{i}") for i in range(9)]
        with patch("src.generators.blog_post.load_config", return_value=_CFG_ON), \
             patch("src.generators.blog_post.claude_code_generate",
                   side_effect=lambda p, **k: _batch_output(*(["📌 x"] * p.count("### 素材 ")))) as mock_cli, \
             patch("src.generators.blog_post.save_blog_post", return_value="/p.md"):
            generate_and_save_posts(items, target_date=date.today())
        assert mock_cli.call_count == 3  # 4 + 4 + 1

    def test_batch_gap_falls_back_per_item(self):
        """批次少寫一篇 → 該篇改走 OpenRouter 逐篇，不是整批重來、也不是靜默丟掉。"""
        items = [_item("Alpha"), _item("Beta")]
        with patch("src.generators.blog_post.load_config", return_value=_CFG_ON), \
             patch("src.generators.blog_post.claude_code_generate",
                   return_value="===POST 2===\n📌 乙\n" + BATCH_END_MARKER), \
             patch("src.generators.blog_post.generate_blog_post") as mock_seq, \
             patch("src.generators.blog_post.save_blog_post", return_value="/p.md"):
            generate_and_save_posts(items, target_date=date.today())
        assert mock_seq.call_count == 1
        assert mock_seq.call_args.args[0].item.title == "Alpha"

    def test_cli_dead_falls_back_entirely(self):
        """CLI 沒裝 / OAuth 過期時，整批回 "" → 全部逐篇，pipeline 不該因此空手而歸。"""
        items = [_item("Alpha"), _item("Beta")]
        with patch("src.generators.blog_post.load_config", return_value=_CFG_ON), \
             patch("src.generators.blog_post.claude_code_generate", return_value=""), \
             patch("src.generators.blog_post.generate_blog_post") as mock_seq, \
             patch("src.generators.blog_post.save_blog_post", return_value="/p.md"):
            generate_and_save_posts(items, target_date=date.today())
        assert mock_seq.call_count == 2

    def test_short_abstract_excluded_before_batching(self):
        """摘要過短的不進批次 prompt——省 token，也維持與逐篇路徑一致的跳過行為。"""
        items = [_item("Alpha"), _item("TooShort", abstract_len=10)]
        with patch("src.generators.blog_post.load_config", return_value=_CFG_ON), \
             patch("src.generators.blog_post.claude_code_generate",
                   return_value=_batch_output("📌 甲")) as mock_cli, \
             patch("src.generators.blog_post.generate_blog_post") as mock_seq, \
             patch("src.generators.blog_post.save_blog_post", return_value="/p.md"):
            paths = generate_and_save_posts(items, target_date=date.today())
        assert "TooShort" not in mock_cli.call_args.args[0]
        mock_seq.assert_not_called()
        assert len(paths) == 1

    def test_pinned_flag_propagates(self):
        items = [_item("Alpha")]
        with patch("src.generators.blog_post.load_config", return_value=_CFG_ON), \
             patch("src.generators.blog_post.claude_code_generate",
                   return_value=_batch_output("📌 甲")), \
             patch("src.generators.blog_post.save_blog_post", return_value="/p.md") as mock_save:
            generate_and_save_posts(items, target_date=date.today(), pinned=True)
        assert mock_save.call_args.kwargs["pinned"] is True

    def test_save_failure_skips_item_not_batch(self):
        """一篇寫檔失敗（空文章 guard）不得中斷同批其他篇。"""
        items = [_item("Alpha"), _item("Beta")]
        with patch("src.generators.blog_post.load_config", return_value=_CFG_ON), \
             patch("src.generators.blog_post.claude_code_generate",
                   return_value=_batch_output("📌 甲", "📌 乙")), \
             patch("src.generators.blog_post.save_blog_post",
                   side_effect=[ValueError("refuse to write empty post"), "/ok.md"]):
            paths = generate_and_save_posts(items, target_date=date.today())
        assert paths == ["/ok.md"]
