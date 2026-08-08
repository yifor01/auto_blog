---
title: Scaling Categorical Flow Maps
source: Apple ML
url: https://machinelearning.apple.com/research/scaling-categorical-flow-maps
model: tencent/hy3:free
generated_at: '2026-08-08T06:42:51.674900'
score: 105
---

📌 【Apple ML 研究】擴展 Categorical Flow Maps：17 億參數模型實現 4 步快速生成高品質文本

TL;DR：透過自蒸餾技術，1.7B 參數的 CFM 模型能在僅需 4 步推論下，生成高熵值的高品質文本。

🎣 語言模型（LM）目前多依賴自迴歸（autoregressive）架構，但連續擴散（continuous diffusion）與流匹配（flow matching）模型正展現出巨大的潛力，能為語言建模帶來加速採樣與傾斜（tilting）等連續模態才有的優勢。

🤔 **從離散數據的連續生成問題談起**

目前的技術研究已證明，可以透過簡單的流匹配流程，在高斯分佈與 one-hot 編碼的數據分佈之間進行轉換，進而實現離散數據的連續生成。雖然 Categorical Flow Maps (CFMs) 已能在少步數（few-step） regime 下達到具競爭力的樣本品質，但過往研究的規模大多侷限在 1B 參數以下，大規模擴展（scalability）的能力仍是未知數。

🧩 **訓練 1.7B 參數模型並透過自蒸餾加速**

為了驗證規模化效能，研究團隊採取了以下技術路徑：
1. 在 2.1T tokens 上訓練一個擁有 17 億參數（1.7B）的基礎流模型（base flow model）。
2. 透過自蒸餾（self-distill）技術將其轉化為 CFM 模型。
3. 實現在僅需 4 步推論（inference steps）的情況下，生成具備多樣性且高品質的文本，同時保持接近數據層級的 token entropy（token 熵值）。

📊 **引入似然界限與基準測試評估**

研究進一步在半離散（semi-discrete）設定下，為 CFMs 引入了似然界限（likelihood bound），並證明該模型可以用於標準語言模型基準測試（LM benchmarks）的評分，其結果與離散擴散方法（discrete diffusion methods）處於同等量級。

💡 **大規模訓練的挑戰與實務建議**

在將此類模型推向大規模規模時，研究發現並總結了相關挑戰，並針對以下兩點提供了具體的實務見解（prescriptive insights）：
- 損失權重（loss weighting）的設定。
- 時間調度（time scheduling）的安排。

🎯 **實務啟示**

對於追求推論效能的語言模型開發者而言，這項研究證明了 CFM 架構在擴展至十億級參數規模時，仍能透過蒸餾技術在極短的步數內維持高品質生成，為替代傳統自迴歸架構提供了可行的路徑。

🔗 **來源**
- 標題：Scaling Categorical Flow Maps
- 作者／機構：Oscar Davis, Anastasiia Filippova, Victor Turrisi, Amitis Shidani, Pierre Ablin, Marco Cuturi, Louis Béthune @ Apple / University of Oxford
- 連結：machinelearning.apple.com/research/scaling-categorical-flow-maps

#AI #MachineLearning #NLP #FlowMatching #AppleML #GenerativeAI #DeepLearning #LLM #DiffusionModels #Research
