"""Shared helper utilities for collectors."""

from __future__ import annotations

from datetime import date
from email.utils import parsedate_to_datetime


def parse_entry_date(entry) -> date | None:
    """Parse the publication date from a feedparser entry.

    Tries published, updated, and created fields in that order,
    using both the raw string value and the pre-parsed tuple.
    Returns None if no date can be parsed.
    """
    for field in ("published", "updated", "created"):
        val = entry.get(field)
        if val:
            try:
                return parsedate_to_datetime(val).date()
            except Exception:
                pass
        parsed = entry.get(f"{field}_parsed")
        if parsed:
            try:
                return date(*parsed[:3])
            except Exception:
                pass
    return None
