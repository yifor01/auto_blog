---
title: Build visibility for Codex on Amazon Bedrock with OpenTelemetry and Amazon
  CloudWatch
source: AWS ML
url: https://aws.amazon.com/blogs/machine-learning/build-visibility-for-codex-on-amazon-bedrock-with-opentelemetry-and-amazon-cloudwatch/
model: tencent/hy3:free
generated_at: '2026-08-07T07:50:02.291073'
score: 82
---

📌 【AWS 技術分享】如何在 Amazon Bedrock 上監控 Codex 使用狀況：結合 OpenTelemetry 與 CloudWatch

TL;DR：透過在開發者工作站部署本地 OTel Collector，可在不干擾推理路徑的情況下，實現 Codex 在 Bedrock 上的全方位使用監控。

當企業從「嘗試 AI 程式碼代理」轉向「全面導入工程團隊」時，管理層關注的焦點會從「這工具好用嗎？」轉向「我們如何掌握採用率、管理消耗量、維持可靠性，並負責任地擴展存取規模？」。

🤔 **從實驗轉向規模化：監控的重要性**

當 Codex 透過 Amazon Bedrock 使用 OpenAI 模型，並透過 AWS IAM Identity Center 進行驗證時，企業需要一套機制來區分「局部實驗」與「全面採用」。例如：
- **採用率分析**：多個團隊同時增加活躍用戶，與少數用戶高消耗，代表完全不同的管理需求。
- **代理工作流（Agentic Workflows）**：透過觀察 Tool-call 活動，可以判斷代理工作流在團隊中的普及程度。
- **效能診斷**：透過請求與持續時間（Duration）指標，協助調查使用者體驗下降的原因。

🧩 **不干擾開發流程的架構設計**

此方案的核心設計理念是「不增加集中式代理（Proxy）於模型請求路徑中」，確保開發者仍能於本地直接使用 Codex。

其技術流程如下：
1. **本地收集**：開發者工作站上運行一個僅監聽 `127.0.0.1` 的本地 OTel Collector。
2. **資訊增強**：Collector 接收來自 Codex 的指標，並根據 IAM Identity Center 的身份資訊，自動注入組織層級的屬性（如：部門、團隊、成本中心）。
3. **安全傳輸**：Collector 使用 AWS Signature Version 4 (SigV4) 進行身份驗證，將批次處理後的指標發送到局部的 CloudWatch OTLP 端點。
4. **原生整合**：最終數據直接進入 Amazon CloudWatch，無需額外的 ECS 服務、負載均衡器或 VPC 複雜架構。

📊 **關鍵指標與儀表板功能**

透過部署 `CodexOnBedrock` 儀表板，工程主管可以獲得以下維度的視覺化數據：

| 指標類別 | 具體內容 |
| :--- | :--- |
| **使用量指標** | 24 小時活躍用戶總數、對話輪次（Conversation turns）、API 請求數、Token 使用量 |
| **維度細分** | 模型、Token 類型、使用者、部門、團隊、成本中心、組織、Session 來源 |
| **操作行為** | `codex.turn.tool.call` (工具調用活動) |

⚠️ **重要提醒：Token 消耗不等於帳單**

請注意，CloudWatch 中的 Token 計數是用於趨勢分析與營運行為觀察，**並非正式的結算帳單**。由於價格調整、折扣或抵免額，List-price 預估值可能與實際收費不符。若需精確的成本分攤，應使用 AWS Cost and Usage Reports (CUR) 2.0 或 Amazon Bedrock 提供的成本管理報告。

🎯 **實務部署建議與注意事項**

1. **隱私與治理**：
   - 建議針對高階主管使用「團隊/部門/成本中心」的聚合視圖。
   - 針對「個人使用者」的儀表板，應嚴格限制給系統管理、營運、安全或財務人員，並符合員工監控與數據保留政策。
   - 設計時應將 `log_user_prompt` 設為 `false`，僅收集營運指標而非原始碼或 Prompt 內容。

2. **維護指標基數（Cardinality）**：
   - 避免在維度中使用專案名稱或臨時識別碼，以免產生過多低價值序列。
   - 應先定義好組織元數據（Metadata）的標準值、所有權與更新流程。

3. **效能與成本控制**：
   - CloudWatch OTel 指標按每 GB 攝取量計費，PromQL 查詢則按掃描樣本數計費。
   - 在大規模推行前，務必審核 CloudWatch 的定價模型。

🔗 **來源**
- 標題：Build visibility for Codex on Amazon Bedrock with OpenTelemetry and Amazon CloudWatch
- 作者／機構：Claudio Mazzoni @ AWS ML
- 連結：aws.amazon.com/blogs/machine-learning/build-visibility-for-codex-on-amazon-bedrock-with-opentelemetry-and-amazon-cloudwatch/

#AI #AWS #AmazonBedrock #OpenTelemetry #CloudWatch #Codex #MachineLearning #Observability #DevOps #EngineeringManagement
