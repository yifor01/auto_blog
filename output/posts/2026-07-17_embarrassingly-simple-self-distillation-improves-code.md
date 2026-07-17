---
title: Embarrassingly Simple Self-Distillation Improves Code Generation
source: Apple ML
url: https://machinelearning.apple.com/research/simple-self-distillation
score: 98
model: tencent/hy3:free
generated_at: '2026-07-17T08:07:58.099504'
---

📌 【Apple ML 研究】只用自身輸出微調，LLM 程式碼生成大幅進步

TL;DR：Apple ML 提出簡單自蒸餾（SSD），不需驗證器或 RL，讓 Qwen3-30B 在 LiveCodeBench 提升近 13%。

當多數人認為提升 LLM 程式碼能力得靠強化學習或外部驗證器，Apple ML 的研究卻指出：模型自己的原始輸出，就足以讓它變更強。

🤔 **不靠老師模型、驗證器或 RL 也能自我提升？**

這篇論文提出一個反直覺的問題：一個大型語言模型（LLM）能否只用自己的原始輸出，在沒有 verifier、teacher model 或 reinforcement learning 的情況下，改善 code generation 能力？作者的答案為肯定，方法稱為 simple self-distillation（SSD，簡單自蒸餾）。

🧩 **SSD 的做法：取樣自身解法再標準 SFT**

SSD 的流程相當直覺，一筆資料的處理路徑如下：
- 用模型本身以特定的 temperature 與 truncation 設定，對題目取樣出多組解決方案（solutions）。
- 直接把這些取樣出的樣本，以標準的 supervised fine-tuning（SFT）方式對原模型做微調。

也就是說，訓練資料完全來自模型自己，不引入任何外部標註或更強模型。

📊 **Qwen3-30B 在 LiveCodeBench v6 從 42.4% 漲到 55.3%**

README 指出，SSD 將 Qwen3-30B-Instruct 在 LiveCodeBench v6 的 pass@1 從 42.4% 提升至 55.3%。
- 增益主要集中在較困難的問題上。
- 此方法可泛化到 Qwen 與 Llama 系列，涵蓋 4B、8B、30B 規模，同時包含 instruct 與 thinking 變體。

🤔 **為什麼這麼簡單會有效？**

作者追蹤這些增益來源，歸因於 LLM decoding 中的 precision-exploration conflict（精確度與探索的衝突）。SSD 會以 context-dependent 的方式重塑 token 分佈：
- 在需要精確的情境，抑制 distractor tails（幹擾尾部）。
- 在需要探索的情境，保留有用的多樣性。

💡 **作為現有後訓練的互補方向**

作者將 SSD 定位為改善 LLM code generation 的一個 complementary post-training direction（互補的後訓練方向），而非取代既有方法。

🎯 **實務啟示**

對工程師而言，若手邊有已經能跑出可用程式碼的 LLM，不需要搭建驗證管線或 RL 框架，只要用模型自身取樣結果做一輪 SFT，就可能低成本換來明顯的硬題效能提升，特別適合資源有限、想榨乾既有多語言模型的團隊。

🔗 **來源**
- 標題：Embarrassingly Simple Self-Distillation Improves Code Generation
- 機構：Apple ML
- 連結：https://machinelearning.apple.com/research/simple-self-distillation

#LLM #CodeGeneration #SelfDistillation #SFT #AppleML #Qwen #Llama #LiveCodeBench #PostTraining #PrecisionExploration
