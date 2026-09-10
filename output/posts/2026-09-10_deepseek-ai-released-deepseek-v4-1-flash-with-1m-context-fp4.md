---
title: DeepSeek AI Released DeepSeek-V4.1-Flash with 1M Context, FP4 KV Cache, and
  Cross-Layer Attention Reuse
source: MarkTechPost
url: https://www.marktechpost.com/2026/09/10/deepseek-ai-released-deepseek-v4-1-flash-with-1m-context-fp4-kv-cache-and-cross-layer-attention-reuse/
model: claude-code/sonnet
generated_at: '2026-09-10T19:53:27.084882'
score: 117
---

📌 【DeepSeek 最新技術報告】890 Bytes KV Cache，如何撐起百萬 Token 上下文？

TL;DR：DeepSeek-V4.1-Flash 用 Encoder-Decoder 分工加 FP4 量化，把 KV cache 壓到 890 Bytes/Token。

當 Agent 開始動輒處理百萬 token 的長上下文，真正吃緊的往往不是算力，而是 KV cache 佔用的 HBM、SSD 容量與頻寬。DeepSeek AI 這次的新模型，幾乎是整個繞著這個瓶頸設計的。

🤔 **長上下文 Agent 把 LLM Serving 變成了 Input 密集型負載**

反覆的 prefill 加上百萬 token 的上下文，讓 KV cache 的儲存與搬移成本急遽膨脹。DeepSeek-V4.1-Flash 是一個多模態 Mixture-of-Experts 模型，backbone 有 552B 參數，額外還有 196B 的 Engram 參數，支援 1M token 上下文窗口。Prefill 階段每個 token 只啟動 8B 參數，decode 階段啟動 16B。開源權重採用 MIT 授權，已支援 vLLM、SGLang 與 Hugging Face 上的 Transformers 部署路徑，官方 API 也提供 low、high、max 三種推理強度。

🧩 **Causal Encoder-Decoder 拆分，Prompt 只走一半**

40 層的 backbone 被拆成 20 層 causal encoder 與 20 層 decoder。受 YOCO 架構啟發，decoder 不再自行計算全域 KV，而是透過每層的投影權重，直接從 encoder 最後一層的隱藏狀態推導出來。也就是說，prompt token 的運算到 encoder 就結束，這讓 prefill 的計算量幾乎減半。每一層仍保留 128-token 窗口的 Sliding-Window Attention（SWA），decoder 端的 SWA 狀態則只需重播 prompt 最後 128 個 token 就能重建，官方稱之為「Decoder SWA Bounded Replay」。

在 attention 壓縮上，V4 是 CSA 與 Heavily Compressed Attention 混用，V4.1-Flash 則改用純 CSA2，並且沿著「層」這個軸去砍快取。18 層 encoder 以壓縮比 2 分成 3 組（每組 6 層：1 層 Full、5 層 Reuse），20 層 decoder 則以壓縮比 1 分成 5 組（每組 4 層：第一組是 Full 加 3 層 Reuse，其餘各組是 Reindex 加 3 層 Reuse）。decoder 中還有一個 Hierarchical Sparse Indexer，讓 Full 層建立一個最多 16,384 個位置（2,048 個區塊、每區塊 8 個位置）的候選池，後面的 Reindex 層只需要在這個有限集合裡打分，而不用掃過整個上下文。

主要的 KV cache 被量化成 E2M1 格式，每 16 個通道搭配一個 E4M3 的 scale，走的是類似 NVFP4 但不含全域 scale 的方案，並在後訓練階段透過 quantization-aware training 導入，儲存量比 V4 的 FP8 快取再減半。部署層面也做了分層：SWA KV 不再落地到 SSD，而是放進由 10% host DRAM 切出來的分散式記憶池，TTL 只有數分鐘；全域 KV 則保證 72 小時的生命週期。一旦 SWA 快取 miss，只需重算 128 個 token，而不是「層數 × 窗口大小」那麼多。

其他改動還包括 Single-Pass mHC（把輸入混合係數平移一個 block，讓融合後的 Mega-mHC kernel 可以把 activation 記憶體流量砍半）、放在第 1 和第 14 層的 Engram 條件記憶模組、在預訓練完成後、backbone 凍結狀態下訓練出來的 DSpark 推測解碼，以及 head-wise Muon 最佳化器。

📊 **關鍵數字：KV cache 縮小 437 倍，decode FLOPs 幾乎不隨長度暴增**

全域 KV cache 的最終落地數字是每 token 890 bytes，大約是 DeepSeek-V4-Flash 的四分之一，比起 DeepSeek-V1 更是縮小了約 437 倍。上下文從 4K 拉長到 1M 時，單一 token 的 decode FLOPs 只增加約四分之一。預訓練用了 45T 多模態 token，文字與多模態比例約 7:1；稀疏 attention 從零開始在 64K 序列長度訓練、沒有 dense warmup，隨後在 34T token 規模下把上下文擴展到 1M。Base 模型在世界知識與程式能力上追平 DeepSeek-V4-Pro-Base，但只用了三分之一的總參數與四分之一的啟用參數。

💡 **後訓練沒有新演算法，靠的是規模與多樣性**

官方表示後訓練階段並未引入新演算法，效能提升主要來自大規模合成的可驗證 agent 任務、跨異質 scaffold（Claude Code、Codex、OpenCode、Pi、mini-SWE、DeepSeek Harness）的 RL 訓練，以及來自超過 40 個 teacher 模型的 on-policy distillation。

🎯 **實務啟示**

對於要自建長上下文 Agent 服務的團隊，V4.1-Flash 提供了一份相對完整的「KV cache 工程手冊」：encoder/decoder 分工降低 prefill 成本、分層 attention 壓縮降低快取體積、FP4 量化降低儲存位元數、再搭配分層式記憶體生命週期管理。這些手法即使不直接採用這個模型，也值得作為自家推理系統最佳化的參考藍圖。

🔗 **來源**
- 標題：DeepSeek AI Released DeepSeek-V4.1-Flash with 1M Context, FP4 KV Cache, and Cross-Layer Attention Reuse
- 作者／機構：Asif Razzaq, MarkTechPost
- 連結：https://www.marktechpost.com/2026/09/10/deepseek-ai-released-deepseek-v4-1-flash-with-1m-context-fp4-kv-cache-and-cross-layer-attention-reuse/

#DeepSeek #DeepSeekV4 #LLM #MixtureOfExperts #KVCache #FP4 #Quantization #LongContext #OpenWeights #AIInfrastructure
