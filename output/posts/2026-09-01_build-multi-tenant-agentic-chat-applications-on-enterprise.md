---
title: Build multi-tenant agentic chat applications on enterprise data with Amazon
  Bedrock Managed Knowledge Base
source: AWS ML
url: https://aws.amazon.com/blogs/machine-learning/build-multi-tenant-agentic-chat-applications-on-enterprise-data-with-amazon-bedrock-managed-knowledge-base/
model: claude-code/sonnet
generated_at: '2026-09-01T10:45:21.967056'
score: 98
---

📌 【AWS 實作】多租戶文件問答，如何不用自建隔離邏輯就上線

TL;DR：Amazon Bedrock Managed Knowledge Base 讓多租戶 agentic 文件問答免去自建檢索堆疊與租戶隔離邏輯的重活。

使用者上傳合約、報告或產品手冊，隨即或日後對著它提問——這類多租戶文件問答需求越來越常見，對話介面本身不難做，難的是背後那套多租戶 agentic 檢索系統：每個租戶的文件必須與其他租戶徹底隔離，而且這道邊界必須從「已驗證的身份」而非「客戶端傳來的值」去落實。

🤔 **Agentic 檢索讓隔離問題更棘手**

Agentic 檢索會把問題拆成多個子查詢並執行多次檢索，每一次跳轉（hop）都必須帶著租戶篩選條件，否則隔離就會被破壞。除此之外，團隊還得自建向量與全文搜尋引擎、能解析並嵌入多模態內容的擷取管線，以及同步索引——對一支想快速上線這項功能的團隊來說，這是相當可觀的基礎設施工作量。

🧩 **交給 Managed Knowledge Base 的部分，跟留給應用程式的部分**

Amazon Bedrock Managed Knowledge Base 管理擷取、儲存、embedding 與排序，不需要自行提供或監控容量；它內建的 agentic 檢索會用反覆規劃與多跳檢索來回答複雜問題，並在每一跳都尊重存取權限。透過自訂連接器直接擷取，應用程式可以把文件直接送進知識庫，幾秒內就能被檢索到。知識庫擁有的是檢索與生成的核心元件：決定要查什麼的規劃步驟、向量索引、排序器，以及產出最終回答的模型；應用程式只需要負責產品特有的部分——上傳體驗、聊天介面、身份驗證、逐使用者隔離與自訂商業邏輯。

因為使用者是在應用程式運行期間上傳文件，方案選擇透過自訂連接器資料來源（`IngestKnowledgeBaseDocuments` API）直接擷取，而非適合批次擷取、依排程同步的 S3 連接器——排程同步可能會覆寫或移除使用者剛加入的文件。直接擷取沒有同步機制，文件會一直留著直到你主動刪除；你也自己指定文件 ID，讓逐使用者的管理與更新變得直觀。知識庫還會保留每份原始檔案的副本，可透過 `GetDocumentContent` API 取回，因此應用程式不需要另外維護一套文件儲存系統，使用者也能直接打開回答背後的原始來源。

擷取路徑依檔案大小分流：6MB 以內的檔案（涵蓋多數文字文件、合約、報告）直接以位元組形式送進 API；文字檔最大到 50MB 的較大檔案，會先暫存到 Amazon S3，再以 S3 URI 方式參照擷取，路由規則在伺服器端執行，對使用者是透明的。由於文件 ID 是自訂的，用同一個 ID 重新擷取會就地更新而非產生重複項（沒有部分更新，一次編輯就是一次完整重新擷取）；範例實作用同一張 DynamoDB 表同時追蹤索引狀態與 `(user_id, filename) → document_id` 的對應關係。此外，單次 `IngestKnowledgeBaseDocuments` 呼叫最多可接受 10 份文件，方便 worker 把多個擷取工作打包成一次請求。

💡 **非同步索引生命週期：不是「送進去」就能查**

`IngestKnowledgeBaseDocuments` 是非同步 API，呼叫後立即回傳 `STARTING` 狀態，但文件要等 Bedrock 解析、嵌入並索引完才能被檢索到。文件會經過五個狀態，只有到 `INDEXED` 才算完全可查詢。文中特別提醒：文字內容在 `TEXT_INDEXED` 階段就已經可被檢索，涵蓋多數檢索需求；只有到 `INDEXED` 階段，PDF 等內容裡的多模態元素（圖片、表格）才會可查詢。如果把 `STARTING`（僅接受）就當成可搜尋，對還在索引中的文件查詢會得到空結果——範例實作是在 `TEXT_INDEXED` 這一刻，就把介面上的狀態標記為「就緒」，而不是等到完全 `INDEXED`。

在多租戶情境下，一位使用者的文件絕不能出現在另一位使用者的檢索結果裡。文章提出兩種做法：為每個租戶各建一個獨立知識庫，或用一個共享知識庫、每次查詢都透過 metadata 篩選條件或服務端評估的文件層級存取控制清單（ACL）來限定範圍。

🎯 **實務啟示**

對要做多租戶 SaaS 文件問答的團隊而言，這篇文章的價值在於把「哪些交給託管服務、哪些自己顧」畫得很清楚：擷取、索引、agentic 檢索交給 Managed Knowledge Base；文件 ID 對應、就緒狀態判斷（記得用 `TEXT_INDEXED` 而非等到 `INDEXED`）、以及租戶隔離策略的選擇（獨立知識庫 vs. 共享 + 篩選條件），才是真正需要自己設計的部分。

🔗 **來源**
- 標題：Build multi-tenant agentic chat applications on enterprise data with Amazon Bedrock Managed Knowledge Base
- 作者／機構：George Belsian（AWS）
- 連結：https://aws.amazon.com/blogs/machine-learning/build-multi-tenant-agentic-chat-applications-on-enterprise-data-with-amazon-bedrock-managed-knowledge-base/

#AWS #AmazonBedrock #MultiTenant #RAG #AgenticRetrieval #KnowledgeBase #SaaS #DataIsolation #EnterpriseAI #CloudArchitecture
