---
title: Claude Code sends your email address to websites
source: Hacker News
url: https://github.com/anthropics/claude-code/issues/107757
model: claude-code/sonnet
generated_at: '2026-11-06T22:24:40.641686'
score: 86
---

📌 Claude Code 把使用者 Email 塞進 User-Agent 送出

TL;DR：GitHub issue 曝光 Claude Code 搜尋時外洩 email,引爆開發者社群怒火。

一位開發者在 GitHub 上回報,他每天收到數十封詐騙郵件,原因竟是 Claude Code 在執行網路搜尋時,未經同意就把他的 email 位址寫進 HTTP 請求的 User-Agent header,傳送給任意第三方網站。這則 issue 在 Hacker News 上累積超過 1,500 點、487 則留言,成為近期開發者圈討論度最高的隱私爭議之一。

🤔 搜尋請求裡藏著你的身分

根據 2026 年 11 月 5 日提出的 GitHub issue #107757,回報者 taylor-edwards 描述:Claude Code 在進行 agentic 網路搜尋時,會把使用者的 email 放進 User-Agent header 一併送出。回報者強調,這不該是一個可以 opt-in 或 opt-out 的設定選項,而是應該直接從 harness 中整個移除,因為這個行為對不喜歡 agentic 流量的服務沒有任何幫助,也無法保護使用者在網路上的匿名性,反而成為詐騙者眼中的「金礦」。這則回報的環境資訊標注平臺為 macOS、終端機為 tmux、版本為 2.1.318,並附上標籤 area:security、area:tools、bug、platform:macos。

💡 社群反應激烈,連遷移方案都搬上檯面

這則 issue 獲得超過 680 個 👍 反應、上百個 😄 與 👀 反應,顯示大量開發者都遭遇類似情況或對此表示認同。回報者在文中直接表示,因為對 Anthropic 保護隱私的做法失去信心,正在將公司遷移到搭配 OpenRouter 的 Pi。這種反應某種程度反映出,對開發者工具而言,身分可識別資訊（PII）意外外洩不只是技術 bug,更會直接衝擊使用者對廠商的信任。

從 issue 的後續活動來看,開發者 TortoiseWolfe 在 2026 年 11 月 6 日提交了一個名為「Refuse web calls that carry the account owner's email address」（#297）的 commit,引用了這則 issue 作為修復對象。不過截至目前,issue 狀態仍標示為 open,代表問題的完整修復與驗證仍在進行中。

⚠️ 素材未說明的部分

目前可確認的事實僅限於回報內容與社群反應,至於 email 被寫入 User-Agent 的具體技術原因（例如是哪個功能、哪段程式碼造成)、修復 commit 是否已經正式發布到穩定版本,素材中並未提供進一步細節,不宜過度推測。

🎯 對工程團隊的提醒

這起事件提醒使用 AI coding agent 的團隊,agent 發出的網路請求同樣可能攜帶可識別個資,尤其是在企業環境中,建議檢視 agent 工具實際送出的 HTTP header 內容,並評估是否需要透過 proxy 或網路層稽核來攔截非必要的身分資訊外洩,而不是只信任廠商預設的隱私承諾。

🔗 來源
- 標題：Claude Code sends your email address to websites
- 作者／機構：motoroco
- 連結：https://github.com/anthropics/claude-code/issues/107757

#ClaudeCode #Anthropic #Privacy #DataLeak #AIAgents #DeveloperTools #Security #OpenSource #PII #AICoding
