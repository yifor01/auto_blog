"""Pydantic data models for the auto_post_blog pipeline."""

from __future__ import annotations

import html
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
        """Layer A：來源端 HTML entity 解碼 + 簡→繁。量子位 / ChatPaper 等
        中國 source 的簡體 title/abstract 在建構時就轉繁，一改全下游受惠
        （raw/scored JSON、blog frontmatter title、digest、web UI）。
        對英文/繁中為冪等。

        why 先 unescape 再轉繁：&#8217; 解碼後是 ASCII 標點，OpenCC 不動它；
        反過來則是拿未解碼的髒字串餵 OpenCC。RSS 有 58 筆 title、
        hackernews 有 269 筆 abstract 帶著未解碼 entity。
        """
        # 區域 import 避免 utils <-> models 潛在循環依賴
        from src.utils import to_traditional

        return to_traditional(html.unescape(v))

    @field_validator("tags")
    @classmethod
    def _normalize_tags_to_traditional(cls, v: list[str]) -> list[str]:
        """tags 同樣走 Layer A。漏掉這個，網站的 tag chip 會直接顯示
        簡體（资讯 / 开源 / 科大讯飞），且 tag 篩選會把簡繁當成兩個不同標籤。"""
        from src.utils import to_traditional

        return [to_traditional(html.unescape(t)) for t in v]

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


# Layer A validator 會改寫的欄位——從既有存檔重建時要還原成存檔原值
_LAYER_A_FIELDS = ("title", "abstract", "tags")


def item_from_raw(raw: dict) -> ContentItem:
    """從 `data/raw` 的既有 dict 重建 ContentItem，且**不重複套用 Layer A**。

    why：存檔裡的 title / abstract / tags 已經是 Layer A 的成品，而 s2twp 對繁體
    刻意不冪等（「這個文件的參數」→「這個檔案的參數」）。直接 `ContentItem(**raw)`
    等於再套一次，於是每讀一次就漂一格。寫回 raw 的路徑固然要防（backfill /
    supplement 已改成保留原始 dict），但只要拿這些 item 產出**任何**檔案就一樣會把
    漂移寫進成品——`build_day_lists()` 就是這樣讓 `output/lists` 與 `data/raw`
    出現落差的（實測近 40 天清單型來源 3375 筆中 34 筆非冪等，約 1%），而詳情頁的
    「原始資料 box」直接讀 `data/raw`，兩處並列時同一段文字會顯示不一致。

    why 先完整建構再賦值、而不是 `model_construct()`：後者跳過**所有**驗證含型別
    轉換，`published_date` 會停在 str，`_other_entry()` 的 `.isoformat()` 當場
    AttributeError（已實測）。這裡走完整驗證拿到正確型別，之後才把 Layer A 覆寫過的
    欄位還原——`ContentItem` 沒有開 `validate_assignment`（Pydantic v2 預設關閉），
    賦值不會再次觸發 validator。日後若替 `ContentItem` 加上 `validate_assignment`，
    這個還原會靜默失效，屆時必須改走別的還原手段。

    附帶取捨：還原也跳過了 Layer A 的 `html.unescape()`。這是對的——存檔值本來就
    是已解碼的成品，讀取端的職責是**無損還原**而非二次清洗；歷史髒資料由
    `repair-content` 負責（`data/raw` 的 entity 已於該指令實跑後歸零）。
    """
    item = ContentItem(**raw)
    for field in _LAYER_A_FIELDS:
        if field not in raw:
            continue
        value = raw[field]
        # list 要複製再塞：直接指派是 aliasing，而 backfill / supplement 正好把
        # 同一份 raw dict 當寫回 payload——日後任何原地改 item.tags 的程式碼都會
        # 靜默寫壞 data/raw。字串不可比照辦理（list("abc") 會拆成字元）。
        setattr(item, field, list(value) if isinstance(value, list) else value)
    return item


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
