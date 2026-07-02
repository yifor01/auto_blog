---
title: dmtrKovalenko/fff
source: GitHub Trending
url: https://github.com/dmtrKovalenko/fff
score: 89
model: google/gemma-4-31b-it:free
generated_at: '2026-07-02T19:55:17.508251'
---

📌 **fff：為 AI Agent 與人類打造的極速檔案搜尋工具**

TL;DR：提供耐錯路徑與內容搜尋的輕量化索引庫，大幅降低 AI Agent 搜尋檔案的 context 浪費。

當 AI Agent 在大型程式碼庫中尋找特定檔案時，頻繁地呼叫 `grep` 或 `fzf` 等 CLI 工具不僅速度慢，且容易因為路徑微小錯誤而失敗，導致 AI 浪費大量 Token 在嘗試錯誤的路徑上。

🧩 **耐錯搜尋與記憶體索引的設計理念**

`fff` 並非單純的 CLI 工具，而是一個將檔案搜尋能力模組化為 library 的工具集。其核心設計旨在解決長時執行的程式在多次搜尋時的效能瓶頸：

- **輕量化記憶體索引**：透過 in-memory content index 實現快速內容搜尋。
- **Frecency 排序**：根據檔案的存取頻率（frequency）與近時性（recency）對檔案進行排序，讓最相關的檔案優先被找到。
- **耐錯搜尋 (Typo-resistant)**：對路徑與內容的搜尋具有耐錯能力，減少因輸入錯誤導致的搜尋失敗。
- **背景監控**：內建 background watcher，確保索引內容與實際檔案同步。

📊 **效能表現：超越傳統 CLI 工具**

作者指出，在任何需要執行多次搜尋的長時執行程式（long-running process）中，`fff` 的速度比 `ripgrep` 和 `fzf` 等主流 CLI 工具更快。

🎯 **對 AI Agent 的實務價值：減少 Context 浪費**

`fff` 特別針對 AI 代理（AI Agents）提供了 MCP (Model Context Protocol) 伺服器支援，可整合至 Claude Code, Codex, OpenCode, Cursor, Cline 等 MCP 客戶端。

對於工程師而言，將 `fff` 整合進 AI 工作流的實際好處在於：
1. **減少 Grep 往返次數**：AI 不再需要反覆嘗試不同的搜尋指令。
2. **節省 Context 空間**：精準的搜尋結果意味著 AI 不需要接收大量無關的檔案內容。
3. **加速回應速度**：更快的檔案定位直接提升了 AI 生成答案的效率。

🛠️ **快速安裝與部署**

`fff` 提供了簡單的安裝方式，安裝後即可在 MCP 客戶端中指示 AI 「use fff」來執行搜尋。

- **Linux / macOS**：
  `curl -L https://dmtrkovalenko.dev/install-fff-mcp.sh | bash`
- **Windows (PowerShell)**：
  `irm https://raw.githubusercontent.com/dmtrKovalenko/fff.nvim/main/install-mcp.ps1 | iex`
- **Homebrew**：
  `brew install dmtrKovalenko/fff/fff-mcp`

🔗 **來源**
- 標題：dmtrKovalenko/fff
- 作者／機構：dmtrKovalenko
- 連結：https://github.com/dmtrKovalenko/fff

#AI #OpenSource #MCP #FileSearch #LLM #DeveloperTools #Productivity #Cursor #ClaudeCode #Indexing
