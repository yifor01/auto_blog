---
title: Exploring self-distilled reasoning for supervised fine-tuning with Amazon Nova
source: AWS ML
url: https://aws.amazon.com/blogs/machine-learning/exploring-self-distilled-reasoning-for-supervised-fine-tuning-with-amazon-nova/
model: tencent/hy3:free
generated_at: '2026-07-22T00:44:41.197713'
score: 98
---

這篇內容屬於 **產業部落格報導（AWS ML）**，重點在於介紹 AWS 如何透過技術手段解決 SFT 過程中的推理能力缺失問題。

---

📌 【AWS 研究】解決 SFT 缺乏推理軌跡的問題：利用自我蒸餾提升 Amazon Nova 2 效能

TL;DR：透過 Self-Distilled Reasoning (SDR) 技術，利用 Base 模型產生的思考軌跡來強化 SFT 效能。

🤔 **SFT 訓練中常見的「推理缺失」困境**

在進行監督式微調（Supervised Fine-Tuning, SFT）時，若要讓模型學會複雜的推理能力，通常需要高品質的「思維鏈」（Chain-of-Thought, CoT）推理軌跡作為訓練資料。然而，手動建立這些高品質的「黃金軌跡」（Golden CoT traces）往往既不切實際且成本極高。這導致許多開發者在進行 SFT 時，被迫放棄推理過程，僅使用「輸入 → 輸出」的模式進行訓練。

🧩 **引入 Self-Distilled Reasoning (SDR) 技術**

為了在缺乏推理軌跡的資料集中實現類似的增益，研究者提出了一種稱為「自我蒸餾推理」（Self-Distilled Reasoning, SDR）的方法。

其核心設計理念如下：
1. 針對缺乏推理軌跡的 SFT 資料集，利用 Base 模型（如 Amazon Nova 2 Lite）來產生思考標記（Thinking tokens）。
2. 將這些由模型自身產生的思維鏈作為替代方案，用於訓練該模型。
3. 這種做法與「自我蒸餾」（Self-distillation）的概念一致，即在訓練過程中將資訊從模型自身蒸餾回自身。

📊 **實驗觀察：提升效能並緩解災難性遺忘**

透過在三個基準測試（Benchmarks）上的驗證，SDR 展現了以下關鍵特性：
- **提升目標效能**：引入 SDR 能有效提升模型在特定任務上的表現。
- **緩解災難性遺忘（Catastrophic Forgetting）**：在進行 SFT 時，模型往往會遺忘原有的能力，而 SDR 有助於減輕這種現象。
- **對比 Model Merging**：雖然「模型合併」（Model Merging）可以透過將 SFT 後的檢查點與 Base 模型合併來保留舊技能，但 SDR 在提升目標效能的表現上展現了不同的價值。

🎯 **實務啟示**

對於需要對 Amazon Nova 2 進行客製化（Customization）的工程師來說，如果手邊的 SFT 資料集僅有標準的輸入與輸出，沒有詳細的推理過程，可以嘗試使用 SDR 技術，利用 Base 模型產生的 CoT 來補足資料，從而解鎖模型在程式碼（Coding）與數學（Math）等高難度問題上的潛力。

🔗 **來源**
- 標題：Exploring self-distilled reasoning for supervised fine-tuning with Amazon Nova
- 作者／機構：Rushil Anirudh @ AWS ML
- 連結：https://aws.amazon.com/blogs/machine-learning/exploring-self-distilled-reasoning-for-supervised-fine-tuning-with-amazon-nova/

#AmazonNova #AWS #SFT #CoT #MachineLearning #SelfDistillation #LLM #FineTuning #AIResearch #ReasoningModels
