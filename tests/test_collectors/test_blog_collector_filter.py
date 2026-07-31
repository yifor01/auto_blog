"""Tests for BlogCollector._is_valid_blog_entry filter."""
import pytest
from src.collectors.blog_collector import BlogCollector


class TestIsValidBlogEntry:
    def test_rss_feed_title_filtered(self):
        """title 含 'rss feed' 應被過濾。"""
        assert BlogCollector._is_valid_blog_entry(
            title="RSS Feed (Blog and Notes)",
            url="https://example.com/posts",
            abstract="Some abstract here.",
        ) is False

    def test_subscribe_title_filtered(self):
        """title 含 'subscribe' 應被過濾。"""
        assert BlogCollector._is_valid_blog_entry(
            title="Subscribe via Email",
            url="https://example.com/subscribe",
            abstract="Sign up for updates.",
        ) is False

    def test_feed_url_filtered(self):
        """URL 最後一段為 'feed' 應被過濾。"""
        assert BlogCollector._is_valid_blog_entry(
            title="Latest Articles",
            url="https://example.com/feed",
            abstract="A real abstract.",
        ) is False

    def test_empty_abstract_filtered(self):
        """abstract 為空應被過濾。"""
        assert BlogCollector._is_valid_blog_entry(
            title="A Valid Article Title",
            url="https://example.com/2024/article",
            abstract="",
        ) is False

    def test_valid_article_passes(self):
        """正常文章應通過。"""
        assert BlogCollector._is_valid_blog_entry(
            title="Understanding Transformer Architecture",
            url="https://example.com/2024/transformer",
            abstract="This article explains the transformer model in detail...",
        ) is True

    def test_empty_url_filtered(self):
        """URL 為空應被過濾（無法追蹤來源）。"""
        assert BlogCollector._is_valid_blog_entry(
            title="A Valid Article Title",
            url="",
            abstract="A proper abstract with enough content.",
        ) is False

    def test_feed_word_in_path_middle_passes(self):
        """URL 路徑中間含 'feed' 字詞但非最後一段，應通過（防誤殺）。"""
        assert BlogCollector._is_valid_blog_entry(
            title="Feed-Forward Networks Explained",
            url="https://example.com/2024/feed-forward-network",
            abstract="Deep dive into feed-forward neural network layers...",
        ) is True
