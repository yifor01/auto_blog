---
title: 'Smaller, faster, safer: running Kimi and GLM at scale'
source: Hacker News
url: https://blog.cloudflare.com/smaller-faster-safer-models/
model: tencent/hy3:free
generated_at: '2026-08-04T08:28:32.821788'
score: 107
---

📌 【Cloudflare Workers AI】如何在大規模部署下，讓 Kimi 與 GLM 跑得更快、更省成本？

TL;DR：透過量化 KV cache 與模型權重，Cloudflare 在不犧牲準確度的前提下，大幅提升了長文本模型的記憶體容量與推理效能。

面對 Moonshot 的 Kimi K-series 與 Z.ai 的 GLM 等大型 Mixture-of-Experts (MoE) 模型，工程師面臨的最大挑戰往往不是運算能力，而是 GPU 記憶體的限制。當處理長文本時，記憶體通常會先被 KV cache 佔滿，而非模型權重。

Cloudflare Workers AI 透過結合 SGLang 推理框架，開發了三項核心優化技術來解決這個問題。

🧩 **量化 KV cache：讓長文本容量翻倍**

當模型生成文字時，會將處理過的 token 的 attention keys (K) 與 values (V) 儲存在 KV cache 中。對於長文本模型，這個 cache 會迅速膨脹並耗盡記憶體。

- **技術手段**：將預設的 16-bit (BF16) 精度改為 8-bit 浮點數 (FP8, e4m3)。
- **實測結果**：以 Kimi K2.6 為例，在 H200 部署環境下，上下文容量從約 68.6 萬 tokens 提升至 137 萬 tokens，直接翻倍。
- **效能與成本**：雖然 FP8 在單個 token 的運算上會因轉換而微幅變慢，但它讓 GPU 能同時處理更多併發請求。在 64 併發時，FP8 的吞吐量比 BF16 高出約 41%，且每 token 成本降低約 30%。

📊 **壓縮模型權重：提升解碼階段的吞吐量**

除了 KV cache，模型權重本身也是記憶體大戶。

- **技術手段**：針對 GLM 5.2，將權重從 8-bit 浮點數壓縮至 4-bit 整數 (INT4)。
- **實測結果**：模型 Checkpoint 從 705 GB 縮減至 421 GB（約減少 40%）。在 8 路 tensor-parallel 部署下，單顆 GPU 的記憶體佔用從 88 GB 降至 52 GB，剩餘空間可容納約 118 萬 tokens 的 KV cache。
- **解碼與預填 (Prefill) 的差異化策略**：
    - **解碼階段 (Decode)**：受限於記憶體頻寬。INT4 權重減少了傳輸量，在低併發時，效能提升最高可達 55%。
    - **預填階段 (Prefill)**：屬於計算密集型 (compute-bound)。由於 INT4 需要展開回原格式，效能反而略低於 FP8。
    - **實務做法**：Cloudflare 採用分離設計，在解碼階段使用 INT4 以求快速，在預填階段使用 FP8 以求高吞吐。

💡 **建立 KV cache 完整性檢查：在高併發下保護資料正確性**

當我們透過量化技術讓更多請求共享單一 GPU 記憶體時，隨之而來的是資料安全性問題。為了防止 paged attention 或 continuous batching 在高壓下發生錯誤，Cloudflare 建立了一層防禦機制。

- **設計理念**：為每個物理 cache page 分配一個標籤 (tag)，並在讀取前檢查該 page 與請求預期是否匹配。若不匹配則直接中止請求，避免回傳錯誤資料。
- **效能成本**：透過將驗證改為獨立的 batch check（而非融合進 attention kernel），將對吞吐量與 p95 延遲的影響控制在 1% 以內。

🎯 **實務啟示**

對於需要部署長文本模型 (Long-context LLM) 的工程師來說，這項研究提供了兩個關鍵啟示：
1. **解耦設計的重要性**：針對預填 (Prefill) 與解碼 (Decode) 階段採用不同的量化策略，可以在不犧牲效能的情況下達到最佳化。
2. **記憶體與精度的平衡**：量化 KV cache 能極大化單一硬體的容量，且在經過測試後，對模型精準度（如 MMLU、GSM8K 等指標）的影響幾乎可以忽略不計。

🔗 **來源**
- 標題：Smaller, faster, safer: running Kimi and GLM at scale
- 連結：https://blog.cloudflare.com/smaller-faster-safer-models/

#AI #LLM #Cloudflare #MachineLearning #GPU #Inference #Quantization #Kimi #GLM #SGLang
