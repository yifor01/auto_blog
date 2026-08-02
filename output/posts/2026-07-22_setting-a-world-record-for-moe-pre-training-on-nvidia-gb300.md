---
title: Setting a World Record for MoE Pre-Training on NVIDIA GB300 NVL72
source: NVIDIA Developer
url: https://developer.nvidia.com/blog/setting-a-world-record-for-moe-pre-training-on-nvidia-gb300-nvl72/
model: tencent/hy3:free
generated_at: '2026-07-22T00:46:21.624751'
score: 92
---

這是一篇針對「產業新聞」型別的技術部落格文章。

📌 【NVIDIA】GB300 NVL72 創下世界紀錄：MoE 預訓練效能突破 1,648 TFLOPs/GPU

TL;DR：NVIDIA GB300 NVL72 透過硬體與軟體協同設計，在 DeepSeek-V3 訓練中創下驚人效能紀錄。

隨著 Frontier Model 的預訓練趨向 Mixture of Experts (MoE) 架構，訓練瓶頸已從單純的運算量，轉移到當每個 Token 的運算成本下降時，如何有效率地在數千顆 GPU 間進行通訊。

🧩 **硬體架構：透過 Rack-scale 設計解決通訊瓶頸**

為了應對 MoE 架構對通訊的高度需求，NVIDIA GB300 NVL72 採用了完全協同設計的 AI 基礎設施：

*   **第五代 NVLink**：提供低延遲、具備記憶體語意（memory-semantic）的機架內（intra-rack）通訊。
*   **高頻寬表現**：每顆 GPU 擁有 1.8 TB/s 頻寬，並具備 130 TB/s 的非阻塞式（non-blocking）All-to-All 頻寬。
*   **跨機架通訊**：透過 NVIDIA ConnectX-8 SuperNICs，搭配 Quantum-X800 InfiniBand 或 Spectrum-X Ethernet，確保多個機架間的效能穩定且可預測。

📊 **DeepSeek-V3 訓練創下世界紀錄**

在訓練 DeepSeek-V3 (671B) 的過程中，NVIDIA GB300 NVL72 展現了卓越的擴展性：

*   **效能指標**：每顆 GPU 達到了 1,648 TFLOPs 的預訓練效能。
*   **線性擴展性**：當規模從 256 顆 GPU 擴展至 1,024 顆 GPU 時，每顆 GPU 的吞吐量（throughput）仍能維持在 97% 以上。

💡 **軟體創新：驅動 3x 到 10x 的效能提升**

硬體效能的釋出，仰賴於 NVIDIA 在軟體層級的持續貢獻。透過 NVIDIA Megatron Core、TorchTitan 以及 JAX 等軟體創新，相較於前幾代產品，效能提升了 3 倍至 10 倍。這種硬體與軟體的持續協同設計，讓研究人員能在相同的基礎設施下，以更快的速度訓練更大規模的模型並進行更多實驗。

🎯 **實務啟示**

對於處理超大規模 MoE 模型的工程師而言，單純堆疊運算單元已不足夠；未來訓練效能的關鍵在於「擴展（Scale-up）」與「擴散（Scale-out）」網路的緊密耦合，以及軟體層級對大規模分散式訓練的最佳化能力。

🔗 **來源**
- 標題：Setting a World Record for MoE Pre-Training on NVIDIA GB300 NVL72
- 作者／機構：Kirthi Devleker, Farshad Ghodsian, Syed Ahmed and Sukru Burc Eryilmaz @ NVIDIA
- 連結：https://developer.nvidia.com/blog/setting-a-world-record-for-moe-pre-training-on-nvidia-gb300-nvl72/

#NVIDIA #MoE #DeepSeek #GB300 #NVLink #AIInfrastructure #MachineLearning #GenerativeAI #GPU #HighPerformanceComputing
