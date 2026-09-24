---
title: Build a multi-account AI agent with AgentCore Gateway and MCP
source: AWS ML
url: https://aws.amazon.com/blogs/machine-learning/build-a-multi-account-ai-agent-with-agentcore-gateway-and-mcp/
model: claude-code/sonnet
generated_at: '2026-09-24T20:47:03.858106'
score: 87
---

📌 【AWS】多帳戶 AI Agent 怎麼查資料不搬資料？AgentCore Gateway 給出答案

TL;DR：AWS 用 AgentCore Gateway 把各部門帳戶的 MCP 伺服器整合成單一端點，讓 Agent 跨帳戶查詢卻不需複製資料。

企業裡每個團隊都把資料留在自己的 AWS 帳戶裡，理由很直接：權責清楚、範圍隔離、部署節奏各自獨立。問題是，一個只看得到單一帳戶資料的 Agent 用處有限，但要串接分散帳戶的資料，過去往往意味著複製資料或纏鬥複雜的跨帳戶 IAM 設定。AWS 在這篇技術文章中，示範了如何用 Amazon Bedrock AgentCore Gateway 搭配 Model Context Protocol（MCP）解開這個結。

🤔 **資料留在原地，只有查詢結果跨帳戶流動**

核心設計目標很簡單：資料留在原本擁有它的業務線（LOB）帳戶，一次請求只讓該次查詢需要的特定資料流出，底層資料集本身不離開所屬帳戶。作者以一個中央平臺帳戶負責跑 Agent 與 LLM 推論，各業務線帳戶各自把資料與工具包裝成 MCP 伺服器，平臺帳戶的 AgentCore Gateway 則提供一個統一端點，讓 Agent 能跨已註冊的業務線發現並呼叫工具。

🧩 **Hub-and-Spoke 架構：Gateway 是唯一入口**

整體架構分三層：中央平臺帳戶、分散的業務線帳戶，以及作為整合層的 AgentCore Gateway。平臺帳戶用 AgentCore Runtime（一個具備 session 隔離、按用量計費、內建驗證的 serverless 環境）跑 Agent，LLM 推論則透過 Amazon Bedrock 執行，讓平臺團隊能統一控管可用模型、套用 Amazon Bedrock Guardrails，並在單一計費邊界追蹤成本。

業務線團隊不會直接暴露 S3 儲存桶或資料庫，而是把資料與工具包裝成 MCP 伺服器：例如零售銀行團隊提供 get_balance、get_profile；貸款團隊提供 get_credit_score、search_lending_policies（後者查詢的是包在 MCP 伺服器裡的 Amazon Bedrock Knowledge Bases，對銀行政策 PDF 做 RAG 檢索）。這些 MCP 伺服器同樣跑在各自帳戶的 AgentCore Runtime 上，業務線團隊因此完全掌握自己要暴露什麼工具、背後跑什麼商業邏輯，只要 MCP 工具介面維持一致，就能自由更換實作而不影響平臺端的 Agent。

📊 **一次請求怎麼跨帳戶跑完全程**

當 Agent 呼叫工具時，Gateway 會從 AgentCore Identity 取得 OAuth 2.0 machine-to-machine 憑證，附加到外送請求並路由到正確的業務線 MCP 伺服器；該伺服器再對 Okta 的 OIDC 端點驗證這個 token 後才在本地處理請求。業務線的 MCP 伺服器只回傳工具產出的特定結果，不是原始資料集，這個結果再作為推論的上下文流回平臺帳戶，原始資料全程不被複製或搬遷。範例應用程式裡的追蹤面板會顯示這次請求存取了哪些業務線，以及 AgentCore 的 Policy（Cedar）授權是否有拒絕紀錄。

新增一個業務線只需要在 Gateway 加一個 target，Agent 透過 tools/list 方法自動在下一次呼叫時發現新工具，不需要改動 Agent 本身的程式碼。

💡 **生產環境的一道關鍵配置**

每個業務線的 Runtime 都會驗證進來的 OAuth token，但文章特別提醒，在生產環境中業務線團隊應設定 allowedWorkloadConfiguration，把 Runtime 呼叫限制在身分鏈確實包含 Gateway 的請求，避免有人繞過 Gateway 的 Policy 與 Cedar 授權直接存取。

🎯 **實務啟示**

這套架構把跨帳戶治理的重擔從「Agent 程式碼裡手刻」搬到「Gateway 層統一設定」：內容安全靠 Guardrails、存取控制靠 Cedar Policy、身分驗證靠 AgentCore Identity，業務線團隊只需要維護好自己的 MCP 工具介面。對已經用多帳戶模型隔離團隊資料的組織來說，這是一條不必先做資料湖整併、就能讓 Agent 跨團隊查詢的實作路徑。

🔗 **來源**
- 標題：Build a multi-account AI agent with AgentCore Gateway and MCP
- 作者／機構：Senthil Kamala Rathinam，AWS Machine Learning Blog
- 連結：https://aws.amazon.com/blogs/machine-learning/build-a-multi-account-ai-agent-with-agentcore-gateway-and-mcp/

#AWS #AgentCore #MCP #AIAgent #CloudArchitecture #MultiAccount #Bedrock #OAuth #IAM #EnterpriseAI
