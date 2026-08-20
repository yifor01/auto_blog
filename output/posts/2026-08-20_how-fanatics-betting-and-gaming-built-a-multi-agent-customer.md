---
title: How Fanatics Betting and Gaming built a multi-agent customer support system
source: AWS ML
url: https://aws.amazon.com/blogs/machine-learning/how-fanatics-betting-and-gaming-built-a-multi-agent-customer-support-system/
model: claude-code/sonnet
generated_at: '2026-08-20T06:33:31.096166'
score: 90
---

📌 兩分鐘湧入 40 通詢問：Fanatics 用多代理架構撐住運彩即時客服

TL;DR：Fanatics Betting and Gaming 在 AWS 上用 Bedrock 多代理 orchestrator 架構取代決策樹聊天機器人，同時兼顧跨州法規與責任博弈合規。

NFL 季後賽或超級盃這種高流量賽事期間，客服詢問量可能在兩分鐘內湧入超過 40 通，而且每一通背後的答案都可能因客戶所在州別不同而不同。傳統以決策樹為基礎的聊天機器人在這種複雜度下難以招架，往往讓客戶感到挫折，也把成本往人工客服隊列推。

🤔 每一州規則都不一樣，還得即時抓出問題博弈徵兆

Fanatics Betting and Gaming（FBG）是 Fanatics 旗下的運彩平臺，在美國多個州營運。每個州對支付方式、儲值上限、提款時程與責任博弈要求都有各自規定，印第安納州客戶得到的答案會跟紐澤西州客戶不同。客戶詢問範圍也很廣，從交易紀錄、帳戶設定到投注規則、自我排除選項都有，沒有單一模型或知識庫能全部涵蓋。更棘手的是，營運商必須即時辨識並回應問題博弈的徵兆，這需要理解對話語境，而不只是關鍵字比對。FBG 需要一個能自主處理這種複雜度、同時清楚知道何時該轉交真人客服的系統。FBG 技術長 Ian Botts 表示：「隨著規模成長，我們知道支援體驗必須跟著進化，希望客戶能得到更快、更準確的答案，同時絕不在責任博弈或合規上妥協。」

🧩 Supervisor Agent 統籌一組專責工具

FBG 沒有做單一龐大的聊天機器人，而是設計了一套多代理系統，讓不同代理各自處理客戶互動的不同面向。客戶訊息從 FBG 手機 App 出發，經 Salesforce Einstein 作為聊天介面層，透過標準 REST 呼叫送到跑在 Amazon EKS 上的 Spring AI 服務，先驗證客戶 token，接著訊息會通過 Amazon Bedrock Guardrails 偵測 prompt injection，再由以 Amazon Nova 2 Lite 驅動的責任博弈分類代理，依合規核准的分類框架評估每則訊息，高嚴重度分類會立即連同完整對話 context 轉交真人客服。

通過這些關卡後，訊息才抵達運行 Anthropic Claude on Amazon Bedrock 的 Supervisor Agent，由它依客戶意圖決定呼叫哪些工具，包括 RAG pipeline、帳戶與交易的 Model Context Protocol（MCP）伺服器，以及轉真人客服工具，部分工具透過 MCP 呼叫、部分直接內建在服務裡，最後由 Supervisor Agent 整合各工具回應，生成自然語言答案。

💡 為什麼選 EKS、Bedrock 與 Spring AI

FBG 把整套 AI stack 跑在既有的 Amazon EKS 平臺上，MCP 伺服器與 Spring AI 服務都是 Kubernetes 服務，因為團隊在 EKS 上已有深厚的維運經驗，能沿用既有容器平臺獨立部署、擴縮並迭代每個代理；MCP 伺服器與 Spring AI 服務可以各自依需求擴縮，要新增業務領域或功能時，加一個新 MCP 伺服器只是多一個 Kubernetes 部署，個別工具也能單獨更新而不必重新部署整個系統。選擇 Amazon Bedrock，是看中它 model-agnostic 的單一 API，能讓每項任務配對最適合的模型、也方便日後替換更好的模型，且因為 Bedrock 跑在 FBG 既有 AWS 環境內，系統自動繼承既有的安全與治理控管，Amazon Bedrock Guardrails 則提供合規要求的責任 AI 防護。至於應用框架選 Spring AI，是因為團隊本身有深厚的 Java 經驗，能藉此快速推進，Spring AI 也原生支援 MCP；文中也指出，若團隊主力是 Python，AWS 的開源 SDK Strands Agents 提供類似的 agent 協調與 MCP 支援可作替代。

🎯 模組化是能快速迭代的關鍵

FBG 軟體工程資深經理 Luis Fernandez Rocha 提到：「我們把系統設計成每個代理都有明確職責、可以獨立改進，這種模組化讓我們能快速行動，需要支援新的案例類型或新的業務單位時，只要加一個新工具或代理，不用動到系統其他部分。」對於想做類似客服系統的團隊，這個案例的參考價值在於：用 orchestrator 模式加 MCP 標準化工具通訊協定，讓新增能力不必牽動核心系統；並在高風險分類（如問題博弈徵兆）上，讓專責分類代理直接觸發帶完整 context 的人工轉接，而不是讓 Supervisor Agent 自行判斷。

🔗 來源
- 標題：How Fanatics Betting and Gaming built a multi-agent customer support system
- 作者／機構：Parker Bradshaw，AWS Machine Learning Blog
- 連結：https://aws.amazon.com/blogs/machine-learning/how-fanatics-betting-and-gaming-built-a-multi-agent-customer-support-system/

#MultiAgent #AmazonBedrock #MCP #CustomerSupport #SportsBetting #AmazonEKS #RAG #ResponsibleGaming #GenAI #LLM
