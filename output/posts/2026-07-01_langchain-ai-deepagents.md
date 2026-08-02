---
title: langchain-ai/deepagents
source: GitHub Trending
url: https://github.com/langchain-ai/deepagents
score: 101
model: google/gemma-4-31b-it:free
generated_at: '2026-07-01T20:31:22.224248'
---

📌 【LangChain 新專案】Deep Agents：開箱即用的生產級 Agent 框架

TL;DR：基於 LangGraph 打造，提供預設最佳化、支援子代理與持久化記憶的開源 Agent 框架。

開發 AI Agent 最痛苦的往往不是選擇模型，而是如何處理長路徑（long-horizon）的任務、管理龐大的上下文，以及在生產環境中確保狀態可追蹤。LangChain 這次推出的 Deep Agents 試圖將這些複雜的工程細節封裝成一個「電池內建（batteries-included）」的框架，讓工程師能快速部署一個具備複雜能力的代理。

🧩 **以「強觀點」設計，專為多步驟複雜任務最佳化**

Deep Agents 並非一個空白的工具箱，而是一個具有「Opinionated」設計的框架，其預設設定經過調校，特別針對需要多步驟、長路徑運作的任務。其核心設計理念包含：

- **高度可擴展**：開發者可以在不分叉（fork）程式碼的情況下，直接覆蓋或替換任何元件。
- **模型無關性**：只要 LLM 支援 Tool Calling（工具呼叫），無論是頂尖模型、開源權重模型或本地模型皆可運作。
- **生產級基礎**：建構於 LangGraph 之上，原生支援串流（streaming）、持久化（persistence）與檢查點（checkpointing），並透過 LangSmith 提供追蹤、評估與部署能力。

🧩 **核心功能：從子代理到沙盒環境**

為了處理複雜任務，Deep Agents 提供了多項實作功能：

- **子代理（Sub-agents）**：可將任務委派給具有獨立上下文視窗（context windows）的子代理。
- **上下文管理**：支援對長對話進行摘要，並將工具輸出卸載（offload）至磁碟以節省記憶體。
- **檔案系統與 Shell 存取**：支援在可插拔的本地、沙盒或遠端後端進行檔案讀寫與搜尋，並可在指定的沙盒中執行指令。
- **持久化記憶與人機協作**：提供可插拔的狀態與儲存後端以實現跨會話記憶，並支援 Human-in-the-loop 機制，讓人類在工具執行前進行核准、編輯或拒絕。
- **技能與工具**：支援可按需載入的重複使用行為（Skills），並可整合自定義函式或任何 MCP 伺服器。

🎯 **實務啟示：從「組裝」轉向「配置」**

對於 AI 工程師而言，Deep Agents 的價值在於將許多重複的 Agent 工程模式（如記憶管理、沙盒執行、子代理分工）標準化。如果你需要快速建立一個類似 Claude Code 或 Cursor 的編碼代理，可以使用其預建的 Deep Agents Code 終端機工具，直接透過 curl 指令安裝。

對於追求靈活度的團隊，可以使用 `uv add deepagents` 快速匯入，利用 `create_deep_agent` 建立代理，在享受預設最佳化設定的同時，僅在必要時覆蓋特定元件。

🔗 **來源**
- 標題：langchain-ai/deepagents
- 作者／機構：langchain-ai
- 連結：https://github.com/langchain-ai/deepagents

#AI #LangChain #LangGraph #Agent #LLM #OpenSource #TypeScript #Python #MCP #SoftwareEngineering
