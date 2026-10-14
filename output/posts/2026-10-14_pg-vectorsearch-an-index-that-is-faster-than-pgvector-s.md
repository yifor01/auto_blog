---
title: 'Pg_vectorsearch: An index that is faster than pgvector''s IVFFlat and HNSW'
source: Hacker News
url: https://github.com/timescale/pg_vectorsearch
model: claude-code/sonnet
generated_at: '2026-10-14T20:53:05.951903'
score: 104
---

📌 PostgreSQL 新索引 PRISM:號稱同時打敗 IVFFlat 與 HNSW

TL;DR:Timescale 開源 pg_vectorsearch,其 PRISM 索引宣稱在億級向量規模下比 HNSW 更快、更省記憶體。

向量資料庫的標準答案長期是 pgvector 的 HNSW 或 IVFFlat,但如果有一種索引同時比兩者都快,還能用更少的記憶體撐住一億筆向量,會是怎麼做到的?這就是 pg_vectorsearch 這個新 PostgreSQL extension 想回答的問題。

🤔 **解決什麼問題**

pg_vectorsearch 是一個用於高效能 approximate nearest neighbor (ANN) 搜尋的 PostgreSQL extension,目前狀態為 alpha,官方明確標示僅供測試、尚不建議用於生產環境,且 prereleases 之間可能無法直接升級,需要砍掉重建 extension 與索引。核心賣點是它的 PRISM 索引(Partitioned Routing Index for Similarity Matching):概念上類似 pgvector 的 IVFFlat,但用了更先進的量化、路由與分區技術,以 C 語言實作。官方宣稱在一億筆向量的資料集上,PRISM 不只比 IVFFlat 與 HNSW 快,在同等 recall 下,相較圖結構的 HNSW,PRISM 使用的記憶體僅為四分之一。

🧩 **核心架構:分層路由 + RaBitQ 量化 + SIMD**

PRISM 用一個 hierarchical centroid tree 將向量切分到不同 cluster,並依賴 PostgreSQL 的 buffer cache 讓這棵樹保持在記憶體中。向量本身經過 RaBitQ 量化後存入 posting lists,頁面佈局針對 SIMD 距離計算最佳化(支援 AVX2、AVX512、NEON)。RaBitQ 編碼帶有理論誤差界(error bounds),讓搜尋可以直接排除「不可能是最近鄰」的向量,大幅減少需要對全精度向量做 rerank 的數量。

一次查詢的流程大致是:
1. 走訪 centroid tree 找出最接近的 cluster(走 buffer cache)
2. 掃描 posting lists 取得候選向量(buffer cache + 非同步 I/O)
3. RaBitQ 兩階段過濾:估計距離 → 套用誤差界 → 篩選進入 rerank
4. 從 heap 取出全精度向量做最終 rerank
5. 回傳 k 個最近鄰

索引支援動態更新(insert、update、delete),透過 `prism_rebalance` 程序對過大的 posting list 做分裂。插入時向量會直接附加到對應的 posting list,list 本身不會自動分裂,所以除了 `REINDEX` 外,維護時需要依賴這個 rebalance 程序。

🧪 **怎麼用:原生型別,或直接插在既有 pgvector 表上**

pg_vectorsearch 提供兩條使用路徑。第一種是原生型別:新專案或還沒用 pgvector 的話,可以直接用 `vec32`(float32)或 `vec16`(float16)欄位型別,不需要安裝其他 extension。第二種是相容既有 pgvector 表:如果資料表已經有 `vector` 或 `halfvec` 欄位,可以把 pg_vectorsearch 裝在 pgvector 旁邊,直接在原欄位上建 PRISM 索引,資料表與查詢語法完全不用改。因為 `vec32`/`vec16` 與 pgvector 的 `vector`/`halfvec` 二進位相容,兩套 extension 可以並存在同一個 schema 裡。

兩條路徑都使用相同的運算子(`<->`、`<#>`、`<=>`)與調參選項,對應 L2、inner product、cosine 三種距離。大多數部署情境下,官方建議唯一需要調的參數是 `prism.nprobe`,預設 0 代表自動達到約 0.95 recall,調高換 recall、調低換速度。

⚠️ **適用場景與限制**

建置需求是 PostgreSQL 18+、GNU C11 編譯器(GCC 11+ 或 Clang 14+)與 Meson build system,CBLAS 則是加速 RaBitQ 編碼的可選依賴。因為官方明確定調為 alpha,目前更適合用在評估與測試環境,而非直接上生產。想從 HNSW 遷移的團隊,可以先在既有表上並存建 PRISM 索引,用 `EXPLAIN` 驗證查詢計畫是否改走 PRISM,確認無虞後再移除舊的 HNSW 索引——這也是 README 示範的遷移方式。

🎯 **實務啟示**

如果你的向量檢索規模正在往億級邁進,又受夠了 HNSW 建索引的記憶體開銷,pg_vectorsearch 提供了一條「不用改 schema、不用改查詢」的漸進式評估路徑:先裝在既有 pgvector 表旁邊跑基準測試,再決定是否全面切換。但鑑於 alpha 狀態與升級路徑的限制,建議先在非關鍵資料集上驗證穩定性。

🔗 **來源**
- 標題:Pg_vectorsearch: An index that is faster than pgvector's IVFFlat and HNSW
- 作者/機構:jascha_eng(Hacker News);專案由 Timescale 維護(GitHub: timescale/pg_vectorsearch)
- 連結:https://github.com/timescale/pg_vectorsearch

#PostgreSQL #VectorSearch #ANN #Timescale #pgvector #RaBitQ #SIMD #DatabaseEngineering #OpenSource #RAG
