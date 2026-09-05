---
title: 'From silos to insights: Federated data access patterns for AI agents'
source: Amazon.com
url: https://aws.amazon.com/blogs/big-data/from-silos-to-insights-federated-data-access-patterns-for-ai-agents/
model: claude-code/sonnet
generated_at: '2026-09-05T19:14:22.664792'
score: 78
---

📌 AWS 部落格：用 MCP 打通企業資料孤島，讓 agent 自己去查資料

TL;DR：AWS 整理三種以 MCP 伺服器和 Amazon Bedrock AgentCore 打造的聯邦式資料存取模式。

每次想讓 AI agent 多查一份報表，是不是都得先找資料工程師搭一條新的資料管道？這篇 AWS 部落格文章想解決的正是這件事。

🤔 資料留在原地，不必事事都經過資料工程師

文章開頭指出，AI agent 現在可以直接觸及企業資料原本存放的地方，而不必把每一個問題都繞道經過資料工程團隊處理。這篇文章的核心，是整理出三種讓 agent 做到這件事的參考架構模式。

🧩 以 MCP 伺服器與 Bedrock AgentCore 為基礎

摘要指出，這三種模式都建立在 Model Context Protocol（MCP）伺服器與 Amazon Bedrock AgentCore 之上，其中第一種模式與資料目錄（catalog）有關；受限於目前取得的素材在此處被截斷，另外兩種模式的細節與差異未能在本文中進一步說明，有興趣的讀者建議直接參考原文。

⚠️ 素材有限，細節請看原文

這篇文章本身應該包含每種模式的具體架構與適用情境，但目前拿到的摘要只到「三種模式，第一種與 catalog 有關」為止，無法進一步展開技術細節或比較優劣，這裡不強行補充未提及的內容。

🎯 實務啟示

如果你的團隊已經在用 Amazon Bedrock AgentCore 建構 agent，而企業資料分散在多個系統、想避免每次查詢都要資料工程師手動介入，這篇文章提供的三種聯邦式資料存取模式值得作為架構設計的起點，實際選型前建議完整讀過原文評估每種模式的取捨。

🔗 來源
- 標題：From silos to insights: Federated data access patterns for AI agents
- 作者／機構：James Wu, AWS
- 連結：https://aws.amazon.com/blogs/big-data/from-silos-to-insights-federated-data-access-patterns-for-ai-agents/

#MCP #AmazonBedrock #AgentCore #DataFederation #AIAgents #EnterpriseData #AWS #DataArchitecture #LLMTools #DataCatalog
