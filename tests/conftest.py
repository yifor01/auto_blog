"""共用 fixtures 與測試輔助函式。"""

from __future__ import annotations

from datetime import date
from unittest.mock import MagicMock

import pytest

from src.models import ContentItem, ScoredItem, SourceType


# ──────────────────────────────────────────────────────────
# 基礎資料 fixtures
# ──────────────────────────────────────────────────────────

@pytest.fixture
def sample_config() -> dict:
    """最小可用 config，供 scoring 測試使用。"""
    return {
        "llm": {
            "model": "test-model",
            "fallback_model": None,
            "max_tokens": 500,
            "request_delay_seconds": 0,
        },
        "scoring": {
            "top_institutions": ["Google", "OpenAI", "Anthropic", "Microsoft", "Apple"],
            "hot_keywords": ["agent", "reasoning", "RAG", "multimodal"],
            "rule_threshold": 25,
            "llm_top_k": 5,
            "final_top_k": 3,
            "hf_upvote_bonus_threshold": 10,
            "github_stars_high": 100,
            "github_stars_medium": 50,
        },
        "dedup": {"lookback_days": 7},
        "generation": {"blog_post": {"language": "zh-TW"}, "note": {"language": "zh-TW"}},
    }


@pytest.fixture
def arxiv_item() -> ContentItem:
    return ContentItem(
        source=SourceType.ARXIV,
        source_name="arXiv",
        title="A Novel Agent-based Reasoning Framework",
        url="https://arxiv.org/abs/2601.00001",
        authors=["Alice Smith", "Bob Jones"],
        abstract="We propose a novel framework for LLM-based agents with advanced reasoning. " * 20,
        published_date=date(2026, 2, 26),
        organization="Google",
        raw_metadata={"arxiv_id": "2601.00001"},
    )


@pytest.fixture
def hf_item() -> ContentItem:
    return ContentItem(
        source=SourceType.HF_PAPERS,
        source_name="HuggingFace Papers",
        title="State-of-the-Art Multimodal RAG System",
        url="https://huggingface.co/papers/2601.00002",
        authors=["Carol Lee"],
        abstract="A scalable retrieval augmented generation system for multimodal data. " * 15,
        published_date=date(2026, 2, 26),
        raw_metadata={"upvotes": 25, "arxiv_id": "2601.00002"},
    )


@pytest.fixture
def github_item() -> ContentItem:
    return ContentItem(
        source=SourceType.GITHUB,
        source_name="GitHub Trending",
        title="awesome-ai-agents",
        url="https://github.com/user/awesome-ai-agents",
        authors=[],
        abstract="A curated list of AI agents and tools.",
        published_date=date(2026, 2, 26),
        raw_metadata={"stars_today": 150},
    )


@pytest.fixture
def rss_item() -> ContentItem:
    return ContentItem(
        source=SourceType.RSS,
        source_name="TechCrunch AI",
        title="OpenAI launches new reasoning model",
        url="https://techcrunch.com/2026/02/26/openai-model",
        authors=["Reporter Name"],
        abstract="OpenAI today announced a new reasoning model surpassing existing benchmarks.",
        published_date=date(2026, 2, 26),
        organization="OpenAI",
    )


@pytest.fixture
def scored_item(arxiv_item) -> ScoredItem:
    return ScoredItem(
        item=arxiv_item,
        rule_score=45.0,
        rule_reasons=["🏢 頂流機構: Google", "🔥 熱門關鍵字: agent, reasoning"],
        llm_score=75.0,
        llm_reason="創新的 agent 推理框架，高部落格價值",
        novelty=17.0,
        impact=16.0,
        trending=15.0,
        practicality=14.0,
        blog_worthiness=13.0,
    )
