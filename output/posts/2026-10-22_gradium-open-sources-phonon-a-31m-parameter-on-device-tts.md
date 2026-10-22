---
title: Gradium Open-Sources Phonon, a 31M-Parameter On-Device TTS Model Under Apache
  2.0
source: MarkTechPost
url: https://www.marktechpost.com/2026/10/22/gradium-phonon-31m-on-device-tts/
model: claude-code/sonnet
generated_at: '2026-10-22T20:46:46.098577'
score: 97
---

📌 Kyutai 團隊再出手：31M 參數、64.5MB 的端側 TTS 開源了

TL;DR：Gradium 開源 Phonon 系列端側 TTS 模型，31M 參數跑贏多款競品，手機 CPU 上 6.9ms 出聲。

語音合成要落地到手機、瀏覽器、Raspberry Pi 這類裝置，一直卡在「模型太大、延遲太高、還要串雲端 API」的三重門檻。現在這道門檻被壓到 64.5 MB 的檔案大小，還能在筆電 CPU 上跑出近 30 倍實時速度，而且完全不用等雲端回應。

🤔 **從 Kyutai 到 Gradium，端側語音的延續**

Phonon 是 Gradium 開源的小型 TTS 模型家族，Gradium 是從 Kyutai 分拆出來的巴黎語音 AI 公司。模型分成 31M 與 40M 兩種尺寸，英文版 Phonon 31M 以 Apache 2.0 授權發布，整個模型檔案僅 64.5 MB。這代表開發者可以在手機、筆電、嵌入式開發板甚至瀏覽器裡直接跑語音合成，不需要 GPU、不需要呼叫雲端、也沒有按字計費的成本問題。這個專案延續了 Kyutai 的 Continuous Audio Language Models 研究與 Pocket TTS 的技術路線。

🧩 **架構拆解：causal transformer + flow-matching + Mimi decoder**

Phonon 採用 causal transformer 作為骨幹，prefix 部分把文字與 speaker embedding 組合在一起餵進模型。文字輸入端使用 SentencePiece tokenizer，詞彙量 4,000 個 token，直接讀取原始文字，不經過 phoneme 轉換這一步。

骨幹模型每 80 毫秒的 frame 產生一個 latent vector，接著由一個 flow-matching head 把這個向量加上雜訊，一次推論就轉換成 audio embedding。再透過一個縮小版的 Kyutai Mimi decoder，輸出 24 kHz 的 PCM 音訊。另外有一個獨立的 end-of-speech head，負責判斷何時該停止生成。

兩個尺寸的差異在於深度：Phonon 31M 用 6 層 transformer，寬度 512，8 個 attention head；Phonon 40M 則是 9 層,寬度同為 512。兩者都是從一個更大的 Phonon teacher 模型蒸餾（distillation）而來，訓練使用 NVIDIA H100 叢集，配合 NCCL 與 CUDA Graphs。

📊 **盲測評分與硬句子測試，數字說話**

Gradium 做了 1,189 位評審、17,270 票的 blind pairwise listening test。美國英文項目中，Phonon 40M 拿下 2117 Elo，Phonon 31M 拿下 2098 Elo,對照 Kokoro 2043、NeuTTS 2034、Magpie 1939。

準確度測試用的是公開的 hard-sentence 資料集，每個語言 500 句,內容充滿電話號碼、email、郵遞區號這類容易念錯的內容。Phonon 31M 的 WER（詞錯誤率）為 1.70%，對照 Kokoro 的 3.50% 與 NeuTTS Nano 的 8.71%,主要差距來自內建的文字正規化（text normalization）。換到較簡單的 Seed-TTS 測試集，差距就收斂了：Phonon 31M 的 LLM WER 是 0.51%，Kokoro 是 0.45%。

速度方面,在搭載 4 執行緒的 MacBook Air M5 CPU 上，Phonon 31M 首個音訊輸出僅需 6.9 毫秒，跑出 29.9 倍實時速度；Kokoro 因為不支援串流，需要 517 毫秒才能開始。加上 Arm KleidiAI 與 Apple Accelerate 加速後，Phonon 31M 可以達到 46.7 倍實時。在 Raspberry Pi 5 上啟動只要 38 毫秒、3.7 倍實時，相較之下 Gradium 稱 Kokoro 在同一裝置上需要 7 秒才能啟動。Snapdragon 8 Elite Gen 5 上啟動 7.5 毫秒、24 倍實時；NVIDIA L40S 用 CUDA 僅需 5 毫秒就能出聲；AMD EPYC 7413 CPU 則是 43 毫秒。

🎯 **工程師能直接拿來做什麼**

Runtime 以 MIT 或 Apache-2.0 授權開放,支援 Rust、Python(`pip install ptts`)、Swift、C、C++,以及透過 `phonon-tts` 在瀏覽器執行。還附上 OpenAI 相容的伺服器與 WebSocket 伺服器,可以直接載入 Transformers、MLX-Audio、Ollama、LM Studio 使用。如果需要自訂音色,可以在 Gradium Studio 做 voice cloning 或 voice design,訓練完的音色一樣能在本機離線執行。對於要把語音功能塞進資源受限裝置的團隊,這是一個授權寬鬆、延遲極低且有完整公開評測的選項。

🔗 **來源**
- 標題：Gradium Open-Sources Phonon, a 31M-Parameter On-Device TTS Model Under Apache 2.0
- 作者／機構：Asif Razzaq，MarkTechPost
- 連結：https://www.marktechpost.com/2026/10/22/gradium-phonon-31m-on-device-tts/

#TTS #OnDeviceAI #OpenSource #SpeechSynthesis #EdgeAI #Kyutai #Gradium #ApacheLicense #VoiceAI #MachineLearning
