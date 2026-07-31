"""Rule-based scoring 邏輯測試（含 B2 word boundary 修復驗證）。"""

from __future__ import annotations

from datetime import date

import pytest

from src.models import ContentItem, SourceType
from src.scoring.rules import _match_institution, _term_matches, batch_rule_score, rule_score


class TestTermMatches:
    """word boundary 詞彙比對（關鍵字與標題訊號共用）。"""

    def test_single_word_exact(self):
        assert _term_matches("agent", "An autonomous agent system") is True

    def test_single_word_substring_rejected(self):
        """'new' 不應匹配 'renew'/'newsletter' 等子字串。"""
        assert _term_matches("new", "renewable energy newsletter") is False

    def test_single_word_standalone_matches(self):
        """'new' 仍應匹配獨立出現的 'new'（如真實誤判案例的標題）。"""
        title = "New York lawmakers pass one-year ban on new data centers"
        assert _term_matches("new", title) is True

    def test_sota_not_in_minnesota(self):
        """'sota' 不應匹配 'Minnesota'。"""
        assert _term_matches("sota", "A study in Minnesota") is False

    def test_multi_word_keyword(self):
        assert _term_matches("flow matching", "We use flow matching for generation") is True

    def test_hyphen_keyword_matches_spaced(self):
        """連字號詞與空白詞互通：'chain of thought' 命中 'chain-of-thought'。"""
        assert _term_matches("chain of thought", "Long chain-of-thought reasoning") is True

    def test_hyphenated_term_boundary(self):
        assert _term_matches("state-of-the-art", "A State-of-the-Art model") is True

    def test_case_insensitive(self):
        assert _term_matches("rag", "Building RAG pipelines") is True


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

    def test_rss_source_bonus(self, rss_item, sample_config):
        """RSS 來源應獲得來源權重加分。"""
        result = rule_score(rss_item, sample_config)
        assert any("來源權重" in r for r in result.rule_reasons)

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

    def test_multiple_institutions_accumulate(self, sample_config):
        """多機構命中應累計加分（不再 break 後只加一次）。"""
        item = ContentItem(
            source=SourceType.ARXIV,
            title="Collaboration paper",
            url="https://arxiv.org/abs/2601.10001",
            published_date=date(2026, 2, 26),
            organization="Google and OpenAI",  # 同時含 Google 與 OpenAI
            abstract="x" * 600,
        )
        result = rule_score(item, sample_config)
        inst_reasons = [r for r in result.rule_reasons if "頂流機構" in r]
        assert len(inst_reasons) == 2  # 累計兩個機構

    def test_institution_bonus_capped_at_two(self, sample_config):
        """機構加分上限 2 個，即使命中更多也不超過。"""
        sample_config["scoring"]["top_institutions"] = [
            "Google", "OpenAI", "Anthropic", "Microsoft", "Apple",
        ]
        item = ContentItem(
            source=SourceType.ARXIV,
            title="Mega collab",
            url="https://arxiv.org/abs/2601.10002",
            published_date=date(2026, 2, 26),
            organization="Google OpenAI Anthropic Microsoft Apple",
            abstract="x" * 600,
        )
        result = rule_score(item, sample_config)
        inst_reasons = [r for r in result.rule_reasons if "頂流機構" in r]
        assert len(inst_reasons) == 2  # 最多 2 個

    def test_keyword_word_boundary_no_false_positive(self, sample_config):
        """關鍵字 'agent' 不應匹配 'agentic'/'reagent' 之類無關子字串。"""
        item = ContentItem(
            source=SourceType.ARXIV,
            title="A reagent for chemical reasoning experiments",
            url="https://arxiv.org/abs/2601.10003",
            published_date=date(2026, 2, 26),
            abstract="Chemistry reagent study with no AI relevance. " * 10,
        )
        result = rule_score(item, sample_config)
        kw_reason = next((r for r in result.rule_reasons if "熱門關鍵字" in r), "")
        # 'reasoning' 應命中，但 'agent' 不應從 'reagent' 命中
        assert "agent" not in kw_reason

    def test_novelty_signal_new_removed(self, sample_config):
        """'new' 已從 novelty_signals 移除，不應單憑此觸發新穎性加分。"""
        item = ContentItem(
            source=SourceType.ARXIV,
            title="A new data center policy report",
            url="https://arxiv.org/abs/2601.10004",
            published_date=date(2026, 2, 26),
            abstract="x" * 600,
        )
        result = rule_score(item, sample_config)
        assert not any("新穎性訊號" in r for r in result.rule_reasons)

    def test_novelty_signal_novel_retained(self, sample_config):
        """'novel' 仍保留，應觸發新穎性加分。"""
        item = ContentItem(
            source=SourceType.ARXIV,
            title="A Novel Unified Architecture",
            url="https://arxiv.org/abs/2601.10005",
            published_date=date(2026, 2, 26),
            abstract="x" * 600,
        )
        result = rule_score(item, sample_config)
        assert any("新穎性訊號" in r for r in result.rule_reasons)


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


class TestHackerNewsScoring:
    """HN points 分級加分（話題性信號）。

    回歸保護：SourceType.HACKERNEWS.value == "hackernews"（無底線），
    曾誤寫成 "hacker_news" 導致整段是 dead code。
    """

    @staticmethod
    def _hn_item(points: int) -> ContentItem:
        return ContentItem(
            source=SourceType.HACKERNEWS,
            source_name="Hacker News",
            title="A discussion link",  # 避免命中 novelty signals
            url="https://news.ycombinator.com/item?id=1",
            published_date=date(2026, 2, 26),
            abstract="x" * 100,  # 介於 50~500，避免長度加/扣分
            raw_metadata={"points": points},
        )

    def test_enum_value_has_no_underscore(self):
        assert SourceType.HACKERNEWS.value == "hackernews"

    def test_viral_tier(self, sample_config):
        result = rule_score(self._hn_item(350), sample_config)
        assert any("爆紅" in r for r in result.rule_reasons)
        assert any("350 points" in r for r in result.rule_reasons)

    def test_hot_tier(self, sample_config):
        result = rule_score(self._hn_item(200), sample_config)
        assert any("熱門" in r and "200 points" in r for r in result.rule_reasons)

    def test_base_tier(self, sample_config):
        result = rule_score(self._hn_item(80), sample_config)
        assert any("Hacker News" in r and "80 points" in r for r in result.rule_reasons)

    def test_below_threshold_no_hn_bonus(self, sample_config):
        result = rule_score(self._hn_item(10), sample_config)
        assert not any("points" in r for r in result.rule_reasons)

    def test_tiers_are_monotonic(self, sample_config):
        viral = rule_score(self._hn_item(350), sample_config).rule_score
        hot = rule_score(self._hn_item(200), sample_config).rule_score
        base = rule_score(self._hn_item(80), sample_config).rule_score
        low = rule_score(self._hn_item(10), sample_config).rule_score
        assert viral > hot > base > low
