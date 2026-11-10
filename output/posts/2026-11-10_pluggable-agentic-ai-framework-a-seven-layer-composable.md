---
title: 'Pluggable Agentic AI Framework: A seven-layer composable enterprise agentic
  AI reference architecture on Amazon Bedrock AgentCore'
source: AWS ML
url: https://aws.amazon.com/blogs/machine-learning/pluggable-agentic-ai-framework-a-seven-layer-composable-enterprise-agentic-ai-reference-architecture-on-amazon-bedrock-agentcore/
model: claude-code/sonnet
generated_at: '2026-11-10T00:53:47.989459'
score: 97
---

📌 從原型到生產環境：Amazon Bedrock AgentCore 的七層 Agent 參考架構

TL;DR：AWS 提出可組合的七層企業級 agentic AI 參考架構，直指 PoC 撐不住生產流量的根本原因。

每個做 AI agent 的團隊,最終都會被問到同一個問題:「我們要怎麼在生產環境大規模運行這些 agent?」而 proof-of-concept 從來沒打算回答這個問題,因為它只是用來證明模型能完成任務,不是用來承受真實流量、成本壓力與安全審查。這道鴻溝,正是多數 agentic AI 專案卡住的地方。

🤔 每個團隊都在重造同一套 scaffolding

AWS 觀察到,幾乎每個建置 agent 的團隊都在重複打造自己的路由邏輯、自己的 guardrails、自己的 observability,而且往往是事後補上,而非從一開始就內建進設計裡。這篇文章提出的 Pluggable Agentic AI Framework,就是想提供一套共享的、可直接拿來組裝的生產級架構。

🧩 七層架構,各自有自己的穩定契約

- **Data and Knowledge**:agent 的能力上限就是它能存取的資料。這層負責 retrieval、embedding,以及結構化與非結構化資料的存取,契約很單純:接受一個查詢,回傳最相關的上下文。範例元件包括 Amazon Bedrock Knowledge Base、Vector Engine for Amazon OpenSearch Serverless、Amazon S3 Vectors 與 Amazon DynamoDB。
- **Model and Inference**:模型選擇應該由設定驅動,而不是寫死在 agent 或應用邏輯裡。簡單任務用小而快的模型,需要細緻推理的請求用大模型,並且要用具代表性的真實業務資料做模型評估。像 LiteLLM 這類 proxy 可以提供跨 provider 的一致介面,讓你依評估結果切換模型而不用重寫應用邏輯。
- **Orchestration**:簡單任務用單一 agent 從頭做到尾;複雜、跨領域的工作則用 supervisor 把任務分派給各自專精的 specialist agent,每個 specialist 只綁定特定能力與特定工具集。文章特別提醒,不要打造一個什麼都做的萬能 agent——context 會不斷膨脹,延遲上升,準確度下降,tool 也會氾濫到讓 agent 做出意料之外的行為。文章建議讓 specialist 嚴格限制在被授權的工具範圍內執行(bounded autonomy),並將 supervisor 與 specialist 解耦,讓 supervisor 透過集中式 agent registry 發現 specialist,再透過 MCP、A2A 這類標準協議呼叫。建議的元件是 Strands Agents 做 specialist、Amazon Bedrock AgentCore harness 做 orchestrator,以及 AWS Agent Registry 與 Amazon Bedrock AgentCore Gateway 做集中式發現與路由。
- **Security and Guardrails**:agentic AI 帶來傳統安全框架沒處理過的風險,從 prompt injection、tool misuse 到記憶體與資料中毒都有。預設把所有外部內容視為不可信,每個請求無論來自使用者、其他 agent 或自動化流程,都要透過像 Amazon Bedrock AgentCore Identity 這類服務做認證,再用細粒度存取控制判斷每次 tool 呼叫是否被允許。給 agent 的應該是暫時性的、範圍受限的憑證,而不是長期有效的密鑰。敏感資料如 PHI、PII 要在 agent 與 tool 的請求/回應中被遮罩。高影響力的操作要經過人工審核,並部署 circuit breaker 在異常行為升級前先止血,所有重大決策都要記錄在防竄改的審計軌跡裡。建議元件是 Amazon Bedrock Guardrails、Amazon Bedrock AgentCore Identity and Policy,以及 AWS 的安全與治理控制。
- **Application**:這層只負責呈現對話、把請求往下傳給 orchestration 層,刻意保持輕薄,不要把商業邏輯塞進來。文章也提到可以在這個邊界放一個輕量的 decision model,用一次呼叫就能評分出請求是否在範圍內、需不需要轉人工、是否緊急,用機率而非自由文字輸出,讓真正的 agentic loop 只在有價值時才啟動。
- **Observability**:要從第一天就監看每一層,而不是等出事才補。除了 log 與 metric 之外,端到端的 agent trace、每個請求的成本與 token 用量、first token 的時間、呼叫是否安全,都要在上線前就有延遲、錯誤率與花費的儀表板。主動監控遠比事後救火便宜。

💡 鬆耦合的核心思想

整套架構最關鍵的設計原則,是每一層都有穩定的契約,讓底層元件可以替換。文中特別強調的 orchestration 層的「解耦」最值得注意:把 supervisor 與 specialist 分開,不只是架構上好看,更直接影響你能否獨立測試、獨立擴展、獨立定義每個 agent 的安全模型。

🎯 實務啟示

這套七層架構更適合當作「落地檢查清單」來用:資料層的 retrieval 契約夠不夠穩定?model routing 有沒有跟業務邏輯耦合?orchestration 有沒有切出獨立可測試的 specialist?security 是不是在設計階段就內建,而不是上線前才補?observability 有沒有從 day one 就覆蓋所有層?把這些問題逐一對照自己的系統,通常就能看出 PoC 與生產系統之間真正缺的那一塊。

🔗 來源
- 標題:Pluggable Agentic AI Framework: A seven-layer composable enterprise agentic AI reference architecture on Amazon Bedrock AgentCore
- 作者／機構:Sindhura Palakodety(AWS Machine Learning Blog)
- 連結:https://aws.amazon.com/blogs/machine-learning/pluggable-agentic-ai-framework-a-seven-layer-composable-enterprise-agentic-ai-reference-architecture-on-amazon-bedrock-agentcore/

#AgenticAI #AWS #BedrockAgentCore #MultiAgent #AIArchitecture #LLMOps #AIObservability #AISecurity #MCP #EnterpriseAI
