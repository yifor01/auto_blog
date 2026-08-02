---
title: 'Length Value Model: Scalable Value Pretraining for Token-Level Length Modeling'
source: Apple ML
url: https://machinelearning.apple.com/research/length-value-model
score: 105
model: tencent/hy3:free
generated_at: '2026-07-21T08:25:23.588119'
---

📌 【Apple ML 研究】LenVM：將生成長度轉化為價值預估，實現 Token 等級的精準控制

TL;DR：LenVM 透過將剩餘長度建模為價值預估問題，讓 LLM 能在推理時精準預測並控制生成長度。

🤔 **長度控制是目前 LLM 的痛點**

在現代的自回歸（autoregressive）模型中，Token 是計算的基本單位。然而，生成內容的長度不僅直接影響推理成本（Inference Cost），也會影響推理效能（Reasoning Performance）。目前的處理方式大多停留在粗粒度的序列層級（Sequence-level），缺乏對 Token 等級（Token-level）的精細建模。

🧩 **LenVM：將長度預估轉化為價值估計問題**

Apple 研究團隊提出的 Length Value Model (LenVM) 提出了一個全新的框架，在每個解碼步驟（Decoding step）預測剩餘的生成長度。其核心設計理念如下：

- **問題形式化**：將長度建模視為一個「價值估計」（Value estimation）問題。
- **獎勵機制**：為每個生成的 Token 分配一個恆定的負獎勵（Constant negative reward）。
- **預測目標**：模型預測一個有界且經過折現（Discounted return）的報酬，這個報酬可以作為剩餘生成時程（Generation horizon）的單調代理指標（Monotone proxy）。
- **技術優勢**：這種設計使得監督訊號具備「無須標註（Annotation-free）」、「密集（Dense）」、「無偏（Unbiased）」且「可擴展（Scalable）」的特性。

📊 **精準匹配長度，效能與效率兼得**

透過在大型語言模型（LLM）與視覺語言模型（VLM）上的實驗，LenVM 展示了極強的推理控制能力：

- **長度匹配能力**：在 LIFEBench 的精準長度匹配任務中，將 LenVM 應用於 7B 模型後，長度得分從 30.9 大幅提升至 64.8，表現優於多款頂尖的封閉原始碼模型。
- **效率與效能的平衡**：LenVM 允許開發者在效能與效率之間進行連續控制。在 GSM8K 任務中，若限制 Token 預算為 200 個，LenVM 能維持 63% 的準確率，而僅使用 Token 預算作為基準的對照組僅有 6%。
- **長度預測能力**：模型能從 Prompt 的邊界（Prompt boundary）準確預測總生成長度。

💡 **解讀生成動態的全新視角**

除了控制長度，LenVM 的 Token 等級價值值（Token-level values）還提供了一個可解釋的視角，讓我們能觀察生成過程中的動態變化，揭示特定的 Token 如何將推理過程導向較短或較長的模式。

🎯 **實務啟示**

對於需要嚴格控制 API 成本或推理資源（如邊緣運算裝置）的工程師來說，LenVM 提供了一種在不依賴人工標註長度資料的情況下，實現 Token 等級精準控制的可能性。

🔗 **來源**
- 標題：Length Value Model: Scalable Value Pretraining for Token-Level Length Modeling
- 作者／機構：Zhen Zhang, Changyi Yang, Zijie Xia, Zhen Yang, Chengzhi Liu, Zhaotiao Weng, Yepeng Liu, Haobo Chen, Jin Pan, Chenyang Zhao, Yuheng Bu, Alkesh Patel, Zhe Gan, Xin Eric Wang @ Apple ML
- 連結：https://machinelearning.apple.com/research/length-value-model

#LLM #VLM #AppleML #LengthModeling #InferenceOptimization #TokenLevel #MachineLearning #ValueEstimation #GenerativeAI #AIResearch
