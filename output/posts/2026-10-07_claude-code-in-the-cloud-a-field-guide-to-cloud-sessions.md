---
title: 'Claude Code in the cloud: a field guide to cloud sessions'
source: Claude Blog
url: https://claude.dev/blog/claude-code-in-the-cloud/
model: claude-code/sonnet
generated_at: '2026-10-07T22:27:39.081480'
score: 83
---

📌 Claude Code上雲端:三個任務同時跑,各自一臺機器不互撞

TL;DR:雲端session讓每個Claude Code任務跑在獨立VM上,平行作業不再搶檔案、搶port。

你在自己的筆電上同時開兩個Claude Code工作階段,大概會遇到兩個麻煩:它們共用同一份working tree,可能改到同一個檔案、搶同一個port;而且只要筆電睡著或Wi-Fi斷線,工作就停了。Anthropic這篇指南示範的雲端session,把這兩個麻煩直接解決掉。

🤔 **本機session的三個先天限制**

本機執行的Claude Code session有三個特性:共用你的working tree(兩個session同時跑同一個repository會互相干擾檔案與port)、使用你本人的credentials、電腦睡眠或斷網就會停止。

🧩 **雲端session怎麼運作**

雲端session讓Claude Code跑在屬於自己的機器上。每個任務都會拿到一臺全新的虛擬機器,repository會被clone到一個新分支上,而且環境設定已經事先裝好。你可以從claude.ai/code、Claude手機App、桌面App、終端機,或是Slack啟動一個雲端session,再透過瀏覽器、手機、桌面App追蹤進度。工作完成後,成果會停在一個分支上,你可以直接把它變成pull request。

雲端session內含在Pro、Max、Team、Enterprise方案裡,不額外收費,用量算在Claude Code原有的額度裡(依方案不同,組織擁有者可能需要先手動開啟)。文中也提到現有Pro、Max個人訂閱戶可以在10月7日前申請一次性雲端session獎勵額度,Pro方案100美元、Max方案250美元,額度將在11月4日到期,用完或過期後回歸一般方案用量,且不適用於Projects或Routines。

📊 **實測:三個任務、三臺機器、同一份repository**

作者用一個名叫tidepool(預測三個虛構港口潮汐的小型Node API)的範例repository,在16秒內依序啟動三個雲端session,各自處理一個問題:

1. `npm test`大約四次會跑出一次失敗——找出根因並修好,再連續跑30次以上驗證
2. `docs/API.md`跟`src/server.js`的內容對不上——重寫文件讓每個endpoint、參數、預設值、回應格式都對齊程式碼,並實際啟動伺服器用curl逐一驗證
3. 讓`src/logger.js`輸出每行一個JSON物件,保留LOG_LEVEL,並記錄method、path、status、duration_ms等欄位,同時補上測試

三個session分別跑了61秒、65秒、72秒,全部在第一個啟動後87秒內完成(其中重建repository的setup步驟就佔了每個任務三分之一到一半以上的時間,正式使用GitHub clone時可以省略)。結果:第一個session在`TtlCache.get`裡找到一個競態條件(cache在loader執行完才存值,導致同一個key在載入中被再次呼叫會重複觸發loader),改成先存進行中的promise、載入失敗就移除該項,並連續跑了40次`npm test`零失敗。第二個session啟動伺服器、對每個endpoint跑curl,找出文件裡五個錯誤(列出API實際不會回傳的欄位、文件了一個程式碼根本沒讀的`days`參數、把公尺寫成英尺、漏掉`/next-high`endpoint、沒寫錯誤回應),還發現一個不在任務範圍內的bug(`from=`格式錯誤時回傳200加空列表)但選擇只記錄成caveat,沒有擅自修改程式碼。第三個session寫好JSON logger、把request log改成結構化欄位、加了五個測試,但提交時發現有一個測試失敗,重跑八次裡失敗五次,追查後發現正是第一個session在修的同一個競態條件——它提出了相同的修法,但因為超出自己任務範圍而沒有動手修改cache,並在摘要裡誠實註明測試套件並不乾淨。

💡 **隔離性既是優點,也要留意銜接**

logger session完全不知道cache修復正在進行中,正好說明了雲端session的隔離特性:每個session有自己的repository副本、自己的程序、自己的分支,文件session和logger session都各自啟動了API伺服器來測試,彼此互不影響。但這也意味著拆分平行任務時,最好沿著檔案邊界切分,依合理順序合併分支,並預期某個session回報的問題,可能正是另一個session正在處理的。

🧩 **雲端session底層架構的四個關鍵**

每個任務都拿到專屬機器:全新VM搭配clone到新分支的repository,session之間碰不到彼此的檔案或port。你的GitHub token不會進入VM:由一個proxy代持,session拿到的是只能推送到自己working分支的短期憑證。repository的Claude設定會跟著走:CLAUDE.md、rules、skills、agents、commands都會隨repo帶上,但你個人的設定不會跟著走。閒置的VM會被回收:重新打開session會拿到全新VM並還原對話紀錄,所以在意的工作要記得commit。

🎯 **實務啟示**

雲端session不是要取代本機session,而是兩者互補。需要同時跑多個獨立任務、任務會長時間執行、或是不想讓本機熄屏中斷工作時,雲端session是更合適的選擇;而需要即時互動、或任務需要存取本機SSH金鑰、雲端CLI等本機才有的資源時,本機session仍是必要的。拆分平行任務時建議沿檔案邊界切,並對分支合併順序與session之間的資訊落差有心理準備。

🔗 **來源**
- 標題:Claude Code in the cloud: a field guide to cloud sessions
- 作者/機構:Anthropic
- 連結:https://claude.dev/blog/claude-code-in-the-cloud/

#ClaudeCode #Anthropic #CloudComputing #DeveloperTools #CICD #AIAgents #SoftwareEngineering #ParallelComputing #GitHubIntegration #DevOps
