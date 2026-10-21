---
title: 'Mistral AI Releases Voxtral 3: Speech-to-Text, TTS and a Voice Agent SDK'
source: MarkTechPost
url: https://www.marktechpost.com/2026/10/20/mistral-voxtral-3-speech-models-voice-agent-sdk/
model: claude-code/sonnet
generated_at: '2026-10-21T20:59:53.598540'
score: 95
---

📌 【Mistral AI】Voxtral 3：聽、想、說三階段合一的語音 Agent

TL;DR：Mistral 一次發布 3 款語音辨識模型、1 款 TTS 與語音 Agent SDK，WER 與價格雙雙對標大廠。

如果你曾為了做一個語音客服 Bot，分別串接三家不同公司的辨識、對話與合成 API，光是對齊延遲與音色就耗掉大半時間，那 Mistral 這次的發布值得細看：它把聽、推理、說三件事收進同一條串流管線。

🧩 **4 個模型＋1 套 SDK，全部公開預覽**

Mistral AI 發布 Voxtral 3，是一個語音模型家族搭配語音 Agent SDK。陣容包含 3 款轉錄（transcription）模型、1 款文字轉語音（TTS）模型，以及一套建構在 LiveKit 之上的 SDK，四個模型目前都在 Mistral API 上公開預覽。所有轉錄模型都支援 diarization（區分說話者）與 context biasing，後者可輸入關鍵字或自由文字來提升辨識召回率；批次轉錄功能涵蓋 50 種語言，包含 24 種歐盟官方語言。

SDK 的核心是把語音互動拆成一條串流管線中的三個階段：Realtime Transcribe 3 負責聆聽並偵測使用者何時停止說話；一個通用 LLM（例如 Mistral Small 4）負責推理與呼叫工具；Voxtral Speech 3 則用符合當前對話語氣的方式回覆。每個對話回合可在 1 秒內完成,使用者插話時 Agent 會即時停止說話。這套 SDK 同時支援透過 SIP 的電話通話,以及透過 WebRTC 的瀏覽器或應用程式會話。因為每個階段都是獨立模型，團隊可以自由替換其中的 LLM、語音或語言。

📊 **自家公布的跑分：準度逼近頂標，速度是弱點**

以下數據由 Mistral 自行公布：

| 指標 | Voxtral Small | Voxtral Mini | 對照對手 |
|---|---|---|---|
| Artificial Analysis AA-WER | 2.1% | 2.2% | 僅輸給 Fun-Realtime-ASR-preview（1.7%）與 MAI-Transcribe-2（2.0%） |
| 速度係數（speed factor） | 65.8x | — | MAI-Transcribe-2 為 307.5x，速度上仍有落差 |

在 FLEURS 35 測試中，即時轉錄模型呈現延遲換準度的取捨：2,400 毫秒延遲時 WER 為 5.7%，480 毫秒時 6.4%，壓到 240 毫秒時升至 7.4%。對照組中，Gemini 3.5 Realtime Transcribe 為 4.2%、MAI-Transcribe-2 Streaming 為 5.8%，兩者都優於 Voxtral 的即時設定;而 GPT Live Transcribe（8.4%）與 Scribe v2 Realtime（8.7%）則落後於 Voxtral 的所有設定。

TTS 方面，Voxtral Speech 3 定價每百萬字元 13 美元，Mistral 表示這低於 OpenAI TTS-1、Deepgram、ElevenLabs Flash 與 Gemini Flash。模型提供情緒（emotion）、節奏（pacing）、重音（emphasis）的明確控制，模型頁面列出約 90 毫秒的首音延遲（time-to-first-audio）與 34 種情緒標籤；Pro Voice 功能可從 30 分鐘音訊中學習並模仿特定說話者的風格。Artificial Analysis 將其列入兩個 TTS 競技場（arena）的前 12 名。

💡 **部署面：歐美全球端點＋OpenRouter 同步上架**

這些模型可在 Mistral 的歐洲、美國與全球端點上運行;OpenRouter 也同步列出全部三款新模型，並提供歐盟託管、零資料保留（zero-data-retention）的端點選項。

🎯 **實務啟示**

對於正在做語音客服、電話 Agent 的團隊，Voxtral 3 的吸引力在於「三階段模型可拆換」的架構彈性，而不必被綁死在單一供應商的全端解決方案上；context biasing 與 diarization 原生支援，也省去額外接第三方服務的麻煩。但速度係數明顯落後 MAI-Transcribe-2，若場景對吞吐量極度敏感，仍需實測評估。

🔗 **來源**
- 標題：Mistral AI Releases Voxtral 3: Speech-to-Text, TTS and a Voice Agent SDK
- 作者／機構：Asif Razzaq / MarkTechPost
- 連結：https://www.marktechpost.com/2026/10/20/mistral-voxtral-3-speech-models-voice-agent-sdk/

#MistralAI #Voxtral #SpeechToText #TextToSpeech #VoiceAgent #LiveKit #ASR #TTS #AIAudio #LLM
