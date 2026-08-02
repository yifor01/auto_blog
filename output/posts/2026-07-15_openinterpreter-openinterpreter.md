---
title: openinterpreter/openinterpreter
source: GitHub Trending
url: https://github.com/openinterpreter/openinterpreter
score: 105
model: tencent/hy3:free
generated_at: '2026-07-15T07:55:07.694743'
---

📌 Open Interpreter 轉 Rust，最佳化低成本模型

TL;DR：Open Interpreter 推出 Rust 重寫版，讓低成本模型也能跑 coding agent。

🎣 昂貴的旗艦 LLM 才能穩定駕馭的 coding agent，現在有一個開源專案專為便宜模型設計。當多數代理還在比拼頂級模型時，Open Interpreter 反向操作。

🤔 **Open Interpreter 是 Codex 分支，專攻低成本模型效能**
README 指出，Open Interpreter 是一個 coding agent，定位為 OpenAI's Codex 的 fork，核心焦點在於 emulating the agent harness that gets the best performance out of low-cost models（模擬能讓低成本模型發揮最佳效能的代理架構）。對想在本地以較少預算執行自動程式設計助理的開發者，這提供了一個可能的選擇。

🧩 **Rust 重寫加上可切換 harness，模擬最佳代理架構**
專案說明提到這是新的 Rust 版本。其設計理念圍繞 harness emulation：使用者可在終端機以 `/harness` 指令切換多種內建 harness，包含 native、claude-code、claude-code-bare、zcode、kimi-cli、qwen-code、deepseek-tui、swe-agent、minimal 等。此外，內建 QA skill 提供 computer use 能力，可透過 agent-browser 驅動真實瀏覽器中的 web apps，或用 trycua 操作測試原生 apps，讓任何模型都能操作與驗證介面。

💡 **curl 一行裝好，終端機輸入 i 即可開始 session**
安裝方式相當簡單：macOS 與 Linux 執行 `curl -fsSL https://www.openinterpreter.com/install | sh`，Windows 則用 `irm https://www.openinterpreter.com/install.ps1 | iex`。完成後在終端機鍵入 `i` 或 `interpreter` 便能啟動 session。互動介面（TUI）中可用 `/model` 切換 providers 與 models，用 `/harness` 檢視或切換 Rust-native model harnesses。專案也支援以 Agent Client Protocol 模式（`interpreter acp`）接入編輯器，設定與 session 狀態皆儲存在本地 `~/.openinterpreter` 資料夾。

🎯 **本地優先、原生沙箱，適合預算有限的開發者**
從工程實踐看，Open Interpreter 強調在 macOS、Linux、Windows 原生沙箱中執行命令，並將配置留在本地，符合本地優先（local-first）需求。它同時支援 exec、MCP、skills、hooks、permissions、AGENTS.md 等機制，便於整合進現有工作流。對於不想綁定高價 API、希望用低成本模型試驗 coding agent 的團隊，這個 Rust 重寫的 fork 值得一試。

🔗 **來源**
- 標題：openinterpreter/openinterpreter
- 作者／機構：openinterpreter
- 連結：https://github.com/openinterpreter/openinterpreter

#OpenInterpreter #CodingAgent #Rust #LowCostModels #LLM #Codex #AgentHarness #LocalFirst #QA #MCP
