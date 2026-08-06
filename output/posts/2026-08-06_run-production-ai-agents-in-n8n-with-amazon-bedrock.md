---
title: Run production AI agents in n8n with Amazon Bedrock AgentCore harness
source: AWS ML
url: https://aws.amazon.com/blogs/machine-learning/run-production-ai-agents-in-n8n-with-amazon-bedrock-agentcore-harness/
model: tencent/hy3:free
generated_at: '2026-08-06T08:27:27.172081'
score: 107
---

📌 【AWS 新功能】在 n8n 中打造生產級 AI Agent：透過 Amazon Bedrock AgentCore 實現持久記憶與工具調用

TL;DR：透過新推出的開源 n8n 節點，無需撰寫基礎設施程式碼，即可在 n8n 中使用 AgentCore 架構部署具備持久記憶與工具能力的 AI Agent。

🎣 **從單次模型調用到生產級 Agent 的鴻溝**

在 n8n 中使用內建的 AI Agent 節點來進行單次模型調用（Model Call）非常方便，但要將其推向「生產環境」，僅有模型是不夠的。一個真正的生產級 Agent 需要具備以下能力：
- **持久記憶**：能夠跨越單次執行流程保留對話狀態。
- **工具使用**：能夠操作瀏覽器或在程式碼沙箱（Code Sandbox）中執行指令。
- **任務處理能力**：能夠處理複雜且長期的任務，而非僅僅是單次問答。

開發這些「腳手架」（Scaffolding）通常是工程師最耗時的部分。

🧩 **Amazon Bedrock AgentCore：為 Agent 提供運作骨架**

Amazon Bedrock AgentCore 是一個用於大規模構建、連接與最佳化 Agent 的平臺。其核心能力 **AgentCore harness** 現已正式發佈（GA），它扮演了「架構支撐」的角色。

當模型負責「推理」時，Harness 則負責「執行」：
- 執行編排迴圈（Orchestration loop）。
- 調用工具（Call tools）。
- 管理上下文視窗（Context window）。
- 維持跨回合的狀態（State across turns）。
- 從錯誤中恢復並隔離每個會話（Session isolation）。

🎯 **整合至 n8n：無需基礎設施程式碼的視覺化開發**

透過全新的開源社群節點 `@aws/n8n-nodes-agentcore`，你可以直接在 n8n 的視覺化編輯器中調用完整的 AgentCore 架構。

💡 **關鍵特性與設計理念**
- **多模型支援**：不綁定單一供應商，支援 Amazon Bedrock、OpenAI、Google Gemini 以及所有由 LiteLLM 支援的供應商；甚至可以在同一個對話的不同回合間切換模型。
- **記憶體層級結構**：
  1. **Agent 層**：持有共享的配置。
  2. **Actor ID 層**：將不同使用者的記憶體進行隔離。
  3. **Session ID 層**：在同一個使用者內，隔離不同的對話紀錄。
- **工具與技能（Skills）**：支援加入程式碼解釋器（Code Interpreter）、雲端瀏覽器、遠端 MCP 伺服器，以及從 S3 或 Git 載入的「技能包」（Skills）。
- **VPC 私有化部署**：支援在你的虛擬私有雲（VPC）中運行，確保 Agent 在私有網路環境下運作。

📊 **實作流程與開發重點**

在 n8n 中配置該節點時，主要透過 **Harness ARN** 進行操作。開發流程大致如下：

1. **配置憑證**：使用與 AWS Lambda 或 S3 節點相同的 AWS 憑證模式。
2. **啟動 Agent**：首次執行時，AWS 會自動配置 Agent（約需 30-60 秒），並自動建立受管理的記憶體儲存空間。
3. **建立記憶**：透過提供相同的 `Session ID`，Agent 能從先前的對話中讀取資訊（例如：記住使用者的飲食偏好）。
4. **賦予工具**：例如加入一個沙箱環境下的程式碼解釋器，讓 Agent 能精準計算平均值或標準差，而非僅靠模型估算。
5. **部署至 VPC**：設定 Subnet 與 Security Group，讓 Agent 可以在不經由 NAT Gateway 的情況下，透過 VPC Endpoint 存取 ECR 與 S3。

⚠️ **注意事項與成本管理**
- **權限原則**：建議使用 AWS IAM Identity Center 或 STS 的臨時憑證，並遵循最小權限原則。
- **資源清理**：AgentCore harness、受管理的記憶體儲存空間以及 VPC Endpoints 均會產生 AWS 費用。完成測試後，請務必刪除不再需要的資源。

🎯 **實務啟示**

對於需要將 AI 流程從「實驗」轉向「生產」的工程師來說，AgentCore harness 解決了最困難的基礎設施層面問題。透過 n8n 的視覺化介面，開發者可以快速驗證「具備記憶與工具能力」的 Agent 邏輯，而無需從零開始撰寫複雜的編排與狀態管理程式碼。

🔗 **來源**
- 標題：Run production AI agents in n8n with Amazon Bedrock AgentCore harness
- 作者／機構：Sundar Raghavan @ AWS ML
- 連結：https://aws.amazon.com/blogs/machine-learning/run-production-ai-agents-in-n8n-with-amazon-bedrock-agentcore-harness/

#AI #n8n #AmazonBedrock #AgentCore #AWS #MachineLearning #AIAgents #Automation #OpenSource #CloudComputing
