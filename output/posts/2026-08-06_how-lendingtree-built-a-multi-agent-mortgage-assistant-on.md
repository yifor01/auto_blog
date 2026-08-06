---
title: How LendingTree built a multi-agent mortgage assistant on Amazon Bedrock
source: AWS ML
url: https://aws.amazon.com/blogs/machine-learning/how-lendingtree-built-a-multi-agent-mortgage-assistant-on-amazon-bedrock/
model: tencent/hy3:free
generated_at: '2026-08-06T08:49:56.777723'
score: 72
---

📌 【LendingTree 案例】如何利用 Amazon Bedrock 打造多代理（Multi-agent）房貸助手

TL;DR：LendingTree 透過 Amazon Bedrock 部署三種獨立 AI 代理，實現具備教育功能與產品媒合能力的房貸諮詢。

買房是人生重大的財務決策，但面對「折現點（discount points）」、「發放費（origination fees）」或「債務收入比（DTI）」等專業術語，消費者往往感到無從下手。LendingTree 為了簡化流程，決定超越傳統聊天機器人的範疇，打造一個能回答深層問題並媒合合適貸款方案的 AI 助手。

🤔 **從簡單對話轉向複雜決策的挑戰**

傳統聊天機器人通常只能處理基礎問答，但房貸諮詢涉及極高的合規性要求（如 PII 個人識別資訊保護、內容過濾）以及複雜的邏輯判斷。LendingTree 需要一個既能教育消費者，又能精準對接內部貸款 API 的系統，這需要比單一模型更複雜的架構。

🧩 **三層代理架構：主管、教育者與媒合者**

為了應對複雜任務，LendingTree 採用了多代理架構，透過 LangGraph 進行協調，並利用 Model Context Protocol (MCP) 進行連線：

*   **主管代理 (Supervisor Agent)**：扮演協調者角色。它基於 LangGraph 的狀態機（State Machine）設計，採用「計畫與執行（plan-and-execute）」模式。主管負責分析使用者意圖，並決定要把任務分配給誰。
*   **教育代理 (Education Worker)**：專注於知識傳遞。它使用 RAG（檢索增強生成）技術，透過 Amazon Bedrock Knowledge Bases 連結權威文件，並以 Amazon OpenSearch Service 作為向量資料庫，確保回答內容有據可查，而非僅依賴模型預訓練知識。
*   **媒合代理 (Matching Worker)**：負責執行具體商業邏輯。它會收集使用者偏好，並呼叫 LendingTree 內部的貸款方案、資格與利率 API，提供個人化的貸款選項對比。

📊 **動態模型選擇：在效能與成本間取得平衡**

LendingTree 實作了多模型架構，主管代理會根據任務複雜度自動切換模型：
*   **Amazon Nova Pro**：用於複雜推理與關鍵分類任務。
*   **Amazon Nova Lite**：用於對話式回應與輕量級分類。

這種設計能在確保可靠性的同時，有效控制運算成本。

💡 **高可用與高安全性設計**

為了滿足金融業嚴格的監管要求，該系統在架構中嵌入了多重防護：
*   **雙重安全檢查**：訊息在傳輸時會同時經過 Amazon Bedrock Guardrails（進行內容過濾與 PII 脫敏）以及基於 LLM 的安全性分類器，兩者並行運作且不增加延遲。
*   **對話記憶持久化**：使用 Amazon RDS 上的 LangGraph PostgreSQL checkpointer，確保對話在代理切換或服務重啟後，使用者仍能擁有連續的上下文體驗。
*   **容器化部署**：所有代理服務皆運行在 Amazon ECS (AWS Fargate) 上，各代理可根據需求獨立擴展。

🎯 **實務啟示**

對於需要處理複雜業務邏輯的 AI 應用，單一 Prompt 或單一 Agent 往往難以應對。透過將任務拆解為「主管 + 專業工作者」的模式，並結合 RAG 技術確保事實正確性，開發者可以建立更具專業深度且符合合規要求的企業級 AI 應用。

🔗 **來源**
- 標題：How LendingTree built a multi-agent mortgage assistant on Amazon Bedrock
- 作者／機構：Eric Hanson @ AWS ML
- 連結：https://aws.amazon.com/blogs/machine-learning/how-lendingtree-built-a-multi-agent-mortgage-assistant-on-amazon-bedrock/

#AI #MultiAgent #AmazonBedrock #LLM #LangGraph #RAG #MachineLearning #AWS #FinTech #GenerativeAI
