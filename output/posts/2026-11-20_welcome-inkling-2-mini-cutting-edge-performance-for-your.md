---
title: Welcome Inkling 2 Mini, Cutting-edge Performance for your Local Setup
source: HuggingFace Blog
url: https://huggingface.co/blog/inkling2mini
model: claude-code/sonnet
generated_at: '2026-11-20T23:17:20.773414'
score: 107
---

📌 Inkling 2 Mini：24層權重跑出48層的推理深度

TL;DR：26B 模型靠迴圈機制長出 48 層效果，本地可跑，效能直逼同級大模型。

一個模型的總參數標著 26B，但每個 token 真正動用的只有 3B，剩下的容量跑去哪了？答案藏在一段會被重複執行三次的中間層區塊裡。

🤔 為什麼要讓層「跑三次」

一般要擴充模型容量，常見做法是堆更多層或拉大每層寬度，但這會直接推高參數量與記憶體需求。Inkling 2 Mini 的做法不同：24 個解碼器層中，中間 12 層以迴圈方式重複執行三次，讓模型的行為等同於擁有 48（6＋3×12＋6）個邏輯層，但實體權重只需要儲存 24 層份量。因此 Mini 的隱藏維度只有 2,304（Inkling 2 Small 為 4,608），每層從 128 個專家（Small 為 384 個）中路由 8 個，大幅壓低實體參數量，卻維持每個 token 跑滿 48 次層存取的運算深度。

🧩 跨迴圈傳遞的「訊息」機制

單純把同一組權重重複跑三次並不會自動帶來好處，Inkling 2 Mini 的關鍵設計在於「cross-pass messages」：每次進入迴圈核心（第 6–17 層）時，輸入都來自第一次六層運算的輸出，而不是上一輪迴圈的輸出。每個迴圈層會用自己學到的 query 讀取上一輪輸出產生的訊息（針對 query、key、value 與 MLP 輸入各有一則），再由一個小型 gating controller 根據目前輸入與這則訊息，決定要遺忘多少舊資訊、融入多少新訊息。這讓每一輪迴圈都是在修正前一輪算出來的結果，而非從頭重算。

架構上，每六層區塊中有五層採用滑動視窗注意力（視窗上限 1,024 token），一層採用全注意力；注意力配置為 24 個 query head、8 個 KV head，搭配學習式相對位置 logits、學習式 sink 與輸出閘門，全注意力層則使用動態 key/value 卷積。路由器會從 128 個 SwiGLU 專家中選出 8 個，正規化分數後乘以 8 做權重縮放。第二、三輪迴圈時，每個核心層會額外關注前一輪的兩個殘差區塊，並透過四個 rank-64 的閘門把訊息混入 query、key、value 與 MoE 輸入。文字解碼器寬度為 2,304，每個專家的中間層寬度為 1,152。

除了標準版，Thinking Machines Lab 也釋出了一個研究用變體（TML-d24-varloop-research），架構相同，但訓練時支援可變的迴圈次數。設成 1 或 2 輪可讓推理明顯加速，代價是生成品質可能略微下降。

📊 本地模型榜單上的表現

根據 Artificial Analysis Intelligence Index v5（AAv5），Inkling 2 Mini 在同量級模型中名列前茅。與 Gemma 4 31B、Muse Glimmer、Qwen3.8-27B、Nemotron 3.5 Super VL 的對比中，Inkling 2 Mini 在 48 項基準測試中贏了 32 項，涵蓋程式撰寫與自動化研究、知識工作的 agentic 搜尋與工具呼叫、視覺理解與生成、推理與知識、安全與對齊等類別。程式碼相關測試上，它在 FrontierCode v2.0 領先，在 Terminal-Bench 4.0 與 Qwen3.8-27B 打平，但在 AutomationBench-AA v1.0.6 落後 Qwen。HuggingFace 團隊也提到，在他們的主觀測試（vibe tests）中，Inkling 2 Mini 至少與 Qwen3.8-27B 同一水準，但強調仍需要更多驗證。

🧩 多種推理框架的 day-zero 支援

模型同時支援圖片與文字輸入，context 長度達 1M token，並以混合精度格式發佈：專家權重採用 NVFP4 與 MXFP8。官方還附上一個 DSpark drafter，用小幅記憶體代價換取額外的推理加速。在使用端，transformers、llama.cpp（Llama App）與 MLX 皆已支援，SGLang 則提供 day-zero 的推理支援，可用於資料中心硬體上的生產部署。在 transformers 中可直接透過 AutoModelForMultimodalLM 載入標準版模型；若要使用研究用的變動迴圈版本，只需在載入時於 text_config 設定 loop_num_passes 即可調整迴圈輪數。模型也支援透過 reasoning_effort 參數（從 none 到 max，或 0.0–0.99 之間的數值）調整推理強度，預設為 high（0.9）。

🎯 實務啟示

對於想在本地端跑大模型能力、卻受限於顯示卡記憶體的工程師，Inkling 2 Mini 的「迴圈增容」設計提供了一個新的取捨維度：不是單純壓縮參數，而是用重複運算換取更深的邏輯深度。若硬體吃緊，變動迴圈版本的研究變體值得留意，它讓你能在推理速度與生成品質之間即時取捨，不需要重新訓練或更換模型。

🔗 來源
- 標題：Welcome Inkling 2 Mini, Cutting-edge Performance for your Local Setup
- 作者／機構：HuggingFace（merve、Pedro Cuenca、Aritra Roy Gosthipaty、Guarin Flück 等）
- 連結：https://huggingface.co/blog/inkling2mini

#LLM #MixtureOfExperts #LoopedTransformer #LocalAI #OpenSource #Multimodal #ThinkingMachinesLab #Transformers #MLX #SGLang
