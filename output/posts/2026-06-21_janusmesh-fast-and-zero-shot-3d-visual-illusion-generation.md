---
title: 'JanusMesh: Fast and Zero-Shot 3D Visual Illusion Generation via Cross-Space
  Denoising'
source: HuggingFace Daily Papers
url: https://huggingface.co/papers/2606.20563
score: 83
model: google/gemma-4-31b-it:free
generated_at: '2026-06-21T19:50:24.580830'
---

📌 JanusMesh：透過跨空間去噪實現快速且零樣本的 3D 視覺幻象生成

TL;DR：提出一個無需訓練的框架，透過雙分支去噪與視角條件紋理合成，將文字驅動的 3D 視覺幻象生成速度大幅提升。

在 3D 視覺藝術中，「視覺幻象」（Visual Illusion）是一種迷人的現象：同一個 3D 物體在不同視角下會呈現完全不同的影像。然而，要精準控制這種「視角依賴」的生成，通常需要繁重的訓練成本與複雜的最佳化過程。

🤔 **打破 3D 幻象生成的訓練門檻**

傳統的 3D 幻象生成往往面臨訓練時間長且缺乏靈活性的問題。JanusMesh 試圖解決如何讓系統在「無需訓練（Training-free）」且「零樣本（Zero-shot）」的情況下，僅憑文字指令就能快速生成具有語義一致性的 3D 視覺幻象。

🧩 **跨空間雙分支去噪與紋理合成架構**

為了實現無縫的幾何融合與語義連貫性，JanusMesh 將生成過程解耦為兩個核心階段：

1. **跨空間雙分支去噪 (Cross-Space Dual-Branch Denoising)**：將生成過程拆分為雙分支處理，在不同空間中進行去噪，以確保 3D 結構能同時滿足多個視角的視覺需求。
2. **視角條件紋理合成 (View-Conditioned Texture Synthesis)**：根據特定視角條件合成紋理，確保最終生成的 3D 網格在不同視角切換時，能保持語義上的連貫且無縫融合。

🎯 **實務啟示**

對於從事 3D 內容創作或 AI 藝術的工程師而言，JanusMesh 的「無需訓練」特性意味著降低了部署門檻。開發者不再需要針對特定幻象效果準備大量資料集進行微調，即可快速嘗試不同的文字驅動 3D 視覺效果，這為快速原型開發與互動式 3D 藝術創作提供了新的技術路徑。

🔗 **來源**
- 標題：JanusMesh: Fast and Zero-Shot 3D Visual Illusion Generation via Cross-Space Denoising
- 連結：https://huggingface.co/papers/2606.20563

#3DGeneration #VisualIllusion #ZeroShot #ComputerVision #TextTo3D #Denoising #TextureSynthesis #GenerativeAI #JanusMesh #3DModeling
