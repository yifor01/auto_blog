---
title: Accelerating Dropless MoE Training in JAX with NVIDIA Transformer Engine
source: NVIDIA Developer
url: https://developer.nvidia.com/blog/accelerating-dropless-moe-training-in-jax-with-nvidia-transformer-engine/
model: claude-code/sonnet
generated_at: '2026-09-14T21:06:26.049198'
score: 109
---

📌 【NVIDIA】Dropless MoE 訓練提速10.4倍，瓶頸到底在哪？

TL;DR：NVIDIA以JAX搭配Transformer Engine最佳化MoE訓練，單GPU算力從103衝到1068 TFLOPS。

DeepSeek、Qwen、Mixtral這類MoE模型能用更少的訓練算力打贏dense模型的效能，但很少人注意到，在GB200上跑DeepSeek-V3訓練時，一個未最佳化的baseline版本，GPU有高達84%的核心運算時間，其實都花在等跨GPU通訊上，實際算力只有103 TFLOPS/GPU。

🤔 為什麼MoE訓練特別難最佳化

Dense模型裡，每個token都流經同一顆前饋網路（FFN），GEMM形狀規則、批次容易堆疊。MoE不一樣：router會動態把token分配給Top-K個專家，而且router是學出來的，訓練過程中會逐漸偏好特定專家，每個batch、甚至同一batch裡每個專家收到的token數都不一樣。這代表沒有乾淨的矩形GEMM可用，只有形狀不規則的「ragged tensor」。多數函式庫是為均勻矩形資料最佳化的，遇到這種情況效率自然打折。再加上expert parallelism（EP）底下，token要被dispatch到對的GPU、算完再combine回原本順序，如果這條路徑沒處理好，通訊就會主導整個訓練流程，GPU大半時間在等資料而非做運算。

🧩 Dropless與capacity-based，兩種取捨

文章區分了兩種MoE訓練策略：capacity-based MoE會給每個專家固定的token額度，超出的部分要嘛被丟棄、要嘛被padding塞進去，計算規則、硬體友善，但要在模型品質（丟token）與效能（padding浪費算力）之間二選一。Dropless MoE則堅持每個token都要被指定的專家處理，不管負載多不均衡，這對模型品質更有利，但對系統的要求也更高，需要MegaBlocks論文提出的block-sparse矩陣乘法思路，把專家運算重新表達成可變長度的稀疏GEMM。

Transformer Engine針對dropless MoE在JAX上提供三個關鍵構件：group-aware MXFP8量化、MXFP8 grouped GEMM，以及最佳化過的EP dispatch/combine運算。

過去要處理不規則的專家GEMM，常見做法是用迴圈跑多次GEMM kernel（需要把token數從裝置複製回主機，這會卡在關鍵路徑上並打斷CUDA graph），或是用batched GEMM把所有專家都補齊到最壞情況的token容量（等於白算一堆padding）。Grouped GEMM改用單一kernel呼叫處理所有專家矩陣乘法，各自只計算實際擁有的token數量，不需要事先知道形狀就能維持CUDA graph完整。這套grouped_gemm／ragged_dot介面是用cuBLAS與cuBLASLt實作，在Blackwell GPU上還能開啟MXFP8 block scaling，讓Tensor Core在不規則專家形狀下依然能被充分利用。

至於dispatch與combine，naive做法是把兩個階段串成一條序列，GPU中間會停下來等資料、記憶體被反覆讀寫，通訊與運算彼此空等。Transformer Engine把dispatch與combine整合進同一條融合kernel路徑，並交由NCCL EP這個專為expert parallel不規則流量設計的通訊後端處理，其中還內建token去重機制：當同一個token要被送到同一rank上的多個專家、或同一遠端InfiniBand節點上的多個rank時，資料只需經過網路傳輸一次，再於接收端複製，藉此省下頻寬。除此之外，還有JAX host offloading（forward pass過程中，中間activation不必整段都留在裝置記憶體上）與XLA multistreaming collectives等額外最佳化。

📊 GB200上實測：10.4倍效能提升

以DeepSeek-V3在GB200上的訓練為例，未最佳化的baseline只有103 TFLOPS/GPU，其中84%的累積kernel時間耗在跨GPU通訊上；導入JAX加上Transformer Engine的這套目標式kernel最佳化後，實測達到1,068 TFLOPS/GPU，等於10.4倍的效能提升。

💡 深入分析：grouped GEMM與EP是互補的兩塊拼圖

文章把grouped GEMM與EP定位成一組互補關係：grouped GEMM處理「每個專家內部發生了什麼」，EP處理「專家周圍的一切」，也就是token怎麼被送過去、怎麼被送回來。少了任何一塊，另一塊最佳化得再好，整體效能都會被拖累。

🎯 實務啟示

如果團隊正在NVIDIA GPU叢集上用JAX訓練自己的MoE模型，與其自己手刻dispatch迴圈或忍受padding造成的算力浪費，直接採用Transformer Engine提供的grouped GEMM與整合式EP dispatch/combine原語，會是更務實的起點，尤其是在導入expert parallelism、且不想在通訊與GPU利用率之間反覆權衡的情況下。

🔗 來源
- 標題：Accelerating Dropless MoE Training in JAX with NVIDIA Transformer Engine
- 作者／機構：Tanya Lenz，NVIDIA Developer
- 連結：https://developer.nvidia.com/blog/accelerating-dropless-moe-training-in-jax-with-nvidia-transformer-engine/

#MoE #JAX #NVIDIA #TransformerEngine #GPUOptimization #DeepLearning #LLMTraining #ExpertParallelism #GroupedGEMM #DeepSeek
