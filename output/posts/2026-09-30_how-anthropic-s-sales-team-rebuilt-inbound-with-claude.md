---
title: How Anthropic's sales team rebuilt inbound with Claude Managed Agents
source: Claude Blog
url: https://claude.com/blog/how-anthropics-sales-team-rebuilt-inbound-with-claude-managed-agents
model: claude-code/sonnet
generated_at: '2026-09-30T21:32:20.883030'
pinned: true
---

📌 Anthropic 業務團隊怎麼用 Claude Agent 重建詢價流程

TL;DR：Anthropic 用 Claude Managed Agents 打造購買代理人，讓多數詢價客戶不再苦等業務回覆。

潛在客戶填完表單後,要等好幾天才有人聯繫,等待流失的不只是耐心,還有成交的時機。Anthropic 自家業務團隊就曾親身面對這個問題,而他們選擇的解法,是把第一線的問答交給 Claude。

🤔 舊流程為什麼撐不住

原本的詢價流程很單純：客戶填表單，交給業務開發代表（BDR）初步篩選，再轉給客戶經理（AE）跟進。這套流程在詢價量不大時運作良好，但 Anthropic 每個月收到的詢價高達數萬筆，內部 BDR 團隊根本無法一一消化。結果是業務代表每天花大量時間回答文件裡早就寫清楚的問題（方案價格、是否有席次下限、能否符合 HIPAA 合約要求），卻沒有足夠餘力覆蓋整個詢價佇列。

🧩 一個能走到結帳流程的「購買代理人」

Anthropic 用 Claude Managed Agents（beta）打造了一個 buying agent，部署在 Contact Sales 與 Pricing 頁面、產品內部，以及 email 往來中。客戶描述自身團隊需求後，代理人會追問幾個問題，接著回答方案、安全性與資料相關疑問，最後推薦合適的方案與席次數。每段對話最終會走向三種結果之一：直接導向結帳、附上完整對話紀錄轉交業務代表跟進、或單純提供一個快速解答就結束。整個體驗刻意設計成「選擇加入（opt-in）」，客戶可以一開始就選擇要和代理人對話還是找業務代表。

🧩 為什麼選擇 Claude Managed Agents

團隊指出，這個代理人的底層架構其實很簡單：一段提示詞、幾個工具，加上跑在 Claude Managed Agents 上的 Claude 模型。因為平臺已經處理好了 hosting、session 管理與工具編排，工程團隊得以把心力放在設計購買體驗，而不是搭建底層基礎設施。文中提到的幾個關鍵優勢包括：一位工程師在短短幾週內就完成初版代理人；技術與非技術人員都能直接在 Console 中審閱、編修 system prompt，且改動會先上到 staging agent 測試再上線；每次改動都會保留成獨立版本，內部測試約一週後就迭代到第七版；平臺支援排程執行（scheduled runs），為未來擴展其他客戶互動場景留下空間。

📊 轉換率翻倍，成交也更快

代理人目前每天處理數千則對話，全天候運作。被代理人轉交給業務代表的客戶，轉換為商機的機率是舊表單留下的名單的兩倍以上，成交速度也快了大約五天。團隊也提到，需要真人介入才能完成的對話比例，較先前下降了大約一半。

💡 幾個值得借鏡的建構心得

團隊分享了幾項實作經驗：給 Claude 一個目標，而不是一長串規則，效果反而更好，例如單純說「你的目標是理解客戶需求、篩選潛在客戶、推薦最適合的方案」就比列出所有判斷條件的流程圖更有效；提示詞並非越長越好，「少即是多」在實測中勝出；讓業務等領域專家（SME）持續參與開發迭代，能大幅提升代理人的真實可用性；即使代理人常把小型團隊導向較便宜的 Team 方案而非 Enterprise，團隊也視此為優點,因為讓客戶買到「對的」方案,比一味往上升級更能留住客戶;每一次代理人把客戶轉交給真人時附上的原因，都被團隊當作產品改進的回饋訊號。

⚠️ 限制

這個體驗被刻意設計為 opt-in，代表並非所有客戶都會與代理人互動；面對更大型或複雜的交易，代理人仍會選擇轉交真人業務處理。此外，文中對於對話量、轉換率等數據多以倍數與大致比例呈現，並未公布具體原始數字。

🎯 實務啟示

對正在打磨銷售或客服類 AI 代理人的團隊來說，這個案例提供了一個可複製的思路：選用 managed agent 平臺能大幅降低基礎設施投入，讓團隊把精力集中在提示詞設計、工具選擇與領域知識庫上；而把每一次「代理人轉交真人」的原因當成產品回饋來源，是一個值得直接搬過去用的設計模式。

🔗 來源
- 標題：How Anthropic's sales team rebuilt inbound with Claude Managed Agents
- 作者／機構：Carl Johnson, Anthropic
- 連結：https://claude.com/blog/how-anthropics-sales-team-rebuilt-inbound-with-claude-managed-agents

#Anthropic #Claude #ClaudeManagedAgents #AIAgents #SalesAutomation #EnterpriseAI #ConversationalAI #B2B #AIforSales #ProductivityAI
