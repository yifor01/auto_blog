"""src/logger.py 雙模式日誌基礎設施測試。"""
from __future__ import annotations
import json
import logging
import os
import re
from io import StringIO
from unittest.mock import patch

import pytest

# 此時 src/logger.py 尚不存在，測試應 fail with ImportError


class TestJsonFormatter:
    def _make_record(self, msg, level=logging.INFO, **kwargs):
        from src.logger import JsonFormatter

        r = logging.LogRecord(
            name="autopb.test",
            level=level,
            pathname="test.py",
            lineno=1,
            msg=msg,
            args=(),
            exc_info=None,
        )
        for k, v in kwargs.items():
            setattr(r, k, v)
        return r

    def test_output_is_valid_json(self):
        from src.logger import JsonFormatter

        assert json.loads(JsonFormatter().format(self._make_record("hello"))) is not None

    def test_required_fields(self):
        from src.logger import JsonFormatter

        parsed = json.loads(JsonFormatter().format(self._make_record("x")))
        assert {"ts", "level", "logger", "msg"} <= parsed.keys()

    def test_level_is_string(self):
        from src.logger import JsonFormatter

        parsed = json.loads(
            JsonFormatter().format(self._make_record("w", level=logging.WARNING))
        )
        assert parsed["level"] == "WARNING"

    def test_extra_fields_included(self):
        from src.logger import JsonFormatter

        r = self._make_record("x")
        r.collector = "arxiv"
        r.count = 42
        parsed = json.loads(JsonFormatter().format(r))
        assert parsed.get("collector") == "arxiv"
        assert parsed.get("count") == 42

    def test_ts_is_iso_format(self):
        from src.logger import JsonFormatter

        parsed = json.loads(JsonFormatter().format(self._make_record("x")))
        assert re.match(r"\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}", parsed["ts"])

    def test_exception_included(self):
        from src.logger import JsonFormatter

        try:
            raise ValueError("test")
        except ValueError:
            import sys

            r = logging.LogRecord(
                name="autopb.test",
                level=logging.ERROR,
                pathname="t.py",
                lineno=1,
                msg="fail",
                args=(),
                exc_info=sys.exc_info(),
            )
        parsed = json.loads(JsonFormatter().format(r))
        assert "exc" in parsed and "ValueError" in parsed["exc"]


class TestSetupLogging:
    def test_json_mode_via_env(self):
        from src.logger import JsonFormatter, setup_logging

        root = logging.getLogger("autopb")
        root.handlers.clear()
        with patch.dict(os.environ, {"AUTOPB_LOG_FORMAT": "json"}):
            setup_logging()
        assert isinstance(root.handlers[0].formatter, JsonFormatter)

    def test_rich_mode_explicit(self):
        from rich.logging import RichHandler

        from src.logger import setup_logging

        root = logging.getLogger("autopb")
        root.handlers.clear()
        setup_logging(json_mode=False)
        assert isinstance(root.handlers[0], RichHandler)

    def test_json_mode_explicit(self):
        from src.logger import JsonFormatter, setup_logging

        root = logging.getLogger("autopb")
        root.handlers.clear()
        setup_logging(json_mode=True)
        assert isinstance(root.handlers[0].formatter, JsonFormatter)

    def test_idempotent(self):
        from src.logger import setup_logging

        root = logging.getLogger("autopb")
        root.handlers.clear()
        setup_logging(json_mode=True)
        setup_logging(json_mode=True)
        assert len(root.handlers) == 1


class TestGetLogger:
    def test_namespace(self):
        from src.logger import get_logger

        assert get_logger("scoring").name == "autopb.scoring"

    def test_same_name_same_instance(self):
        from src.logger import get_logger

        assert get_logger("utils") is get_logger("utils")


class TestJsonOutputIntegration:
    def test_json_log_lines_parseable(self):
        from src.logger import JsonFormatter, get_logger

        stream = StringIO()
        h = logging.StreamHandler(stream)
        h.setFormatter(JsonFormatter())
        lg = logging.getLogger("autopb._test")
        lg.handlers.clear()
        lg.addHandler(h)
        lg.setLevel(logging.DEBUG)
        lg.propagate = False
        lg.info("done", extra={"count": 5})
        lg.warning("slow", extra={"wait": 10})
        stream.seek(0)
        for line in stream.readlines():
            line = line.strip()
            if line:
                p = json.loads(line)
                assert "ts" in p and "level" in p and "msg" in p
