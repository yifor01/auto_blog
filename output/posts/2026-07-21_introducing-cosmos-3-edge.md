---
title: Introducing Cosmos 3 Edge
source: HuggingFace Blog
url: https://huggingface.co/blog/nvidia/cosmos3edge
score: 103
model: tencent/hy3:free
generated_at: '2026-07-21T08:26:05.782006'
---

這篇內容屬於**開源專案（GitHub/Hugging Face）與產業新聞**的結合，重點在於 NVIDIA 發布的新模型及其在邊緣運算（Edge Computing）的應用能力。

📌 【NVIDIA 開源新動作】Cosmos 3 Edge 登場：4B 引數模型讓機器人實現即時推理與動作生成

TL;DR：NVIDIA 發布 4B 引數開源世界模型 Cosmos 3 Edge，專為邊緣裝置設計，實現機器人即時控制。

🎣 **從資料中心走向物理世界：邊緣運算的挑戰**

要在工廠、倉庫或醫院等現實環境中運作，物理 AI 系統必須具備三大能力：理解場景變化、預測下一步發展，並判斷動作對世界的影響。然而，要在記憶體受限的邊緣裝置上實現資料中心等級的效能，一直是技術上的瓶頸。

🧩 **4B 引數的小型世界模型 (World Model)**

NVIDIA 在 Hugging Face 的 Cosmos 3 儲存庫中發布了 Cosmos 3 Edge。這是一個擁有 40 億（4-billion）引數的開源世界模型，旨在協助機器人和視覺 AI 代理（Vision AI Agents）理解環境、進行即時推理，並在邊緣裝置上生成機器人動作。

📊 **在 VANTAGE-Bench 表現領先，且具備即時控制能力**

作為一個經過後訓練（Post-trained）的世界動作模型（World Action Model, WAM），Cosmos 3 Edge 在同規模（4B 引數）模型中展現了強大的競爭力：

- **視覺分析能力**：在 VANTAGE-Bench 排名第一。
- **機器人策略學習**：達到目前技術的最佳水準（State-of-the-art）。
- **即時控制效能**：在 NVIDIA Jetson Thor 上，以 640×360 解析度的觀察值進行推理，每筆推理可生成 32 個動作，並能達到 15 Hz 的即時控制頻率。

🚀 **支援多種 NVIDIA 邊緣運算硬體**

該模型設計為緊湊型開源模型，可作為小型視覺語言模型（VLM）使用，並在 NVIDIA 的邊緣運算平臺提供高吞吐量與高準確度的即時推理，包含：
- NVIDIA RTX PRO GPU
- NVIDIA DGX
- NVIDIA GeForce RTX™ GPU
- NVIDIA Jetson 系列（包含新發布的 Jetson T2000 與 T3000 模組）

🎯 **實務啟示**

對於開發機器人與智慧基礎設施的工程師而言，Cosmos 3 Edge 提供了一個在有限記憶體下，仍能兼顧「視覺理解」與「動作生成」的開源解決方案，降低了從雲端模型落地到實體裝置的技術門檻。

🔗 **來源**
- 標題：Introducing Cosmos 3 Edge
- 作者／機構：Pranjali Joshi, Saeed Babamohamadi @ NVIDIA
- 連結：https://huggingface.co/blog/nvidia/cosmos3edge

#NVIDIA #Cosmos3Edge #EdgeAI #Robotics #WorldModel #HuggingFace #ComputerVision #MachineLearning #AI #OpenSource
