---
title: Shopify opens checkout to browser-based AI agents
source: TechCrunch AI
url: https://techcrunch.com/2026/09/28/shopify-opens-checkout-to-browser-based-ai-agents/
model: claude-code/sonnet
generated_at: '2026-09-28T22:44:54.541463'
score: 88
---

📌 Shopify 讓 AI Agent 直接刷卡結帳，Amazon 和 Adidas 卻反其道而行

TL;DR：Shopify 開放瀏覽器端 AI Agent 透過 WebMCP 完成結帳（含 Shop Pay），跟同業封鎖 Agent 購物的路線正好相反。

當 Amazon 和 Adidas 選擇把 AI Agent 擋在購物流程之外時，Shopify 週一宣布了完全相反的方向：讓瀏覽器端的 AI Agent 可以直接在商家網站上完成整筆交易，而不只是逛逛商品、加進購物車。

🤔 **從「幫你逛街」到「幫你結帳」**

Shopify 先前已經替 storefront 與購物車支援了 WebMCP，讓瀏覽器端的 Agent 能夠瀏覽商家庫存、搜尋商品、把商品加入購物車。這次更新把能力延伸到結帳環節（包含 Shop Pay）：Agent 現在可以讀取結帳畫面、更新結帳內容,並在買家授權後直接送出交易——而且不再依賴螢幕截圖或網頁爬蟲。

🧩 **三個新工具，把結帳變成結構化 API**

這次更新新增了三個工具：`get_checkout`（檢視結帳內容）、`update_checkout`（修改如收件地址、配送方式等資訊）、`complete_checkout`（在買家授權後送出訂單）。負責 Shopify agentic commerce 產品的 staff product manager Gil Greenberg 在 X 上表示，這項功能正逐步開放給所有符合資格的 Shopify 商家。他也建議開發者：「如果你的 Agent 是在買家的瀏覽器中運作，就該使用 storefront 與結帳環節提供的 WebMCP 工具來完成下單，而不是去解析為人類設計的 HTML。」他強調這些 WebMCP 工具是透過 UCP（Universal Commerce Protocol）刻意設計的結構化、高效率 API，用來確保商業事實的準確性、必要的揭露資訊與交接流程。

💡 **兩條協定，服務兩種 Agent**

Shopify 目前同時提供兩條技術路徑：原本就有的 hosted MCP 伺服器，服務 server-to-server 運作的 Agent；以及這次擴展的 WebMCP（一項提案中的標準），服務直接在買家瀏覽器內運作的 Agent。兩者底層都建立在 Shopify 的 Universal Commerce Protocol（UCP）之上,提供統一的方式來搜尋與探索商品、建立購物車、完成結帳。文章也提到，Muse 與 Instinct 這兩個知名 AI Agent 已經與 Shopify 建立直接的 agentic commerce 合作關係，其中與 Instinct 的合作正是在同一天宣布。

🎯 **實務啟示**

如果你正在開發或整合瀏覽器端購物 Agent，這次更新代表你不再需要靠截圖辨識或 DOM 爬蟲去猜測結帳頁面的結構，而是可以直接呼叫 `get_checkout`／`update_checkout`／`complete_checkout` 這類結構化 API 完成流程,這對降低 Agent 購物流程的錯誤率、提升相容性會有直接幫助。但同時也要留意，不同平臺在「是否歡迎 Agent 自動結帳」這件事上立場並不一致（Shopify 開放,Amazon、Adidas 封鎖），構建跨平臺的購物 Agent 時,協定相容性與商家政策都需要分別處理。

🔗 **來源**
- 標題：Shopify opens checkout to browser-based AI agents
- 作者／機構：Sarah Perez @ TechCrunch
- 連結：https://techcrunch.com/2026/09/28/shopify-opens-checkout-to-browser-based-ai-agents/

#Shopify #WebMCP #AgenticCommerce #MCP #AIAgents #Ecommerce #ShopPay #UCP #ConversationalCommerce #TechNews
