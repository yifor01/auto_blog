---
title: 'OrbitQuant: Data-Agnostic Quantization for Image and Video Diffusion Transformers'
source: HuggingFace Daily Papers
url: https://huggingface.co/papers/2607.02461
score: 94
model: google/gemma-4-31b-it:free
generated_at: '2026-07-06T20:27:03.845063'
---

📌 OrbitQuant：讓 Diffusion Transformer 量化不再需要針對每個時間步反覆校正

TL;DR：透過正規化旋轉基底（normalized rotated basis），實現無需跨時間步與模態重新校正的量化技術。

在部署 Diffusion Transformer (DiT) 時，量化（Quantization）面臨一個棘手問題：模型在不同時間步（timesteps）與不同模態（modalities）下的啟用值分佈差異極大，導致傳統量化方法往往需要針對不同狀態進行繁瑣的校正（recalibration），大幅增加部署成本。

🤔 **跨時間步與模態的量化校正痛點**

Diffusion 模型在生成過程中的每一階段（時間步）特徵分佈都在變動，這意味著單一的量化引數難以在所有階段都保持高精度。如果為了維持品質而對每個時間步進行校正，會導致推理過程變得極其低效。

🧩 **利用正規化旋轉基底消除校正需求**

OrbitQuant 提出了一種 Data-Agnostic（與資料無關）的量化方案，其核心設計在於：

- **引入旋轉基底**：使用一種正規化後的旋轉基底（normalized rotated basis）來處理權重與啟用值。
- **消除校正流程**：透過這種數學變換，模型能夠在不同時間步與模態之間保持一致性，從而消除了在推理時針對不同時間步重新校正的必要。
- **後訓練量化 (PTQ)**：該方法屬於 Post-Training Quantization，不需要對模型進行昂貴的重新訓練即可達成高效量化。

🎯 **實務啟示**

對於需要部署影像或影片生成模型的工程師而言，OrbitQuant 的價值在於簡化了量化部署的管線（pipeline）。如果能擺脫對特定時間步校正資料的依賴，將能顯著降低模型在不同生成階段的記憶體管理複雜度，並提升推理速度。

🔗 **來源**
- 標題：OrbitQuant: Data-Agnostic Quantization for Image and Video Diffusion Transformers
- 連結：https://huggingface.co/papers/2607.02461

#AI #DiffusionTransformer #Quantization #PTQ #DeepLearning #ImageGeneration #VideoGeneration #ModelCompression #Efficiency #OrbitQuant
