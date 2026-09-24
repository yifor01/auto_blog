---
title: Once Claude can measure something, it can make it faster
source: Hacker News
url: https://claude.dev/blog/how-we-made-claude-ai-faster/
model: claude-code/sonnet
generated_at: '2026-09-24T20:44:52.846952'
score: 88
---

📌 【Anthropic】把 Claude 變成自己的效能工程師，兩週讓 claude.ai 快 3 倍

TL;DR：Anthropic 讓 Claude 自主找瓶頸、寫 benchmark、上線修復，兩週內把 claude.ai 平均加速 3.1 倍。

使用者一直在抱怨 claude.ai 太慢，而 Anthropic 團隊的做法很不尋常：不是直接派工程師去排查，而是開一個 Slack channel，把 Claude 放進每一個討論串，讓它自己去找瓶頸、驗證假設、寫程式修，人類只負責定目標、做取捨、審核每一個變更。

🤔 一個 Slack channel，一個常駐指令

團隊在衝刺開始前只給 Claude 一段標準指令：你的工作是負責 claude.ai 網站與桌面 app 的效能，包括監控每次部署有沒有效能退化、評估現有 telemetry 是否準確完整、維護觀測儀表板、主動修復觀察到的問題與唾手可得的改善、提出效能專案構想，並與人類隊友溝通。文章特別寫明，終極目標是讓這個 channel 盡可能自主運作，「但今天我們知道還做不到」。

🧩 先找出 95% 使用量集中在哪四段旅程

Claude 透過 Datadog MCP server 分析使用資料，找出四個涵蓋 95% 使用者活動的關鍵旅程：啟動 app、開始新對話、載入既有對話、傳送訊息。橫跨 web 與桌面、以及不同產品線，這四段旅程共拆解出十三項可直接比較的量測指標。團隊為每個指標補齊 instrumentation，確保「使用者互動開始」到「結果渲染完成」之間的量測是可比的，並區分出 client 端與 server 端各自的耗時。

衝刺一開始，團隊列出約二十個針對特定旅程的候選專案，由 Claude 估算每個專案能省下多少毫秒，據此設定衝刺目標。結果到第三天，十三項目標裡已經命中十二項——原訂計畫提前完成後，團隊把剩下的時間交給 Claude 自己去找新的優化空間，包括「開放接受各種瘋狂點子」。

📊 十三項指標，平均快 3.1 倍

以下是 8 月 13 日與 8 月 27 日的 p75 real user monitoring 對比：

| 旅程 | 平臺 | 優化前 | 優化後 | 加速倍數 |
|---|---|---|---|---|
| 啟動 app | claude.ai web 冷載入 | 3,085 ms | 550 ms | 5.6x |
| 啟動 app | 桌面 app 冷啟動 | 6,310 ms | 3,328 ms | 1.9x |
| 開始對話 | Chat web | 416 ms | 273 ms | 1.5x |
| 開始對話 | Chat 桌面 | 460 ms | 224 ms | 2.1x |
| 開始對話 | Claude Code 桌面 | 837 ms | 347 ms | 2.4x |
| 載入對話 | Chat web | 1,557 ms | 646 ms | 2.4x |
| 載入對話 | Chat 桌面 | 1,353 ms | 488 ms | 2.8x |
| 載入對話 | Claude Cowork 桌面雲端 | 2,566 ms | 728 ms | 3.5x |
| 載入對話 | Claude Code 桌面 | 545 ms | 262 ms | 2.1x |
| 傳送訊息 | Chat web | 180 ms | 59 ms | 3.1x |
| 傳送訊息 | Chat 桌面 | 140 ms | 64 ms | 2.2x |
| 傳送訊息 | Claude Cowork 桌面雲端 | 928 ms | 48 ms | 19x |
| 傳送訊息 | Claude Code 桌面 | 250 ms | 52 ms | 4.8x |

十三項指標的幾何平均加速為 3.1 倍。團隊估算，這樣的改善每天能為使用者省下數萬小時的等待時間。具體改動包括：把靜態輸入框直接烤進 HTML，讓使用者在 React 初始化期間就能打字；為桌面殼層預先編譯 V8 code cache，避免主程序每次都要重新編譯；切換對話時保持輸入框不卸載；使用者滑鼠懸停時預先抓取該對話的 session；以及把側邊欄的 re-render 次數砍掉 90%。

💡 當「毫秒」太吵，就換一把尺

團隊很快發現一個限制：wall-clock 時間會受使用者真實感受影響，但雜訊太大，不適合當 CI 的硬性門檻。於是他們和 Claude 一起找出一整套確定性（deterministic）的替代量測：純 JS 熱路徑用 Valgrind 搭配 `node --predictable` 數指令數；瀏覽器路徑則用 React commit 次數、V8 precise coverage 的函式呼叫次數、layout／style 重新計算次數、DOM mutation 次數這一整串「梯子」。但每一個新 benchmark 都被要求先證明自己真的能追蹤真實的 wall-clock 延遲，團隊甚至明講：如果某個 benchmark 沒辦法證明能帶來可量測的實際加速，就會被下架，避免 Claude 爬錯山頭。例如，團隊要求 Claude 用指令計數去優化「組裝對話訊息樹」的例行程式，以及 Claude Code 輸出中的狀態列掃描器，並先驗證指令數下降確實對應到真實延遲下降。

📊 三千多次變更，零客戶可見事故

整個衝刺期間，團隊用的是內部研究模型「Claude Tag（beta）」，能力大致相當於 Opus 5.5。過程中合併了超過三千個變更，沒有發生任何客戶可見的事故或回滾。人類團隊的角色始終是設定目標、做取捨判斷、審核每一個實際上線的變更。

🎯 實務啟示

這個案例對做效能優化的工程團隊有兩個可直接借鏡的地方：第一，把「模糊的抱怨（很慢）」轉成「95% 使用量集中在哪四段旅程」這種可量測、可分解的問題，是任何優化工作的起點，不論執行者是人還是 AI。第二，當 wall-clock 太吵不適合當 CI gate 時，找一把「確定性但需要先驗證與真實延遲相關」的替代尺規，比盲目相信某個看起來合理的代理指標更可靠——這條「先證明相關性，再拿來當門檻」的紀律，本身就是值得搬進團隊流程的做法。

🔗 來源
- 標題：Once Claude can measure something, it can make it faster
- 作者／機構：matthieu_bl（Hacker News 投稿）
- 連結：https://claude.dev/blog/how-we-made-claude-ai-faster/

#Anthropic #ClaudeAI #PerformanceEngineering #WebPerf #AIAgents #DeveloperProductivity #Observability #RUM #FrontendPerformance #AIOps
