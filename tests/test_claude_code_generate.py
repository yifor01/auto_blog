"""claude_code_generate 測試（全 mock subprocess，不得真的叫起 CLI）。

這一支是批次生成走的 subprocess 路徑，與 llm_chat 完全分離：它沒有 model chain、
沒有 key 輪替、沒有 retire，失敗一律回 "" 讓上層 fallback 回 OpenRouter 逐篇生成。
"""
import json
import subprocess
from unittest.mock import patch

from src.utils import claude_code_generate


def _completed(stdout: str, returncode: int = 0):
    return subprocess.CompletedProcess(args=["claude"], returncode=returncode, stdout=stdout, stderr="")


def _payload(result: str, **extra):
    return json.dumps({"result": result, "total_cost_usd": 0.4, "usage": {"output_tokens": 100}, **extra})


class TestSuccess:
    def test_returns_result_field(self):
        with patch("subprocess.run", return_value=_completed(_payload("===POST 1===\n📌 標題"))):
            assert claude_code_generate("prompt") == "===POST 1===\n📌 標題"

    def test_prompt_goes_through_stdin_not_argv(self):
        """prompt 有 3 萬字元且含 shell 特殊字元，必須走 stdin。"""
        with patch("subprocess.run", return_value=_completed(_payload("ok"))) as m:
            claude_code_generate("$(rm -rf /) `whoami` 素材")
        assert m.call_args.kwargs["input"] == "$(rm -rf /) `whoami` 素材"
        assert not any("素材" in str(a) for a in m.call_args.args[0])

    def test_disables_tools_and_mcp(self):
        """素材是外部可控輸入（RSS/HN），批次生成一律無工具面。"""
        with patch("subprocess.run", return_value=_completed(_payload("ok"))) as m:
            claude_code_generate("prompt")
        argv = m.call_args.args[0]
        assert argv[:2] == ["claude", "-p"]
        assert "--allowed-tools" in argv and argv[argv.index("--allowed-tools") + 1] == ""
        assert "--strict-mcp-config" in argv

    def test_model_and_timeout_passed(self):
        with patch("subprocess.run", return_value=_completed(_payload("ok"))) as m:
            claude_code_generate("prompt", model="opus", timeout=123)
        argv = m.call_args.args[0]
        assert argv[argv.index("--model") + 1] == "opus"
        assert m.call_args.kwargs["timeout"] == 123


class TestFailuresReturnEmpty:
    """所有失敗都回 ""，不 raise——上層據此 fallback，不該讓 pipeline 整個炸掉。"""

    def test_cli_not_installed(self):
        with patch("subprocess.run", side_effect=FileNotFoundError("claude")):
            assert claude_code_generate("prompt") == ""

    def test_nonzero_exit(self):
        with patch("subprocess.run", return_value=_completed("", returncode=1)):
            assert claude_code_generate("prompt") == ""

    def test_timeout(self):
        with patch("subprocess.run", side_effect=subprocess.TimeoutExpired("claude", 900)):
            assert claude_code_generate("prompt") == ""

    def test_malformed_json(self):
        with patch("subprocess.run", return_value=_completed("not json at all")):
            assert claude_code_generate("prompt") == ""

    def test_is_error_flag(self):
        """CLI exit 0 但 payload 標 is_error（額度用盡、rate limit 都走這條）。"""
        with patch("subprocess.run", return_value=_completed(_payload("Credit balance too low", is_error=True))):
            assert claude_code_generate("prompt") == ""

    def test_empty_result(self):
        with patch("subprocess.run", return_value=_completed(_payload("   "))):
            assert claude_code_generate("prompt") == ""
