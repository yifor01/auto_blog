---
title: NVIDIA Vera Rubin NVL72 Achieves up to 2x Blackwell Ultra Performance in MLPerf
  Training v6.1
source: NVIDIA Developer
url: https://developer.nvidia.com/blog/nvidia-vera-rubin-nvl72-achieves-up-to-2x-blackwell-ultra-performance-in-mlperf-training-v6-1/
model: claude-code/sonnet
generated_at: '2026-11-17T01:03:12.515600'
score: 89
---

📌 NVIDIA Vera Rubin 架構首秀 MLPerf 訓練榜：七項裡拿下六項最快

TL;DR：MLPerf Training v6.1 首次納入 Vera Rubin 架構成績，六項 benchmark 效能達 GB300 NVL72 的 1.4 到 2 倍。

當 AI agent 要處理的任務愈來愈複雜，縮短 time-to-train（訓練所需時間）就直接決定一個團隊每季能跑多少次模型與 agent 的迭代實驗。MLPerf Training v6.1 是 NVIDIA Vera Rubin 架構的首次亮相，而結果顯示其 CUDA 軟體堆疊在第一輪就已相當成熟。

📊 七項裡六項最快，最後一項交給規模取勝

Vera Rubin NVL72 在七項 benchmark 中的六項拿下最快訓練時間，相較高度最佳化過的 GB300 NVL72 最多快了 2 倍。剩下的第七項 DeepSeek-V3 671B，NVIDIA 則改用一座 10,240 顆 GPU 的 GB300 NVL72 叢集，拿下本輪全場最快的絕對成績。NVIDIA 是這一輪唯一提交完整七項 benchmark 成績的廠商，Vera Rubin 在首次亮相就跑完整套測試。

| 模型類型 | Benchmark | GPU 數量 | Vera Rubin 相對 GB300 倍數 |
|---|---|---|---|
| MoE | DeepSeek-V3 671B | 1,024 | 2x |
| MoE | Qwen3.5 397B GRPO (RL) | 64 | 1.4x |
| MoE | gpt-oss 20B | 64 | 1.6x |
| Dense | Llama 2 70B LoRA | 72 | 1.5x |
| Dense | Llama 3.1 8B | 72 | 1.6x |
| Diffusion | FLUX.1 | 72 | 1.5x |
| Recommender | DLRMv4 | 128 | 1.4x |

從表中可以看出一個規律：模型規模愈大、通訊負擔愈重，Vera Rubin 的優勢就愈明顯，其餘項目則穩定落在 1.4 到 1.6 倍之間，涵蓋語言、影像生成、推薦系統與強化學習等不同模態與架構。

🧩 DeepSeek-V3 671B：通訊最吃重的一項，優勢也最大

DeepSeek-V3 671B 是一個 6,710 億參數、token-dropless 的 MoE 模型，是整套測試裡負擔最重的工作負載，因為專家平行（expert parallelism）會讓每一輪迭代都伴隨大量 all-to-all 通訊，網路效率因此直接反映在訓練時間上。Vera Rubin NVL72 用 1,024 顆 GPU（16 個機櫃）把這項訓練壓到 4.14 分鐘，GB300 NVL72 在相同的 1,024 顆 GPU 配置下則需要 8.03 分鐘，接近 2 倍差距，是本輪最大的世代提升。而在更大規模下，GB300 NVL72 用 10,240 顆 GPU（160 個機櫃）跑出 1.38 分鐘的全場最快絕對成績，證明其橫向擴展架構即便超出單一機櫃規模仍然穩定。

🧩 agentic RL post-training 首度登場，Vera Rubin 拿下第一

MLPerf Training v6.1 新增了第一個 agentic LLM 強化學習 post-training benchmark：Qwen3.5 397B GRPO。這類工作負載會不斷產生 rollout、評分、更新權重，對推論引擎與訓練引擎之間的大量權重搬移特別吃重。Vera Rubin NVL72 在 1,024 顆 GPU 下以 10.44 分鐘拿下最快成績（NeMo RL 搭配 TensorRT-LLM），GB300 NVL72 同規模則需要 13.78 分鐘；Vera Rubin 同時也用 vLLM 作為推論後端跑出 10.94 分鐘，證明同一套硬體能支援兩種不同的推論後端。由於驅動模擬環境高度 CPU-bound，Vera CPU 在這裡扮演關鍵角色：單一 Vera CPU 機櫃的 256 顆 CPU 可以同時撐住超過 22,500 個並行 RL 環境，在 GPU 全力生成 token 與更新權重的同時，CPU 端持續模擬環境、餵進回饋訊號。

🧩 機櫃內外的網路協同設計

機櫃內部，Vera Rubin NVL72 透過銅纖 NVLink 6 spine 連接 72 顆 GPU 與 36 顆 CPU，每 GPU 頻寬達 3.6 TB/s、每機櫃合計 260 TB/s，讓 MoE 的專家派發（expert dispatch）不會卡在關鍵路徑上。跨機櫃則透過 ConnectX-9 SuperNIC，走 Quantum-X800 InfiniBand 或 Spectrum-X Ethernet 向外擴展，兩種架構都用 adaptive routing 與壅塞控制來隱藏 MoE 突發流量造成的通訊延遲。這樣的設計直接反映在數字上：DeepSeek-V3 benchmark 從 256 顆 GPU 擴展到 1,024 顆 GPU（4 個機櫃到 16 個機櫃）時，Vera Rubin NVL72 維持了 97% 以上的整體擴展效率。

🎯 實務啟示

對規劃訓練基礎設施的團隊來說，這輪結果值得關注的不是單一數字，而是覆蓋面：從大規模預訓練到 agentic RL post-training 全部拿下最快成績，說明效能提升不是集中在某一種模型架構，而是貫穿整條建模流程。NVL72 維持一致的 72-GPU 機櫃網域設計，也意味著每一代升級都能帶來可預期的效能提升，不需要為此改變既有的維運方式。

🔗 來源
- 標題：NVIDIA Vera Rubin NVL72 Achieves up to 2x Blackwell Ultra Performance in MLPerf Training v6.1
- 作者／機構：Farshad Ghodsian, NVIDIA Developer
- 連結：https://developer.nvidia.com/blog/nvidia-vera-rubin-nvl72-achieves-up-to-2x-blackwell-ultra-performance-in-mlperf-training-v6-1/

#NVIDIA #VeraRubin #MLPerf #AITraining #GPU #MoE #ReinforcementLearning #NVLink #AIInfrastructure #DeepSeek
