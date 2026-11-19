---
title: Protect agent tool calls with Skyflow and Amazon Bedrock AgentCore Gateway
source: AWS ML
url: https://aws.amazon.com/blogs/machine-learning/protect-agent-tool-calls-with-skyflow-and-amazon-bedrock-agentcore-gateway/
model: claude-code/sonnet
generated_at: '2026-11-19T23:47:23.208150'
score: 88
---

📌 Agent 呼叫工具時，誰在保護你丟出去的敏感資料？

TL;DR：Skyflow 攔截器接進 Amazon Bedrock AgentCore Gateway，讓敏感資料在送進工具或模型前先被去識別化。

企業導入 AI agent 時，多數資安控制都盯著「模型的輸入輸出」，卻很少有人管「agent 呼叫工具時傳出去、工具回傳回來」的這段資料流。這正是 Skyflow 與 AWS 這次合作要補的洞。

🤔 **問題：工具呼叫是一條沒人管的資料流**

Agent 現在不只回答問題，還會透過 MCP 伺服器、SaaS API、文件儲存、網路搜尋等工具真正「採取行動」，而每一次工具呼叫本質上都是一次資料流動。逐個修補每個 agent 無法規模化，也碰不到第三方工具；控制必須放在「每一次工具呼叫都會經過的那個節點」上，才能讓授權、內容安全與資料保護一致套用到所有 agent 與工具。Amazon Bedrock AgentCore Gateway 正是這個節點：它是每個 agent 使用工具的前置閘道，不論 agent 用什麼框架或模型。

🧩 **方法：把 Skyflow Detect 做成 Gateway 的請求/回應攔截器**

AgentCore Gateway 支援 interceptor（攔截器）機制：可以用一個 AWS Lambda 函式，在每一次通過閘道的呼叫上執行自訂程式碼。請求攔截器會在呼叫抵達工具前看到它，回應攔截器則在結果送回 agent 前看到它，兩者都能檢視、改寫或直接擋下該次呼叫。

Skyflow 把這個機制接成一個單一的 Lambda 函式，同時掛在 AgentCore Gateway 的請求與回應兩個攔截點上。每個攔截點都會呼叫 Skyflow Detect 找出敏感實體（姓名、email、電話、政府 ID、卡號、生日、地址等），用 token 取代原始值，或反過來把 token 還原成原始值；原始值則保存在 Skyflow Vault 中，供被授權的系統日後反查。

Skyflow 的 Gateway 設定會依工具決定套用三種保護模式中的哪一種：
- **Shield the tool（保護工具）**：例如網路搜尋，客戶姓名以 token 形式送出，搜尋服務商永遠看不到真實姓名，結果回來後再還原給分析師。
- **Shield the model（保護模型）**：客戶姓名與 email 以 token 形式送進模型做推論（例如草擬回覆信），回來的草稿再還原成真實值。
- **Shield the document（保護文件）**：攔截器本身不處理檔案內容，而是驗證 presigned URL 後交給 Skyflow Detect 直接抓取並去識別化，agent 拿到的是一份乾淨副本的連結，檔案位元組不會經過 Lambda。

架構上，攔截器從 Parameter Store 讀取政策、從 Secrets Manager 讀取 Skyflow API 金鑰，每次決策都記錄到 Amazon CloudWatch，並用一個approved區域內的 Skyflow Detect 與 Skyflow Vault 做去識別化與還原。針對模型呼叫,攔截器會在 Amazon DynamoDB 中留一筆短期記錄，記下該次呼叫鑄造了哪些 token，以便只還原這些 token（記錄本身不含原始值）。

📊 **情境示範：歐洲銀行的信用卡爭議調查**

文章用一家有嚴格資料駐留義務的歐洲銀行為例：分析師要求 agent 調查一筆爭議交易,agent 會先上網搜尋商家資訊,再從 Amazon S3 拉出爭議案件的備註做摘要。沒有保護的情況下，客戶姓名等敏感資訊會直接暴露給第三方搜尋服務與模型；接上 Skyflow 攔截器後,同一套流程在每個環節都改成以 token 傳遞，只有被授權的一方能看到還原後的真實值。

💡 **開源且可直接掛接既有 Gateway**

Skyflow 攔截器以 MIT 授權開源在 GitHub 的 agentcore-skyflow 儲存庫，Skyflow 本身也已上架 AWS Marketplace。文章指出，若你已經在跑一個 AgentCore Gateway，可以直接把這個攔截器掛接上去；該儲存庫也包含本文完整的參考部署（agent、gateway 與其目標工具），可用 AgentCore CLI 部署。Skyflow 另外提供多種 vault 部署模式與地區選擇，以滿足不同的資料駐留需求。

🎯 **實務啟示**

如果你的 agent 架構已經用 AgentCore Gateway 統一管理工具呼叫，這類攔截器模式值得參考：資料保護只需在閘道這一個節點做一次設定,就能同時覆蓋所有 agent 與工具，不必修改既有 agent 或工具程式碼。對於需要嚴格資料駐留與稽核的產業（如金融），這種「工具與模型都拿不到原始敏感值,僅授權系統可還原」的設計，是把隱私控制與 agent 自主行動解耦的一種做法。

🔗 **來源**
- 標題：Protect agent tool calls with Skyflow and Amazon Bedrock AgentCore Gateway
- 作者／機構：Joe McCarron, AWS ML
- 連結：https://aws.amazon.com/blogs/machine-learning/protect-agent-tool-calls-with-skyflow-and-amazon-bedrock-agentcore-gateway/

#AWS #BedrockAgentCore #Skyflow #DataPrivacy #AIAgents #MCP #Deidentification #AgentSecurity #OpenSource #EnterpriseAI
