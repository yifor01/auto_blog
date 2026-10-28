---
title: Building an Agentic AI Platform on Amazon Bedrock AgentCore
source: AWS ML
url: https://aws.amazon.com/blogs/machine-learning/building-an-agentic-ai-platform-on-amazon-bedrock-agentcore/
model: claude-code/sonnet
generated_at: '2026-10-28T21:54:37.916231'
score: 97
---

📌 Agent 上線卡在哪？AWS 用 Bedrock AgentCore 蓋出企業級控制面

TL;DR：AWS 公開企業 Agentic AI 平臺藍圖，解決多團隊治理與落地的真正瓶頸。

把 agent 推上生產環境,卡關的往往不是模型或工具呼叫本身,而是周邊的一切:有多少團隊能在安全環境裡開發、誰該擁有哪個模型與工具、AgentOps 與錯誤處理要守在什麼邊界裡,以及平臺、業務線、財務團隊要怎麼跨帳戶看到成本與健康狀態。AWS 這篇文章正是針對這個「周邊問題」給出一套參考架構。

🤔 **平臺團隊與業務團隊的分工難題**

文章把管理平臺的團隊稱為 Platform team,在平臺上建置與擁有 agent 的團隊稱為 Workstream team。每個 Workstream team 都需要一條「鋪好的路」:已核准的模型與工具、短生命週期的 workload identity、隔離的 runtime 與記憶體、自動化評估、回滾機制、telemetry,以及成本歸因。問題是,當每個團隊各自拼湊這些能力時,控制措施會逐漸走偏、共用服務變成瓶頸,所有權也難以稽核。

🧩 **四個平面與 AgentCore 的模組化服務**

這套企業 Agentic AI 平臺建在 Amazon Bedrock 與 Amazon Bedrock AgentCore 之上。AgentCore 本身提供 runtime、gateway、identity、memory、policy、registry、evaluations 等模組化服務；而「Enterprise Agentic AI Platform Blueprint」在此基礎上,把企業需要的額外契約,包括所有權、帳戶邊界、軟體交付、可觀測性、成本治理與退役流程,都寫成可部署的基礎設施即程式碼(IaC)。

整套架構分成四個平面:開發者體驗、平臺控制、Workstream 執行,以及保證與維運。文章特別強調,擴充的單位是「Workstream cell」,而不是手動設定的單一 agent 或一個共用的 workload 帳戶。

組織層面,企業通常採用三種營運模式之一,此藍圖實作的是「聯邦模式」:Platform team 是樞紐,由平臺產品經理、架構師、平臺工程師、agent 維運工程師與安全治理負責人組成;Workstream team 是輻條,由 agent 開發者、業務技術負責人與 AI/ML 工程師組成,上方則是執行贊助者與 CISO。Platform team 負責定義範本、版本、政策與准入規則;每個 Workstream 帳戶則各自跑一份自己的 Runtime、Memory、Tool Gateway 實例,讓某個團隊的故障或回滾只會留在自己的邊界內。

開發者體驗平面本質上是一個經組織核准、有版本管理的 agent 範本目錄。藍圖內建了 Strands、LangGraph、CrewAI 的參考範本,只要保留相同的推理 gateway、工具 gateway、identity、政策、評估與交付契約,團隊也可以換用其他框架。應用團隊擁有 prompt、agent 邏輯、工具與評估案例;Platform team 則擁有共用控制措施與發布要求。

🧩 **帳戶拓撲與治理機制**

架構上把企業治理、共用 Platform 服務、團隊自有的執行環境分成不同帳戶層,並可整合進既有的 landing zone(預先配置好的安全多帳戶 AWS 環境)。一個組織可以同時運行多套已驗證的 Platform 環境,以及許多組 Workstream 帳戶對。文章建議先從一個具代表性的 cell 開始,驗證完 onboarding、生產環境推廣、回滾、集中可觀測性,以及「零殘留」退役流程之後,再複製這套基線。

安全上,Service control policies 用來限制 Platform 與 Workstream 帳戶的最大可用權限,但這只是補充,而非取代 IAM、gateway 授權、Guardrails、資源政策、網路控制與管線證據。藍圖會針對確切的帳戶與區域渲染並檢視「實際生效」的政策,而不是只信賴原始碼裡的意圖;任何新增或修改的組織政策,都需要先在沙箱或代表性 cell 裡跑過 soak 測試、精確的允許/拒絕測試與回滾計畫,才能大範圍套用。

交付上,由經過審查的 Platform 與 Workload 管線強制執行推廣順序,Workstream 的部署步驟沒有任何手動快速通道;Platform team 擁有發布契約,但 Workstream team 各自操作自己的管線實例與部署節奏。退役則遵循嚴格的依賴順序:先撤銷 Platform alias 授權,再撤銷 Workstream 的 Gateway 與工具角色,最後才是 Runtime、Memory 與應用資源,每一步都要驗證,最終還要用庫存清查確認零殘留資源。

⚠️ **這是參考實作,不是現成的通用解**

文章明確指出,這份儲存庫是參考實作,開發者可依需求調整;目前部署與功能是以 eu-west-1(愛爾蘭)區域為基礎,若要換元件、換區域或擴大到更廣的組織範圍,都需要自行補上對應的可用性、安全、負載、回滾、可觀測性與拆除證據。

🎯 **實務啟示**

對正在規劃企業內部多團隊 agent 平臺的工程團隊,這篇文章提供的不是新演算法,而是一套可直接參考的治理骨架:把「模型/工具核准」與「團隊自主開發」拆成兩個平面,用 Workstream cell 當作可複製的最小單位,並用管線閘門與零殘留退役把治理落實成可驗證的流程,而不是文件上的規範。

🔗 **來源**
- 標題：Building an Agentic AI Platform on Amazon Bedrock AgentCore
- 作者／機構：Omar Elkharbotly（AWS ML Blog）
- 連結：https://aws.amazon.com/blogs/machine-learning/building-an-agentic-ai-platform-on-amazon-bedrock-agentcore/

#AmazonBedrock #AgentCore #AgenticAI #AWS #EnterpriseAI #CloudArchitecture #MultiAccountAWS #MLOps #AIGovernance #PlatformEngineering
