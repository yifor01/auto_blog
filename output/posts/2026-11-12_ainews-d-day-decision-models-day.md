---
title: '[AINews] D-Day (Decision Models Day)'
source: Latent Space
url: https://latent.space/p/ainews-d-day-decision-models-day/
model: claude-code/sonnet
generated_at: '2026-11-12T22:56:07.871679'
score: 101
---

📌 【Google】搶先 Anthropic 推出校準決策模型 Gemini Decision 1

TL;DR：Gemini Decision 1 單次打分取代逐 token 生成，宣稱比 Flash-Lite 便宜五倍。

當所有人都在等 Anthropic 推出決策模型時，這次搶先上場的卻是 Google：在 AI Engineer CODE 大會上，Sundar Pichai 與 Logan Kilpatrick 直接端出了 Gemini Decision 1，一個不生成文字、只負責打分的模型。

🤔 什麼是「決策模型」

Gemini Decisions API 背後的 Gemini Decision 1，處理的是封閉選項（closed-set）的決策任務，像是 yes/no、單選題或 rubric 評分，用一次前向傳遞直接打分，而不是像一般 LLM 那樣逐 token 生成文字。這個專案最初是 Google DeepMind 內部的原型，一個小團隊大約六週就把它做成正式的模型與 API 上線。

🧩 規格：多模態輸入、1000 道題、毫秒級延遲

Gemini Decision 1 支援 yes/no、最多 255 個選項的單選題，以及 rubric 評分，輸入可以是文字、圖片、音訊、影片或 PDF，單次請求最多處理 1000 道問題，context 長度 256K，每個答案都附上信心分數，端到端延遲約 150 到 250 毫秒。價格是每百萬輸入 token 0.10 美元，輸出完全不收費，Google 表示這大約比 Flash-Lite 便宜五倍。

📊 跟 TypeSafe Jev 1.14 的對比，各說各話

Google 自己公布的測試顯示，Decision 1 在七個共同基準中的五個勝過 TypeSafe 的 Jev 1.14，例如 JevBench 上是 92.2% 比 90.0%，而 Jev 的輸入定價是每百萬 token 0.042 美元。但獨立測試機構 Artificial Analysis 的結果比較保守：

| 指標 | Gemini Decision 1 | 對照 |
|---|---|---|
| Decision Index 總分 | 66 | 與 Elephant 9B、Jev 1.14 同分，落後 Drex Max v1.1、GLiDE v1.2 約 7 分 |
| AA-Omniscience-Decision | 66，同級最佳 | - |
| HLE-MultiChoice | 49，同級最佳 | - |
| AA-Paperclip（整份文件全對率） | 33% | Drex Max 63% |
| 每百萬任務成本 | 345 美元 | Drex Max 103 美元、Jev 156 美元 |
| 平均單題延遲 | 211 毫秒 | Jev 92 毫秒 |
| Brier score | 0.18 | - |

💡 早期採用與一個值得注意的混合架構

Stitch 用這個 API 做出一個從粗略提示到多畫面產品流程的快速設計實驗，大約 5 秒完成；LangChain 在發布當天就支援，共用與 TypeSafe 分類器相同的基礎類別。Cloudflare 在 AI Engineer 大會上展示了一種混合 agent 架構：讓快速決策模型負責工具選擇與日誌擷取，大型推理模型只負責最終診斷，在他們的 demo 中把六次 LLM 呼叫減成一次，token 用量從約 4 萬降到約 1800。

🎯 實務啟示

如果你的 agent pipeline 裡有大量分類、路由或工具選擇這類封閉選項任務，一直丟給通用 LLM 其實是在浪費延遲與成本。Cloudflare 的架構提供了一個可參考的模式：用便宜的決策模型處理高頻率的判斷，把昂貴的推理模型留給真正需要深度分析的最後一步。不過獨立評測顯示 Decision 1 在某些任務（如整份文件全對率）上還落後競品，選型前值得按自己的任務類型實測。

🔗 來源
- 標題：[AINews] D-Day (Decision Models Day)
- 作者／機構：Latent Space
- 連結：https://latent.space/p/ainews-d-day-decision-models-day/

#GeminiDecision1 #GoogleDeepMind #DecisionModels #AIAgents #LLMOps #ClassificationModel #AIbenchmark #Cloudflare #LangChain #AIInfrastructure
