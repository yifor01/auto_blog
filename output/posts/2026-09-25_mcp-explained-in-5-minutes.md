---
title: MCP Explained in 5 Minutes
source: KDnuggets
url: https://www.kdnuggets.com/mcp-explained-in-5-minutes
model: claude-code/sonnet
generated_at: '2026-09-25T20:57:27.212210'
score: 72
---

📌 MCP 新規格轉 Stateless，遠端伺服器更好擴充

TL;DR：MCP 2026-07-28 規格把協定核心改為 stateless，同時一次看懂如何用 Claude Code 串接 Tavily、GitHub、Playwright。

幾乎每個人都聽過 MCP，也知道它跟 AI 代理、程式助理、工具呼叫脫不了關係，但真正說得清楚「它到底怎麼運作」的人卻少很多。一旦搞懂基本流程，整套系統其實比想像中簡單。

🤔 沒有標準介面之前，每個服務都要客製串接

MCP 的核心概念是給 AI 應用一套與外部工具、資料源溝通的標準語言。沒有 MCP 時，每個 API、資料庫、程式庫或瀏覽器都可能需要各自的客製整合；有了 MCP，AI 應用可以透過同一套標準介面連接不同的 MCP 伺服器。MCP 不會取代既有 API，MCP 伺服器通常仍是代表 AI 應用去呼叫底層 API 或服務，MCP 標準化的是這些能力「如何被呈現、發現與呼叫」。一個 MCP 伺服器可以暴露三種能力：Tools（模型可執行的動作，例如搜尋網頁、建立 issue、執行查詢）、Resources（應用可讀取的資訊，例如檔案、文件、資料庫紀錄）、Prompts（伺服器提供的可重複使用提示樣板或工作流程）。對多數 AI 代理工作流而言，Tools 是最關鍵的一環，因為它讓模型不只是產生文字，還能真正與外部系統互動。

🧩 host → client → server 的呼叫流程

MCP 採用 client-server 架構：host 是 AI 應用本身（例如 Claude Code），host 內的 MCP client 連上一個或多個 MCP server，這些 server 再暴露 tools、resources 或 prompts 給外部服務。例如問「搜尋最新的 PyTorch 版本並摘要主要變更」，Claude 會先判斷這需要即時資訊，接著檢視可用的 MCP 工具、選擇一個網頁搜尋工具，透過 MCP 伺服器送出請求並取回搜尋結果。重點是 MCP 本身不做推理，是模型決定何時該用工具、該拿結果做什麼，MCP 只提供讓工具可被呼叫的標準連線。

文中實際示範了三種串接：用 `claude mcp add --transport http tavily https://mcp.tavily.com/mcp` 接上 Tavily 做網頁搜尋；用帶有 GitHub PAT 的 header 接上官方 GitHub 遠端 MCP 伺服器來讀取儲存庫、審查 PR 或查看 issue；以及用 `claude mcp add playwright npx @playwright/mcp@latest` 接上 Playwright 做瀏覽器自動化，Playwright MCP 主要透過結構化的無障礙（accessibility）快照，讓模型取得頁面元素的結構化表示以進行互動。

📊 最新規格的重點：協定核心變成 stateless

MCP 2026-07-28 規格帶來一個架構層級的改變：協定核心變成 stateless，不再需要維護與特定伺服器的持續 session，每個請求都自帶處理所需的資訊，讓遠端 MCP 伺服器更容易在標準雲端基礎設施上水平擴展。這次更新還包括：無需持續協定 session 的 stateless 請求、更好的伺服器與 gateway 路由辨識、可重複使用而不必每次重新抓取的 tool／resource／prompt 清單快取、支援工具先詢問更多資訊再繼續執行的多步互動、針對長時間執行任務的 Tasks 支援，以及更強的遠端伺服器身分驗證，並允許以擴充方式加入新能力而不需更動協定核心。

🎯 給工程團隊的啟示

一旦掌握「模型 → MCP → 工具 → 結果」這個基本流程，MCP 就不再是抽象名詞，而是一套可以直接拿來串生產環境代理的標準管線。新規格的 stateless 化尤其值得留意：如果你正在規劃遠端 MCP 伺服器的部署方式，這代表未來的擴展策略可以更貼近一般無狀態 API 服務的做法，而不必額外處理 session 親和性的問題。

🔗 來源
- 標題：MCP Explained in 5 Minutes
- 作者／機構：Abid Ali Awan, KDnuggets
- 連結：https://www.kdnuggets.com/mcp-explained-in-5-minutes

#MCP #ClaudeCode #AIAgents #ModelContextProtocol #Tavily #GitHub #Playwright #ToolUse #AgenticAI #DeveloperTools
