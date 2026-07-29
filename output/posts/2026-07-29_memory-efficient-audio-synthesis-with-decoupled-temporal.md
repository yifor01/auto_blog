---
title: Memory Efficient Audio Synthesis with Decoupled Temporal Depth Diffusion Transformers
source: Apple ML
url: https://machinelearning.apple.com/research/audio-synthesis-diffusion-transformers
model: tencent/hy3:free
generated_at: '2026-07-29T14:09:14.739399'
score: 108
---

📌 【Apple 研究】解耦時空深度的 DiT 架構，實現手機端的高效音訊合成

TL;DR：透過解耦時間與深度處理，在極低記憶體消耗下達成 16 倍於即時速度的音訊合成。

隨著生成式 AI 邁向裝置端（on-device）運算，如何在有限的硬體資源下，將語義 Token 轉換為高品質音訊，成為關鍵挑戰。Apple 研究團隊提出了一種新型音訊解碼器（detokenizer），旨在為 Siri Expressive Voices 提供即時、高保真度的語音合成能力。

🧩 **解耦時空處理的 RVQ 三階段設計**

為了在 Apple Matrix Coprocessor (AMX) 的嚴格計算與記憶體限制下運作，研究提出了一種基於殘差向量量化（Residual Vector Quantization, RVQ）的架構，將語義音訊 Token 轉換為高品質音訊，其核心包含三個組件：

1.  **Streaming Encoder**：負責處理串流輸入。
2.  **Temporal Decoder**：負責處理時間維度的解碼。
3.  **Depth Decoder**：負責處理深度維度的解碼。

這種設計系統性地將「時間」與「深度」處理進行解耦（decoupled），大幅提升處理效率。

💡 **用單一 DiT 結構取代多層解碼器**

傳統的多解碼器架構通常需要為每個 RVQ 層級配置專用的解碼器，而本研究提出了一種基於 Diffusion Transformer (DiT) 風格的設計：

- **Stage Conditioning**：使用單一且可重複使用的 Depth Decoder，透過階段條件化（stage conditioning）以自回歸（autoregressive）方式生成所有 RVQ 層級。
- **Causal Sliding Window Attention**：採用因果滑動視窗注意力機制，並搭配固定視窗的 Key-Value 緩存（KV caching），使得記憶體複雜度與序列長度無關，達成常數級別（constant complexity）的記憶體消耗。

📊 **在 AMX 上實現 16 倍於即時的速度**

該架構已部署於 AMX 進行測試，其效能表現顯著優於傳統的 Transformer 或 GAN 方案：

| 項目 | 效能數據 |
| :--- | :--- |
| **生成速度** | 每步約 10ms（約為即時速度的 16 倍） |
| **峰值執行記憶體** | 約 21MB |
| **裝置端資產大小** | 329MB |

這種恆定且微小的記憶體佔用，讓裝置能在運行基礎模型（foundation model）的同時，持續進行長達 20 至 320 秒音訊的串流合成。

🎯 **實務啟示**

對於開發裝置端 AI 應用（如語音助手）的工程師而言，這項研究證明瞭「解耦處理」與「常數記憶體複雜度」是解決裝置端資源受限問題的關鍵。透過將複雜度從線性或平方級降低至常數級，能在有限的硬體空間內，實現高保真度與低延遲的即時體驗。

🔗 **來源**
- 標題：Memory Efficient Audio Synthesis with Decoupled Temporal Depth Diffusion Transformers
- 作者／機構：Apple ML
- 連結：https://machinelearning.apple.com/research/audio-synthesis-diffusion-transformers

#Apple #AudioSynthesis #DiffusionTransformer #DiT #MachineLearning #OnDeviceAI #SpeechSynthesis #RVQ #DeepLearning #EdgeAI
