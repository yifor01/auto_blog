---
title: The RealReal won’t let AI agents hog designer clothing
source: The Verge AI
url: https://www.theverge.com/news/1018713/meta-muse-agentic-shopping-ai-the-realreal
model: claude-code/sonnet
generated_at: '2026-10-26T21:58:22.747682'
score: 68
---

📌 AI Agent 不停刷購物車,RealReal 被迫升級防禦機制

TL;DR：Meta Muse 可被指示反覆佔用商品保留時段,平臺緊急封堵代理購物。

一個 AI agent 不會累,也不會不耐煩。如果你叫它「每 20 分鐘幫我重新搶一次這件外套」,它會毫無怨言地重複做到你喊停為止——而這正是 The Verge 之前揪出的漏洞。

🤔 **一個保留機制,被 agent 玩出漏洞**

二手精品電商 The RealReal 的購物車設計是：商品一旦被加進購物車,就會進入「保留中」狀態,20 分鐘內其他顧客無法購買。The Verge 先前報導指出,使用 Meta 的 Muse agent,可以指示它在每次 20 分鐘保留到期的瞬間重新把商品加回購物車,等於無限延長保留,讓其他真人顧客數小時甚至更久都買不到該商品。

🧩 **RealReal 的回應：卡住所有 agent 的登入與結帳**

報導發布後,The RealReal 技術長 Luke Friang 回覆表示,公司已針對 Muse 這個使用案例進行修補,更新了機器人防禦（bot defense）設定,讓所有 agent 要登入、加入購物車、結帳都變得困難許多。但他也說,agent 仍可以繼續顯示商品清單,並把 Muse 使用者導向商品頁面——換句話說,封鎖的是「下單動作」,不是「瀏覽推薦」。Friang 表示公司會隨著 AI 購物演化持續強化防護。

📊 **購物是 Muse 目前最大的使用場景**

根據報導引用 Meta 第三季財報電話會議的說法,購物是 Muse 目前最常見的使用情境,平均購買金額超過 200 美元;Meta 也提到美國地區 40 天內有 1000 萬人下載這款 App。

💡 **當 agent 不受人類耐心限制,平臺的假設就會崩潰**

一般顧客不會無限次把同一件衣服加進又移出購物車,人的耐性是天然的節流閥。但 agent 沒有這個限制,原本設計給真人使用習慣的保留機制,碰上「不會累的代理人」就變成可被無限利用的漏洞。這也呼應了 Amazon 等零售商直接封鎖 agent 購物的理由：一旦顧客不再直接造訪網站,而是透過聊天機器人中介,廣告收入與顧客關係都會被稀釋。

🎯 **實務啟示**

對建置購物或自動化 agent 的工程師而言,這是一個提醒：目標系統原本的業務邏輯（如保留時段、庫存鎖定)往往是針對人類行為假設設計的,agent 的高頻重複行為可能觸發意料外的濫用情境,應該主動加上節流與使用倫理的考量。對平臺方工程師而言,bot defense 需要從「擋爬蟲」擴展到「擋高頻但看起來合法的 agent 行為」。

🔗 **來源**
- 標題：The RealReal won't let AI agents hog designer clothing
- 作者／機構：Mia Sato, The Verge
- 連結：https://www.theverge.com/news/1018713/meta-muse-agentic-shopping-ai-the-realreal

#AIAgent #MetaMuse #AgenticShopping #Ecommerce #BotDefense #TheRealReal #AIBusiness #OnlineShopping #AIsafety #TechPolicy
