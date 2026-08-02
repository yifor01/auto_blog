---
title: huggingface/speech-to-speech
source: GitHub Trending
url: https://github.com/huggingface/speech-to-speech
score: 93
model: google/gemma-4-31b-it:free
generated_at: '2026-07-03T19:54:03.401390'
---

📌 【HuggingFace 開源】打造低延遲語音代理，模組化 pipeline 讓 STT/LLM/TTS 全面可替換

TL;DR：HuggingFace 提供一套模組化語音代理流水線，支援 OpenAI Realtime 相容 API，可實現全本地化部署。

想要打造一個能即時對話的語音代理（Voice Agent），最困難的往往不是單一模型的效能，而是如何將多個模型串接成一個低延遲且穩定的流水線。

🧩 **模組化設計：VAD → STT → LLM → TTS**

`speech-to-speech` 專案將語音代理的流程拆解為四個可替換的模組，確保開發者能根據需求靈活調整：
1. **VAD (Voice Activity Detection)**：偵測使用者是否開始或結束說話。
2. **STT (Speech-to-Text)**：將語音轉為文字（預設使用 Parakeet TDT 進行本地處理）。
3. **LLM (Large Language Model)**：處理邏輯並生成回覆（支援 OpenAI 相容協定）。
4. **TTS (Text-to-Speech)**：將文字轉回語音（預設使用 Qwen3-TTS 進行本地處理）。

💡 **全面相容 OpenAI Realtime API 與本地化部署**

該專案透過 WebSocket API 暴露介面，且與 OpenAI Realtime 協定相容，這意味著任何支援該協定的客戶端都能直接連線。在 LLM 的選擇上，開發者擁有極高的自由度：
- **雲端方案**：連線至託管服務商或 HF Inference Providers。
- **本地方案**：透過 vLLM 或 llama.cpp 在自有硬體上執行。例如，可以使用 llama.cpp 部署 Gemma 4 並將其作為後端，實現完全開源且本地化的技術棧。

📊 **已在數千臺 Reachy Mini 機器人中實戰驗證**

這套流水線並非僅是實驗性質的 Demo，README 指出它已作為對話後端，在數千臺 Reachy Mini 機器人的生產環境中執行，證明了其在實際應用中的穩定性與低延遲表現。

🎯 **實務啟示**

對於 AI 工程師而言，這個專案提供了一個「即插即用」的語音代理框架。如果你需要快速搭建一個語音對話系統，不需要從零開始處理 WebSocket 串流或模型串接，直接利用其模組化設計，即可在「雲端 API 快速原型」與「全本地化隱私部署」之間自由切換。

🔗 **來源**
- 標題：huggingface/speech-to-speech
- 作者／機構：HuggingFace
- 連結：https://github.com/huggingface/speech-to-speech

#HuggingFace #VoiceAgent #STT #TTS #LLM #OpenSource #OpenAIRealtime #Gemma4 #vLLM #Robotics
