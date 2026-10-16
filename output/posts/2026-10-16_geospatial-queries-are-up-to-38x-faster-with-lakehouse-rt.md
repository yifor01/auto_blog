---
title: Geospatial queries are up to 38X faster with Lakehouse//RT
source: Databricks
url: https://www.databricks.com/blog/geospatial-queries-are-38x-faster-lakehousert
model: claude-code/sonnet
generated_at: '2026-10-16T20:21:09.888816'
score: 52
---

📌 空間查詢加速38倍背後的架構

TL;DR：Databricks讓Spatial SQL跑在新推出的Lakehouse//RT上，高併發下最高快38倍。

當一家公司必須為地理空間應用另外維護一套PostGIS架構，只為了滿足低延遲需求時，資料卻因此多了一份副本、多了一條同步管線、多了一層治理負擔。

🤔 **為什麼空間工作負載需要新架構**

Databricks指出，保險、農業、能源、電信、零售、物流等產業的客戶已採用其今年推出的Spatial SQL（GA版），包括GEOMETRY資料型別、100多個空間函式、高效能spatial join、AI/BI maps與Delta Sharing。但對於同時有spatial OLAP與即時地理位置應用需求的組織，許多仍依賴傳統資料倉儲，並為每個應用場景另外搭建以PostGIS為核心的專用架構,這會導致更多資料副本、更多同步管線與更多治理成本。

🧩 **四大支柱架構**

Databricks現在提出地理空間工作負載的四個支柱：Lakehouse負責長時間執行的spatial OLAP；Lakebase負責spatial OLTP、應用程式與代理；Databricks Apps提供專屬體驗；而新加入的**Lakehouse//RT**則負責即時分析。GEOMETRY與GEOGRAPHY資料型別屬於開放lakehouse的一部分，在Apache Spark中可用，並支援Delta與Iceberg v3所使用的同一套底層parquet檔案格式。

📊 **用SpatialBench跑出來的數字**

Databricks以SpatialBench為基準，拿Lakehouse//RT與傳統雲端資料倉儲對比：

| 情境 | 效能提升 |
|---|---|
| 一系列空間查詢，整體平均 | 3X |
| 測試查詢中的最佳表現 | 最高20X |
| 50個並行使用者的高負載情境 | 最高38X |

此外，Lakehouse//RT整體被設計為能在governed lakehouse資料上直接提供毫秒級查詢效能，Databricks表示其預覽客戶觀察到延遲低至10毫秒、併發量最高可達每秒12,000次查詢。

💡 **最佳實務：直接用原生GEOMETRY型別**

Databricks在文中特別提醒，在跑SpatialBench的查詢8時，建議移除將well-known binary轉換為GEOMETRY的`ST_GeomFromWKB`呼叫，改用原生GEOMETRY型別，因為這樣才能讓查詢最佳化與file-skipping發揮作用，拿到最好的效能。

⚠️ **目前仍是Beta，且為廠商自行benchmark**

Spatial SQL在Lakehouse//RT上目前為Beta階段，上述倍數提升數字來自Databricks自行發布的SpatialBench測試結果，並未提及第三方獨立驗證。

🎯 **實務啟示**

對已經在用Databricks Spatial SQL的團隊來說，官方強調不需要改程式碼,只要建立一個Lakehouse//RT warehouse，把現有查詢指向它即可取得加速，這代表遷移成本主要是基礎設施層級的切換，而不是重寫查詢邏輯，值得評估是否能藉此收斂掉原本另外維護的PostGIS專用堆疊。

🔗 **來源**
- 標題：Geospatial queries are up to 38X faster with Lakehouse//RT
- 作者／機構：Databricks
- 連結：https://www.databricks.com/blog/geospatial-queries-are-38x-faster-lakehousert

#Databricks #SpatialSQL #Geospatial #Lakehouse #DataEngineering #RealTimeAnalytics #BigData #DeltaLake #CloudDataWarehouse #DataPlatform
