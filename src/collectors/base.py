"""Base collector interface."""

from __future__ import annotations

from abc import ABC, abstractmethod
from datetime import date

from src.models import ContentItem


class BaseCollector(ABC):
    """所有 collector 的抽象基底類。"""

    name: str = "base"

    @abstractmethod
    def collect(self, target_date: date | None = None) -> list[ContentItem]:
        """收集指定日期的內容。None 表示今天。"""
        ...

    def __repr__(self) -> str:
        return f"<{self.__class__.__name__}>"
