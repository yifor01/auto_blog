---
title: Distilled Reinforcement Learning for LLM Post-training
source: HuggingFace Daily Papers
url: https://huggingface.co/papers/2607.17247
score: 106
model: tencent/hy3:free
generated_at: '2026-07-21T08:24:27.896220'
---

📌 【研究論文】結合教師指導與 RL：DistilledRL 解決 LLM 蒸餾的知識轉移困境

TL;DR：DistilledRL 整合教師模型指導與強化學習，突破傳統蒸餾無法有效獲取新知識的限制。

🤔 **RL 與 OPD 的技術僵局**

目前大型語言模型（LLM）的後訓練（post-training）主要依賴兩大範式：強化學習（RL）與 On-policy Distillation (OPD)。然而，這兩者各有其侷限性：

- **強化學習 (RL)**：依賴粗粒度的結果監督（coarse-grained outcome supervision），導致難以進行精確的「信用分配」（credit assignment），且難以讓模型習得全新的知識。
- **On-policy Distillation (OPD)**：透過 KL 散度無條件地匹配教師模型的 Logits。這產生了一個兩難：與自己相似的教師模型提供的資訊量有限；而差異太大的教師模型則難以提供有效的指導，導致 OPD 往往侷限於「同家族模型」之間的蒸餾。

🧩 **DistilledRL：提供精細指導的整合方案**

為了克服上述問題，研究者提出了 DistilledRL，旨在將教師模型的監督整合進 RL 的目標函式中，提供精細的指導（fine-grained guidance），從而有選擇性地轉移新知識，避免無條件的模仿。

該方法包含三個核心組成部分：
1. 帶有剪裁（clipping）的反向重要性取樣（reverse importance sampling）。
2. 負樣本重設（negative sample reset）。
3. 序列層級的幾何歸一化（sequence-level geometric normalization）。

📊 **實驗證實能有效轉移「先前無法取得」的知識**

透過簡明且具解釋性的案例研究，研究證明 DistilledRL 能有效地從教師模型轉移先前學生模型所不具備的知識。

在廣泛的實驗中，無論是在「同家族」還是「跨家族」的蒸餾設定下，DistilledRL 在 Pass@1 與 Pass@k 的指標上，表現皆顯著優於標準的 RL 與 OPD。

🎯 **實務啟示**

對於需要進行模型小型化或知識轉移的工程師來說，DistilledRL 提供了一種平衡「模仿能力」與「探索新知」的新路徑，特別是在需要跨架構（cross-family）進行模型最佳化時，具有重要的應用價值。

🔗 **來源**
- 標題：Distilled Reinforcement Learning for LLM Post-training
- 連結：https://huggingface.co/papers/2607.17247

#LLM #ReinforcementLearning #Distillation #MachineLearning #NLP #PostTraining #AIResearch #DeepLearning #KnowledgeTransfer #MachineLearningEngineering
