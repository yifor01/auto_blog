---
title: NVIDIA Shows 3 Ways to Speed Up MoE Inference on DGX Spark, Lifting Ling-3.0-flash
  Throughput 42.5%
source: MarkTechPost
url: https://www.marktechpost.com/2026/11/03/nvidia-dgx-spark-moe-inference-ling-3-0-flash/
model: claude-code/sonnet
generated_at: '2026-11-03T22:35:23.600128'
score: 88
---

📌 NVIDIA 三招疊加，DGX Spark 上 MoE 推理吞吐量多 42.5%

TL;DR：NVIDIA 在桌上型 DGX Spark 疊加三項優化，讓 124B 參數的 MoE 模型解碼吞吐量提升 42.5%，準確率幾乎不變。

一臺放在桌上的工作站，要跑一個 1,240 億參數的 MoE 模型，聽起來就吃力；但 NVIDIA 的最新技術文章顯示，光靠軟體層的三項優化疊加，就能讓同一臺機器的解碼吞吐量多出四成以上，而且幾乎不影響答案品質。

🤔 瓶頸在哪：記憶體頻寬而非算力

NVIDIA 技術部落格以 Ant Group inclusionAI 的 Ling-3.0-flash 為測試對象，這是一個 124B 參數、5.1B 活化參數的 MoE 模型，跑在 DGX Spark 上——NVIDIA 的桌上型系統，搭載 GB10 Grace Blackwell Superchip，128GB 統一記憶體，273GB/s 記憶體頻寬，峰值算力可達 1 petaFLOP 的 sparse FP4，官方標示可支援到 200B 參數模型的推理。NVIDIA 團隊在 batch size 1 的情境下分析 Ling-3.0-flash-fp4，發現解碼階段是 memory-bound：讀取模型權重主導了執行時間，其中 MoE 計算與負責對詞彙表打分的 LM head 是兩個耗時大戶。這指出兩個優化方向：每個解碼步驟搬動更少的 byte，以及每輪驗證產生更多 token。

🧩 三項優化逐一拆解

Baseline 採用官方 W4A8 配方：FlashInfer 的 MXFP4 MoE kernel、CUTLASS dense GEMM，加上 FP32 的 LM-head 路徑。在一個 32K 輸入、2K 輸出的合成測試上，跑出每 token 27.71 毫秒（36.09 tokens/秒）。

1. 換用 Humming MXFP4 MoE kernel：把 FlashInfer 的 MoE backend 換成獨立的 kernel 函式庫 Humming，利用 NVRTC 針對實際矩陣形狀、資料型態與 GPU 在執行期編譯 kernel（包括 768 寬的 expert 層），每個 kernel 幾秒內就能編譯完成；相較之下，FlashInfer 的 CUTLASS 路徑要用 ninja 編譯 97 個目標，耗時數十分鐘。吞吐量因此提升 9.3%，達到 39.45 tokens/秒。
2. 線上量化 FP8 LM head：LM head 是一個 157,184 x 2,560 的矩陣，以 BF16 儲存，每產生一個 token 就要讀取整個矩陣。只把這一層在載入時量化成 FP8，讀取量就能減半，設定環境變數 `SGLANG_ENABLE_FP8_LM_HEAD=1` 即可啟用，但不能與 baseline 的 `--enable-fp32-lm-head` 選項並用。搭配 Humming 後，吞吐量達到 43.94 tokens/秒，比 baseline 提升 21.7%，比單用 Humming 再多 11.4%。
3. 搭配 NEXTN 的 MTP 投機解碼：Ling-3.0-flash 內建 NEXTN 預測層，不需要額外的 draft model。它一次起草 3 個 token，模型一次驗證 4 個位置；驗證成本大約是一般解碼步驟的 2.26 倍，主要成本來自 MoE 而非 attention——驗證 4 個 token 可能一次激活多達 32 個 expert，而非平常的 8 個。在合成測試中，平均每輪接受 3.90 個 token，吞吐量躍升到 102.88 tokens/秒，比 baseline 高出 185.1%。

⚠️ 疊加時的整合陷阱

