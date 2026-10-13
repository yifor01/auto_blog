---
title: 'ReplaySSM: Rethinking State Storage for Faster Hybrid-Model Decoding'
source: NVIDIA Developer
url: https://developer.nvidia.com/blog/replayssm-rethinking-state-storage-for-faster-hybrid-model-decoding/
model: claude-code/sonnet
generated_at: '2026-10-12T23:46:59.438523'
score: 121
---

📌 【NVIDIA 新研究】SSM 解碼卡在記憶體頻寬？ReplaySSM 重寫 state 儲存法

TL;DR：NVIDIA 與 Princeton Dao AI Lab 合作提出 ReplaySSM，把 state 拆成 checkpoint 加 buffer，讓混合模型的 SSM 層解碼重新變快。

🎣 想像一個混合式 LLM 推理服務，真正拖慢速度的居然不是 attention 層，而是原本該又快又省的 SSM 層——這正是 NVIDIA 在服務端 batch size 下觀察到的現象。

🤔 **SSM 層為什麼反而變成瓶頸**

混合架構（hybrid model）把少量 attention 層與多個 state space model（SSM）層交錯排列，NVIDIA Nemotron 3、Qwen3.5 到 Qwen3.8、Kimi-K3、GLM-5.3-Flash 都是這樣設計，SSM 層採用 Mamba-2、Gated DeltaNet（GDN）或 Kimi Delta Attention（KDA）。SSM 層的設計初衷是加速解碼：用固定大小的 state 取代隨 context 長度成長的 KV cache。但在實際服務的 batch size 下，SSM 層而非 attention，才是最高達 100K token context 下的延遲瓶頸。SSM 層還讓兩個原本能穩定加速 attention 解碼的技巧——speculative decoding 與量化——變得複雜。

原因出在 SSM 每個解碼步驟同時做兩件事：讀取 state 產出這個 token 的輸出，以及更新 state 成為下一個 token 的 state。傳統解碼把這兩件事綁在一起，三個挑戰都由此而生：

- **state 記憶體傳輸量**：每一步都要讀出、寫回完整的 state，但實際算術量很小，等於是被 HBM 頻寬卡住而非算力。在 Nemotron-3-Super-NVFP4、batch size 256、單張 NVIDIA Blackwell Ultra B300 GPU 的測試中，SSM 層在長達 100K context 以內都是解碼步驟中最大的開銷來源，原因是層數多了五倍，加上單層 FP32 state 就要 4 MiB，相當於一個 FP8 KV cache entry（每 token 0.5 KiB）累積 8K token 的大小。
- **speculative decoding 的回滾問題**：drafter 先提出 T 個候選 token，驗證後若要回滾，attention 只需移動 KV cache 指標即可，但 SSM 一旦把草稿資訊摘要進 state，就沒有簡單的逆運算。vLLM 的變通做法是每個草稿 token 後都存一次 state 快照，等於每步一次讀、T 次寫，還會限制 GPU 記憶體能同時服務多少請求，導致 speculative decoding 在服務規模下對 SSM 幾乎沒有幫助。
- **state 量化誤差累積**：量化後的 state 既是輸出來源，也是下一次更新的輸入，捨入誤差會隨每一步重新進入遞迴；KV cache 則只是被多次讀取，不會寫回自己，因此能承受比 SSM state 更低的精度。

🧩 **把 state 拆成 checkpoint 加輸入 buffer**

ReplaySSM 把 SSM 的遞迴公式展開成一個長度為 h 的視窗：目前的 state 等於「衰減過的 checkpoint」加上「視窗內每個輸入所貢獻的加權外積總和」。傳統解碼是逐步計算左式，ReplaySSM 則改用右式：把 state 表示成一個 checkpoint，加上一小段最近輸入記錄的 buffer（以 Mamba-2 為例是衰減係數、value、key）。

大部分步驟（非 flush 步驟）只需把當前輸入附加進 buffer，直接從 checkpoint 加 buffer 算出輸出，完全不用存整個 state。等 buffer 累積到設定長度 L 筆記錄時才觸發 flush：把 buffer 裡的輸入折算進 checkpoint，把新的 checkpoint 寫回 HBM 一次，再清空 buffer。輸出結果與傳統解碼相比，差異僅在浮點運算誤差範圍內。

用三個問題概括：ReplaySSM 做了什麼——快取最近的 SSM 輸入，把 state 表示成 checkpoint 加這些輸入；改變了什麼——把輸出計算與 state 更新拆開，輸出每步都算，checkpoint 每個視窗才更新一次；達成什麼——降低 state 記憶體傳輸量、簡化 speculative decoding 的回滾、支援低精度 state 讀取而不讓捨入誤差透過遞迴持續累積。

📊 **大 batch 下明顯加速，單一請求則沒有感覺**

團隊在四個混合模型上評估：Nemotron-3-Nano-4B、Nemotron-3-Super-120B-A12B（Mamba-2，分別跑在 H100 與 B300），Qwen3.5-4B、Qwen3.5-122B-A10B（GDN，同樣分跑在 H100 與 B300）。ReplaySSM 在 vLLM 中實作，state 維持預設的 FP32 精度，視窗長度設為 L=16（四個模型表現最好的設定），speculative decoding 測試則用各模型自帶的 multi-token prediction（MTP）head 產生草稿 token。

因為非 flush 步驟只寫入少量輸入向量而非整個 state matrix，主要的 state 傳輸量大約減半。在服務規模的 batch size 256 下，解碼速度達到 1.46 倍以上；但在 batch size 1 時，其他延遲來源主導，ReplaySSM 在這些測試中沒有帶來加速效果。

⚠️ 材料明確指出，ReplaySSM 的記憶體傳輸優化在小 batch、互動式低延遲場景下不適用，效益集中在服務端大 batch size 的情境；至於 speculative decoding 回滾與量化誤差兩項好處的具體數字，原文對應段落未完整列出。

🎯 **實務啟示**

ReplaySSM 已整合進 NVIDIA TensorRT-LLM、vLLM、FlashInfer，並已在 GLM-5.3-Flash 與 Kimi-K3 的生產環境中運行，程式碼公開在 GitHub。對正在服務混合架構模型的團隊來說，這是一個不需要改動模型權重、可直接套用的推理層最佳化，特別適合高 batch size 的服務場景。

🔗 **來源**
- 標題：ReplaySSM: Rethinking State Storage for Faster Hybrid-Model Decoding
- 作者／機構：Michelle Horton（NVIDIA Developer；研究為 NVIDIA 與 Princeton Dao AI Lab 共同合作）
- 連結：https://developer.nvidia.com/blog/replayssm-rethinking-state-storage-for-faster-hybrid-model-decoding/

#SSM #Mamba2 #GatedDeltaNet #TensorRTLLM #vLLM #LLMInference #NVIDIA #HybridModels #SpeculativeDecoding #Quantization
