---
title: Agentic observability with Amazon OpenSearch Service MCP Apps
source: AWS ML
url: https://aws.amazon.com/blogs/machine-learning/agentic-observability-with-amazon-opensearch-service-mcp-apps/
model: claude-code/sonnet
generated_at: '2026-08-26T06:24:15.374654'
score: 99
---

📌 觀察力代理人的「查證斷點」：AWS 用 MCP Apps 把圖表塞進聊天視窗

TL;DR：Amazon OpenSearch Service 推出 MCP Apps，讓 observability agent 的回覆直接附帶可互動視覺化，省去切換工具查證的時間。

Observability agent 反應很快，幾分鐘內就能查完 alert、關聯 log 與 trace，並產出一個根因假設。真正拖慢速度的不是查詢本身，而是「查證」：你得讀完文字摘要、打開瀏覽器、切到 trace waterfall、看 service map 確認影響範圍，再逐一比對 agent 說的和畫面上看到的是否一致。agent 省下的是查詢時間，沒省下的是你跳來跳去、重新建立上下文的時間。

🤔 **agent 生成答案只要幾秒，你的查證卻停在人類速度**

典型的調查流程是這樣的：工程師先問 agent，拿到文字型的根因假設；接著離開 IDE，打開瀏覽器登入另一個 observability UI；然後手動重跑查詢，試圖在別的工具裡重現 agent 找到的結果；比對完文字輸出與實際儀表板後，再回到 agent 對話，但這時往往已經失去調查的節奏。這個外部查證迴圈，正是拖累 agentic 自動化速度優勢的瓶頸。文章特別點出，選擇本地部署 agentic observability 的團隊本來就是為了掌控與成本效率，但這個選擇的代價是查證仍然發生在另一個獨立工具裡，速度追不上 agent 本身。

🧩 **Dual Response：文字給 agent 推理，視覺化給人類查證**

Amazon OpenSearch Service 現在支援 MCP Apps，這項能力擴充了 Model Context Protocol，讓每次 tool call 的回應同時包含兩個部分：一段結構化文字摘要，以及一個在同一個對話串中渲染的互動視覺化（trace waterfall、service topology、log pattern view）。

架構上由三個角色組成：一個跑在本機的 MCP server、你的 agentic IDE，以及 OpenSearch UI 應用程式。本機 MCP server 作為 IDE 與 OpenSearch UI 之間的安全橋樑，暴露一組 observability 工具給 AI agent 呼叫。每次 tool call 都會經過 MCP server，送到 OpenSearch UI 端點執行查詢，再把 dual response 傳回 IDE。OpenSearch UI 是一個 serverless 介面，可對接 OpenSearch domain、serverless collection、CloudWatch，以及 Amazon Managed Service for Prometheus。

一個完整的 tool call 流程如下：
1. Agent 呼叫 MCP App tool，帶入參數如 trace ID 或 service 篩選條件與時間範圍。
2. 本機 MCP server 用配置的 AWS 憑證做身分驗證，把請求轉發到 OpenSearch UI 端點。
3. OpenSearch UI 對連接的資料來源執行查詢，同時組出結構化文字摘要（trace ID、總時長、span 數量、關鍵路徑、失敗來源分析）與一個互動式視覺化 artifact（如 trace waterfall，顯示 span 層級、時間軸與錯誤標註）。
4. MCP server 把兩者打包成單一 MCP 回應，IDE host 偵測到視覺化 payload 後將其渲染成對話串中的互動元件。

因為視覺化是伺服器端直接對真實資料來源執行程式碼產生的，而不是 AI 對結果的二次詮釋，所以輸出是確定性（deterministic）的，你看到的就是實際查詢結果。

📊 **從 triage 到 trace，工具沿調查生命週期串接**

文章描述 MCP Apps 涵蓋整個調查生命週期：先由 triage 與 response 工具列出活躍告警、跨資料來源關聯相關告警並呈現嚴重程度分佈；找到受影響服務後，log 調查工具搜尋錯誤模式並將相似 log 條目聚類，鎖定失敗特徵；最後由 trace 調查工具定位具體的分散式 trace，顯示 span 層級與延遲分解，指出失敗的確切起源。

🎯 **實務啟示**

對於已經在自建本地 agentic observability 的團隊，MCP Apps 提供了一個把「查證」搬回 agent 對話串內的方式，減少工具切換造成的上下文流失。由於本機 MCP server 掌管憑證與資料存取，資料仍留在自己的 AWS 帳號內，這對重視掌控權而選擇本地部署的團隊來說是可以直接評估導入的增量能力，而非另一套需要遷移的獨立平臺。

🔗 **來源**
- 標題：Agentic observability with Amazon OpenSearch Service MCP Apps
- 作者／機構：Hang Zuo（AWS）
- 連結：https://aws.amazon.com/blogs/machine-learning/agentic-observability-with-amazon-opensearch-service-mcp-apps/

#AWS #OpenSearch #Observability #MCP #AgenticAI #DevOps #CloudWatch #Prometheus #AIAgents #SRE
