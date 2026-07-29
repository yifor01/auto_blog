---
title: Memory Efficient Audio Synthesis with Decoupled Temporal Depth Diffusion Transformers
source: Apple ML
url: https://machinelearning.apple.com/research/audio-synthesis-diffusion-transformers
model: tencent/hy3:free
generated_at: '2026-07-29T08:28:51.948838'
score: 105
---

📌 【Apple ML 研究】分離時深度擴散 Transformer：讓裝置端音訊合成更省記憶體

TL;DR：透過解耦時域與深度處理，在極低記憶體消耗下實現超即時音訊合成。

當我們談論生成式 AI 時，如何在行動裝置有限的運算資源與記憶體內，實現高品質且即時的語音合成，一直是業界的挑戰。Apple 研究團隊提出的這項技術，正是為了讓 Siri Expressive Voices 能夠在裝置端（On-device）以極高的效率運行。

🧩 **解耦時域與深度處理的 RVQ 架構**

為了將基礎模型輸出的語義音訊 Token（semantic audio tokens）轉換為高保真音訊，研究人員設計了一種基於殘差向量量化（RVQ）的解碼器，其核心在於將處理過程系統性地拆解：

- 串流編碼器（Streaming encoder）
- 時域解碼器（Temporal decoder）
- 深度解碼器（Depth decoder）

這種設計透過「解耦（Decouple）」時域與深度的處理流程，大幅提升了架構的效率。

💡 **用單一 DiT 架構取代多層解碼器**

傳統的多解碼器架構通常需要為每個 RVQ 層級配置專用的解碼器，但本研究提出了一種創新做法：

1. 使用一個可重複使用的深度解碼器（Depth decoder）。
2. 採用類 Diffusion Transformer (DiT) 風格的階段條件化（Stage conditioning）。
3. 以自回歸（Autoregressively）的方式生成所有 RVQ 層級。

這種設計不僅簡化了架構，更有效降低了運算負擔。

📊 **實現常數級別的記憶體複雜度**

針對長序列生成的挑戰，該架構引入了因果滑動視窗注意力機制（Causal sliding window attention），並配合固定視窗的鍵值快取（Fixed-window key-value caching）。這使得記憶體複雜度不再隨序列長度增加而呈線性或平方成長，而是維持在常數水平。

在 Apple Matrix Coprocessor (AMX) 上的實際測試數據如下：

| 指標 | 效能表現 |
| :--- | :--- |
| 生成速度 | 每生成步長約 10ms (比即時快 16 倍) |
| 峰值執行記憶體 | 約 21MB |
| 裝置端資產大小 | 329MB |

這項技術讓裝置能夠在執行基礎模型之餘，同時進行長達 20 至 320 秒音訊的連續串流合成。

🎯 **實務啟示**

對於開發行動端 AI 應用的工程師而言，這項研究展示了「解耦處理」與「常數記憶體複雜度」設計的重要性。透過將複雜的生成任務拆解並優化注意力機制，我們可以在極度受限的硬體環境下，實現高品質且具備即時性的生成式體驗。

🔗 **來源**
- 標題：Memory Efficient Audio Synthesis with Decoupled Temporal Depth Diffusion Transformers
- 作者／機構：Apple ML
- 連結：https://machinelearning.apple.com/research/audio-synthesis-diffusion-transformers

#AppleML #AudioSynthesis #DiffusionTransformer #OnDeviceAI #MachineLearning #RVQ #SpeechSynthesis #MobileAI #DeepLearning #EfficientAI
