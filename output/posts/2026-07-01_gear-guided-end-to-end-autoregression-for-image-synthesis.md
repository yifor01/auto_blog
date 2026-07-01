---
title: 'GEAR: Guided End-to-End AutoRegression for Image Synthesis'
source: HuggingFace Daily Papers
url: https://huggingface.co/papers/2606.32039
score: 86
model: google/gemma-4-31b-it:free
generated_at: '2026-07-01T20:41:54.121816'
---

📌 GEAR：透過端到端聯合訓練，打破影像合成的 VQ 瓶頸

TL;DR：GEAR 透過表示對齊與雙讀出機制，實現 VQ Tokenizer 與自回歸生成器的端到端聯合訓練。

在傳統的自回歸影像合成流程中，VQ Tokenizer（向量量化分詞器）與後續的自回歸生成器通常是分開訓練的。這種分階段的設計導致生成器必須適應一個固定的量化空間，若 Tokenizer 的特徵表達不夠理想，後續的生成品質將面臨天花板。

🤔 **解決非微分問題的端到端訓練**

GEAR 提出了一種 Guided End-to-End AutoRegression 框架，旨在讓 VQ Tokenizer 與自回歸生成器在同一過程中共同演進。其核心挑戰在於量化過程（Quantization）通常是不可微的，導致梯度無法直接回傳。

🧩 **利用表示對齊與雙讀出機制提升品質**

為了克服上述問題，GEAR 引入了以下技術設計：

- 表示對齊 (Representation Alignment)：讓 Tokenizer 與生成器在相同的表示空間中進行對齊，確保兩者對影像特徵的理解一致。
- 雙讀出方法 (Dual Read-out Approach)：透過這種機制解決非微分問題，讓梯度能有效傳遞，進而提升模型的收斂速度並最佳化特徵品質。

💡 **同步演進帶來的高效能**

相較於傳統分階段訓練，GEAR 的聯合訓練模式讓 Tokenizer 能根據生成器的需求動態調整特徵分佈，而非死板地遵循預訓練的量化碼本，從而提升整體的影像合成效能。

🎯 **實務啟示**

對於開發影像生成模型的工程師而言，GEAR 的設計證明瞭「聯合訓練」能比「分階段訓練」更有效地最佳化特徵品質。若目前的 VQ-VAE 或 VQGAN 瓶頸在於 Token 質素限制了生成器的表現，考慮引入表示對齊與可微的讀出機制可能是提升品質的關鍵方向。

🔗 **來源**
- 標題：GEAR: Guided End-to-End AutoRegression for Image Synthesis
- 連結：https://huggingface.co/papers/2606.32039

#AI #ImageSynthesis #Autoregressive #VQTokenizer #EndToEndTraining #ComputerVision #DeepLearning #RepresentationAlignment #GenerativeAI #GEAR
