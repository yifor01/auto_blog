---
title: Govern AI agent tool access with Amazon Bedrock AgentCore Gateway
source: AWS ML
url: https://aws.amazon.com/blogs/machine-learning/govern-ai-agent-tool-access-with-amazon-bedrock-agentcore-gateway/
model: claude-code/sonnet
generated_at: '2026-08-22T06:19:10.374938'
score: 89
---

📌 AI Agent 的工具存取誰在管?AWS AgentCore Gateway 用四個階段收斂 MCP 亂象

TL;DR:AgentCore Gateway 把散落在各處 mcp.json 的憑證與工具存取,收攏成單一治理入口,依痛點分階段導入。

如果有人問你:「哪些 AI agent 能存取客戶資料?是誰授權的?憑證外洩會暴露什麼範圍?」你能在一分鐘內回答嗎?AWS 這篇技術部落格開門見山地指出,這正是他們在與客戶對談時反覆遇到的問題。

🤔 **問題:散落各處的 mcp.json**

文章描述了一個常見場景:基礎架構工程師打開同事的筆電除錯,發現設定資料夾裡有個 `mcp.json`,裡面用明文寫著正式環境資料庫密碼,旁邊還有一行註解寫著「TODO: rotate this」。當 AI agent 透過 Model Context Protocol(MCP)連接內部工具時,若缺乏集中治理,安全團隊往往完全看不到哪些 agent 正在存取內部工具、是誰授權的,以及風險暴露的範圍。

文章歸納出企業導入 MCP 時常見的五種結構性問題:憑證散落(每個本地設定檔都有密碼)、政策漂移(N×M 組設定各自演化、彼此不同步)、稽核缺口(答不出「誰在何時呼叫了什麼」)、成本不透明(支出無法歸因到團隊),以及影子 IT(未經審查就自行部署的整合)。以政策漂移為例,若一個團隊有 10 個 AI 助理連接 5 個內部 API,就得手動維護 50 組獨立憑證,一旦後端政策變動,50 個地方都要跟著改。

🧩 **解法:一個治理入口,分四個階段導入**

文章建議不要一次打造完整閘道(gateway),而是依實際痛點分階段擴充,每個階段都能獨立產生價值:

- **Scope 1(Connect,串接)**:當 MCP 憑證散落在本地設定、安全團隊毫無盤點時採用。做法是用 Amazon Cognito 簽發的 JWT 做身分驗證,搭配 AgentCore Identity 集中管理憑證,並用 Amazon CloudWatch Logs、AWS CloudTrail 啟用稽核。此階段只註冊一個低風險的 Lambda 工具(例如唯讀的工單查詢),授權維持粗顆粒度:任何通過驗證的客戶端都能呼叫任何已註冊工具。
- **Scope 2(Control,控管)**:當答不出「誰在什麼政策下呼叫了哪個工具」時採用,導入 Cedar RBAC/ABAC、PII 遮蔽、3LO 使用者同意與 DCR(動態客戶端註冊)等機制,並搭配 Amazon Bedrock Guardrails 做安全與隱私控制。
- **Scope 3(Catalog,目錄)**:當工具註冊需要走冗長工單流程、地端系統又被排除在外時採用,部署 AWS Agent Registry、Resources MCP、Open Policy Agent,並依工具做成本歸因。
- **Scope 4(Harden,強化)**:當使用者規模超過 1,000 人,卻仍缺乏斷路器(circuit breaker)、私有連線、失效轉移機制時採用,加入私有連線、治理儀表板、淘汰(deprecation)流程與跨區域容錯。

文章也提到,若組織偏好自架方案,可用 Kong Gateway、Open Policy Agent、NeMo Guardrails、LangFuse 等工具達成類似效果。

📊 **Scope 1 落地範例**

以 Scope 1 為例,文章給出具體的三階段導入節奏:第一天布建 Cognito User Pool、部署 Gateway、註冊一個低風險 Lambda 工具;第二到第三天把更新後的 mcp.json 透過 MDM 分發下去,並驗證從 token 取得、`tools/list` 到 `tools/call` 的完整路徑;第一週確認每次呼叫都能在 CloudWatch Logs 與 CloudTrail 中留下紀錄。

🎯 **實務啟示**

對正在導入 agentic 工具鏈的團隊來說,這篇文章提供了一個務實的判斷框架:不需要一開始就打造大而全的治理平臺,而是對照自己目前卡在哪個階段的痛點(串接、控管、目錄、強化),再決定該補上哪些能力。這種「依痛點漸進擴充」的思路,也適用於任何自行串接 MCP 工具鏈的團隊,即便不是使用 AWS 的方案。

🔗 **來源**
- 標題:Govern AI agent tool access with Amazon Bedrock AgentCore Gateway
- 作者／機構:Talha Chattha, AWS ML
- 連結:https://aws.amazon.com/blogs/machine-learning/govern-ai-agent-tool-access-with-amazon-bedrock-agentcore-gateway/

#AWS #BedrockAgentCore #MCP #AIGovernance #AgenticAI #ModelContextProtocol #CloudSecurity #IAM #EnterpriseAI #ToolAccess
