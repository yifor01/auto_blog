---
title: How we eliminated $1 million a year of wasted AI agent spend in one hour
source: Databricks
url: https://www.databricks.com/blog/how-we-eliminated-1-million-year-wasted-ai-agent-spend-one-hour
model: claude-code/sonnet
generated_at: '2026-09-02T10:05:06.523102'
score: 97
---

📌 七個小 bug,一年悄悄燒掉 120 萬美元

TL;DR:Databricks 用追蹤加自然語言查詢,一小時揪出百萬美元的 agent 浪費。

一個 agent 任務照樣完成,成本儀表板也只是多跳了 10%,看起來像是用量成長,實際上可能是七個沒人發現的小 bug 在背後燒錢。Databricks 工程團隊用這個方法,一小時內找到並修好了每年造成 120 萬美元損失的問題。

🤔 **agent 不會大聲喊救命,只會默默重試**

Databricks 內部大量使用 AI agent 加速開發,這些 agent 需要透過 MCP 伺服器上的工具存取系統日誌、使用量資料表、支援工單、wiki 等資源。團隊發現一個關鍵風險:當工具出錯時,呼叫它的 agent 很少直接失敗,而是重試、猜測,最終想辦法繞過問題,過程中悄悄燒掉 token 與工程師的時間。這種浪費特別危險,因為從外部看任務仍然完成,聚合的 token 支出儀表板呈現的成長很容易被誤讀成正常的用量增加。

🧩 **追蹤每一次工具呼叫,再用白話文問問題**

Databricks 靠兩項工具找出問題:Unity Gateway 會為每一次 MCP 工具呼叫自動產生 OpenTelemetry 追蹤紀錄,包含工具名稱、參數、錯誤(若有)、token 數、延遲與串連同一工作階段的 session ID,不需要額外埋碼,因為 Gateway 本來就在每次呼叫的路徑上。Genie One 則讓團隊直接用自然語言對這張追蹤資料表提問,不用自己寫 SQL 或摸索 schema。團隊把「agent 好像在 Jira 呼叫上打轉」這種模糊的懷疑,丟給 Genie One,幾分鐘內就拿到一份量化排序過的 bug 清單。

📊 **一個 `.split()` 呼叫,一年燒掉 8.7 萬美元**

在單一 24 小時的觀測窗口中,團隊在 Jira 與 Google Drive/Docs 的工具伺服器中找到多個問題,包括 `KeyError: 'fields'`、`'list' object has no attribute 'split'`、GDrive 的 `Invalid field selection` 等。當中頻率最高的一個 bug,一天發生 535 次:Jira 的 `issues.search` 工具要求 `fields` 參數是逗號分隔字串(例如 `"key,summary,status"`),但模型依據 JSON 慣例與同一個工作階段中其他工具呼叫的線索,合理地推斷應該傳入陣列。伺服器收到陣列後呼叫 `.split()` 直接丟出一段對 agent 毫無意義的 Python 錯誤訊息,agent 因此重新猜測,平均要 12 輪才能恢復,30% 的工作階段還會重複踩到同一個錯。單是這一個 `.split()` 呼叫,估計每年造成 8.7 萬美元的 token 浪費與 4,850 小時的 agent 等待時間。Google Drive 的 `Invalid field selection` 錯誤影響範圍更大:49.6% 的 `drive_file_get` 呼叫都失敗,原因是模型持續傳入看起來合理的 Drive API 欄位名稱(如 `id`、`name`、`mimeType`),但工具的端點並不接受。

七個 bug 加總起來,估計每年造成約 49.9 萬美元的 token 浪費,以及約 1.2 萬工程時的 agent 等待時間,合計約 120 萬美元的生產力損失。找出全部七個 bug、量化影響並修好,整個過程大約花了一小時。

💡 **工具該適應 LLM 怎麼呼叫它,而不是反過來**

Databricks 團隊的結論是,錯誤訊息品質確實與恢復成本高度相關,但更值得注意的問題是模型一開始為什麼會「呼叫錯」。多數情況下模型並沒有呼叫錯:MCP 工具的參數規格經常刻意寫得比較鬆散,一方面為了泛用性,一方面每多一行參數說明都要在每次呼叫時多付 token 成本。結果就是規格含糊時,模型會用合理的猜測填補空白,而 JSON 陣列本來就是「一串欄位」的合理猜測。真正的 bug 不是模型呼叫錯了工具,而是伺服器只接受眾多合理解讀中的一種,對其餘的都直接崩潰。設計原則因此該反過來:工具要能吸收模型自然會給出的變化,例如把陣列轉成字串、對缺省參數給預設值、忽略非預期的額外參數,而不是要求呼叫方精準命中作者心中唯一的那種格式。

🎯 **實務啟示**

修 bug 本身不難,難的是知道要修什麼。如果團隊已經有 agent 透過 MCP 工具運作,替呼叫路徑加上追蹤、再用自然語言查詢工具去問「哪裡一直出錯」,是一個成本很低但能直接轉換成實際節省的排查方法,而不是等成本儀表板出現異常增長才去猜原因。

🔗 **來源**
- 標題:How we eliminated $1 million a year of wasted AI agent spend in one hour
- 作者／機構:Databricks
- 連結:https://www.databricks.com/blog/how-we-eliminated-1-million-year-wasted-ai-agent-spend-one-hour

#AIAgents #MCP #Observability #Databricks #LLMOps #CostOptimization #AgentTooling #OpenTelemetry #AIInfrastructure #ToolCalling
