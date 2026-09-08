---
title: Build durable agents with Temporal and Lakebase
source: Databricks
url: https://www.databricks.com/blog/build-durable-agents-temporal-and-lakebase
model: claude-code/sonnet
generated_at: '2026-09-08T20:10:55.279502'
score: 87
---

📌 Agent 要等審核員好幾天才能繼續,你的架構撐得住嗎?Temporal + Lakebase 的耐久執行方案

TL;DR：Databricks 展示如何用 Temporal 做耐久執行、Lakebase Postgres 做可查詢狀態,讓長時間等待人工審核的 agent 撐過 worker 重啟與工具呼叫失敗。

一個個人貸款核保 agent 收集證據、套用政策後,可能要等審核員好幾天才有回應。這段等待期間,worker 可能重啟,工具呼叫可能失敗。應用程式必須保留已完成的工作、能夠恢復執行,並讓審核員隨時看得到目前的證據——這正是 Databricks 這篇參考架構想解決的問題。

🤔 **雲端 agent 的存活時間,可能比啟動它的 worker 還長**

使用者今天開始一個 session,明天回來,可能是在另一個 worker 上繼續執行。部署與程序失敗是常態,所以 agent 的進度必須獨立於執行它的程序而存活。要能恢復,不只需要已完成操作的結果,還需要控制流程本身的狀態:哪些操作已被排程、哪些結果已被記錄、agent 目前在等什麼、又已經接受了哪些指令。單純的對話紀錄只能涵蓋部分狀態,恢復機制需要的是完整的控制流程歷史。

🧩 **Temporal 管控制流程,Lakebase 管應用面狀態**

在 Temporal 的模型裡,Workflow 是一次 agent 執行的耐久控制流程;Activity 是對模型、工具或資料庫的一次呼叫,其結果會被記錄進 Workflow 的 Event History,並可重試;Signal 則是送給執行中 Workflow 的非同步指令,例如審核員的核準決定。

這份參考實作(Temporal Lakebase AgentWorkflow)是一個可執行的個人貸款核保 agent:呼叫多個工具、讀取受治理的政策、產出建議並等待審核員回應。Temporal 與 Lakebase 儲存的是給不同消費者看的不同狀態:Temporal 的 Event History 驅動 replay(重播),Lakebase 儲存的是應用面視圖——目前執行狀態、訊息、證據、審核狀態與指標。Unity Catalog 仍是政策的來源,一張 synced table 讓政策可以在 Postgres 中被查詢,而 Change Data Feed(CDF)則提供把操作歷史送回 Unity Catalog 管理的 Delta 歷史表的回傳路徑。這兩個系統並不共用交易:Lakebase 的寫入是以 Temporal Activity 的形式在「至少一次執行」語意下進行,靠決定性識別碼、限制條件、有守衛的更新與 Postgres upsert,確保 Activity 重複嘗試時仍指向同一筆邏輯記錄。

作者選擇貸款核保作為案例,是因為同一次執行必須收集證據、套用政策、產出建議、並等待人員決策,worker 可能在任何步驟之間失敗,政策也可能在不重新部署應用程式的情況下變動,而 UI 需要在 Workflow 結束前就能看到目前的證據。範例中,申請人資料由模擬的信用局與收入來源取代真實資料,工具呼叫順序則是固定的,以求簡化。

📊 **一筆申請怎麼流過整個系統**

每個請求包含使用者 ID、申請人 ID、金額、用途、模型選擇與回合上限。FastAPI 指派 run_id,啟動 LoanUnderwritingWorkflow,並讓這個 ID 貫穿 API、Temporal 執行與 Lakebase 資料列。第一回合中,credit_check 回傳信用分數、信用額度、逾期紀錄與目前債務;income_verification 回傳收入與僱用證明;debt_to_income_calc 計算負債收入比;policy_lookup 依貸款用途載入政策,並依核准、轉介、直接拒絕三種門檻評估證據。範例中的邊緣案例申請人信用分數 665、年收入經核實為 76,000 美元、月負債 2,400 美元,並有一筆非實質性的逾期標記。政策評估結果會記錄每一條規則、門檻、實際數值、通過/失敗結果、來源、建議與理由。模型只能給建議,不能做決定;審核員核准、拒絕或要求補件,補件要求會變成另一則使用者訊息、開啟新的一個 agent 回合。

技術堆疊方面,React 與 FastAPI 負責 HTTP 與 UI(啟動執行、呈現證據、列出案件、送出審核決定);Temporal Cloud 儲存 Event History 並派送任務;Worker 重播 Workflow 程式碼並執行模型、工具與 Lakebase 的 Activity,網路與資料庫 I/O 都被排除在具決定性的 Workflow 程式碼之外。Lakebase 保有兩個操作 schema:agent_ops 存放執行狀態、訊息、工具呼叫、審核紀錄、事件與指標,可直接用 SQL 查詢;agent_policy 則是唯讀的 synced 政策表,供 policy_lookup 使用。

在重試策略上,呼叫模型的 Activity 允許最多 4 次嘗試、3 分鐘的排程到完成逾時;工具呼叫的 Activity 允許最多 3 次嘗試、60 秒的開始到完成逾時;Lakebase 的 Activity 允許最多 5 次嘗試、15 秒逾時。文中也點出一個具體風險:Lakebase 的工具結果寫入可能在 Worker 回報 Activity 完成之前就已提交,若此時連線中斷,Temporal 沒有記錄到完成結果,就會再排一次嘗試——兩次嘗試代表的是同一筆邏輯寫入,靠 run_id 錨定的穩定識別身分來確保不會重複產生記錄。測試案例特別涵蓋了完成工具呼叫後 worker 崩潰、已提交但 Activity 完成訊息遺失、審核被擱置數天、瀏覽器端決定過期、以及執行過程中政策變動等情境。

⚠️ **這是廠商組合方案,不是通用模板**

這套架構額外引入了兩個受管理的系統,以及兩者之間的一份「投影契約」(projection contract),換取的是韌性與可擴展性,但也代表你需要同時維運 Temporal 與 Lakebase 兩套基礎設施。文章也明確指出,這個組合最適合的場景是:agentic session 必須撐過 worker 更換、需要在長時間等待後接受輸入、需要向應用程式曝露關聯式狀態、並且要在執行期間套用受治理的資料。若場景不具備這些特徵,引入這套組合的維運成本可能大於收益。

🎯 **實務啟示**

若你的 agent 有「長時間等待人工決策」與「工具呼叫需要強一致恢復」這兩個特徵(例如審核流程、批准流程),這篇文章提供的 Workflow/Activity/Signal 劃分方式,以及用決定性識別碼處理「至少一次執行」下重複寫入的做法,值得直接參考;若只是短生命週期的一次性任務,不必然需要引入這麼重的架構。

🔗 **來源**
- 標題：Build durable agents with Temporal and Lakebase
- 作者／機構：Databricks
- 連結：https://www.databricks.com/blog/build-durable-agents-temporal-and-lakebase

#Temporal #Databricks #Lakebase #DurableExecution #AIAgents #UnityCatalog #WorkflowOrchestration #Postgres #AgenticAI #DataEngineering
