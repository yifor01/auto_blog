---
title: 'From Delta Sharing to OpenSharing: what changed, what''s next'
source: Databricks
url: https://www.databricks.com/blog/delta-sharing-opensharing-what-changed-whats-next
model: claude-code/sonnet
generated_at: '2026-11-05T23:09:04.879757'
score: 76
---

📌 Delta Sharing升級成OpenSharing,連agent skill和AI模型都能跨平臺共享

TL;DR:Databricks與Linux Foundation把Delta Sharing擴展為OpenSharing,開放共享agent skill、AI模型與地端資料。

當企業不只要共享一張表格,還想把agent會用到的skill和模型也一起交給合作夥伴時,一個只認得Table的開放協定就卡住了。2026年6月,Databricks與Linux Foundation做的不是幫協定加功能,而是重新定義它能裝下的東西。

🤔 背景:從「不複製資料」到「不只是資料」

Delta Sharing在2021年的Data + AI Summit上推出,要解決的問題很直接:企業想把即時資料分享給夥伴、客戶或其他團隊,卻不想匯出檔案、搭建脆弱的ETL,也不想逼每個接收端都換到同一個平臺上。Delta Sharing建立在Delta Lake與Parquet之上,被貢獻給Linux Foundation成為開放協定,provider授權一張table,接收端就能直接用Apache Spark、Power BI、Tableau、pandas等各種工具即時查詢。根據Databricks公布的資料,Delta Sharing已經是採用最廣的開放資料共享協定,Amadeus、Atlassian、LSEG、SAP、Stripe、The Trade Desk等組織用它做跨雲、跨平臺協作;到OpenSharing宣布時,Delta Sharing已累積超過28000個資料接收者,其中約三分之一的share是透過開放connector跨平臺流動,而不是侷限在Databricks對Databricks之間。

但共享的內容早就不只table了。透過Databricks對Databricks的共享,團隊多年前就已經在交換views、各種格式的volumes、notebooks和已註冊的ML模型。等到agent進入場景,需要移動的變成agent skill、agent本身,以及它們運行所需的語意context,企業也希望這類governed、zero-copy的存取能跨平臺,而不只留在Databricks內部;同時,開放協定本身仍只圍繞著table,企業還持續要求和Apache Iceberg等格式有更廣的互通性,以及讓留在地端或私有雲的資料也能納入同一套governed共享模型,不用先搬遷。這些缺口加在一起,逼著Databricks重新思考Delta Sharing的範疇,而不是單純加功能。

🧩 架構變化:新增的資產層級、Iceberg支援與地端串接

OpenSharing在開放規格裡引入Share → Schema → Asset的層級,把共享範圍從Table延伸到Volumes(任意格式的檔案目錄)、Agent Skills,以及AI模型;Agent和Page/Glossary這兩種類型目前還只是社群提案,尚在討論中。這代表provider可以把底層table和建立在其上的AI資產打包成一個資料產品,透過同一個協定整套共享出去。OpenSharing也新增對Apache Iceberg REST Catalog(IRC)相容client的支援,讓provider能把資料分享給任何Iceberg相容引擎,不限於Delta Sharing原生client。透過Databricks Storage Ecosystem,儲存廠商可以執行一個直接連到Unity Catalog的OpenSharing伺服器,讓留在地端或私有雲的資料在不先搬遷的前提下被納入治理並共享出去;MinIO的AIStor整合已經正式上線,其他儲存夥伴則在預覽階段或規劃在2026年稍晚推出。至於zero-copy的credential vending模式維持不變:provider不搬動資料,而是由sharing伺服器發出臨時、範圍受限的憑證,伺服器本身並不在資料傳輸路徑上。

💡 深入分析:治理權交給Linux Foundation,相容性沒有被打破

OpenSharing已經被貢獻給Linux Foundation AI & Data Foundation,目前處於sandbox階段,也就是新專案進入incubation前的起點;之後規格上的任何變更都要走公開提案與審查流程,而不是由單一廠商拍板,這和Delta Lake、Delta Sharing過去作為Linux Foundation專案時的治理模式一致。Databricks共同創辦人兼CTO Matei Zaharia把這次演進定調為:「Delta Sharing證明了產業會選擇開放而非被鎖定,OpenSharing把這個原則延伸到整個AI stack,同時把跨平臺生態擴展到Iceberg接收者與地端provider。」Linux Foundation CEO Jim Zemlin則表示目標是打造一套「讓組織能跨平臺、跨生態系統安全且互通地交換AI資產」的通用、廠商中立框架。值得強調的是,既有的Delta Sharing client與整合仍然相容OpenSharing,這是協定的演進而不是斷裂,delta-io/delta-sharing這個repository會和新成立的OpenSharing-IO/OpenSharing GitHub組織並存。

🎯 實務啟示

如果你現有的share、recipient、connector已經在正常運作,不需要做任何migration;把OpenSharing開啟給Unity Catalog metastore只是一個設定步驟,原本熟悉的Create Share、Create Recipient、Grant Access流程對新的資產類型一樣適用。如果你的下游剛好標準化在Iceberg工具鏈上,或者資料還留在地端、私有雲裡,這次擴展代表你不用先搬資料,就能把它們接進同一套governed共享模型。

🔗 來源
- 標題:From Delta Sharing to OpenSharing: what changed, what's next
- 作者／機構:Databricks
- 連結:https://www.databricks.com/blog/delta-sharing-opensharing-what-changed-whats-next

#Databricks #OpenSharing #DeltaSharing #LinuxFoundation #UnityCatalog #DataGovernance #ApacheIceberg #AIInfrastructure #DataSharing #OpenSource
