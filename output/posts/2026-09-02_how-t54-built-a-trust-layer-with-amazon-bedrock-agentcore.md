---
title: How t54 built a trust layer with Amazon Bedrock AgentCore payments
source: AWS ML
url: https://aws.amazon.com/blogs/machine-learning/how-t54-built-a-trust-layer-with-amazon-bedrock-agentcore-payments/
model: claude-code/sonnet
generated_at: '2026-09-02T10:24:09.505065'
score: 84
---

📌 20 萬筆自主付款零人工核可，AWS Bedrock AgentCore 怎麼做信任層

TL;DR：t54 在 Amazon Bedrock AgentCore Payments 上打造信任層，讓 agent 自主完成 20 萬筆以上的微額付款且無需人工逐筆核准。

Agent 能研究、能推理、能協調多步驟工作流，但一旦碰到付費牆就卡住了，因為它沒有錢包、沒有卡片、也沒有額度上限。t54 的做法是把「該不該付」這件事變成程式碼裡的一道硬性關卡。

🤔 **問題：機器速度的交易，人根本審不完**

t54 的客戶要部署能自主替第三方服務付費的 agentic 系統。文中舉例，一個監控股票部位並在部位變動時通知分析師的 agentic 系統，需要即時付費取得市場資料 API。給 agent 一個錢包不難，難的是周邊治理：如何設定支出上限避免單一失控迴圈把帳戶掏空、如何隔離憑證讓 agent 永遠碰不到原始金鑰、如何為合規稽核每一筆交易，並且要在數十個 agent、上百個端點的規模下同時做到這些。在低量時人工審核還撐得住，但當每小時要處理數千次 API 呼叫時，人工審核就會失效。

🧩 **架構：x402 協定 + Trustline 五項訊號 + IAM 角色分離**

Amazon Bedrock AgentCore Payments 提供支出基礎設施：session 層級的支出限額、憑證隔離與付款執行。t54 的產品 x402-secure 則提供信任判斷：即時為端點與鏈上付款地址評分,決定該不該付款。底層協定是 x402，一種利用 HTTP 402 狀態碼讓客戶端直接透過 HTTP 為 API 付費的開放標準。當 agent 呼叫一個付費端點並收到 402 回應時，由 Amazon Bedrock AgentCore Payments 負責簽署與結算，agent 本身不會接觸私鑰。

評分引擎 Trustline 在每筆付款結算前，會評估五項獨立訊號：付款地址的鏈上歷史、目的網頁的合法性、服務的社群媒體足跡、API 的即時健康狀態，以及綜合以上四者的整體風險分數。t54 刻意設計成沒有任何單一薄弱訊號能單獨授權一筆交易。產品線中還包含 ClawCredit，一套原生支援 agent 的信用額度設施，與 AgentCore Payments 的 session 支出上限各自獨立運作。

架構上採取嚴格的權責分離：透過 IAM 把系統拆成四種角色，agent runtime 能執行付款,但不能更改自己的額度、開通新錢包,或直接存取憑證。實務上 agent 在被呼叫時只拿到一組 session ID 與 instrument ID，開發者憑證透過 Amazon Bedrock AgentCore Identity 加密存放在 AWS Secrets Manager,不會從 API 回傳；終端使用者的錢包簽署金鑰則留在錢包供應商（Coinbase）手中。一旦 agent 用完額度就會停止,沒有從 agent 內部重新開通 session 的路徑。

📊 **規模：2000 萬筆交易，單筆 0.001 到 0.01 美元**

t54 創辦人 Chandler Fang 表示，x402-secure 上線至今已處理超過 2000 萬筆由 AI agent 發起的交易，每筆金額介於 0.001 到 0.01 美元之間，屬於高頻、快速的小額呼叫，是人力無法即時審核的規模。他也提到，過程中已攔截過被判定為高風險的付款端點,讓 session 保住支出上限,並把 agent 導向更安全的服務。

⚠️ **代價：多一道即時風控檢查，就多一點延遲**

主導整合的 Frank He 表示，最困難的決定是把風險檢查做成每次 ProcessPayment 前的強制關卡,而非旁路執行的輔助功能。為每個端點即時評分會增加一點延遲，但他認為讓付款在完成信任確認之前就結算,是不能接受的取捨：「我們接受一點額外延遲，換來一個保證：沒有經過最新風險判斷,任何交易都不會結算。」這道信任檢查是確定性的程式碼關卡，不是模型自行判斷的建議，模型無法覆寫。

🎯 **實務啟示**

對正在設計 agentic 支付或高頻自動化交易系統的工程團隊而言，這個案例點出一個核心原則：花錢的元件不該同時是設定花錢規則的元件。把風險判斷做成獨立、確定性的程式碼關卡，並用 IAM 等機制強制角色分離，是在「速度」與「可控性」之間取得平衡的具體做法，也是導入自主付款前必須先補上的治理層,而不是事後補救的選項。

🔗 **來源**
- 標題：How t54 built a trust layer with Amazon Bedrock AgentCore payments
- 作者／機構：Chris Wajule, AWS Machine Learning Blog
- 連結：https://aws.amazon.com/blogs/machine-learning/how-t54-built-a-trust-layer-with-amazon-bedrock-agentcore-payments/

#AgenticAI #AWSBedrock #AgentCore #x402 #AIAgents #AgenticCommerce #IAM #FinTech #AutonomousPayments #AIInfrastructure
