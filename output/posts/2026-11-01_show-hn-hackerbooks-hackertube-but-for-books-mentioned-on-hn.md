---
title: 'Show HN: HackerBooks – HackerTube, but for books mentioned on HN'
source: Hacker News
url: https://hackerbooks.org
model: claude-code/sonnet
generated_at: '2026-11-01T21:24:00.184787'
score: 58
---

📌 開發者只負責「做決定」：HackerBooks 是 Claude 包辦寫成的 HN 書單站

TL;DR：仿造 Karpathy 的 HackerTube，把 Hacker News 留言裡提過的書整理成資料庫，程式碼幾乎全由 Claude Opus 5.5 寫成。

Karpathy 做了 HackerTube，把 HN 留言裡提到的 YouTube 影片整理成清單。這次有人動了同樣的念頭，只是換成書——而且這個開發者幾乎沒自己動手寫一行程式碼。

🤔 **靈感來自 HackerTube，標的換成書**

作者 roansh 在 Show HN 貼文中提到，看到 Karpathy 的 HackerTube 後，想要一個同樣邏輯但針對書籍的版本：掃過 2007 年至今所有 HN 留言，找出被提及的書名，並附上留言連結讓讀者回溯原始討論脈絡。

🧩 **收錄門檻：至少兩位不同留言者提過**

目前站上收錄約 1.65 萬本書，收錄標準是「至少兩位不同的 HN 留言者」都提到過同一本書。每本書底下都連回實際提到它的留言串，方便讀者直接看當年的討論情境。作者特別說明，整個資料管線（data pipeline）與網站本身幾乎都是 Claude 寫的，他自己的角色是「steered and made calls」——也就是引導方向、做取捨判斷，以及處理像買網域名稱這類瑣事。

💡 **資料是開放的，可下載**

網站的 about 頁面提供資料下載，等於把整個書單資料庫公開給任何想自行分析或二次利用的人。

⚠️ **「提及次數」不等於「推薦」**

作者坦言這套統計方法不完美：只要一本書被提到，無論是被稱讚還是被批評，都會被計入一次提及，所以排名高不代表評價好。他也公開邀請讀者回報「漏收的愛書」或「配對錯誤的書名」，顯示這套自動化比對仍有誤判空間。

🎯 **給工程師的啟示**

這是一個「人只做決策，AI 包辦實作」的side project案例：資料爬取、比對邏輯、前端網站全交給 agentic coding 完成，開發者的工作量集中在產品判斷與把關，而不是寫程式碼本身。對於想評估 agentic coding 工具能把個人專案做到多完整的工程師，這是一個值得觀察的真實樣本。

🔗 **來源**
- 標題：Show HN: HackerBooks – HackerTube, but for books mentioned on HN
- 作者／機構：roansh（Hacker News）
- 連結：https://hackerbooks.org

#HackerNews #ShowHN #Claude #AgenticCoding #SideProject #AIBuiltProduct #DataPipeline #OpenData #Anthropic #BookRecommendations
