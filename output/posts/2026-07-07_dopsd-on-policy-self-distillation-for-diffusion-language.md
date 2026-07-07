---
title: 'dOPSD: On-Policy Self-Distillation for Diffusion Language Models'
source: HuggingFace Daily Papers
url: https://huggingface.co/papers/2607.04428
score: 97
model: google/gemma-4-31b-it:free
generated_at: '2026-07-07T21:11:47.992925'
---

📌 Diffusion LLM 的新突破：透過 On-Policy 自蒸餾強化推理能力

TL;DR：dOPSD 透過內部去噪軌跡的自蒸餾，提升擴散語言模型在數學推理與程式碼生成上的效能。

擴散語言模型（Diffusion LLMs）在生成能力上具有潛力，但在後訓練（Post-training）階段如何有效強化推理能力，一直是研究中的一大挑戰。

🤔 **Diffusion LLM 在推理強化上的困境**

傳統的語言模型強化路徑已相當成熟，但 Diffusion LLM 在面對需要高度邏輯性的數學推理與程式碼生成時，如何透過後訓練進一步提升效能，仍缺乏高效的解決方案。

🧩 **利用內部去噪軌跡進行 On-Policy 自蒸餾**

為了克服上述問題，這項研究提出了名為 dOPSD 的方法。其核心理念在於利用模型內部的去噪軌跡（denoising trajectories）進行 On-Policy 自蒸餾。

具體作法是讓模型在生成過程中的去噪路徑成為學習物件，透過這種自蒸餾機制，讓模型在生成推理類內容時能更精準地最佳化輸出結果。

📊 **數學推理與程式碼生成效能提升**

根據研究結果，dOPSD 方法能有效改善 Diffusion LLM 在以下兩個關鍵領域的表現：
- 數學推理（Mathematical Reasoning）
- 程式碼生成（Code Generation）

🎯 **實務啟示**

對於開發 Diffusion LLM 的工程師而言，這項研究提供了一個新方向：不需要依賴外部的大量標記資料，而是透過挖掘模型自身的去噪軌跡（Internal Trajectories）來進行自我最佳化，這為擴散模型在複雜邏輯任務上的應用開闢了新的可能性。

🔗 **來源**
- 標題：dOPSD: On-Policy Self-Distillation for Diffusion Language Models
- 連結：https://huggingface.co/papers/2607.04428

#DiffusionLLM #SelfDistillation #Reasoning #CodeGeneration #MathematicalReasoning #OnPolicy #MachineLearning #NLP #GenerativeAI #dOPSD
