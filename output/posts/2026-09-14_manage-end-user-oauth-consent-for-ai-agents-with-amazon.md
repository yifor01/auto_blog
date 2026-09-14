---
title: Manage end-user OAuth consent for AI agents with Amazon Bedrock AgentCore
source: AWS ML
url: https://aws.amazon.com/blogs/machine-learning/manage-end-user-oauth-consent-for-ai-agents-with-amazon-bedrock-agentcore/
model: claude-code/sonnet
generated_at: '2026-09-14T21:09:47.701080'
score: 79
---

📌 AgentCore 新增同意入口,AI Agent 存取 GitHub/Slack 免自架 OAuth

TL;DR：Amazon Bedrock AgentCore 推出 Consent Portal,把 OAuth session binding 這個基礎設施代管掉,免除自建授權流程的負擔。

AI agent 要代替使用者操作 GitHub、Slack 這類第三方服務,聽起來簡單,實作起來卻藏著一段麻煩的中間層:使用者要先向服務提供者驗證身分並明確授權,而應用程式接下來必須把拿到的 OAuth 授權安全地綁定回「是哪個使用者授權的」,這個過程叫 session binding(工作階段綁定)。這篇 AWS Machine Learning Blog 文章介紹的 Consent Portal,就是為了把這段麻煩事從客戶自己身上拿掉。

🤔 過去,客戶得自己蓋一套授權基礎設施

文章指出,過去使用 AgentCore Identity 三方(3LO,three-legged OAuth,即 OAuth 2.0 authorization code flow)流程的客戶,必須自行建置並維運整套 session binding 基礎設施:呈現授權網址、架設公開的 HTTPS callback、驗證回來的使用者身分、管理瀏覽器工作階段,還要呼叫 CompleteResourceTokenAuth 完成整個流程。這些都是與核心業務無關,卻必須做對的「管線工程」。

🧩 Consent Portal 怎麼運作

現在 AgentCore Identity(Amazon Bedrock AgentCore 的一項能力)提供了 Consent Portal:一個代管的網頁體驗,同時也是 AgentCore Gateway 的 session binding 端點。管理員針對一個 gateway 建立 portal,把產生的網址分享給使用者;使用者用組織自己的身分提供者(IdP)登入,檢視這個 agent 可以存取哪些服務,再逐一對個別提供者授予同意。整個瀏覽器導轉與 session binding 都由 portal 處理,授權後拿到的 token 則存進 AgentCore Identity 的 token vault。

文中用一個名為 Example Corp 的例子說明:公司提供開發者一個透過 AgentCore Gateway 存取的 AI 程式碼助理,底下掛了 GitHub 與 Slack 兩個 target。管理員用公司自己的 IdP 驗證員工身分,確保每一筆 GitHub、Slack 的 OAuth 授權都能對應回是哪位員工核准的;開發者則可以個別、獨立地連接 GitHub 或 Slack,之後回到 IDE 或 MCP 用戶端(例如 Kiro、Claude Code、Cursor、Visual Studio Code)使用工具時,不需要重複被提示授權。

設定流程上,管理員需要完成六個步驟,包括設定 IdP、gateway targets、執行角色(execution role)與 Consent Portal 本身;IdP 必須能發出 JSON Web Token(JWT)格式的存取 token,文中以 Okta 的自訂授權伺服器、Auth0 的 audience 設定為例。Portal 上線後的網址格式固定為 https://<gateway-name>.consent-portal.bedrock-agentcore.<region>.amazonaws.com。使用者端則只需完成第七步:登入並針對每個服務個別授權,文中的截圖示範了 GitHub 已連接、Slack 尚未連接可以並存的狀態,授權過的服務下次開啟 portal 時仍會保持已連接,除非授權被撤銷、過期或需要重新同意,使用者也能主動選擇中斷連線。

💡 稽核與收尾都內建在流程裡

這項功能把稽核也一併處理了:所有同意操作都會記錄進 AWS CloudTrail,可以透過篩選事件來源 bedrock-agentcore.amazonaws.com 查看,例如 GetResourceOauth2Token 事件會記錄使用的憑證提供者、請求的 scope、OAuth 流程類型與 portal 的執行角色,且敏感的 token 與 state 值會被自動遮蔽,方便在授權失敗時用 errorCode 與 errorMessage 定位問題。文中也提醒收尾時的順序:必須先刪除 gateway target,才能刪除它所參照的外部憑證提供者,順序顛倒會刪不掉。

⚠️ 這仍是需要管理員先把地基打好的功能

Consent Portal 省掉的是「自建授權介面與 session binding 邏輯」這一層,但管理員仍需要完成 IdP 整合、IAM 執行角色、OAuth 憑證提供者等一系列設定才能讓 portal 上線,並不是零設定的即插即用。

🎯 實務啟示

對正在把 agent 接到需要使用者授權的外部服務(GitHub、Slack 或其他 SaaS)的團隊來說,這解決的是一個容易被低估、卻極其容易在安全性上出錯的環節:把 OAuth token 正確綁定到對的使用者身上。尤其是透過 IDE 或 MCP 用戶端呼叫工具的場景,使用者只要授權一次,後續呼叫就能沿用已儲存的 token,對開發體驗與安全治理都是實質的改善。

🔗 來源
- 標題：Manage end-user OAuth consent for AI agents with Amazon Bedrock AgentCore
- 作者／機構：Swara Gandhi(AWS Machine Learning Blog)
- 連結：https://aws.amazon.com/blogs/machine-learning/manage-end-user-oauth-consent-for-ai-agents-with-amazon-bedrock-agentcore/

#AWS #BedrockAgentCore #OAuth #AIAgents #MCP #IdentityManagement #CloudTrail #DeveloperTools #Security #AgenticAI
