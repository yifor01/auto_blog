---
title: Token Time Continuous Diffusion for Language Modeling
source: HuggingFace Daily Papers
url: https://huggingface.co/papers/2607.14106
score: 94
model: tencent/hy3:free
generated_at: '2026-07-18T07:34:19.331803'
---

📌 【HuggingFace Papers】Token Time Continuous Diffusion：用連續空間與逐 token 時間提速擴散語言模型

TL;DR：TTCD 在連續空間對映噪聲到 token，並以逐 token 時間提升高加速下的生成品質。

擴散語言模型（diffusion LM）想在高速生成下保持準確，往往卡在離散空間反覆取樣的瓶頸。這篇論文提出一個反直覺的做法：讓不同 token 以不同速率從噪聲走向成品。

🤔 **離散空間平行取樣是高加速失真的主因**

既有的擴散語言模型若純粹在離散空間迭代，需要在高加速時平行取樣多個 token，而這種平行取樣正是高速下準確度下降的關鍵來源。

🧩 **連續空間 + 逐 token 時間的雙重設計**

TTCD（token time continuous diffusion）是一種新的擴散語言模型，其設計有兩個核心：

- 在連續空間運作，確定性地將 Gaussian 噪聲對映到最終的 token 畫布，不需要額外的取樣步驟。
- 引入 per-token time 的新概念，部分 token 從噪聲到 token 的速率比其他的快。

這樣的設計有三個作用：更好地建模條件生成、讓較有把握的 token 以更快速率進行、在精煉（refinement）過程中允許 token 間有不同程度的互動影響。

📊 **160M 模型在 OpenWebText 的表現**

作者訓練了一個 1.6 億引數的 TTCD 模型，使用 OpenWebText 資料集，隨後進行 self-distill。

- 在高加速下，無條件生成品質與同規模、同資料、同 self-distill 的數個現有模型相當。
- 條件生成則優於這些對比模型。
- 在 Sudoku 求解任務上也觀察到類似的增益。
- 整體而言，TTCD 在高加速下優於離散模型。

⚠️ **素材未提及的細節**

摘要未說明具體的評估指標數值、架構層數、訓練超引數，也未提及與哪些特定模型逐一對比，因此無法進一步量化差距。

🎯 **實務啟示**

若你在做 diffusion LM 相關研究，TTCD 指出兩條可嘗試的路徑：一是改用連續空間避免離散平行取樣的誤差累積，二是用 per-token time 讓模型自己決定哪些 token 該先定案。對追求低延遲生成的場景，這比單純堆離散迭代步數更有機會保住品質。

🔗 **來源**
- 標題：Token Time Continuous Diffusion for Language Modeling
- 連結：https://huggingface.co/papers/2607.14106

#DiffusionLM #LanguageModeling #ContinuousSpace #TokenTime #TTCD #SelfDistillation #OpenWebText #ConditionalGeneration #Sudoku #HuggingFacePapers
