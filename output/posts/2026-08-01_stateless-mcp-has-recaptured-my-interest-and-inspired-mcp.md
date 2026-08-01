---
title: Stateless MCP has recaptured my interest (and inspired mcp-explorer and datasette-mcp)
source: Simon Willison
url: https://simonwillison.net/2026/Jul/31/stateless-mcp/
model: tencent/hy3:free
generated_at: '2026-08-01T08:10:03.959582'
score: 90
---

📌 【MCP 2.0 重磅更新】從 Stateful 轉向 Stateless，簡化 LLM 工具調用的實作門檻

TL;DR：MCP 2.0 引入無狀態（Stateless）規範，將兩次 HTTP 請求簡化為一次，大幅降低開發複雜度。

隨著 AI Agent 框架日益成熟，如何讓大型語言模型（LLM）安全且高效地存取外部工具，已成為工程師關注的核心。2026 年 7 月 28 日，Model Context Protocol (MCP) 發布了 2.0 規範，這項由 Anthropic 推出的標準，旨在定義一種標準化的方式，讓 Agent 框架能輕鬆擴充新工具。

🤔 **從複雜的 Session 管理，進化到單次請求的簡潔**

在舊版的「有狀態（Stateful）」MCP 規範（作者稱之為 Legacy MCP）中，開發者必須處理複雜的會話狀態。一個典型的工具調用需要兩次 HTTP 請求：
1. 第一次：初始化會話並取得 `Mcp-Session-Id`。
2. 第二次：使用該 ID 來實際呼叫工具。

而在全新的「無狀態（Stateless）」MCP 2.0 規範中，整個流程被簡化為單次 HTTP 請求。這對工程師而言有兩大好處：
- **實作更簡單**：無論是客戶端還是伺服器端，程式碼邏輯都變得更乾淨。
- **更適合擴展 Web 應用**：開發者不再需要維護伺服器端的 Session ID，也不用擔心路由問題（例如確保同一個會話必須連到同一個後端機器）。

🧩 **更安全且低門檻的工具調用方式**

雖然讓 Agent 直接擁有終端機（Shell）與 `curl` 的權限看起來更靈活，但這也帶來了極高的安全風險，且需要極強的模型能力才能穩定操作。

相比之下，使用 MCP 規範的優勢在於：
- **易於審核與控制**：比起隨機的指令執行，MCP 工具的行為更容易預期。
- **對小模型友善**：由於介面簡單，即便是在筆電上運行的輕量化模型，也能夠流暢地驅動 MCP 工具。

📊 **實踐成果：從 CLI 工具到資料庫插件**

作者透過這次規範更新，快速開發了三個實用的工具來驗證新規範的威力：

1. **mcp-explorer**
   這是一個無狀態的 Python CLI 工具，讓開發者可以互動式地探測 MCP 伺服器。開發者可以直接使用 `uvx` 執行，無需安裝，即可查詢工具列表、JSON Schema 以及輸出結果（例如直接取得 SVG 圖片）。

2. **datasette-mcp**
   這是一個 Datasette 插件，為任何 Datasette 實例增加 `/mcp` 端點。它提供三個核心工具：`list_databases()`、`get_database_schema()` 以及 `execute_sql()`（目前僅限唯讀）。這讓 LLM 能直接對託管的資料庫進行 SQL 查詢。

3. **llm-mcp-client**
   作者嘗試將 MCP 直接整合進 `llm` 工具中，讓模型在執行任務時，能透過推理過程（Reasoning trace）來決定並執行相關的 SQL 查詢。

🎯 **實務啟示**

對於正在構建 AI Agent 的工程師來說，MCP 2.0 的無狀態化標誌著「工具化」標準的成熟。當工具調用變得像單純的 API 請求一樣簡單時，我們應該更專注於如何定義更精準的工具介面，並利用其安全性優勢，將 LLM 應用於處理更敏感的業務邏輯。

🔗 **來源**
- 標題：Stateless MCP has recaptured my interest (and inspired mcp-explorer and datasette-mcp)
- 作者／機構：Simon Willison
- 連結：simonwillison.net/2026/Jul/31/stateless-mcp/

#AI #MCP #LLM #Anthropic #AgenticWorkflow #SoftwareEngineering #Python #DataScience #API #MachineLearning
