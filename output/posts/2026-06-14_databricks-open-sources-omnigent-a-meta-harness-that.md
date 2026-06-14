---
title: 'Databricks Open-Sources Omnigent: A Meta-Harness That Composes, Governs, and
  Shares AI Agents Across Claude Code, Codex, and Pi'
source: MarkTechPost
url: https://www.marktechpost.com/2026/06/13/databricks-open-sources-omnigent-a-meta-harness-that-composes-governs-and-shares-ai-agents-across-claude-code-codex-and-pi/
score: 102
model: google/gemma-4-31b-it:free
generated_at: '2026-06-14T19:34:31.135961'
---

📌 【Databricks 開源】Omnigent：讓不同 AI Agent 像樂高一樣可互換的「元框架」

你是否也面臨這種窘境：為了完成一個功能，得在 Claude Code 寫邏輯、在 Codex 檢查語法、再把結果貼到 Slack 或文件裡？目前大多數的 AI Agent 都是「孤島」，每個 Harness（外殼）只記得自己的對話紀錄，導致工程師在多個 Agent 之間頻繁地複製貼上。

🤔 **AI Agent 太多，反而增加了「切換成本」**

目前的 AI Agent 實作通常包含一個模型加上一個 Harness（例如 Claude Code、Codex 或 Pi）。問題在於，這些 Harness 之間缺乏統一的介面。當工程師同時操作四五個不同的 Agent 時，資訊碎片化嚴重，缺乏一個能橫跨不同工具的共享層來進行協作與管理。

🧪 **定義一個更高層級的「Meta-Harness」**

Databricks AI 團隊針對此問題開發了 Omnigent，並以 Apache 2.0 協議開源。其核心設計理念非常簡單：無論內部的模型如何被呼叫，對使用者而言，介面始終是「輸入訊息/檔案 $\rightarrow$ 輸出文本流/工具呼叫」。

Omnigent 將這個過程標準化，將原本獨立的 Agent 封裝成可互換的組件。它不再是單一的 Agent，而是一個位於所有 Agent 之上的「元框架 (Meta-Harness)」。

⚙️ **將 heterogeneous Agents 轉化為可協作的工人**

Omnigent 的架構分為兩個核心部分，將複雜的 Agent 管理簡化為統一的 API：

- **Runner (執行器)**：將任何 Agent 封裝在一個沙盒會話 (Sandboxed Session) 中，提供統一的 API 介面。
- **Server (伺服器)**：負責策略管理與共享。它將每個會話同步至終端機 (Terminal)、App 與 Web API。

這意味著你可以在終端機輸入一個指令啟動會話，同時在瀏覽器 (localhost:6767) 或手機上看到完全同步的訊息、子 Agent 狀態、終端機輸出與檔案。

💡 **從「單一工具」演進到「Agent 協作系統」**

Omnigent 的真正價值在於它將不同廠商的工具「標準化」：
- **廣泛的相容性**：它能封裝終端機編程 Agent (如 Claude Code, Codex, Pi) 以及 SDK (如 OpenAI Agents, Claude Agents SDK)。
- **協調能力**：它能將多個不同類型的 Agent 視為「可互換的工人」，由一個統一的編排器 (Orchestrator) 進行協調。
- **安全底層**：透過名為 「Omnibox」 的 OS 沙盒，能管控作業系統存取權限並轉換網路請求，確保執行安全。

⚠️ **需自行提供模型與基礎設施，非開箱即用的模型**

值得注意的是，Omnigent 是一個框架而非模型本身。使用者需要自行提供對應的模型憑證 (Credentials) 與基礎設施，Omnigent 則負責在頂層運行並管理這些 Agent。

🎯 **開發者如何實踐：從「切換視窗」轉向「定義流程」**

對於 AI 工程師而言，Omnigent 的出現讓開發工作流可以從「手動搬運資訊」轉向「定義 Agent 協作鏈」：
- **減少認知負荷**：利用統一的介面管理所有 Agent，不再需要在不同工具間切換。
- **建立 Agent 管道**：可以嘗試將不同擅長領域的 Agent (例如一個擅長重構、一個擅長測試) 組合在同一個會話中。
- **跨裝置同步**：利用其 Server 架構，在開發時能靈活在終端機與 Web UI 之間切換。

🔗 **相關資訊**
📝 Databricks Open-Sources Omnigent: A Meta-Harness That Composes, Governs, and Shares AI Agents
👤 Asif Razzaq (via MarkTechPost)
🔗 文章連結：https://www.marktechpost.com/2026/06/13/databricks-open-sources-omnigent-a-meta-harness-that-composes-governs-and-shares-ai-agents-across-claude-code-codex-and-pi/

你目前在開發流程中使用過多少個不同的 AI Agent？你認為統一的介面能解決你的痛點嗎？歡迎在下方討論 👇

#Databricks #OpenSource #AIAgents #ClaudeCode #LLMOps #軟體工程 #Omnigent
