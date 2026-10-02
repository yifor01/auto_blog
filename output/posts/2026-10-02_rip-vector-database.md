---
title: RIP, vector database
source: Hacker News
url: https://turbopuffer.com/blog/rip-vector-database
model: claude-code/sonnet
generated_at: '2026-10-02T21:30:54.355386'
score: 94
---

📌 turbopuffer拆掉ANN主索引，重構v3儲存架構

TL;DR：turbopuffer要把向量索引從「主索引」降為「次要索引」，目標是讓text、regex、SQL查詢全面提速。

一個撐起過100B+向量、服務Cursor和Notion的向量資料庫，現在主動承認自己的核心設計已經「撐到頭了」，這本身就值得工程師停下來看看發生了什麼事。

🤔 **ANN主索引拖累了非向量查詢**

turbopuffer從v1開始就是一個serverless向量資料庫，用物件儲存（object storage）當真相來源，搭配分層NVMe SSD／記憶體快取拿到效能，這套取捨已經被Cursor、Notion等早期客戶驗證過。但這篇文章指出，這套架構在往text search、regex search、attribute filtering、aggregation等非向量查詢擴張時，開始遇到三個結構性問題：儲存放大（多向量表示時，文件內容必須在每個向量底下重複儲存一次）、寫入放大（SPFresh在重新平衡向量分群時，會連帶搬動整份文件內容及其所有倒排索引）、以及向量化受限（ANN索引的cluster大小落在100-200筆，但像DuckDB用2048筆、ClickHouse用到約6.5萬筆的批次大小才能發揮現代向量化查詢引擎的效能）。

🧩 **從C0L1位址到讓ANN變成「只是另一個索引」**

turbopuffer v1把每個向量分群（cluster）再分群成樹狀結構（源自SPANN，後改用支援增量索引的SPFresh），每個向量都有一個由ClusterId與LocalId組成的「ANN位址」（如C0L1），所有東西都用這個位址當主鍵儲存——這就是文中所說「ANN索引是主索引」的意思。v2在這個基礎上加入了attribute filtering（把屬性值映射到ANN位址的倒排索引）與BM25全文搜尋（儲存term count、document length等BM25評分所需的metadata）。v3要做的改變很直接：不再用ANN位址當主鍵，讓ANN變成眾多次要索引之一。

📊 **FTS重構的前例：索引縮小10倍，查詢快20倍**

文章提到一個已經發生過的案例作為佐證：FTS v1把posting list依照ANN cluster邊界切分，每個block平均只有約1.5筆posting；FTS v2把posting重新組織成固定約256筆的block後，索引縮小了10倍，查詢最高快了20倍。這個結果之所以可能，是因為posting list被獨立出來存放、只是指向文件，不必再跟著cluster的版面走。turbopuffer目前的規模是單索引撐住100B+向量、200ms p99延遲、1k+ QPS，整體引擎則承載1T+文件、10M+寫入/秒、25k+查詢/秒；v3目前的進度是「100% CI通過」，團隊的下一步是先追上、再超越現有效能水準。

💡 **分離「索引結構」與「文件儲存」才是通用解法**

FTS v2的經驗等於是turbopuffer團隊的一次小規模驗證：只要把某種查詢型態的資料結構，從「必須跟著ANN cluster走」的限制中解放出來，就能拿到可觀的效能提升。v3要做的，就是把這個原則從FTS一個查詢型態，推廣到aggregation、GROUP BY等所有查詢計畫上。

⚠️ **效能調校才剛開始，風險在於動到已經調到極致的ANN效能**

文章也坦承，目前的ANN索引設計已經被打磨到「真的很好用」的程度，任何大改動都有可能讓ANN搜尋效能出現退步，這也是為什麼他們強調接下來要先做到效能持平（parity），再往上追求超越。

🎯 **實務啟示**

如果你的系統同時需要向量搜尋、全文搜尋、屬性過濾甚至SQL聚合，這篇文章提供了一個很具體的反例：單一索引結構（即便是設計得很好的ANN索引）如果被當成所有查詢計畫的主索引，長期會在儲存放大、寫入放大與向量化批次大小上處處受限。評估向量資料庫時，值得多問一句：它的非向量查詢是建立在獨立的儲存結構上，還是被迫掛在向量索引的版面之下。

🔗 **來源**
- 標題：RIP, vector database
- 作者／機構：turbopuffer（razin，Hacker News轉載）
- 連結：https://turbopuffer.com/blog/rip-vector-database

#VectorDatabase #turbopuffer #SearchEngine #ANN #FullTextSearch #DatabaseArchitecture #ObjectStorage #SystemsDesign #SPFresh #QueryEngine
