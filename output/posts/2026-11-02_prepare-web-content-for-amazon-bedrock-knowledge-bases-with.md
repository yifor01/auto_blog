---
title: Prepare web content for Amazon Bedrock Knowledge Bases with Crawl4AI
source: AWS ML
url: https://aws.amazon.com/blogs/machine-learning/prepare-web-content-for-amazon-bedrock-knowledge-bases-with-crawl4ai/
model: claude-code/sonnet
generated_at: '2026-11-03T00:11:43.293420'
score: 78
---

📌 用Crawl4AI補強Amazon Bedrock知識庫的網頁擷取

TL;DR：當內建Web Crawler連接器不夠用時，用開源Crawl4AI先清洗內容再送進Bedrock Knowledge Bases。

RAG（Retrieval Augmented Generation）應用的答案品質,說到底就是「墊進去的資料有多乾淨」——而這正是多數團隊在導入Amazon Bedrock Knowledge Bases時最容易忽略的一步。

🤔 **內建爬蟲夠用,但不是每個網站都適用**

Amazon Bedrock Knowledge Bases是Bedrock的全託管RAG能力,接上資料來源後,擷取、儲存、索引與檢索都由AWS管理,不用自己架設或擴展向量資料庫,預設也使用服務託管的嵌入(embedding)與重排序(reranking)模型。對於網頁內容,官方建議的起點是Amazon Bedrock Web Crawler連接器:給定種子URL或網站地圖,它會在你設定的範圍與速率限制內爬取,遵守robots.txt,且第一次完整爬取後,之後每次同步只會擷取新增、更新與刪除的內容,也能等待JavaScript載入的內容。但有些資料來源需要更多控制,例如只索引頁面的主要內容區塊、移除導覽列等版面雜訊,或是替每份文件附加自訂的metadata屬性——這類需求就是Crawl4AI這套開源Python爬蟲介入的地方。

🧩 **Crawl4AI只負責前段整理,後段仍交給Bedrock**

這套工作流程的分工很清楚:Crawl4AI的角色在它把來源文件與metadata sidecar準備好、寫入Amazon S3之後就結束了,從擷取(ingestion)之後的解析、分塊(chunking)、嵌入、索引與檢索,全部交還給Amazon Bedrock Knowledge Bases透過其S3資料來源連接器處理。文章也特別澄清,這是針對已知網頁資源的批次擷取(batch ingestion),不是像Amazon Nova的Web Grounding那種推論時的即時網頁存取。

整個流程由排程觸發一個AWS Fargate任務:啟動時先從AWS Systems Manager Parameter Store讀取非機密的管線設定,AWS CDK(Cloud Development Kit)在部署時把實作打包成容器映像檔,排程觸發後依序執行爬取(crawl)、上傳(upload)、擷取(ingest)三個步驟,邏輯都寫在scripts/container_entrypoint.py裡:

- **爬取步驟**:執行有邊界的爬取,為每個成功準備好的頁面寫出一份Markdown文件與對應的metadata sidecar。選擇輸出Markdown是因為它能保留標題、清單與表格結構,不必把整份原始HTML都帶進擷取流程。
- **上傳步驟**:把每份Markdown文件與其sidecar一起送到設定好的S3 bucket。命名規則很嚴格——例如page.md的sidecar必須命名為page.md.metadata.json;每個sidecar大小上限10KB,一旦超過上限,整次執行會在寫入任何檔案前就直接報錯中止。管線只會上傳本次爬取產生的路徑,不會把過期的本地檔案一併送出。
- **擷取步驟**:呼叫StartIngestionJob啟動擷取任務,讓知識庫把S3裡的新文件交給資料來源的擷取管線處理,同樣的API對managed與customer-managed兩種知識庫都適用。

目前流程只處理公開頁面,不支援需要登入的站點;若來源需要身分驗證,文章建議先評估Amazon Bedrock Web Crawler本身提供的basic、表單式與SAML驗證選項,若要在Crawl4AI管線裡擴充驗證,還需要額外處理session、把憑證存進AWS Secrets Manager,並做安全審查。

📊 **分塊策略一旦選定就不能改**

Managed knowledge base會用其託管解析器自動選擇解析方式,但分塊策略(chunking strategy)是在建立資料來源時就要決定,之後無法變更,要換策略只能重新建立一個新的資料來源。Customer-managed knowledge base則多出語意分塊(semantic)與層級分塊(hierarchical)等額外選項。文章建議,應該拿具代表性的頁面與評估問題,實際比較不同分塊策略的檢索結果,再決定正式環境要用哪一種。

⚠️ **部署前要注意的幾個雷**

部署用AWS CDK完成,需要先確保Docker正在執行,並把AWS_DEFAULT_REGION設成知識庫所在的區域——因為cdk deploy會用環境或profile裡的區域,不是bootstrap指令裡指定的區域。文章也提醒,範例指令裡的ACCOUNT_ID、REGION與四個必填的context參數都只是語法上合法的範例值,若沒替換就直接部署,會部署出一個指向你並不擁有的bucket的堆疊。首次爬取的maxDepth與maxPages預設限制在一層連結深度、25個頁面以內。

🎯 **實務啟示**

如果現有的Bedrock Web Crawler已經能滿足需求,就沒必要引入額外的Crawl4AI管線;但一旦遇到需要自訂metadata屬性、去除版面雜訊或只取主要內容區塊的場景,把Crawl4AI當成S3資料來源的前處理層,是在不自建爬蟲服務的前提下取得更多控制權的務實做法。完整實作範例可在aws-samples的對應repository中取得。

🔗 **來源**
- 標題：Prepare web content for Amazon Bedrock Knowledge Bases with Crawl4AI
- 作者／機構：Daxeshkumar Patel（AWS Machine Learning Blog）
- 連結：https://aws.amazon.com/blogs/machine-learning/prepare-web-content-for-amazon-bedrock-knowledge-bases-with-crawl4ai/

#AmazonBedrock #RAG #KnowledgeBases #Crawl4AI #AWS #LLM #DataIngestion #OpenSource #VectorSearch #CloudArchitecture
