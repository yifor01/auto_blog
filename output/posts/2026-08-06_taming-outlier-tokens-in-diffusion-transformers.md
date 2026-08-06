---
title: Taming Outlier Tokens in Diffusion Transformers
source: Apple ML
url: https://machinelearning.apple.com/research/taming-outlier-tokens
model: tencent/hy3:free
generated_at: '2026-08-06T08:38:28.249778'
score: 93
---

📌 【Apple ML 研究】解決 Diffusion Transformers 中的 Outlier Tokens 問題，提升生成品質

TL;DR：透過 Dual-Stage Registers (DSR) 介入，解決 DiT 中高範數 Token 導致的生成瑕疵。

🤔 **高範數 Token 會干擾注意力機制**

在 Vision Transformers (ViT) 中，研究發現會出現極少數具有「高範數 (high-norm)」的 tokens。這些 token 會吸引過多的注意力權重，但實際上卻攜帶極少的局部資訊。雖然這在 ViT 中已被觀察到，但在生成模型中的影響仍待深入探討。

🧩 **Outlier Tokens 存在於編碼器與去噪器中**

研究指出，這種現象同時存在於現代 Representation Autoencoder (RAE)-DiT 流程的兩個階段：
1. **預訓練的 ViT 編碼器**：會產生 outlier representations。
2. **DiT 去噪器 (Denoiser)**：DiT 內部也會發展出 outlier tokens，且在中間層（intermediate layers）的情況尤為明顯。

⚠️ **單純遮蔽高範數 Token 並無效果**

研究發現，僅僅對這些高範數 token 進行遮蔽（masking）並不能提升效能。這顯示問題的核心不在於少數極端數值，而更接近於「受損的局部 patch 語義 (corrupted local patch semantics)」。

🧩 **提出 Dual-Stage Registers (DSR) 進行介入**

為了應對此問題，研究團隊提出了 Dual-Stage Registers (DSR) 方案，針對兩個組件進行 register-based 的介入：
- **針對編碼器**：若有可用資料則使用訓練好的 registers，否則在測試階段採用遞迴式 (recursive) registers。
- **針對去噪器**：引入 diffusion registers。

📊 **在 ImageNet 與大規模圖文生成中皆能提升品質**

實驗結果顯示，透過上述介入手段，在 ImageNet 任務以及大規模 text-to-image 生成任務中，皆能一致地減少 outlier artifacts（離群值產生的瑕疵），並進一步提升生成品質。研究強調，控制 outlier tokens 是構建更強大 DiT 的重要要素。

🎯 **實務啟示**

對於開發生成式 AI 模型的工程師而言，這項研究提示我們，Transformer 架構在處理視覺資料時，內部的 token 數值分布不均（outliers）會直接影響生成結果。透過引入類似 Register 的機制來穩定 token 表現，可能是優化 DiT 效能的關鍵方向。

🔗 **來源**
- 標題：Taming Outlier Tokens in Diffusion Transformers
- 作者／機構：Xiaoyu Wu, Yifei Wang, Tsu-Jui Fu, Liang-Chieh Chen, Zhe Gan, Chen Wei @ Apple ML / Rice University
- 連結：machinelearning.apple.com/research/taming-outlier-tokens

#AI #ComputerVision #DiffusionTransformers #DiT #MachineLearning #AppleML #Transformer #ImageGeneration #OutlierTokens #DeepLearning
