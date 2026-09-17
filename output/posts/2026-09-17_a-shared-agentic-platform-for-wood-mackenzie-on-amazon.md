---
title: A shared agentic platform for Wood Mackenzie, on Amazon Bedrock AgentCore
source: AWS ML
url: https://aws.amazon.com/blogs/machine-learning/a-shared-agentic-platform-for-wood-mackenzie-on-amazon-bedrock-agentcore/
model: claude-code/sonnet
generated_at: '2026-09-17T20:39:56.746455'
score: 82
---

📌 Wood Mackenzie 用 AgentCore 打造共用 Agent 平臺 APEX

TL;DR：Wood Mackenzie 建了一套跨團隊共用的 Agent 基礎設施 APEX，用 Amazon Bedrock AgentCore 取代重複造輪子的自建 runtime。

打造一個能跑的 Agent prototype，一個下午就能完成。但把它送進生產環境,才是真正燒工程資源的地方。文中引用的產業調查指出，企業導入 AI 的實驗幾乎已是普遍現象，但真正把 Agent 規模化用進生產流程的組織，仍只有約四分之一。Wood Mackenzie 內部的數字更直接：88% 的 AI POC 從未走到大規模部署。

🤔 **問題不在模型，在架構**

Forrester 的分析指出，Agent 失敗的主因多是模糊性、協調失靈、系統行為不可預期，而不是單純的程式錯誤。被提及最多的單一瓶頸是評估與可觀測性：團隊很難事先判斷一個非決定性（non-deterministic）的 Agent 何時會出錯，傳統回歸測試根本抓不到。緊接著是治理與身分問題，不少主管坦承無法立即關閉一個行為異常的 Agent。而底層還有一個更根本的重複勞動:每個團隊各自重新實作驗證、guardrails、記憶體與追蹤，還把模型寫死在程式碼裡，換供應商就等於重寫一次。

Wood Mackenzie 在 APEX 之前，Woody、Lens AI、ST Trading App 三個應用原本都各自準備搭建自己的 Agent stack。如果放著不管,三套系統會各自付一次基礎設施的稅,而且彼此的記憶體、工具與評估邏輯完全無法共用。

🧩 **APEX 的分層架構**

團隊評估了 hosting model、成本模型、是否 model-agnostic、擴展性、治理與企業支援等條件後，選擇以 Amazon Bedrock AgentCore 為底層。AgentCore 支援任意開源框架（Strands Agents、LangGraph、LangChain、LlamaIndex、CrewAI、Google ADK、OpenAI Agents SDK 等），也支援 Model Context Protocol（MCP）與 Agent-to-Agent（A2A）協定，因此團隊不必在「開源彈性」與「AWS 服務安全性」之間二選一。

APEX 的架構分層大致如下：
- 使用者端：Woody、Lens AI、ST Trading App 三個應用，透過 APEX frontend SDK 存取。
- 後端核心：由 AgentCore 的 Runtime、Identity、Gateway、Memory、Observability 組成，再加上 Orchestrator、向量資料庫、Amazon Bedrock model catalog 與 Amazon Bedrock Guardrails。
- 基礎設施：WM IaC Framework（用 AWS CDK 與 GitHub 版本控管平臺資源、guardrails 寫成程式碼）。
- 外部連接：MCP 層負責串接第三方系統，包含 AWS Marketplace 與合作夥伴系統。

一個請求的實際流程是:使用者驗證與 AgentCore Identity 先確立呼叫者身分與權限，且這個身分／授權會貫穿整個 Agent 呼叫鏈，而不只是在入口檢查一次；Orchestrator 接手路由，並查詢 Woodmac Agent Registry(一個可跨組織發現、共用、重用 Agent、工具與技能的登記中心，內建治理與審批流程);AgentCore Runtime 在無伺服器、session-isolated 的環境中執行 Agent 程式碼(內部跑的是 AI Agents Studio，支援 Strands Agents、LangGraph、CrewAI、n8n、Vertex、OpenAI 等框架);模型呼叫透過 Amazon Bedrock model catalog，讓換模型供應商不需要重寫 Agent；工具則透過 AgentCore Gateway 曝露出來，把 API、AWS Lambda 函式與既有 MCP server 轉成 Agent 可用的工具，並支援 IAM、OAuth 2.1、API key 三種驗證方式。

💡 **計費模式如何配合 Agent 的真實負載**

AgentCore 採用用量計費、不需預付承諾或最低費用，各服務可獨立計費，團隊可以只採用其中一項能力（例如 AgentCore memory）而不必整套遷移。Runtime 計費依每秒實際 CPU 與記憶體用量計算，且 I/O 等待期間不計 CPU 費用。這點對 Agent workload 特別重要,因為這類工作通常有 30% 到 70% 的時間都在等待模型回應、工具呼叫或資料庫查詢，若用預先配置的算力，這段等待時間也照樣付錢。

🎯 **實務啟示**

當一個組織裡有多個團隊同時在建 Agent 應用，先把身分、guardrails、記憶體、可觀測性這些基礎設施收斂成共用平臺，能省下重複投入的成本，也讓評估與治理有統一的著力點。這篇雖然帶有廠商案例宣傳色彩，但其分層架構與「身分授權貫穿整個呼叫鏈」的設計思路，對任何要規模化多團隊 Agent 部署的工程組織都有參考價值。

🔗 **來源**
- 標題：A shared agentic platform for Wood Mackenzie, on Amazon Bedrock AgentCore
- 作者／機構：Shridhar Navanageri（AWS Machine Learning Blog）
- 連結：https://aws.amazon.com/blogs/machine-learning/a-shared-agentic-platform-for-wood-mackenzie-on-amazon-bedrock-agentcore/

#AgenticAI #AmazonBedrock #AgentCore #AIInfrastructure #EnterpriseAI #MultiAgent #MLOps #CloudArchitecture #AIObservability #AWS
