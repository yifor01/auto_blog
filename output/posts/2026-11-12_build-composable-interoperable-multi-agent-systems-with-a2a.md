---
title: Build composable, interoperable multi-agent systems with A2A on AWS
source: AWS ML
url: https://aws.amazon.com/blogs/machine-learning/build-composable-interoperable-multi-agent-systems-with-a2a-on-aws/
model: claude-code/sonnet
generated_at: '2026-11-12T23:01:44.264242'
score: 90
---

📌 AWS 實測:用 A2A 協議串接兩個不同框架、不同帳戶的 AI Agent

TL;DR:AWS 用一個部署好的參考架構證明,LangChain 與 Strands Agents 寫的 agent 可以跨組織、跨框架協作,且不用共享任何密鑰。

多代理系統聽起來很美好,直到你發現對方公司的 agent 是用別的框架寫的,而你完全不想把自己的系統 prompt、工具清單或模型選擇暴露給對方。這正是跨組織多代理協作的現實痛點,AWS 這篇文章用一個實際部署的三 agent、雙帳戶架構,示範 Agent-to-Agent(A2A)協議怎麼解決這個問題。

🤔 問題:沒有共同語言,跨組織協作就得客製整合

當多代理系統跨越組織邊界,各方的 agent 需要互相發現、溝通、交換任務,卻不能暴露內部實作,也不能要求對方換成同一套框架。沒有 A2A 之前,軟體供應商(ISV)只能對每個客戶、每套框架寫一份客製整合程式。A2A 現在已經是 Linux Foundation 的專案,AWS 是支持者之一,協議本身建立在既有的 OAuth 2.0 與 OpenID Connect(OIDC)認證標準之上,這篇文章延續 AWS 先前「Open Protocols for Agent Interoperability」系列中介紹的 Agent Card 發現機制與 A2A server 模式,把場景推進到真正的跨組織、跨框架情境。

🧩 架構:三個 agent、兩個帳戶,只交換公開資訊

這套參考架構把三個 agent 分在兩個 AWS 帳戶:企業端與 SaaS 供應商端各自擁有自己的 Amazon Cognito user pool,各自用自己的身分提供者認證。

- Enterprise Orchestrator:企業端的使用者入口,用 LangChain 搭配 Amazon Bedrock 的 Anthropic Claude Sonnet 4.6。它在啟動時會從 SaaS agent 的 well-known URL 抓取 Agent Card,並為卡片上描述的每個技能自動建立對應的 LangChain 工具,讓模型自行決定呼叫哪個工具,完全不需要寫死的路由邏輯。使用者透過只接受企業自家 token 的 Amazon API Gateway HTTPS 端點連進來。
- Enterprise Context Agent:同樣用 LangChain,但搭配 Amazon Nova Lite,提供內部帳戶中繼資料,例如政策規則、資料分類、業務重要性、值班升級聯絡人。這個 agent 用官方 a2a-sdk(AgentCard、AgentExecutor 與符合規範的 JSON-RPC 路由),固定在 a2a-sdk[http-server]==1.2.2 版本。
- Compliance SaaS Agent:跑在 SaaS 供應商自己帳戶的 Amazon Bedrock AgentCore 上,用 Strands Agents SDK 建構,依照企業自訂的內部政策(例如正式環境不可有公開儲存空間、機密資料需靜態加密)去掃描帳戶。文章中這部分用的是模擬合規發現的合成資料。

企業端的兩個 agent 都跑在 Amazon ECS + AWS Fargate、VPC 私有子網路裡,沒有公開 IP。雙方在 onboarding 階段只交換身分提供者 URL、client ID、scope、端點 URL 這些公開值,之後互相信任彼此 user pool 發出的 token,全程不共享任何密鑰。

💡 真正的對等關係:SaaS agent 也會「回頭問」企業端

這個設計最有意思的地方是雙向性:SaaS 合規 agent 在開始掃描前,會先呼叫企業端的 Context Agent 詢問哪些帳戶是正式環境、適用哪些內部政策、該升級給誰,這個 callback 只會打到客戶在 onboarding 時登記的那個位址。這讓兩個 agent 變成真正的對等關係,而不是單純的 client 對 server。企業端完全看不到 SaaS agent 的內部工具、系統 prompt 或模型選擇,SaaS card 只公開一個整理過的技能,不會暴露內部工具名稱——這意味著 ISV 可以隨意改動內部架構,只要 Agent Card 與 A2A 介面維持相容即可。

文章也特別澄清 A2A 與 MCP 的分工:MCP 是 agent 連接自己工具和資料來源的 client-server 模型,A2A 則是 agent 對 agent 的對等協作,雙方都不暴露內部。在正式環境中,SaaS agent 可以對內用 MCP 接自己的掃描工具,對外仍透過 A2A 暴露同一個介面。

⚠️ 部署前要知道的成本與流程

整套系統透過三份依序執行的 Jupyter notebook 部署:Notebook 1(企業帳戶,約 3 分鐘)建立企業身分並寫入 onboarding 請求;Notebook 2(SaaS 供應商帳戶,約 5 分鐘)部署合規 agent 並寫入 onboarding 回應;Notebook 3 執行端對端測試驗證部署。常駐資源包括 NAT gateway、兩個 Fargate 任務、內部 Network Load Balancer、兩個 VPC 介面端點,再加上 Bedrock 與 Bedrock AgentCore 按用量計費,費用依地區而異,用完記得執行 Clean up 步驟。

🎯 實務啟示

這篇文章的價值不在 A2A 協議本身(協議本身已是 Linux Foundation 的開放標準,並非 AWS 原創),而在於它把跨組織、跨框架、雙向 OAuth 這些「說起來容易做起來難」的細節,落地成一份可以直接照抄的參考架構。如果你的團隊要對外(客戶、夥伴或用不同框架的內部團隊)開放 agent 能力,這套「只交換公開端點資訊、各自認證各自的 token、新增技能只需註冊 Agent Card」的模式,值得直接拿來當起點。

🔗 來源
- 標題:Build composable, interoperable multi-agent systems with A2A on AWS
- 作者/機構:Amit Chaudhary(AWS ML Blog)
- 連結:https://aws.amazon.com/blogs/machine-learning/build-composable-interoperable-multi-agent-systems-with-a2a-on-aws/

#A2A #MultiAgentSystems #AWS #LangChain #StrandsAgents #AmazonBedrock #AgentCore #OAuth #AgentInteroperability #CloudArchitecture
