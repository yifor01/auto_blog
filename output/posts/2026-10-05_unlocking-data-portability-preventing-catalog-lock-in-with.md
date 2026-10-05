---
title: 'Unlocking Data Portability: Preventing Catalog Lock-in with REGISTER and UNREGISTER
  APIs'
source: Databricks
url: https://www.databricks.com/blog/unlocking-data-portability-preventing-catalog-lock-register-and-unregister-apis
model: claude-code/sonnet
generated_at: '2026-10-05T23:29:06.155571'
score: 72
---

📌 Iceberg Catalog 也能好聚好散：UNREGISTER API 終結資料表搬遷的 Split-Brain 風險

TL;DR：Databricks 替 Apache Iceberg REST catalog 新增 UNREGISTER 端點，讓資料表能在不同 catalog 間乾淨交接，不必重寫或複製檔案。

搬一張 Iceberg 資料表到新 catalog，你會碰到一件尷尬的事：執行 DROP TABLE 會把底層資料和 metadata 一起刪光，但如果只把表「註冊」到新 catalog，舊 catalog 卻渾然不知自己已經被取代。這個看似基本的操作，在開放表格格式生態裡其實一直缺一塊拼圖。

🤔 開放表格格式只解決了一半的開放性

隨著 lakehouse 架構普及，資料逐漸從封閉的資料倉儲搬到開放儲存與表格格式，讓 Spark、Trino 等多種引擎可以直接存取同一份資料，不必重複複製。但 Databricks 在部落格中指出，開放格式只是開放性方程式的一半；真正的開放還需要在資料治理與管理方式上具備可移植性，讓組織能隨架構演進自由更換 catalog，而不被單一 catalog 綁死。

🧩 REGISTER 解決一半，UNREGISTER 補上另一半

理解這個問題前，得先知道 catalog 在查詢流程中的角色。當引擎要查詢一張表時，會先向 catalog 請求載入該表以取得最新狀態；catalog 回傳的 metadata 會指向物件儲存中的實際資料位置，引擎再依此讀取 Parquet 檔案。由於 schema、歷史紀錄、統計資訊等重要 metadata 連同資料本身都放在儲存層，與運算層完全解耦，catalog 扮演的其實是「協調提交」的中央權威角色，確保不會有兩個寫入者同時悄悄覆寫彼此的資料。

REGISTER 端點本身並不複雜：只要把載入該表時取得的 metadata 位置交給新 catalog，新 catalog 就能接手這張表，這也是 Iceberg REST 規格原本就定義好的操作。

問題在於，Iceberg 的各個 catalog 之間彼此獨立、互不通訊。如果只做 REGISTER，舊 catalog 完全不知道自己已被取代，仍自認是這張表的唯一擁有者。於是兩個 catalog 都以為自己掌握提交協調權，第一次寫入就會讓表分岔，導致查詢結果不一致，甚至悄悄遺失資料，這就是所謂的 split-brain 情境。

Databricks 因此把 UNREGISTER 貢獻進 Apache Iceberg REST catalog 規格，讓舊 catalog 能在不動到任何底層資料檔案的前提下，移除自己對該表的管理紀錄，同時回傳這張表最新的 metadata 位置，也就是下一個 catalog 接手提交協調所需的確切指標。實際呼叫方式是對表資源送出一個空的 POST 請求：

POST <uc-iceberg-rest-base>/v1/{prefix}/namespaces/{namespace}/tables/{table}/unregister

回應內容就是下一個 catalog 需要接手的 metadata 指標。整個搬遷流程因此變成三步驟：先向舊 catalog 執行 UNREGISTER、取得位置指標，再向新 catalog 執行 REGISTER，確保任何時刻都只有一個 catalog 在管理這張表。

⚠️ 搬遷仍有操作眉角

Databricks 特別提醒，正式環境的遷移不只是呼叫兩個 API，還牽涉到安全地停止寫入作業、重新導向任務等操作性步驟，這部分留待後續文章說明。目前 REGISTER 與 UNREGISTER 在 Unity Catalog 上以 private preview 形式提供，須透過帳戶團隊申請試用。

🎯 實務啟示

對同時使用多引擎、多 catalog 的資料團隊來說，這組 API 的意義不只是技術便利，而是把「換 catalog」從不可逆的風險操作，變成有明確協定可循的標準流程。若你的架構正考慮在 Spark、Trino 等引擎間切換治理層，值得關注這個方向，但實際遷移前仍建議按照官方後續指引規劃寫入端的停機與切換步驟。

🔗 來源
- 標題：Unlocking Data Portability: Preventing Catalog Lock-in with REGISTER and UNREGISTER APIs
- 作者／機構：Databricks
- 連結：https://www.databricks.com/blog/unlocking-data-portability-preventing-catalog-lock-register-and-unregister-apis

#ApacheIceberg #DataEngineering #Lakehouse #UnityCatalog #Databricks #DataPortability #OpenTableFormat #DataGovernance #RESTCatalog #BigData
