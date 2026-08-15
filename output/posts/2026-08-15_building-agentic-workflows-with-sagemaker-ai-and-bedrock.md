---
title: Building agentic workflows with SageMaker AI and Bedrock AgentCore
source: AWS ML
url: https://aws.amazon.com/blogs/machine-learning/building-agentic-workflows-with-sagemaker-ai-and-bedrock-agentcore/
model: nvidia/nemotron-3-ultra-550b-a55b:free
generated_at: '2026-08-15T06:15:36.539627'
score: 102
---

📌 【AWS 技術實踐】混合使用 Bedrock 與 SageMaker AI：如何構建具備全方位觀測能力的 Multi-Agent 工作流

TL;DR：透過 Bedrock AgentCore 整合 SageMaker AI 上的自建模型，實現多代理協作並解決 Token 觀測空白。

🤔 **混合模型的挑戰：如何在不重寫框架的情況下使用自定義模型？**

在構建 Agentic Workflow（代理工作流）時，開發者常面臨一個難題：如何將託管的基礎模型（Foundation Models, FMs）與自己針對特定領域優化或成本考量而部署的模型混合使用，且不需為了這種混合需求而重寫整個代理框架？

🧩 **架構設計：利用 Bedrock AgentCore 實現模型靈活性**

透過 Amazon Bedrock AgentCore 的 runtime 功能，工程師可以建立一個生產級的架構，讓不同專業的代理（Agents）協作完成複雜任務：

* **協調機制**：使用者請求進入運行於 Amazon Bedrock AgentCore runtime 中的 Orchestrator Agent（協調代理）。
* **代理工具模式 (Agents as Tools)**：協調代理使用 Strands Agents 的模式，將請求路由至專門的代理。
* **混合路徑**：
    * **預算代理 (Budget Agent)**：透過 Amazon Bedrock 調用 Claude Sonnet 4.6。
    * **財務分析代理 (Financial Analysis Agent)**：透過 SageMaker AI 的 OpenAI 相容 Endpoint 調用 Qwen 3.5 9B。
* **優點**：這種組合在單一架構中同時實現了成本優化、資料在地化（Data Residency）以及模型選擇的靈活性。

📊 **解決觀測盲點：手動填補 SageMaker 模型的 Token 追蹤**

在使用 Amazon Bedrock AgentCore 時，系統會自動使用 OpenTelemetry 進行儀表化（Instrumentation），但這並非萬能。

⚠️ **自動化儀表化的侷限**
目前的自動化機制僅能識別透過 `boto3` 發出的 Amazon Bedrock 模型推論調用。這會導致一個關鍵問題：當 Strands Agents 調用 SageMaker 上的 Qwen 模型時，消耗的 Token 數量在 Trace（追蹤）中是完全不可見的，這使得監控成本、檢測效能退化或偵錯延遲變得極其困難。

💡 **如何實現 Token 級別的觀測？**
為了彌補這個缺口，開發者需要手動發送一個 `gen_ai.chat` span，將 SageMaker 代理的調用封裝起來，並從 Strands 的 `AgentResult.metrics.accumulated_usage` 中提取 Token 使用量。

實作中有兩個關鍵細節：
1. **解決 vLLM 串流問題**：預設情況下，vLLM 在串流回應中不會包含 usage chunk。必須在請求中加入 `stream_options: {"include_usage": True}`，否則 `accumulated_usage` 會永遠是 0。
2. **處理 Token 過期**：SageMaker AI 的 OpenAI 相容 API 需要 Bearer Token，且會過期。建議實作一個繼承自 `httpx.Auth` 的子類別來處理自動刷新 Token 的邏輯。

🎯 **實務啟示**

對於需要大規模部署 Multi-Agent 系統的工程師來說，這套方案提供了一個標準範例：不要僅僅滿足於模型能跑，更要確保「可觀測性（Observability）」能覆蓋到所有自建的 Endpoint，否則在生產環境中，你將無法精確計算每個 Agent 的實際成本。

🔗 **來源**
- 標題：Building agentic workflows with SageMaker AI and Bedrock AgentCore
- 作者／機構：Ayush Sharma @ AWS ML
- 連結：https://aws.amazon.com/blogs/machine-learning/building-agentic-workflows-with-sagemaker-ai-and-bedrock-agentcore/

#AI #AWS #SageMaker #AmazonBedrock #AgenticWorkflows #MultiAgent #MachineLearning #LLM #OpenTelemetry #MLOps
