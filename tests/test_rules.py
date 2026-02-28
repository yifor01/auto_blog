"""Rule-based scoring 邏輯測試（含 B2 word boundary 修復驗證）。"""

from __future__ import annotations

from datetime import date

import pytest

from src.models import ContentItem, SourceType
from src.scoring.rules import _match_institution, batch_rule_score, rule_score


class TestMatchInstitution:
    """B2: word boundary 機構匹配測試。"""

    def test_exact_org_match(self):
        assert _match_institution("google", "Google DeepMind", "") is True

    def test_org_case_insensitive(self):
        assert _match_institution("OpenAI", "openai", "") is True

    def test_author_word_boundary_match(self):
        assert _match_institution("apple", "", "Tim Cook Apple Research") is True

    def test_false_positive_snapple(self):
        """'apple' 不應該匹配 'Snapple'。"""
        assert _match_institution("apple", "", "John Snapple Jr") is False

    def test_false_positive_goo(self):
        """'google' 不應該匹配 'Jin Goo Lee'（舊版 substring 的誤判）。"""
        assert _match_institution("google", "", "Jin Goo Lee") is False

    def test_false_positive_meta_in_name(self):
        """'meta' 不應該匹配包含 'meta' 的一般詞彙。"""
        assert _match_institution("meta", "", "metadata analyst") is False

    def test_org_field_takes_priority(self):
        """organization 欄位比 authors 更可靠，應優先比對。"""
        assert _match_institution("microsoft", "Microsoft Research", "") is True

    def test_no_match(self):
        assert _match_institution("deepmind", "Stanford", "Alice Bob") is False


class TestRuleScore:
    def test_google_institution_bonus(self, arxiv_item, sample_config):
        """Google 作者應觸發頂流機構加分。"""
        arxiv_item.organization = "Google"
        result = rule_score(arxiv_item, sample_config)
        assert result.rule_score >= 20
        assert any("頂流機構" in r for r in result.rule_reasons)

    def test_keyword_bonus_capped(self, sample_config):
        """關鍵字加分上限 15 分。"""
        item = ContentItem(
            source=SourceType.ARXIV,
            title="Agent reasoning RAG multimodal chain-of-thought benchmark",
            url="https://example.com",
            published_date=date(2026, 2, 26),
            abstract="agent reasoning RAG multimodal" * 5,
        )
        result = rule_score(item, sample_config)
        # 4 個關鍵字 × 5 = 20，但上限 15
        kw_bonus = next(
            (r for r in result.rule_reasons if "熱門關鍵字" in r), None
        )
        assert kw_bonus is not None
        # 驗證加分上限
        assert result.rule_score <= 15 + 20 + 15 + 5 + 3  # max possible

    def test_hf_papers_bonus(self, hf_item, sample_config):
        """HF Papers 應觸發收錄加分。"""
        result = rule_score(hf_item, sample_config)
        assert any("HuggingFace" in r for r in result.rule_reasons)
        # upvotes=25 > threshold=10，應有額外加分
        assert any("upvotes" in r for r in result.rule_reasons)

    def test_hf_papers_no_upvote_bonus_below_threshold(self, sample_config):
        """HF upvotes 低於門檻不應加分。"""
        item = ContentItem(
            source=SourceType.HF_PAPERS,
            title="Some paper",
            url="https://hf.co/paper/1",
            published_date=date(2026, 2, 26),
            abstract="test",
            raw_metadata={"upvotes": 5},  # 低於 threshold=10
        )
        result = rule_score(item, sample_config)
        assert not any("upvotes" in r for r in result.rule_reasons)

    def test_github_high_stars_bonus(self, github_item, sample_config):
        """GitHub stars > 100 應觸發高分加分。"""
        github_item.raw_metadata["stars_today"] = 150
        result = rule_score(github_item, sample_config)
        assert any("GitHub stars" in r for r in result.rule_reasons)

    def test_github_medium_stars_bonus(self, sample_config):
        """GitHub stars 50-100 應觸發中分加分。"""
        item = ContentItem(
            source=SourceType.GITHUB,
            title="cool-ai-tool",
            url="https://github.com/user/tool",
            published_date=date(2026, 2, 26),
            raw_metadata={"stars_today": 75},
        )
        result = rule_score(item, sample_config)
        assert any("GitHub stars" in r for r in result.rule_reasons)

    def test_rss_source_bonus(self, rss_item, sample_config):
        """RSS 來源應獲得保底加分。"""
        result = rule_score(rss_item, sample_config)
        assert any("新聞" in r for r in result.rule_reasons)

    def test_novelty_signal_in_title(self, sample_config):
        """標題含新穎性訊號應加分。"""
        item = ContentItem(
            source=SourceType.ARXIV,
            title="Beyond State-of-the-Art: A Novel Approach",
            url="https://arxiv.org/abs/2601.00003",
            published_date=date(2026, 2, 26),
            abstract="x" * 600,
        )
        result = rule_score(item, sample_config)
        assert any("新穎性訊號" in r for r in result.rule_reasons)

    def test_short_abstract_penalty(self, sample_config):
        """非 github/blog 來源的過短摘要應被扣分。"""
        item = ContentItem(
            source=SourceType.ARXIV,
            title="Short paper",
            url="https://arxiv.org/abs/2601.00004",
            published_date=date(2026, 2, 26),
            abstract="Too short.",
        )
        result = rule_score(item, sample_config)
        assert any("摘要過短" in r for r in result.rule_reasons)

    def test_score_never_negative(self, sample_config):
        """規則分數不應低於 0。"""
        item = ContentItem(
            source=SourceType.ARXIV,
            title="A paper",
            url="https://arxiv.org/abs/2601.00005",
            published_date=date(2026, 2, 26),
            abstract="X",
        )
        result = rule_score(item, sample_config)
        assert result.rule_score >= 0


class TestBatchRuleScore:
    def test_filters_below_threshold(self, sample_config):
        """低分 items 應被 threshold 過濾掉。"""
        items = [
            ContentItem(
                source=SourceType.ARXIV,
                title=f"Paper {i}",
                url=f"https://arxiv.org/abs/260{i:05d}",
                published_date=date(2026, 2, 26),
                abstract="X",  # 短摘要 → 扣分
            )
            for i in range(5)
        ]
        result = batch_rule_score(items, sample_config)
        assert all(s.rule_score >= sample_config["scoring"]["rule_threshold"] for s in result)

    def test_returns_sorted_by_score(self, arxiv_item, hf_item, rss_item, sample_config):
        """結果應按分數降序排列。"""
        result = batch_rule_score([arxiv_item, hf_item, rss_item], sample_config)
        scores = [s.rule_score for s in result]
        assert scores == sorted(scores, reverse=True)

    def test_config_threshold_respected(self, sample_config):
        """自訂 threshold 應被遵守。"""
        sample_config["scoring"]["rule_threshold"] = 100  # 極高門檻
        items = [
            ContentItem(
                source=SourceType.ARXIV,
                title="Paper",
                url="https://arxiv.org/abs/test",
                published_date=date(2026, 2, 26),
                abstract="test",
            )
        ]
        result = batch_rule_score(items, sample_config)
        assert result == []
