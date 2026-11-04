---
title: How Indegene is modernizing and scaling enterprise data quality in life sciences
source: AWS ML
url: https://aws.amazon.com/blogs/machine-learning/how-indegene-is-modernizing-and-scaling-enterprise-data-quality-in-life-sciences/
model: claude-code/sonnet
generated_at: '2026-11-04T23:00:21.186644'
score: 65
---

📌 當技術規則與業務規則分家,資料品質就變成一場永久拉鋸戰

TL;DR：生命科學企業服務商 Indegene 用 LLM agent 把業務規則與技術規則收斂到同一個治理流程,在 AWS 上打造 Data Quality Agent。

資料工程師確認 HCP ID（醫療專業人員 ID）不是 null、格式正確、唯一且對應到有效參照記錄——這是技術規則。業務團隊要確認某個產品在特定地區的市佔率加總是否等於 100%,或某位 HCP 的處方行為是否符合其專科與資格條件——這是業務規則。前者活在程式碼裡,後者活在詞彙表、SOP 與領域專家的經驗裡,兩者要保持一致並被統一治理,本來就很難,而這正是 Indegene 想解決的問題。

🤔 **靜態驗證抓得到格式錯誤,抓不到「業務上合理」**

Indegene 是生命科學產業的策略運營夥伴,服務全球前 20 大生物製藥公司,橫跨商業、醫學、市場准入等業務職能。文章指出,檢查 null 值、資料型別、唯一性或參照完整性這類傳統驗證techniques仍然必要,但它們無法捕捉業務情境——驗證產品層級結構、客戶分群、地域對齊或商業規則,需要靜態驗證邏輯難以表達的領域知識。更麻煩的是,每個新資料集都要重新跑資料剖析、規則定義、SQL 開發與驗證,規則散落在 SQL script、pipeline 程式碼、試算表、資料目錄與各種工具設定裡,schema 或業務定義一變動,維護成本就直線上升。

🧩 **把 Data Quality Agent 嵌進統一資料平臺,而非做成獨立工具**

Indegene 的解法是把資料品質能力嵌入自家的 NEXT Unified Data Platform（NEXT UDP）,這是專為生命科學打造的 AI 驅動資料平臺,把分散的商業、醫學、臨床與企業資料整合進單一治理環境。NEXT UDP 提供多個獨立 AI agent,包括 Data Ingestion agent、Data Quality agent、Orchestration agent、Data Catalog agent 與 SQL Bot Generator agent,可單獨使用於資料管線中,也可進一步客製化支援 agent 對 agent 溝通。

Data Quality Agent 建構在 Amazon Bedrock、Strands Agents 與 Amazon Bedrock AgentCore 之上。Amazon Bedrock 提供多種基礎模型選擇,並建立在安全、隱私與負責任 AI 控制的基礎上——這點對生命科學產業特別重要,因為資料常涉及敏感的醫療專業人員與患者資訊。Strands Agents 簡化 agent 的建構與更新,其評估工具協助 Indegene 測試規則準確性,這在高度監管的生命科學環境中是關鍵需求。agent 本身運行在 Amazon Bedrock AgentCore 上,直接繼承既有的 AWS 安全與稽核控制,讓團隊能專注在資料品質邏輯本身,而不是 agent 基礎設施。

📊 **用兩個互補知識庫,把業務情境灌進規則生成**

為了解決「資料在業務情境下是否合理」這個難題,Data Quality Agent 依賴兩個互補的知識庫。第一個是內部企業知識庫,整合內部業務詞彙表、資料字典、SOP、法規指引、已核准的資料品質規則、已驗證的腳本、剖析結果、歷史異常紀錄與領域專家（SME）回饋,這些內容經過向量化後,透過 Retrieval Augmented Generation（RAG）檢索,用來生成紮根於企業標準與既有成功案例的資料品質規則。第二個是外部參考知識庫,用經過核准的標準化資料品質框架、網路搜尋與受控的網頁爬取方式建立並定期更新。這套 agent 最終產出的是人機協同治理下、可直接執行的 SQL 與 Python 驗證程式碼,而不只是一份規則文件。

💡 **技術規則與業務規則的分裂,本質上是治理問題**

這篇文章點出的核心張力值得留意:並不是技術驗證不夠好,而是技術規則與業務規則長期分散在不同載體（程式碼 vs. 詞彙表／SOP／SME 經驗）裡,導致兩者難以對齊與統一治理。Indegene 的做法本質上是用 RAG 把原本只存在人腦與文件裡的業務知識結構化,讓 LLM 能在生成規則時同時參照技術規範與業務語境,而不是讓資料品質停留在「定期治理活動」,變成持續性、可規模化的能力。

🎯 **實務啟示**

如果你的團隊也面臨「資料工程師寫的規則」和「業務部門認可的規則」兩套語言對不上的問題,這個案例提供的思路是:不要把資料品質當成獨立工具硬接進既有平臺,而是把業務詞彙表、SOP、歷史異常等「活知識」做成 RAG 知識庫,讓 LLM 在生成可執行驗證程式碼的同時,自動對齊業務情境,同時搭配人機協同審核,而不是讓模型直接上線跑規則。

🔗 **來源**
- 標題：How Indegene is modernizing and scaling enterprise data quality in life sciences
- 作者／機構：Bhagyashree Chandak（與 Shravan K S, Indegene Limited 共同撰寫）
- 連結：https://aws.amazon.com/blogs/machine-learning/how-indegene-is-modernizing-and-scaling-enterprise-data-quality-in-life-sciences/

#DataQuality #LifeSciences #AmazonBedrock #AgenticAI #RAG #StrandsAgents #AgentCore #DataGovernance #EnterpriseAI #LLMAgent
