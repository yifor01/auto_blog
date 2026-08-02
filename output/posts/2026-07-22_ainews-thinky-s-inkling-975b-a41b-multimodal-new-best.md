---
title: '[AINews] Thinky''s Inkling: 975B-A41B multimodal, new best American Apache
  2.0 open model (with Inkling-Small, 276B-A12B)'
source: Latent Space
url: https://www.latent.space/p/ainews-thinkys-inkling-975b-a41b
model: tencent/hy3:free
generated_at: '2026-07-22T00:45:04.473399'
score: 97
---

這是一篇針對「產業新聞」型別的技術部落格文章。

📌 【AINews】Thinking Machines 發布 Inkling 系列：975B 參數規模開源，主打原生多模態與高效推理

TL;DR：Thinking Machines 推出 Inkling 開源模型家族，以 975B 參數 MoE 架構實現文本、影像與音訊的原生多模態推理。

🎣 **不追求 Benchmark 資料極致，而是打造實用的開源基石**

當大多數研究重點都放在刷高 Benchmark 分數時，Thinking Machines Lab 選擇了另一條路。他們剛發布了 Inkling 系列，這不是一個為了刷榜而生的旗艦模型，而是一個旨在提供高度可定製性、具備實用價值的開源權重（open-weights）多模態基礎模型。

🧩 **975B 參數規模與原生多模態能力**

Inkling 採用 Mixture-of-Experts (MoE) 架構，其設計核心在於平衡效能與成本，並透過可控的「思考強度」來達成高效推理。

* **模型架構與規模**：
  * 主力模型 Inkling：總參數 975B，每次推論時僅動用 41B 參數（active parameters）。
  * Inkling-Small：較輕量化的版本，動用參數為 12B。
* **訓練規模與資料**：
  * 預訓練資料量達 45 兆 (trillion) tokens。
  * 資料涵蓋文本、影像、音訊與影片。
* **核心能力**：
  * 支援高達 1M tokens 的上下文長度（context window）。
  * 具備原生（native）處理文本、影像與音訊的能力，而非僅是透過外掛模組連線。

💡 **提供不同規模的選擇，兼顧成本與延遲**

除了 975B 的大型模型，Inkling 系列同時釋出了 Inkling-Small 的預覽版。這款模型採用相似的訓練配方，但擁有更低的成本與延遲，適合需要快速反應的應用場景。

根據開發者描述，Inkling 是從零開始（trained from scratch）訓練的，並已在 Tinker 平臺與 Playground 上提供支援，開發者甚至可以在當天進行 fine-tuning。

🎯 **實務啟示**

對於工程師而言，Inkling 的價值不在於它是否在排行榜上排名第一，而在於其「可定製性」與「原生多模態」的特性。對於需要處理音訊或影像，且希望在成本與推理速度之間取得平衡的專案，這種 MoE 架構的大規模開源模型提供了極具吸引力的基準（baseline）。

🔗 **來源**
- 標題：[AINews] Thinky's Inkling: 975B-A41B multimodal, new best American Apache 2.0 open model (with Inkling-Small, 276B-A12B)
- 作者／機構：Latent Space
- 連結：https://www.latent.space/p/ainews-thinkys-inkling-975b-a41b

#AI #MachineLearning #Multimodal #MoE #OpenWeights #ThinkingMachines #Inkling #LLM #AIResearch #GenerativeAI
