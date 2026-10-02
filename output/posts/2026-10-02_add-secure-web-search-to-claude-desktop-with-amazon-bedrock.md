---
title: Add secure Web Search to Claude Desktop with Amazon Bedrock AgentCore
source: AWS ML
url: https://aws.amazon.com/blogs/machine-learning/add-secure-web-search-to-claude-desktop-with-amazon-bedrock-agentcore/
model: claude-code/sonnet
generated_at: '2026-10-02T21:41:37.819453'
score: 74
---

📌 幫 Claude Desktop 接上即時網路搜尋，全程留在 AWS 邊界內

TL;DR：AgentCore Gateway 讓 Claude Desktop 用企業 IAM SSO 安全接上即時 Web Search，免第三方金鑰。

模型的知識停在訓練截止那一天，不管問的是最新文件更新、即時報價還是今天的天氣，它都答不出來。這篇 AWS 教學示範如何在不引入任何第三方 API 金鑰、不讓查詢流量離開 AWS 邊界的前提下，幫 Claude Desktop 補上這塊缺口。

🤔 模型的知識停在訓練那一天

Claude Desktop 跑在 Amazon Bedrock 上雖然能提供強大的 AI 協助，但缺乏整合式網路搜尋時，回答只能依賴模型訓練當下的知識。Amazon Bedrock AgentCore 是用來建置、串接與最佳化 agent 的平臺，其中的 AgentCore Gateway 能把 Claude Desktop 接上 Web Search：一個由涵蓋數百億份文件的 Amazon 網路索引支援、相容 MCP 的全代管搜尋服務，所有查詢流量都留在 AWS 基礎設施內，不需要管理外部 API 金鑰。

🧩 從 IAM Identity Center 到 JWT 的六個步驟

許多企業已經用 AWS IAM Identity Center 做 SSO，這篇教學就把它當成 AgentCore Gateway 的身分驗證來源。由於 Gateway 採 JWT-based inbound authentication，中間需要 Amazon Cognito 當聯邦橋接層，走 OAuth 2.0 authorization code grant flow：IAM Identity Center 用 SAML 處理登入，Cognito 簽發 JWT，Gateway 在每次請求時驗證 token，整條驗證鏈完全留在 AWS 內部。

具體步驟是：

- Step 1：在目標 AWS 帳號建立 Cognito user pool，作為 AgentCore Gateway 的 OIDC token 簽發者。
- Step 2：在 AWS Organizations 管理帳號建立 SAML application，與 Cognito 做聯邦。
- Step 3：回到目標帳號，把 IAM Identity Center 註冊為 Cognito user pool 的 SAML 身分提供者，並建立帶 client secret 的 app client。
- Step 4：用前面取得的 Cognito user pool ID 與 app client ID，建立 Inbound Auth Type 為 JWT 的 AgentCore Gateway，並啟用 Web Search target。
- Step 5：在 Claude Desktop 的 Connectors and Extensions 設定裡新增 server，點選登入測試，瀏覽器會導向 IAM Identity Center 的 SSO 登入頁完成驗證。
- Step 6：登入成功後，Claude Desktop 透過 MCP 的 tools/list 呼叫發現 WebSearchTool；之後只要模型判斷需要即時資訊，就會跳出工具執行核准視窗，使用者可選擇 Deny、Allow for this task 或 Allow once。

⚠️ 目前只開放三個地區，其餘身分系統可替換

Web Search on Amazon Bedrock AgentCore 目前只在美國東部（維吉尼亞北部）、歐洲（愛爾蘭）與亞太（東京）三個 Region 開放，建立 Gateway 前要先確認所在地區支援。文中也特別說明，雖然示範用的是 IAM Identity Center，但同樣的模式可以套用在任何 SAML 或 OIDC 相容的身分提供者，只要在 Cognito 設一個聯邦來源就能替換。

🎯 讓既有 SSO 治理直接延伸到 agent 工具呼叫

對已經用 IAM Identity Center 做內部 SSO 治理的企業，這條路徑讓 Claude Desktop 的網路搜尋能力可以直接套用既有的身分治理框架，不必額外管理第三方金鑰或引入新的信任系統。對想把 agent 工具呼叫做到「可審計、可逐次核准」的團隊，文中示範的工具執行核准視窗（Deny／Allow once／Allow for this task）也是值得參考的互動設計。

🔗 來源
- 標題：Add secure Web Search to Claude Desktop with Amazon Bedrock AgentCore
- 作者／機構：Jishnu Dasgupta，刊於 AWS Machine Learning Blog
- 連結：https://aws.amazon.com/blogs/machine-learning/add-secure-web-search-to-claude-desktop-with-amazon-bedrock-agentcore/

#AWS #BedrockAgentCore #Claude #MCP #IAMIdentityCenter #AmazonCognito #WebSearch #EnterpriseAI #OAuth2 #AgentSecurity
