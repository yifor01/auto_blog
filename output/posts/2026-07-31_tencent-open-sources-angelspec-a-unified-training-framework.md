---
title: 'Tencent Open-Sources AngelSpec: A Unified Training Framework for MTP and Block-Parallel
  Speculative Decoding on Hy3 Models'
source: MarkTechPost
url: https://www.marktechpost.com/2026/07/30/tencent-open-sources-angelspec-a-unified-training-framework-for-mtp-and-block-parallel-speculative-decoding-on-hy3-models/
model: tencent/hy3:free
generated_at: '2026-07-31T08:37:58.014963'
score: 103
---

📌 【Tencent 開源】AngelSpec：針對不同工作負載設計專門的 Speculative Decoding 訓練框架

TL;DR：AngelSpec 透過 MTP 與 Block-Parallel 兩種專門化架構，解決推論加速中「接受率」與「驗證延遲」的矛盾。

🎣 **別再用一套模型應付所有場景**

目前的 Speculative Decoding（投機採樣）研究大多試圖尋找一個在混合基準測試中表現均衡的草稿模型（drafter），但現實中的服務流量（serving traffic）並非如此單一。當面對不同性質的任務時，單一的架構往往無法同時兼顧驗證效率與接受率。

🤔 **加速效率受限於兩個反向變數**

Speculative decoding 是一種無損（lossless）的技術，由輕量級的 drafter 提議數個未來 token，再由目標模型透過 rejection sampling 在一次 forward pass 中進行驗證。其加速效果取決於兩個關鍵指標：
1. 被接受的 draft tokens 數量。
2. 完成一輪「提議—驗證」循環所需的時間。

然而，這兩個指標在不同領域中呈現反向關係：在對熵值（entropy）要求高的開放式對話中，雖然語意有效的候選序列很多，但隨著提議深度增加，接受率會快速下降；若此時生成過長的 block，反而會浪費運算資源。

🧩 **針對不同任務提供兩套互補的架構**

AngelSpec 將「工作負載的異質性」（workload heterogeneity）視為核心設計約束，並針對不同場景提供了兩套專門的架構，而非提供一個折衷的方案：

*   **針對對話場景：Autoregressive MTP (Multi-Token Prediction)**
    *   **設計理念**：對話任務中，目標模型可能從多個語意有效的續寫中挑選任何一個，導致接受率隨深度遞減。
    *   **做法**：使用 MTP 架構提出較短的候選序列，以適應這種特性。
    *   **訓練資料**：使用豐富且多樣化的對話導向資料。

*   **針對程式碼與數學推理：Block-Parallel (DFlash 系列)**
    *   **設計理念**：程式語法、重複的識別碼與形式化表達式會對未來 token 產生強大的約束力，產生較長的預測區間。
    *   **做法**：利用 block-parallel drafting 來攤提（amortize）長區間預測的成本。
    *   **訓練資料**：強化使用程式碼與數學相關的樣本。

📊 **Hy3 模型的訓練特性**

根據 README 描述，原始的 Hy3 模型在訓練時僅包含單層 MTP，且不使用遞迴式自我條件展開（recurrent self-conditioned unrolling）。雖然在推論時可以遞迴地重複使用該 block，但訓練目標並未針對長鏈條的自我生成進行準備。

🎯 **實務啟示**

對於需要部署 LLM 服務的工程師來說，AngelSpec 提示了一個重要的設計方向：不要試圖訓練一個「全能」的草稿模型，針對對話與邏輯推理這兩種截然不同的流量特性，採用專門化的訓練策略與架構，能更有效地平衡推論的接受率與計算延遲。

🔗 **來源**
- 標題：Tencent Open-Sources AngelSpec: A Unified Training Framework for MTP and Block-Parallel Speculative Decoding on Hy3 Models
- 作者／機構：Michal Sutter @ MarkTechPost
- 連結：https://www.marktechpost.com/2026/07/30/tencent-open-sources-angelspec-a-unified-training-framework-for-mtp-and-block-parallel-speculative-decoding-on-hy3-models/

#Tencent #AngelSpec #SpeculativeDecoding #LLM #MachineLearning #MTP #InferenceOptimization #OpenSource #DeepLearning #AIArchitecture
