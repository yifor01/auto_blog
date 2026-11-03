---
title: ServiceNow on-behalf-of token exchange with Bedrock AgentCore Gateway
source: AWS ML
url: https://aws.amazon.com/blogs/machine-learning/servicenow-on-behalf-of-token-exchange-with-bedrock-agentcore-gateway/
model: claude-code/sonnet
generated_at: '2026-11-03T22:38:09.469688'
score: 83
---

📌 AgentCore Gateway 如何讓 AI Agent 代表使用者呼叫 ServiceNow

TL;DR：AWS 示範用 Bedrock AgentCore Gateway 做 OBO token 交換,讓 Agent 呼叫 ServiceNow API 時保留使用者身分。

當 AI Agent 代表使用者呼叫企業內部 API 時,一個容易被忽略卻後果嚴重的問題是：下游服務收到的請求,身分是「這個應用程式」,而不是「真正發起動作的那位使用者」。這聽起來只是個技術細節,實際上卻會打穿稽核軌跡,繞過使用者層級的存取控制,違反最小權限原則——對企業客戶而言,這往往是能不能上線的關鍵。

🤔 **Token 的 audience 對不上,是問題的根源**

Agent 呼叫 AgentCore Gateway 時,帶的 JWT 的 audience claim 對應的是 Agent 自己的應用程式註冊(例如以 3ff88e17 開頭的 client ID);但 ServiceNow 期待看到的 audience,卻是它自己 API connector 的 client ID(例如以 5d4a7a11 開頭)。兩者對不上,身分就斷在半路。

🧩 **On-Behalf-Of 流程：三個角色,一次交換**

這篇文章示範的架構,串接了 AWS、Microsoft Entra ID 與 ServiceNow 三方,核心是透過 AgentCore Gateway 做 OBO（on-behalf-of）token 交換,流程可以拆成四步：

1. 使用者取得一個 JWT,用來呼叫 Agent。
2. Agent 用這個 JWT 向 Gateway 認證,token 的 scope 對應 Agent 自己的應用程式註冊。
3. Gateway 執行 OBO 流程,把這個 token 換成一個新 token,scope 對應到 ServiceNow 的 API connector,但原始使用者的身分被保留下來——具體做法是 Gateway 把輸入 token、Agent 應用程式的 client 憑證、目標 scope,以及參數 requested_token_use: on_behalf_of 一起送到 Entra 的 token endpoint;Entra 驗證使用者確實同意了這個委派,才核發新 token,且使用者的 claims 原封不動保留。
4. ServiceNow 收到合法 token 後,用其中的 preferred_username claim 對應到既有的 ServiceNow 使用者,套用該使用者的權限來處理這個 API 呼叫。

這個模式並不只限於 ServiceNow,文章也提到可以套用到任何用 OAuth 保護的 REST API。

🧩 **實際設定：Entra 兩個應用程式註冊 + ServiceNow 入站整合**

落地時,需要在 Microsoft Entra ID 建立兩個應用程式註冊：一個代表 ServiceNow API connector(需要在「Expose an API」裡新增一個名為 user_impersonation 的 scope,這是 OBO 流程交換 token 時實際請求的 scope),另一個代表 AI Agent 本身(需要建立 client secret,並設定對 ServiceNow API connector 的 API 存取權限)。

在 ServiceNow 端,則要到 System OAuth 底下的 Inbound Integrations,新增一個「第三方 OIDC 身分提供者核發 ID token」的入站整合,填入剛才建立的 ServiceNow API connector 的 client ID,再設定一個 OIDC provider,指向 Entra 租戶的 metadata URL,並把使用者 claim(例如 preferred_username)對應到 ServiceNow 的 Email 欄位。文章特別提醒,如果 Entra 租戶沒有在 token 裡放 JTI,要記得關掉 JTI 驗證;Entra 本身用的是一個叫 uti 的內部 claim,等同於 JTI,可以考慮把它對應成 jti claim,增加重播攻擊防護與黑名單能力。最後要建立一個 auth scope(例如命名為 APIConnector),並把它限制在 Agent 實際需要的 API 上,例如只開放 Table API。

🧩 **AgentCore Gateway：原生支援 OBO,但要選對 MCP 版本**

完成 Entra 與 ServiceNow 的設定後,就是在 AgentCore 建立 outbound auth 設定(Build → Identity → Add Outbound Auth → Add OAuth client),選擇 Customized provider,填入 Agent 應用程式的 client ID、client secret 與 Entra 的 discovery URL,並在 Additional configurations 裡選擇 JWT authorization grant,讓 Gateway 知道要用 JWT 型的 grant type 來做 token 交換。

建立 Gateway 時(Build → Gateways → Create gateway),有個容易漏掉的關鍵設定：必須在 Additional configurations 裡選擇 MCP version 2025-11-25,因為原生 OBO 支援只在這個版本以上才有——用更早版本 MCP 建立的 Gateway,是無法事後開啟原生 OBO 的。接著設定 inbound identity 使用既有的身分提供者設定(對應 Agent 的應用程式註冊),在 JWT Authorization Configuration 填入 Agent 的 Application ID,最後新增一個指向 ServiceNow REST endpoint 的 target,並以 inline 方式定義 schema。

💡 **身分傳遞不是加密,是治理**

這個架構的價值不在於「多一層安全」,而在於讓企業既有的身分治理機制(誰能看什麼、誰做了什麼)在 Agent 自動化之後依然成立。文章也提到,正式環境下可以把身分傳遞與 Amazon Bedrock Guardrails 搭配使用,過濾有害內容並驗證 Agent 輸入輸出,兩者解決的是不同層面的風險。

🎯 **實務啟示**

如果你的團隊正在把 Agent 接進企業既有系統(ServiceNow、Salesforce 等常見 OAuth 保護的 SaaS),這篇教學給出的是一個可以直接複用的設定清單,而不是抽象架構圖:兩個 Entra 應用程式註冊、ServiceNow 的 OIDC inbound integration、以及 AgentCore Gateway 上「MCP 版本要對」這個容易踩雷的細節。對於已經在用 Entra 做內部 OBO 整合的團隊,文章也特別強調,這裡的 Entra 端設定和標準 OBO 整合並無二致,真正的新東西是 Gateway 怎麼把這條鏈路接起來。

🔗 **來源**
- 標題：ServiceNow on-behalf-of token exchange with Bedrock AgentCore Gateway
- 作者／機構：Greg Biegel, AWS
- 連結：https://aws.amazon.com/blogs/machine-learning/servicenow-on-behalf-of-token-exchange-with-bedrock-agentcore-gateway/

#AWS #BedrockAgentCore #ServiceNow #OAuth #OnBehalfOf #MicrosoftEntra #IdentityManagement #AIAgents #EnterpriseIntegration #MCP
