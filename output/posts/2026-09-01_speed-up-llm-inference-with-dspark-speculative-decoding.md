---
title: Speed Up LLM Inference with DSpark Speculative Decoding
source: KDnuggets
url: https://www.kdnuggets.com/speed-up-llm-inference-with-dspark-speculative-decoding
model: claude-code/sonnet
generated_at: '2026-09-01T10:47:43.551745'
score: 92
---

📌 【DeepSeek】DSpark 讓本地推理生成快了 31%

TL;DR：DeepSeek 的 DSpark 投機解碼在 llama.cpp 上讓 Qwen3-8B 生成速度提升約 31%，同一張 GPU 不加卡也能跑更快。

多加幾張 GPU 不是唯一的加速方式，投機解碼（speculative decoding）不需要更多硬體,就能讓生成速度變快。

🤔 **投機解碼的幾種流派**

傳統做法用一個較小的草稿模型（draft model）先生成候選 token，再由主模型驗證；Multi-Token Prediction（MTP）則一次預測多個未來 token；Medusa 與 EAGLE 改進草稿的產生方式；DFlash 則平行產生一整塊候選 token。DeepSeek 的 DSpark 走另一條路：把平行草稿與一個輕量的序列化元件結合在一起。

🧩 **平行速度 + 序列資訊，兩者兼顧**

平行草稿模型能一次生成一整塊 token，速度快，但區塊後段的預測因為不完全依賴前面已預測出的 token，準確度容易下降。DSpark 用平行骨幹搭配一個輕量的序列化元件，讓後段的草稿位置能夠參考前面已預測 token 的資訊，同時保留平行生成大部分的速度優勢。DSpark 也能估計草稿 token 通過驗證的機率，讓信心較低的區塊部分可以直接被丟棄，省下驗證運算，llama.cpp 的實作也開放了信心門檻（confidence threshold）這個選項。

🧩 **實測設定：Qwen3-8B + llama.cpp + CUDA**

作者從原始碼建置最新版 llama.cpp 並啟用 CUDA，接著下載 Qwen3-8B 的 Q4_K_M 目標模型與對應的 dspark-Qwen3-8B Q8_0 草稿模型。基準測試先在不啟用投機解碼的情況下跑一次生成，再用相同的 prompt、token 上限與 decoding 設定（`--temp 0 --top-k 1`），加上 `-md` 載入草稿模型、`--spec-type draft-dspark`、`--spec-draft-n-max 3` 等參數重新跑一次，確保兩次測試盡量是同條件比較。

📊 **實測結果：95.0 → 124.9 tokens/s**

| 設定 | Prompt 速度 | 生成速度 |
|---|---|---|
| Qwen3-8B 基準 | 294.6 t/s | 95.0 t/s |
| Qwen3-8B + DSpark | 88.0 t/s | 124.9 t/s |

生成速度從 95.0 提升到 124.9 tokens/s，大約是 1.31 倍、31.5% 的提升。文中也提到 prompt 處理速度在啟用 DSpark 後反而變低，但作者強調這次測量的重點是自迴歸生成速度，對於需要產生較長回應的任務，生成端的吞吐量提升影響會更明顯。

💡 **DeepSeek 官方數字僅供參考，不代表這次實測結果**

文中提到，DeepSeek 官方宣稱在 DeepSeek-V4 的正式部署中，DSpark 相較先前 MTP-1 生產基準線，將每使用者生成速度提升了 60–85%。作者特別提醒，這個數字不應被當作小型本地模型的預期表現，因此才自行實測比較，兩者情境並不直接可比。

⚠️ **模型支援仍是最大限制**

作者認為，就本地 LLM 加速而言，MTP 仍然是更實用的選項，原因是設定更簡單、支援的模型範圍也更廣。DSpark 的優勢在於草稿品質較好時，可以帶來更高的 token 接受率，但目前只有少數模型有相容的 DSpark 草稿模型可用，llama.cpp 中的支援也還很新，依模型與建置版本不同，可能會遇到臭蟲或不穩定的情況。

🎯 **實務啟示**

如果手上剛好有支援的模型組合，DSpark 在 llama.cpp 中設定門檻不高，值得直接拿現有 GPU 實測比較；但若模型選擇有限或追求穩定性，MTP 目前仍是更廣泛可用的加速路線。

🔗 **來源**
- 標題：Speed Up LLM Inference with DSpark Speculative Decoding
- 作者／機構：Abid Ali Awan, KDnuggets
- 連結：https://www.kdnuggets.com/speed-up-llm-inference-with-dspark-speculative-decoding

#DeepSeek #DSpark #SpeculativeDecoding #LLMInference #llamacpp #Qwen3 #CUDA #LLMOptimization #GPUAcceleration #LocalLLM
