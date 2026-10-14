---
title: Generate presentations with Amazon Bedrock AgentCore
source: AWS ML
url: https://aws.amazon.com/blogs/machine-learning/generate-presentations-with-amazon-bedrock-agentcore/
model: nvidia/nemotron-3-ultra-550b-a55b:free
generated_at: '2026-10-14T21:04:41.105345'
score: 78
---

📌 用 Amazon Bedrock AgentCore 自動產出客戶簡報，90 秒搞定上百頁財報分析

TL;DR：AWS 示範用 AgentCore Runtime 編排 Supervisor Agent，結合 RAG 與多模型工具，將手動製作 PPT 的流程壓縮至 90 秒內。

金融服務團隊每週都要花大量時間把財報、合規文件、市場分析整理成客戶簡報，動輒閱讀數百頁、抽取關鍵數據、排版、產圖。AWS 機器學習部落格最新實作展示：透過 Amazon Bedrock AgentCore 建立的 AI Agent 系統，能在內部測試環境下於 90 秒內完成這套流程，且內容皆落地於來源文件。

🧩 **Supervisor Agent + 工具導向架構，而非單體函式**

單一 Agent 若要同時負責檢索、大綱、生文、生圖、組裝 PPTX，職責過重。方案採用工具導向設計：部署單一 Supervisor Agent 於 AgentCore Runtime，依請求判斷呼叫「文件生成工具」或「摘要生成工具」。新增能力只需在 Agent 程式碼定義新工具，既有工具不受影響。

- **AgentCore Runtime**：提供隔離容器、Session 管理、內建身分識別與可觀測性，支援任意框架與模型。
- **Strands Agents SDK**：開源框架實作 Supervisor 邏輯，於 `agent/app.py` 定義系統提示與行為，`agent/tools.py` 宣告兩支工具。
- **模型組合**：Anthropic Claude Sonnet 4.6（內容創作）、Amazon Titan Text Embeddings v2（向量檢索）、Stability AI Stable Image Inpaint（投影片配圖），皆透過 Amazon Bedrock 取用。

📊 **RAG 落地企業知識庫，降低幻覺風險**

核心資料流：文件存放於 Amazon S3 → 切塊、嵌入（Titan Text Embeddings v2） → 寫入 Amazon OpenSearch Serverless 向量索引 → Supervisor Agent 呼叫工具時，以 `retrieve_and_generate` API 檢索相關片段 → 作為 Claude Sonnet 4.6 的上下文生成回應。

> 註：OpenSearch Serverless Collection 的 Data Plane 必須保持公開可存取，因 Bedrock Knowledge Bases 從 AWS 代管基礎設施存取，而非客戶 VPC Endpoint。資料層面以 IAM Data Access Policy 保護，儀表板僅限 VPC 存取。

⚠️ **內建 Guardrails 多層把關**

Amazon Bedrock Guardrails 透過 AWS CDK 部署自定義策略，於模型呼叫層級統一套用，涵蓋文件生成管線的多個階段，滿足企業合規與內容安全需求，免去逐個部署手動配置。

🔧 **企業級整合：.NET 8 Minimal API + 容器化 Lambda + VPC 隔離**

- **對外介面**：Amazon API Gateway → .NET 8 Minimal API（AWS Lambda） → Amazon DynamoDB 維護對話狀態 → 呼叫 AgentCore Runtime Endpoint。
- **文件生成工具**：PPTX Generator Lambda（Python 容器映像，經 Docker/Finch 建構、推至 Amazon ECR）。
- **摘要工具**：Summary Generator Lambda 直接查詢 Knowledge Base。
- **輸出**：生成檔案存回 S3，回傳預簽 URL 供下載。
- **安全性**：Amazon VPC 隔離、AWS KMS 加密、IAM 最小權限。

🚀 **三階段部署：建構 → 基礎設施 → AgentCore Runtime**

專案提供公開倉庫與 CDK 腳本，部署流程：
1. **建構階段**：`build.sh` 編譯 .NET 專案、建構 PPTX Generator 容器映像、推送 ECR、產出 `asset-output`。
2. **基礎設施階段**：`deploy.sh` 依序建立四個 CloudFormation Stack（網路、資料、應用、AgentCore 資源）。
3. **Agent 部署**：`deploy-agentcore.sh` 建構 Supervisor Agent 容器（ARM64）、推送 ECR、建立 AgentCore Runtime 與 Endpoint、寫入 Systems Manager Parameter Store 供 Chat API 參考。

部署完成後，CloudFormation 輸出 API Gateway 端點與資源識別碼即可串接。

🎯 **實務啟示：把「文件密集型流程」拆解為 Agent + Tools + RAG 的標準化樣板**

這個範例雖以財報生 PPT 為切入點，但其架構模式可泛化至任何「大量非結構化文件 → 結構化輸出」的場景：合約審閱產出摘要報告、法規文件生成合規檢核表、技術手冊轉訓練教材。關鍵在於：
- 用 **Supervisor Agent 路由工具** 取代巨石式 Prompt，擴充性更強。
- **AgentCore Runtime** 解決容器化、Session、身分、觀測的基建負擔。
- **Knowledge Bases + OpenSearch Serverless** 提供受管 RAG，工程師專注於切塊策略與檢索品質調校。
- **Guardrails 在模型層統一套用**，合規成本攤平。

若團隊正評估將文件處理自動化納入產品路線圖，此倉庫可作為可直接部署、可客製化的參考實作起點。

🔗 **來源**
- 標題：Generate presentations with Amazon Bedrock AgentCore
- 作者／機構：Ian Lunsford @ AWS Machine Learning Blog
- 連結：https://aws.amazon.com/blogs/machine-learning/generate-presentations-with-amazon-bedrock-agentcore/

#AWS #Bedrock #AgentCore #GenerativeAI #RAG #LLM #Automation #PresentationGeneration #EnterpriseAI #StrandsAgents
