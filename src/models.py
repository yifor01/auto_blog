"""Pydantic data models for the auto_post_blog pipeline."""

from __future__ import annotations

import re
from datetime import date, datetime
from enum import Enum
from typing import Any

from pydantic import BaseModel, Field, field_validator, model_validator


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
    SEMANTIC_SCHOLAR = "semantic_scholar"


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

    @field_validator("title", "abstract")
    @classmethod
    def _normalize_to_traditional(cls, v: str) -> str:
        """Layer A：來源端簡→繁。量子位 / ChatPaper 等中國 source 的簡體
        title/abstract 在建構時就轉繁，一改全下游受惠（raw/scored JSON、
        blog frontmatter title、digest、web UI）。對英文/繁中為冪等。"""
        # 區域 import 避免 utils <-> models 潛在循環依賴
        from src.utils import to_traditional

        return to_traditional(v)

    @field_validator("tags")
    @classmethod
    def _normalize_tags_to_traditional(cls, v: list[str]) -> list[str]:
        """tags 同樣走 Layer A。漏掉這個，網站的 tag chip 會直接顯示
        簡體（资讯 / 开源 / 科大讯飞），且 tag 篩選會把簡繁當成兩個不同標籤。"""
        from src.utils import to_traditional

        return [to_traditional(t) for t in v]

    def dedup_key(self) -> str:
        """用於去重的 key: 優先用 arxiv id, 否則用正規化後的 URL."""
        arxiv_id = self.raw_metadata.get("arxiv_id", "")
        if arxiv_id:
            # 去掉版本後綴（2606.11190v1 → 2606.11190），
            # 讓 arxiv / hf_papers / semantic_scholar 三來源的同篇論文能互相去重
            canonical = re.sub(r"v\d+$", "", arxiv_id)
            return f"arxiv:{canonical}"
        # 區域 import 避免 utils <-> models 潛在循環依賴
        from src.utils import normalize_url

        return normalize_url(self.url)


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
