"""Reddit collector using public JSON endpoints."""

from __future__ import annotations

import time
from datetime import date, datetime
from zoneinfo import ZoneInfo

from src.collectors.base import BaseCollector
from src.logger import get_logger
from src.models import ContentItem, SourceType
from src.utils import build_link_abstract, get_http_client, load_config

_logger = get_logger("collectors.reddit")

TZ_TPE = ZoneInfo("Asia/Taipei")


class RedditCollector(BaseCollector):
    name = "reddit"

    def collect(self, target_date: date | None = None) -> list[ContentItem]:
        config = load_config()
        cfg = config.get("collectors", {}).get("reddit", {})
        if not cfg.get("enabled", True):
            return []

        target_date = target_date or date.today()
        subreddits: list[str] = cfg.get("subreddits", ["LocalLLaMA", "MachineLearning"])
        min_upvotes: int = cfg.get("min_upvotes", 50)
        max_results: int = cfg.get("max_results", 30)
        time_filter: str = cfg.get("time_filter", "day")

        # 計算目標日期的時間範圍（台灣時區）
        start_dt = datetime(target_date.year, target_date.month, target_date.day, tzinfo=TZ_TPE)
        start_ts = start_dt.timestamp()
        end_ts = start_ts + 86400

        items: list[ContentItem] = []
        seen_ids: set[str] = set()
        client = get_http_client()

        try:
            for i, sub in enumerate(subreddits):
                if i > 0:
                    time.sleep(2.0)

                try:
                    url = f"https://old.reddit.com/r/{sub}/top/.json"
                    resp = client.get(
                        url,
                        params={"t": time_filter, "limit": 100},
                        headers={"User-Agent": "Mozilla/5.0 (compatible; autopb/1.0)"},
                    )
                    resp.raise_for_status()
                    data = resp.json()
                except Exception as e:
                    _logger.warning("Reddit fetch error", extra={"subreddit": sub, "error": str(e)})
                    continue

                for child in data.get("data", {}).get("children", []):
                    post = child.get("data", {})
                    post_id = post.get("id", "")
                    if post_id in seen_ids:
                        continue
                    seen_ids.add(post_id)

                    score = post.get("score", 0)
                    if score < min_upvotes:
                        continue

                    # 日期過濾：created_utc → 台灣時區
                    created_utc = post.get("created_utc", 0)
                    if not (start_ts <= created_utc < end_ts):
                        continue

                    title = post.get("title", "")
                    if not title:
                        continue

                    post_url = post.get("url", "")
                    reddit_url = f"https://www.reddit.com{post.get('permalink', '')}"
                    # self post 用 reddit URL，link post 用原始 URL
                    is_self = post.get("is_self", False)
                    final_url = reddit_url if is_self else (post_url or reddit_url)

                    num_comments = post.get("num_comments", 0)
                    selftext = (post.get("selftext") or "").strip()

                    if selftext:
                        abstract = selftext[:500]
                    elif not is_self:
                        engagement = f"{score} upvotes, {num_comments} comments on r/{sub}"
                        domain = post.get("domain", "reddit.com")
                        abstract = build_link_abstract(final_url, client, engagement, domain)
                    else:
                        abstract = f"reddit.com — {score} upvotes, {num_comments} comments on r/{sub}"

                    items.append(
                        ContentItem(
                            source=SourceType.REDDIT,
                            source_name=f"r/{sub}",
                            title=title,
                            url=final_url,
                            authors=[post.get("author", "")],
                            abstract=abstract,
                            published_date=target_date,
                            tags=["reddit", sub.lower()],
                            raw_metadata={
                                "score": score,
                                "num_comments": num_comments,
                                "subreddit": sub,
                                "reddit_url": reddit_url,
                                "post_id": post_id,
                            },
                        )
                    )

                    if len(items) >= max_results:
                        break

                if len(items) >= max_results:
                    break
        except Exception as e:
            _logger.error("Reddit collection error", extra={"error": str(e)})
        finally:
            client.close()

        _logger.info("Reddit collection complete", extra={"count": len(items)})
        return items
