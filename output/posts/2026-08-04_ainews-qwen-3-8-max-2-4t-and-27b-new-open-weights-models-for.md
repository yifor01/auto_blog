---
title: '[AINews] Qwen 3.8 Max(2.4T) and 27B, new open weights models for Coding and
  Cowork'
source: Latent Space
url: https://www.latent.space/p/ainews-qwen-38-max24t-and-27b-new
model: tencent/hy3:free
generated_at: '2026-08-04T08:33:31.177255'
score: 95
---

📌 【Alibaba Qwen 重磅發布】2.4T 參數巨獸 Qwen 3.8 Max 登場，開源界的新天花板？

TL;DR：Alibaba 發布 2.4T 參數旗艦模型 Qwen 3.8 Max，主攻長程代理人任務與多模態推理，並承諾下週釋出開源權重。

在經歷了去年的轉型與管理層變動後，市場曾對 Qwen 能否持續提供具競爭力的模型持有疑慮。隨著 Qwen 3.8 Max 的問世，這份疑慮已蕩然無存。這不僅是一個參數規模達 2.4T 的巨型模型，更展示了 AI 在長程任務（Long-horizon）與自主協作上的驚人潛力。

🧩 **2.4T 參數規模與 MoE 架構設計**

根據第三方技術摘要，Qwen 3.8 Max 採用了大規模的混合專家模型（MoE）架構：

- 總參數規模：2.4T
- 每次 Token 啟用的參數（Active Parameters）：95B
- 啟動比率：約為 4%
- 支援能力：具備原生多模態規劃能力，視覺資訊直接整合進執行迴圈，而非僅作為輸入通道。

📊 **自主協作與長程任務的極限測試**

Qwen 3.8 Max 的設計核心在於處理需要長時間、多步驟的複雜工作流，其展示的案例包括：

- **自主編程**：具備超過 10 天的無人值守編程能力，並能建立自我演進的編程測試框架。
- **自主研究**：在 125 小時的迭代研究迴圈中，自主發明了一種新的資料選擇方法，在基準測試中超越原論文結果 2.71 分。
- **晶片設計優化**：執行完整的矽設計流程（從 RTL 編輯到實體佈局），在滿足 500 MHz 時序收斂的前提下，將閘門數量從 8,298 降至 678，並減少 81% 的晶圓面積。
- **電商策略執行**：在為期 365 天的模擬營運中，透過博弈論談判與庫存規劃，實現了 4.16 倍的投資報酬率。

🚀 **基準測試表現：直逼 Claude Opus 等頂尖模型**

在多項關鍵指標上，Qwen 3.8 Max 展示了與西方頂尖閉源模型並駕齊驅的實力：

| 測試項目 | Qwen 3.8 Max 表現 | 對比參考 |
| :--- | :--- | :--- |
| **Frontend Code Arena** | 排名第 4 (1,668 Elo) | 僅次於 Claude Opus 5 [Max] 與 Kimi K3 |
| **Vision Arena** | 排名第 2 (1,305) | 僅落後 Claude Fable 5 [High] 13 分 |
| **SWE-bench** | 87.3% | 高於 GPT-5.5 (82.6%) 與 GLM-5.2 (83.3%) |
| **Vals Index** | 66.1 (開源模型第 2 名) | 與 Claude Opus 4.7 表現持平 |

⚠️ **API 價格與可用性**

目前該模型已透過 API 提供服務，價格極具競爭力：
- 輸入：$2.00 / M tokens
- 輸出：$6.00 / M tokens
- 快取（Cached）：$0.25 / M tokens

Alibaba 同時也宣布，除了旗艦級的 3.8 Max，**Qwen 3.8-27B 也將於下週釋出開源權重（Open Weights）**。

🎯 **實務啟示**

對於工程師而言，Qwen 3.8 Max 的出現標誌著開源模型已進入「巨型稀疏模型（Giant Sparse Models）」時代。其強大的長程代理人（Agentic）能力與多模態視覺反饋，意味著未來開發者可以利用這類模型來處理更複雜的自動化工作流，例如自動化軟體工程、複雜硬體設計或長週期的商務決策，而不再侷限於單次的指令對話。

🔗 **來源**
- 標題：[AINews] Qwen 3.8 Max(2.4T) and 27B, new open weights models for Coding and Cowork
- 作者／機構：Latent Space
- 連結：https://www.latent.space/p/ainews-qwen-38-max24t-and-27b-new

#AI #LLM #Qwen #Alibaba #OpenWeights #MachineLearning #AgenticAI #Multimodal #Coding #TechNews
