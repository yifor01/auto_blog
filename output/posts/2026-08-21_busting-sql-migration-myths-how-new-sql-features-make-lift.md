---
title: 'Busting SQL Migration Myths: How New SQL Features Make Lift-and-Shift to Lakehouse
  Easier'
source: Databricks
url: https://www.databricks.com/blog/busting-sql-migration-myths-how-new-sql-features-make-lift-and-shift-lakehouse-easier
model: claude-code/sonnet
generated_at: '2026-08-21T06:38:59.496762'
score: 64
---

📌 新 SQL Scripting 語法讓老預存程序無痛搬進 Lakehouse

TL;DR：Databricks SQL Scripting 支援 cursor、例外處理與原子交易，讓舊有預存程序可直接翻譯而非重寫。

倉儲裡總有那麼一批預存程序，每晚默默跑著，寫它們的人早已離職，第 47 行還留著一句「請勿更動這段程式碼」。這正是資料湖倉遷移專案裡最卡關的部分，而 Databricks 這篇文章要處理的就是這塊硬骨頭。

🤔 **搬資料容易，搬程序邏輯難**

文章指出，把資料搬到 lakehouse 已經是相對成熟的課題，真正的摩擦點在於資料倉儲的程序化核心：巢狀 cursor、動態建立的暫存表、跨多張表打包在單一交易裡的更新邏輯，以及企業內部仍高度仰賴 SQL 技能這個現實。過去每次談遷移，這些預存程序都是第一個被攔下來的理由：「這段不能大改，我們團隊只熟 SQL。」

🧩 **示範案例：以「翻譯」取代「重寫」**

Databricks 以一個常見的複合型預存程序為例：這支程序處理每日訂單，先把未處理訂單暫存進暫存表，比對客戶主檔進行驗證，逐筆記錄驗證失敗的訂單，再更新區域營收彙總並將訂單標記為已處理，全程包在一個交易裡，失敗就整批回滾。文章強調，過去要遷移這類程序，等於得整段改寫成 Python 與 Spark，耗費數週工時、引入新 bug，還會讓原本熟悉 SQL 的團隊失去對自家商業邏輯的維護能力；而這次示範走的是「翻譯」而非「重寫」的路線。

具體對應包括：原本包在 `BEGIN...EXCEPTION...END` 裡的例外處理，改用 `DECLARE EXIT HANDLER FOR SQLEXCEPTION`；暫存表不需要 `EXECUTE IMMEDIATE` 或 `ON COMMIT PRESERVE ROWS`，直接用 session 範圍的 `CREATE TEMP TABLE` 對應（但目前尚不支援 `CREATE OR REPLACE TEMP TABLE`，需要可重跑時得先手動 drop）；經典的 cursor 驗證迴圈，Databricks SQL Scripting 自 Runtime 18.1 起原生支援 `OPEN`、`FETCH`、`CLOSE`，`%NOTFOUND` 對應為 `CONTINUE HANDLER FOR NOT FOUND`，迴圈標籤與 `LEAVE` 取代 `EXIT WHEN`，`SELECT ... INTO` 則改寫成 `SET var = (SELECT ...)`。文章也提到，若原始程式碼庫是 Teradata BTEQ script，其中的 `.GOTO` 與 `.LABEL` 可對應到帶標籤迴圈搭配 `LEAVE`、`ITERATE` 改寫。整套 SQL Scripting 支援完整的程序化工具集：`IF/ELSE`、`WHILE`、`FOR`、`LOOP`、`REPEAT`、`LEAVE`、`ITERATE`、`SIGNAL/RESIGNAL`。

交易語意的部分，原本仰賴隱含交易搭配明確 `COMMIT`，在 Databricks 上改用 `BEGIN ATOMIC...END`，成功時自動 commit、失敗時自動 rollback，`MERGE` 陳述式可直接搬移，明確的 `COMMIT` 則由 `BEGIN ATOMIC` 接手。文章特別指出一項差異：Databricks 提供 row-level 衝突偵測，並以 Oracle 與 Snowflake 都採用 table-level locking、迫使批次工作序列化執行作為對照，意味著併發批次只要沒有觸及相同的資料列，就不會互相衝突。

📊 **註冊進 Unity Catalog 後多出的東西**

文章認為，遷移後最大的差異不在程式碼本身，而在部署之後：程序會被註冊進 Unity Catalog，因而獲得存取控制、欄位層級的資料血緣（lineage）與跨工作區的可發現性，相較於原本「只有三個人知道密碼」的舊系統，是治理面向的實質提升。

⚠️ **宣稱的效率提升與限制**

文章宣稱，即使是有大量 PL/SQL package 相依性的複雜預存程序，這種機械式翻譯流程也能將遷移時程縮短 50% 到 75%，因為它保留了原始商業邏輯，讓 SQL 團隊得以延續維護工作。不過目前已知至少有一項限制：`CREATE OR REPLACE TEMP TABLE` 尚未支援。

🎯 **實務啟示**

對正在評估資料倉儲遷移的工程團隊來說，這篇文章給出的訊息是：與其一開始就把整批預存程序改寫成 Python/Spark，不如先挑一支最小、最少人願意碰的預存程序，用文章提到的 Agentic Code Convertor 試跑一次翻譯流程，實際比對控制流程與交易語意是否對得上，再決定是否擴大到整批遷移。

🔗 **來源**
- 標題：Busting SQL Migration Myths: How New SQL Features Make Lift-and-Shift to Lakehouse Easier
- 作者／機構：Databricks
- 連結：https://www.databricks.com/blog/busting-sql-migration-myths-how-new-sql-features-make-lift-and-shift-lakehouse-easier

#Databricks #Lakehouse #SQLScripting #DataMigration #UnityCatalog #StoredProcedures #DataEngineering #DataWarehouse #ETL #CloudMigration
