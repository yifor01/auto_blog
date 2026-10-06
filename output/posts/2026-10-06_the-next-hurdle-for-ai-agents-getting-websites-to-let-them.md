---
title: 'The next hurdle for AI agents: getting websites to let them in'
source: TechCrunch AI
url: https://techcrunch.com/2026/10/06/the-next-hurdle-for-ai-agents-getting-websites-to-let-them-in/
model: claude-code/sonnet
generated_at: '2026-10-06T22:05:57.182770'
score: 72
---

📌 AI 代理人想幫你買東西，網站卻把門關上了

TL;DR：Meta Muse、ChatGPT Dots 等個人 AI 代理人正大量被電商、航空網站攔截，問題出在人機驗證機制還沒跟上 agent 時代。

你讓 AI 代理人幫你訂機票、買菜、訂餐廳位子，結果它卡在一個「請點擊確認你是人類」的按鈕前，任務失敗。這不是單一網站的個案，而是這波消費級 AI 代理人正在全面撞上的牆。

🤔 **從回答問題到代為行動，門檻變了**

Meta 的 Muse、Instinct，以及 ChatGPT 的 Dots，代表新一代消費 AI：它們不只是聊天，而是真的能訂機票、訂餐廳、下單買菜。使用者不需要懂技術、不用自己架設 agent，但代理人要完成任務，得先「進得了」對方的網站。

🧩 **攔截有兩種：故意的，和不小心的**

TechCrunch 報導指出，Amazon 已明確封鎖 Meta Muse 存取其商品目錄與購物流程。但更多案例其實是誤傷：Walmart 雖與 Muse 有正式合作，使用者仍反覆回報購買失敗，官方解釋問題出在「請驗證你是人類」的按鈕，一旦代理人操作流程被中斷，驗證就會失敗，代理人隨之被踢出。社群媒體上還有 Yelp、eBay、Zillow、Pizza Hut、Adidas 以及多家航空公司被提及有類似攔截情況，甚至有人反映 eBay 因使用 agentic AI 而被停權。Delta 向 TechCrunch 表示目前並未與第三方 AI 代理人有訂票整合，若要開放必須同時考量安全與顧客體驗；United 則引用其使用條款，禁止未經書面許可的自動化存取。Yelp 更明確表示：非人類流量若未透過其資料授權方案付費合作，一律不允許。

💡 **問題根源：反機器人機制沒有區分「好代理人」與「壞機器人」**

報導指出，Cloudflare 等 CDN 業者在 9 月 15 日調整了爬蟲預設設定，允許網站封鎖 AI 訓練用途的爬取，但原本為安全理由設定封鎖機器人的網站，連帶也擋掉了廣告頁面上的 AI 代理人流量。Cloudflare 對此表示沒有具體資料可說明是否與 Muse 等代理人攔截有關，並指向其 Radar 公開資料平臺，但該資料無法區分善意與惡意流量。為解決這個問題，Meta、Walmart、Stripe、Sierra、Genesys、Rocket、NiCE、Decagon 等業者已開始合作制定一套開放標準，專注於電商場景下代理人與企業系統之間的通訊協定，目的是分辨「代表使用者行動的好機器人」與「惡意機器人」。

⚠️ **使用者根本不知道是誰在擋**

這次報導最值得注意的一點是「混亂」本身：使用者分不清是網站故意封鎖，還是傳統反垃圾機制誤判，結果既怪罪零售商，也怪罪代理人服務商。Meta 目前的作法是與特定品牌建立正式合作（如 Walmart），並在 Muse App 內維護一份不斷擴充的「連接器」清單，確保已知合作夥伴的存取是被允許的；但許多新公布的合作夥伴尚未出現在清單中，顯示這套名單仍在整理擴充階段。

🎯 **實務啟示**

對開發 agentic 商務應用的工程師來說，這是一個清楚的訊號：純粹依賴爬蟲式自動化去模擬人類操作網站，長期注定與反機器人系統對撞。真正可規模化的路徑是走向正式的 agent-to-agent 協定與 API 層合作，而不是讓代理人偽裝成瀏覽器使用者去點擊驗證按鈕。評估導入 AI 購物代理人前，務必先確認目標網站是否有正式合作或 API 支援，否則踩到反機器人機制只是遲早的事。

🔗 **來源**
- 標題：The next hurdle for AI agents: getting websites to let them in
- 作者／機構：Sarah Perez, TechCrunch AI
- 連結：https://techcrunch.com/2026/10/06/the-next-hurdle-for-ai-agents-getting-websites-to-let-them-in/

#AIAgents #AgenticAI #Ecommerce #WebSecurity #BotDetection #MCP #Cloudflare #Meta #ConsumerAI #TechPolicy
