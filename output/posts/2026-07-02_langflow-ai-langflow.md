---
title: langflow-ai/langflow
source: GitHub Trending
url: https://github.com/langflow-ai/langflow
score: 88
model: google/gemma-4-31b-it:free
generated_at: '2026-07-02T19:57:00.045436'
---

📌 【開源專案】Langflow：將 AI 工作流視覺化，並快速轉化為 API 與 MCP 伺服器

TL;DR：提供視覺化介面構建 AI Agent 與工作流，支援 Python 定製並能直接部署為 API 或 MCP 伺服器。

對於開發 AI 應用的人來說，最痛苦的往往不是選擇哪個 LLM，而是如何將複雜的 Prompt、向量資料庫與多個工具串接成一個穩定且可維護的工作流。

🛠️ **從視覺化編排到程式碼層級的靈活控制**

Langflow 將 AI 代理（Agent）與工作流的構建過程視覺化，讓開發者能快速迭代。其核心設計在於平衡「便捷性」與「控制權」：

- **視覺化建構**：透過視覺化介面快速搭建與調整流程，降低初步開發的門檻。
- **Python 定製化**：提供原始碼存取許可權，開發者可以使用 Python 自定義任何元件，不受限於內建功能。
- **即時測試環境**：內建互動式 Playground，支援分步控制（step-by-step control），讓開發者能立即測試並精煉流程。

🧩 **多代理協作與企業級整合能力**

除了單一工作流，Langflow 針對複雜場景提供了更深層的整合方案：

- **多代理編排**：支援 Multi-agent orchestration，包含對話管理與檢索（Retrieval）功能。
- **多樣化的部署路徑**：建構完成的工作流可以部署為 API，或匯出為 JSON 格式以整合至任何 Python 應用程式中。
- **MCP 伺服器支援**：可將工作流部署為 MCP (Model Context Protocol) 伺服器，使工作流能直接作為工具被 MCP 使用者端呼叫。
- **可觀測性與安全性**：整合 LangSmith 與 LangFuse 等工具以監控執行狀況，並提供企業級的安全性與可擴展性。

🚀 **低門檻的安裝與啟動方式**

為了降低環境配置的複雜度，Langflow 提供了兩種啟動路徑：

1. **Langflow Desktop**：最簡單的入門方式，Windows 與 macOS 使用者無需管理 Python 環境或手動安裝套件，所有依賴項均已內建。
2. **本地安裝 (OSS Python pack)**：針對開發者，要求 Python 3.10–3.14 環境，並建議使用 `uv` 進行快速安裝：
   `uv pip install langflow -U`

🎯 **實務啟示**

對於需要快速驗證 AI 產品原型的團隊，Langflow 的價值在於將「設計 $\rightarrow$ 測試 $\rightarrow$ 部署」的迴圈縮短。特別是將工作流直接轉化為 MCP 伺服器的能力，讓 AI Agent 能更輕易地與現有開發工具鏈整合，而非僅僅停留在一個獨立的聊天視窗中。

🔗 **來源**
- 標題：langflow-ai/langflow
- 作者／機構：langflow-ai
- 連結：https://github.com/langflow-ai/langflow

#AI #LLM #Langflow #Agent #Workflow #MCP #Python #OpenSource #AIInfrastructure #LowCode
