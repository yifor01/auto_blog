---
title: Brave Search API now accepts agentic payments via the x402 protocol
source: Hacker News
url: https://brave.com/blog/search-api-agentic-payments/
model: claude-code/sonnet
generated_at: '2026-11-13T22:56:40.925290'
score: 79
---

📌 Brave Search API 支援 x402,搜尋請求直接用加密貨幣逐次付費

TL;DR：Brave Search API 整合 x402 協定,讓 AI agent 可以不開帳號、按次用 USDC 付費搜尋。

要讓一個自主運作的 AI agent 去呼叫某個 API,傳統做法是先幫它辦帳號、辦 API key、綁定付款方式。這套流程對人類開發者來說很正常,但對一個應該要能自主行動的 agent 來說,反而是個笨重的中間步驟。Brave Search API 現在讓 agent 可以直接跳過辦帳號這一步,改用開放的 x402 協定逐次付費。

🤔 **Agent 要用 API,為什麼還要先辦帳號？**

Brave Search API 是 Brave 提供給開發者、用來建構網路資料應用程式的開發工具。這次更新讓開發者與自主運作的 AI agent,可以在需要「agentic 搜尋」時,直接以程式化方式查詢 Brave 的獨立搜尋索引、為 agent 的回應提供依據（grounding）,並即時完成付款結算,不再需要傳統的 API key 管理流程。

🧩 **收到 HTTP 402,就簽署付款重新送出請求**

Brave Search API 在 x402 協定下的端點,要求的是「每次請求都要付款」,而不是傳統的身分驗證。運作流程是：
- Agent 送出一個沒有附帶付款資訊的請求。
- 伺服器回應 HTTP 402 Payment Required,裡面寫明這次搜尋的價格與所需的付款細節。
- Agent 簽署對應金額的 USDC 付款,附上簽名後重新送出同一個請求。
- 付款驗證通過後,搜尋執行,結果連同這筆 Base 區塊鏈上交易的收據一起回傳。

Brave 自己架設了接受 USDC（在 Base 區塊鏈上）的 facilitator,官方表示未來會支援其他網路與其他穩定幣。要串接 x402,最簡單的路徑是安裝 Purl Wallet,這是 Stripe 開發的 CLI 錢包,專門給 agent 使用;只要把 Base 鏈上的 USDC 轉進錢包,就可以開始查詢。

📊 **定價沿用既有 API 費率**

Brave 的 LLM Context 端點（專門為 agent 提供搜尋依據而設計的 API）每次查詢 0.005 美元（每千次 5 美元）;一般網頁搜尋、新聞、圖片、影片與地區搜尋端點同樣是每次 0.005 美元。目前在 Base 鏈上交易所需的 gas fee,會由 Brave 在限定時間內代為負擔。由於每一次請求本身就附帶付款,使用這項服務也不再需要先申請 Brave Search API 帳號。

💡 **代理支付基礎設施的一塊拼圖**

x402 協定本身是為了解決「機器與機器之間即時結算」這個問題而設計的,HTTP 402 這個長年閒置的狀態碼終於有了實際用途。Brave 這次的整合,把它用在一個相對具體且高頻的場景：搜尋 API 呼叫。對比起要去中心化交易所換幣、簽多重簽署合約那種複雜場景,搜尋付費的金額小、頻率高,正好適合驗證這種「按次微額付款」模式是否能在真實流量下跑得順暢。

🎯 **對開發者的實際意義**

如果你在打造自主運作的 agent 系統,不需要再為每個 agent 實例管理 API key 與帳單方案,只要幫 agent 的錢包補上 USDC,它就能依照實際用量付費取得搜尋結果。這種模式也讓「用多少、付多少」變得更精確,不必再為了避免超額而預先訂閱較高的方案。

🔗 **來源**
- 標題：Brave Search API now accepts agentic payments via the x402 protocol
- 連結：https://brave.com/blog/search-api-agentic-payments/

#Brave #x402 #AgenticAI #AIAgents #Web3 #USDC #PaymentProtocol #SearchAPI #Blockchain #DeveloperTools
