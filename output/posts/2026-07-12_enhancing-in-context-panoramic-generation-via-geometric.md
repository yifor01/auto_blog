---
title: Enhancing In-context Panoramic Generation via Geometric-aware Pretraining
source: HuggingFace Daily Papers
url: https://huggingface.co/papers/2607.08765
score: 75
model: google/gemma-4-31b-it:free
generated_at: '2026-07-12T08:12:34.706071'
---

📌 全景影像生成新突破：Canvas360 透過幾何感知預訓練提升一致性

TL;DR：Canvas360 提出兩階段框架，結合幾何感知預訓練與微調，強化全景生成的幾何一致性與全域性連貫性。

生成一張高品質的全景圖（Panoramic Image）最困難的不是細節，而是在 360 度視角下如何保持幾何結構不崩潰，且左右接縫處能完美銜接。

🧩 **Canvas360 的兩階段生成框架**

為了克服全景影像在全域性連貫性上的挑戰，Canvas360 採取了「預訓練 $\rightarrow$ 微調」的兩階段設計：

1. **幾何感知預訓練 (Geometry-aware Pretraining)**：透過針對幾何特性的預訓練，讓模型在生成初期就能理解全景影像的空間結構。
2. **後續微調 (Fine-tuning)**：在預訓練基礎上進一步最佳化，以提升最終生成的影像品質。

📊 **大規模資料集與建模技術**

該框架的核心競爭力在於其結合了大規模資料集以及新穎的建模技術。作者宣稱，這種組合能有效改善全景生成中常見的幾何不一致問題，確保影像在 360 度環繞視角下具有更好的全域性連貫性。

🎯 **實務啟示**

對於從事 AIGC 或全景影像生成的工程師而言，這項研究證明了「幾何先驗」的重要性。在處理具有強空間約束的影像生成時，直接進行微調可能不足夠，在預訓練階段就將幾何感知（Geometry-aware）納入模型設計，可能是提升生成穩定性的關鍵路徑。

🔗 **來源**
- 標題：Enhancing In-context Panoramic Generation via Geometric-aware Pretraining
- 連結：https://huggingface.co/papers/2607.08765

#AI #GenerativeAI #PanoramicGeneration #ComputerVision #Canvas360 #GeometricConsistency #ImageSynthesis #MachineLearning #DeepLearning #InContextGeneration
