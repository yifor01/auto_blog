---
title: 'Focusing on What Matters: Saliency-Harnessing Accurate Routing for Diffusion
  MoE'
source: HuggingFace Daily Papers
url: https://huggingface.co/papers/2606.26938
score: 87
model: google/gemma-4-31b-it:free
generated_at: '2026-06-30T20:40:12.308015'
---

📌 透過 Saliency 引導路由，提升 Diffusion MoE 的計算分配精準度

TL;DR：SharpMoE 利用乾淨的潛在特徵與軌跡路由損失，最佳化 Diffusion 模型中 MoE 的 token 分配效率。

在 Diffusion 模型中匯入 Mixture-of-Experts (MoE) 雖然能增加模型容量，但如何精準地將計算資源分配給真正「重要」的 token，一直是提升效率的挑戰。

🤔 **Diffusion MoE 的路由效率瓶頸**

傳統的 MoE 路由在處理多步驟去噪（denoising）時，往往面臨路由效率低下的問題，無法在複雜的生成過程中精準識別哪些 token 需要更多計算資源。

🧩 **SharpMoE 的兩大技術核心**

為了改善路由分配，SharpMoE 提出了以下兩種機制：

- **利用乾淨特徵識別關鍵 Token**：使用 clean latent features 作為指引，幫助模型識別出具有顯著性（salient）的 token，確保計算資源聚焦在真正關鍵的特徵上。
- **軌跡路由損失 (Trajectory Routing Loss)**：在多步驟的去噪過程中，引入軌跡路由損失來最佳化路由路徑，實現更精確的計算分配。

🎯 **實務啟示**

對於開發生成式 AI 的工程師而言，這項研究提示了一個方向：在 MoE 的路由設計中，不應僅依賴當前的輸入，而可以利用「乾淨特徵」或「生成軌跡」等先驗資訊，來決定計算資源的分配，從而達到效能與效率的平衡。

🔗 **來源**
- 標題：Focusing on What Matters: Saliency-Harnessing Accurate Routing for Diffusion MoE
- 連結：https://huggingface.co/papers/2606.26938

#Diffusion #MoE #Saliency #DeepLearning #GenerativeAI #Routing #SharpMoE #MachineLearning #ComputeEfficiency #Denoising
