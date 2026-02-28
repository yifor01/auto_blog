"""Rule-based pre-scoring for fast filtering."""

from __future__ import annotations

import re

from src.models import ContentItem, ScoredItem
from src.logger import get_logger
from src.utils import load_config

_logger = get_logger("scoring.rules")


def _match_institution(inst: str, org: str, authors_str: str) -> bool:
    """機構名稱比對：優先精確比對 organization 欄位，再用 word boundary 比對作者串。

    使用 word boundary 避免 "google" 匹配到 "Googlemorphic" 或人名中含此字串的誤判。
    """
    inst_lower = inst.lower()
    # 優先比對 organization 欄位（最可靠）
    if inst_lower in org.lower():
        return True
    # 用 word boundary 比對作者名串
    pattern = r"\b" + re.escape(inst_lower) + r"\b"
    return bool(re.search(pattern, authors_str.lower()))


def rule_score(item: ContentItem, config: dict | None = None) -> ScoredItem:
    """對單個 ContentItem 進行 rule-based 評分。"""
    if config is None:
        config = load_config()

    scoring_cfg = config.get("scoring", {})
    top_institutions = scoring_cfg.get("top_institutions", [])
    hot_keywords = [k.lower() for k in scoring_cfg.get("hot_keywords", [])]

    # 從 config 讀取門檻值（有預設值保持向後相容）
    hf_upvote_threshold = scoring_cfg.get("hf_upvote_bonus_threshold", 10)
    github_stars_high = scoring_cfg.get("github_stars_high", 100)
    github_stars_medium = scoring_cfg.get("github_stars_medium", 50)

    score = 0.0
    reasons: list[str] = []

    # 1. 頂流機構加分
    org = item.organization
    authors_str = " ".join(item.authors)
    for inst in top_institutions:
        if _match_institution(inst, org, authors_str):
            score += 20
            reasons.append(f"🏢 頂流機構: {inst}")
            break  # 只加一次

    # 2. 熱門關鍵字加分
    text = f"{item.title} {item.abstract}".lower()
    matched_kw = [kw for kw in hot_keywords if kw in text]
    if matched_kw:
        kw_score = min(len(matched_kw) * 5, 15)  # 每個 +5, 上限 15
        score += kw_score
        reasons.append(f"🔥 熱門關鍵字: {', '.join(matched_kw[:5])}")

    # 3. HF Daily Papers 收錄加分
    if item.source.value == "hf_papers":
        score += 15
        reasons.append("⭐ HuggingFace Daily Papers 收錄")
        upvotes = item.raw_metadata.get("upvotes", 0)
        if upvotes > hf_upvote_threshold:
            score += 10
            reasons.append(f"👍 HF upvotes: {upvotes}")

    # 4. GitHub stars 加分
    if item.source.value == "github":
        stars = item.raw_metadata.get("stars_today", 0)
        if stars > github_stars_high:
            score += 15
            reasons.append(f"⭐ GitHub stars today: {stars}")
        elif stars > github_stars_medium:
            score += 10
            reasons.append(f"⭐ GitHub stars today: {stars}")

    # 5. Hacker News points 加分
    if item.source.value == "hackernews":
        hn_points = item.raw_metadata.get("points", 0)
        if hn_points > 300:
            score += 15
            reasons.append(f"🔥 HN 高分: {hn_points} points")
        elif hn_points > 100:
            score += 10
            reasons.append(f"⬆️ HN 熱門: {hn_points} points")
        else:
            score += 5
            reasons.append(f"📰 Hacker News: {hn_points} points")

    # 6. 來源類型保底加分
    # 為了讓文章、新聞來源不容易被論文海淹沒，給予基礎加分
    if item.source.value in ("rss", "blog"):
        score += 15
        reasons.append("📰 文章/新聞來源加分")
    elif item.source.value == "chatpaper":
        score += 5
        reasons.append("📄 ChatPaper 收錄")

    # 7. 標題品質加分 (有數字、比較、新方法等訊號)
    title_lower = item.title.lower()
    novelty_signals = [
        "novel", "new", "first", "state-of-the-art", "sota",
        "surpass", "outperform", "efficient", "scalable",
        "beyond", "rethinking", "revisiting",
    ]
    if any(sig in title_lower for sig in novelty_signals):
        score += 5
        reasons.append("💡 標題含新穎性訊號")

    # 8. 摘要長度品質 (太短可能是低質量)
    if len(item.abstract) > 500:
        score += 3
    elif len(item.abstract) < 50 and item.source.value not in ("github", "blog"):
        score -= 5
        reasons.append("⚠️ 摘要過短")

    return ScoredItem(
        item=item,
        rule_score=max(score, 0),
        rule_reasons=reasons,
    )


def batch_rule_score(
    items: list[ContentItem],
    config: dict | None = None,
) -> list[ScoredItem]:
    """批量 rule-based 評分並排序。"""
    if config is None:
        config = load_config()

    scored = [rule_score(item, config) for item in items]
    scored.sort(key=lambda x: x.rule_score, reverse=True)

    threshold = config.get("scoring", {}).get("rule_threshold", 25)
    passed = [s for s in scored if s.rule_score >= threshold]
    _logger.info("Rule scoring complete", extra={"total": len(items), "passed": len(passed), "threshold": threshold})
    return passed