這三項優化並非自動相容。同時開啟 FP8 LM head 與 MTP 時，draft 必須共用完整的 LM-head 模組，否則框架會悄悄 fallback，draft 會把 FP8 權重誤判成 BF16，接受長度掉到 1.00，吞吐量甚至低於未優化的 baseline。NVIDIA 團隊建議在啟動時逐一檢查每項優化是否真正生效，並指出 Ling cookbook notebook 裡示範了如何同時啟用兩者。

📊 真實任務上的數據（GSM8K 全部 1,319 題，5-shot chain-of-thought，temperature 0.6，top_p 0.95，top_k 29）

| 指標 | Baseline | 三項優化後 |
|---|---|---|
| 每輸出 token 耗時 | 26.45 ms | 18.56 ms |
| 解碼吞吐量 | 37.81 tokens/秒 | 53.89 tokens/秒（+42.5%） |
| 平均延遲 | 15.21 秒 | 11.49 秒（-24.5%） |
| 準確率 | 96.89% | 96.82%（統計上無顯著差異） |
| 平均接受長度 | — | 2.68 |

NVIDIA 團隊指出合成測試（接受長度 3.90）與真實任務（2.68）的落差有三個原因：合成輸出較重複使 draft 較容易被接受；合成測試用 greedy decoding，而 GSM8K 用 sampling；GSM8K 答案也較短，中位數約 310 token，遠低於合成測試固定的 2K token 輸出。

💡 模型本身的定位與定價

Ling-3.0-flash 屬於 Ant Group inclusionAI 的 Ling 3.0 系列，採 MIT 授權開源，陣容還包括 7.9B MoE、1.3B 活化參數的 Ling-3.0-tiny，兩者都附 base checkpoint 以及 FP8、INT4、GGUF 版本（flash 還多了 FP4）。模型卡顯示 Ling-3.0-flash 在 SWE-Bench Pro 拿 56.6 分、SWE-Bench Multilingual 72.4 分、MathArena AIME 2026 93.2 分、HMMT Feb 2026 87.0 分；OpenRouter 上 Artificial Analysis 的數據則是 GPQA Diamond 85.5%、Terminal-Bench 2.1 55.4%，而最難的 Humanity's Last Exam 自報 22.7 分、獨立測試 23.7%。

API 報價上，Artificial Analysis 列出 inclusionAI 的 API 為每百萬 input token 0.075 美元、output token 0.22 美元，以 7:2:1 的 cache-hit、input、output 比例換算，混合價約每百萬 token 0.05 美元；OpenRouter 上 Novita 與 DeepInfra 的報價是 input 0.06 美元、output 0.18 美元。對照同級模型，Step 3.7 Flash 混合價 0.18 美元、Gemini 3.5 Flash-Lite 0.33 美元、GPT-5（medium）1.34 美元——這些僅為價格比較，未經品質校正。量化對品質的影響也不大：FP4 版本 GPQA-diamond 為 83.68 分（BF16 為 84.97），IFBench 從 74.49 降到 73.87，ArcPrize 從 68.75 降到 68.06，降幅最大的是 SciCode，從 41.24 降到 38.43，而 NVIDIA 在 DGX Spark 上測試的正是這個 FP4 checkpoint。

🎯 實務啟示

對自建推理服務的工程師而言，面對 memory-bound 的 MoE 解碼瓶頸，可以從兩個方向下手：換用針對實際矩陣形狀動態編譯的 kernel 函式庫，減少浪費的編譯與讀取開銷；以及把讀取量大但對精度不敏感的層（如 LM head）選擇性量化。如果模型本身已內建類似 NEXTN 的預測層，投機解碼帶來的吞吐量提升可能最顯著，但務必確認各項優化之間沒有 silent fallback——用環境變數與模組共用設定時，務必跟官方 notebook 核對，否則可能適得其反。

🔗 來源
- 標題：NVIDIA Shows 3 Ways to Speed Up MoE Inference on DGX Spark, Lifting Ling-3.0-flash Throughput 42.5%
- 作者／機構：Asif Razzaq／MarkTechPost
- 連結：https://www.marktechpost.com/2026/11/03/nvidia-dgx-spark-moe-inference-ling-3-0-flash/

#NVIDIA #DGXSpark #MoE #LLMInference #SpeculativeDecoding #Quantization #Ling3 #InclusionAI #GPUOptimization #EdgeAI
