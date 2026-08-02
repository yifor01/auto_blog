---
title: 'NVIDIA Releases Cosmos 3 Edge: A 4B-Parameter Open World Model That Reasons
  and Generates Robot Actions On-Device'
source: MarkTechPost
url: https://www.marktechpost.com/2026/07/21/nvidia-releases-cosmos-3-edge-a-4b-parameter-open-world-model-that-reasons-and-generates-robot-actions-on-device/
score: 102
model: tencent/hy3:free
generated_at: '2026-07-21T08:28:08.970826'
---

這篇內容屬於「產業新聞」，我將針對 NVIDIA 發布 Cosmos 3 Edge 模型及其技術架構進行轉寫。

📌 【NVIDIA 新發布】Cosmos 3 Edge：4B 參數模型實現機器人邊緣端推理與動作生成

TL;DR：NVIDIA 發布 Cosmos 3 Edge，讓機器人能在受限的邊緣裝置上進行即時環境理解與動作生成。

🤔 **解決邊緣端裝置的效能與記憶體挑戰**

在工廠、倉庫與醫院等實際應用場景中，機器人需要在資源受限的邊緣裝置（Edge devices）上執行，同時具備資料中心等級的處理能力。Cosmos 3 Edge 正是為了填補這項技術缺口而設計。

🧩 **世界模型（World Model）如何賦予機器人推理能力**

世界模型的核心在於學習環境隨時間變化的規律，並能表徵物體、運動、空間關係以及動作所產生的影響。以機器人抓取物體為例，世界模型不只能辨識物體，還能進行以下推理：
- 追蹤物體位置與機械手臂（Gripper）的移動。
- 預測動作發生後的視覺結果。
- 推論導致環境變化的動作原因。
- 根據目標生成對應的動作指令。

透過共享表徵（Shared representation），模型能理解當前世界狀態、模擬可能的未來，並將這些未來與具體動作連結起來。

🏗️ **Mixture-of-Transformers 雙塔架構設計**

Cosmos 3 系列包含 Cosmos 3 Nano (16B) 與 Cosmos 3 Super (64B)，而本次發布的 Edge 版本則是規模最小的第三層級，大小約為 Super 版本的 1/16。其技術架構採用 Mixture-of-Transformers，包含兩個塔式結構（Two towers）：

1. **Autoregressive Tower（自迴歸塔）**：處理視覺與文字 Token，用於理解與推理。
2. **Diffusion Tower（擴散塔）**：處理視覺、音訊與動作 Token，用於預測、生成與神經模擬（Neural simulation）。

這兩座塔各自擁有獨立的正規化層（Normalization layers）與多層感知器（MLP），但會共用多模態注意力層（Multimodal attention layers），藉此對齊語言、影片、音訊與動作之間的資訊，讓模型在生成輸出前能先對場景進行推理。

📊 **Cosmos 3 系列產品規格對照**

| 型號 | 參數規模 | 備註 |
| :--- | :--- | :--- |
| Cosmos 3 Super | 64B | 2026/05/31 於 GTC Taipei 發布 |
| Cosmos 3 Nano | 16B | 2026/05/31 於 GTC Taipei 發布 |
| Cosmos 3 Edge | 4B | 專為邊緣端裝置設計 |

🎯 **實務啟示**

對於開發機器人與視覺 AI 代理（Vision AI agents）的工程師而言，Cosmos 3 Edge 的推出意味著複雜的世界模型推理不再僅限於雲端，具備高參數規模的模型正逐漸走向裝置端（On-device），這對需要低延遲與高隱私性的工業與醫療自動化至關重要。

🔗 **來源**
- 標題：NVIDIA Releases Cosmos 3 Edge: A 4B-Parameter Open World Model That Reasons and Generates Robot Actions On-Device
- 作者／機構：Asif Razzaq @ MarkTechPost
- 連結：https://www.marktechpost.com/2026/07/21/nvidia-releases-cosmos-3-edge-a-4b-parameter-open-world-model-that-reasons-and-generates-robot-actions-on-device/

#NVIDIA #Cosmos3 #EdgeAI #WorldModel #Robotics #MachineLearning #ComputerVision #AIOnDevice #Transformer #AutonomousSystems
