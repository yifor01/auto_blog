---
title: Learning Structured Reasoning via Tractable Trajectory Control
source: Apple ML
url: https://machinelearning.apple.com/research/learning-structured-reasoning
score: 89
model: google/gemma-4-31b-it:free
generated_at: '2026-07-02T19:54:43.849357'
---

📌 【Apple ML 研究】透過可控軌跡控制，讓 LLM 學會更結構化的推理模式

TL;DR：提出 Ctrl-R 框架，透過引導 RL 探索多樣化推理模式，提升語言與視覺語言模型在數學推理上的表現。

當 LLM 在思考複雜問題時，有時會出現如「wait」等代表自我驗證的詞彙，顯示出某種湧現的推理行為。但問題在於，這些高品質的推理軌跡在隨機取樣中極其稀少，傳統的強化學習 (RL) 很難保證模型能穩定習得這些多樣化的思考模式。

🤔 **隨機取樣難以捕捉稀疏的推理路徑**

在未受限的取樣過程中，複雜的推理軌跡（Reasoning Trajectories）分佈稀疏。若僅依賴標準 RL，模型往往無法有效地探索並獲取解決複雜問題所需的特定推理模式，導致模型在面對高難度任務時缺乏靈活性。

🧩 **Ctrl-R：透過軌跡控制引導探索**

為了克服上述問題，研究團隊提出了 Ctrl-R 框架，其核心理念是將「結構化推理」引入 RL 過程：

1. **主動引導 Rollout**：Ctrl-R 不再依賴純隨機取樣，而是透過可控的軌跡控制（Tractable Trajectory Control），在 Rollout 過程中主動引導模型探索對解決問題至關重要的特定推理模式。
2. **無偏估計與最佳化**：產出的行為策略（Behavior Policy）能支援準確的重要性取樣（Importance-sampling）估計，確保在進行 on-policy 最佳化時能保持無偏。
3. **權重縮放機制**：引入一個冪次縮放因子（Power-scaling factor）作用於重要性取樣權重，讓模型能選擇性地從這些探索性的、分佈外（out-of-distribution）的軌跡中學習，同時維持最佳化的穩定性。

📊 **在數學推理任務中取得一致提升**

實驗結果顯示，Ctrl-R 能讓模型有效地探索並內化先前難以獲取的推理模式。這種能力在語言模型（Language Models）以及視覺語言模型（Vision-Language Models）的數學推理任務中，均帶來了穩定的效能提升。

🎯 **實務啟示**

對於致力於提升模型推理能力的工程師而言，這項研究提供了一個重要方向：與其期待模型在隨機探索中「撞到」正確的思考路徑，不如設計一套能主動引導模型進入特定推理狀態的控制機制，並配合權重調整來平衡探索與穩定性。

🔗 **來源**
- 標題：Learning Structured Reasoning via Tractable Trajectory Control
- 作者／機構：Po-Nien Kung, Zhen Yang, Jeffrey Luo, Cheng-Fu Yang, Haikang Deng, Zi-Yi Dou, Yinfei Yang, Nanyun Peng, Zhe Gan, Kai-Wei Chang @ Apple ML / UCLA
- 連結：https://machinelearning.apple.com/research/learning-structured-reasoning

#LLM #ReinforcementLearning #StructuredReasoning #MathematicalReasoning #AppleML #RL #TrajectoryControl #VisionLanguageModels #MachineLearning #ICML
