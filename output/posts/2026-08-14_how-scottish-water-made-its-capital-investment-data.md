---
title: How Scottish Water Made Its Capital Investment Data Conversational With Databricks
  Genie
source: Databricks
url: https://www.databricks.com/blog/how-scottish-water-made-its-capital-investment-data-conversational-databricks-genie
model: claude-code/sonnet
generated_at: '2026-08-14T07:34:30.483227'
score: 72
---

📌 蘇格蘭水務用聊天取代報表，靠的是 Genie 加 MCP

TL;DR：蘇格蘭水務用 Databricks Genie 打通 Teams，讓專案數據問答秒回，省去查報表的時間。

一個資料量充足的部門，居然還是天天在等數字，這是蘇格蘭水務（Scottish Water）資本投資（Capital Investment）團隊過去長期面對的怪象。

🤔 **問題不是沒資料，是找不到資料**

蘇格蘭水務的資本投資部門需要快速掌握專案狀態、財務績效、交付里程碑與風險，這些資訊原本就存在，但散落在龐大的報表體系中，要嘛得自行翻找，要嘛得仰賴資料專員從底層資料表中萃取。結果是分析師花時間重做已經存在的分析，交付團隊等著數字被抽出來，而重要的專案資訊也不一定能即時傳到真正需要做決策的人手上。

🧩 **SPARK：把 Genie 接進 Teams 的內部品牌**

SPARK 是蘇格蘭水務為其專案組合資料自然語言介面取的內部品牌名稱，底層建構在 Databricks Genie 之上。使用者不必再去搜尋正確的報表，而是直接提問，答案則根據治理後的資料回覆。SPARK 把這個體驗直接帶進團隊原本就在使用的 Microsoft Teams：使用者透過 Copilot 在 Teams 中提交問題，由 Copilot supervisor agent 負責調度，再透過 Model Context Protocol（MCP）連接到 Databricks Genie Space；Genie 將問題轉譯成查詢，對 Unity Catalog 中的治理資料執行，並把結果回傳給使用者。透過 SPARK，團隊可以直接詢問實際的業務問題，答案立即來自經過治理的 metric views，不必再花時間定位報表。

💡 **信任感是靠治理堆出來的**

對話式分析要能真正被使用，前提是使用者信任答案。蘇格蘭水務從一開始就把治理內建進設計：Genie 體驗建立在 Unity Catalog 的治理資料與共享語意定義之上，確保答案一致、可解釋，並與既有的業務邏輯對齊。為了讓 Genie space 在實務上可靠，蘇格蘭水務依照自己的業務規則、術語與真實使用者提問來設定，而非套用通用配置；上線後也建立了監控機制，追蹤採用率、答案品質與效能表現，並將整套方案設計成可以在不同環境間安全、一致地推廣，而非一次性專案。

🎯 **實務啟示**

這個案例展示的是一種可複製的架構模式：把治理後的資料層（Unity Catalog）、對話式查詢引擎（Genie）與既有協作工具（Teams／Copilot）透過 MCP 串接起來，讓使用者在原有工作流程中就能取得可信任的答案。對正在規劃企業內部對話式分析的工程團隊來說，「先把語意層與治理做扎實，再談自然語言介面」是這個案例中值得借鏡的順序。

🔗 **來源**
- 標題：How Scottish Water Made Its Capital Investment Data Conversational With Databricks Genie
- 作者／機構：Databricks
- 連結：https://www.databricks.com/blog/how-scottish-water-made-its-capital-investment-data-conversational-databricks-genie

#Databricks #Genie #MCP #UnityCatalog #ConversationalAnalytics #DataGovernance #MicrosoftTeams #EnterpriseAI #DataEngineering #NaturalLanguageQuery
