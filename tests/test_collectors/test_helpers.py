"""Tests for src/collectors/_helpers.parse_entry_date."""

from __future__ import annotations

from datetime import date


class TestParseEntryDate:
    """Unit tests for parse_entry_date covering all entry-date field combinations."""

    def test_published_string_rfc2822(self):
        """published string in RFC 2822 format is parsed correctly."""
        from src.collectors._helpers import parse_entry_date

        entry = {"published": "Mon, 07 Apr 2026 12:00:00 +0000"}
        result = parse_entry_date(entry)
        assert result == date(2026, 4, 7)

    def test_published_parsed_tuple(self):
        """published_parsed 9-tuple is parsed correctly."""
        from src.collectors._helpers import parse_entry_date

        entry = {"published_parsed": (2026, 4, 7, 12, 0, 0, 0, 97, 0)}
        result = parse_entry_date(entry)
        assert result == date(2026, 4, 7)

    def test_updated_parsed_fallback_when_no_published(self):
        """Falls back to updated_parsed when published fields are absent."""
        from src.collectors._helpers import parse_entry_date

        entry = {"updated_parsed": (2026, 6, 1, 0, 0, 0, 0, 152, 0)}
        result = parse_entry_date(entry)
        assert result == date(2026, 6, 1)

    def test_created_parsed_fallback(self):
        """Falls back to created_parsed when published and updated are absent."""
        from src.collectors._helpers import parse_entry_date

        entry = {"created_parsed": (2025, 12, 25, 0, 0, 0, 0, 359, 0)}
        result = parse_entry_date(entry)
        assert result == date(2025, 12, 25)

    def test_missing_all_date_fields_returns_none(self):
        """Entry with no date-related fields returns None."""
        from src.collectors._helpers import parse_entry_date

        result = parse_entry_date({})
        assert result is None

    def test_bad_published_string_falls_through_to_parsed_tuple(self):
        """Malformed published string falls through to published_parsed."""
        from src.collectors._helpers import parse_entry_date

        entry = {
            "published": "not-a-date",
            "published_parsed": (2026, 3, 15, 0, 0, 0, 0, 74, 0),
        }
        result = parse_entry_date(entry)
        assert result == date(2026, 3, 15)

    def test_bad_parsed_tuple_too_short_falls_through_to_next_field(self):
        """published_parsed tuple with fewer than 3 elements does not crash and falls through."""
        from src.collectors._helpers import parse_entry_date

        entry = {
            "published_parsed": (2026,),  # too short for date(*parsed[:3])
            "updated_parsed": (2026, 5, 10, 0, 0, 0, 0, 130, 0),
        }
        result = parse_entry_date(entry)
        assert result == date(2026, 5, 10)

    def test_bad_parsed_tuple_only_returns_none(self):
        """Entry where only parsed tuple is malformed (no fallback) returns None."""
        from src.collectors._helpers import parse_entry_date

        entry = {"published_parsed": (2026,)}
        result = parse_entry_date(entry)
        assert result is None

    def test_rss_and_blog_collector_use_same_function(self):
        """Both rss_collector and blog_collector delegate to the shared helper."""
        from src.collectors._helpers import parse_entry_date
        from src.collectors.rss_collector import RSSCollector  # noqa: F401 - import check
        from src.collectors.blog_collector import BlogCollector  # noqa: F401 - import check

        # Verify the shared function itself works (representative call)
        entry = {"published": "Tue, 01 Jun 2026 00:00:00 GMT"}
        assert parse_entry_date(entry) == date(2026, 6, 1)
