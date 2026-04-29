---
title: "QB-LIF: Learnable-Scale Quantized Burst Neurons for Efficient SNNs"
source: ChatPaper/Computer Vision and Pattern Recognition
url: https://arxiv.org/abs/2604.25688
score: 109
model: tencent/hy3-preview:free
generated_at: 2026-04-29T20:10:26.774629
---

📌 【清華等團隊】打破 1-bit 限制，SNN 也能高效處理高維資訊

你以為脈衝神經網路（SNN）只能靠堆疊時間步長來換取準確度？這篇來自浙江大學、中科大、清華大學及加州大學系統的最新研究，提出了一種名為 QB-LIF 的新架構，在極低延遲下直接超越了傳統二元 SNN 的效能天花板。

🤔 **1-bit 脈衝限制深層 SNN 的資訊吞吐量**

傳統 SNN 依賴二元脈衝（0 或 1）進行通訊，這種稀疏的 event-driven 特性雖然省電，但在短時間模擬（short simulation horizons）下，1-bit 的資訊傳輸量成了嚴重的瓶頸。當網路越深，這種資訊壓縮導致的損耗就越明顯，導致 SNN 在複雜任務上往往難以與 ANN 競爭。

🧪 **重構突發脈衝：可學習尺度的飽和量化**

研究團隊提出的 Quantized Burst-LIF (QB-LIF) 神經元，不再使用死板的預設多閾值結構，而是將「突發脈衝（Burst Spiking）」重新定義為「膜電位的飽和均勻量化」。

- **可學習尺度 (Learnable Scale)**：量化尺度不再是超參數，而是可訓練的參數，讓每一層能根據膜電位的分佈自動適應最佳的脈衝解析度。
- **硬體友好的摺疊策略**：為了不破壞 SNN 的硬體效率，他們提出了「可吸收尺度策略 (Absorbable Scale Strategy)」，在推理階段將量化尺度摺疊進突觸權重中，維持了嚴格的「僅累加 (Accumulate-only, AC)」執行範式。

 **ReLSG-ET：解決多級離散空間的優化難題**

在離散的多級脈衝空間中進行優化極具挑戰。為此，團隊設計了 ReLSG-ET（帶指數尾的整流線性代理梯度）。這種梯度函數能在突發間隔中維持穩定的梯度流，確保模型在訓練時能收斂到更好的局部最優解。

💡 **靜態與事件驅動雙贏，低延遲下效能顯著提升**

在 CIFAR-10/100、ImageNet 等靜態影像，以及 CIFAR10-DVS、DVS128-Gesture 等事件驅動數據集上的實驗顯示，QB-LIF 在超低延遲（極少的時間步）下表現優於二元及固定突發的 SNN。

關鍵在於，它既保留了 SNN 的神經形態相容性（Neuromorphic compatibility），又解決了長期以來資訊表達能力不足的問題。

⚠️ **非主流熱點，但對邊緣 AI 至關重要**

雖然 SNN 並非當前 Computer Vision 社群最熱門的顯學，但對於專注於事件型視覺（Event-based Vision）、邊緣 AI 推理以及低功耗硬體設計的工程師而言，這項研究展示了如何在保持硬體效率的前提下，大幅提升模型表現。

🎯 **邊緣計算的新思路：量化與神經形態的結合**

對於開發者來說，QB-LIF 提供了一個重要啟示：在追求低功耗與低延遲的場景下，SNN 不應只是 ANN 的配角。透過將量化技術與神經元動態結合，並針對硬體特性（如 AC 運算）進行演算法層面的優化，我們能建構出更適合邊緣設備的高效模型。

🔗 **論文連結**
📝 QB-LIF: Learnable-Scale Quantized Burst Neurons for Efficient SNNs
👤 Dewei Bai, Hongxiang Peng, Jiajun Mei, Yang Ren, Hong Qu
🏛️ Zhejiang University; USTC; Tsinghua University; UCLA; UCSD
🔗 論文：https://arxiv.org/abs/2604.25688

對於在邊緣設備上部署 AI 模型，你更看重「極致省電」還是「模型準確度」？歡迎分享你的看法 👇

#SNN #SpikingNeuralNetworks #邊緣AI #ComputerVision #清華大學 #浙江大學 #低功耗運算 #神經形態計算
