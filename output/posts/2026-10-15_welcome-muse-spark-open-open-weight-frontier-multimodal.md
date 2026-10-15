---
title: 'Welcome Muse Spark Open: open-weight frontier multimodal mixture-of-experts
  model from Meta'
source: HuggingFace Blog
url: https://huggingface.co/blog/meta-muse-spark-open
model: claude-code/sonnet
generated_at: '2026-10-15T20:30:53.900374'
score: 110
---

📌【Meta 開源】816B 參數 MoE 模型，推論只動用 42B

TL;DR：Meta 開源旗艦多模態模型 Muse Spark Open，用 MoE 架構把文字、圖像、音訊、影片塞進同一個介面，主打 agentic coding。

816B 參數聽起來是個跑不動的龐然大物，但 Meta 讓它在推論時只啟用其中 42B，靠的是把密集前饋網路換成一個有 256 位專家、每次只挑 8 位出場的 MoE 架構。這是繼 8 月發布的小型密集模型 Muse Glimmer 之後，Muse 系列的旗艦版本。

🤔 **為 agentic coding 而練的模型**

Meta 把 Muse Spark Open 訓練在真實的開發者工作流程上，包括多檔案重構與長時間除錯。模型被設計成能夠規劃、行動、觀察、自我修正地處理長任務，包括帶著圖像一起瀏覽網頁。輸入端支援文字、圖像、音訊與影片，輸出則統一是文字，讓同一個模型可以讀一張截圖、聽一段語音備忘，或是看一段畫面錄影，同時處理你的程式碼。

| 項目 | 規格 |
|---|---|
| 模型大小 | 約 816B 總參數，每個 token 約啟用 42B |
| 專家路由 | 每個 MoE 層 256 位專家，每個 token 選 8 位 |
| 輸入 | 文字、圖像、音訊、影片 |
| 輸出 | 文字 |
| 上下文窗口 | 最多 1M tokens |
| Checkpoint 格式 | BF16、NVFP4 |

模型權重放在 `Muse-Spark-Open-816B-A42B` 與 `Muse-Spark-Open-816B-A42B-NVFP4` 兩個 repository。Muse Spark Open 與 Muse Glimmer 使用相同的 tokenizer 與詞表，對話模板也沿用 Muse Glimmer 的格式，只是為新增的模態加了擴充。

🧩 **架構細節：MoE、感知編碼器與音訊編碼器**

語言模型本體有 62 層，隱藏維度 8192，每層有 128 個 query head 與 16 個 key-value head（屬於 grouped-query attention），每個 head 維度 64。attention 區塊帶有輸出閘（output gate）與輸出正規化層，並對 query 與 key 做正規化（QK-norm）。每個區塊把輸入與輸出透過一個學習得到的殘差閘（residual gate）結合，而不是單純相加。

Muse Glimmer 在每層只用一個密集前饋網路，Muse Spark Open 則把它換成 MoE 區塊：每層 256 位專家，路由器每次為每個 token 選出 8 位。每位專家是一個把維度從 8192 投影到 4096、再投影回 8192 的前饋網路，並對自己的輸出做正規化。這些專家合計佔了整個模型約 97% 的參數，但每個 token 只動用 8 位專家，因此計算量約等同一個 42B 的模型，不過因為全部 256 位專家都要留在記憶體裡，部署時仍需要一個 816B 模型的記憶體容量。

影像與影片輸入透過一個 1.8B 參數的感知編碼器轉成 token，這個編碼器有 50 層、隱藏維度 1536、16 個 attention head，將每張圖切成 14×14 的 patch，輸出 4096 維特徵；位置資訊來自學習到的絕對位置嵌入與 2D RoPE，每四層加上最後一層使用完整 attention，其餘層用稀疏 attention。這套設計沿用了 Meta 的 Perception Encoder 研究，影片輸入也走同一個編碼器。

音訊則透過獨立的音訊編碼器處理，每 80 毫秒輸出一個音訊 token，等於每秒 12.5 個 token（10 秒音訊約對應 125 個輸入 token）。編碼器本體是一個卷積金字塔，每個階段由不同 patch 大小的嵌入器加上兩個 kernel 大小為 7、stride 為 1 的一維卷積區塊組成，依序對應 [16, 6, 5, 4] 四種 patch 大小，最後階段再經過 RMSNorm → 線性投影 → RMSNorm。

📊 **1M tokens 上下文與部署方式**

上下文窗口在推論時可達 1M tokens（`max_position_embeddings` 設為 1,048,576），圖像、影片、音訊 token 都共用同一個窗口。靠 grouped-query attention，每個 token 只為 KV cache 增加 2×16×64×62＝126,976 個數值，BF16 下約 250KB，換算到滿額 1M tokens 的上下文約需 266GB。

部署上，BF16 checkpoint 約 1.5TB，在 transformers 裡需要 4 個節點、每節點 8 張 H200，以張量平行（TP=32）運作；NVFP4 版本則可以跑在單一 B200 節點上。transformers 提供 `MuseSparkForConditionalGeneration` 與對應的 processor，並透過 `DistributedConfig` 設定張量平行（`tp_size`）與專家平行（`ep_size`）。推理時還能透過 `reasoning_effort` 參數在 low/medium/high/xhigh 四個等級間切換，對應模型內部接受的 16、64、256、512 整數值。

💡 **跟 Muse Glimmer 的差異**

Muse Glimmer 是密集小模型，適合本地跑；Muse Spark Open 則是把同一套設計放大並換成 MoE，是目前美國開放權重模型中最具能力的一款。兩者共用 tokenizer 與感知編碼器架構，意味著從 Muse Glimmer 上累積的使用經驗，有機會直接延伸到這個更大的模型上。

🎯 **實務啟示**

對想要本地或私有部署多模態 agent 的團隊，Muse Spark Open 的 MoE 設計代表「記憶體要備好 816B 的量，但運算只要 42B 的算力」，這對選擇硬體拓樸（張量平行 vs. 專家平行）會是關鍵考量。而 1M tokens 的上下文搭配多模態輸入，也讓它成為處理長時間螢幕錄影或語音除錯紀錄的候選方案。

🔗 **來源**
- 標題：Welcome Muse Spark Open: open-weight frontier multimodal mixture-of-experts model from Meta
- 作者／機構：Hugging Face（Meta 模型）
- 連結：https://huggingface.co/blog/meta-muse-spark-open

#MuseSparkOpen #Meta #MixtureOfExperts #MultimodalAI #OpenWeights #AgenticCoding #LLM #Transformers #LongContext #AIInfrastructure
