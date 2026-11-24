---
title: Sharing catalog metadata across data platforms, engines, and agents
source: Databricks
url: https://www.databricks.com/blog/sharing-catalog-metadata-across-data-platforms-engines-and-agents
model: claude-code/sonnet
generated_at: '2026-11-24T03:44:33.966679'
score: 67
---

📌 Iceberg Catalog長出標籤欄位，中繼資料終於能跨平臺走

TL;DR：Databricks等多家業者為Iceberg REST Catalog加入labels欄位，讓context不再被鎖在單一系統。

企業的lakehouse架構裡往往塞滿各種工具，但同一張表的「這是什麼資料、歸誰負責、能不能外流」這類context，過去只活在產生它的那個catalog裡。別的平臺要用，得重新手刻分類、搭自訂的同步pipeline，agent也因此常常拿不到完整資訊。Databricks聯合Google Cloud、Salesforce、ClickHouse、Atlan、Collibra、DataHub、Immuta、Trust3 AI、PhoenixAI與Datastrato，一起把這個問題丟回Apache Iceberg社群解決。

🤔 **中繼資料不該比資料本身更封閉**

Databricks的立場很直接：catalog的中繼資料應該和它描述的資料一樣開放、一樣可攜。只要context維持在單一來源系統裡，不同團隊、不同工具就得各自重建分類邏輯,這對正在把agent接進資料生態系的組織來說是一道明顯的摩擦力。

🧩 **在Iceberg REST LoadTable回應裡多一個labels欄位**

Databricks與Apache Iceberg社群合作，在Iceberg REST的LoadTable回應中新增一個選用的labels欄位，讓catalog能用標準方式對外公開table層級與column層級的context。Labels本質上是字串key-value pair，可以描述業務歸屬、使用目的、敏感程度等由catalog維護的資訊；這個標準只定義了「怎麼共享」的格式，並不規定詞彙表或解讀方式，所以每個平臺都能照自己的方式去使用這些標籤。

文章給出的例子是一張叫support_cases的表：資料管理者（data steward）替整張表標上domain=customer_support與Databricks系統標籤system.certification_status=certified，再替issue_summary這個欄位標上content_type=support_case_summary。公開這些標籤的catalog，就會把它們放進Iceberg REST的LoadTable回應裡。下游平臺可以直接讀取這些table層級與column層級的標籤來讓這張表變得更好用；PyIceberg已經在為下一個0.13版本加入讀取catalog labels的支援,讓Python應用程式（包括資料探索工具與agent）能直接檢視同一張support_cases表的標籤。

在Databricks這一端，Unity Catalog透過一項名為Tag Exchange的功能，把自己既有的table層級與column層級tag以catalog labels的形式對外公開。Databricks把這稱為邁向「開放治理」願景的一步：context一旦在某個系統裡維護好，就該能在每一個與資料互動的平臺、引擎、AI agent上被重複使用，而詮釋方式則留給各工具自行決定。

🧩 **現在能怎麼用**

Tag Exchange目前以Beta形式提供，公開Unity Catalog的table與column層級tag。要啟用的話，在Databricks Previews portal裡打開「Tag Exchange via Iceberg REST Catalog」這個選項即可。

⚠️ **標準只規定格式，不規定語意**

這份標準刻意保持輕量：它只定義labels怎麼被放進API回應裡，不去規定這些key該長什麼樣子、value又該怎麼被解讀。好處是每個平臺可以照自己的治理邏輯延伸使用，但也意味著跨系統要真正「看懂」同一個標籤，仍需要協調一套共用的命名慣例。

🎯 **實務啟示**

對正在打造跨平臺資料探索或agentic workflow的工程師來說，這代表未來可以少寫一套中繼資料同步pipeline:直接從Iceberg REST Catalog的LoadTable回應讀取labels即可。但因為標準不規定詞彙表，設計agent或治理政策時仍要自己定義一套可被各方理解的key命名規範,否則「開放格式」只解決了傳輸問題，沒解決語意對齊問題。

🔗 **來源**
- 標題：Sharing catalog metadata across data platforms, engines, and agents
- 作者／機構：Databricks
- 連結：https://www.databricks.com/blog/sharing-catalog-metadata-across-data-platforms-engines-and-agents

#ApacheIceberg #DataGovernance #UnityCatalog #Databricks #DataCatalog #Lakehouse #MetadataManagement #DataEngineering #AIAgents #OpenStandards
