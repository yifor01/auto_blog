---
title: 'Sizing Lakebase Search: lessons from a real app and 4 million passages'
source: Databricks
url: https://www.databricks.com/blog/sizing-lakebase-search-lessons-real-app-and-4-million-passages
model: claude-code/sonnet
generated_at: '2026-10-14T20:56:31.587294'
score: 91
---

📌 400 萬筆資料實測：Lakebase Search 的資料庫規格該怎麼挑

TL;DR：Databricks 用內部搜尋工具 Slide Hub 與 400 萬筆 MIRACL 段落，實測 Lakebase Postgres 在不同規格下的效能極限。

多加運算資源不一定會變快——Databricks 的實測發現，Lakebase Postgres 的規模一旦衝過某個門檻，瓶頸就會從資料庫轉移到應用程式本身，而這個轉折點比許多人想像得更早出現。

🤔 **Slide Hub：一個真實的內部搜尋應用**

Slide Hub 是 Databricks 內部工具，讓 field engineer 從約 700 份內部簡報（活動演講、產品與架構簡報）中找到並重用單張投影片，同時透過 MCP（Model Context Protocol）server 把同一套搜尋能力提供給 AI agent 使用。投影片、投票、搜尋紀錄與變更歷史全部存在同一個 Lakebase Postgres 資料庫，這個真實使用案例也成為本次 benchmark 的基準。

🧩 **架構：搜尋就長在資料庫裡**

Lakebase Search 於九月正式 GA，本質是一組 Postgres extension，資料不需要搬到獨立的搜尋系統。`lakebase_vector` 負責儲存 embedding 並支援 `lakebase_ann` 索引做近似最近鄰（ANN）搜尋，索引用 IVF partitioning 分組向量，再用 RaBitQ quantization 把每個向量壓縮到約 1 bit／維度；`lakebase_text` 則支援 `lakebase_bm25` 索引，用 `<@>` 運算子做 BM25 關鍵字排序。

Slide Hub 採用 hybrid search：向量搜尋與 BM25 關鍵字搜尋各取 200 個候選，用 Reciprocal Rank Fusion（RRF，k=60）把兩份排名融合，再套用 0.70 的相似度門檻過濾掉太不相關的向量結果、對標題命中加權、notes 權重設為 0.5，最後套用權限過濾並接上投票資料——這整套排序邏輯只用一條 SQL 完成，與應用邏輯共用同一條連線、同一組權限與同一次 commit。

計算資源分兩層：Lakebase Postgres 以 Compute Unit（CU）計費，1 CU 約配置 2GB 記憶體與對應的 CPU／本地 SSD，可在 0.5～64 CU 之間自動擴縮（上限最多比下限多 16），固定規格最高到 112 CU，32 CU 以下可以 scale to zero。資料庫會用 Local File Cache（LFC）保留近期讀取的頁面，快取隨 CU 增長，最多使用 75% 的記憶體。應用層的 Databricks Apps 則是固定規格：MEDIUM 最多 2 vCPU／6GB，LARGE 最多 4 vCPU／12GB，每個 worker process 持有 8 條資料庫連線。

📊 **CU 規模與效能的關係**

| 規格 | 平均延遲 | File Cache | 備註 |
|---|---|---|---|
| 1 CU | 146 ms | 1.5 GB | 需從 storage 讀取 14.9M 頁 |
| 8 CU | 34 ms | 12 GB | throughput 較 1 CU 提升約 50% |
| 16 CU（搭配 MEDIUM app） | 僅再提升 4% | — | 資料庫連線多半閒置 |
| 16 CU + LARGE app（4 workers） | — | — | 至少達 662 req/s，此時瓶頸是負載產生器本身 |

結論很直接：8 CU 以下，資料庫是瓶頸，該加 CU；8 CU 之後，瓶頸轉移到應用層，該加 app worker。連線池同樣關鍵——在 50 個使用者的情境下，沒有連線池時只有 45 req/s、p95 延遲 2.4 秒，加上連線池後提升到 85 req/s、p95 降到 0.7 秒；而 embedding 快取在負載測試下沒有觀察到明顯差異。

候選數量（candidate limit）也值得注意：Slide Hub 原先出貨設定是每種方法各取 1,000 個候選，官方文件範例則用 40。實測把候選數降到 200 時，前 10 筆結果中有 90.5% 與 1,000 候選的結果一致，命中總數則是 1,000 候選情況下的 81%，考慮到使用者很少翻到第 200 筆以後，Slide Hub 最終改用 200 候選，冷啟動（compute 從 scale to zero 甦醒後的第一次查詢）延遲從原本更高的水準降到 2.9 秒，重複查詢只要 40 毫秒。冷啟動的延遲主要來自連線喚醒端點（約 1 秒）與頁面逐步從 storage 讀入直到快取熱機，第一次查詢還要額外付出約 75 毫秒的查詢規劃時間。

規模測試使用 MIRACL English（完整語料 32,893,221 筆段落）切出 1M、2M、4M 三個子集，用 1024 維的開源模型 `gte-large-en-v1.5` 做 embedding，自架在單張 A10G GPU 上跑出 379 passages／秒，整個語料耗時 2.95 GPU 小時，相較於用模型服務端點跑同樣工作要花 $48.87；兩種方式產出的向量幾乎一致（平均 cosine 相似度 1.0000，最低 0.9978）。`lakebase_ann` 索引隨語料增長：1M 時 5.8GB，2M 時 11.5GB，4M 時 23.0GB，而用 binary COPY 在 8 CU 下載入全部 400 萬筆只花 19 分鐘。由於 Lakebase Postgres 每 CU 大約只能提供 1.6GB 的 file cache，當索引大小超過快取容量時會發生什麼事，是素材本身留下、尚待後續驗證的開放問題。

⚠️ **規模持續成長後的行為仍待觀察**

素材明確指出「索引大於快取時會發生什�麼」這個問題尚未在文中給出具體答案，這裡不做過度延伸推測。

🎯 **實務啟示**

如果你要在自己的 Lakebase Postgres 上加搜尋功能，可以照這個順序排優先序：先精簡 candidate limit（不必無腦設大），再把 CU 調到資料庫不再是瓶頸，最後才是增加應用層 worker 數與資料庫連線池大小；同時別忘了連線池本身就能帶來接近兩倍的吞吐量提升。

🔗 **來源**
- 標題：Sizing Lakebase Search: lessons from a real app and 4 million passages
- 作者／機構：Databricks
- 連結：https://www.databricks.com/blog/sizing-lakebase-search-lessons-real-app-and-4-million-passages

#Databricks #Lakebase #PostgreSQL #VectorSearch #BM25 #HybridSearch #DatabasePerformance #RAG #MCP #Benchmarking
