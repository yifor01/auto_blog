---
title: How U Mobile built agentic telco operations with Amazon Bedrock AgentCore
source: AWS ML
url: https://aws.amazon.com/blogs/machine-learning/how-u-mobile-built-agentic-telco-operations-with-amazon-bedrock-agentcore/
model: claude-code/sonnet
generated_at: '2026-11-04T23:00:21.186558'
score: 67
---

📌 一個購買失敗的錯誤碼,背後是客戶重試 30 次的三天煎熬

TL;DR：馬來西亞電信商 U Mobile 用 Amazon Bedrock AgentCore 打造多代理客服系統,官方量測顯示部分類別工單量下降達 84.5%。

客戶想買一個數據加購包,卻一直失敗。傳統流程裡,客服人員得翻介面日誌找錯誤碼,查 BSS API 確認資格,再對照內部知識庫核對政策,全部查完才能動手寫一句回覆。這不是單一問題,是一個協調問題。馬來西亞 5G 業者 U Mobile 的資訊系統部門（ISD）針對這個痛點,打造了名為 AiDaH（AI-Driven Agentic Helpdesk）的系統。

🤔 **傳統自動化能幫你寫字,不能幫你跑系統**

U Mobile 的 IT 環境橫跨 BSS/CRM 系統、號碼可攜平臺、大數據分析、基礎設施監控工具,混合地跑在地端與雲端。在 AiDaH 之前,即使是常規診斷也得人工跨多個系統與入口網站逐一查核,每一次查核都是一次context switch,查不出來就升級給後端 IT 團隊,使用者只能等。文章指出,傳統自動化工具能幫客服寫出更好的回覆,但不能「導航多個系統、分析結果、提出修正動作」,而這正是促使團隊轉向 agentic 架構的理由。

🧩 **六層架構,把 70% 的請求擋在模型呼叫之前**

U Mobile 與 AWS 及 AWS Partner Axrail 合作,基於 Amazon Bedrock AgentCore 建構了六層架構,整個平臺部署在 Asia Pacific（Singapore）Region。員工透過 Microsoft Teams 與一個以 Amazon CloudFront、AWS WAF 保護的 web portal 互動。每個請求先經過涵蓋角色權限控管、身分驗證與 guardrails 的安全檢查,再進入成本最佳化的路由層:約 70% 的請求用確定性關鍵字比對就能解決,完全不呼叫模型;20% 交給輕量模型分類;只有 10% 真正需要完整的 orchestrator 處理。能處理這個請求的最便宜路徑,就是實際會跑的路徑。

再往下是八個涵蓋 CRM、客戶問題管理、號碼可攜、訂單與 SIM 作業、基礎設施監控、大數據分析、雲端成本管理與財務作業的專家 agent,彼此透過 Agent2Agent（A2A）協定溝通,得以委派子任務、完成單一 agent 無法獨力處理的跨系統工作流。第四層是 AgentCore Gateway,透過統一的 Model Context Protocol（MCP）介面把 U Mobile 的後端系統暴露給 agent,背後是 AWS Lambda 與 MCP 伺服器負責把 agent 意圖轉成對特定系統的呼叫。知識層則用 Amazon Bedrock Knowledge Bases 搭配 Amazon OpenSearch Serverless 向量儲存,涵蓋共用的企業知識庫與獨立的財務語料;AgentCore memory 維持跨回合的對話脈絡,Amazon DynamoDB 儲存六級角色權限模型與 session metadata。地端與雲端系統則透過 AWS Transit Gateway 與 AWS Site-to-Site VPN 的 IPsec 加密通道連接,不對外公開網路。

📊 **從 2 個試點 agent 到 150 多個營運場景**

時間軸顯示這是逐步擴張的過程:2025 年底以 2 個試點 agent 與 Amazon Bedrock Knowledge Bases 開始概念驗證;2026 年第一季,內部 IT helpdesk 以 4 個 agent、20 個營運場景上線試行;到年中擴充到三層路由與 6 個 agent;2026 年第三季,AiDaH 以 8 個 agent 正式服務 50 位 L2 客服中心與分行使用者,目前涵蓋超過 150 個記錄在案的營運場景。U Mobile 內部量測顯示,關鍵類別的工單量下降幅度最高達 84.5%。

💡 **一個實際案例:同一個錯誤,客戶重試了 30 次**

文中舉了一個生產環境案例:一位客戶回報無法購買加購包,AiDaH 追查出根本原因是錯誤碼「Subscriber has pending order」,並進一步發現這位客戶在三天內透過多個管道嘗試購買超過 30 次,每一次都被同一個待處理訂單擋下。AiDaH 在單一回應中就呈現了根本原因與修復步驟——這類調查過去得跨好幾個系統人工進行。文章也特別強調,人工決策點被保留在「對真實客戶帳戶造成變更的那一刻」:系統自行完成調查與診斷,但支援人員仍需審核確認後,動作才會真正執行。

🎯 **實務啟示**

AiDaH 的路由設計值得借鏡:不是每個請求都要丟給最貴的 orchestrator,先用確定性規則與輕量模型過濾掉大部分簡單請求,把昂貴的推理留給真正需要的那一小部分,這種分層成本控制思路對任何想落地多代理系統的團隊都適用。

🔗 **來源**
- 標題：How U Mobile built agentic telco operations with Amazon Bedrock AgentCore
- 作者／機構：Jin Tiong Lim, AWS
- 連結：https://aws.amazon.com/blogs/machine-learning/how-u-mobile-built-agentic-telco-operations-with-amazon-bedrock-agentcore/

#AgenticAI #AmazonBedrock #AgentCore #Telecom #MultiAgentSystems #A2AProtocol #AWS #CustomerSupport #RAG #CloudArchitecture
