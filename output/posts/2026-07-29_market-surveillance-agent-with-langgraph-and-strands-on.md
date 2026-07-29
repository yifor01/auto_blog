---
title: Market surveillance agent with LangGraph and Strands on AgentCore
source: AWS ML
url: https://aws.amazon.com/blogs/machine-learning/market-surveillance-agent-with-langgraph-and-strands-on-agentcore/
model: tencent/hy3:free
generated_at: '2026-07-29T14:12:45.629580'
score: 86
---

📌 【AWS ML 技術分享】結合 LangGraph 與 Strands，建構金融級市場監控多代理人系統

TL;DR：利用 LangGraph 進行工作流編排並搭配 Strands 進行推理，打造具備容錯與可觀察性的多代理人系統。

當 AI 應用從簡單的聊天機器人演進為複雜的自主系統時，企業面臨的新挑戰在於：如何協同多個代理人（Agent）來處理現實世界的生產環境工作流。傳統的單一代理人模式在面對需要專業知識、動態決策與強健錯誤恢復機制的複雜業務流程時，往往顯得力不從心。

🤔 **金融監控對多代理人協作的嚴苛需求**

以金融服務業為例，市場監控系統必須協調多個專業代理人來完成以下任務：
- 分析交易模式。
- 調查可疑活動。
- 生成完整的報告。
同時，整個過程必須維持嚴格的合規性與可靠性標準。

🧩 **LangGraph 負責宏觀工作流編排，Strands 負責微觀推理**

為了應對上述挑戰，該解決方案結合了兩種框架：

1. **LangGraph：宏觀工作流編排 (Macro-level orchestration)**
   - 擅長管理狀態（State）與有向圖（Directed graphs）以進行多代理人協調。
   - 提供對工作流執行與代理人間共享狀態的細粒度控制。
   - 其核心持久層（Persistence layer）支援生產環境關鍵功能，包括人機協作（Human-in-the-loop）與基於檢查點（Checkpoint）的錯誤恢復機制。

2. **Strands：智慧代理人推理引擎 (Intelligent reasoning engine)**
   - 作為工作流節點（Nodes）內部的推理引擎。
   - 具備模型無關（Model-agnostic）的能力，可與各種大型語言模型（LLM）提供者整合。
   - 提供靈活的工具整合（Tool integration）與全面的可觀察性（Observability）。

💡 **基於 Amazon Bedrock AgentCore 的生產級架構**

隨著 Amazon Bedrock AgentCore 的推出，將代理人解決方案推向生產環境的難度得以降低。透過結合 LangGraph 與 Strands，開發者可以建構出強大的代理人 AI 系統，既能處理複雜的使用案例，又能提供企業級應用所需的基礎設施可靠性與可觀察性。

🎯 **實務啟示**

對於需要處理複雜業務邏輯的工程師而言，將「工作流管理（Orchestration）」與「單一代理人推理（Reasoning）」解耦，並利用具備持久化能力的框架（如 LangGraph）來確保系統在出錯時能從檢查點恢復，是建構生產級 Agentic AI 的關鍵路徑。

🔗 **來源**
- 標題：Market surveillance agent with LangGraph and Strands on AgentCore
- 作者／機構：Gleb Geinke @ AWS ML
- 連結：https://aws.amazon.com/blogs/machine-learning/market-surveillance-agent-with-langgraph-and-strands-on-agentcore/

#AI #LangGraph #Strands #AWS #AmazonBedrock #AgenticAI #MultiAgentSystems #MachineLearning #FinancialTech #LLM
