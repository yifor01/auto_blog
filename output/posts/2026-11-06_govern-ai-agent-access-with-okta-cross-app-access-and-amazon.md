---
title: Govern AI agent access with Okta Cross App Access and Amazon Bedrock AgentCore
  – Part 1
source: AWS ML
url: https://aws.amazon.com/blogs/machine-learning/govern-ai-agent-access-with-okta-cross-app-access-and-amazon-bedrock-agentcore-part-1/
model: claude-code/sonnet
generated_at: '2026-11-06T22:24:40.642058'
score: 81
---

📌 誰的 Agent 能代表誰？Okta XAA 給出三個權杖的答案

TL;DR：AWS 與 Okta 示範如何用三段式權杖鏈,讓 AI agent 的存取權限可被即時撤銷。

當一個 AI agent 能幫你讀取客戶資料、更新工單,它其實是「代表」某個人在行動。問題是,你的身分團隊要怎麼回答：這個 agent 能代表哪個人、在哪個應用程式裡行動,又要怎麼在必要時立刻擋下它?傳統的「每個應用各自 OAuth 同意」或「共用服務帳號」都無法回答這個問題。

🤔 共用服務帳號解決不了的授權問題

這正是 Amazon Bedrock AgentCore 與 Okta Cross App Access（XAA）這篇文章要解決的問題。Okta 作為身分提供者（IdP),把「哪個 agent 能代表哪個使用者」的決策收斂到自己身上：你在 Okta 註冊 agent,管理員核准它能存取的應用程式,Okta 則在每次 agent 要求代表使用者行動時評估政策。文章提到,在測試中,當管理員移除某個使用者對 agent 的指派後,Okta 在約 1 秒內就拒絕了該 agent 針對這位使用者的新請求,而已核發的權杖也會在 5 分鐘內到期失效。

🧩 Okta 決定授權,AgentCore 執行授權

這套架構把角色切得很清楚：Okta 是治理層,負責決定哪個 agent 能代表哪個使用者對哪個資源行動;Amazon Bedrock AgentCore 是執行層,負責持有 agent 的憑證,把 Okta 的決策轉換成資源端能接受的存取權杖,並讓這兩種身分都保留在權杖裡。具體用到兩個 AgentCore 能力：AgentCore runtime 驗證 Okta 核發的授權,AgentCore Identity 把授權兌換成短效期的 access token,過程中 agent 程式碼完全看不到底層憑證,權杖則保存在它的 token vault 裡。文章測得,AgentCore Identity 為一筆平均耗時約 30 秒的請求,額外增加了約 0.6 秒的延遲。

每一筆請求攜帶三種權杖,分別記錄不同的決策：ID token 代表使用者是誰,Identity Assertion JWT Authorization Grant（ID-JAG）是 Okta 的授權決定,access token 則是資源端實際接受的憑證。整套流程跑在 AgentCore runtime 上的一個任務代理與兩個 MCP 伺服器構成的架構裡:前端（BFF）以 agent 身分向 Okta 要求 ID-JAG,agent 的 client secret 存放在 AWS Secrets Manager 而非程式碼或設定檔中;AgentCore Identity 的 credential provider 負責第二次權杖交換,指向自訂授權伺服器,以 agent 身分驗證,並將 on-behalf-of grant 設為 JWT_AUTHORIZATION_GRANT,讓 AgentCore Identity 以 jwt-bearer 方式把 ID-JAG 當作 assertion 送出。文章特別提醒,Okta 把兩次交換都綁定在 ID-JAG 指名的 client 上,因此每個 Okta agent 都需要各自獨立的 credential provider：測試中如果用一個 agent 的 ID-JAG 去兌換另一個 agent 的身分,Okta 會直接拒絕,並回報 client_id 不一致的錯誤。

AgentCore runtime 會替每個 agent 建立並管理一個 workload identity。請求通過 runtime 的 JWT authorizer 後,runtime 會取得該 workload identity 對應的 workload access token 並交給你的程式碼,AgentCore Identity 接著用背後的 ID-JAG 作為交換的 assertion。文章提醒一個容易踩的坑：AgentCore Python SDK 把這個 workload access token 放在 BedrockAgentCoreContext,而不是 entrypoint 收到的請求 header 裡;他們第一版程式碼誤以為權杖會在 header 中,結果在全部 21 筆測試請求上都走錯了路,改成自行呼叫 GetWorkloadAccessTokenForJWT 並建立了第二個 workload identity。改回從 context 讀取後,問題才解決。

📊 權杖交換只花半秒,重複呼叫更快

文章實測 10 筆請求,agent 第一次呼叫兌換 ID-JAG 大約耗時半秒;針對第二個 MCP 伺服器的第二次呼叫,則直接回傳同一個權杖,中位數延遲僅 58 毫秒,而且不會重複兌換這個單次有效的 ID-JAG。只要同一使用者產生新的 ID-JAG,就會換到新的 access token,確保每筆請求都反映 Okta 最新的授權決策。

IAM 角色的設計也刻意收斂：agent 的執行角色只需要兩條政策陳述,範圍限定在該 agent 自己的 workload identity 與 credential provider（以及該 provider 的 secret),完全不需要 GetWorkloadAccessToken 的權限,因為這個權杖是由 runtime 取得,而不是 agent 本身。

⚠️ 示範程式碼,部署前要過資安與法務這一關

文章明確說明,除了 GitHub 上的 AWS 範例 08-okta-xaa-delegation-chain,其餘程式碼片段與設定僅用於說明架構概念,並非完整可直接部署的方案,實際導入前需要與資安及法務團隊確認是否符合組織的安全、法規與合規要求。

🎯 給正在設計 Agent 身分治理的團隊

這篇文章給出的參考價值在於：把「誰能代表誰」的治理決策留在既有的 IdP 裡,而不是在每個 agent 或工具裡各自重新發明一套授權邏輯。如果你的組織已經用 Okta 管理人類使用者的存取,這個三段式權杖鏈模式可以讓 agent 的身分治理延伸同一套信任根,而不是另開一套平行系統。

🔗 來源
- 標題：Govern AI agent access with Okta Cross App Access and Amazon Bedrock AgentCore – Part 1
- 作者／機構：Hammad Ausaf
- 連結：https://aws.amazon.com/blogs/machine-learning/govern-ai-agent-access-with-okta-cross-app-access-and-amazon-bedrock-agentcore-part-1/

#AmazonBedrock #AgentCore #Okta #IAM #AIAgents #ZeroTrust #IdentityGovernance #AWS #OAuth #CloudSecurity
