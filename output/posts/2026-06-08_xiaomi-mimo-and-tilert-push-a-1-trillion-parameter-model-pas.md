---
title: Xiaomi MiMo and TileRT Push a 1-Trillion-Parameter Model Past 1000 Tokens Per
  Second on Commodity GPUs
source: MarkTechPost
url: https://www.marktechpost.com/2026/06/08/xiaomi-mimo-and-tilert-push-a-1-trillion-parameter-model-past-1000-tokens-per-second-on-commodity-gpus/
score: 99
model: google/gemma-4-31b-it:free
generated_at: '2026-06-08T20:37:58.172843'
---

📌 【小米最新研究】萬億參數模型突破 1000 TPS，商品級 GPU 也能跑出極速推理

當模型規模攀升至萬億（Trillion）參數時，推理速度（Inference Speed）往往成為部署的最大瓶頸。要在不依賴昂貴定制晶片的情況下，讓這種量級的模型達到每秒 1000 個 Token 的輸出速度，目前幾乎被認為是不可能的任務。

但小米 MiMo 團隊與 TileRT 系統組合作，證明了這在標準商品級 GPU 上是可以實現的。

🤔 **萬億參數的規模，與記憶體頻寬的死鬥**

對於萬億參數模型而言，最大的挑戰不在於運算力，而在於「記憶體頻寬」。即便使用 FP8 或 FP16 精度，巨大的權重數據在記憶體與 GPU 核心之間傳輸的壓力極其沉重，導致解碼速度（Decode Speed）緩慢。

小米提出的 MiMo-V2.5-Pro-UltraSpeed 並非追求提升模型能力，而是專注於極限的「生成速度」優化。其核心理念是：透過「模型與系統的極端協同設計 (Extreme Model-System Codesign)」，在單個標準 8-GPU 節點上突破速度上限。

🧪 **三層協同設計：量化、推測解碼與系統優化**

要達到 1000 TPS 的成績，單一技術無法達成，小米採取了三層疊加的策略：

1️⃣ **選擇性 FP4 量化 (MXFP4)**
為了降低記憶體壓力，小米將權重壓縮至 FP4。關鍵在於「選擇性」：僅對參數量最大且對量化耐受度較高的 MoE (Mixture-of-Experts) 專家層使用 MXFP4，其餘模組則維持 FP8 精度。配合量化感知訓練 (QAT)，使模型品質能與原版基本持平。

2️⃣ **DFlash 推測解碼 (Speculative Decoding)**
採用推測解碼機制，利用一個較小的草稿模型 (Draft Model) 預測後續 Token，再由萬億參數的大模型進行並行驗證。透過拒絕採樣 (Rejection Sampling) 確保輸出結果與標準解碼完全一致，在不損失品質的前提下大幅提升吞吐量。

3️⃣ **TileRT 系統執行優化**
由 TileRT 負責底層執行，確保上述的量化權重與推測解碼能在 GPU 上高效運行。這三者必須緊密對齊，才能將生成峰值推至近 1200 TPS。

🚀 **萬億規模、單節點、1000+ TPS**

這次突破最令人關注的數據在於：
- **規模**：萬億參數 (1-Trillion-Parameter)
- **速度**：突破 1000 tokens/sec (峰值接近 1200 TPS)
- **硬體**：僅使用單個標準 8-GPU 商品級節點 (Commodity GPUs)

這意味著在不更換硬體架構的情況下，透過精準的量化策略與系統協同，能將萬億級模型的推理效率提升到一個全新的量級。

⚠️ **技術細節部分私有，實作門檻較高**

雖然結果驚人，但由於 DFlash 推測解碼與 TileRT 的具體實作細節屬於小米私有技術，外部開發者難以直接複製其完整流程。此外，此優化重點在於「速度」而非「能力」，其核心價值在於證明了商品級硬體在極端優化下的潛能。

🎯 **對 AI 工程師的啟示：從「單點優化」轉向「系統協同」**

這項研究給我們的最大啟發是：未來的推理優化不能只靠單一的量化或單一的算法，而是需要「模型-系統協同設計」。

- **精準量化**：不要全盤量化，應針對 MoE 專家層等對量化不敏感的模組採取低精度 (FP4)，保留關鍵模組精度。
- **推測解碼**：在追求極速生成時，Speculative Decoding 是目前最有效的無損加速路徑。
- **硬體利用率**：在標準 GPU 上透過系統層優化，能挖掘出遠超預期的吞吐量。

🔗 **資訊來源**
📝 Xiaomi MiMo and TileRT Push a 1-Trillion-Parameter Model Past 1000 Tokens Per Second on Commodity GPUs
👤 Asif Razzaq / MarkTechPost
🔗 詳情：https://www.marktechpost.com/2026/06/08/xiaomi-mimo-and-tilert-push-a-1-trillion-parameter-model-past-1000-tokens-per-second-on-commodity-gpus/

你認為在商品級 GPU 上追求極速推理，對未來 Agent 的即時響應會有什麼影響？歡迎在下方討論 👇

#AI #LLM #Xiaomi #MiMo #TileRT #GPU #Inference #MoE #量化 #推理加速
