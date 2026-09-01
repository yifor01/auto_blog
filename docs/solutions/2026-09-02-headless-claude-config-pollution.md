# `claude -p` 被使用者 `~/.claude` 劫持：CI 會過、本機會掛的 bug

日期：2026-09-02
相關 commit：`172da72`

## 問題

把評分改走 Claude Code CLI 批次之後，第一次用真實素材實跑：**8 筆全部缺漏**。

`claude_code_generate()` 有回傳值、`is_error` 是 `False`、returncode 是 0。抓原始輸出來看：

```
評分已完成並輸出。

提醒：今天 auto_post_blog 有 2 個 commit，vault daily-note 還沒記錄。收工前記得跑 `/wrap-up`。
```

模型完全沒有照 `===SCORE N===` 契約輸出，而是回了一句工作總結加一句與任務無關的提醒。

## Root cause

`claude -p` 的 headless session **會載入使用者 `~/.claude` 的全部設定**：

- `~/.claude/settings.json` 的 hooks——SessionStart hook 把「收工前記得跑 /wrap-up」注入這個 session 的 context
- `~/.claude/CLAUDE.md`——全域指令
- 全域 output style——本機當時是「簡短、先講結論」風格

三者合起來，模型判斷「回一句話總結」才是正確行為，批次契約被蓋掉。

**關鍵不對稱**：GitHub Actions 的 runner 沒有 `~/.claude`，所以生產環境從來沒爆過。批次生成從 2026-08-12 上線就一直帶著同一個 bug，只是每天都在 Actions 上跑，本機的 `cli web` 自動觸發路徑沒人細看輸出。

診斷訊號因此與一般 bug 相反：**CI 綠、本機紅**。

## 解法

`argv` 加 `--safe-mode`：

```python
argv = [
    "claude", "-p",
    "--model", model,
    "--safe-mode",          # ← 關掉 CLAUDE.md / skills / plugins / hooks / MCP / output styles
    "--allowed-tools", "",
    "--strict-mcp-config", "--mcp-config", '{"mcpServers":{}}',
    "--output-format", "json",
]
```

auth 不受影響，OAuth 照常運作。

## 試過但不行的方法

| 方法 | 為什麼不行 |
|---|---|
| `--bare` | help 讀起來像正解（skip hooks / CLAUDE.md），但同段也寫「Anthropic auth is strictly `ANTHROPIC_API_KEY` or apiKeyHelper（**OAuth and keychain are never read**）」。用 OAuth 的專案實測回 `Not logged in · Please run /login` |
| `--settings '{"hooks":{}}'` | 是**合併**不是覆蓋，使用者 hooks 照跑。加 `--disable-slash-commands` 也一樣 |
| `CLAUDE_CONFIG_DIR` 指到空目錄 | 可行但要 symlink `.credentials.json` 進去。多一層活動零件，`--safe-mode` 是一等公民 flag，優先 |

## 可複用的 pattern

**任何把 `claude -p`（或任何 agent CLI）當成 API 呼叫的自動化，都要顯式隔離使用者設定。**

判準是一句話：*這個 subprocess 的行為，會不會因為「誰在哪台機器上跑」而改變？* 會的話，那些差異就是靜默故障源。

同類的第一次教訓是 MCP——`--strict-mcp-config --mcp-config '{"mcpServers":{}}'` 早就在 argv 裡了。這次只是把同一個推理延伸到 hooks 與 CLAUDE.md，本來就該一起做。

## 回歸測試

`tests/test_claude_code_generate.py::TestSuccess::test_safe_mode_isolates_user_config` 斷言 `--safe-mode` 在 argv 裡。**這個測試在 CI 上永遠會過，就算 flag 被拿掉、bug 復發，CI 也照樣綠**——它守的是「不要手滑刪掉」，不是「行為正確」，因為真正的行為差異在 CI 上無法重現。
