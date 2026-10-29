---
title: How MoEngage turned over 400 APIs into agent tools with AgentCore Gateway
source: AWS ML
url: https://aws.amazon.com/blogs/machine-learning/how-moengage-turned-over-400-apis-into-agent-tools-with-agentcore-gateway/
model: claude-code/sonnet
generated_at: '2026-10-29T22:03:32.041069'
score: 95
---

📌 AWS 如何助攻 MoEngage，把 400 支內部 API 變成 Agent 工具

TL;DR：MoEngage 用 Amazon Bedrock AgentCore Gateway 把 400 支私有 API 轉為受權限管控的 agent 工具，省下約半年工程時間，新 API 上線從幾天縮短成幾小時。

當工程團隊開始打造 AI agent 時，往往會發現 agent 需要的能力早就存在，是公司內部跑了好幾年的 REST API。真正的難題從來不是「再做一個功能」，而是「怎麼讓幾百支私有 API 安全地被模型呼叫，同時不把身份驗證的決定權交給 LLM，也不讓上下文視窗被工具定義塞爆」。

🤔 **400 支 API、25 個團隊、7 個地區，卻連不上 agent**

MoEngage 是服務超過 1,350 個消費品牌的客戶互動平臺，橫跨 push、email、in-app、SMS、WhatsApp 與 RCS。產品背後是約 400 支內部 REST API，由 25 個工程團隊維護，分散在 7 個 AWS 地區的私有 VPC 中，出於資料落地（data residency）承諾，這些 API 從未對公開網路開放。能力已經在生產環境跑著，問題是如何讓 agent 安全地碰到它。

🧩 **先否決「每個團隊自己做 MCP server」**

MCP（Model Context Protocol）提供了 agent 發現與呼叫工具的標準方式，最直覺的做法是每個團隊各自架一臺 MCP server。MoEngage 評估後直接否決：超過 20 臺 MCP server 意味著 20 套要監控、修補、跟上協定演進的部署；跨領域的 agent（例如同時要讀取 campaign、查 segment、看發送數據的那種）得連上多臺 server 再自行整合；而每個團隊都要額外具備與自身產品無關的 MCP 知識。

於是 MoEngage 定下一條貫穿後續所有決策的原則：個別工程團隊不實作 MCP。團隊只需要寫好 REST API、宣告哪些操作可以變成工具，一份寫得清楚的 OpenAPI 規格就是團隊的責任終點；MCP 層則完全由 AI Platform 團隊統一擁有。這條原則立刻衍生出三個要求：一個agent只需連接一次的中央工具入口、由伺服器端強制執行的逐 agent 授權，以及不需要每接一支新 API 就重建一次的私有連線。

🧩 **四個不能妥協的限制**

評估方案前，MoEngage 先定出四個必須同時滿足的限制：

- **不能開公開端點**：內部 API 依政策必須留在 VPC 內，就算加了額外驗證也不能對外開放，否則每新增一支 API 就要跑一輪網路改動與安全審查，乘上 7 個地區後維運面會爆炸式成長。
- **身份不能是 agent 的決定**：每次內部 API 呼叫都帶著租戶、使用者、角色與資料庫情境，如果這些是模型可見的工具參數，模型可能答錯，也可能被誘導篡改，身份必須由呼叫端的服務注入，結構上就不在模型的掌控範圍內。
- **400 支工具的目錄塞不進上下文視窗**：以每支工具約 50 tokens 的 JSON schema 估算，一次完整的 tools/list 就超過 20,000 tokens，在 agent 做任何事之前就先燒掉大量 token 預算。
- **客戶端過濾不能解決問題**：像 ADK 或 MCP SDK 裡的 tool_filter，完整目錄早已經傳輸過網路，用客戶端慣例做過濾不是真正的授權邊界，不該讓一個不該看到寫入操作的 agent，連目錄都收到那些工具。

🧩 **AgentCore Gateway 怎麼接住這四個限制**

Amazon Bedrock AgentCore Gateway 是一個全託管的 MCP server：把 OpenAPI 規格註冊成 target，Gateway 會自動產生 MCP 工具並把呼叫路由到後端服務。四項特性恰好對應上述限制：

1. **OpenAPI 進，MCP 工具出**：不需要自建 MCP server，團隊維護的規格本身就是工具定義。每個操作會變成命名為 `Target___operationId` 的工具，例如 `CampaignsAPI___searchCampaigns`，規格一改工具就跟著變。
2. **Cedar 政策在目錄序列化前就先過濾**：AgentCore 的政策引擎用部分評估（partial evaluation）在 tools/list 階段就依 principal 過濾工具。每個 agent 用自己的 IAM 角色認證，Cedar 政策決定它能看到、能呼叫哪些工具，這是伺服器端的範圍限縮，不是事後的客戶端過濾。例如一個 campaign QA bot 只拿到讀取權限，寫入工具根本不會出現在它的 tools/list 回應裡。
3. **透過 Amazon VPC Lattice 的受管出口**：Gateway 經由 AgentCore 受管出口（managed egress）連到內部服務，入口則只能透過帶有私有 DNS 的 VPC 介面端點存取，沒有任何公開路徑。新增一支 API 只是加一個 target，不是改一次網路拓撲。
4. **語意搜尋作為 Gateway 內建能力**：透過 `x_amz_bedrock_agentcore_search`，agent 可以用描述任務的方式找工具，不必知道確切名稱，省去自建探索層，也順便化解了改名風險：即使 `get_segment_user_count` 改成 `get_segment_size`，搜尋「segment user count」仍能找到它，因為比對發生在描述而非識別字上。

📊 **結果：工程時間省下約半年，上線時間從天變成小時**

MoEngage 表示這個方法省下約半年的平臺工程投入，新 API 上線從過去的幾天縮短到幾小時。整個路徑中，沒有任何產品團隊寫過 MCP server 程式碼，沒有為單次整合額外佈建網路，整條路徑上也不存在公開端點。

🎯 **實務啟示**

把 MCP 層和業務邏輯層切開，由平臺團隊統一擁有協定細節，業務團隊只需交出一份乾淨的 OpenAPI 規格，是讓 agent 化改造能規模化、而不是每接一個新能力就重造一次輪子的關鍵。授權與可見性要在伺服器端的工具目錄生成階段就處理完，而不是寄望模型或客戶端「自律」。

🔗 **來源**
- 標題：How MoEngage turned over 400 APIs into agent tools with AgentCore Gateway
- 作者／機構：Nikhil Kumar（與 MoEngage 的 Shakir Khan 共同撰寫）
- 連結：https://aws.amazon.com/blogs/machine-learning/how-moengage-turned-over-400-apis-into-agent-tools-with-agentcore-gateway/

#AWS #AgentCore #MCP #AIAgents #Bedrock #APIManagement #CloudArchitecture #MoEngage #VPCLattice #AgenticAI
