---
title: Liquid AI Releases LiquidCodec, a 74M-Parameter Streaming Audio Codec
source: MarkTechPost
url: https://www.marktechpost.com/2026/11/12/liquid-ai-liquidcodec-streaming-audio-codec/
model: claude-code/sonnet
generated_at: '2026-11-13T22:51:17.369814'
score: 92
---

📌 LiquidCodec：74M 參數的串流語音 Codec

TL;DR：Liquid AI 開源 LiquidCodec，用 GFSQ 量化與全因果編碼器打造比 Mimi 更快的語音 tokenizer，為 LFM3-Audio 系列模型提供底層壓縮。

同樣是把語音轉成 token、再把 token 還原回聲音，LiquidCodec 的 encode 速度卻比它要取代的 Mimi 快了約 13 倍——而參數量只有對方的四分之三左右。

🤔 **語音 codec 要解決什麼**

語音 codec 的任務是把連續的音訊訊號壓縮成語言模型能預測的離散 token，再把 token 轉回可聽的音訊。Liquid AI 在設計 LiquidCodec 時設定了兩個目標：讓 token 容易被預測，以及讓還原回語音的速度夠快。LiquidCodec 正是用來取代先前 LFM2-Audio-1.5B 所使用的 Kyutai Mimi（96.2M 參數），成為 LFM3-Audio-2B 與 LFM3-Omni-2B 背後的語音 tokenizer。

🧩 **GFSQ 取代 RVQ，因果架構支援串流**

LiquidCodec 將 24 kHz 的音訊壓縮成 12 條 token 串流，每 80 毫秒的音訊片段會變成 12 個離散 token。整體流程是 encode → quantize → decode：編碼器與解碼器都使用 Liquid AI 自家 LFM3 架構的模組，兩者結構對稱，且編碼器完全是因果式（causal），天然適合串流場景。

量化方式是關鍵差異：傳統的 residual vector quantization（RVQ）讓每個 codebook 補上前一個 codebook 遺漏的資訊，彼此之間存在依賴關係；LiquidCodec 改用 grouped finite scalar quantization（GFSQ），各個 group 彼此獨立，因此可以用 MaskGIT 風格的 transformer 平行預測全部 12 個 codebook，而不必像 RVQ 那樣逐層序列化預測。解碼器則直接預測頻譜係數，避開了常見於波形解碼器中、成本較高的可學習轉置卷積上採樣（transposed-convolution upsampling）。

🧩 **兩階段訓練，外加 edge 用的 QAT**

訓練分兩階段：第一階段用 264,000 小時、涵蓋 107 種語言的語音資料，只用波形與頻譜損失，不含 adversarial loss；第二階段在 55,000 小時的全頻段語音（24 kHz 或以上）上微調，加入 adversarial critics，Liquid AI 表示這一步消除了第一階段遺留的金屬感雜訊。最後還有一個只微調解碼器的 quantization-aware training（QAT）步驟，專門針對邊緣裝置推理最佳化。

📊 **實時係數比較**

Liquid AI 在 Apple M4 Max MacBook Pro 的單一 CPU 執行緒上以 FP32 自行測得以下即時倍數（real-time factor，數字越低越快，為自評數據）：

| 模型 | Encode RTF | Decode RTF |
|---|---|---|
| LiquidCodec | 0.0028 | 0.0115 |
| Mimi（12 codebook） | 0.0361 | 0.0329 |
| NanoCodec | 0.2145 | 0.2543 |
| X-Codec 2 | 0.7359 | 0.0379 |

換算下來，LiquidCodec 的 encode RTF 比 Mimi 低約 13 倍，decode RTF 低約 2.9 倍。測試集涵蓋 LibriSpeech test-clean、Seed-TTS 英文與中文，以及 FLEURS 的德、法、中、日、韓 5 種語言。另外，Q4_0 搭配 decoder-only QAT 可將解碼器體積縮小 3.5 倍，而 LibriSpeech 上的 ViSQOL 分數僅從 4.319 微降到 4.292。

💡 **對串流應用的意義**

GFSQ 讓 12 個 codebook 可以平行預測而非逐層等待，這對需要低延遲的語音對話系統特別有價值；再加上官方提供 llama.cpp 可用的 Q4_0、Q4_K_M、Q8_0 GGUF 版本，搭配 LFM3-Audio-2B 與 LFM3-Omni-2B，邊緣裝置部署的門檻又降低了一截。

🎯 **實務啟示**

模型可透過 Hugging Face Transformers 以 `trust_remote_code=True` 載入，呼叫 `encode()` 取得音訊 code、`decode()` 還原波形，官方也提供原生的 `LiquidCodecStreamingCache` 支援逐 chunk 解碼。對正在打造低延遲語音助理或 edge 端語音應用的工程師來說，這是個值得直接拿來測試的 drop-in 替代品。

🔗 **來源**
- 標題：Liquid AI Releases LiquidCodec, a 74M-Parameter Streaming Audio Codec
- 作者／機構：Asif Razzaq（MarkTechPost）
- 連結：https://www.marktechpost.com/2026/11/12/liquid-ai-liquidcodec-streaming-audio-codec/

#LiquidAI #AudioCodec #SpeechAI #StreamingInference #OpenSource #GGUF #llamacpp #TextToSpeech #EdgeAI #MachineLearning
