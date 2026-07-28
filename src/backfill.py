"""隔日補票：回頭更新 HF 論文的 upvotes 並重建當日清單排序。

HF 論文在發布當天票數幾乎還沒累積（pipeline 跑在台灣時間凌晨 2 點，
論文往往剛上架幾小時），拿當下的票數排序等於用雜訊排序。
隔天再抓一次列表頁即可拿到已經沉澱的票數，成本是每天多打 HF 一次請求。

只動 upvotes 一個欄位：raw 的 `raw_metadata.upvotes` 與 `output/lists/{date}.json`
的 hf 排序，其餘內容（abstract / 標題 / 其他來源）完全不碰。
"""

from __future__ import annotations

import os
from datetime import date, timedelta

from src.collectors.hf_papers import fetch_upvotes
from src.lists import build_day_lists, get_lists_path
from src.logger import get_logger
from src.models import ContentItem, SourceType
from src.utils import RAW_DIR, console, load_json, save_json

_logger = get_logger("backfill")


def get_raw_path(d: date):
    return RAW_DIR / f"{d.isoformat()}.json"


def backfill_hf_upvotes(target_date: date, quiet: bool = False) -> dict:
    """回補某日 HF 論文票數，更新 raw 並重建 lists。

    回傳統計 dict（updated / changed / max_delta），沒有可回補的資料時
    各項為 0——呼叫端不需要處理例外，任何失敗都只是「這次沒補到」。
    """
    stats = {"date": target_date.isoformat(), "updated": 0, "changed": 0, "max_delta": 0}

    # 安全網：測試裡若有人不小心走到這條路徑，會打真實 HF 並改寫真實 data/raw
    # （run_pipeline 的自動回補就踩過一次），因此在 pytest 下直接不動作
    if os.environ.get("PYTEST_CURRENT_TEST") and not os.environ.get("AUTOPB_ALLOW_BACKFILL_IN_TESTS"):
        return stats

    raw_path = get_raw_path(target_date)
    if not raw_path.exists():
        _logger.info("Backfill skipped: no raw data", extra={"date": str(target_date)})
        return stats

    raw_data = load_json(raw_path)
    if not raw_data:
        return stats

    items = [ContentItem(**it) for it in raw_data]
    hf_items = [it for it in items if it.source == SourceType.HF_PAPERS]
    if not hf_items:
        _logger.info("Backfill skipped: no HF items", extra={"date": str(target_date)})
        return stats

    votes = fetch_upvotes(target_date)
    if not votes:
        _logger.warning("Backfill skipped: no votes fetched", extra={"date": str(target_date)})
        return stats

    for it in hf_items:
        # raw_metadata 裡的 hf_url 才是原始論文頁網址（url 欄位同值，但 hf_url 更明確）
        key = it.raw_metadata.get("hf_url") or it.url
        if key not in votes:
            continue
        old = int(it.raw_metadata.get("upvotes") or 0)
        new = votes[key]
        stats["updated"] += 1
        if new != old:
            it.raw_metadata["upvotes"] = new
            stats["changed"] += 1
            stats["max_delta"] = max(stats["max_delta"], new - old)

    if stats["changed"] == 0:
        _logger.info("Backfill: no vote changes", extra={"date": str(target_date), "checked": stats["updated"]})
        return stats

    save_json([it.model_dump() for it in items], raw_path)

    # lists 的 hf 段是依 upvotes 排序後截斷的，票數變了就得整段重建
    lists_path = get_lists_path(target_date)
    if lists_path.exists():
        save_json(build_day_lists(items, target_date), lists_path)

    _logger.info(
        "Backfill complete",
        extra={
            "date": str(target_date),
            "updated": stats["updated"],
            "changed": stats["changed"],
            "max_delta": stats["max_delta"],
        },
    )
    if not quiet:
        console.print(
            f"🔁 補票 {target_date}: {stats['changed']}/{stats['updated']} 篇票數更新"
            f"（最大 +{stats['max_delta']}），清單已重排"
        )
    return stats


def backfill_recent(reference_date: date, days: int = 1, quiet: bool = False) -> list[dict]:
    """回補 reference_date 之前 days 天的票數（days=1 就是只補前一天）。"""
    return [
        backfill_hf_upvotes(reference_date - timedelta(days=offset), quiet=quiet)
        for offset in range(1, days + 1)
    ]
