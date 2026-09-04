---
title: Designing lifecycle policies for AgentCore memory
source: AWS ML
url: https://aws.amazon.com/blogs/machine-learning/designing-lifecycle-policies-for-agentcore-memory/
model: claude-code/sonnet
generated_at: '2026-09-04T19:49:09.202171'
score: 94
---

📌 AI Agent 也需要學會遺忘：AgentCore 記憶生命週期怎麼設計

TL;DR：AWS 提供可部署的 AgentCore memory 生命週期架構，用 TTL、評分、合併三道機制解決 agent 記憶過期問題。

一個客服 agent，把四個月前就已經結案的帳單爭議，當成還在進行中的案件回覆客戶；另一個 agent 則持續給出早已被取代的部署建議，因為它的記憶裡還留著舊版 runbook。這不是想像中的邊緣案例，而是 AWS 在生產環境觀察到的真實問題：長期運作的 agent，如果沒有主動管理記憶，品質會隨時間劣化，還可能帶來合規風險。

🤔 記憶會累積，但沒有人幫它斷捨離

AWS 這篇文章提出「記憶生命週期管理」的概念：系統性地為 agent 記憶評分、合併、修剪。這套方案鎖定的是週期內會累積大量互動資料的 agent，例如客服、業務顧問、IT helpdesk bot；如果是個人助理這類低流量場景，作者建議可以先從單純的 TTL 過期與 GDPR 合規做起。

🧩 三種記憶類型，搭配三道生命週期政策

方案先建立一套共用的記憶分類，再對應到三個互補的政策，各自解決 unbounded memory 的不同失效模式：

第一道是 TTL 過期，直接刪除超過設定天數的記憶，預設 episodic memory 為 90 天。TTL 不判斷記憶是否還有用，但提供了硬上限，也是合規的必要條件；文章建議依記憶類型差異化設定，摘要型記憶 30 到 60 天過期，語意型記憶 6 到 12 個月，procedural memory 甚至可以不設 TTL。由於 AgentCore memory 本身沒有內建自動刪除的 TTL 機制，實作上是利用 ListMemoryRecords 的 BEFORE 篩選運算子，搭配系統產生的時間戳記欄位（x-amz-agentcore-memory-createdAt）取出過期記錄後刪除。TTL 修剪會排在評分與合併之前執行，避免對本來就該被清除的記憶浪費運算資源。

第二道是相關性評分，用一個三項加權公式綜合「建立時間新舊」「最後存取時間」「存取頻率」，算出 0.0 到 1.0 的分數。系統只公開一個直覺參數 pruneDays（未被存取的記憶分數低於門檻所需的大致天數），預設 pruneDays=45、threshold=0.3 時對應的 decay_rate 約為 0.02676。三個權重加總為 1.0 時分數會落在 [0.0, 1.0] 區間，且可依 agent 特性調整，例如反覆查詢同一份 troubleshooting 手冊的客服 bot，可以拉高存取頻率的權重；即時交易助理則可以拉高新鮮度權重。由於 AgentCore memory 的 API 本身沒有 lastAccessedAt 欄位，這套方案改用 AWS CloudTrail 記錄每一次 GetMemoryRecord 事件，Memory Scorer 會讀取過去 25 小時的 CloudTrail 日誌，聚合成每筆記錄的最後存取時間與次數，並將存取歷史持久化在 Amazon S3，讓頻率計算能反映真實的長期使用狀況，而不只是單日快照。

第三道是合併，在低分記憶被刪除前給它最後一次機會：透過 Amazon Bedrock 把多筆相關的 episodic memory 合併成一筆精簡的 semantic memory，例如五筆關於部署偏好的記憶合併成一筆權威事實。合併提示要求模型保留關鍵事實、去除重複，並回傳信心分數；若 Bedrock 呼叫失敗，系統會保留原始記憶不變，並記錄失敗的刪除操作供人工檢視。作者也提醒，合併本質上是有損的，LLM 摘要五筆記憶為一筆時可能遺失細節，對高風險領域建議把原始記憶歸檔到冷儲存而非直接刪除，並在正式環境中搭配 Amazon Bedrock Guardrails 過濾有害內容、用 grounding check 驗證合併結果是否忠於原始素材。

🧩 一條由 Step Functions 串起的夜間工作流

整套架構由 Amazon EventBridge 每晚觸發一個 AWS Step Functions 狀態機，依序呼叫五個 Lambda 函式：Memory Pruner（TTL 過期）、Memory Scorer（用 CloudTrail 資料做相關性評分）、Memory Consolidator（透過 Bedrock 做 LLM 合併）、Metrics Emitter（送出 CloudWatch 指標）、Run Output Writer（結果寫回 S3）；任何失敗都會路由到 Amazon SNS 主題發出告警。完整程式碼與 AWS CDK stack 已釋出在 GitHub repository。

🎯 對正在維運長期 agent 的工程師來說

這篇文章把「記憶」當成一種需要主動管理的受管資源，而不是預設無限累積的黑盒子。如果你的 agent 已經上線數月、開始出現引用過期資訊的狀況，這套 TTL、評分、合併三層架構，以及公開的 CDK 程式碼，提供了一個可以直接落地評估的起點，而不必從零設計整套記憶治理機制。

🔗 來源
- 標題：Designing lifecycle policies for AgentCore memory
- 作者／機構：Akarsha Sehwag, AWS
- 連結：https://aws.amazon.com/blogs/machine-learning/designing-lifecycle-policies-for-agentcore-memory/

#AIAgents #AmazonBedrock #AgentCore #AWS #MemoryManagement #LLMOps #StepFunctions #CloudArchitecture #AgenticAI #MLOps
