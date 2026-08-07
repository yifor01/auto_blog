---
title: Building an agentic app deployer with Amazon Bedrock and AWS Lambda
source: AWS ML
url: https://aws.amazon.com/blogs/machine-learning/building-an-agentic-app-deployer-with-amazon-bedrock-and-aws-lambda/
model: tencent/hy3:free
generated_at: '2026-08-07T07:35:22.118640'
score: 92
---

📌 【AWS 技術解析】用 Agentic Pattern 解決企業內部工具開發的長尾問題

TL;DR：透過「規劃代理」與「配置代理」分離的架構，讓非技術員工能透過自然語言部署 Web App。

🤔 **企業內部的「小工具」開發困境**

在許多企業中，存在大量需求卻無法落實的內部工具。例如：運費計算器、簡單的表單或針對試算表的儀表板。這些工具規模太小，不足以排入開發者的 Backlog，但數量卻多到無法忽視。傳統的部署流程（包含 Repository、CI/CD、身份驗證、DNS 與維護）對非技術團隊來說門檻太高，導致這些需求被無限期擱置。

PDI Technologies 為了打破這個僵局，開發了 **PDI Brew**。這是一個讓員工只需用英文描述需求，幾秒鐘內就能獲得一個完整配置、具備 SSO 登入功能且運行在 AWS 上的多租戶 Web 應用程式的系統。

🧩 **雙代理架構：分離「意圖」與「執行」**

PDI Brew 採用了一種「Agentic Provisioning Pattern」（代理配置模式），將系統拆解為兩個具有不同信任層級（Trust Profiles）的代理：

1.  **規劃代理 (Planning Agent) —— 負責捕捉意圖**
    *   **職責**：與使用者對話、協助細化需求、生成前端介面，並最終輸出一個結構化的 **部署清單 (Deploy Manifest)**（包含應用名稱、類型、資料 Schema 與存取控制設定的 JSON 格式）。
    *   **兩種路徑**：
        *   **Path A (Vibe Skill)**：作為技能整合在現有的 AI 助手（如 Claude、ChatGPT）中，提供豐富的對話體驗。
        *   **Path B (Amazon Bedrock)**：在 AWS 信任邊界內透過 Bedrock 進行模型調用，確保數據不流出 AWS 邊界，適合對數據駐留有嚴格要求的團隊。

2.  **配置代理 (Provisioning Agent) —— 負責確定性執行**
    *   **實作**：運行於 **AWS Lambda** 上。
    *   **職責**：接收 JSON 部署清單，進行工作負載分類，並將 AWS SDK for JavaScript v3 與 Microsoft Graph API 作為工具進行編排。
    *   **特性**：為了避免 AI 幻覺（Hallucination），配置過程是決定性（Deterministic）且可審核的。

📊 **非同步編排與資源配置流程**

當部署清單傳遞至 Lambda 後，配置代理會根據需求選擇路徑：
*   **靜態應用**：僅配置 S3、CloudFront 與 DynamoDB 註冊表。
*   **全端應用**：除了上述資源，還會驅動 DynamoDB、API Gateway，以及針對需要 AI 能力的應用配置 Lambda 與 IAM。
*   **身份管理**：透過 Microsoft Graph API 建立並管理 M365 群組。

針對耗時較長的步驟（例如 M365 群組的目錄同步），Lambda 會使用 **非同步自我調用 (Asynchronous Self-invocation)**，即透過 `lambda:InvokeFunction` 的 `Event` 類型模式在背景執行，並立即回傳應用程式 URL 給使用者，避免同步請求超時。

💡 **解耦後的架構優勢**

*   **安全性與治理**：每個應用程式都繼承相同的平臺標準，並能選擇性地啟用受控的 AI 能力（如對話、摘要、分類），且開發者無需直接接觸模型端點或 API Key。
*   **靈活性**：透過 `PLANNER_MODE` 環境變數，企業可以針對不同組織或工作區，自由切換使用「AI 助手模式」或「Bedrock 模式」。
*   **擴展性**：規劃層與配置層分離，未來若要將 Bedrock 調用替換為更強大的託管代理運行時（Managed Agent Runtime），完全不會影響現有的部署流程。

🎯 **實務啟示**

對於需要快速迭代內部工具的工程團隊，這種「規劃與執行分離」的模式提供了極高的安全性與穩定性。透過將「不確定性」的語言理解留在規劃層，而將「確定性」的資源配置交給 Lambda 執行，可以有效降低 AI 引入的風險，同時大幅提升非技術人員的開發效率。

🔗 **來源**
- 標題：Building an agentic app deployer with Amazon Bedrock and AWS Lambda
- 作者／機構：Ramesh Kadali @ AWS ML
- 連結：https://aws.amazon.com/blogs/machine-learning/building-an-agentic-app-deployer-with-amazon-bedrock-and-aws-lambda/

#AWS #AmazonBedrock #AWSLambda #GenerativeAI #AgenticWorkflow #CloudComputing #Serverless #SoftwareEngineering #DevOps #PDI_Technologies
