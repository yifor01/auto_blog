---
title: The Web Search Your Agent Inherited Isn't Good Enough
source: Databricks
url: https://www.databricks.com/blog/web-search-your-agent-inherited-isnt-good-enough
model: claude-code/sonnet
generated_at: '2026-09-17T20:39:56.746879'
score: 76
---

📌 你的 Agent 用的網路搜尋，其實是繼承來的次級品

TL;DR：不同 Agent harness 內建的網路搜尋結果不一致，Databricks 提出 Omnigent 加合作夥伴搜尋來統一治理。

一個工程師要建一個 Agent，持續監控幾十萬個潛在客戶與既有客戶帳號,找出資金到位、換高層、產品發布、招募增加這類代表「這個帳號現在有機會談」的訊號。帳號資料本身已經在 Databricks 的 Delta table 裡，由 Unity Catalog 治理,並與公司自己的用量與 pipeline 資料串接好了。問題是，真正推動這些帳號變化的訊號在公司外部,在網路上。

🤔 **同一個邏輯，被重寫了三次**

第一版不是一套系統,而是同一套 enrichment 邏輯，在三個不同工具裡各自重寫了一次。第一次用 Claude Code 實作，因為決定哪些帳號要重新檢視、串接搜尋、寫摘要這些 Agent 化的工作,大部分邏輯都在這裡完成。同事提到 Codex 處理某類批次腳本比較快，於是把 enrichment loop 搬過去試。第三份索性跳過 harness,直接呼叫模型 API,用在一個只需要單一 prompt 和單一回應、不需要工具編排的夜間排程任務。同一份工作,三套實作，每套都是為了配合當下手邊的工具而長成那樣。

每個 harness 都各自綁定自己的工具與網路搜尋,接法也各不相同,於是工程師得用三種不同的設定格式,重寫同一套 enrichment 邏輯。真正花時間的地方，不是改進帳號 enrichment 的品質,而是搞懂 Claude Code 要怎麼宣告工具、為什�麼同一個 MCP server 接到 Codex 裡行為不同,以及原始 API 路徑缺了另外兩套工具白送的哪些東西。

而且工具並不等價,結果自然也不等價。一個 harness 內建的網路搜尋回傳的資料,跟另一個不一樣;某個來源在一套工具裡能讀到,在另一套裡卻讀不到。內建的網路搜尋工具能找到高層級資訊(如募資輪次、高層異動),卻經常漏掉更細緻的細節(如技術堆疊變動)。更麻煩的是,三套實作之上沒有任何統一的視角:沒有共用的計量表,沒人能看到或限制幾十萬個帳號跑一輪的總花費;沒有共用的規則,哪些來源可以讀、什麼時候要人工核准，三套各自為政或根本沒設;沒有共用的記錄,一旦結果出錯,沒有地方能重建 Agent 當時讀了什麼、花了多少、做了什麼決定。它「大致上」能跑出結果,這正是它一直沒被真正修好的原因:好用到讓人捨不得丟,又沒好到能完全信任。

🧩 **Omnigent：把三套實作收斂成一個定義**

Databricks 提出的 Omnigent，是架在各個 harness 之上的一層:工程師只需要定義一次 Agent、它跑在哪個模型上、能碰哪些工具、在什麼政策與限制下運作。三次重寫收斂成一份定義，工具不再是每個 harness 自帶什麼就用什麼,而是宣告在 Agent 上、設定一次就能自由替換。跑在 Databricks 代管的模型上時,模型呼叫會經過 Foundation Model APIs,每一次呼叫的成本、稽核與治理都集中在一個地方，而不是分散在三套 runtime 裡;要換模型或調整成本結構時,只需要改一行設定。

🧩 **網路搜尋變成一個決定,而不是三個**

Omnigent 讓你可以為每個任務設定一致的搜尋選擇,但這個決定本身仍需要指定一個搜尋合作夥伴。文中以 Nimble 為例:Nimble 的 Search API 能用即時網路資料佐證答案；面對需要深入研究的任務,Nimble 的 Web Search Agents 會自動處理搜尋與資料擷取的編排,跨多個來源交叉比對,並回傳附上引用來源的答案,形成一套一般搜尋做不到的稽核軌跡。文中也提到，Nimble 針對 JavaScript 渲染、篩選器、分頁背後的資料有專門的擷取能力,並會記住過去最有效的擷取路徑重複使用,以降低 token 成本。

📊 **一組來自廠商測試的數字**

文中引用 Nimble 自己的測試結果:加入 Nimble 的網路搜尋後,LLM benchmark 準確率從 46% 提升到 71%，同時網路搜尋成本降低一半。這是 Nimble 自行公布的比較數字(對比 Claude 內建搜尋)，讀者宜將其視為廠商測試結果,而非獨立第三方驗證的結論。

⚠️ **這是一篇產品導向的內容**

這篇文章的核心其實是在推廣 Databricks 的 Omnigent 與合作夥伴 Nimble 的搭配使用方式,文中對痛點的描述(三套 harness、三套搜尋結果不一致)具體且貼近真實工程場景,但解法段落帶有明顯的廠商推廣色彩,效能數字也僅來自單一合作廠商的自我測試,沒有獨立驗證。

🎯 **實務啟示**

如果你的團隊也在 Claude Code、Codex、原始 API 之間反覆搬同一套 Agent 邏輯,值得盤點清楚哪些是「工具編排的重複勞動」,哪些才是真正的業務邏輯,把前者收斂成一層共用宣告(模型、工具、政策),能讓工程時間回到後者。至於要不要引入特定的第三方搜尋服務,建議自己拿實際任務跑一輪基準測試,而不是直接採信單一廠商公布的準確率數字。

🔗 **來源**
- 標題：The Web Search Your Agent Inherited Isn't Good Enough
- 作者／機構：Databricks
- 連結：https://www.databricks.com/blog/web-search-your-agent-inherited-isnt-good-enough

#AgenticAI #WebSearch #Databricks #Omnigent #LLMTools #AIGovernance #MCP #AgentInfrastructure #DataEnrichment #AIObservability
