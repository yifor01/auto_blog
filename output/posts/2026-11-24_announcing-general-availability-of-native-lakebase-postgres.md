---
title: Announcing General Availability of native Lakebase Postgres sink for Spark
  Structured Streaming
source: Databricks
url: https://www.databricks.com/blog/announcing-general-availability-native-lakebase-postgres-sink-spark-structured-streaming
model: claude-code/sonnet
generated_at: '2026-11-24T03:44:33.966776'
score: 66
---

📌 Lakebase原生Postgres Sink正式GA，免寫自訂foreach writer

TL;DR：Databricks推出原生Lakebase sink，串流pipeline百毫秒內把特徵寫進可服務的OLTP資料庫。

Fraud detection、即時個人化推薦、即時特徵計算這類低延遲場景，最終都需要把算好的結果寫進一個serving-ready的OLTP資料庫。問題是，從串流pipeline寫進Lakebase這件事，過去得自己刻一個foreach writer，還要處理batching、retry、upsert,複雜又難在高負載下維持效能。Databricks現在宣布，Apache Spark Structured Streaming的原生Lakebase sink已經正式GA。

🤔 **一個foreach writer要做的事太多了**

批次寫入要兼顧吞吐量、要有bounded queue做backpressure、要管理connection pool並刷新OAuth token、要用backoff重試暫時性失敗、要在batch內去重，還要正確實作upsert語意（例如保留最大timestamp，或只在新事件的排序值更新時才更新該欄位）。即使是經驗豐富的工程師，寫好並調校這些邏輯也要耗上數週，而且寫完之後它會變成一個要長期維護的元件:吞吐量退化要修、憑證刷新機制要跟、程式碼還要隨版本更新。

🧩 **原生sink同時支援micro-batch與Real-Time Mode**

這個新sink把上述所有事情都接管了，工程師只需要一行writeStream呼叫就能把資料寫進Lakebase。Databricks用一個影片串流平臺的推薦特徵pipeline示範：擷取使用者的watch與like事件，計算每個使用者最近觀看的6部影片與按讚的3部影片,再以user_id為key，把結果以一列一位使用者的形式upsert進Lakebase，供推薦模型在inference時查詢排序依據。

寫入路徑分兩種。如果Lakebase表已註冊在Unity Catalog中,用.toTable()搭配完整的catalog.schema.table路徑即可,連接器會以執行的使用者或service principal管理憑證，表不存在時還會自動建立。如果表沒有註冊在Unity Catalog，則改用format("postgresql")直接指向Lakebase endpoint；同樣的format("postgresql")路徑也支援透過Unity Catalog connection寫入外部PostgreSQL資料庫（例如Amazon RDS或自架資料庫，DBR 19以上、Public Preview階段）。Upsert行為可以透過宣告upsertkey來維持每個key一列，DBR 19起還支援合併策略（merge strategies），決定衝突時非key欄位要怎麼更新，不用自己手寫ON CONFLICT SQL。

📊 **20K events/sec、500萬使用者、每筆upsert只要0.015毫秒**

Databricks用一個40核心的classic compute叢集（DBR 18 LTS），對一個8-CU的Lakebase專案，以5分鐘的RTM checkpoint間隔，跑了持續1小時、每秒約2萬筆事件的測試，累積到500萬活躍使用者的狀態規模。測試期間完成了6350萬次upsert，根據pg_stat_statements統計，平均每筆SQL語句只花約0.015毫秒,Lakebase端還留有相當的效能餘裕。端到端延遲（從Kafka輸入的timestamp算到資料落地Lakebase）顯示,sink能在事件產生後100到200毫秒內完成寫入,下游應用或模型查詢時則是個位數毫秒等級的回應。

需要留意的是，Databricks特別註明這些數字只反映這套特定設定（輸入速率、保留的state量、RTM叢集大小、Lakebase規模），實際表現會隨環境而不同；連接器也提供batchinterval與batchsize兩個參數供效能調校。

⚠️ **限制**

原生Lakebase sink目前不支援Lakeflow Declarative Pipelines；RealTime與ProcessingTime trigger只能跑在classic compute上，serverless環境則需改用Trigger.AvailableNow。

🎯 **實務啟示**

如果你正在搭建即時特徵庫或fraud detection pipeline，這個sink等於省掉了自己刻、自己維護foreach writer的那幾週工作量,同時GA版本的效能數字也給出了一個可參考的基準（8-CU規模下毫秒級upsert）。要上線前記得確認使用的是DBR 18 LTS以上版本，並依自己的輸入速率與state規模分別調校Spark叢集與Lakebase的容量，而非直接套用文章中的測試數字。

🔗 **來源**
- 標題：Announcing General Availability of native Lakebase Postgres sink for Spark Structured Streaming
- 作者／機構：Databricks
- 連結：https://www.databricks.com/blog/announcing-general-availability-native-lakebase-postgres-sink-spark-structured-streaming

#ApacheSpark #StructuredStreaming #Lakebase #PostgreSQL #Databricks #RealTimeData #FeatureStore #DataEngineering #StreamProcessing #OLTP
