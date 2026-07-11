---
title: 'Flash-BoN: Instant Drafts for Inference-Time Scaling in Diffusion Models'
source: HuggingFace Daily Papers
url: https://huggingface.co/papers/2607.04461
score: 93
model: google/gemma-4-31b-it:free
generated_at: '2026-07-11T08:18:12.657895'
---

📌 Flash‑BoN：用即時草稿加速擴散模型推理，效能突破固定時限

TL;DR：Flash‑BoN 透過時間步截斷、層跳過與 activation proxy 產生低成本草稿，並以多階段驗證取代傳統抽樣，在相同執行時間下提升文字生成影像效能。

🤔 為何要重新思考擴散推理？

即使硬體持續進步，Diffusion Model 的逐步去噪仍是耗時的瓶頸。開發者常在「固定時鐘預算」下求得更高畫質，卻受限於每一步的計算成本。若能先產生快速、粗糙的草稿，再用少量資源精煉，是否能在相同時間內得到更好結果？

🧩 Flash‑BoN 的核心概念：草稿 + 多階段驗證

Flash‑BoN 以三項低成本技巧產出「草稿候選」：

1. **timestep truncation** – 只執行部分時間步，提前停止去噪程式。  
2. **layer skipping** – 在模型前向傳播時跳過部分層，減少計算量。  
3. **activation proxies** – 使用簡化的啟用近似，快速估算中間特徵。

產生的草稿雖然品質不完整，但足以作為後續篩選的基礎。接著，系統會執行**多階段驗證**：逐步加大計算資源，只對最有潛力的草稿進行更精細的去噪與修正。這樣的流程在「固定牆時」預算內，能夠比傳統一次性完整去噪的方法取得更佳的影像品質。

📊 成效概述

根據摘要，Flash‑BoN 在相同的執行時間限制下，**超越現有的加速方法**。雖未提供具體數值，但可確認其驗證流程在效率與品質間取得更好的平衡。

🎯 實務啟示：如何在專案中應用草稿驗證思路

- **快速原型**：在開發階段，可先以 timestep truncation 或 layer skipping 產生低解析度草圖，快速檢視概念。  
- **資源分配**：將預算集中於少數高潛力草稿的深度修正，避免對所有樣本均衡投入，提升整體產出速率。  
- **模組化實作**：Flash‑BoN 的三個草稿產生技巧皆可作為獨立外掛加入現有 Diffusion pipeline，降低整合門檻。

🔗 來源  
- 標題：Flash‑BoN: Instant Drafts for Inference‑Time Scaling in Diffusion Models  
- 連結：https://huggingface.co/papers/2607.04461  

#DiffusionModels #TextToImage #InferenceScaling #FlashBoN #AIAcceleration #DraftGeneration #MultiStageVerification #MachineLearning #GenerativeAI #Efficiency  
