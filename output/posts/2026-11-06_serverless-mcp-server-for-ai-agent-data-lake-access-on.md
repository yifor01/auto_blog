---
title: Serverless MCP server for AI agent data lake access on Amazon ECS Fargate
source: AWS ML
url: https://aws.amazon.com/blogs/machine-learning/serverless-mcp-server-for-ai-agent-data-lake-access-on-amazon-ecs-fargate/
model: claude-code/sonnet
generated_at: '2026-11-06T22:29:18.876580'
score: 80
---

📌 讓 AI Agent 讀懂整座資料湖：用 MCP 打造可共用的查詢閘道

TL;DR：用 metadata 驅動的 MCP 閘道統一多個 agent 存取企業資料湖。

當每個 AI agent 都自己寫一套 SQL 產生邏輯、自己管一套權限，schema 一改就要全部重新部署——這是許多企業導入 AI 助理後真正的痛點，而不是模型能力不足。

🤔 背景：資料存取零散，上線一個資料集要花好幾天

Amazon 北美 Sort Center（NASC）的規劃團隊需要對話式查詢來管理產能、人力與貨物流向，但資料湖裡有數千個資料集，涵蓋營運指標、商業分析與領域資料。過去每個團隊各自從零打造整合：agent 各自內嵌 SQL 產生邏輯、schema 知識與連線處理，schema 一變動就要逐一修補每個 agent；權限控管分散，沒有單一稽核點；上線一個新資料集需要客製工具程式碼、查詢驗證與重新部署，通常每個表格都要花上好幾天的工程時間。

🧩 架構：四層職責分離，metadata catalog 是核心

系統拆成四層：client、MCP server、tools、知識庫更新（knowledge-base refresh），各自獨立擴充與部署。請求流程是：使用者從 web chat、Slack、IDE 外掛或外部 agent 發出查詢 → 經 Amazon Route 53 解析 → Application Load Balancer（配置 HTTPS 與 AWS WAF）→ Amazon Cognito 做身份驗證並豐富請求內容 → 進入私有子網的 client 層（Amazon ECS Fargate，session 狀態存在 Amazon DynamoDB）→ 轉送到內部 ALB 後方的 MCP server 層（同樣跑在 ECS Fargate 上）。

MCP server 層由 Amazon Bedrock 驅動的 agent 負責協調，工具用 FastMCP（Python 框架）建置，每次模型互動都套用 Amazon Bedrock Guardrails。資料層由 Amazon Athena 與 Amazon Redshift 執行 SQL 查詢，Amazon Bedrock Knowledge Bases 負責語意搜尋；資料寫入 Amazon S3 與知識庫則由 AWS Lambda 處理。Fargate task 本身是無狀態的，對話狀態存在 DynamoDB，所以 task 可以隨時被取代或擴充而不丟資料。

🧩 metadata 驅動：上線新資料集不用寫程式

metadata catalog 儲存 schema 描述、欄位層級語意與資料表關聯，agent 產生 SQL 時直接查詢這份 catalog，所以 schema 改變時不需要寫死 table 結構或重新部署。新增資料集只需要一份 JSON metadata 檔，描述該表的 schema、商業情境與欄位語意，搭配一個可選的 context mapping 項目。

`business_description_for_the_table` 欄位可以放引擎專屬的查詢提示（例如「字串常值一律用 date() 包起來」），減少 SQL 驗證失敗；`column_details` 把每個 column_name [type] 配上自然語言描述與範例值；`sample_values` 讓 agent 學到真實資料格式，例如知道 `warehouse_id` 存的是 `FC-EAST-07` 這種代碼，而不是「東區廠區」這種拼寫名稱。context mapping 設定可以把每次查詢限定在相關資料表範圍，減少雜訊並提升 SQL 產生準確度；新增一個商業領域只需要在這份 mapping 加一筆項目。團隊實測這樣的範圍限定能把整體互動延遲維持在 15 到 20 秒。

🧩 安全與介面

透過 `/mcp` 這個 FastMCP 驅動的 JSON-RPC endpoint，外部相容 MCP 的客戶端（例如 Amazon Q Developer 或 IDE 擴展）可以直接發現並呼叫工具。Athena 查詢工具在工具層就限制只能執行 SELECT，寫入操作在碰到資料湖之前就被拒絕。Amazon Bedrock Guardrails 套用在每一次模型互動上，負責過濾有害內容、做 grounding 檢查並協助阻擋 prompt injection，這些防護統一生效在 MCP server 層，不論哪個 agent 連進來都享有一致的內容安全政策。

⚠️ 限制

文章僅公開查詢路徑的延遲範圍（15–20 秒），未提供其他效能或規模數據；工具層目前也只支援 SELECT 查詢。

🎯 實務啟示

如果組織也面臨「每個 agent 各自接資料源」的問題，metadata catalog 加共用 MCP 閘道是值得參考的解法：把 schema 知識與查詢邏輯從 agent 程式碼抽出來，改成設定檔驅動，上線新資料集就不需要重新部署整個 agent。把身份驗證、WAF、Guardrails 與 SELECT-only 限制都收斂在 MCP server 這一層，能讓多個 agent 或應用程式共用同一套治理機制，而不是各自實作一份。

🔗 來源
- 標題：Serverless MCP server for AI agent data lake access on Amazon ECS Fargate
- 作者／機構：Aishwarya Pawar, AWS
- 連結：https://aws.amazon.com/blogs/machine-learning/serverless-mcp-server-for-ai-agent-data-lake-access-on-amazon-ecs-fargate/

#MCP #AWS #AIAgent #DataLake #ECS #Fargate #Bedrock #TextToSQL #ServerlessArchitecture #EnterpriseAI
