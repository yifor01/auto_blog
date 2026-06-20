---
title: jamiepine/voicebox
source: GitHub Trending
url: https://github.com/jamiepine/voicebox
score: 98
model: google/gemma-4-31b-it:free
generated_at: '2026-06-20T19:36:57.107806'
---

📌 Voicebox：整合 7 種 TTS 引擎的本地化 AI 語音工作室

TL;DR：一個開源且本地運行的語音 I/O 框架，整合語音克隆、多語言合成與 dictation 功能。

當前語音 AI 市場被 ElevenLabs（輸出）與 WisprFlow（輸入）這類雲端服務主導，但對於追求隱私與低延遲的工程師來說，將整個語音 I/O 流程搬到本地端才是最終目標。

🛠️ **將語音輸入與輸出整合在單一本地端 App**

Voicebox 定位為一個「本地優先 (local-first)」的 AI 語音工作室，旨在提供一個免費且開源的替代方案。它將語音流程的兩端結合：一方面提供語音合成 (TTS)，另一方面提供 dictation（將語音轉文字並輸入至任何應用程式），並透過內建的本地 LLM 進行精煉與設定個人化角色 (personas)。

🧩 **核心功能與技術組成**

- **多引擎合成 (TTS)**：整合了 7 種不同的 TTS 引擎，包含 Qwen3-TTS、Qwen CustomVoice、LuxTTS、Chatterbox Multilingual、Chatterbox Turbo、HumeAI TADA 與 Kokoro。
- **語音克隆與預設**：支援 zero-shot 語音克隆（僅需數秒參考音檔即可克隆），或使用 Kokoro 與 Qwen CustomVoice 提供的 50 多種預設聲音。
- **多語言支援**：涵蓋 23 種語言，包含英文、阿拉伯文、日文、印地文與斯瓦希里文等。
- **表現力與後處理**：透過 Chatterbox Turbo 支援 [laugh]、[sigh]、[gasp] 等副語言標記 (paralinguistic tags) 以增加表現力；並提供 pitch shift、reverb、delay 等後處理效果。
- **AI Agent 整合**：可為任何支援 MCP (Model Context Protocol) 的 AI agent 設定自定義語音。

🔒 **隱私優先的本地化運行**

Voicebox 強調完整的隱私保護，所有的模型、語音數據與錄音內容均在使用者本地機器上運行，不會上傳至雲端。

🎯 **實務啟示**

對於開發者而言，Voicebox 的價值在於將碎片化的 TTS 引擎與輸入法功能整合進單一工作流。如果你需要建立一個完全私有的語音交互系統，或希望在不依賴 API 訂閱的情況下實驗不同 TTS 引擎的效能差異，這是一個高效的整合工具。

🔗 **來源**
- 標題：jamiepine/voicebox
- 作者／機構：jamiepine
- 連結：https://github.com/jamiepine/voicebox

#AI #OpenSource #TTS #VoiceCloning #LocalLLM #SpeechSynthesis #Privacy #MCP #Voicebox #MachineLearning
