---
title: Build self-service AWS Health analytics to find actionable health insights
  with AI agents powered by Amazon Bedrock
source: AWS ML
url: https://aws.amazon.com/blogs/machine-learning/build-self-service-aws-health-analytics-to-find-actionable-health-insights-with-ai-agents-powered-by-amazon-bedrock/
score: 101
model: google/gemma-4-31b-it:free
generated_at: '2026-06-25T20:21:31.824919'
---

📌 【AWS 實作】利用 Amazon Bedrock 與 AI Agent 打造 AWS Health 自助分析工具

TL;DR：透過開源專案 Chaplin，利用 AI Agent 與 MCP 協定將 AWS Health 事件轉化為可行動的自然語言洞察。

週一早上的營運團隊經常面臨一個噩夢：面對 50 個以上帳號中湧入的 Amazon Linux 2 終止支援、RDS 版本棄用或 EC2 例項汰換通知，如何在海量資訊中快速分辨哪些會影響生產環境？哪些需要立即處理？

🤔 **從「被動救火」到「主動分析」的痛點**

對於管理數十甚至數百個帳號的大型企業，AWS Health 雖然透過 API 與 Amazon EventBridge 提供完整資料，但傳統的反應式管理存在明顯缺口：
- 缺乏自助分析能力：無法快速識別事件的業務影響與優先順序。
- 依賴外部支援：團隊必須等待技術客戶經理 (TAM) 解讀事件，導致關鍵決策延遲。
- 資源錯置：工程師花太多時間在處理瑣碎的營運通知，而非專注於創新。

🧩 **Chaplin：基於 MCP 協定的 AI Agent 解決方案**

為了打破上述僵局，AWS 推出了開源解決方案 Chaplin (Customer Health and Planned Lifecycle Intelligence Nexus)。其核心設計理念是將 AI Agent 的能力透過 Model Context Protocol (MCP) 暴露給使用者。

這套系統的運作邏輯如下：
- 整合 Amazon Bedrock：利用 Bedrock 提供的 AI 能力驅動 Agent。
- 匯入 MCP 協定：讓使用者能直接透過支援 MCP 的 AI 助手，以自然語言詢問健康事件。
- 擺脫預設面板：不再依賴固定格式的 Dashboard 模式，而是提供精準且具備上下文的回答。
- 優先化行動：Chaplin 能將可採取行動的事件（如即將連結至 AWS Transform 模板的事件）在環境中浮現並排定優先順序。

🎯 **實務啟示：將運維分析「對話化」**

對於維運工程師而言，這代表了從「查詢 API → 篩選資料 → 人工分析」到「直接詢問 AI → 獲取洞察 → 執行動作」的轉型。透過將 AWS Health 資料與 AI Agent 結合，企業可以大幅降低對支援團隊的依賴，將日常的健康事件分析轉化為自助服務。

🔗 **來源**
- 標題：Build self-service AWS Health analytics to find actionable health insights with AI agents powered by Amazon Bedrock
- 作者／機構：Aurelio DeSimone @ AWS ML
- 連結：https://aws.amazon.com/blogs/machine-learning/build-self-service-aws-health-analytics-to-find-actionable-health-insights-with-ai-agents-powered-by-amazon-bedrock/

#AWS #AmazonBedrock #AIAgents #MCP #AWSHealth #CloudOperations #OpenSource #DevOps #ModelContextProtocol #CloudManagement
