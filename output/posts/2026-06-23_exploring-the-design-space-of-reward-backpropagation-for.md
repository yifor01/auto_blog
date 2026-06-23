---
title: Exploring the Design Space of Reward Backpropagation for Flow Matching
source: HuggingFace Daily Papers
url: https://huggingface.co/papers/2606.11075
score: 90
model: google/gemma-4-31b-it:free
generated_at: '2026-06-23T20:28:34.395997'
---

📌 FlowBP：透過替代軌跡框架降低 Flow Matching 模型的對齊成本

TL;DR：FlowBP 透過替代軌跡框架減少記憶體使用與梯度連結，最佳化 Flow Matching 模型的獎勵反向傳播。

在 text-to-image 生成模型的對齊過程中，如何高效地將獎勵（Reward）反向傳播回模型以最佳化生成品質，一直是一個挑戰。特別是在 Flow Matching 框架下，計算路徑的複雜度往往帶來沉重的記憶體壓力。

🤔 **Flow Matching 對齊中的記憶體與梯度瓶頸**

在對齊生成模型時，傳統的反向傳播過程往往需要處理長鏈的梯度傳遞（gradient chaining），這不僅消耗大量記憶體，且在計算上極其低效。這使得在 Flow Matching 模型中實現高效的獎勵導向最佳化變得困難。

🧩 **利用替代軌跡（Surrogate Trajectory）降低開銷**

為了克服上述限制，FlowBP 提出了一套新的框架，其核心設計在於使用「替代軌跡」來處理反向傳播。

- 減少記憶體使用：透過替代軌跡框架，避免了對完整路徑的依賴。
- 簡化梯度傳遞：降低了梯度連結（gradient chaining）的複雜度，使訓練過程更為精簡。
- 跨模型通用性：根據研究，該方法在多個不同的 text-to-image 模型上均能維持效能表現。

🎯 **實務啟示**

對於開發生成模型對齊方案的工程師而言，FlowBP 提供了一種在不犧牲效能的前提下，降低記憶體成本的替代路徑。這意味著未來在微調 Flow Matching 模型時，可能不再需要極端巨大的記憶體資源即可完成獎勵對齊。

🔗 **來源**
- 標題：Exploring the Design Space of Reward Backpropagation for Flow Matching
- 連結：https://huggingface.co/papers/2606.11075

#AI #GenerativeAI #FlowMatching #RewardBackpropagation #TextToImage #ModelAlignment #DeepLearning #FlowBP #MachineLearning #Optimization
