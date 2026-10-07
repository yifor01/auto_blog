---
title: How Cornerstone OnDemand cut database diagnosis by 78% with Amazon Bedrock
source: AWS ML
url: https://aws.amazon.com/blogs/machine-learning/how-cornerstone-ondemand-cut-database-diagnosis-by-78-with-amazon-bedrock/
model: claude-code/sonnet
generated_at: '2026-10-07T22:23:57.186455'
score: 88
---

📌 資料庫故障診斷砍78%：Cornerstone 的多代理實戰

TL;DR：Cornerstone OnDemand 用 Amazon Bedrock 加 Strands Agents 打造多代理系統 Orion AI，把資料庫診斷時間從 45 分鐘壓到 10 分鐘。

半夜資料庫告警響起，工程師要手動連線 SQL Server、查系統視圖找 blocking chain、翻 log 比對慢查詢，再跨團隊交接——這套流程平均要花 45 分鐘。服務全球 140 個國家、1.4 億用戶的 Cornerstone OnDemand，用一個三人團隊、六個月時間，把這段流程重新設計成一句自然語言對話。

🤔 **四十五分鐘的人工偵錯，到底卡在哪**

在導入 Orion AI 之前，Cornerstone 的 Enterprise DataOps 團隊處於被動救火狀態：工程師要手動建立資料庫連線、跨系統查詢、交叉比對證據以形成根因假設；SRE 與資料團隊之間存在 15 分鐘的回報延遲；重複告警過多，稀釋了真正需要處理的訊號。團隊的時間大量花在「人工協調」而非真正解決問題。

🧩 **Hub-and-spoke：一個總指揮，十三個專職 agent**

Orion AI 採用 hub-and-spoke 拓撲，由一個 meta-orchestrator 負責把任務分派給 13 個領域專屬的 specialist agent，涵蓋基礎設施監控、資料庫診斷、資料庫生命週期操作、客戶分析與知識支援等。架構以 Strands Agents（AWS 的開源 agent 編排框架）為底層：Agent 類別是 specialist 與 orchestrator 共用的建構單位，工具是標上 `@tool` 裝飾器的一般 Python 函式，工具規格直接從型別提示與 docstring 推導，不需另外維護 schema；BedrockModel 包裝各 agent 使用的 Amazon Bedrock 模型，MCPClient 則負責連接外部工具伺服器。執行時，hub 透過內建的 `call_agent` 工具按名稱呼叫 specialist，每個 specialist 跑自己的工具呼叫迴圈，再把整合後的文字回傳給 hub 組裝最終回覆。

路由機制採「關鍵字優先、語意搜尋為後備」：約 80% 的查詢透過記憶體內的關鍵字快速路徑在 1 毫秒內完成判斷，無法靠關鍵字判斷意圖時才會退到 Amazon Titan Text Embeddings V2 驅動的語意搜尋；當兩者都不適用時，Amazon Bedrock Knowledge Bases 提供的 RAG 能力會檢索既有的維運文件，確保回答有據可循。記憶管理則分三層並行讀取：短期記憶存放在加密的 Amazon DynamoDB，搭配 Amazon Nova 2 Lite 非同步產生的滾動式對話摘要；長期記憶透過 Amazon Bedrock AgentCore 依使用者 ID 做跨 session 記憶，任務完成時觸發事件做摘要與整併；第三層是任務內多個 sub-agent 共用的暫存便箋。整個記憶讀取有 500 毫秒硬性逾時與 4,000 token 預算的限制，並以 LRU 快取加速。系統以容器化服務部署在 Amazon ECS 上，連線皆走 TLS，MCP token 與 REST API 授權逐次請求提供，不寫死在程式碼裡。

📊 **45 分鐘變 10 分鐘，告警量砍 65%**

| 指標 | 導入前 | 導入後 |
|---|---|---|
| 資料庫診斷時間 | 約 45 分鐘 | 約 10 分鐘（降低 78%） |
| 人工交接步驟 | 10 多個步驟 | 一次自然語言互動 |
| SRE 到資料團隊回報延遲 | 15 分鐘 | 消除 |
| 重複告警 | 每 10 則 | 剩 3–4 則送達工程師（中位數降 65%） |
| 開發投入 | — | 三人團隊、六個月交付 |

診斷之外，Orion AI 也會接手後續的補救流程：定位根因、建議修復方案，並直接建立填好資訊、指派給正確 on-call 工程師的 Jira 工單。

💡 **兩條設計原則：資料主權與深度整合**

Cornerstone 在建構 Orion AI 時堅守兩個原則：一是在 AWS 共同責任模型下用雲端原生控制機制保護資料隱私，二是與既有維運工具深度整合，讓工程師在原本協調工作的同一個 web 應用裡與 agent 互動，而不是另開一套系統。

🎯 **實務啟示**

Orion AI 展示了一個可複製的模式：用窄範圍、單一職責的 specialist agent 取代一個大而全的 agent，搭配分層記憶與關鍵字優先路由控制延遲與成本。對於正考慮將 LLM 導入維運流程的團隊，這個案例證明小團隊、短週期也能交付可量化的效率提升。

🔗 **來源**
- 標題：How Cornerstone OnDemand cut database diagnosis by 78% with Amazon Bedrock
- 作者／機構：Derek Ziehl（AWS Machine Learning Blog）
- 連結：https://aws.amazon.com/blogs/machine-learning/how-cornerstone-ondemand-cut-database-diagnosis-by-78-with-amazon-bedrock/

#MultiAgent #AmazonBedrock #StrandsAgents #DataOps #AIOps #AWS #RAG #LLMAgents #DatabaseOps #CloudComputing
