---
title: Build OpenClaw agents that transact with Amazon Bedrock AgentCore payments
source: AWS ML
url: https://aws.amazon.com/blogs/machine-learning/build-openclaw-agents-that-transact-with-amazon-bedrock-agentcore-payments/
model: claude-code/sonnet
generated_at: '2026-08-18T06:25:31.497527'
score: 105
---

📌 讓 AI Agent 自己付錢：OpenClaw 接上 Bedrock AgentCore 支付層

TL;DR：AWS 與 OpenClaw Foundation 合作，讓自主代理能在人類預先核准的額度內自動完成 HTTP 402 付費請求。

當一個自主代理在瀏覽網頁、呼叫 API 或查詢 MCP 伺服器的過程中，撞上一個要求先付款才能繼續的 HTTP 402 回應，通常代理只能停下來等人類處理。這篇文章示範了如何讓代理在「事先核准的額度內」自己把這筆錢付掉，而不需要每次都叫醒一個人。

🤔 **為什麼需要一個有界限的支付層**

長時間執行的研究或工作流代理，可能在沒有操作者在場時遇到需要付費的 API 或內容端點。許多按次計費的 API、內容服務、運算服務與 MCP 工具，單筆交易金額可能不到一美元甚至只有幾分錢，信用卡處理的最低手續費在這種規模下並不划算，穩定幣支付則能支援小額且近乎即時的清算，這也是 x402 這類 HTTP 原生協議適合用於代理發起支付的原因。AgentCore payments 是 Amazon Bedrock AgentCore 的一項能力，提供錢包整合、支出限額，以及一個能跟著 x402、Machine Payments Protocol（MPP）等代理支付協議演進的一致支付層。

🧩 **把「管理權」和「執行權」分開**

整個設計的核心原則，是把錢包供應商憑證，以及建立或擴大支付 session 的權限，放在模型看不到的地方；模型面向的執行環境（runtime）只能在既定額度內發起已核准的支付，無法建立、延長或替換 session。文章明確指出，這個設計並不阻止 prompt injection，而是假設不受信任的輸入有可能操縱模型，於是把 runtime 的權限用收款人、資產、網路、單筆金額、累積預算與到期時間這幾個維度直接限制死。

這次整合使用的是 OpenClaw，一個運行在使用者裝置上、透過本地 Gateway 連接模型、工具與訊息通道的 AI 助理，由 OpenClaw Foundation 維護，功能透過外掛擴充。AWS 與 OpenClaw 團隊合作開發的 aws-agents-pay 外掛，只對模型暴露兩個工具：get_payment_session_status（查詢目前設定的支付 session 狀態）與 get_paid_content（請求一個已核准的付費網址，並在既定政策內完成付款）。人類則在一個受信任的終端機裡，用管理權限完成錢包供應、建立支付 session、核准收款人、設定預算等操作，session 建立時還需要在互動式終端機輸入 approve 才會生效。

🧩 **底層基礎設施**

AgentCore Identity 負責儲存錢包供應商的憑證；AgentCore Observability 在設定好遙測傳輸後，能透過 Amazon CloudWatch 與 AWS X-Ray 提供日誌、指標與追蹤。支付連接目前支援 Coinbase 錢包或 Stripe Privy 錢包，兩者都是內嵌式穩定幣錢包，視供應商與地區可用性，可透過穩定幣或簽帳卡儲值法幣，兩者也都使用 AgentCore Identity 做憑證儲存與每個 session 的支出限額控管。

文章附上的示範中，一個名為「Bob」的 AI 助理在 OpenClaw gateway 應用裡回答「西雅圖現在天氣如何」，接著執行了一筆 0.001 USDC 的測試付款（在 Base Sepolia 測試網），用來支付一個付費天氣 API。目前 OpenClaw 在 Agent Toolkit for AWS 中的設定流程，以 Base Sepolia 作為測試範例、Base 作為正式環境，也支援自訂到 Ethereum 及其他 EVM 相容鏈與 Solana。

“Payments are a natural extension of what plugins already do in OpenClaw: give an agent a new capability through a well-defined tool, not a special case bolted on afterward.” —— Patrick Erichsen, Member of Technical Staff, OpenClaw Foundation

🎯 **實務啟示**

這套模式的價值不在於協議本身多新穎，而在於它把「代理可以自己花錢」這件事，用 IAM 角色分權（管理、管理面、代理執行、服務操作分開）與明確的支付政策做成了可落地的工程模式。對於已經在用 OpenClaw 或評估 Bedrock AgentCore 的團隊，這是一個可以直接照著 AgentCore payments IAM 角色指南去複製的起點，尤其適合需要串接大量小額付費 API 或 MCP 工具的長時間執行代理。

🔗 **來源**
- 標題：Build OpenClaw agents that transact with Amazon Bedrock AgentCore payments
- 作者／機構：Daniel Wirjo, AWS
- 連結：https://aws.amazon.com/blogs/machine-learning/build-openclaw-agents-that-transact-with-amazon-bedrock-agentcore-payments/

#AWS #BedrockAgentCore #OpenClaw #AIAgents #x402 #AgenticPayments #MCP #StablecoinPayments #AgentTooling #CloudAI
