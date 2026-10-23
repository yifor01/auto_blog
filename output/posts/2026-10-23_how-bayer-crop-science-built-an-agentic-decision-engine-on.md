---
title: How Bayer Crop Science built an agentic decision engine on Amazon Bedrock AgentCore
  with AWS Unified Operations
source: AWS ML
url: https://aws.amazon.com/blogs/machine-learning/how-bayer-crop-science-built-an-agentic-decision-engine-on-amazon-bedrock-agentcore-with-aws-unified-operations/
model: claude-code/sonnet
generated_at: '2026-10-23T20:45:41.519784'
score: 83
---

📌 Bayer用Bedrock AgentCore打造決策引擎，8成問題不用找工程師

TL;DR：Bayer Crop Science用AWS Bedrock AgentCore打造多agent自然語言介面,讓育種決策查詢自動化,上線後八成問題不需工程師介入。

育種人員想知道一個workflow昨天為什麼失敗,過去得靠人工翻日誌、等工程師支援,可能耗掉一個多小時。Bayer Crop Science的新系統,把這個時間壓到十分鐘以內。

🤔 **當「跑workflow」不再是瓶頸,「看懂workflow」才是**

Bayer Crop Science的育種決策需要橫跨基因體學、田間試驗、影像、環境條件與模型輸出的資料。公司先建了Connected Decision Engine(CDE),讓育種人員、分析師、研究員、資料科學家與資料工程師能用一致的方式執行數百組機器學習模型配置,同時保留執行歷程與操作控管。但隨著採用度上升,瓶頸從「跑workflow」轉移到「理解workflow」——想知道一個workflow為什麼失敗、一個模型做了什麼、一個結果從哪裡來,使用者得自己知道該去哪個系統查:API、文件、metadata store、dashboard、日誌,樣樣都要摸過一輪。

🧩 **supervisor agent routing + 22個領域專家agent**

為了補上這個落差,Bayer建了Agentic Decision Engine(ADE),一個架在CDE上的多agent自然語言介面。使用者透過React前端提出問題,請求先經過Microsoft Entra ID的身分驗證代理,再進入agent層。GitHub Actions負責建置agent容器映像檔,推送到Amazon ECR,再部署到Amazon Bedrock AgentCore runtime。

架構核心是一個Supervisor Agent,用LangGraph(團隊看重它明確的圖狀控制流程與多步驟workflow的checkpointing能力)做orchestration,負責分類每個請求、選擇對應的專家agent,並在問題跨領域時整合多個答案。ADE在生產環境中跑了22個專家agent,每個都只專注一個領域:Domain Expert Agent透過RAG回答概念性問題,Operational Agent從CDE抓即時workflow狀態與結果,Troubleshooting Agent分析維運telemetry,Visualization Agent產生圖表或回傳既有dashboard。另外有一個客製化的「Models as Skill」機制,把模型程式碼與文件轉成技能定義存進中央登錄庫,讓agent能根據模型實際實作回答,而非憑通用模型知識瞎猜。

資料層依職責分開:DynamoDB存LangGraph的checkpoint狀態,Aurora PostgreSQL存session紀錄、使用者回饋與分析資料,ElastiCache用TTL快取agent回應,S3上的領域內容經Amazon Titan Text Embeddings V2嵌入後存進Amazon OpenSearch Serverless做RAG,CloudWatch負責runtime與應用程式telemetry。AgentCore Gateway把後端API以Model Context Protocol(MCP)工具的形式暴露給agent,並把身分驗證與授權邏輯留在agent程式碼之外。

舉例來說,當育種人員問「我的phenotyping workflow昨天為什麼失敗?」,Supervisor會判斷意圖並路由給Troubleshooting Agent,該agent讀取CloudWatch的telemetry,並透過AgentCore Gateway查CDE API拿到的workflow狀態,找出失敗點,再經Supervisor回傳診斷結果。

為了準備上線並在上線後維運ADE,Bayer找了AWS Unified Operations合作,配置了一位Technical Account Manager(TAM)與一位生成式AI領域專家工程師(DSE),兩人作為ADE團隊的延伸成員,從設計階段一路跟到生產環境,每週三次技術站會一起做設計決策。

💡 **三個值得借鏡的架構決策**

Bayer團隊在建置過程中有幾個原則值得其他企業agent專案參考:

- **執行context用session,恢復能力靠持久化儲存**:AgentCore runtime提供的隔離session能在單次session生命週期內保留執行context,但不是可靠的持久化儲存。ADE把LangGraph的checkpoint寫進DynamoDB,讓graph在擴縮容、重啟或跨越session邊界後仍能恢復,不必依賴某個執行環境一直存活。
- **身分驗證按信任邊界分開處理,不要一個token用到底**:Bayer的使用者身分統一用Microsoft Entra ID,但ADE內部服務之間用AWS原生機制互相授權。團隊沒有硬套一個token跨所有信任邊界,而是讓Entra ID維持使用者身分來源,IAM負責服務間呼叫授權,AgentCore Gateway的outbound授權處理對CDE的存取,再用一個Lambda請求攔截器做客製驗證並傳遞下游工具需要的授權屬性。團隊的心得是:agent系統裡的身分問題常常集中在使用者身分、agent身分、工具身分三者的交接處,每個環節都要明確定義issuer、audience、claims、scope與憑證有效期,而不是沿用上一站的token。
- **新模型版本上線前先驗證相容性**:團隊在建置期間曾評估一個啟用reasoning模式的新模型版本,發現它在工具呼叫與結構化輸出的組合上,與ADE既有的agent實作方式不相容。

📊 **上線成效**

ADE第一階段上線後,約八成的使用者問題不需工程師介入就能解決;以Troubleshooting Agent為例,原本需要工程師耗時一小時以上翻日誌、等支援的診斷流程,現在壓縮到十分鐘以內。

⚠️ **這是系統整合案例,而非新演算法**

這個案例的價值更多在於工程落地的細節——身分邊界設計、狀態持久化、模型版本相容性驗證——而非全新的AI方法。對於想複製這套架構的團隊來說,這些維運層面的決策,反而是最容易被低估、卻最容易踩雷的部分。

🎯 **實務啟示**

建置企業級多agent平臺時,可以直接借用Bayer的三個原則:把「執行用的session」和「可恢復用的持久化狀態」分開設計;依信任邊界(使用者、agent、工具)分別定義身分驗證機制,而不是圖方便共用一個token;升級底層模型版本前,務必先驗證工具呼叫與結構化輸出的相容性,避免上線後才發現agent行為跑掉。

🔗 **來源**
- 標題：How Bayer Crop Science built an agentic decision engine on Amazon Bedrock AgentCore with AWS Unified Operations
- 作者／機構：Subbu Dandamudi（AWS ML Blog）
- 連結：https://aws.amazon.com/blogs/machine-learning/how-bayer-crop-science-built-an-agentic-decision-engine-on-amazon-bedrock-agentcore-with-aws-unified-operations/

#AWS #BedrockAgentCore #MultiAgent #EnterpriseAI #LangGraph #AgenticAI #CropScience #MachineLearning #CloudArchitecture #AIOps
