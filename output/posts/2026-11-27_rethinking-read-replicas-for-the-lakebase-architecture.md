---
title: Rethinking read replicas for the lakebase architecture
source: Databricks
url: https://www.databricks.com/blog/rethinking-read-replicas-lakebase-architecture
model: claude-code/sonnet
generated_at: '2026-11-27T01:14:48.686415'
score: 68
---

📌 Lakebase如何讓Postgres Read Replica「秒開秒關」

TL;DR：運算與儲存分離後，Lakebase的read replica幾秒內就能建好、不複製資料、閒置時自動歸零。

傳統Postgres的read replica號稱能彈性擴充讀取流量，但用過的人都知道：建一個要等幾分鐘到幾小時，流量退了它還留在那裡燒錢。問題究竟出在哪裡？

🤔 Replica其實是整臺機器的物理複製品

在RDS這類傳統托管Postgres架構下，Postgres以單一執行個體運行，資料掛在該執行個體的儲存卷上；要擴充讀取能力只有兩條路：換更大的執行個體，或建read replica分流一部分讀取。但在RDS上建replica，本質上就是蓋一臺新機器：資料庫越大，snapshot與volume就越大；流量越大，replica要回放的WAL就越多，小資料庫可能要花幾分鐘，大資料庫可能要花上幾小時。而且「已建好」不代表「已就緒」——RDS的replica volume上線後仍會持續從S3背景載入資料區塊，AWS官方也提示在載入完成前效能可能達不到完整水準。建立snapshot的過程還會短暫暫停primary的I/O（除非跑Multi-AZ），primary上任何長時間執行的交易也會拖慢整個流程。結果是許多團隊乾脆放棄replica，直接把primary撐大來扛流量峰值，或者24小時常駐一個replica以防萬一。

🧩 把運算與持久狀態拆開，replica不再複製任何東西

Lakebase Postgres把執行與持久狀態拆開：運算本身不擁有任何持久資料，因此可以讓多個運算同時掛在同一份儲存上，這正是Lakebase裡replica運作的核心機制。一個read replica就是一個獨立的、唯讀的運算節點，讀取的是primary所使用的那一份儲存；建立過程不依賴資料庫大小，所以在小資料庫和大資料庫上建replica都只需要幾秒鐘。它也不會給primary增加任何複製負擔：primary照常把WAL串流給safekeepers，replica則直接從safekeepers讀取，完全不經過primary。傳統架構下N個replica意味著N+1份資料副本，每一份都要獨立佈建、填入資料並個別計費；而在Lakebase Postgres裡，N個replica仍然只有一份資料，所有運算節點（primary及其所有replica）讀的都是儲存層裡同一份資料。replica會在shared buffer與本機NVMe上維護一份本地快取，但快取不是副本——它一開始是空的，只有replica實際用到某些資料頁時才會從pageserver載入，且不包含任何持久狀態。

📊 計費跟著實際用量走，不再跟著資料庫大小走

計費模式也因此改變：傳統replica是一個執行個體，按小時計費，不管它服務一次查詢還是一百萬次查詢，團隊得按峰值去配置並24小時付錢；Lakebase replica則只按實際使用的運算量計費。儲存方面，RDS上每個replica都自帶一份完整大小的儲存卷，三個replica掛在1TB資料庫上就要為4TB儲存付錢；在Lakebase Postgres裡，同樣的設置仍然只為1TB付錢，replica只增加運算成本，不增加儲存成本。

💡 當建replica只要幾秒，過去不划算的用法開始合理

當建一個replica只要幾秒、不佔儲存、閒置時又能自動歸零，過去因為成本與等待時間而放棄的用法開始變得合理——可以為每一種工作負載單獨建一個replica，用完就刪除或讓它自動歸零，而不是讓所有流量都擠在同一個共用replica上。

🎯 實務啟示

文章列出幾個可以直接套用的場景：把feed、商品頁、搜尋等重讀流量導去獨立replica，讓primary專心處理寫入；每次發布新版本或遇到流量高峰時，現場建一個replica，流量退了就讓它歸零；把BI工具、dashboard、報表掛到專屬replica上，避免大範圍掃描跟應用程式搶CPU與快取；當Agent、合作夥伴、稽核方或第三方工具需要存取即時資料又不該有寫入權限時，直接給一個唯讀replica比設定唯讀角色更省事；夜間CSV匯出、搜尋索引重建、群發電子報等背景工作，也該丟到replica上執行，避免拖慢正式環境。

🔗 來源
- 標題：Rethinking read replicas for the lakebase architecture
- 作者／機構：Databricks
- 連結：https://www.databricks.com/blog/rethinking-read-replicas-lakebase-architecture

#Postgres #Lakebase #Databricks #ReadReplica #DatabaseArchitecture #CloudInfrastructure #OLTP #ScalableDatabases #DevOps #DataEngineering
