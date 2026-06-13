---
title: andrewyng/aisuite
source: GitHub Trending
url: https://github.com/andrewyng/aisuite
score: 98
model: google/gemma-4-31b-it:free
generated_at: '2026-06-13T19:33:57.513797'
---

📌 【Andrew Ng 最新開源】aisuite：一套讓 LLM 跨模型統一調用，並實現桌面 AI Agent 的輕量框架

你是否在開發 AI Agent 時，被不同 LLM 供應商（OpenAI, Anthropic, Google）各自不同的 API 格式搞得頭大？每次切換模型都要重寫一遍調用邏輯，這種重複性工作不僅低效，更增加了維護成本。

🤔 **跨模型調用的痛點：API 碎片化與開發成本**

目前 AI 生態系中，每個模型供應商都有自己的 Chat Completions 格式。雖然有 LangChain 等框架嘗試統一，但對於許多工程師來說，有時只需要一個更輕量、更直接的介面，而不需要承擔過重的框架依賴。

Andrew Ng 團隊推出的 `aisuite` 正是為了解決這個問題，旨在提供一個統一的進入點，讓開發者能用同一套代碼輕鬆在不同模型之間切換，並在此基礎上快速構建 Agent。

🧪 **雙層設計：從統一 API 到 Agent 實作**

`aisuite` 的設計分為兩個核心層級，將基礎通訊與高層邏輯解耦：

1. **Chat Completions API (底層)**：提供統一的介面，讓開發者可以用相同的方式調用不同供應商的模型。
2. **Agents API (上層)**：在統一 API 之上構建，整合了 Tools（工具）與 Toolkits（工具集），讓 AI 能從單純的「聊天」轉化為能「執行任務」的代理。

這種分層設計讓工程師可以根據需求，選擇僅僅是統一模型接口，或是直接開發複雜的 Agent 邏輯。

🚀 **實作範例：OpenCoworker 桌面 AI 同事**

為了證明 `aisuite` 的實用性，該專案同步開源了 **OpenCoworker**。這是一個直接運行在桌面端的 AI Agent，展示了 `aisuite` 如何將 LLM 轉化為真正的生產力工具：

- **深度研究與執行**：不只能聊天，還能進行深度研究並在電腦上執行具體任務。
- **上下文感知**：在獲得權限後可讀取本地文件以獲取背景資訊。
- **跨平台溝通**：能讀取與發送 Slack 訊息、電子郵件等。
- **產出實體交付物**：能直接生成 PDF 報告、文檔或電子表格。
- **自動化排程**：支持定時任務，例如每天自動提供新聞摘要。

💡 **本地化與靈活性：BYOK 與隱私保障**

`aisuite` 與 OpenCoworker 在部署上提供了極高的靈活性：

- **Bring Your Own Key (BYOK)**：支持 OpenAI, Anthropic, Google 的 API Key。
- **完全本地化**：支持透過 Ollama 運行，確保所有數據留在使用者自己的機器上，解決企業級開發最擔心的隱私外洩問題。
- **開源參考**：OpenCoworker 的源碼位於 `platform/` 目錄下，為想要構建自有 Agent Harness 的工程師提供了完整的實作參考。

⚠️ **目前的限制與適用場景**

由於 OpenCoworker 是作為 `aisuite` 的參考實現，其功能深度依賴於所連接的模型能力。對於極其複雜的長流程工作流，可能仍需額外的狀態管理機制。此外，目前 OpenCoworker 的可執行檔主要支持 macOS (Apple Silicon) 與 Windows 10/11。

🎯 **工程實踐建議：快速原型開發的理想選擇**

如果你正在構建 AI Agent，且希望在不同模型之間快速做 A/B Test，或者想開發一個能與本地文件、第三方通訊軟體互動的桌面助手，`aisuite` 是一個非常高效的起點。

建議開發者先從 `aisuite` 的統一 API 開始，將模型切換邏輯抽象化，再利用其 Agents API 逐步加入工具集，模仿 OpenCoworker 的結構來構建自己的桌面代理。

🔗 **專案連結**
📝 aisuite / OpenCoworker
👤 Andrew Ng
🔗 GitHub: https://github.com/andrewyng/aisuite

你會選擇將 AI Agent 部署在雲端，還是像 OpenCoworker 這樣直接運行在桌面端？歡迎在下方分享你的看法 👇

#AI #LLM #OpenSource #AndrewNg #AIagent #Python #aisuite #OpenCoworker #生產力工具
