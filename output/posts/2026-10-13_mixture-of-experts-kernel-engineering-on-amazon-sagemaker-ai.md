---
title: Mixture-of-Experts kernel engineering on Amazon SageMaker AI
source: AWS ML
url: https://aws.amazon.com/blogs/machine-learning/mixture-of-experts-kernel-engineering-on-amazon-sagemaker-ai/
model: claude-code/sonnet
generated_at: '2026-10-13T22:01:11.505640'
score: 105
---

📌 【AWS 實測】Hopper GPU 上,把矩陣轉置一下就能讓 MoE 快 2-4%

TL;DR:AWS 拆解 MoE fused kernel 在 Hopper 架構上的瓶頸,靠 swap-AB 轉置與後端選型拿到實測效能提升。

一行矩陣轉置,能不能讓一整個 MoE 推理 pipeline 變快?AWS 這篇文章給出的答案是:在 Hopper GPU 上,答案是可以,而且背後的原因全部來自 WGMMA 指令集的硬體限制,而不是演算法本身。

🤔 **decode 階段的 MoE,天生就和 Hopper 的指令集對不上**

NVIDIA Hopper 架構靠 WGMMA(Warp Group Matrix Multiply Accumulate)指令來跑矩陣乘法,這個指令由 128 個執行緒組成的 warpgroup 協同執行。問題在於它的操作數不對稱:矩陣列維度(M)在硬體層級被固定成 64,行維度(N)則可變。Operand A 必須對齊這個固定的 M=64,Operand B 才對齊可變的 N。這個限制是 ISA 層級的硬體事實,不是軟體可以繞過的邏輯。

在標準 MoE 層的矩陣乘法中,M 是 token 數(batch size),K 是 hidden dimension,N 是專家輸出維度。但在 decode 階段,系統一次只處理每個使用者序列的一個 token,所以 M 經常小到 1。這代表 Operand A 變成一個極薄的橫向向量(例如 1×4096),根本填不滿硬體強制要求的 64 列,WGMMA 執行時,大量 Tensor Core 的運算單元就處於「空轉」狀態。

更麻煩的是,fused MoE kernel 為了避免替每個專家分別啟動 kernel,會把所有被選中的專家一起分組運算,這讓有效的 N 維度(專家數 × 專家 intermediate size)在 top-k=8 的情境下膨脹到數萬甚至數十萬。M 小到 1、N 大到誇張,這個層級的不對稱比一般 dense layer 嚴重得多。

🧩 **把矩陣轉置,讓大維度去對齊硬體的「大列」**

AWS 的做法是利用矩陣轉置的代數性質,在進入 PTX assembly 層之前,把矩陣乘法反過來:B^T [N,K] × A^T [K,M] → C^T [N,M]。這個「Swap-AB」的動作把原本龐大的專家輸出維度 N(例如 8192)挪到第一個 operand 位置,剛好輕鬆填滿硬體強制的 64 列門檻,讓 Tensor Core 不再空轉。同時,因為大型、連續的權重區塊被放進了主要插槽,Hopper 的硬體拷貝引擎可以非同步地把資料從 shared memory 預取進暫存器,讓運算管線保持飽和,不需要 CPU 介入排程。

📊 **H200 上端到端輸出吞吐量提升 2-4%**

AWS 表示,這個優化在大規模 MoE 模型上,於 H200 實測帶來 2-4% 的端到端輸出吞吐量提升,並已經把這個優化上游貢獻回 vLLM,從 0.24.0 版開始可用。

💡 **後端選擇一樣重要:低併發下 Triton 比 CUTLASS 快**

除了 kernel 本身的排列方式,vLLM 內建的 MoE oracle 會依量化方案把運算路由到 Triton、FlashInfer+CUTLASS 或其他後端。AWS 的 profiling 發現,對 Hopper 上採用 FP8 tensor 量化的模型,Triton 後端在低併發情境下持續勝過預設的 FLASHINFER_CUTLASS 路徑。原因在於 CUTLASS 仰賴標準 C++ template,把 FP8 scaling、矩陣乘法、專家彙總拆成多個獨立數學運算,過程中需要反覆讀寫 HBM;Triton 後端則把整條 pipeline 合併成單一硬體 pass,資料只從 HBM 讀取一次,全程留在 GPU 的 SRAM 暫存器與運算檔案裡處理完才寫回,省掉拖慢 CUTLASS 的來回搬資料開銷,還搭配針對可變 token bucketing 設計的動態排程。

⚠️ **優化高度綁定硬體世代**

這整套優化的前提是 Hopper 的 WGMMA 固定 M=64 這個具體硬體事實,換到不同世代或不同廠商的架構,瓶頸位置與對應解法未必相同,需要重新做硬體層級的分析才能套用。

🎯 **如果你在跑 MoE 推理服務**

直接的行動項目很具體:確認你用的 vLLM 版本是否 ≥0.24.0 以吃到 Swap-AB 優化;如果你的 workload 是 FP8 量化且併發量不高,值得手動測試把 MoE 後端切到 Triton 是否比預設的 FlashInfer+CUTLASS 更快,而不是完全信任框架預設的路由決策。

🔗 **來源**
- 標題:Mixture-of-Experts kernel engineering on Amazon SageMaker AI
- 作者／機構:Mona Mona(AWS Machine Learning Blog)
- 連結:https://aws.amazon.com/blogs/machine-learning/mixture-of-experts-kernel-engineering-on-amazon-sagemaker-ai/

#MixtureOfExperts #GPUKernel #vLLM #NvidiaHopper #WGMMA #InferenceOptimization #CUDA #Triton #LLMInference #AWS
