---
title: How nOps shipped FinOps agents 75% faster with Amazon Bedrock AgentCore
source: AWS ML
url: https://aws.amazon.com/blogs/machine-learning/how-nops-shipped-finops-agents-75-faster-with-amazon-bedrock-agentcore/
model: tencent/hy3:free
generated_at: '2026-08-11T07:06:46.696804'
score: 94
---

📌 【AWS 案例】從 API 依賴轉向 Agent-Native：nOps 如何利用 Amazon Bedrock AgentCore 提升 75% 的交付速度

TL;DR：nOps 透過轉向 Amazon Bedrock AgentCore 與 Databricks 協作，將 FinOps 代理程式從複雜的 API 堆疊轉型為統一的代理原生架構。

隨著企業雲端支出（AWS、GCP、Azure）日益複雜，傳統的 FinOps（財務營運）分析需要處理極高精確度的數據。nOps 作為雲端優化方案，正致力於透過 AI 代理（Agent）自動化處理預留實例（RI）與節省計畫（Savings Plans）等複雜任務。然而，隨著業務規模擴張，原本基於 API 堆疊的架構遇到了嚴重的開發瓶頸。

🤔 **舊架構的瓶頸：開發速度與精準度的拉鋸戰**

在初期階段，nOps 透過 Kubernetes、LangChain/LangGraph 以及包裝後的 Web API 來構建 FinOps AI 代理「Clara」。雖然這能快速完成初步交付，但也暴露了結構性限制：

- **開發摩擦**：現有的基礎設施並非為「以分析為驅動的代理程式」設計，導致迭代速度緩慢且複雜。
- **精準度問題**：試圖在非專用基礎設施上構建進階 AI 能力，容易導致結果不準確。
- **維護負擔**：隨著產品組合與客戶群擴大，維護高度可靠且具備多租戶隔離性的複雜工作流變得極具挑戰。

🧩 **架構轉型：從 API 依賴轉向 Agent-Native**

為了加速產品交付並提升回應品質，nOps 棄用了舊有的架構，轉而採用以 Amazon Bedrock AgentCore 為核心的專用架構。

**1. 核心編排與執行 (Orchestration)**
nOps 選擇 Amazon Bedrock AgentCore 作為執行時（Runtime）與編排中心。這讓工程師能專注於領域邏輯（Domain Logic），而非基礎設施。
- **單一代理架構**：不同於複雜的多代理路由器（Multi-agent router），Clara 採用單一代理架構，直接透過 Strands 工具存取畫布操作、查詢執行、資料源發現與工作流編排。這避免了代理間傳遞導致的延遲與錯誤傳播。
- **記憶體策略**：利用 AgentCore 記憶體實現三種策略：語義事實（Semantic facts）、使用者偏好（User preferences）與畫布摘要（Canvas summaries），讓 AI 能隨著使用時間增加而學習使用者的行為。

**2. 數據層的革命：引入 Metric Views 確保數據一致性**
過去，AI 必須透過模型上下文協定（MCP）在每次查詢時重新計算複雜的商業邏輯（如：扣除折扣後的真實成本），這極易出錯。
- **解決方案**：透過 Databricks Lakehouse Metric Views 提供受控的語義層。
- **實作差異**：
  - **原始 SQL/MCP 方式**：模型必須每次都重新計算各種 AWS 定價計畫與折扣後的加總。
  - **Metric View 方式**：模型只需查詢預定義的指標（例如：`true_customer_cost`）與維度（例如：`account_name`）。這確保了對話中的答案與儀表板（Dashboard）的輸出完全一致。

**3. 狀態與安全隔離**
- **持久化狀態**：使用 Databricks Lakebase（Serverless PostgreSQL）儲存產品物件、對話會話與查詢規格，讓分析洞察可以轉化為可分享的持久化分析產出。
- **租戶隔離**：利用 Amazon Bedrock Guardrails 在代理執行前進行預檢，執行跨租戶數據存取政策檢查與提示詞攻擊（Prompt-attack）偵測。

📊 **從 API 驅動轉向代理原生帶來的價值**

透過這次轉型，nOps 成功實現了以下目標：
- **提升交付速度**：產品交付速度提升了 75%。
- **降低運維複雜度**：透過受管理的代理執行時環境與單一 AWS CDK Stack，簡化了部署流程。
- **提升分析精準度**：透過受控的語義層，解決了 AI 在處理複雜財務邏輯時的不確定性。

🎯 **實務啟示**

對於需要處理高度結構化數據的 AI 應用，**「不要讓 LLM 去學習複雜的商業邏輯，而是讓 LLM 去查詢已經定義好的指標（Metrics）」**。將複雜的計算邏輯封裝在資料層（如 Metric Views），而非讓模型在 Prompt 中進行計算，是確保企業級 AI 應用精準度的關鍵。

🔗 **來源**
- 標題：How nOps shipped FinOps agents 75% faster with Amazon Bedrock AgentCore
- 作者／機構：Jordan Stein @ AWS ML
- 連結：https://aws.amazon.com/blogs/machine-learning/how-nops-shipped-finops-agents-75-faster-with-amazon-bedrock-agentcore/

#AI #FinOps #AWS #AmazonBedrock #AgenticAI #Databricks #CloudOptimization #MachineLearning #LLM #CloudComputing
