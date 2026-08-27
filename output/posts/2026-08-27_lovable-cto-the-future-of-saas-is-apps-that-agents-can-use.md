---
title: 'Lovable CTO: The Future of SaaS Is Apps That Agents Can Use'
source: Latent Space
url: https://www.latent.space/p/lovable-future-of-saas
model: claude-code/sonnet
generated_at: '2026-08-27T17:28:20.763587'
score: 91
---

📌 Lovable CTO：SaaS 的下一步，是能被 Agent 直接呼叫的「能力」

TL;DR：Lovable 把應用程式拆解成 agent 可透過 MCP 直接呼叫的 capability，讓人機兩種介面共存一個應用。

如果你打造的應用程式，未來越來越少人類會親自打開它，那還算是一個「App」嗎？Lovable 給出的答案是：它會變成一組「能力」（capability），由公司的 AI 大腦統一呼叫。

🤔 **從原型工具到「一個入口做完所有事」**

Lovable 在近期部落格文章中提出「為團隊打造數位大腦、串接你日常工具」的願景。Lovable CTO Fabian Hedin 在 Latent Space 專訪中說：「你可以走到這樣的境界——用一個入口就能完成你所有的工作。」Lovable 仍然是拿來建構應用程式的工具,但接下來會讓使用者建構 Hedin 所謂的「capability」：應用程式中一個 agent 可以直接呼叫的有用功能,不需要人類先打開該應用程式。

具體做法是把已發布的應用程式,透過一個託管的 MCP 伺服器,將特定功能開放為工具,讓同一個應用同時擁有傳統人類 UI 與 agent 介面,可以從 ChatGPT、Claude 等相容 MCP 的 AI 客戶端直接呼叫。

🧩 **三年內從原型工具長成「軟體公司的操作系統」**

Lovable 前身是 2023 年推出的開源程式碼工具 GPT Engineer，最初鎖定原型製作。2024 年 11 月轉為商業產品，隔月改名 Lovable。Hedin 說，團隊注意到使用者不只在平臺上做原型或 MVP（最小可行產品），而是打造真正服務客戶的產品；接著又出現使用者建構內部軟體，例如 CRM、後臺管理面板、客服系統，用來支撐對外產品或作為企業內部工具。

這樣的快速產品演進伴隨強勁的成長：據主要投資方 Menlo Ventures 合夥人 Deedy Das 的推文，Lovable 年化營收已突破 5 億美元，累積建立超過 6000 萬個專案，Lovable 打造的應用每月訪問量超過 9 億次，近三分之二的財星 500 大企業員工使用過此平臺。本月 Menlo Ventures 領投 Lovable 4 億美元 C 輪融資（EQT 管理的 Scaleup Europe Fund 也參與），估值達 133 億美元。

💡 **「別叫它 agent」：連接情境與能力,而非派一個員工做事**

Hedin 對「agent」這個詞相當謹慎：「它會讓人聯想到像員工一樣執行任務,那是一種容易理解的想像方式,但底層真正在做的,其實是連接對的情境（context）與能力。」他舉例,Lovable 內部打造了一個工具,協助支援團隊核發使用者點數、管理平臺,這些能力現在都已經整合進 Lovable 的內部 agent,而且能非同步運作——排程稍後檢查部署狀態或監控例行流程,再把結果回報到同一個對話串。

Hedin 也承認 Vercel（其內部 agent 稱為 @𝚟）等公司正朝相同方向前進,但他認為 Lovable 的切入點是「成為打造 agent 所需能力的最佳場所」，「協調這些能力是簡單的部分,確保它們串接良好、建構正確、可靠運作,才是困難的部分。」

⚠️ **最大的挑戰是安全性**

如果員工用 Lovable 打造一個連接公司 Slack 的應用，必須確保不會不小心把個人訊息或機密資訊暴露給公司大腦。Lovable 用「connector」處理外部系統連接，其中一種「app user connector」會保留每個使用者的身分與來源系統權限，憑證以加密形式儲存在伺服器端、由 Lovable 的連接閘道處理，而不會暴露給產生出來的應用程式本身——應用程式拿到的是綁定該使用者的短效金鑰。Hedin 的說法是：「我們把連接外部系統的部分,和被撰寫出來的應用程式程式碼分開。應用程式只與 Lovable 平臺介接,但應用程式本身永遠拿不到那些憑證。」

🎯 **實務啟示**

如果你的團隊正在評估要不要把內部工具「agent 化」，Lovable 的路徑提供一個參考模型：先把功能拆成可獨立呼叫的能力單元、用 MCP 之類的協定曝露出來，再單獨處理權限與憑證隔離，而不是讓每個應用各自兜一套呼叫外部系統的邏輯。

🔗 **來源**
- 標題：Lovable CTO: The Future of SaaS Is Apps That Agents Can Use
- 作者／機構：Latent Space
- 連結：https://www.latent.space/p/lovable-future-of-saas

#Lovable #AIAgents #MCP #SaaS #AppBuilder #NoCode #AgenticAI #StartupFunding #DeveloperTools #ProductStrategy
