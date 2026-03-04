"""Pydantic data models for the auto_post_blog pipeline."""

from __future__ import annotations

from datetime import date, datetime
from enum import Enum
from typing import Any

from pydantic import BaseModel, Field, model_validator


class SourceType(str, Enum):
    ARXIV = "arxiv"
    CHATPAPER = "chatpaper"
    HF_PAPERS = "hf_papers"
    RSS = "rss"
    BLOG = "blog"
    GITHUB = "github"
    HACKERNEWS = "hackernews"
    REDDIT = "reddit"
    NEWSAPI = "newsapi"


class ContentItem(BaseModel):
    """統一的內容條目，所有 collector 產出都轉換成這個格式。"""

    source: SourceType
    source_name: str = ""  # e.g. "TechCrunch AI", "arXiv"
    title: str
    url: str
    authors: list[str] = Field(default_factory=list)
    abstract: str = ""
    published_date: date
    tags: list[str] = Field(default_factory=list)
    organization: str = ""
    raw_metadata: dict = Field(default_factory=dict)

    def dedup_key(self) -> str:
        """用於去重的 key: 優先用 arxiv id, 否則用 URL."""
        arxiv_id = self.raw_metadata.get("arxiv_id", "")
        if arxiv_id:
            return f"arxiv:{arxiv_id}"
        return self.url


class ScoredItem(BaseModel):
    """篩選後帶評分的條目。"""

    item: ContentItem
    rule_score: float = 0.0
    rule_reasons: list[str] = Field(default_factory=list)

    # LLM 評分 (只有通過 rule 預篩的才有)
    llm_score: float | None = None
    llm_reason: str = ""
    novelty: float | None = None
    impact: float | None = None
    trending: float | None = None      # 話題性（舊欄位名: relevance）
    practicality: float | None = None  # 實用性
    blog_worthiness: float | None = None

    @model_validator(mode="before")
    @classmethod
    def _migrate_relevance(cls, data: Any) -> Any:
        """向後相容：將舊版 JSON 中的 relevance 欄位對應到 trending。"""
        if isinstance(data, dict) and "relevance" in data and "trending" not in data:
            data = dict(data)
            data["trending"] = data.pop("relevance")
        return data

    @property
    def total_score(self) -> float:
        if self.llm_score is not None:
            return self.rule_score + self.llm_score
        return self.rule_score


class GeneratedContent(BaseModel):
    """生成的內容 (blog post 或 note)."""

    source_item: ScoredItem
    content: str
    prompt_used: str  # 保存完整 prompt，未來可重新呼叫
    model_used: str
    generated_at: datetime = Field(default_factory=datetime.now)
    content_type: str = "blog_post"  # "blog_post" | "note"
