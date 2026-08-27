---
title: 'Object Storage + WAL: Lakebase Postgres for the agentic era'
source: Databricks
url: https://www.databricks.com/blog/object-storage-wal-lakebase-postgres-agentic-era
model: claude-code/sonnet
generated_at: '2026-08-27T17:24:09.189037'
score: 102
---

📌 Databricks Lakebase Postgres：把物件儲存變成資料庫的真相來源

TL;DR：讓 Postgres 的 WAL 而非資料檔案成為「真相」，資料庫複製、還原都變成指標操作。

如果把資料庫想成「現在的狀態」，複製一份資料庫就得搬動全部資料；但如果把資料庫想成「一連串交易的日誌」，複製資料庫就只是複製一個指標。Databricks 的 Lakebase Postgres，賭的正是後面這個想法。

🤔 Agent 工作負載對資料庫提出了新要求

文章指出，agent 與傳統 OLTP 資料庫互動時，經常在儲存層卡住：新增部署、複製、還原、建立 replica，全都意味著搬動大量資料，既耗時又昂貴。物件儲存（如 Amazon S3）則恰恰相反：便宜、效能好、幾乎不用維運，天生適合作為 agent 記憶體的可擴充、低成本儲存層。這帶出了 Lakebase Postgres 的起點問題：能不能把物件儲存放進交易型資料庫的底層？

作者認為，答案不只取決於物件儲存有多快，更取決於「真相來源（source of truth）」放在哪裡。傳統的 OLTP 心智模型是資料為中心（data-centric）：資料組織成表格的列與欄，儲存層是「當下狀態」所在的地方，資料庫的工作就是存取它。但還有另一種模型：交易為中心（transaction-centric），資料庫是一份交易日誌，每筆紀錄是一個操作，儲存層是操作的時間軸，而非當下狀態的快照；當下狀態只是從時間軸中可以推導出來的其中一件事。過去多年資料為中心的模型獨大，因為維運團隊要的就是對「當下」的讀寫；但近年 agent 工作負載要求的幾乎都是對交易歷史的操作，也就是對時間軸的查詢。

🧩 把 WAL 本身當成資料庫

Postgres 其實早就內建這條時間軸：write-ahead log（WAL）。WAL 會在每一次修改寫進資料檔案之前，先把它記錄下來，原本的用途是容錯：如果伺服器在寫日誌與寫資料檔案之間當機，重播 WAL 就能補上缺口。以一張表加一筆 insert 為例，Postgres 會先把這筆變更寫入 WAL；文章用 pg_waldump 攤開日誌內容，顯示一次 insert 對應四筆記錄、屬於同一筆交易，每筆記錄都有一個單調遞增的 log sequence number（LSN），heap 與 btree 這幾行還會指出確切被改動的 8KB 頁面。

換句話說，WAL 記的不是「新增了一列資料」，而是「哪個 relation 的哪個頁面，在時間軸上哪個位置」被改動。把它當成復原機制看，它是當機後要重做的工作清單；但把它當成交易日誌看，它是一份完整、依序、位元組層級的頁面異動紀錄，且每一筆都有獨一無二的名字，也就是 LSN。這個名字讓「時間軸」天生就是可定址的：不需要在 Postgres 裡額外加東西，就能讓「資料庫在某個時間點的樣子」成為一個定義明確的概念，只需要一個能把日誌保留下來、並能回答日誌查詢的儲存層。

在傳統 Postgres 部署中，WAL 只是達成目的的手段：資料檔案才是「資料庫」，日誌用來保護它，一旦異動安全落地就會被清掉。Lakebase Postgres 把這個關係反過來：讓日誌本身成為資料庫，資料檔案則變成從日誌衍生出來、可被快取的表示法。這樣一來就能保留完整時間軸，複製或倒轉資料庫也不再需要搬動資料——資料庫的「複製」變成一個指標，而不是另一套檔案，部署、還原、建立 replica 因此便宜到可以像對待程式碼一樣對待它們。

