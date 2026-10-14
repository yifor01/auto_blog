---
title: Power real-time applications and agents with Document Intelligence
source: Databricks
url: https://www.databricks.com/blog/power-real-time-applications-and-agents-document-intelligence
model: claude-code/sonnet
generated_at: '2026-10-14T21:09:34.703961'
score: 76
---

📌 Databricks文件智慧API轉正式版，解析、分類、擷取一次打包

TL;DR：Databricks將文件解析、分類、擷取REST API轉為正式版，讓應用與agent即時把文件轉成結構化資料。

Databricks指出，其企業客戶每天收到的文件數以百萬計。這些文件裡藏著營運、客戶、財務的關鍵脈絡，卻長期卡在同一個瓶頸：文件進來之後，得先有人讀過、把重點手動抄出來，才能進入下游的商業分析或決策流程。隨著文件量成長，這個人工環節的延遲與成本只會跟著放大。

🤔 **人工讀文件，正是downstream決策的瓶頸**

無論是發票核對、合約審查還是客服單據歸類，表面上是不同的工作流程，卻共享同一個卡點：在資料能被拿去做分析或決策之前，必須先有人把非結構化文件讀懂、拆解成可用的欄位。這一步沒有自動化,整條管線就動不了。

🧩 **Parsing、分類、擷取三合一，決策路由API搶先測試**

Databricks宣布，用於解析（parsing）、分類（classification）、擷取（extraction）的文件智慧REST API現已正式上線（Generally Available）；另外新增一支用於文件路由的決策（decisions）REST API，目前為beta測試階段。開發者可以在文件抵達的當下呼叫這些API，讓工作流程自動判斷「這份文件是什麼」、拉出需要的細節，再把結果交給對的人或對的agent接手下一步。

💻 **從發票擷取欄位到律師審約，一個REST呼叫搞定**

Databricks舉例，可用`ai_extract` REST API從發票中擷取欄位。這類即時文件理解能力也能直接嵌入既有的工作場域：在Databricks Apps中，可以打造一個合約收件流程，讓律師上傳合約後，開啟審核表單時關鍵條款已經自動填好。除了這種人機協作（human-in-the-loop）的互動式應用，這些API也能被架在Agent Bricks上的自訂agent呼叫,在agent需要理解或分析收到的文件、再決定下一步動作時使用。Databricks也提供以Genie Code輸入prompt來建置此類工作流程的方式，或直接參考REST API文件與解析、分類、擷取各自的操作指南。

🎯 **給正在建置文件工作流程的工程師**

如果你的團隊正苦於為合約、發票、客服單據之類的文件自建擷取管線，這類平臺內建的REST API提供了一條直接整合進既有應用或agent決策流程的路徑，不必從零打造文件理解模型，但實際擷取精準度與延遲表現仍需依自身文件類型實測評估。

🔗 **來源**
- 標題：Power real-time applications and agents with Document Intelligence
- 作者／機構：Databricks
- 連結：https://www.databricks.com/blog/power-real-time-applications-and-agents-document-intelligence

#DocumentIntelligence #Databricks #AgentBricks #RESTAPI #DocumentProcessing #AIAgents #DataExtraction #EnterpriseAI #Automation #LLMOps
