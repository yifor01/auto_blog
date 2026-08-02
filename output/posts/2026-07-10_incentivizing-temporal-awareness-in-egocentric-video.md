---
title: Incentivizing Temporal-Awareness in Egocentric Video Understanding Models
source: Apple ML
url: https://machinelearning.apple.com/research/incentivizing-temporal-awareness-egocentric
score: 101
model: google/gemma-4-31b-it:free
generated_at: '2026-07-11T08:02:49.283102'
---

📌 【Apple 研究】解決 MLLM 「無視時序」問題：用 RLVR 強化第一視角影片理解

TL;DR：提出 TGPO 演算法，透過對比「正確時序」與「隨機打亂」的幀順序，強迫模型學習時間邏輯而非空間捷徑。

當前多模態大語言模型 (MLLM) 在視覺理解上表現強勁，但在第一視角 (Egocentric) 影片分析中卻有一個致命傷：它們往往缺乏「時間意識」。模型經常依賴單幀的空間特徵（Spatial Shortcuts）來猜測答案，而忽略了事件發生的正確順序與演變過程。

🤔 **空間捷徑導致的時序推理缺失**

在第一視角影片中，推理過程高度依賴事件的先後順序。然而，現有的訓練目標缺乏對時序推理的明確獎勵，導致模型傾向於尋找畫面中的空間特徵來得出答案，而非真正理解時間上的因果關係。

🧩 **TGPO：透過對比時序順序來強化意識**

為了修正這個問題，研究團隊提出了 Temporal Global Policy Optimization (TGPO)，這是一種基於可驗證獎勵的強化學習 (RLVR) 演算法。其核心機制如下：

1. **對比生成**：模型會針對「正確時序的影片幀」與「隨機打亂順序的影片幀」分別生成輸出。
2. **獎勵校準**：透過對比這兩組輸出，推匯出經過全域性標準化 (Globally Normalized) 的獎勵訊號。
3. **導向推理**：該機制會明確獎勵那些能區分時序差異、展現時間相干性 (Temporally Coherent) 的推理過程。
4. **整合訓練**：TGPO 可與 GRPO 和 GSPO 整合，支援冷啟動 (Cold-start) 的強化學習訓練，有效抑制模型對空間捷徑的依賴。

📊 **在五大基準測試中提升因果相干性**

研究團隊在五個第一視角影片基準測試中進行實驗，結果顯示 TGPO 在以下兩方面有顯著提升：
- **時序定位 (Temporal Grounding)**：能更精準地定位事件發生的時間點。
- **因果相干性 (Causal Coherence)**：推理邏輯更符合時間演進，且效能優於先前基於 RL 的影片推理方法。

🎯 **實務啟示**

對於開發影片理解模型的工程師來說，這項研究提供了一個可擴展的思路：當模型出現「只看畫面不看順序」的傾向時，可以嘗試設計一種「對比式」的獎勵機制——將正確順序與打亂順序的結果進行對比，強迫模型學習那些必須依賴時間維度才能獲得的特徵。

🔗 **來源**
- 標題：Incentivizing Temporal-Awareness in Egocentric Video Understanding Models
- 連結：https://machinelearning.apple.com/research/incentivizing-temporal-awareness-egocentric

#ComputerVision #MLLM #ReinforcementLearning #RLVR #EgocentricVideo #TemporalAwareness #TGPO #AppleML #VideoUnderstanding #CausalReasoning
