---
title: 'GLM-5.3 vs. GLM-5.3 Flash on DeepSWE: Cost, Coding, and Routing'
source: Together AI
url: https://www.together.ai/blog/glm-5-3-vs-glm-5-3-flash-on-deepswe-cost-coding-and-routing
model: claude-code/sonnet
generated_at: '2026-08-29T12:03:03.776942'
score: 87
---

📌 GLM-5.3 Flash 先發、必要再升級，成本降57%

TL;DR：Together AI 實測顯示，先跑 GLM-5.3 Flash、測試沒過再升級全模型的 cascade 策略，比單獨用全模型更省錢又更準。

把一個模型的價格砍到十七分之一，你猜品質會掉多少？答案是：遠比你想的少，而且掉的還不是你以為的那個能力。

🤔 **同一個家族，兩種尺寸**

GLM-5.3 與 GLM-5.3 Flash 是同一個模型家族的兩種規模：GLM-5.3 是完整的開放權重模型，Flash 則是經過蒸餾（distillation）的精簡版，每次執行（rollout）成本只有全模型的十七分之一。Together AI 在 DeepSWE 這個涵蓋多種程式語言與任務類型的軟體工程能力基準上，對兩者各跑了 113 個任務、每個任務 4 次試驗，總計 900 次 rollout（全模型 452 次、Flash 448 次），逐項比較兩者的表現落差。

📊 **關鍵數據：品質差距比你想的小**

| 指標 | GLM-5.3（完整版） | GLM-5.3 Flash |
|---|---|---|
| pass@1 | 69.0% ± 2.7 | 63.4% ± 4.1 |
| 平均成本／次 | $3.99 | $0.24 |
| $100 可解任務數 | 17 | 264 |
| 平均輸出 token | 80k | 73k |
| 平均步數 | 125 | 123 |

單次嘗試（pass@1）全模型領先 5.6 個百分點，但這個差距會隨著多次嘗試迅速收斂：pass@2 縮小到 4 個百分點，pass@4 只剩 2.6 個百分點（87.6% 對 85.0%）。若把兩個模型組成 cascade（先跑 Flash，測試不過再升級全模型），可以解出 80.9% 的任務、平均每題只要 $1.70；相較之下單獨用全模型是 69.0%、每題 $3.99——多解 12 個百分點，成本卻低了 57%。

💡 **蒸餾拿走的是穩定性，不是能力**

Together AI 進一步把任務依表現分成「完全解不出」「時好時壞」「穩定解出」三類，發現全模型能穩定解出（4 次全過）的 48 個任務，沒有一個在 Flash 上變成完全解不出；全模型至少解出過一次的 99 個任務中，Flash 仍能解出 93 個，覆蓋率達 94%。換句話說，蒸餾沒有真正刪除模型解題的能力，而是削弱了它的可靠度——這正是為什麼 pass@1 的差距遠大於 pass@4。

更值得注意的是「用力思考」這件事：在全模型表現時好時壞的任務裡，跑得比較久的那次有 61% 機率是成功的一次，代表它能靠額外的推理步驟把難題解出來；同樣情境下 Flash 只有 46%，甚至低於丟硬幣的機率——意味著 Flash 跑得再久，也不太能把握把一個原本失敗的嘗試扳回來。這個落差不是因為 Flash 亂跑，它的步數變異係數（0.12）其實比全模型（0.14）還低，只是「多想一下」對它幫助有限。

從領域細分來看，Flash 並非全面落後：在並行與持久性（concurrency and durability）任務上反而多贏 8 分（62→70），Python 多贏 5 分，資料建模多贏 4 分；但在 JavaScript、查詢與設定、狀態式反應（stateful reactivity）、Rust 與語言底層機制上則讓出優勢。整體來說，全模型仍拿下較多語言與領域的勝場，但差距並非一面倒。

⚠️ **唯一真正的退步：更容易誤傷原本過關的測試**

有一項數據沒有站在 Flash 這邊：Flash 在已經通過的基準測試上，有 6.9% 的機率反而把它弄壞，全模型則是 4.4%。這代表用 Flash 時最好額外加一道回歸測試（regression run）把關，避免它在修好一個問題的同時悄悄破壞另一個。

🎯 **實務啟示**

這份報告本質上比較像是一次成本工程實驗，而非全新方法上的突破：它驗證的是「先用便宜模型、失敗再升級」這個簡單 cascade 策略在實際任務上真的划算。對正在設計 agent 流程或 CI 自動修復管線的工程師來說，與其糾結該選哪一個模型，不如考慮把 Flash 當預設執行者、只在測試判定失敗時才呼叫全模型，同時務必替 Flash 的輸出補上回歸測試這一關。

🔗 **來源**
- 標題：GLM-5.3 vs. GLM-5.3 Flash on DeepSWE: Cost, Coding, and Routing
- 作者／機構：Together AI
- 連結：https://www.together.ai/blog/glm-5-3-vs-glm-5-3-flash-on-deepswe-cost-coding-and-routing

#GLM53 #OpenWeightModels #LLMBenchmark #DeepSWE #ModelDistillation #AICost #CodingAgents #TogetherAI #SoftwareEngineering #AIInference
