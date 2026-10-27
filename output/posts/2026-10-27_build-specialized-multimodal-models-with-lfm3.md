---
title: Build specialized multimodal models with LFM3
source: HuggingFace Blog
url: https://huggingface.co/blog/LiquidAI/lfm3
model: claude-code/sonnet
generated_at: '2026-10-27T21:36:49.825749'
score: 90
---

📌 LiquidAI 發表 LFM3：35% 更少參數，打造可微調的專用多模態模型

TL;DR：LiquidAI 新一代 LFM3 以 1.7B 骨幹涵蓋文字、視覺、音訊與決策任務，單張 GPU 就能微調並部署到邊緣裝置。

當多數團隊還在煩惱「一個大模型打天下」的成本與延遲，LiquidAI 給出另一個答案：與其追求更大的通用模型，不如把骨幹做得更強，再讓每個人自己微調出專屬版本。LFM3-1.7B 宣稱用少 35% 的參數就打贏前代 LFM2.5-2.6B，而且這只是六個模型家族裡的第一個。

🤔 **從「一個模型」到「一個骨幹、六種模型」**

LFM2 已證明「短卷積＋attention」的混合架構能在裝置端跑得夠快又不犧牲品質。LFM3 的目標更進一步：針對 agentic 應用場景，在長 context 下提供更高的每參數capability。LiquidAI 用 hardware-in-the-loop 的架構搜尋法，這次涵蓋手機、Raspberry Pi 5、筆電、雲端 CPU/GPU，以及 Qualcomm Hexagon NPU 共 14 種裝置與後端組合，重新設計出新的 tri-hybrid 架構。

🧩 **LFM3-1.7B-Base 的四個關鍵改動**

LFM3-1.7B-Base 共 24 層，核心變化包括：

- Tri-hybrid 層組合：13 層 gated 短卷積（kernel size 從 3 提升到 7）、5 層 sliding-window attention（256-token 視窗）、6 層 global attention。
- Head-wise gated attention：每個 attention head 的輸出由一個 sigmoid gate 調節，讓沒用的 head 可以自行關閉，同時有助於抑制量化時的 activation outlier。
- Partial RoPE：global attention 層只對每個 head 的高頻率一半做旋轉，另一半則不受距離影響地匹配內容；SWA 層仍保留完整 RoPE。
- Sandwich norm：每個區塊的輸入與輸出都做正規化，讓 activation 維持在合理尺度。

LFM3-1.7B-Base 使用與 LFM2.5-8B-A1B 相同的 128K 詞彙表，在 22T tokens 上預訓練，最後 3.5T tokens 是以 agentic traces 與工具呼叫為主的中段訓練，context window 也因此延伸到 256K。

📊 **效能與六大模型總覽**

每參數表現上，LFM3-1.7B 在短 prompt 下與 LFM2-1.2B 持平，但在 8K tokens context 下速度快了約 25%。在 agentic 任務上差距更明顯：WebArena-Verified 上拿下 38.42 分，對比前代的 3.02，甚至在瀏覽器與商業應用的長任務上超越 Qwen3.5-9B。

所有模型都從同一個 LFM3-1.7B-Base 分支出來：

| 模型 | 輸入 | 輸出 | 基礎架構 |
|---|---|---|---|
| LFM3-1.7B | 文字 | 文字 | LFM3-1.7B-Base |
| LFM3-VL-2B | 文字、圖像、影片 | 文字 | 骨幹 + 視覺編碼器 |
| LFM3-Audio-2B | 文字、音訊 | 文字、語音 | 骨幹 + 音訊編碼器/解碼器 + LiquidCodec |
| LFM3-Omni-2B | 文字、圖像、影片、音訊 | 文字、語音 | 骨幹 + 視覺與音訊編碼器 + 音訊解碼器 |
| d1-2B | 文字、圖像、影片 | 校準過的答案 | LFM3-VL-2B |
| d1-omni-2B | 文字、圖像、影片、音訊 | 校準過的答案 | LFM3-Omni-2B |

新的視覺編碼器結合卷積與 attention，比前代 LFM VL 模型使用的 SigLIP2 編碼器少用 3 倍運算量；164M 參數規模下，與 Qwen3.5-2B 的視覺編碼器準確度相當，卻少用 2.2 倍 FLOPs（兩者都以相同的 LFM2.5-230M 語言骨幹測量）。影片輸入會把每兩個取樣幀嵌入成一個時間切片，讓時間序列長度減半。音訊編碼器混合 sliding-window attention 與短卷積，並且是完全 causal 的設計，可以邊聽邊 prefill，最低 time to first token 可達 50 毫秒。新的音訊 tokenizer LiquidCodec 在 Apple M4 Max 單一 CPU 執行緒上能以約 87 倍即時速度產生語音，並支援串流解碼。

LFM3-VL-2B 是第一個支援影片輸入的 LFM 視覺模型，會先逐步推理再作答，並能辨識物體與其空間關係。相較 LFM2.5-VL-3B（3.1B 參數），LFM3-VL-2B 只有 1.9B 參數，卻把 62 個視覺 benchmark 的平均分數從 57.6 推高到 71。

🎯 **實務啟示**

對需要在裝置端跑 agent 的團隊，LFM3-1.7B 在 4-bit 精度下約 1GB，加上 256K context，意味著可以把工具呼叫、結構化輸出這類任務直接放到邊緣裝置執行，而不必依賴雲端大模型。更重要的是每個模型都設計成能在單張 GPU 上微調，這讓「針對自家資料與部署環境做專用化」變得可行，而不是只能選擇通用大模型的妥協。

🔗 **來源**
- 標題：Build specialized multimodal models with LFM3
- 作者／機構：LiquidAI（HuggingFace Blog）
- 連結：https://huggingface.co/blog/LiquidAI/lfm3

#LFM3 #LiquidAI #MultimodalAI #EdgeAI #OnDeviceInference #FoundationModels #FineTuning #VisionLanguageModel #AgenticAI #OpenWeightModels
