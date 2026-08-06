---
title: An SLM trained on $8 ESP32-S3
source: Github.com
url: https://github.com/Carloscodix/qapla
model: tencent/hy3:free
generated_at: '2026-08-06T08:43:59.746243'
score: 86
---

📌 【硬體極限挑戰】在 8 顆 ESP32-S3 上從零訓練 Transformer

TL;DR：作者在 8 顆 ESP32-S3 微控制器上，從零開始完成一個字元級 (char-level) Transformer 的完整訓練迴圈。

當我們討論大型語言模型 (LLM) 時，腦中浮現的通常是成千上萬顆 GPU 組成的叢集。但如果我們將目標縮小到微控制器 (MCU) 等級的硬體，訓練一個 Transformer 模型是否可行？

🧩 **不只是推論，而是完整的訓練迴圈**

這是一個名為 qapla 的開源專案，其核心挑戰在於它不只是在微控制器上進行模型推論 (Inference)，而是實踐了完整的訓練過程。

- **模型架構**：採用字元級 (char-level) Transformer。
- **訓練方式**：從零開始訓練 (trained from scratch)。
- **技術實現**：開發者手寫了 C 語言版本的反向傳播 (backprop) 演算法，而非僅是調用現成的深度學習框架。
- **硬體配置**：由 8 顆 ESP32-S3 晶片共同協作完成。

🎯 **實務啟示**

這個專案展示了在資源極度受限的嵌入式環境中，透過手寫底層演算法與硬體協作，實現微型模型訓練的可能性。對於研究邊緣運算 (Edge AI) 或低功耗機器學習的工程師來說，這提供了極具參考價值的極限測試範例。

🔗 **來源**
- 標題：An SLM trained on $8 ESP32-S3
- 作者／機構：Carloscodix
- 連結：https://github.com/Carloscodix/qapla

#AI #MachineLearning #Transformer #ESP32 #EmbeddedAI #Microcontroller #CProgramming #EdgeAI #TinyML #SLM
