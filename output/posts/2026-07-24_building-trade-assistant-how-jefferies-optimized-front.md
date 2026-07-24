---
title: 'Building trade assistant: How Jefferies optimized front office trading operations
  with AI'
source: AWS ML
url: https://aws.amazon.com/blogs/machine-learning/building-trade-assistant-how-jefferies-optimized-front-office-trading-operations-with-ai/
model: tencent/hy3:free
generated_at: '2026-07-24T08:15:38.513592'
score: 93
---

這是一篇針對「產業新聞／部落格報導」型別的技術文章。

📌 【Jefferies 實務案例】打造 Agentic AI 交易助手，讓交易員跳過寫程式與 IT 排隊

TL;DR：Jefferies 利用 Agentic AI 整合海量資料，讓交易員無需寫程式即可進行即時資料分析。

🎣 **當資料量與決策速度產生落差**

在投資銀行的前臺交易部門，交易員必須在毫秒間針對客戶行為、交易模式與市場趨勢做出決策。然而，面對分佈於多種視覺化工具中、高達數百萬列的資料，交易員往往既沒有時間，也沒有編寫程式的能力來建立分析系統。傳統做法必須依賴專家進行分析，並與 IT 團隊協作開發客製化儀錶板，這過程往往耗時數天甚至數週，導致資料與決策之間出現嚴重的落差。

🧩 **基於 Strands Agents 的 Agentic AI 架構**

為了縮短這個落差，Jefferies 在 AWS 上建構了 Agentic AI 交易助手，其核心目標是在不要求編寫程式碼、不需等待 IT 處理的前提下，將即時資料分析的能力直接交還給交易員。

該解決方案的核心技術架構包含：
- **Strands Agents**：一個 Agent 框架 SDK，能透過編排基礎模型 (Foundation Models, FMs) 與外部工具的呼叫，讓 AI Agent 具備推理、規劃與執行 (reason, plan, and act) 的能力。
- **Amazon Bedrock**：提供大型語言模型 (LLMs) 的支援。
- **Amazon Bedrock Knowledge Bases**：用於管理與檢索知識庫。
- **Model Context Protocol (MCP)**：利用此開放標準，讓 AI Agent 能透過統一介面，安全地連線到各種不同的資料來源與工具。

💡 **從資料整合轉向即時決策**

這套解決方案代表了資本市場前臺股票交易員與資料互動方式的轉變。透過 Agentic AI，Jefferies 成功解決了資料分散在多個工具中導致難以達成端到端可視性 (end-to-end visibility) 的痛點。

🎯 **實務啟示**

對於金融工程師或企業架構師而言，Jefferies 的做法展示了「Agentic AI」在解決複雜業務流程中的價值：不再只是回答問題，而是透過 MCP 等標準化協議，讓 AI 具備「呼叫工具」的能力，從而解決資料孤島與開發流程緩慢的問題。

🔗 **來源**
- 標題：Building trade assistant: How Jefferies optimized front office trading operations with AI
- 作者／機構：Sanjay Nagraj @ AWS ML
- 連結：https://aws.amazon.com/blogs/machine-learning/building-trade-assistant-how-jefferies-optimized-front-office-trading-operations-with-ai/

#AI #AgenticAI #AWS #MachineLearning #Jefferies #FinTech #AmazonBedrock #LLM #DataAnalytics #InvestmentBanking
