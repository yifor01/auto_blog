"""slugify() 測試：特殊字元分隔、黏字 bug、截斷不留殘字、中文保留。"""

from __future__ import annotations

from src.utils import slugify


class TestSlugify:
    def test_slash_becomes_dash_not_glued(self):
        """`/` 應轉成分隔符 `-`，而非直接刪除導致黏字。"""
        assert slugify("memvid/memvid") == "memvid-memvid"

    def test_dot_and_slash_org_repo(self):
        assert slugify("onyx-dot-app/onyx") == "onyx-dot-app-onyx"

    def test_ellipsis_and_slash(self):
        """`aaif/goose…goose` 不應黏成 aaif-goosegoose。"""
        assert slugify("aaif/goose…goose") == "aaif-goose-goose"

    def test_collapses_consecutive_dashes(self):
        assert slugify("a // b -- c") == "a-b-c"

    def test_strips_leading_trailing_dashes(self):
        assert slugify("--hello--") == "hello"

    def test_underscore_becomes_dash(self):
        assert slugify("foo_bar_baz") == "foo-bar-baz"

    def test_truncate_no_partial_word(self):
        """超長標題截斷後不應留下殘字（如 world-modeli）。"""
        title = "A Frame Is Worth One Token Efficient Generative World Modeling"
        result = slugify(title, max_len=60)
        assert len(result) <= 60
        # 退回最後一個完整單字，不以殘字結尾
        assert not result.endswith("-")
        assert result.split("-")[-1] in title.lower().split()
        assert "modeli" not in result.split("-")

    def test_truncate_at_word_boundary_keeps_word(self):
        """切點剛好在分隔符時，前一個完整單字應保留。"""
        # "abc-def-ghi" max_len=7 -> "abc-def"（位置 7 是 '-'）
        assert slugify("abc-def-ghi", max_len=7) == "abc-def"

    def test_empty_input_fallback(self):
        assert slugify("") == "untitled"

    def test_all_special_chars_fallback(self):
        assert slugify("///...___") == "untitled"

    def test_chinese_preserved(self):
        """中文（unicode 單字字元）應保留，維持既有行為。"""
        assert slugify("深度學習模型") == "深度學習模型"

    def test_lowercases(self):
        assert slugify("Hello World") == "hello-world"
