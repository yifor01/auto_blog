---
title: How Circle K accelerated DevOps incident triage to under 15 minutes with Amazon
  Bedrock
source: AWS ML
url: https://aws.amazon.com/blogs/machine-learning/how-circle-k-accelerated-devops-incident-triage-to-under-15-minutes-with-amazon-bedrock/
model: claude-code/sonnet
generated_at: '2026-11-03T00:09:09.725809'
score: 85
---

📌 Circle K靠Amazon Bedrock，把事故排查壓到15分鐘內

TL;DR：Circle K用Amazon Bedrock打造自動化事故分析agent，平均排查時間降到15分鐘內。

警報響起，工程師得先花45到60分鐘翻log、查服務健康狀態、在幾個工具之間交叉比對症狀，才能真正開始修復。這是許多DevOps團隊熟悉的模式，而Circle K把它變成了可被自動化取代的流程。

🤔 門市越開越多，警報也跟著線性成長

Circle K在27個國家營運超過17,200家便利商店與加油站，背後是支撐POS系統、會員應用程式與電動車充電服務的雲端原生架構，全部跑在AWS上。隨著數位業務擴張，每多一個服務上線，就多一組警報，而每一組警報都要重複同一套人工調查流程：查Amazon CloudWatch裡的log、看Amazon OpenSearch Service裡的應用層追蹤、確認Amazon ECS任務狀態、再對照GitHub上的內部runbook。這套流程能解決問題，但也暴露出重複性context收集的成本，以及排查深度會因值班工程師對該服務的熟悉程度而有落差。

🧩 兩個平行agent先查,再交給熟悉脈絡的agent收尾

團隊評估過在自建基礎設施上採用開源agent框架，但那意味著要自己負責model hosting、prompt版本管理、tool orchestration與安全控制。最終選擇Amazon Bedrock，因為公司本就跑在AWS上，Bedrock可以直接套進既有的IAM政策、VPC設定與日誌流程，同時Amazon Bedrock不會把客戶資料分享給模型供應商，也不會用來訓練基礎模型，符合Circle K對事故資料（可能包含敏感資訊）的安全要求。

整體管線從Grafana警報開始：警報發到Amazon SNS，轉送到Amazon SQS佇列，一個AWS Lambda函式輪詢佇列、取出警報內容，觸發以Amazon Bedrock Flows建置的orchestration流程。流程內，兩個agent平行執行：AWSResourceExplorerAgent查詢跨多個AWS Organizations帳戶的基礎設施，包括ECS任務狀態、Application Load Balancer目標健康度，以及CloudWatch指標與log；OpenSearchExplorerAgent則查詢OpenSearch裡的應用層log與分散式追蹤，因為OpenSearch回傳的log資料量大，獨立出一個agent可以讓每個agent的context window保持可控，這個agent同時也是唯一能存取describing各服務與其依賴關係的knowledge base（以Bedrock Knowledge Bases做RAG）的agent。兩個agent完成後，GitHubExplorerAgent才接著執行，它拿到前兩者的輸出，找到受影響服務的GitHub repository，搜尋應用程式碼、基礎設施定義與最近的commit，鎖定問題來源並提出具體修復建議——放在平行agent之後執行，是因為它已經知道該查什麼，而不用做大範圍的搜尋。三個agent的輸出最後匯入一個不帶任何工具的AnalysisPrompt節點，由它產出結構化摘要：可能根因、支持證據、受影響的服務與負責人、建議的修復步驟，再由Lambda貼回Slack頻道。

📊 從45分鐘到15分鐘，一個實例走過整條管線

以文中的範例警報為例：某服務的HTTP 5xx錯誤率連續3分鐘超過5%，觸發警報。AWSResourceExplorerAgent查到目標帳戶內ECS任務健康狀態異常，資料庫連線池耗盡，ECS服務正在嘗試重啟；OpenSearchExplorerAgent則回報應用log中出現該服務連到後端PostgreSQL資料庫時的「connection refused」錯誤。整個流程從警報發出到Slack摘要送達，耗時5到15分鐘，依事故複雜度而定。Circle K內部事故回應指標顯示，部署這套系統後，平均排查時間降到15分鐘以內，相當於縮短67到75%。

💡 用managed服務換掉自建orchestration的重擔

這套架構的關鍵選擇，是把agent orchestration與RAG能力都交給managed服務：Bedrock提供agent原生的tool use能力，可以直接呼叫AWS API、查資料庫、檢索文件，不需要自己寫orchestration程式碼；Bedrock Knowledge Bases則處理內部product card的ingestion與檢索，團隊不必額外維運一個向量資料庫。這讓DevOps團隊把精力放在prompt設計與tool定義上，而不是基礎設施管理。文中也提到團隊之後進一步把架構遷移到Amazon Bedrock AgentCore，但這部分的細節與教訓屬於後續內容，本篇素材未詳述。

🎯 實務啟示

這個案例的方法本身並不新穎——平行查詢、依序收斂、單次呼叫產出結構化摘要，是常見的agentic pipeline設計——但它示範了把「重複性的context收集」自動化、同時保留工程師判斷空間的具體做法：讓on-call工程師收到的不是原始警報，而是已經整理好根因、證據與建議動作的摘要，才是縮短MTTR的關鍵。

🔗 來源
- 標題：How Circle K accelerated DevOps incident triage to under 15 minutes with Amazon Bedrock
- 作者／機構：Marek Klatowicz，AWS Machine Learning Blog
- 連結：https://aws.amazon.com/blogs/machine-learning/how-circle-k-accelerated-devops-incident-triage-to-under-15-minutes-with-amazon-bedrock/

#AWS #AmazonBedrock #DevOps #IncidentResponse #AgenticAI #LLM #CloudOps #SRE #RAG #Automation
