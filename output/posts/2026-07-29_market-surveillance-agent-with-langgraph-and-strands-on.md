---
title: Market surveillance agent with LangGraph and Strands on AgentCore
source: AWS ML
url: https://aws.amazon.com/blogs/machine-learning/market-surveillance-agent-with-langgraph-and-strands-on-agentcore/
model: tencent/hy3:free
generated_at: '2026-07-29T08:30:09.868632'
score: 97
---

📌 【AWS ML 技術分享】結合 LangGraph 與 Strands，打造金融級市場監控多代理系統

TL;DR：利用 LangGraph 進行工作流編排，並搭配 Strands 強化代理推理，解決複雜金融監控需求。

🤔 **單一代理模式難以應對複雜業務流程**

隨著 AI 應用從簡單的聊天機器人轉向自主系統，組織面臨著如何編排複雜多代理（multi-agent）工作流的新挑戰。傳統的單一代理（single-agent）方法在處理需要專業知識、動態決策與強健錯誤恢復機制的複雜業務流程時，往往力有未逮。金融服務業便是典型案例：市場監控系統必須協調多個專業代理，在維持嚴格合規與可靠性標準的同時，分析交易模式、調查可疑活動並生成完整報告。

🧩 **LangGraph 負責宏觀編排，Strands 負責微觀推理**

為了應對上述挑戰，本方案結合了兩大框架：

*   **LangGraph**：負責宏觀層級的工作流編排（macro-level workflow orchestration）。其優勢在於管理狀態（state）與有向圖（directed graphs）以進行多代理協調，並能對工作流執行與代理間共享的狀態進行細粒度控制。其核心持久化層（persistence layer）支援生產環境所需的關鍵功能，例如人機協作（human-in-the-loop）以及基於檢查點（checkpoint）的故障恢復。
*   **Strands**：作為工作流節點內的推理引擎（reasoning engine）。Strands Agent 具備模型無關（model-agnostic）的能力，能與各種大型語言模型（LLM）供應商整合，同時提供靈活的工具整合與全面的可觀測性（observability）。

💡 **在 AWS 基礎設施上實現生產級代理系統**

透過結合 LangGraph 的編排能力與 Strands 的推理能力，並利用 Amazon Bedrock AgentCore 提供的基礎設施，工程師可以構建出具備高可靠性與可觀測性的生產級代理 AI 系統，藉此處理複雜的企業級應用場景。

🎯 **實務啟示**

對於需要處理複雜邏輯與嚴格合規要求的企業（如金融業），將「工作流編排」與「代理推理」解耦，並利用具備狀態持久化能力的框架，是將 Agentic AI 從實驗室推向生產環境的關鍵路徑。

🔗 **來源**
- 標題：Market surveillance agent with LangGraph and Strands on AgentCore
- 作者／機構：Gleb Geinke @ AWS ML
- 連結：https://aws.amazon.com/blogs/machine-learning/market-surveillance-agent-with-langgraph-and-strands-on-agentcore/

#AI #MachineLearning #LangGraph #Strands #AWS #AmazonBedrock #MultiAgent #FinancialTech #AgenticAI #LLM
