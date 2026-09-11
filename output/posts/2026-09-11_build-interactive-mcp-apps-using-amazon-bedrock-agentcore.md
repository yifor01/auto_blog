---
title: Build interactive MCP Apps using Amazon Bedrock AgentCore
source: AWS ML
url: https://aws.amazon.com/blogs/machine-learning/build-interactive-mcp-apps-using-amazon-bedrock-agentcore/
model: claude-code/sonnet
generated_at: '2026-09-11T19:52:03.894743'
score: 93
---

📌 【AWS 技術分享】讓你的服務同時「長」在 ChatGPT 與 Claude 裡

TL;DR：用 Amazon Bedrock AgentCore 部署 MCP App，一套後端就能在多個 AI host 顯示互動式 HTML 卡片。

當使用者愈來愈習慣直接跟 ChatGPT、Claude 這類 AI host 對話來使用服務，純文字回應已經不夠用了。問題是，如果每個 host 都要客製一套整合，維護成本會直接爆炸。

🤔 **不綁定單一 AI host 的互動介面**

MCP Apps 是 Model Context Protocol（MCP）的擴充,讓 MCP 伺服器可以直接在 AI host 內渲染互動式 HTML widget,而不只是回傳文字。Amazon Bedrock AgentCore 則提供了承載這些服務的平臺，其中 AgentCore runtime 是一個安全、無伺服器、session 隔離的主機環境,原生支援 MCP;AgentCore Gateway 則把它包裝成一個外部 AI host 可以連接的單一安全端點。因為 MCP Apps 是與 host 無關的標準,同一套後端不管在 ChatGPT、Claude 或其他支援該擴充的 host 中打開,體驗都一致。

🧩 **架構：MCP 伺服器只是薄薄一層協定轉接器**

文章以範例應用 Unicorn Rentals（獨角獸租賃）示範整套架構。使用者可以瀏覽可租用的獨角獸、預訂、查看目前租約、歸還獨角獸。整個服務由跑在 AgentCore runtime 上的一臺 MCP 伺服器提供,前面掛上 AgentCore Gateway。MCP 伺服器是用 TypeScript 寫的 Express.js 應用,基於官方 @modelcontextprotocol/sdk 加上 @modelcontextprotocol/ext-apps 擴充。工具透過 registerAppTool 註冊（例如 list_unicorns、book_unicorn、view_bookings、return_unicorn）,並在 tool config 的 _meta.ui.resourceUri 欄位指定要渲染哪個 widget,tool 呼叫回傳的 structuredContent 則是要注入 widget 的資料;Widget 本身以 MCP Resources 形式用 registerAppResource 註冊,回傳 widget 的 HTML。

真正的業務邏輯完全不在 MCP 層,而是由一個獨立的 AWS Lambda 函式處理庫存查詢與訂位操作,搭配 Amazon DynamoDB 做持久化。Lambda 對 MCP 一無所知——作者強調,在真實場景中這部分完全可以換成已經跑在 Amazon ECS、Amazon EKS 或其他運算服務上的既有服務,MCP 伺服器只是一層薄的協定轉接器。

部署面,AgentCore runtime 設定為 NODE_22 環境，透過 resource-based policy 限制只有 AgentCore Gateway 的執行角色能呼叫,其餘一律拒絕;Gateway 對外採 No Auth 接收請求,再用自己的 IAM 執行角色以 SigV4 呼叫 runtime,呼叫方不需要自己處理 AWS 憑證;AWS WAF 則在 Gateway 端點前加上 IP 允許清單、受管威脅偵測規則與速率限制。

📦 **怎麼用**

部署流程由單一 deploy.sh script 統籌建置與 CDK stack 部署,下載原始碼後執行部署腳本,即可在自己的 AWS 帳號建立所需資源。部署完成後輸出的 GatewayResourceUrl,就是用來連接 AI host 的端點。

實際體驗上,文章示範了四個互動步驟：問「Can you show all unicorns?」會以互動卡片顯示每隻獨角獸的圖片、名稱、描述、時薪與可租狀態;訂位後立即以卡片確認訂單編號、日期、時薪;查詢目前租約時則改以純文字回應（因為不是每個請求都需要豐富介面）;歸還獨角獸時系統會依租用時長與時薪計算總費用並回報。

🎯 **實務啟示**

對想把服務接進 AI host 生態的團隊來說，這個模式的價值在於解耦：業務邏輯留在原本的服務裡，MCP 層只負責協定轉接與 widget 渲染，一套實作就能跨多個 host 使用，不必為每個 AI host 各自客製整合。

🔗 **來源**
- 標題：Build interactive MCP Apps using Amazon Bedrock AgentCore
- 作者／機構：Dantis Stephen（AWS ML Blog）
- 連結：https://aws.amazon.com/blogs/machine-learning/build-interactive-mcp-apps-using-amazon-bedrock-agentcore/

#MCP #ModelContextProtocol #AmazonBedrock #AgentCore #AWS #AIAgents #LLMTooling #ChatGPT #Claude #InteractiveUI
