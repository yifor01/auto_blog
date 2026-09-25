---
title: 'From Data to Dialogue: How S&P Global Energy Made Its Structured Data Estate
  Conversational with Databricks Genie Agents and MCP'
source: Databricks
url: https://www.databricks.com/blog/data-dialogue-how-sp-global-energy-made-its-structured-data-estate-conversational-databricks
model: claude-code/sonnet
generated_at: '2026-09-25T20:57:27.212113'
score: 74
---

📌 領域專家免寫程式，直接發布對話式資料代理

TL;DR：S&P Global Energy 用 Databricks Genie Agent 搭配 MCP，讓 SME 不寫程式就能發布可對話的結構化資料介面。

企業資料最大的痛點，往往不是模型不夠聰明，而是模型根本碰不到資料。S&P Global Energy 的能源業務橫跨化學品、原油、精煉油品、天然氣與電力、液化天然氣（LNG）等多個商品線，每條線底下又是一整個資料家族——光是 LNG 就包含設施規格、貨物（cargo）、停機（outage）、供需基本面、netback、歷史與預測價格、合約等子領域。過去要讓這些資料能被 AI 助理理解，每一個新的對話式資料體驗都得跑完整套工程流程：需求盤點、API 設計、text-to-SQL 工程化、測試、部署，耗時動輒數月。

🤔 誰最懂資料，誰卻離資料存取層最遠

問題核心在於組織分工：真正理解資料含義的是 SME（領域專家）與分析師，但實際打造資料存取層的是工程團隊。每一個洞見都得排進工程待辦清單才能變成可用介面，這道牆正是時間差的根源。

🧩 三層架構，每層交給最懂的人

S&P Global Energy 的解法分三層。第一層是 SME 策展：SME 挑選特定商業領域相關的資料表，依子類別分組，為每個資料組建立一個聚焦的 Genie Agent，而不是每個商品線一個龐大代理（例如 LNG 底下，cargo、outages、netbacks 各自是獨立 Genie Agent）；SME 會在其中補上資料表與欄位說明、範例查詢、高風險指標對應的可信資產，以及業務定義（例如「floating storage」在 LNG 情境下的精確定義），整個過程不需要寫程式。第二層是 MCP 伺服器：每個 Genie Agent 會自動以 Databricks 受管理的 MCP 伺服器形式對外暴露，端點格式為 `https://<workspace-hostname>/api/2.0/mcp/genie/{genie_space_id}`，不需要額外部署，基本只提供兩個工具，採「送出查詢、再輪詢結果」的非同步模式，權限則完全由 Unity Catalog 控管。第三層是 MCP 代理組合：真實商業問題常橫跨多個資料組（例如「Sabine Pass 的停機事件如何影響貨物運往亞洲的溢價」同時牽涉 Outages 與 Cargo 兩個 Genie Agent），團隊沒有打造一個萬用巨型代理，而是用 FastMCP 的 proxy 與 composition 能力，把同一商品線底下的多個 group-level Genie MCP 伺服器掛載成一個具命名空間工具的複合端點。

💡 SME 從「提需求的人」變成「發布的人」

這個架構最直接的效果是發布方式改變了：SME 建立並策展 Genie Agent 的當下，MCP 端點就同時存在，不再需要等待完整開發週期。SME 變成發布者，工程團隊專注於標準化代理連線，治理則統一由 Unity Catalog 承接，不必另外打造一層安全機制。

⚠️ 未提供的部分

文章並未公開具體的準確率、延遲或使用規模等量化數據，文中的 FastMCP 程式碼片段也標註為示意用途，需依實際版本與驗證設定調整，落地前仍需自行驗證可複現性。

🎯 給工程團隊的啟示

如果你的組織也面臨「懂資料的人不會寫代理、寫代理的人不懂資料」的結構性落差，這個案例的價值不在於 Genie 或 FastMCP 本身，而在於「策展是領域活動，不是工程活動」的分工原則：把語意層（表格說明、業務定義、範例查詢）的擁有權交還給 SME，工程只負責標準化連線與治理，能大幅縮短資料到對話的距離。

🔗 來源
- 標題：From Data to Dialogue: How S&P Global Energy Made Its Structured Data Estate Conversational with Databricks Genie Agents and MCP
- 作者／機構：Databricks
- 連結：https://www.databricks.com/blog/data-dialogue-how-sp-global-energy-made-its-structured-data-estate-conversational-databricks

#MCP #DatabricksGenie #DataEngineering #EnterpriseAI #UnityCatalog #TextToSQL #AIAgents #FastMCP #EnergyData #ConversationalAI
