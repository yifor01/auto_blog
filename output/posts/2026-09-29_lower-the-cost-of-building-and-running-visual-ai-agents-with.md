---
title: Lower the Cost of Building and Running Visual AI Agents with NVIDIA VSS Blueprint
  3.3
source: NVIDIA Developer
url: https://developer.nvidia.com/blog/lower-the-cost-of-building-and-running-visual-ai-agents-with-nvidia-vss-blueprint-3-3/
model: claude-code/sonnet
generated_at: '2026-09-29T21:47:59.880120'
score: 81
---

📌 NVIDIA VSS 3.3：一句話組裝影像 AI Agent，token 砍 80%

TL;DR：NVIDIA VSS Blueprint 3.3 同時降低開發與運算成本，讓影像 AI Agent 更容易上線。

一條果汁裝瓶產線，只靠一句自然語言描述，30 分鐘內、花費幾美元的 coding-agent 用量，就能組裝出一個會偵測溢出、自動驗證警報、還能寫班次報告的視覺 AI Agent。這是 NVIDIA 在 VSS Blueprint 3.3 中示範的場景。

🤔 視覺 AI Agent 為何又貴又難維護

NVIDIA Metropolis Blueprint for Video Search and Summarization（VSS）把 VLM（如 NVIDIA Cosmos）、LLM（如 NVIDIA Nemotron）、RAG 與 MCP 工具串接起來，將即時與錄製影片轉換成自然語言搜尋、視覺問答、經驗證的警報與自動報告。但一套真正能上線的視覺 AI 應用，往往需要同時涵蓋偵測、串流處理、事件偵測、檢索、摘要與報告等多個工作流程，這帶來三種重複出現的成本：開發成本（微服務、Kafka、Redis、Elasticsearch、Video IO and Storage 等基礎設施的選型與串接）、運算成本（每多一路串流、每個 frame window、每個 prompt 都會拉高 GPU 使用量與延遲）、以及變更成本（從 POC 走向正式環境時的維護負擔）。

🧩 兩把降低成本的鑰匙

VSS 3.3 針對開發與運算兩端分別提出解法：

- **Build Vision Agent skill（vss-build-vision-ai）**：讓 Claude Code、Codex 或任何相容 agentskills.io 的 coding agent，能用自然語言描述需求，組成兼具警報、搜尋、摘要等能力的單一應用，並可在既有部署上以「最小差量」延伸，不必重建整套堆疊。
- **Adaptive Efficient Video Sampling（Adaptive EVS）**：透過剪除畫面中與前一幀相比沒有變化區塊的視覺 token，並將 VLM 的運算批次集中在事件發生的時刻，減少冗餘的 VLM 處理。EVS 原本已以固定剪除率存在於 vLLM 與 Cosmos NIM microservice 中，VSS 3.3 的 adaptive 版本則整合進即時 VLM microservice，改為依每個 patch、每一幀動態決定要保留哪些 token。

💡 「最小差量」是如何運作的

Build Vision Agent skill 不會從零產生部署，而是從四個經驗證的開發者 profile 中挑選最接近需求的一個作為 Foundation：base（VLM 密集字幕與問答）、alerts（即時 VLM 警報或 RT-CV 偵測搭配行為分析與 VLM 警報驗證）、lvs（長影片摘要）、search（物件與影片 embedding 加上 agentic 搜尋）。接著只計算「必要的差異」：只新增或移除特定服務、只保留某能力實際會用到的服務、並讓共用角色收斂成單一實例——例如兩個都需要偵測器的能力會共用同一個偵測器，兩個都需要 Kafka 與 Elasticsearch 的能力會共用同一組訊息匯流排與 Elasticsearch 部署（各自寫入自己的索引）。當規則無法自動判斷時，系統會提出一個結構化問題，而不是自行猜測。

產出內容包含 `_builds/<name>/override.env`、`compose.yml` 與展平後的 `resolved.yml`，原始的 `deploy/docker/` 目錄不會被修改；部署前還會先顯示架構圖供檢視，再執行驗證、部署與就緒檢查。系統也會詢問是否部署 NemoClaw（內建 VSS skill 的 host-side sandbox）作為 agent harness，若選擇不要，則產生由 VSS CLI 驅動的無介面堆疊。

📊 官方揭露的數字

- 從一句 prompt 到完整部署一個裝瓶線溢出偵測 agent：30 分鐘內，幾美元的 coding-agent 用量
- Adaptive EVS 在 60 分鐘影片摘要情境下：VLM 輸入 token 減少 80%
- 同一張 GPU 上可承載的並行串流數：增加 46%

🎯 實務啟示

如果團隊正在維運多個各自獨立的影片分析 pipeline，VSS 3.3 的「共用基礎設施＋最小差量」設計思路值得參考：與其為每個新能力重建一整套 Kafka／Elasticsearch／偵測器，不如先盤點哪些角色可以收斂共用。而 Adaptive EVS 的做法也提醒工程師，VLM 的運算成本大部分浪費在「畫面沒變但仍重複編碼」上，針對這點做 token 剪除，往往比單純換更大 GPU 更划算。

🔗 來源
- 標題：Lower the Cost of Building and Running Visual AI Agents with NVIDIA VSS Blueprint 3.3
- 作者／機構：Elizabeth Goodman, NVIDIA Developer
- 連結：https://developer.nvidia.com/blog/lower-the-cost-of-building-and-running-visual-ai-agents-with-nvidia-vss-blueprint-3-3/

#NVIDIA #VisualAI #VideoAnalytics #VLM #AIAgents #EdgeAI #ComputerVision #MCP #Cosmos #GenerativeAI
