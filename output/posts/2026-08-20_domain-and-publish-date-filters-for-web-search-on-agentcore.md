---
title: Domain and publish date filters for Web Search on AgentCore
source: AWS ML
url: https://aws.amazon.com/blogs/machine-learning/domain-and-publish-date-filters-for-web-search-on-agentcore/
model: claude-code/sonnet
generated_at: '2026-08-20T06:39:22.580572'
score: 74
---

📌 AWS AgentCore 新增網域與發布日期過濾，讓 agent 不再引用過期或不可信來源

TL;DR：Bedrock AgentCore 的 Web Search 新增執行期網域與日期過濾，server-side 強制執行、可與管理員政策疊加。

一個金融服務 agent 不該從沒經過審核的部落格取得答案依據；一個產品資訊 agent 也不該在使用者問「現在有沒有貨」時，引用三年前的價格或庫存資料。當 AI agent 用 Web Search 為回答提供依據時，組織端需要能控制 agent 查閱哪些來源、以及這些來源必須有多新。

🤔 **組織層級政策不夠用**

Amazon Bedrock AgentCore 是一個可以用任何框架或模型來建置、串接、最佳化 agent 的平臺。過去它已支援管理員層級的網域政策，但真實世界的 agent 工作負載往往需要比「整個組織適用同一套規則」更細緻的控管，例如同一個 agent 在不同任務情境下，需要動態縮小查詢範圍。

🧩 **執行期過濾：admin 與 runtime 兩層疊加**

AWS 宣布為 Bedrock AgentCore 的 Web Search 新增執行期（runtime）網域與發布日期過濾能力，隨 web-search connector 1.2.0 版本推出。這項能力讓每一次 tools/call 呼叫都能帶入 include（允許清單）或 exclude（封鎖清單）的網域列表，每個清單各自最多支援 100 個網域；也能用 ISO-8601 UTC 格式限定內容的發布日期範圍。兩種過濾條件皆為選填，若不帶入則維持既有行為，所有已索引內容都符合資格。

整個流程完全在伺服器端完成：agent 送出帶有 query 與 filters 的 tools/call，Gateway 會將執行期過濾條件與管理員層級政策合併，對 Web 索引執行過濾後的查詢，再對原始結果做合規驗證，只回傳通過驗證的結果，沒有 client-side 的過濾迴圈，也不需要額外的往返呼叫。

設計上有一個關鍵原則：執行期過濾只能縮小、不能擴大管理員設定的範圍。合併邏輯上，include 清單採「交集」，exclude 清單採「聯集」。舉例來說，若管理員允許 [a.com, b.com, c.com]，執行期呼叫又帶入 [b.com, c.com, d.com]，最終只有 b.com 與 c.com 會被搜尋，d.com 因為不在管理員清單內而被靜默捨棄；反之在封鎖清單上，只要任一層封鎖某網域，該網域就會被封鎖。當過濾條件啟用時，Web Search 會以精準度優先於召回率，無法通過過濾條件驗證的結果會直接被排除，而不是回傳未過濾的結果，因此啟用過濾後收到的結果數量可能變少，但每一筆都符合指定條件。

此次更新也將 Web Search 的服務範圍擴大到 eu-west-1（都柏林）與 ap-northeast-1（東京）兩個新的 AWS 區域，讓歐洲與亞太地區的客戶能從更接近工作負載的區域端點呼叫服務，降低延遲；AgentCore 採用零出網（zero-egress）架構，搜尋查詢不會離開 AWS，這讓有資料鄰近性要求的受監管客戶，多了一條不需跨大西洋傳輸流量的路徑。

📊 **三個實際使用情境**

素材中舉出的範例包括：法務團隊用 agent 監控 SEC 執法動態，透過 include 清單將來源限定在 sec.gov，並將日期範圍限縮在最近五週內，過濾後的結果不含任何第三方法律評論或過期文件；製藥公司法規事務團隊要求每一筆答案只能引用 FDA、NIH 或 ClinicalTrials.gov，即使某篇 WebMD 文章在查詢結果中排名第一，也不會進入模型的 context window；交易部門的 agent 用來在盤中產生股票動態摘要，過去曾發生使用者詢問「半導體股最新狀況」時，agent 引用上一季的舊分析，導致交易員根據過期資訊做出決策的問題。

🎯 **實務啟示**

對正在打造需要合規稽核的 agent（金融、醫療、法務等場景）的團隊來說，這種「管理員政策 + 執行期動態過濾」的雙層模型值得參考：把治理底線鎖在組織層級、無法被單次呼叫繞過，同時保留給個別查詢按情境縮小範圍的彈性，比起把所有規則寫死在單一層，更貼近真實世界裡不同任務對來源可信度與時效性的差異化需求。

🔗 **來源**
- 標題：Domain and publish date filters for Web Search on AgentCore
- 作者／機構：Gaurav Deshmukh, AWS ML
- 連結：https://aws.amazon.com/blogs/machine-learning/domain-and-publish-date-filters-for-web-search-on-agentcore/

#AWS #BedrockAgentCore #MCP #WebSearch #AIAgents #DataGovernance #RAG #EnterpriseAI #LLM #AgenticAI
