---
title: Creating the NVIDIA Nemotron 3 Ultra NVFP4 Checkpoint with NVIDIA Model Optimizer
source: NVIDIA Developer
url: https://developer.nvidia.com/blog/creating-the-nvidia-nemotron-3-ultra-nvfp4-checkpoint-with-nvidia-model-optimizer/
score: 96
model: google/gemma-4-31b-it:free
generated_at: '2026-06-26T20:02:52.253524'
---

📌 【NVIDIA 技術分享】利用 NVFP4 量化將 Nemotron 3 Ultra 記憶體佔用降低 3.2 倍

TL;DR：透過 NVIDIA Model Optimizer 將 Nemotron 3 Ultra 量化為 NVFP4，在維持 BF16 準確度的同時，大幅提升推論吞吐量。

隨著 Context Window 越來越長，高效搬運巨大的模型權重已成為影響效能的關鍵瓶頸。為了降低記憶體佔用並提升速度，量化（Quantization）成為主流方案，而 NVIDIA 在 Blackwell 架構中引入的 NVFP4（4-bit 浮點數）則提供了更極端的壓縮可能性。

🤔 **解決大模型權重搬運的效能瓶頸**

在 decode-heavy（解碼密集型）的工作負載中，權重搬運的效率直接決定了推論速度。NVIDIA 針對 Nemotron 3 Ultra (550B) 採用 NVFP4 量化，旨在將模型壓縮至更小格式，以減少硬體資源佔用並提升吞吐量。

🧩 **非單一格式的混合精度量化策略**

許多開發者誤以為 NVFP4 檢查點的所有層都使用 NVFP4 儲存，但實際上，為了維持模型準確度，NVIDIA 採用了針對不同層之敏感度進行的混合精度設計：

- **維持 BF16 精度**：Embedding 層、Output classification 層以及 MTP 層，由於對準確度影響較大，因此保留 BF16。
- **量化至 NVFP4**：MoE routed experts 等層則被量化為 NVFP4 以降低體積。

這種根據層敏感度選擇精度的做法，讓模型在大幅壓縮的同時，仍能在幾乎所有基準測試中達到與 BF16 相當的準確度。

📊 **3.2 倍的空間壓縮與顯著的吞吐量提升**

透過 NVIDIA Model Optimizer 進行量化後，Nemotron 3 Ultra 展現了顯著的效能提升：

- **體積縮減**：模型大小從 BF16 的 1,121 GB 縮減至 352.3 GB，達到 3.2 倍的壓縮率，硬體佔用直接減半。
- **推論效能**：在 decode-heavy 工作負載下，其推論吞吐量最高可達 GLM-5.1 754B FP4 模型的 5.9 倍。

🎯 **實務啟示**

對於部署超大型模型（如 500B 級別）的工程師來說，盲目地將所有層量化為低位元可能會導致準確度崩潰。實務上的最佳做法是採取「混合精度量化」：識別對精度敏感的關鍵層（如 Embedding 或輸出層）並保留高精度，而將佔體積最大的權重層（如 MoE Experts）量化為 NVFP4，才能在效能與準確度之間取得最佳平衡。

🔗 **來源**
- 標題：Creating the NVIDIA Nemotron 3 Ultra NVFP4 Checkpoint with NVIDIA Model Optimizer
- 作者／機構：Seonghee Lee, Sachin Beldona, Carlo del Mundo, Chris Hoge and Trenton Starkey @ NVIDIA
- 連結：https://developer.nvidia.com/blog/creating-the-nvidia-nemotron-3-ultra-nvfp4-checkpoint-with-nvidia-model-optimizer/

#NVIDIA #Nemotron3 #NVFP4 #Quantization #Blackwell #ModelOptimizer #LLM #Inference #MoE #ModelCompression
