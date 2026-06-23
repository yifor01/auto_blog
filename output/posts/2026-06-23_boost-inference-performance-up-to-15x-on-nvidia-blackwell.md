---
title: Boost Inference Performance up to 15x on NVIDIA Blackwell Using DFlash Speculative
  Decoding
source: NVIDIA Developer
url: https://developer.nvidia.com/blog/boost-inference-performance-up-to-15x-on-nvidia-blackwell-using-dflash-speculative-decoding/
score: 102
model: google/gemma-4-31b-it:free
generated_at: '2026-06-23T20:24:30.577733'
---

📌 【NVIDIA】DFlash 區塊擴散解碼，將 Blackwell 推論效能提升至 15 倍

TL;DR：DFlash 透過區塊擴散模型將推測解碼從「序列生成」轉為「並行生成」，大幅提升 LLM 吞吐量與互動速度。

當 AI 系統從單次對話演進為複雜的多代理人（multi-agent）協作工作流時，推論延遲成為最大的瓶頸。傳統自迴歸（Autoregressive）LLM 必須逐個生成 token，這種序列化過程導致 GPU 利用率低，在對延遲敏感的服務場景中嚴重限制了吞吐量。

🤔 **從逐字生成到區塊並行的挑戰**

為了緩解上述瓶頸，推測解碼（Speculative Decoding）通常使用一個輕量化模型來預測未來的 token，再由大型目標模型進行並行驗證。然而，傳統的草稿模型（drafter）依然是序列化生成，這在一定程度上限制了加速效果。

🧩 **DFlash：將推測解碼轉化為區塊並行工作**

NVIDIA 推出的 DFlash 是一個開源的輕量化區塊擴散模型（block diffusion model），其核心設計理念在於改變草稿生成的邏輯：

- **區塊生成**：DFlash 不再逐個生成 token，而是在單次前向傳播（forward pass）中直接生成一整塊候選 token 區塊。
- **效能轉換**：將原有的序列化草稿過程轉化為 GPU 擅長的區塊並行運算。
- **品質保證**：在加速的同時，依然能保持目標模型原有的輸出品質。

📊 **實測效能：吞吐量最高提升 15 倍**

根據 NVIDIA 提供的基準測試，DFlash 在不同模型與框架上的表現顯著優於現有方案（如 EAGLE-3）：

- **吞吐量突破**：在 gpt-oss-120b 模型上，吞吐量提升最高可達 15 倍。
- **互動速度翻倍**：在相同併發數下，Llama 3.1 8B 的互動速度幾乎翻倍。
- **跨模型加速**：在 vLLM 與 SGLang 框架下，Gemma 4 31B 提升達 5.8 倍，Qwen3 8-B 提升達 5.1 倍。

🎯 **實務啟示：無痛整合至現有推論框架**

對於 AI 工程師而言，DFlash 的最大價值在於其高相容性與低部署門檻：

1. **無需重構程式碼**：DFlash 已整合至 SGLang、vLLM 與 TensorRT-LLM 等主流推論框架，開發者可直接採用。
2. **快速部署**：可直接使用 Hugging Face 上釋出的模型權重（checkpoints）。
3. **硬體適配**：支援多種 NVIDIA GPU 架構與模型系列，特別是在 Blackwell 架構上能發揮最大效能。

🔗 **來源**
- 標題：Boost Inference Performance up to 15x on NVIDIA Blackwell Using DFlash Speculative Decoding
- 作者／機構：Amr Elmeleegy, Benjamin Chislett, Fernando Xiong, Michael Iovine, Omri Almog and Hao Zhang @ NVIDIA Developer
- 連結：https://developer.nvidia.com/blog/boost-inference-performance-up-to-15x-on-nvidia-blackwell-using-dflash-speculative-decoding/

#NVIDIA #Blackwell #LLM #SpeculativeDecoding #DFlash #Inference #vLLM #SGLang #TensorRTLLM #GPU
