"""雙模式日誌：Rich（CLI）vs JSON lines（背景執行）。

用法：
    from src.logger import get_logger, setup_logging
    setup_logging()                    # CLI 入口呼叫一次
    logger = get_logger("collectors")  # 回傳 autopb.collectors logger
"""
from __future__ import annotations

import logging
import os
from datetime import datetime
from zoneinfo import ZoneInfo
from typing import Any


class JsonFormatter(logging.Formatter):
    """LogRecord → single-line JSON。"""

    _BUILTIN_ATTRS = frozenset({
        "name", "msg", "args", "levelname", "levelno", "pathname",
        "filename", "module", "exc_info", "exc_text", "stack_info",
        "lineno", "funcName", "created", "msecs", "relativeCreated",
        "thread", "threadName", "processName", "process", "message",
        "taskName",
    })

    def format(self, record: logging.LogRecord) -> str:
        import json
        import traceback

        record.message = record.getMessage()
        payload: dict[str, Any] = {
            "ts": datetime.fromtimestamp(record.created, tz=ZoneInfo("Asia/Taipei")).isoformat(),
            "level": record.levelname,
            "logger": record.name,
            "msg": record.message,
        }
        for key, val in record.__dict__.items():
            if key not in self._BUILTIN_ATTRS:
                payload[key] = val
        if record.exc_info:
            payload["exc"] = "".join(
                traceback.format_exception(*record.exc_info)
            ).rstrip()
        return json.dumps(payload, ensure_ascii=False, default=str)


def setup_logging(json_mode: bool | None = None) -> None:
    """初始化 autopb root logger（冪等）。

    Args:
        json_mode: True=JSON，False=Rich，None=從 AUTOPB_LOG_FORMAT env 偵測。
    """
    from rich.logging import RichHandler

    if json_mode is None:
        json_mode = os.environ.get("AUTOPB_LOG_FORMAT", "").lower() == "json"

    root = logging.getLogger("autopb")

    if root.handlers:
        existing_is_json = isinstance(
            getattr(root.handlers[0], "formatter", None), JsonFormatter
        )
        if existing_is_json == json_mode:
            return
        root.handlers.clear()

    root.setLevel(logging.DEBUG)

    if json_mode:
        handler = logging.StreamHandler()
        handler.setFormatter(JsonFormatter())
    else:
        handler = RichHandler(rich_tracebacks=True, show_path=False, markup=False)

    root.addHandler(handler)


def get_logger(name: str) -> logging.Logger:
    """回傳 autopb.{name} logger。"""
    return logging.getLogger(f"autopb.{name}")
