---
title: Push-based CDC into Unity Catalog with Zerobus Ingest and Debezium
source: Databricks
url: https://www.databricks.com/blog/push-based-cdc-unity-catalog-zerobus-ingest-and-debezium
model: claude-code/sonnet
generated_at: '2026-11-05T23:05:25.902502'
score: 81
---

📌 NVIDIA與Databricks聯手：免Kafka的CDC管線進Unity Catalog

TL;DR：Debezium加上Zerobus Ingest，CDC資料不用經過Kafka就能直接寫入Delta table。

當資料庫待在企業內網、不接受任何外部服務的inbound連線時，要把它的異動資料送進lakehouse，往往要先掛一整套Kafka——但Databricks與NVIDIA最新開源的方案，把這一整段省掉了。

🤔 **問題：資料庫在內網，只能往外推資料**

許多team的PostgreSQL資料庫位於私有公司網路、客戶控制環境或受限subnet，網路政策會封鎖外部服務的inbound連線。擁有資料庫的team通常也想自己掌握capture這個環節，自己跑讀取write-ahead log的程式，自己決定哪些連線可以離開自己的網路；另一邊，異動資料則要落到受Unity Catalog治理的Delta table，讓pipeline與分析師可以直接在上面建東西。

🧩 **兩種架構：傳統message bus vs. Zerobus**

在許多企業環境裡，從內網往外連線遠比允許外部inbound連線容易被核准。傳統作法是用Debezium把capture agent部署在內網，把異動事件往外推到一個message bus（例如Kafka）。但跑Kafka需要容量規劃，預估尖峰負載需要多少broker做實體擴充，估算需要多少partition做邏輯擴充讓consumer跟得上生產速度，這通常需要一個有Kafka部署與維運經驗的專職team。資料進了Kafka之後，還要再做一次複製工作，把事件搬進lakehouse，可能透過Spark、Kafka Connector或其他工具部署ingestion job，結果就是從Debezium到lakehouse要經過兩個hop的架構。

Zerobus Ingest則讓最終目的地只有lakehouse這一個選項時，可以跳過中間的message bus這一跳，不只讓整個端到端架構變得更精簡，也省掉部署與維運Kafka基礎設施的需求。用Zerobus作為Debezium的sink，尖峰時段也能持續運作，不需要額外調校。

💡 **誰做了什麼：Debezium讀log，Zerobus負責寫入**

Debezium是開源的log-based CDC平臺，從2015年開始發展，不靠polling資料表，而是讀取資料庫的transaction log（例如PostgreSQL的write-ahead log、MySQL的binlog、MongoDB的change stream），把每個異動事件轉成結構化事件，支援PostgreSQL、MySQL、SQL Server、Oracle、MongoDB等廣泛的connector生態。由於是tail log而非polling，Debezium對主資料庫的負擔很小，延遲低，也能保留commit順序。

Debezium有兩種運作型態：一種是跑在Kafka Connect裡的plugin，另一種是「standalone server」，可以跑在一般的運算資源上。Debezium Server（standalone runtime）扮演來源端的agent，直接把異動事件送到Databricks的Zerobus Ingest，不需要Kafka cluster當傳輸層。

Zerobus Ingest是一個serverless、push-based的ingestion服務，直接把資料寫進受Unity Catalog治理的Delta table，不需要跑任何message broker，設計上就是要處理高吞吐、高並行的workload。省掉message broker這一步，也就省掉了擴充與維運ingestion pipeline把資料搬進lakehouse的工作。

這個整合Debezium與Zerobus的sink，由NVIDIA與Databricks工程師合作開發並貢獻到開源的Debezium專案，已經隨Debezium Server 3.7版本一起發行。Databricks打造了typed Zerobus Ingest sink，NVIDIA則貢獻了envelope mode。

🧩 **Typed mode與Envelope mode**

Zerobus Ingest是append-only的，異動事件落地後，下一步是透過merge建出Type-1維度表，取得每個primary key最新版本。Debezium裡的Zerobus sink提供兩種table契約：

- Typed mode（預設）：把每個異動事件對應到一張沿用來源資料表原生欄位的table。
- Envelope mode（NVIDIA貢獻）：把完整的Debezium異動事件，連同交付安全機制一起，落到一張固定九欄位的table裡，紀錄可用JSON（存在VARIANT欄位）或Protobuf編碼。

Envelope mode保留了下游處理需要的證據：`source_position`帶有來源的partition與offset，包含PostgreSQL的LSN；`idempotency_key`是依照目的地、partition、key、操作與來源position算出的SHA-256身分識別，重送的事件會得到相同的key。這個key的作用是識別事件，本身不負責排序或在table上去重；如果後面一組交付失敗，前面已經確認交付的那組還是可能再被送一次，所以交付保證是at-least-once，重複的部分要靠下游用`idempotency_key`處理。Envelope mode還會依目的地與操作類型過濾，並在record過大時直接拒絕，讓它的offset不會被提交。

事件落到Delta之後，常見的做法是用medallion式的分層流程，把原始異動feed變成分析師與應用程式可以直接使用的table。

⚠️ **這是一套取捨，不是萬能解**

Zerobus Ingest本身是append-only，要變成「目前狀態」的current-state table，還是需要額外的merge步驟（例如用AUTO CDC依照來源LSN排序）。選擇哪種CDC架構，最終還是要看團隊自己的網路限制、維運偏好與既有基礎設施。

🎯 **對工程師的意義**

如果你的team已經在用Debezium做CDC，但苦於要額外維護一整套Kafka只是為了把資料搬進lakehouse，這個NVIDIA與Databricks共同貢獻的Zerobus sink提供了一條直接的路徑：Debezium Server讀log、Zerobus Ingest寫Delta table，中間不用再插一層訊息匯流排。Envelope mode的idempotency key與source position設計，也代表下游依然能用熟悉的方式處理at-least-once交付與去重，不用自己從零刻一套。

🔗 **來源**
- 標題：Push-based CDC into Unity Catalog with Zerobus Ingest and Debezium
- 作者／機構：Databricks
- 連結：https://www.databricks.com/blog/push-based-cdc-unity-catalog-zerobus-ingest-and-debezium

#CDC #Debezium #Databricks #NVIDIA #UnityCatalog #DeltaLake #DataEngineering #Lakehouse #PostgreSQL #StreamingData
