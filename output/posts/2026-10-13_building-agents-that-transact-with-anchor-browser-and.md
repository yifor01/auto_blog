---
title: Building agents that transact with Anchor Browser and AgentCore payments
source: AWS ML
url: https://aws.amazon.com/blogs/machine-learning/building-agents-that-transact-with-anchor-browser-and-agentcore-payments/
model: claude-code/sonnet
generated_at: '2026-10-13T22:04:10.835402'
score: 94
---

📌 AI代理自動付費瀏覽：AWS用x402解開402卡關

TL;DR：AWS讓Anchor Browser代理透過AgentCore payments自動完成x402付費請求，無需人工介入也不碰觸私鑰。

當AI agent嘗試存取按次計價的研究API或付費內容，伺服器回的不是資料，而是一個HTTP 402 Payment Required。沒有錢包、沒有預算、沒有付款邏輯的agent，任務就這樣卡住，等人來處理。

🤔 **402卡關背後，是整套自建支付堆疊的工程負擔**

x402是一種開放標準，讓伺服器透過402狀態碼回傳金額、可接受的付款方式與收款地址，由請求方完成交易。問題是，目前開發者必須自己把整套支付堆疊塞進agent裡：錢包、私鑰、預算控制、簽署付款證明、附加付款標頭、重試邏輯、結算、記錄,每一項都要自己寫、自己保護、自己維護。

這不只是工程量問題，還牽涉三個安全風險：一是失控支出,沒有在基礎設施層強制預算上限，一個bug、重試迴圈或prompt injection就可能觸發連續扣款；二是私鑰外洩,私鑰若留在agent執行環境裡，就和不受信任的網頁、第三方工具共享同一執行空間；三是簽署流程暴露,若簽署基礎設施可從執行環境直接存取，攻擊者可能嘗試竊取金鑰或將付款導向未授權地址。對瀏覽器型agent來說，還有一個額外限制：付款必須發生在同一個瀏覽器session內，否則session recording和live view會和實際執行的流程不一致。

🧩 **把敏感操作搬出agent，留在Anchor Browser裡的只剩兩個元件**

Anchor Browser是專為AI agent打造的雲端瀏覽器自動化方案,每個agent session跑在受管理的瀏覽器環境裡,維持登入狀態、處理導航、擷取網路請求，並提供即時的頁面互動畫面。Amazon Bedrock AgentCore payments則是AgentCore裡的全託管支付能力，讓AI agent能自主探索、存取並付費使用API、MCP伺服器與網頁內容。

這個整合的核心是Payment Manager,建立時指定authorizer類型與IAM角色，AgentCore會配置對應的workload identity於Amazon Bedrock AgentCore Identity。錢包金鑰與私鑰留在AgentCore payments與設定好的錢包供應商（如Coinbase CDP或Stripe Privy）手上，從不進入agent執行環境。端點探索則透過Amazon Bedrock AgentCore Gateway串接Coinbase x402 Bazaar MCP伺服器，讓agent能用程式化方式找到可用的付費x402端點。

結果是，Anchor Agent端只保留兩個跟付款相關的元件：一個budget session，一個x402工具。認證、錢包密鑰、付款上限、觀測性與付款證明簽署，全部移到AgentCore payments這個受管理層。

開發者只需要做一件事：把session的`session.x402`屬性設為`true`（預設為`false`）。啟用後，瀏覽器session就能在同一個session內自動存取x402保護的網站，付款由AgentCore payments簽署並重試，自動化程式碼完全不需要寫入錢包金鑰或付款標頭,透過Chrome DevTools Protocol連線後，agent就像平常一樣導航即可。

🎯 **對工程師的意義：少一套支付堆疊要維護，但多一個真實金流的開關**

這套整合最直接的價值，是把付款的安全邊界從agent runtime移到受管理的基礎設施層,開發者不用再自己處理私鑰保管、重試邏輯和觀測性。但也要記住，啟用`session.x402`等同授權瀏覽器用設定好的付款工具做真實扣款，預算上限與監控（AgentCore透過CloudWatch提供付款嘗試、核准、拒絕與結算的可視性）就是唯一的防線，上線前務必設定好。

🔗 **來源**
- 標題：Building agents that transact with Anchor Browser and AgentCore payments
- 作者／機構：Cher Simon, AWS
- 連結：https://aws.amazon.com/blogs/machine-learning/building-agents-that-transact-with-anchor-browser-and-agentcore-payments/

#AWS #AIAgents #AgentCore #x402Protocol #AnchorBrowser #MachineToMachinePayments #AutonomousAgents #CloudSecurity #APIEconomy #AgenticAI
