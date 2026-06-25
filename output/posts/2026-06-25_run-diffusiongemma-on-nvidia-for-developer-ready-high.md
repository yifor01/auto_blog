---
title: Run DiffusionGemma on NVIDIA for Developer-Ready, High-Throughput Text Generation
source: NVIDIA Developer
url: https://developer.nvidia.com/blog/run-diffusiongemma-on-nvidia-for-developer-ready-high-throughput-text-generation/
score: 102
model: google/gemma-4-31b-it:free
generated_at: '2026-06-25T20:21:06.277079'
---

📌 【NVIDIA】DiffusionGemma 實現文字平行生成，單張 H100 吞吐量達 1,000 tokens/sec

TL;DR：DiffusionGemma 捨棄逐字生成，改用擴散去噪平行產生 Token，大幅提升文字生成吞吐量。

對於開發即時 AI 助手或 Agentic 工作流的工程師來說，最頭痛的往往是 LLM 逐個 Token 生成的低速，這不僅導致使用者體驗不流暢，更直接推高了伺服器的推理成本。

🤔 **突破逐字生成的效能瓶頸**

傳統的文字生成模型採取循序漸進（sequential）的方式，一次僅能產生一個 Token。DiffusionGemma 改變了這個邏輯，它引入擴散去噪（diffusion-based denoising）機制，讓模型能夠在每一步驟中平行生成 256 個 Token，從而打破速度限制。

🧩 **基於 Gemma 4 MoE 架構的平行生成**

DiffusionGemma 由 Google DeepMind 開發，並針對 NVIDIA 平臺進行最佳化。其核心技術特點如下：
- **模型架構**：基於 Gemma 4 26B A4B MoE（混合專家模型）架構。
- **生成方式**：利用擴散去噪技術，將原本的循序生成轉化為平行生成。
- **格式支援**：支援 BF16 與 NVFP4 格式，以提升運算效率。

📊 **不同硬體平臺的吞吐量表現**

根據 NVIDIA 提供的資料，DiffusionGemma 在不同硬體上的生成速度表現顯著：
- **NVIDIA H100 Tensor Core GPU**：單張卡最高可達 1,000 tokens/sec。
- **NVIDIA DGX Station**：最高可達 2,000 tokens/sec。
- **NVIDIA DGX Spark**：最高可達 150 tokens/sec。

對於企業級應用而言，這種高吞吐量意味著能支援更高的併發數（concurrency）並降低單次請求的服務成本。

🎯 **實務啟示：快速部署與整合路徑**

開發者若想將此高吞吐量能力匯入生產環境，可透過以下三種路徑快速實作：
1. **原型開發**：透過 Hugging Face 獲取模型。
2. **生產部署**：利用 NVIDIA NIM 進行高效能部署。
3. **模型微調**：使用 NVIDIA NeMo AutoModel 進行針對性的 fine-tuning。

🔗 **來源**
- 標題：Run DiffusionGemma on NVIDIA for Developer-Ready, High-Throughput Text Generation
- 作者／機構：Anu Srivastava / NVIDIA Developer
- 連結：https://developer.nvidia.com/blog/run-diffusiongemma-on-nvidia-for-developer-ready-high-throughput-text-generation/

#DiffusionGemma #NVIDIA #GoogleDeepMind #LLM #MoE #HighThroughput #TextGeneration #H100 #NIM #NeMo
