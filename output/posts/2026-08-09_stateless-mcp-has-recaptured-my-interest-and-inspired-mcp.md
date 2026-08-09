---
title: Stateless MCP has recaptured my interest (and inspired mcp-explorer and datasette-mcp)
source: Simon Willison
url: https://simonwillison.net/2026/Jul/31/stateless-mcp/
model: tencent/hy3:free
generated_at: '2026-08-09T06:39:18.291522'
score: 89
---

📌 【MCP 2.0 規格更新】從 Stateful 轉向 Stateless，開發者為何重新看好 Model Context Protocol？

TL;DR：MCP 2.0 透過無狀態（Stateless）設計簡化開發流程，並在安全性與效能上優於直接給予 Agent 終端機權限。

隨著 Agent 技術不斷演進，如何安全且高效地讓 LLM 使用外部工具（Tools）一直是核心議題。儘管先前有人認為「給予 Agent 終端機與 curl 權限」更具靈活性，但 Simon Willison 指出，這種做法隱含極高的安全風險，且需要極強的模型能力才能穩定操作。相比之下，Model Context Protocol (MCP) 提供了更易於稽核與控制的標準化方式，讓即便是在筆電上運行的輕量化模型也能流暢驅動工具。

🧩 **從兩次請求縮減至一次：Stateless MCP 的技術優勢**

MCP 2.0（正式名稱為 2026-07-28 Model Context Protocol specification）最重大的改變在於從「有狀態」（Stateful）轉向「無狀態」（Stateless）的架構設計。

*   **Legacy MCP (Stateful)：** 實作複雜，開發者必須處理會話狀態。
    *   Step 1：發送第一個 HTTP 請求以初始化會話並取得 `Mcp-Session-Id`。
    *   Step 2：發送第二個 HTTP 請求來實際呼叫工具。
*   **New MCP (Stateless)：** 流程極簡，僅需單一 HTTP 請求即可完成呼叫。

這種設計對工程師而言有兩大好處：首先，大幅降低了客戶端（Client）與伺服器端（Server）的實作複雜度；其次，由於不再需要維護伺服器端的 Session ID，這對於需要高擴展性的 Web 應用程式來說，是更理想的架構，開發者不再需要擔心路由問題或 Session 狀態同步。

📊 **實踐成果：從 CLI 工具到資料庫插件**

為了驗證新規格的易用性，作者在短時間內開發了多個專案：

1.  **mcp-explorer**：一個無狀態的 Python CLI 工具，用於互動式探測 MCP 伺服器。
    *   透過 `uvx` 即可直接執行，無需安裝。
    *   能回傳完整的 JSON Schema（包含輸入與輸出定義）。
2.  **datasette-mcp**：為 Datasette 實例新增 `/-/mcp` 端點的插件。
    *   提供 `list_databases()`、`get_database_schema()` 與 `execute_sql()` 三種工具。
    *   目前 `execute_sql()` 僅支援唯讀操作。
    *   透過整合，LLM 可以透過執行多次 SQL 查詢來回答複雜問題（例如：查詢某人最近關於 MCP 的言論）。

💡 **安全性思考：為何 MCP 比 Shell 環境更安全？**

在開發 Agent 時，安全性是首要考量。讓 Agent 在開放網路環境中執行任意命令（Command Execution）是非常危險的，這會將數據外洩的風險直接推給終端用戶。

作者認為，與「給予 Agent 終端機與網路存取權限」相比，使用 MCP 能讓開發者更容易理解與推理 Agent 的能力範圍，並能更精準地控制其權限，這對於構建敏感的應用程式至關重要。

🎯 **實務啟示**

如果你正在開發基於 Agent 的應用程式，且需要模型與外部資料或工具互動，MCP 2.0 的無狀態特性提供了一個更輕量、更易於擴展且更安全的標準方案。對於需要高度控制權的生產環境，比起開放 Shell 權限，使用結構化的 MCP 工具集是更穩健的選擇。

🔗 **來源**
- 標題：Stateless MCP has recaptured my interest (and inspired mcp-explorer and datasette-mcp)
- 作者／機構：Simon Willison
- 連結：https://simonwillison.net/2026/Jul/31/stateless-mcp/

#MCP #LLM #Agent #MachineLearning #SoftwareEngineering #Anthropic #Stateless #API #Python #DeveloperTools
