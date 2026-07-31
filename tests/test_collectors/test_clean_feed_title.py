"""Tests for clean_feed_title().

Anthropic 系鏡像 feed（Olshansk/rss-feeds，Selenium 抓取）會把頁面上的
日期與分類標籤黏進 <title>，例如：

    "Jul 24, 2026Frontier Red TeamProject Pilot: Can AI control a drone?"

這些項目走 pinned 路線（免評分直接生成），污染標題會原樣進生成 prompt
與 frontmatter，因此在建 ContentItem 前必須清掉。
"""

from __future__ import annotations

import pytest


class TestCleanFeedTitle:
    """真實樣本取自 feed_anthropic_research.xml（2026-07-26 抓取）。"""

    @pytest.mark.parametrize(
        "raw,expected",
        [
            (
                "Jul 24, 2026Frontier Red TeamProject Pilot: Can AI control a drone?",
                "Project Pilot: Can AI control a drone?",
            ),
            (
                "Jul 13, 2026Societal ImpactsClaude's values across models and languages",
                "Claude's values across models and languages",
            ),
            (
                "Jul 9, 2026Frontier Red TeamClaude plays robotics",
                "Claude plays robotics",
            ),
            (
                "Jul 8, 2026AlignmentAn off switch for dual-use knowledge in AI models",
                "An off switch for dual-use knowledge in AI models",
            ),
            (
                "Jun 18, 2026Frontier Red TeamProject Fetch: Phase two",
                "Project Fetch: Phase two",
            ),
        ],
    )
    def test_strips_leading_date_and_category(self, raw, expected):
        from src.collectors._helpers import clean_feed_title

        assert clean_feed_title(raw) == expected

    def test_strips_date_appearing_after_category(self):
        """有些 entry 的分類在日期之前。"""
        from src.collectors._helpers import clean_feed_title

        raw = "Economic ResearchJun 26, 2026Anthropic Economic Index report: Cadences"
        assert clean_feed_title(raw) == "Anthropic Economic Index report: Cadences"

    def test_leaves_clean_title_untouched(self):
        from src.collectors._helpers import clean_feed_title

        raw = "A global workspace in language models"
        assert clean_feed_title(raw) == raw

    def test_leaves_normal_feed_titles_untouched(self):
        """一般 feed（TechCrunch/OpenAI 等）標題不得被動到。"""
        from src.collectors._helpers import clean_feed_title

        for raw in [
            "Introducing Claude Opus 5",
            "How Deutsche Telekom is rewiring telecommunications with AI",
            "Claude models explained: choosing the best model for your use case",
            "GPT-Red: Unlocking Self-Improvement for Robustness",
        ]:
            assert clean_feed_title(raw) == raw

    def test_does_not_split_camelcase_product_names(self):
        """無日期戳時絕不做分類切除，CamelCase 產品名不受影響。"""
        from src.collectors._helpers import clean_feed_title

        assert clean_feed_title("PyTorch 2.9 released") == "PyTorch 2.9 released"
        assert clean_feed_title("vLLM adds speculative decoding") == "vLLM adds speculative decoding"

    def test_keeps_remainder_when_category_prefix_too_long(self):
        """找不到可信的分類接合點時，只移除日期、保留其餘（安全降級）。"""
        from src.collectors._helpers import clean_feed_title

        raw = "Jul 24, 2026A perfectly ordinary title with no glued category"
        assert clean_feed_title(raw) == "A perfectly ordinary title with no glued category"

    def test_handles_empty_and_whitespace(self):
        from src.collectors._helpers import clean_feed_title

        assert clean_feed_title("") == ""
        assert clean_feed_title("   ") == ""

    def test_date_only_title_yields_empty(self):
        from src.collectors._helpers import clean_feed_title

        assert clean_feed_title("Jul 24, 2026") == ""
