---
title: Optimizing production agents with Amazon Bedrock AgentCore Observability
source: AWS ML
url: https://aws.amazon.com/blogs/machine-learning/optimizing-production-agents-with-amazon-bedrock-agentcore-observability/
model: tencent/hy3:free
generated_at: '2026-08-01T08:13:47.695423'
score: 83
---

📌 【AWS 技術分享】解決 AI Agent 效能瓶頸：從「能動」到「好用」的監控策略

TL;DR：利用 Amazon Bedrock AgentCore Observability 與 CloudWatch，識別並解決 Agent 執行緩慢與記憶體無限制增長問題。

當 AI Agent 從原型轉向正式生產環境時，挑戰會從「如何讓它運作」轉變為「如何保持快速與高效」。在解決了無限迴圈或工具呼叫錯誤等功能性問題後，工程師往往會遇到更隱蔽的挑戰：Agent 運作完全正確，但效能極差。

🤔 **隱形的效能殺手：回應緩慢與記憶體膨脹**

回應延遲（Latency）與無限制的記憶體增長是生產環境中最常見的營運問題。這些問題通常不會觸發錯誤警示，但會隨著時間推移侵蝕使用者信任並增加成本。

*   **回應過慢**：當使用者期待亞秒級（sub-second）回應，卻得到數秒的延遲時，即便任務成功，互動體驗也會崩潰。
*   **記憶體膨脹**：在長對話會話中，隨著 Context（上下文）不斷累積，Agent 可能會觸發 Token 限制、丟失重要資訊，甚至導致會話意外終止。

🧩 **找出效能瓶頸：從 CloudWatch 進行診斷**

要優化 Agent，必須先識別哪些請求違反了你設定的「效能預算」（Performance Budgets）。

1.  **識別高延遲請求**：透過 CloudWatch 查詢執行時間超過預定閾值（例如 3 秒）的 Agent 呼叫，並記錄其 `RequestId`。
2.  **分析執行時間線（Timeline）**：利用 OpenTelemetry trace 查看請求內部的操作序列。常見的耗時來源包括：
    *   **記憶體檢索（Memory Retrieval）**：理想狀況應在 200 毫秒內完成；若超過此時間，代表記憶體組織效率低下。
    *   **工具呼叫（Tool Invocation）**：檢查是否有特定工具導致整體流程變慢。
    *   **Token 生成**：模型生成 Token 是序列化的，生成 500 個 Token 的時間會比 100 個長得多。
    *   **序列化處理（Sequential Operations）**：檢查是否將可以並行（Parallel）執行的獨立操作，改成了一個接一個依序執行。

📊 **優化策略：將「慢」轉為「快」**

針對上述問題，可以採取以下實務手段進行最佳化：

*   **針對工具執行**：實施快取（Caching）、連接池（Connection pooling）或優化資料庫索引；若工具持續緩慢，應獨立進行效能分析。
*   **針對記憶體檢索**：
    *   將大型命名空間（Namespace）拆分為特定主題（如：偏好、歷史、領域知識）。
    *   將舊對話摘要（Summarize）成精簡條目，而非逐字儲存。
    *   為每個命名空間設定容量限制（例如：50 條近期訊息）。
*   **針對 Token 生成**：優化 Prompt，鼓勵模型提供簡短直接的回答（如 2-3 句），並增加長度限制。
*   **針對序列化處理**：將獨立的工具呼叫改為並行執行。例如：原本需要 2s + 1.5s + 1s 的序列化呼叫，改為並行後可能只需 2s，大幅降低延遲。

⚠️ **預防記憶體失控：監控會話狀態**

在長對話會話中，Token 使用量會隨對話時間線性增長。若缺乏定期的記憶體提取（Memory Extraction）與修剪（Pruning），Agent 會面臨 Context Window 耗盡的風險。

透過 CloudWatch Logs Insights 監控記憶體相關的日誌，可以發現 Agent 是否在不斷新增記憶體（如透過 `add_conversation_note` 等工具）卻沒有進行任何整合或刪減，這就是無限制增長的徵兆。

🎯 **實務啟示**

對於正在建置生產級 Agent 的工程師來說，建立「效能預算」與「監控儀錶板」至關重要。不要等到使用者抱怨才發現問題，應主動透過 CloudWatch 監控 P95 回應時間與記憶體增長趨勢，並透過並行化與摘要技術，確保 Agent 在長對話中依然保持高效。

🔗 **來源**
- 標題：Optimizing production agents with Amazon Bedrock AgentCore Observability
- 作者／機構：Joshua Lacy @ AWS ML
- 連結：https://aws.amazon.com/blogs/machine-learning/optimizing-production-agents-with-amazon-bedrock-agentcore-observability/

#AI #LLM #AWS #AmazonBedrock #MachineLearning #AgentCore #Observability #CloudWatch #SoftwareEngineering #PerformanceOptimization
