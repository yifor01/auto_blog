---
title: Building agentic AI applications with a modern data mesh strategy on AWS
source: AWS ML
url: https://aws.amazon.com/blogs/machine-learning/building-agentic-ai-applications-with-a-modern-data-mesh-strategy-on-aws/
score: 103
model: google/gemma-4-31b-it:free
generated_at: '2026-06-25T20:20:36.767169'
---

📌 【AWS 技術分享】Agentic AI 的治理挑戰：為何 RAG 的單點許可權控制不再足夠？

TL;DR：針對 Agentic AI 的自主查詢特性，AWS 提出一套基於 Data Mesh 的多層次治理架構，確保資料存取安全。

當 AI Agent 能自主探索資料庫 Schema、撰寫 SQL 並整合多個來源的答案時，傳統 RAG 的「單點檢查」模式就失效了。如果許可權控制僅在檢索階段，Agent 可能在自主執行工具時，意外觸及不應存取的敏感資料。

🤔 **從 RAG 到 Agentic AI：治理邏輯的根本轉變**

在典型的 RAG 應用中，資料互動相對簡單：從預建的向量索引檢索片段 $\rightarrow$ 根據 metadata 過濾 $\rightarrow$ 呈現結果。這種單一檢查點的模式足以應對。

但 Agentic AI 的行為更複雜，它具備「自主發現」的能力。當 Agent 開始自主查詢訂單資料庫或檢索退貨政策時，治理範圍必須從單純的「結果過濾」擴展到整個互動鏈條：從工具發現、查詢執行到最終的答案合成，每一環節都必須有嚴格的許可權控制。

🧩 **基於 Data Mesh 的多層次治理架構**

為了滿足生產環境的需求，AWS 提出一套 Serverless Data Mesh 架構，將授權控制分散在四個層級，避免單一失效點（Single Point of Failure）導致資料外洩：

1. **Agent Layer（代理層）**：由 AgentCore Runtime 與 LangGraph agent 組成，負責處理客戶請求與邏輯編排。
2. **Gateway Layer（閘道層）**：部署請求與回應攔截器（Interceptors），在資料進出時進行初步攔截。
3. **Tools Layer（工具層）**：提供四個由 AWS Lambda 驅動的 MCP 工具，包括：
    - `get_user_tables`：獲取使用者可見的資料表。
    - `get_schema`：獲取資料表結構。
    - `run_query`：執行實際查詢。
    - `kb_search`：執行知識庫搜尋。
4. **Governed Data Mesh（治理資料網格層）**：底層由 S3 Tables、Athena、Lake Formation 與 S3 Vectors 組成，實現細粒度存取控制 (FGAC)。

🎯 **實務啟示：建立「全鏈路」的授權體系**

對於開發企業級 AI Agent 的工程師而言，這帶來一個關鍵啟示：不能將安全性僅視為「資料檢索後的過濾」。在設計 Agentic AI 時，必須將許可權控制內嵌到工具呼叫（Tool Use）的每一個步驟中。

從「能看到哪些表」$\rightarrow$ 「能讀取哪些欄位」$\rightarrow$ 「能執行什麼查詢」，每一層都應有獨立的授權驗證，才能在賦予 Agent 自主能力的同時，維持企業級的資料治理標準。

🔗 **來源**
- 標題：Building agentic AI applications with a modern data mesh strategy on AWS
- 作者／機構：Venkata Sistla @ AWS ML
- 連結：https://aws.amazon.com/blogs/machine-learning/building-agentic-ai-applications-with-a-modern-data-mesh-strategy-on-aws/

#AI #AgenticAI #AWS #DataMesh #DataGovernance #RAG #LakeFormation #Serverless #LLM #CyberSecurity
