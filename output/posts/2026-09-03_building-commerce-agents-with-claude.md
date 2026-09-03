---
title: Building commerce agents with Claude
source: Claude Blog
url: https://claude.com/blog/claude-for-commerce-agents
model: claude-code/sonnet
generated_at: '2026-09-03T20:05:08.984456'
pinned: true
---

📌 【Anthropic 官方發布】Claude 推出商務 Agent 藍圖，購物車最高大 35%

TL;DR：Anthropic 釋出建構「商務 Agent」的完整藍圖與參考實作，讓企業幾天內就能上線購物與商家用 Agent。

當 Shopify、Priceline 這類平臺已經在用 Claude 打造能「用白話文找、比、買」的購物 Agent，多數工程團隊還在從零摸索該怎麼設計對話式商務體驗。Anthropic 這次直接把內部驗證過的架構、guardrail 與參考實作全部公開。

🤔 **問題：企業想做商務 Agent，卻沒有可依循的架構**

Anthropic 表示，包括零售、市集、電商平臺與旅遊公司在內的許多大型企業，都在用 Claude 建構 Agent，讓消費者能用自然語言搜尋想要的商品、找到它、比較它、買下它。2026 年 9 月 2 日，Anthropic 正式推出一份藍圖，協助工程團隊建構商務 Agent，內容涵蓋 harness、設計模式與 guardrail，讓團隊能在數天內讓商務 Agent 上線，並附上零售、旅遊、電信、票務等垂直領域的購物 Agent與商家 Agent 參考實作，同時提供 Claude Code plugin 作為起點。程式碼可部署在 Claude API、Amazon Bedrock、Microsoft Foundry 或 Google Cloud Vertex AI 上，Anthropic 也與 Accenture、Mastercard、Visa 等生態系夥伴合作，協助客戶與商家社群導入這套藍圖。

🧩 **購物 Agent：從對話直接搜尋、比較到結帳**

購物 Agent 內嵌在企業自己的 App 或網站中，藍圖包含商品目錄（catalog）、購物車、結帳、顧客偏好與訂單歷史的整合介接點，付款環節則交由企業自行串接既有結帳系統或代理式支付（agentic payments）服務商。文中舉例，顧客可以直接說「我需要帳篷、睡袋和爐具，準備跟兩個小孩去露營一個週末」，Agent 就能接手處理。具體能力包括：
- 搜尋商品目錄並組合出正確的商品組合，支援多品項需求。
- 記住顧客偏好並據此客製化推薦。
- 直接在對話中呈現商品、比較與購物車內容，而非只回傳文字。
- 建立購物車並交給結帳流程。
- 在同一段對話中回答客服問題，例如訂單在哪、如何退換貨、退款政策是什麼，不必把顧客導去另一個支援頁面。

Agent 內建 guardrail，設計上會把價格與商品資訊限制在實際目錄資料範圍內，並避免操縱性的加購（upsell）手法。在參考實作中，這些能力被拆分為 skills 與工具，涵蓋商品搜尋、多品項規劃、深度研究、個人化、客服，以及對話中的 UI 呈現。

📊 **商家 Agent：幫店家看數據、抓庫存風險、擬行銷方案**

商家 Agent 則服務店家經營者。例如使用者可以問「上一季的庫存該打幾折才能出清？」，並得到基於自家資料的回答。它能做的事包括：回答銷售表現相關問題（什麼賣得好、什麼賣不動）、追蹤庫存並主動示警（例如某商品在促銷開始前就快賣完）、根據店家自身銷售歷史推薦定價與促銷方案，以及草擬行銷活動內容。當 Agent 主動建議變動時，必須經過人員核准才會真正上線，確保使用者保有最終決定權，Agent 則扮演「看店」的角色。在參考實作中，這些能力對應到銷售分析、目錄與庫存管理、行銷與促銷，以及儀表板等後臺 UI 的 skills。

💡 **業界怎麼看：從支付網路到旅遊平臺的共同表態**

文中引用多方合作夥伴的說法：Visa 首席產品與策略長 Jack Forestell 提到與 Anthropic 合作，把 Claude 的智慧與 Visa 網路的信任、安全、全球觸及結合；Mastercard 全球數位商務化負責人 Sherri Haymond 強調在代理式（agentic）時代，信任是商務的貨幣；Accenture 全球消費品、零售與旅遊業務負責人 Kath Gramling 引述自家研究指出，85% 的消費者已願意與 AI Agent 合作，近三分之四的人甚至更信任個人 AI Agent 勝過自己最好的朋友來代為採購；Priceline AI 體驗副總裁 Cobus Kok 表示旗下 AI 助理 Penny 是用 Claude 打造的最新一代版本；Intuit 首席架構師 Chris Kasten 提到正結合前沿 AI 推理與自家專有資料打造財務智慧系統；Shopify 產品副總裁 Vanessa Lee 則提到正基於 Anthropic 的藍圖打造參考商店實作，透過 Catalog、UCP 與 Shop Sign-in 串接商家的商店。

📈 **零售商實測：購物車變大、成交率變高**

素材開頭即提到，在 Claude 上運行購物 Agent 的零售商，觀察到購物車金額最高成長 35%，顧客完成購買的機率最高提升 60%。素材並未說明這些數字來自多少家零售商或具體衡量方式，讀者可視為方向性參考。

🎯 **實務啟示**

如果你的團隊正打算做對話式購物或商家後臺 Agent，與其自行設計整套架構，不如先看 Anthropic 公開的參考實作，理解它怎麼切分購物 Agent 與商家 Agent 的職責、如何處理付款留白、guardrail 怎麼卡在目錄資料上，再決定哪些部分要客製化。

🔗 **來源**
- 標題：Building commerce agents with Claude
- 作者／機構：Anthropic
- 連結：https://claude.com/blog/claude-for-commerce-agents

#Anthropic #Claude #CommerceAgent #AIAgent #Ecommerce #ConversationalCommerce #AgenticAI #Shopify #RetailTech #LLM