具體做法是把系統拆成兩層。運算層執行標準 Postgres：剖析 SQL、規劃並執行查詢、維護 MVCC、管理鎖與索引，查詢引擎本身完全沒有改寫；差別在於運算節點的職責變成「執行工作」而非「保存資料」，它用 RAM 做 shared buffer、本地 NVMe 當頁面快取，可以隨時啟動、停止、擴縮甚至當機，都不會威脅到資料的持久性。儲存層則負責正確性、持久性與歷史紀錄，生命週期不受任何單一運算節點限制。

寫入路徑上，一次 commit 會經過幾個步驟，其中一步會把 WAL 送到儲存層，這會在 commit 路徑上多一次網路來回；但文章也指出，任何認真看待持久性的 Postgres 部署本來就會跑同步複寫（synchronous replication），本身就是一次網路來回，把 WAL 外部化只是用一次網路來回替換另一次，而非平白多加一次。

讀取路徑則圍繞著一個叫 GetPage@LSN 的核心操作：每個讀取請求會帶著頁面識別碼與 LSN，儲存層回傳該頁面在那個 LSN 當下的樣子，取回的頁面會被快取進 RAM 與 NVMe，之後讀取就會命中本地快取。主節點在穩定狀態下永遠要「最新版本」的每個頁面，行為就跟平常讀取溫快取的 Postgres 沒兩樣；但協定本身並不要求一定要拿最新版本，你可以要求四小時前那個 LSN 的頁面，就會拿到四小時前的樣子。這帶來一個實際效果：即時資料與歷史備份之間的界線消失了，因為 pageserver 從不就地修改檔案，檔案只會被建立、合併、刪除，不會被修改，這剛好完美對應物件儲存「不能就地更新」的特性，也讓保留歷史的成本變得低廉。

資料被組織成兩種 layer 檔案，其中 image layer 會在背景產生，用意有兩個：縮短讀取時要重播的鏈，以及讓舊的差異紀錄可以被回收。因此 GetPage@LSN 本質上變成一次搜尋：從指定的 key 與 LSN 出發，往下走過各層蒐集該頁面的 WAL 紀錄，直到碰到第一個 image 為止；為了讓這個搜尋保持簡短，delta layer 與 image layer 會經由背景 compaction 重新整理，超出保留窗口的層則會被垃圾回收。

⚠️ 真正難的地方：在數千萬個 layer 中做定位

文章坦承，上面描述的搜尋聽起來簡單，實際上不然，而且這一步決定了整個設計是否可行。一次讀取指定一個 key 與一個 LSN，儲存系統得在「該 key、該 LSN 或更早」的條件下找到最接近的 layer，這是一個幾何問題，而且在數千萬個 layer 規模下並不顯而易見該怎麼解：線性掃描太慢；常見的空間資料結構也不合用，R-tree 回答的是包含關係查詢，而非「這個點以下的第一個 layer」；segment tree 的規模則會隨座標空間而非 layer 數量成長。文章指出，可行的做法是先解決簡單版本的問題：固定一個 LSN，算出每個 key 由哪個 layer 回答，這個對應關係只在少數幾個點上改變，把這些變化點記錄進一棵二元搜尋樹，就能用單次查找回答該 LSN 下的任何讀取；但這只解決了單一 LSN 的情況，由於每次新增 layer 都會改變覆蓋範圍，且系統中有數百萬個 LSN，不可能為每個 LSN 各建一棵樹，需要讓這個資料結構「記得自己的歷史」（persistent 資料結構）。原文在此處收尾，未進一步展開這個持久化資料結構的完整解法。

🎯 實務啟示

對正在打造 agent 應用、需要頻繁複製、分支、回溯資料庫狀態的團隊來說，Lakebase Postgres 展示的思路值得留意：與其在資料層之上額外疊一層版本控制，不如直接把資料庫原生就有的 WAL 當成可定址的時間軸來用。如果你的 agent 工作負載本來就大量依賴「建立一份資料庫快照來測試」「回溯到某個時間點除錯」，這種把日誌當真相來源的架構，可能比傳統快照式備份更貼近實際需求。

🔗 來源
- 標題：Object Storage + WAL: Lakebase Postgres for the agentic era
- 作者／機構：Databricks
- 連結：https://www.databricks.com/blog/object-storage-wal-lakebase-postgres-agentic-era

#Postgres #Databricks #Lakebase #ObjectStorage #WAL #DatabaseArchitecture #AIAgents #OLTP #DataEngineering #DistributedSystems
