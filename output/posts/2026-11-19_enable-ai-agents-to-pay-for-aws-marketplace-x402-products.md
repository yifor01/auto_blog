---
title: Enable AI agents to pay for AWS Marketplace x402 products with Amazon Bedrock
  AgentCore payments
source: AWS ML
url: https://aws.amazon.com/blogs/machine-learning/enable-ai-agents-to-pay-for-aws-marketplace-x402-products-with-amazon-bedrock-agentcore-payments/
model: claude-code/sonnet
generated_at: '2026-11-19T23:52:26.067841'
score: 82
---

📌 AWS讓AI Agent用公司帳單自己買Marketplace服務

TL;DR：Amazon Bedrock AgentCore payments擴展到AWS Marketplace，agent可透過x402協定自主採購，費用直接計入AWS帳單。

🎣 **agent要花錢，不用再靠加密錢包**

過去想讓agent自己付費使用第三方API，通常得先申請金鑰、綁信用卡，或是弄一個穩定幣錢包。AWS這次把「付款」這個動作，變成agent可以在整個流程中自己完成的一步，而且錢是從開發者自己的AWS帳單出。

🤔 **從任意x402服務，擴展到整個Marketplace**

2026年8月，Amazon Bedrock AgentCore payments正式上線，讓agent能透過x402、MPP等開放協定，自主支付需要付費的API、MCP伺服器與網路內容，並設有付款額度與完整的可觀測性。這次的更新把這個能力延伸到AWS Marketplace：agent可以發現並購買支援x402的軟體、API、資料與內容，直接用美元從agent開發者的AWS帳單扣款，不再需要穩定幣錢包或額外的API金鑰。開發者也可以透過AgentCore Gateway裡新增的AWS Marketplace連接器，設定並自動化商品發現流程。

🧩 **一次購買的五個步驟**

文章用一個情境說明流程：一位金融分析師問agent「這週關於agentic payments有什麼公告」，模型沒有這週的新聞，於是agent去找搜尋工具：

1. **發現（Discover）**：agent依序呼叫AgentCore Gateway裡三個唯讀工具——搜尋清單（只回傳支援x402的商品）、取得特定清單詳情、列出其履行方式，最後拿到賣方（例如Tavily）的endpoint URL與支援的付款協定。
2. **取得報價**：agent不帶付款資訊呼叫該endpoint，賣方回應HTTP 402，並在PAYMENT-REQUIRED header中附上簽署過的報價；AWS Marketplace會用賣方註冊的金鑰驗證簽章，報價一旦被竄改就會被拒絕。
3. **付款**：agent把報價轉交給ProcessPayment API，付款類型設為AWS_BILLING_X402；若session額度還夠，AgentCore payments就會核發付款token，額度不夠則直接失敗，開發者不會被扣款。
4. **兌換**：agent帶著放在PAYMENT-SIGNATURE header裡的token重新送出請求，取得賣方回傳的內容；token有效期約5分鐘，取得報價、付款、兌換必須在同一輪內完成。
5. **結算**：開發者首次向某賣方購買時，AWS Marketplace會建立雙方的協議，之後每次採購都自動歸入該協議計費，非同步結算後每月出現在AWS帳單上。

護欄機制方面，開發者可以透過AgentCore policy設定花費上限與核准賣方清單，AgentCore payments本身也會強制執行付款session額度，確保agent不會超支；所有交易都可以在AWS CloudTrail與AWS Cost Explorer中稽核。若企業使用Private Marketplace，agent也只能購買被允許的商品。

📊 **官方範例：三個角色互不越權的IAM設計**

AWS在agentcore-samples這個GitHub repo提供了一份可執行的範例。其中`setup_aws_billing.py`會建立Payment Manager與AWS Billing連接器，並設定AWS Marketplace的service-linked role，以及三個權限互相分離的IAM角色：session角色能設定預算但不能付款，agent角色能付款但不能建立session或自行調高預算。`setup_gateway.py`則建立帶有Marketplace連接器的AgentCore Gateway，權限僅限三個唯讀動作；如果想跳過這一步，也可以直接在環境變數設定SELLER_URL，讓agent只對該URL付款。範例中預設session預算是0.05美元、單次請求上限0.02美元，實測對象是一個報價0.01美元的賣方，agent在下單前先比較了兩份清單。執行結束後，範例會印出付款金額、AWS Marketplace商品ID與processPaymentId；由於計量是非同步的，Tavily的帳單項目要等一會才會出現。

生態系夥伴Tavily（一家提供agentic商務即時搜尋的廠商）的創辦人兼CEO Rotem Weiss表示，透過x402把安全交易帶進AWS Marketplace、並把agent連結到經過KYC驗證的供應商，是AWS團隊與Tavily合作設計agentic commerce的信念所在，也是他們認為「企業級agentic commerce」該有的樣子。

💡 **目前只支援固定報價的x402**

目前AWS Billing在上線時只支援x402的「exact」方案，也就是賣方對每個請求報一個固定價格，還不支援動態計價。三個IAM角色互相分權的設計也值得留意：agent本身完全沒有辦法調高自己的預算上限，這個設計邊界是刻意畫在session建立與付款執行之間。

⚠️ **還在成長中的生態系**

x402商品目錄目前仍在擴充可信賴、經過驗證的賣方；設定AWS Billing連接器需要先開通`AWSServiceRoleForMarketplaceAgenticCommerce`這個service-linked role；計量結算是非同步的，帳單項目不會立刻出現。

🎯 **實務啟示**

對需要讓agent自主採購第三方資料或工具的企業團隊，這個整合把付款流程收斂到既有的AWS帳務與稽核工具（CloudTrail、Cost Explorer）裡，省掉管理穩定幣錢包或額外金鑰的麻煩；但建議先用官方GitHub範例跑一遍，理解session角色與agent角色的分權設計，再評估所需的供應商是否已經支援x402的exact方案。

🔗 **來源**
- 標題：Enable AI agents to pay for AWS Marketplace x402 products with Amazon Bedrock AgentCore payments
- 作者／機構：Madhu Samhitha Vangara，AWS Machine Learning Blog
- 連結：https://aws.amazon.com/blogs/machine-learning/enable-ai-agents-to-pay-for-aws-marketplace-x402-products-with-amazon-bedrock-agentcore-payments/

#AWS #AgentCore #x402 #AgenticCommerce #BedrockAgentCore #AIAgents #Marketplace #CloudTrail #PaymentInfra #AgenticAI
