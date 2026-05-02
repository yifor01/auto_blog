---
title: "Moonshot AI Open-Sources FlashKDA: CUTLASS Kernels for Kimi Delta Attention with Variable-Length Batching and H20 Benchmarks"
source: MarkTechPost
url: https://www.marktechpost.com/2026/04/30/moonshot-ai-open-sources-flashkda-cutlass-kernels-for-kimi-delta-attention-with-variable-length-batching-and-h20-benchmarks/
score: 108
model: tencent/hy3-preview:free
generated_at: 2026-05-02T19:20:00.046044
---

📌 【Moonshot AI 开源】FlashKDA 长上下文加速

長上下文 LLM 推理最痛的 Prefill 瓶頸，終於有生產級開源解了。
Moonshot AI 剛放出 FlashKDA，H20 上 Prefill 加速最高 2.22 倍。
它還是 Kimi Linear 的核心組件，KV Cache 用量直接砍 75%。

🤔 **標準注意力二次複雜度卡死長上下文，線性注意力成主流方向**
標準 Softmax 注意力的計算複雜度與序列長度呈二次方關係，隨著上下文長度增加，運算成本會快速飆升，這也是長上下文 LLM 推理的核心瓶頸。為了解決這個問題，學界與產業界近年大力投入線性注意力機制研究，透過近似或替換 Softmax 操作實現線性縮放。
Kimi Delta Attention（KDA）是 Moonshot AI 提出的線性注意力方案，在 Gated DeltaNet 的基礎上加入更細粒度的逐通道（Channel-wise）門控機制，能更有效利用有限的有限狀態 RNN 記憶體。KDA 並非實驗室原型，而是 Moonshot 開源混合模型 Kimi Linear 的核心注意力機制：Kimi Linear 總參數 48B，激活參數僅 3B，採用 3:1 的 KDA 與 MLA（多頭潛在注意力）層比例，長序列生成時 KV Cache 用量最多減少 75%，100 萬上下文長度下的解碼吞吐量是全注意力模型的 6 倍。

🧪 **H20 實測 Prefill 加速 1.72-2.22 倍，支援可變長批次**
FlashKDA（Flash Kimi Delta Attention）是 Moonshot AI 開源的生產級 CUTLASS 基礎 Kernel 實作，對應 KDA 機制的完整運算邏輯，採用 MIT 協議釋出，程式碼託管於 GitHub。
這項實作可直接作為主流 flash-linear-attention 庫的即插即用後端，無需大幅修改現有程式碼即可接入。官方測試在 NVIDIA H20 GPU 上進行，對比 flash-linear-attention 基線，Prefill 階段速度提升幅度為 1.72× 至 2.22×，同時支援可變長度批次（Variable-Length Batching）處理，適配實際推理場景的動態請求長度。

 **Prefill 最高加速 2.22 倍，KV Cache 減量 75%**
FlashKDA 的核心價值在於將 KDA 機制的理論優勢轉化為實際推理效能：
- H20 GPU 上 Prefill 速度較基線提升 1.72× ~ 2.22×
- 搭載 KDA 的 Kimi Linear 模型，長序列生成 KV Cache 用量減少 75%
- 100 萬上下文長度下，解碼吞吐量為全注意力模型的 6 倍
FlashKDA 專門針對 Prefill 階段優化，是 Kimi Linear 能夠實現生產級長上下文推理的關鍵基礎設施。

💡 **生產級 Kernel 才是線性注意力落地的關鍵**
過去多數線性注意力方案僅停留在論文或實驗室原型階段，缺乏生產可用的高效 Kernel 實作，難以真正落地到實際業務中。FlashKDA 的特別之處在於：
1. 基於 CUTLASS 實作，性能經過生產環境驗證，已經跑在 Kimi Linear 的推理鏈路中
2. 相容現有生態，可直接接入 flash-linear-attention 庫
