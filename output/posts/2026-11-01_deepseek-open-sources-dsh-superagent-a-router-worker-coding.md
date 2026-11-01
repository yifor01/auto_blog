---
title: DeepSeek Open-Sources dsh-superagent, a Router-Worker Coding Agent
source: MarkTechPost
url: https://www.marktechpost.com/2026/11/01/deepseek-dsh-superagent-router-worker-coding-agent/
model: claude-code/sonnet
generated_at: '2026-11-01T21:17:19.181613'
score: 94
---

📌 【DeepSeek 開源】人類注意力才是多 agent 系統的瓶頸

TL;DR：DeepSeek 開源 dsh-superagent,用 Router-Worker 兩層架構把 GitHub 請求拆成並行工作項,減少人需要盯著看的 session 數量。

多 agent 系統常被拿來比參數、比分數,但 DeepSeek Harness 團隊最新開源的 dsh-superagent,關注的是另一個問題:當一個人同時開多個 agent session 時,到底能跟上幾個?

🤔 **人能同時追蹤的 session,只有 3 到 5 個**

dsh-superagent 是一個 MIT 授權的研究原型,打包成 DeepSeek Harness 的一個 bundle,運作方式是監聽 GitHub,也可選擇監聽 Feishu。它是一個「等你開口才動作」的 GitHub agent:當獲授權的人對它提出要求,它會開一個稱為 Ticket 的工作項,每個 Ticket 在自己的 session 與目錄裡執行,結果會回到原本的對話串,通常以 pull request 的形式呈現,本地的網頁面板只列出需要人判斷的事項。

這份釋出同時附上一篇設計文章《Exploring Super-agent Design: Towards a More Autonomous Agent System》。DeepSeek 團隊在文中指出,主流 agent 把「一個 session」當成基本單位,但根據 ifeng 轉述該報告的說法,一個人實際上只能主動跟上 3 到 5 個 session,多工的瓶頸不在模型能力,而在人類注意力。

README 把核心原則寫得很直白:盡量少佔用人的注意力,盡量多產出價值。設計理念文件把這句話落實成具體行為:agent 只確認一次,工作中保持安靜,只有在有結果、有疑問或失敗時才會再開口。

🧩 **長駐的 Router 負責調度,獨立的 Worker 負責動手**

研究團隊把架構分成兩層:長時間運行的 Router 負責互動與派工,彼此隔離的 Worker session 負責實際動手做事。在這個原型裡,這個流程很具體:主 session 跑著工具集較小的 dsh-superagent-router 預設設定,每個 Worker 則跑 dsh-superagent-worker。根據其執行文件,Shell 指令會在 5 秒後轉入背景執行,讓 Worker 能持續接收訊息。

主動發起的工作會被把關:授權文件定義了三種接受模式,off、observe(預設)與 auto。在 observe 模式下,agent 只會記錄它原本會接受的請求,而不會真的動手。團隊也列出了原型之外的構想,包括外部 Watchdog、儲存與運算分離,以及非同步的 ReAct 迴圈。

📊 **拿掉事件直通後,快取 token 用量多了近四成**

DeepSeek 用模擬的群組聊天與 GitHub CI 串流做測試,每次執行大約有 300 則訊息,其中約 20 則是真正的工作請求,每種方案各跑 5 次。一項拿掉「事件直通」機制的消融實驗顯示,Router 的決策次數上升了約 30%,快取讀取 token 用量上升約 37%,從 2323 萬上升到 3177 萬。以上數字均為自我報告,且來自 ifeng 對該報告的二次轉述。

⚠️ **數字來自二次轉述,仍是研究原型**

這些測試數字並非第一方論文的原始數據,而是經由 ifeng 轉述的報告內容,解讀時應保留一定保留空間。同時,dsh-superagent 目前明確定位為研究原型,外部 Watchdog、儲存運算分離等構想尚未落地。

🎯 **實務啟示**

對維運 GitHub 專案或內部工具鏈的工程師來說,這個架構值得借鑒的地方在於把「調度」與「執行」明確拆成兩層,並用三種接受模式(off／observe／auto)做漸進式授權,讓團隊可以先用 observe 模式觀察 agent 會做什麼決策,再逐步放寬到自動執行,降低一次性全自動化帶來的風險。

🔗 **來源**
- 標題：DeepSeek Open-Sources dsh-superagent, a Router-Worker Coding Agent
- 作者／機構：Asif Razzaq，MarkTechPost
- 連結：https://www.marktechpost.com/2026/11/01/deepseek-dsh-superagent-router-worker-coding-agent/

#DeepSeek #AIAgent #OpenSource #CodingAgent #GitHub #RouterWorker #LLM #DeveloperTools #AIAutomation #SoftwareEngineering
