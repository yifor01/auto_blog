---
title: 'Show HN: Engrim – A universal, local-first SQLite memory engine for AI CLIs'
source: Hacker News
url: https://github.com/timgordontg/engrim
model: claude-code/sonnet
generated_at: '2026-09-07T20:51:01.987823'
score: 64
---

📌 engrim：一顆 SQLite 記憶體，讓你的 AI Coding Agent 換模型不失憶

TL;DR：本地優先的 SQLite 記憶引擎，讓 Claude Code、Cursor、Antigravity 等工具共享同一份專案記憶。

你是否也曾在專案做到一半時，從 Claude Code 切到 Cursor，結果新的 agent 完全不記得昨天才敲定的架構決策，甚至連「為什麼不用 MongoDB」都要重新解釋一次？開源專案 engrim 想解決的正是這個問題。

🤔 **問題：context 越大，遺忘反而越嚴重**

作者在 README 中提出一個觀察：隨著 context window 擴大到百萬 token 等級，開發者反而面臨「attention dilution（注意力稀釋）」——推理品質隨對話輪數增加而下降，成本隨每一輪對話累加，而一旦清空 context（`/clear`），先前的架構決策、使用者限制與專案狀態就會徹底遺失。engrim 的核心主張是：模型是可拋棄的工具，但專案的決策不是。它試圖把「專案智慧」從單一 AI 供應商或雲端封閉系統中解耦出來，讓開發者可以在同一個專案上自由切換 Google Antigravity、Claude Code、Cursor MCP、Windsurf、Codex CLI，而不會遺失狀態。

🧩 **架構：SQLite + FTS5 + 靜態向量嵌入的混合檢索**

engrim 是一個 project-scoped、本地優先的 SQLite 記憶引擎（資料庫存放於 `~/.engrim/memory.db`）。根據 README 描述，其檢索層結合了 SQLite FTS5 的 BM25 關鍵字搜尋，以及基於 model2vec 的靜態向量嵌入，透過 reciprocal-rank fusion 做混合排序，藉此在近乎零延遲下載入「熱」的相關記憶。

各家 agent 環境透過各自的 hook 或 MCP 協定與 engrim 對接：
- Google Antigravity：PreInvocation 與 Stop hooks
- Claude Code：SessionStart 與 Stop hooks
- Cursor／Windsurf：Model Context Protocol（stdio）
- Codex CLI：Hooks 與 MCP

值得一提的是「Agent Provenance Engine」：每一筆記憶都會記錄 `origin_agent` 欄位（如 antigravity、claude-code、cursor、cli、user），標明這筆決策是哪個 agent 寫入的，執行 `engrim list` 時甚至會顯示「這是透過 Antigravity 做的決策」這類來源標註。既有資料庫也能透過 `ALTER TABLE` 非破壞性地遷移升級。

對外，engrim 提供一個零依賴、走 JSON-RPC 2.0 stdio 的 MCP server，暴露四個核心工具：`engrim_recall`（混合關鍵字＋語意搜尋）、`engrim_add`（寫入決策／事實／回饋等記錄）、`engrim_context`（依字元預算取回開機記憶包）、`engrim_review`（在清空 session 前檢查有無尚未寫入的重要決策）。

🚀 **怎麼用**

安裝方式是 `pip install engrim`，接著執行 `engrim setup`，它會自動偵測機器上已安裝的環境（例如 `~/.gemini`、`~/.claude`、`~/.cursor`、`~/.codex`），一次把對應的 hooks、skill、MCP 設定全部接好；也可以用 `engrim setup --agy`／`--claude`／`--cursor`／`--codex`／`--all` 針對特定平臺設定，並用 `--dry-run` 先預覽會改動哪些設定檔。日常操作則靠 `engrim add` 手動記錄決策，或讓 agent 在做出架構決策時自動寫入；`engrim recall -q "database"` 用來做混合式檢索。

📊 **開發者自述的案例：153,000 token 濃縮成不到 1,000 token**

README 提供了一份作者自行測試的案例：在一個 5 萬行的演算法交易系統上，連續跑了 105 個 session，作者宣稱期間 186 個單元測試零迴歸、跨模型切換零上下文失憶。累積數天的架構討論、參數調整與除錯，共 153,000 多個 token 的工作內容，被壓縮進一份不到 1,000 token 的「作用中記憶包」（約佔 context window 不到 1%），作者稱這是每次重啟 session 時「99% 以上的重載成本削減」。同一份程式碼庫也在 Google Antigravity CLI、Claude Code、Cursor MCP 之間無縫切換，作者表示未觀察到模型漂移或架構性倒退。

💡 **這其實是「整合」的價值，而非全新演算法**

從架構描述來看，engrim 用的檢索技術（BM25 全文檢索、靜態向量嵌入、RRF 融合）本身都不是新發明，真正的工程量在於「膠水層」：針對 Antigravity、Claude Code、Cursor、Codex 這幾種截然不同的 hook／MCP 協定各自寫好 adapter，並在多 agent 協作下維護一致的 provenance 紀錄。對於已經習慣在多個 CLI-based coding agent 間跳轉的團隊來說，這種整合層恰好補上了目前工具鏈缺的一塊。

⚠️ **證據來源需留意**

目前公開的效能數據（105 session、99% 削減等）皆來自作者在單一專案上的自述案例研究，尚未見到第三方或跨專案的獨立驗證，評估時宜將其視為開發者的產品主張而非嚴謹的效能基準。

🎯 **實務啟示**

如果你的團隊本來就會在多個 AI coding agent 間切換，engrim 提供了一個輕量、本地優先且不綁定廠商的方式，把「該記住的東西」外部化，避免每次清空 context 都要重新對齊架構決策，值得拿現有專案小範圍試用看看。

🔗 **來源**
- 標題：Show HN: Engrim – A universal, local-first SQLite memory engine for AI CLIs
- 作者／機構：timgordontg
- 連結：https://github.com/timgordontg/engrim

#AI #OpenSource #SQLite #AIAgents #MCP #DeveloperTools #LLM #ContextWindow #ClaudeCode #AIMemory
