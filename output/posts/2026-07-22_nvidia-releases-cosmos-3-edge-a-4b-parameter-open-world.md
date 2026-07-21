---
title: 'NVIDIA Releases Cosmos 3 Edge: A 4B-Parameter Open World Model That Reasons
  and Generates Robot Actions On-Device'
source: MarkTechPost
url: https://www.marktechpost.com/2026/07/21/nvidia-releases-cosmos-3-edge-a-4b-parameter-open-world-model-that-reasons-and-generates-robot-actions-on-device/
model: tencent/hy3:free
generated_at: '2026-07-22T00:43:20.926360'
score: 105
---

這篇素材屬於「產業新聞」，將聚焦於 NVIDIA 釋出的新模型及其技術架構。

📌 【NVIDIA 新動態】Cosmos 3 Edge 登場：4B 引數模型讓機器人在邊緣端實現世界模型推理

TL;DR：NVIDIA 釋出 Cosmos 3 Edge，讓機器人在記憶體受限的邊緣端即可進行視覺推理與動作生成。

隨著機器人技術邁向實務應用，機器人不再只需要「看見」物體，更需要「理解」物理世界的互動規律。

🤔 **解決邊緣運算的記憶體與效能矛盾**

機器人在工廠、倉庫或醫院等邊緣端（Edge）運作時，面臨著極大的挑戰：它們需要具備資料中心等級的推理能力，但硬體記憶體卻非常有限。Cosmos 3 Edge 正是為了填補這個差距而設計，它是 Cosmos 3 系列中最小的型態，規模僅約 Cosmos 3 Super 的十六分之一。

🧩 **Mixture-of-Transformers 架構：雙塔式設計實現跨模態對齊**

Cosmos 3 Edge 採用了 Mixture-of-Transformers 架構，透過兩組不同的「塔」（Towers）來處理資訊：

- **Autoregressive Tower（自迴歸塔）**：負責處理視覺與文字的 token，用於理解場景並進行推理。
- **Diffusion Tower（擴散塔）**：負責處理視覺、音訊與動作的 token，用於預測、生成以及神經模擬（neural simulation）。

這兩組塔擁有各自獨立的正規化層（normalization layers）與多層感知器（MLP），但透過共享的多模態注意力層（multimodal attention layers），讓模型能在生成輸出前，先對場景進行深度推理，並在語言、影片、音訊與動作之間達成資訊對齊。

💡 **從視覺理解到動作生成的閉環**

一個「世界模型」（World Model）的核心在於理解環境隨時間變化的規律，包含物體、運動、空間關係以及動作產生的影響。

以機器人伸手拿取物體為例，Cosmos 3 Edge 的處理邏輯如下：
1. **感知與理解**：辨識物體及其位置。
2. **模擬未來**：透過共享表徵理解當前世界狀態，並模擬可能的未來結果。
3. **動作生成**：將模擬的結果與目標連結，進而生成達成目標所需的具體動作。

🎯 **實務啟示**

對於開發機器人與視覺 AI 代理人（Vision AI agents）的工程師來說，Cosmos 3 Edge 提供了一個在本地端（On-device）即可進行複雜物理推理的可能性，這對於需要即時反應且對延遲敏感的邊緣運算場景具有極高的實作價值。

🔗 **來源**
- 標題：NVIDIA Releases Cosmos 3 Edge: A 4B-Parameter Open World Model That Reasons and Generates Robot Actions On-Device
- 作者／機構：Asif Razzaq @ MarkTechPost
- 連結：https://www.marktechpost.com/2026/07/21/nvidia-releases-cosmos-3-edge-a-4b-parameter-open-world-model-that-reasons-and-generates-robot-actions-on-device/

#NVIDIA #Cosmos3 #EdgeAI #WorldModel #Robotics #ComputerVision #MachineLearning #AIArchitecture #OnDeviceAI #Transformer
