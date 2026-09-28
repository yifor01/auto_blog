---
title: 'Lakebase Search: State-of-the-art full text and vector search for Postgres'
source: Databricks
url: https://www.databricks.com/blog/lakebase-search-state-art-full-text-and-vector-search-postgres
model: claude-code/sonnet
generated_at: '2026-09-28T22:43:11.548818'
score: 96
---

📌 Postgres 也能扛住 10 億向量：Databricks Lakebase Search 上線

TL;DR：Databricks 推出 lakebase_vector 與 lakebase_text 兩個延伸套件，讓 Postgres 原生支援大規模向量與全文檢索。

當 AI Agent 一次觸發成千上萬筆並行檢索請求時，傳統 OLTP 資料庫的假設就開始站不住腳了。過去的解法通常是在主資料庫外接一個獨立的搜尋引擎，再用 ETL pipeline 把資料同步過去。Databricks 這次的答案是：讓 Postgres 自己扛下搜尋工作負載。

🤔 **pgvector 在大規模場景下的三個痛點**

Databricks 指出，pgvector 是 Lakebase Postgres 中安裝最多的延伸套件，但客戶在規模化使用時普遍遇到三個問題。第一，HNSW 索引必須整個放進記憶體才夠快，因為圖形搜尋（graph traversal）依賴隨機存取，索引一旦溢出到磁碟，效能會掉 10 到 50 倍；以 768 維的 float32 向量估算，一億筆資料大約需要 330GB 記憶體才能維持毫秒級查詢，而且沒有「working set」概念，不管你查全部還是查一小部分，都得為整個索引預先配置資源。第二，寫入同樣被拖慢，因為每一次插入都要在圖形的多個層級做隨機存取式的導航與修改，在標準雲端機器上建立一億筆資料的 pgvector 索引，官方引用的數字是接近 50 小時。第三，維運上更麻煩，HNSW 缺乏全域再平衡機制，要恢復搜尋品質就得整表 REINDEX，這會鎖表並擋住正式環境的寫入；而且單次查詢只跑在單一 Postgres backend process 上，HNSW 索引掃描本身無法平行化，想提高吞吐量只能靠加連線數或讀取複本。

🧩 **把儲存和運算拆開，冷熱都要快**

Lakebase Postgres 本身就是儲存與運算分離的架構：持久資料放在便宜的雲端物件儲存，RAM 與本地 NVMe 則作為熱資料的暫存快取。在這個基礎上，lakebase_vector 的設計必須同時滿足「快取命中時要快」與「冷資料時也不能慢」兩個條件：快取命中時，搜尋只在量化後（quantized）的小體積向量上運作；冷資料時，查詢只抓取需要的區塊，不必爬過整個索引。

具體做法上，lakebase_vector 因為儲存與運算解耦而完全無狀態，節點可以隨查詢按需快取熱資料，閒置時自動歸零，下次查詢再喚醒。索引建置也走平行化路線：先用一小部分隨機抽樣訓練出 centroid（這是唯一需要掃過整個資料集的步驟），之後每個向量各自獨立地被分配到最近的 centroid、量化、寫入對應的叢集區塊，這個流程可以隨核心數線性擴展。Databricks 甚至把索引建置整個移出主資料庫，透過開放格式資料搭配 LTAP 架構，交給 Spark 這類分散式引擎處理，把建置時間壓縮到分鐘級。查詢時，lakebase_vector 先用精簡的 1-bit 編碼廣泛篩選候選項，只對一小份候選清單做全精度重新排序（rerank）；因為索引區塊彼此獨立，單一查詢就能跨 CPU 核心平行化，過濾條件（filter predicate）也是直接在掃描叢集區塊時內聯處理，避免多抓不必要的候選資料。

至於 lakebase_text，則是把原生 BM25 帶進 Postgres：透過全域逆文件頻率（inverse document frequency）為詞彙評分，讓稀有、高意圖的詞彙獲得更高權重，同時壓低常見的填充詞。相較傳統的 tsvector 搭配 GIN 索引，lakebase_text 在走訪索引時會即時評估分數上界，直接跳過不可能進入 top-K 結果的 posting block。兩者結合後，一個查詢就能同時做語意向量搜尋、BM25 關鍵字相關性排序、標準 SQL 過濾，並直接 join 正式環境中的資料表。

📊 **實測數據：吞吐量兩倍、成本四分之一**

在 VectorDBBench 100M 基準測試中，lakebase_vector 的吞吐量是次佳系統的兩倍，成本是使用 pgvector 的雲端 Postgres 供應商的四分之一，而且這還不包含自動擴縮帶來的額外節省。在準確度上，實測顯示 97% recall（真正的最近鄰居有 97% 的機率被正確找到）時，P99 延遲為 71 毫秒。客戶案例方面，Conexiom 在超過一億筆資料上執行搭配 BM25 的混合搜尋，運算資源只用了先前 pgvector 架構的一半，而且整套系統完全無伺服器化。

⚠️ **不是要取代所有搜尋場景**

Databricks 也在文中澄清定位：Databricks AI Search 是另一個開箱即用的管理式搜尋引擎，適合追求高品質檢索又不想手動調校的場景；Lakebase Search 則是在你希望營運資料與搜尋資料都留在同一個資料庫時的選擇。兩者的搭配關係值得工程團隊按需求選擇，而非互斥的替代品。

🎯 **實務啟示**

如果你的系統已經用 Lakebase Postgres，且正被 pgvector 在大規模下的記憶體限制、索引建置時間或維運鎖表問題困擾，直接啟用 lakebase_vector 與 lakebase_text 兩個延伸套件即可評估，不需要另外搭建獨立的向量搜尋引擎與 ETL 管線。

🔗 **來源**
- 標題：Lakebase Search: State-of-the-art full text and vector search for Postgres
- 作者／機構：Databricks
- 連結：https://www.databricks.com/blog/lakebase-search-state-art-full-text-and-vector-search-postgres

#Postgres #VectorSearch #BM25 #Databricks #Lakebase #pgvector #HybridSearch #RAG #DatabaseEngineering #AIInfrastructure
