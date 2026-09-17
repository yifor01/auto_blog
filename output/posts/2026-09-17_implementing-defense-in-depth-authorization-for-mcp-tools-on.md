---
title: Implementing defense-in-depth authorization for MCP tools on Amazon Quick
source: AWS ML
url: https://aws.amazon.com/blogs/machine-learning/implementing-defense-in-depth-authorization-for-mcp-tools-on-amazon-quick/
model: claude-code/sonnet
generated_at: '2026-09-17T20:35:30.472233'
score: 89
---

📌 SSO過關不代表能為所欲為：MCP工具的四道授權閘道

TL;DR：AWS示範用JWT claims串聯四道閘道，為MCP工具打造細粒度、可稽核的縱深防禦授權。

拿到一組有效的 SSO token，是不是就等於可以呼叫任何 MCP 工具、存取任何資料？AWS 這篇部落格給出的答案是：不行。「已驗證身分」不等於「已獲得授權」。

🤔 當MCP工具碰到敏感資料，單靠SSO不夠用

MCP（Model Context Protocol）是一種開放協定，能讓應用程式串接內部工具、資料庫與 API，減少客製整合的工作量。但文章指出，一旦這些工具開始碰觸敏感資料，單純有效的 SSO token 就不再足夠：沒有分層的縱深防禦授權機制，一個範圍過寬的 token 就可能讓呼叫者存取超出其角色範圍的工具與資料，進而讓合規稽核變得複雜。舉例來說，一個受監管組織可能要求登入時強制多因子驗證（MFA），並限制來自未核准國家的存取——身分提供者（IdP）能滿足前者，但唯有授權層能落實後者。

🧩 四道閘道，一道攔截器搞定

AWS 提出的做法，是在 Amazon Bedrock AgentCore Gateway 上掛載一個 AWS Lambda REQUEST 攔截器（interceptor），依固定順序評估 OpenID Connect（OIDC）JWT 中的 claims，共分四道閘道：

1. MFA 驗證
2. 地理位置限制
3. 群組對角色的對應（RBAC）
4. 工具層級的權限檢查

其中第 3、4 道閘道（RBAC 與工具權限）是核心授權層，恆常啟用；第 1、2 道閘道則可透過環境變數彈性開關，依組織的合規需求決定要啟用幾道。文章特別說明第 1 道 MFA 閘道其實有兩層把關：Entra ID 的 Conditional Access Policy 會在核發 token 前就先要求完成 MFA，攔截器內則可另外再檢查 token 中的 amr claim，作為第二層確認；任何一道閘道未通過的請求，會直接被拒絕並回傳 403，不會碰到工具或底層資料，通過的每一筆異動（mutation）則會寫入不可竄改的稽核紀錄。

💡 用PKCE與Resource Indicators把token鎖死在單一端點

技術實作上，Amazon Quick 使用 PKCE（Proof Key for Code Exchange）搭配 RFC 8707 Resource Indicators，將每個 access token 綁定到特定的 API 端點：在 token 交換過程中，Amazon Quick 會把 AgentCore Gateway 的 URL 當作 resource 參數傳給 Entra ID，而當 resource 是以 URL 表示時，Entra ID 要求 client 與 resource 必須是各自獨立的應用程式註冊。文章以一家虛構企業 AnyCompany Global Services 為例，說明這套模式如何應用在一個透過 MCP 存取、架設於 Amazon DynamoDB 上的多租戶風險登記系統，並指出這類需求在金融服務、醫療與政府單位這類需要合規稽核的產業中特別常見。

⚠️ 這是一份接續部署的設定指南，不是從零開始的教學

文章明確說明，這套走查（walkthrough）假設 AWS 端的資源（AgentCore Gateway、攔截器 Lambda、工具 Lambda、DynamoDB 資料表）都已經部署完成，重點放在身分與授權層的設定；此外，啟用 Conditional Access Policy 需要 Microsoft Entra ID P1 或 P2 授權，操作者也需要具備 Global Administrator 或 Application Administrator 權限。

🎯 實務啟示

如果團隊正把敏感資料源透過 MCP 接上像 Amazon Quick 這類 AI 助理，這套「四道閘道＋不可竄改稽核紀錄」的模式，提供了一個可落地的合規範本：核心思路是把 RBAC 與工具層級權限設為恆常防線，再依實際合規要求彈性疊加 MFA 與地理限制，讓每一次工具呼叫都成為一個可被稽核、可被解釋的存取事件。

🔗 來源
- 標題：Implementing defense-in-depth authorization for MCP tools on Amazon Quick
- 作者／機構：Anneline Sibanda, AWS Machine Learning Blog
- 連結：https://aws.amazon.com/blogs/machine-learning/implementing-defense-in-depth-authorization-for-mcp-tools-on-amazon-quick/

#MCP #AWS #AmazonBedrock #AgentCore #Authorization #Cybersecurity #RBAC #JWT #EnterpriseAI #CloudSecurity
