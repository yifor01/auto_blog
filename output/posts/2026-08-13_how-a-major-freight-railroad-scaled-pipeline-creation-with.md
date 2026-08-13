---
title: How a major freight railroad scaled pipeline creation with Genie Code
source: Databricks
url: https://www.databricks.com/blog/how-major-freight-railroad-scaled-pipeline-creation-genie-code
model: claude-code/sonnet
generated_at: '2026-08-13T07:38:21.729755'
score: 68
---

📌 一家貨運鐵路公司如何用 Genie Code 把管線開發變成「工廠」

TL;DR：北美一家大型貨運鐵路公司用 Databricks Genie Code 搭配自訂 Agent Skill,把新資料表的管線開發自動化超過九成,交付時間從數天壓縮到數分鐘。

一條資料管線,原本要花好幾天才能寫完;現在,只要一段兩行的 YAML 提示就能生出可上線的程式碼。這不是效率提升,而是把「開發管線」這件事本身重新設計成了一條生產線。

🤔 **不是遷移一張表的問題,是遷移數百張表的問題**

這家北美最大的貨運鐵路網路之一,鐵路里程約 2 萬英里,每年支撐超過 2500 億加幣的貨物運輸。跟許多大型企業一樣,它的分析資料庫是數十年間陸續疊加起來的:大型主機系統、老舊資料倉儲、企業級 ETL 平臺、專用一體機。在往現代湖倉架構遷移的過程中,真正的挑戰不是搬資料本身,而是要在保留大量遺留業務邏輯的前提下,把管線開發方式簡化並標準化。在自動化之前,建立一張表的管線是多天的工作:要檢視來源 schema、在 Source-to-Target Mapping 試算表裡定義業務邏輯、寫歷史與串流擷取邏輯、寫增量合併管線、實作下游轉換,還要為 schema 演進、欄位改名、型別轉換、軟刪除等情境寫測試。一張表可以這樣做,數百張表就不可行了。

🧩 **Genie Code + 自訂 Agent Skill + Unity Catalog 的組合**

團隊採用的方案由兩個能力組成:用 Genie Code 搭配自訂 Agent Skill 產生可上線的擷取程式碼,以及一個基於 Databricks Apps 的應用程式,負責把來源欄位對應到目標湖倉資料表並產生轉換邏輯。Genie Code 扮演自主 AI 夥伴的角色,自訂 Agent Skill 則把公司自己的擷取模式與合併邏輯編碼進去;Unity Catalog 提供跨 raw、historical、prep 層的 schema 內省能力,Databricks Apps 則支撐來源到目標的欄位對應體驗。產出的管線用 PySpark、Spark SQL 與 Delta Lake 撰寫,並透過 Lakeflow Jobs 執行。稽核慣例、去重邏輯、變更序號合併防護、軟刪除協調與測試模式,全部直接內建在產生流程裡,不再仰賴每位開發者自行套用規範。團隊的核心原則是:在需要推理與探索的地方用 AI,在需要一致性與可重現性的地方用嚴格模式。

自訂 Agent Skill 以一個資料夾的形式上傳到 workspace/.assistant/skills/lakehouse-ingestion/,內含一個 SKILL.md 進入點,加上七個對應不同產出物類型的樣式檔案,涵蓋目錄探索、慣例、原始擷取、歷史載入、增量合併與測試產生。SKILL.md 的 frontmatter 就是 Genie Code 判斷何時載入這個 skill 的依據。

📊 **兩行 YAML,產出六份可上線的產出物**

開發者在 Genie Code 對話中以一段精簡 YAML 提示啟動程式碼產生,最簡單的原始擷取只需要兩行,完整管線也只要六行,內容包含來源與目標表名、主鍵、去重邏輯與更新頻率等核心輸入。接著 Genie Code 依序執行:解析並驗證提示,透過 Unity Catalog metadata 探索歷史層與可信層 schema,自動比對欄位,辨識型別轉換與改名需求,解析轉換模式,依公司標準模式產生所需產出物,再逐一驗證是否符合企業層級的必要約束,包括主鍵覆蓋率、稽核欄位擺放位置、變更序號防護的合併邏輯、支援 REFRESH 的去重,以及測試套件覆蓋率。依模式不同,這套流程支援單一資料表、單次多表,或是由 Unity Catalog volume 中的 CSV／Excel 檔案驅動的批次執行。實務上,這套流程能產生六種可上線產出物:DDL、歷史載入、原始串流擷取、首次增量合併、後續增量合併,以及自動化測試套件。

💡 **AI 負責產生,人類負責把關業務邏輯**

團隊並沒有把這件事當成完全放手的產生問題。在程式碼產生之前,資料設計師會先用一個 Databricks App 檢視遺留來源系統的欄位該如何對應到目標湖倉資料表,這個叫做 Source-to-Target Mapping 的步驟,用來捕捉不該被隨意猜測或盲目自動化的業務邏輯。這個以 Streamlit 建置的 Databricks Apps 應用會掃描來源系統資料表、預先產生欄位對應,再由資料設計師在瀏覽器裡檢視與調整轉換邏輯。所有產生的產出物都留在 Databricks 工作區內,套用與平臺其他部分相同的治理模型,存取控制、metadata 政策與修訂紀錄都是原生的。

📊 **成果:90% 以上自動化,交付時間從天到分鐘**

團隊表示,新資料表的擷取管線自動化程度超過 90%,管線交付時間從數天壓縮到數分鐘。

🎯 **實務啟示**

這個案例對正在推動大規模資料現代化的團隊有一個明確啟示:把 AI 用在「推理與發現」的環節(如 schema 比對、轉換邏輯建議),把嚴格規則用在「一致性與可重現性」的環節(如稽核欄位、合併防護、測試覆蓋),兩者分工而非讓 AI 全權代勞,同時保留人工把關業務邏輯轉換的關鍵步驟,可能是企業導入生成式 AI 建置資料管線時比較務實的路線。

🔗 **來源**
- 標題:How a major freight railroad scaled pipeline creation with Genie Code
- 作者／機構:Databricks
- 連結:https://www.databricks.com/blog/how-major-freight-railroad-scaled-pipeline-creation-genie-code

#Databricks #GenieCode #DataEngineering #UnityCatalog #DeltaLake #AgenticAI #DataPipeline #LakehouseArchitecture #PySpark #AIAutomation
