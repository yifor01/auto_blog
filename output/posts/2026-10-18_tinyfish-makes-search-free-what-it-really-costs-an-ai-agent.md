---
title: 'TinyFish Makes Search Free: What It Really Costs an AI Agent to Read the Web'
source: MarkTechPost
url: https://www.marktechpost.com/2026/10/18/tinyfish-free-search-ai-agent-token-cost/
model: claude-code/sonnet
generated_at: '2026-10-18T19:36:34.196876'
score: 69
---

📌 代理讀一頁網頁，可能吃掉三分之一上下文窗口

TL;DR：AI 代理查資料的隱藏成本不是搜尋 API 費用，而是抓回來的內容塞進模型上下文後要付的 token 費。

團隊編預算時盯著模型推論費率，卻常常忘了一件事：代理每抓一頁網頁，那些文字最終都要變成輸入 token，由模型買單。

🤔 **搜尋代理的兩筆帳，你可能只算了一筆**

根據 MarkTechPost 報導，AI agent 讀取網頁會產生兩種成本：一是檢索費，即搜尋或抓取 API 按請求計費的部分；二是模型處理費，也就是抓回的網頁內容進入模型上下文後，以輸入 token 計費，再加上推理與輸出 token 的費用。網路基礎設施公司 TinyFish 的論點是，企業普遍低估了「抓回的內容量」對模型成本的拉動效果。報導也提到一個背景：隨著企業把任務路由到最便宜且能勝任的模型（Stripe 收購橫跨逾 400 個模型、80 多家供應商的 OpenRouter 即是一例），路由確實能壓低單位 token 價格，但不會改變一頁網頁本身含有多少 token。

🧩 **一頁新聞，各家抓出的字數差了 36 倍**

TinyFish 在 2026 年 6 月 2 日針對 45 個 URL、5 家供應商做了一次抓取品質評測。以一篇正文約 4,300 字元的 Daily Mail 文章為例，Firecrawl 回傳的字元數約為 TinyFish 的 36 倍（Parallel 僅回傳摘錄而非全文，兩者因此不直接可比）。報導特別強調，這只是單一頁面的案例，不能直接推廣到所有網站。

📊 **覆蓋率與訊號比：TinyFish 93%、Tavily 80%、Exa 73%**

在同一份內部評測中，只有字元數達 1,000 以上且判定訊號比超過 30% 才算「覆蓋」成功，結果為 TinyFish 93%、Tavily 80%、Exa 73%、Firecrawl 62%、Parallel 58%；在可用結果中，中位訊號比 TinyFish 為 90.5%、Exa 為 89.7%。報導提醒，這是 TinyFish 自行對自己做的測試，樣本僅 45 個 URL，且新聞類頁面是拉大差距的主因。

若假設所有抓取字元原封不動塞入上下文、不做過濾或摘要，一頁約 42,774 token 的內容，就會吃掉 128K 上下文窗口的三分之一；連抓三頁、約 128,322 token，幾乎不留空間給系統指令、對話歷史或代理自己的回應。報導也引用 Artificial Analysis 的觀察：代理每一輪都會重新送出完整對話，較早的輸入會以快取價計費，快取能降低重讀成本，但不會讓那頁內容從上下文裡消失。

在 Artificial Analysis 固定答案模型（GPT-5.6 Luna, medium）、只換搜尋供應商的測試中（2026 年 9 月 28 日快照，涵蓋 13 家供應商、26 款產品的 12 組設定），模型成本區間為每 1,000 個任務 8.04 美元至 21.65 美元。TinyFish 的搜尋與抓取在published 限制內免費（搜尋每分鐘 30 次、每小時 500 次；抓取每分鐘 150 個 URL、每日 1,000 個，即使帳戶餘額為 0 美元也能用），加上模型費 9.30 美元，是榜上最低的總成本。代價是 TinyFish 的 Search Index 分數僅 71（榜上最低）、DeepSearchQA F1 為 67，每個任務耗時約 59 秒（此時間結合估算的模型處理時間與實測搜尋時間，並非單純 API 延遲）。報導也提醒，Artificial Analysis 用的是自家統一抽取層，這些分數並不直接等同於對 TinyFish Fetch 本身的測量，每 1,000 個任務的榜單成本也不該與每 1,000 次請求的 API 報價混為一談。

⚠️ **這是一篇贊助內容，數字來自單一供應商的自測**

文末明確標示本文由 TinyFish 贊助，覆蓋率與訊號比數據出自 TinyFish 自行執行的內部評測，樣本量有限（45 個 URL）；Artificial Analysis 的榜單數據則是第三方基準，但同樣有方法論上的限制（統一抽取層、固定答案模型）。讀者在引用這些數字時，應留意其行銷語境與測試樣本規模。

🎯 **實務啟示**

在估算代理讀網頁的真實成本時，別只看搜尋 API 的請求費率，要連同抓回內容會佔用多少輸入 token、以及多輪對話重複傳送上下文的疊加效應一起算進去。如果你的代理管線會大量抓取新聞類長文，抓取工具回傳內容的「訊號密度」而非單純「免費額度」，可能才是真正決定總成本的變數。

🔗 **來源**
- 標題：TinyFish Makes Search Free: What It Really Costs an AI Agent to Read the Web
- 作者／機構：Asif Razzaq @ MarkTechPost
- 連結：https://www.marktechpost.com/2026/10/18/tinyfish-free-search-ai-agent-token-cost/

#AIAgents #TokenCost #WebScraping #LLMOps #SearchAPI #ContextWindow #AgentInfrastructure #TinyFish #LLMCost #AIEngineering
