---
title: 'Pay-per-inference for AI agents: How BlockRun and Incarna use Amazon Bedrock
  AgentCore payments'
source: AWS ML
url: https://aws.amazon.com/blogs/machine-learning/pay-per-inference-for-ai-agents-how-blockrun-and-incarna-use-amazon-bedrock-agentcore-payments/
model: claude-code/sonnet
generated_at: '2026-10-08T22:26:01.940864'
score: 84
---

📌 AI 代理的微支付難題：AgentCore Payments 如何讓 Agent 自己付推論費

TL;DR：AWS Bedrock AgentCore Payments 讓 AI agent 透過 x402 自動付費買推論，花費上限由平臺強制執行。

一個 AI agent 跑一次任務，可能要在迴圈裡連續買上百次東西：一次模型推論、一次 API 回應、一次網頁內容，每一筆可能只值零點幾美分，而且沒有人會在旁邊逐筆按「確認付款」。這篇 AWS 機器學習部落格的案例研究，講的就是這個問題怎麼被解決的。

🤔 **信用卡網路，從來不是為這種交易設計的**

文章指出，為 agent 的高頻、低金額支付自建一套金流，等於要同時解決好幾個難題：錢放在哪裡、每筆付款怎麼簽署、如何支援像 x402 這種剛出現的支付協定，以及怎麼防止一個自主運作的 agent 失控超支。Amazon Bedrock AgentCore payments 把這些問題收進一個受管服務裡，讓開發者只需要寫幾行程式碼就能幫 agent 加上付款能力。

🧩 **BlockRun 賣推論，AgentCore Payments 管錢**

案例主角 Incarna 用 AgentCore payments，讓自己的 agent 向 BlockRun 逐次付費購買模型推論。BlockRun 是一個走 x402 協定的按量付費推論路由器，整合超過 15 家供應商、90 多個模型，每次呼叫都是各自獨立報價、授權與結算。整體架構是：AgentCore 負責執行 agent，BlockRun 提供計量推論服務，AgentCore payments 則負責連接客戶的錢包、強制執行花費上限，並代表 agent 的 Incarna 身分簽署每一筆交易。

設定流程大致是：先把 Coinbase CDP 或 Stripe Privy 的憑證存成 payment credential provider，憑證會保存在 AWS Secrets Manager 而不是程式碼裡；接著建立 Payment Manager 與連接器，並設定預設花費上限；再建立 payment instrument，也就是 agent 實際付款用的嵌入式錢包，終端使用者透過導向網址為錢包注資並授權簽署，測試階段可以用 testnet USDC。AgentCore payments 支援兩種 x402 付款機制：價格已知時用 exact，資源為動態定價時用 upto，讓 agent 先授權一個上限金額，供應商最後按實際用量在上限內結算。

💡 **花費上限寫在基礎設施層，agent 的程式碼改不動它**

文章特別強調 payment session 的設計：一個 session 會設定一個花費上限，由 AgentCore payments 在基礎設施層強制執行，agent 自己的程式碼或 prompt 都無法更改這個上限，每個 session 也有到期時間。Incarna 把 session 的額度設定為一天的預算，即使 agent 的邏輯出了問題，花費也不會超過客戶設定的上限。

📊 **三天完成原本預估兩到三個月的整合**

Incarna 團隊完成完整的 AgentCore payments 整合只花了三天：一天開發、兩天測試，寫了大約 200 行應用程式碼，相較於原本預估的兩到三個月大幅縮短。在 beta 階段，agent 累計處理超過 1,000 筆付款，單筆金額從 0.001 美元到 0.05 美元不等，每一筆都在 Base 鏈上以 USDC 獨立結算。Incarna 創辦人 Justin Zhou 表示：「AgentCore payments 涵蓋了 agent 透過 x402 付款所需要的一切：客戶自己擁有的錢包、資金與撤銷流程、平臺強制執行的花費上限,以及能處理兩種 x402 版本的簽署機制,我們一行都沒有自己寫。」

⚠️ **目前仍是 beta 案例，規模化細節有限**

素材只提供了 Incarna 這一個案例在 beta 階段的數據，並未說明更大規模部署下的延展性、安全審計或多 agent 併發情境下的表現，這些都是讀者評估是否導入前需要自行驗證的部分。

🎯 **實務啟示**

對正在打造需要自主購買服務的 agent 系統的工程師來說，這個案例示範了一個值得參考的分工模式：把錢包託管、交易簽署與花費上限強制執行，交給受管的基礎設施層去做，而不是自己從零實作一套金流與風控機制，可以把原本數月的整合工作壓縮到幾天內完成。

🔗 **來源**
- 標題：Pay-per-inference for AI agents: How BlockRun and Incarna use Amazon Bedrock AgentCore payments
- 作者／機構：Peter Jiang（AWS）
- 連結：https://aws.amazon.com/blogs/machine-learning/pay-per-inference-for-ai-agents-how-blockrun-and-incarna-use-amazon-bedrock-agentcore-payments/

#AWS #BedrockAgentCore #AIAgents #x402 #MicroPayments #AgenticAI #Web3 #CloudComputing #Fintech #PayPerUse
