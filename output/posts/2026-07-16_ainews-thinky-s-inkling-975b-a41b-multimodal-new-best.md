---
title: '[AINews] Thinky''s Inkling: 975B-A41B multimodal, new best American Apache
  2.0 open model (with Inkling-Small, 276B-A12B)'
source: Latent Space
url: https://www.latent.space/p/ainews-thinkys-inkling-975b-a41b
score: 102
model: tencent/hy3:free
generated_at: '2026-07-16T08:11:58.108658'
---

📌 【Latent Space 報導】Thinky 釋出 Inkling：975B-A41B 美國 Apache 2.0 開放多模態模型

TL;DR：Thinking Machines 推出開放權重多模態 MoE 模型 Inkling，主打可客製化基底而非衝榜。

每幾個月才浮上檯面的 Thinky（Thinking Machines Lab），這次不只有品味還帶來了實打實的開放模型家族。當多數實驗室拚命擠進排行榜前端，他們卻選擇先交出一個「能用的基底」。

🤔 **不是 SOTA，而是美國開放模型的實用新基線**

根據 Latent Space 的 AINews 整理，Thinking Machines Lab 發表了 Inkling，這不是一個追求 state-of-the-art 的旗艦模型，而是一個定位為「可客製化多模態基底模型」的開放權重（open-weights）家族。Mira Murati 稱其為公司「第一個從零訓練、開放權重的模型」，並在自家 Tinker 平臺提供同日 fine-tuning。

🧩 **975B 總引數、41B 活躍的 MoE 多模態架構**

README 性質的報導指出，Inkling 是一個 Mixture-of-Experts (MoE) transformer，技術規格如下：
- 總引數 975B，活躍引數 41B（標記為 975B-A41B）
- 支援最多 1M tokens 的上下文視窗
- 預訓練語料達 45 trillion tokens，涵蓋文字、圖片、音訊與影片
- 原生支援文字、圖片、音訊推理，並透過可控制的 thinking effort 平衡成本與效能

同家族也預覽了較輕量的 Inkling-Small：活躍引數 12B（276B-A12B），使用類似訓練配方，主打更低成本與延遲下的強效能。

🎯 **開放權重與同日微調，對工程師的實際意義**

對 ML 工程師來說，Inkling 的價值不在刷分，而在「可取得完整權重」並直接在 Tinker 或 Hugging Face 上做 fine-tuning。Soumith Chintala 強調其開放權重、原生多模態與在 Tinker、Hugging Face 上的可用性；這代表團隊能以此為基底，針對自身多模態任務做客製化，而非從頭訓練。

🔗 **來源**
- 標題：[AINews] Thinky's Inkling: 975B-A41B multimodal, new best American Apache 2.0 open model (with Inkling-Small, 276B-A12B)
- 作者／機構：Latent Space
- 連結：https://www.latent.space/p/ainews-thinkys-inkling-975b-a41b

#Multimodal #OpenWeights #MoE #Inkling #ThinkingMachines #LLM #FineTuning #Apache2 #HuggingFace #Tinker
