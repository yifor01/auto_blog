---
title: 'AWS vector solutions: Build agentic AI where your data lives'
source: AWS ML
url: https://aws.amazon.com/blogs/machine-learning/aws-vector-solutions-build-agentic-ai-where-your-data-lives/
model: claude-code/sonnet
generated_at: '2026-08-21T06:37:04.472424'
score: 85
---

📌 向量不搬家:AWS把RAG檢索層做進既有資料庫

TL;DR：AWS主張向量該留在資料原本的家,六種既有服務內建向量搜尋,agent不必搬資料就能檢索上下文。

建置agentic AI系統時,最容易被低估的成本往往不是模型推理,而是把資料搬進一個全新的向量資料庫。AWS這篇文章提出一個相反的原則:讓向量留在資料原本所在的地方。

🤔 知識早就分散在你熟悉的資料庫裡

Agent要規劃、推理並跨多步驟workflow執行任務,快速存取組織知識是關鍵,而這些知識本來就分散在資料庫、物件儲存、搜尋引擎,以及PDF、通話錄影等非結構化來源裡。

🧩 「向量跟著資料走」的決策模型

AWS的核心主張是:如果資料已經在Amazon OpenSearch Service、Amazon S3、Amazon Aurora PostgreSQL、Amazon DynamoDB、Amazon ElastiCache for Valkey或Amazon Neptune裡,就直接在原地加上向量搜尋,不必為此再新增一個服務。這樣可以省去跨服務搬移資料的延遲、免除學習新API/SDK的成本,也能沿用既有資料庫在生產環境驗證過的擴展性與可用性。對於沒有既有資料儲存的全新workload,AWS建議依延遲、成本、存取模式三個主要需求來選擇引擎,若沒有單一主導需求,則預設建議用Amazon OpenSearch Service,因為它能在search、scale與agentic整合之間取得平衡。

📊 效能與成本數據

Amazon OpenSearch Service結合lexical、vector、hybrid搜尋於單一系統,支援多種索引策略、向量量化與metadata過濾;GPU加速可將索引速度提升至最高10倍,成本降至四分之一;目前服務超過10萬個月活躍客戶,每月處理超過10兆次請求。新一代OpenSearch Serverless針對agentic AI優化,自動擴展速度比前一代快20倍,可在幾秒內完成佈建,閒置時能縮到零,相比為尖峰容量預先佈建最高可省下60%成本。

Amazon S3 Vectors則是首個原生支援儲存與查詢向量的雲端物件儲存,相比專用向量資料庫可將上傳、儲存、查詢向量的成本降低最多90%。自正式發布以來,客戶平均每日執行的查詢量較preview期成長超過5倍。近期兩項更新進一步優化體驗:單次查詢可回傳的結果數提升至10,000筆,較過去成長100倍,對套用reranking、聚合、去重的多階段檢索管線特別有用;而超過1000萬個向量的索引,查詢費用最高可降低80%。單一vector index最多可支援20億個向量。

💡 已有客戶案例驗證

Adobe採用OpenSearch Service來擴展其Acrobat AI Assistant,支撐這個整合進Adobe文件生態系、服務數億使用者的對話式生成式AI引擎。BMW Group則以S3 Vectors作為其混合搜尋方案的building block,該方案由Amazon Bedrock AgentCore驅動的智慧搜尋agent所建構。

🎯 選型前先問「資料現在在哪」

工程團隊在導入向量檢索前,可以先盤點資料目前落在哪個AWS服務,優先評估地端加裝向量搜尋而非另起爐灶;只有在延遲、成本或存取模式有明確主導需求時,才考慮專門引擎,例如低頻、大規模查詢的資料湖場景可評估S3 Vectors的低成本模式。值得留意的是,這套決策框架出自AWS官方,實務導入前仍值得與其他向量資料庫方案做交叉比較。

🔗 來源
- 標題：AWS vector solutions: Build agentic AI where your data lives
- 作者／機構：Marc Trimuschat, AWS Machine Learning Blog
- 連結：https://aws.amazon.com/blogs/machine-learning/aws-vector-solutions-build-agentic-ai-where-your-data-lives/

#AWS #VectorSearch #RAG #AgenticAI #OpenSearch #S3Vectors #AuroraPostgreSQL #MachineLearning #CloudComputing #SemanticSearch
