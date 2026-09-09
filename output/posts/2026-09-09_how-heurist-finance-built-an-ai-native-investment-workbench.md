---
title: How Heurist Finance built an AI-native investment workbench on Amazon Bedrock
  AgentCore
source: AWS ML
url: https://aws.amazon.com/blogs/machine-learning/how-heurist-finance-built-an-ai-native-investment-workbench-on-amazon-bedrock-agentcore/
model: claude-code/sonnet
generated_at: '2026-09-09T20:07:39.717827'
score: 82
---

📌 Heurist Finance 如何用 Amazon Bedrock AgentCore 打造會自主買資料的投資顧問

TL;DR：Heurist Finance 用 AgentCore 的付費、身分、沙箱模組，讓 agent 依查詢即時購買金融資料並留下稽核軌跡。

當使用者丟出一句「這檔股票是不是被高估了」，背後的 agent 得先去買一筆要價不斐的機構級資料，自己跑運算，還得證明每一分錢花在哪、每一步操作屬於哪個使用者。這套基礎設施，Heurist 選擇不自己蓋，而是整個搬上 Amazon Bedrock AgentCore。

🤔 **付費資料牆，與代理人花錢的兩難**

Heurist Finance 把機構等級的投資工作流整合進單一聊天介面：蒐集市場資料、讀取財報與新聞、執行深度研究、建立並壓力測試投資組合、監控部位，每個回答都會對照使用者的持倉與偏好作答。問題在於，這些優質的市場、總體經濟、基本面與另類資料多半藏在付費牆或客製 API 後面，沒有單一供應商能涵蓋全部，而在產品還沒有大量使用者之前，簽企業合約也不划算。按查詢購買所需資料是更好的經濟模型，但也代表 agent 必須代表使用者花錢，同時得落實保管、支出上限與稽核要求。每一個動作都要對應到特定使用者、session 與 request，身分因此必須貫穿整個工作流，還需要跨 session 狀態、隔離的程式碼執行環境、付款協調與端到端追蹤。

🧩 **Strands orchestrator 串起 Claude、Aurora 與 AgentCore 全家桶**

Heurist 用 Strands 做 agent orchestration，模型是 Amazon Bedrock 上的 Anthropic Claude。Strands orchestrator 呼叫 Claude、從 Amazon Aurora PostgreSQL 載入投資組合資料，並協調 AgentCore Identity、Memory、Code Interpreter、Observability 與 payments：分析產物寫進 Amazon S3，追蹤紀錄送進 Amazon CloudWatch，憑證留在 AWS Secrets Manager，付費資料請求則透過 AgentCore payments 串接 Base 區塊鏈上的 USDC 穩定幣結算。一次提問可能同時牽涉價格、總經指標、財報、基本面與新聞，再跑相關性分析、情境模擬、圖表或回測，這些運算全部在 AgentCore Code Interpreter 的沙箱裡執行，沒有任意對外連網，分析結束就整個銷毀。付費部分由 Payment Manager 協調 CoinbaseCDP Payment Connector：每次互動會拿到一個帶 maxSpendAmount 上限的 Payment Session，以及一個綁定 Base 網路的 Payment Instrument（內嵌加密錢包），每筆付費請求走 x402 協議，讓 Heurist 不需要供應商合約或預付款，單純按查詢購買資料。AgentCore Identity 則讓已驗證的使用者身分貫穿每一次服務呼叫，每個工具呼叫、付款與記憶體操作都會記錄使用者 ID、workload identity、request ID 與 trace ID，串成一條跨服務的稽核軌跡；Amazon Bedrock Guardrails 同時過濾輸入輸出，協助阻擋針對付款與資料工具的 prompt injection，並執行「不建議未避險單一個股」這類政策。

💡 **一次「PCE 公布對我的投資組合有何影響」提問的完整鏈路**

Orchestrator 先從 Aurora PostgreSQL 讀取使用者投資組合，由 AgentCore Identity 把讀取範圍限定在該使用者；接著呼叫一個付費的共識預測端點，收到 HTTP 402 後，AgentCore payments 檢查 Payment Session 的支出上限並透過 Payment Instrument 簽署付款，orchestrator 帶著 X-PAYMENT header 重新送出請求；Code Interpreter 在沙箱裡計算對投資組合的影響並把圖表寫進 S3；最後 Bedrock 結合使用者的持倉、時間範圍與風險偏好合成回答，連同圖表一起串流回傳。整條路徑把 Aurora、AgentCore Identity、payments、Code Interpreter、S3、Bedrock 與 Observability 串成同一個共享的使用者與追蹤脈絡。

🎯 **省下的不只是工程時間，還有一致的稽核軌跡**

Heurist 估計，相較於自建 LLM orchestration 堆疊，用 AgentCore 大約減少 80% 的 agent 系統工程量，因為身分、跨 session 記憶、沙箱與付款基礎設施都交給平臺處理，也讓每位使用者的邊際成本可預測，支撐零售端的定價策略。團隊的說法是：「AgentCore 把平臺的工作做掉了，我們才能把精力全部投入產品本身，這套受管理的基礎設施幫我們省下了好幾個月。」在這個基礎上，Heurist 正朝三個方向擴充：綁定財報行事曆的事件驅動研究、對市場事件做投資組合層級的分析，以及根據相似時間範圍投資人正在研究的標的提供建議。

🔗 **來源**
- 標題：How Heurist Finance built an AI-native investment workbench on Amazon Bedrock AgentCore
- 作者／機構：JW Wang, AWS Machine Learning Blog
- 連結：https://aws.amazon.com/blogs/machine-learning/how-heurist-finance-built-an-ai-native-investment-workbench-on-amazon-bedrock-agentcore/

#AmazonBedrock #AgentCore #AIAgents #FinTech #Claude #Strands #AWS #x402 #StablecoinPayments #InvestmentTech
