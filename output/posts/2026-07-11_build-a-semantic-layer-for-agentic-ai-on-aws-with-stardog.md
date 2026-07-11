---
title: Build a semantic layer for agentic AI on AWS with Stardog and Amazon Bedrock
  AgentCore
source: AWS ML
url: https://aws.amazon.com/blogs/machine-learning/build-a-semantic-layer-for-agentic-ai-on-aws-with-stardog-and-amazon-bedrock-agentcore/
score: 87
model: google/gemma-4-31b-it:free
generated_at: '2026-07-11T09:53:08.103816'
---

📌 **AWS 實戰：用 Stardog 與 AgentCore 打造 Agentic AI 語意層**

TL;DR：透過 Stardog 建構語意層，讓 Amazon Bedrock AgentCore 無需 ETL 即可跨 Aurora 與 Redshift 進行 Agentic Analytics。

🎣 **當 AI 代理不再只是聊天機器人**

企業分析領域追尋了一個目標：縮短商業問題到可信賴答案之間的距離。從排程報表到儀錶板，再到自助式 BI，瓶頸始終在於人類分析師必須等待資料工程師建立好模型。現在，生成式 AI 代理帶來了新的一步：它們不再只是呈現資料，而是對資料進行推理。

🤔 **Agentic Analytics 的核心挑戰：資料分散且定義不一致**

基礎模型（Foundation Model, FM）已具備規劃多步驟工作流程、推理 Schema 並產生 SQL 的能力，足以扮演初級分析師的角色。然而，真正的難點在於模型推理的底層資料。企業資料散落在不同系統中，對同一事物的定義往往不同。例如，CRM 系統中的「客戶」可能與計費系統中的「客戶」不是同一筆記錄；北美團隊計算的「營收」可能與歐洲團隊計算的數字不一致。這使得直接讓 LLM 查詢資料庫變得困難且容易出錯。

🧩 **解決方案：Stardog 語意層結合 Amazon Bedrock AgentCore**

這篇來自 AWS ML 的文章展示瞭如何利用 Stardog 的 Semantic AI Application 建構一個語意層，並執行 Strands Agents 代理在 Amazon Bedrock AgentCore 上。該架構的關鍵在於：

1.  **無需 ETL 的跨來源查詢**：Stardog 連線 Amazon Aurora 和 Amazon Redshift，透過語意對映解決資料定義不一致的問題，讓代理可以直接查詢這些來源回答「客戶 360 度」等複雜問題，而不需要事先進行 Extract, Transform, Load (ETL)。
2.  **AgentCore 的整合優勢**：選擇 AgentCore 是因為它將入站認證（inbound auth）、託管服務與工具憑證整合為單一受管理服務，簡化了部署複雜性。
3.  **靈活的部署架構**：相同的 Stardog 部署可運作在多種 AWS 運算環境背後，包括 Amazon Elastic Kubernetes Service (EKS)、Amazon Elastic Container Service (ECS) 以及 AWS Lambda，提供工程師彈性選擇基礎設施的能力。

💡 **深入分析：從視覺化到自主推理**

這種方法標誌著從「視覺化資料」到「推理資料」的轉變。Agentic Analytics 意味著每個商業使用者旁邊都有一個自主代理，即時對公司活躍資料進行推理、計劃與迭代，無需排隊等待人工分析。對於工程師而言，這意味著資料管道的維護成本可能降低，因為語意層抽象了底層異質資料庫的複雜性，讓 AI 代理能透過統一的語意視角訪問資料。

⚠️ **限制與注意事項**

根據提供的素材，此方案依賴 Stardog 作為語意中介層來處理資料不一致性。雖然這減少了傳統 ETL 的需求，但仍需正確配置 Stardog 與 Aurora/Redshift 的連線，並在 AgentCore 中妥善管理工具憑證與認證。此外，素材指出基礎模型本身並非瓶頸，真正的挑戰在於確保語意層能準確反映業務邏輯，這需要持續的維護與驗證。

🎯 **實務啟示**

對於正在探索 Agentic AI 的工程團隊，若面臨多源異構資料庫（如 OLTP 與 OLAP 混合）且希望快速實現自然語言查詢能力，可考慮引入語意層（Semantic Layer）作為中介軟體。利用 Amazon Bedrock AgentCore 的託管特性，可以加速代理的建置與部署週期，專注於業務邏輯的語意建模，而非基礎設施的搭建。

🔗 **來源**
- 標題：Build a semantic layer for agentic AI on AWS with Stardog and Amazon Bedrock AgentCore
- 作者／機構：Navin Sharma @ AWS ML
- 連結：https://aws.amazon.com/blogs/machine-learning/build-a-semantic-layer-for-agentic-ai-on-aws-with-stardog-and-amazon-bedrock-agentcore/

#AWS #Bedrock #AgenticAI #SemanticLayer #Stardog #DataAnalytics #MachineLearning #Aurora #Redshift #AgentCore
