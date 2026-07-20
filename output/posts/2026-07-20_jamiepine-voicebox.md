---
title: jamiepine/voicebox
source: GitHub Trending
url: https://github.com/jamiepine/voicebox
score: 90
model: tencent/hy3:free
generated_at: '2026-07-20T08:54:11.904219'
---

📌 【開源專案】Voicebox：本地端跑完整的 AI 語音輸入輸出堆疊

TL;DR：一套本地優先的開源語音工作室，涵蓋克隆、生成與聽寫，隱私全留在機器上。

語音輸入靠 WisprFlow、語音輸出靠 ElevenLabs，兩家雲端服務各自佔了語音 I/O 迴圈的一半。如果有個開源工具能把兩者合而為一，還全部跑在你自己的電腦裡呢？

🤔 **雲端語音工具各管一半，Voicebox 想打通整條鏈**

README 指出，現有的兩大雲端業者分處語音 I/O 的對側：ElevenLabs 負責輸出（TTS）、WisprFlow 負責輸入（聽寫）。Voicebox 的定位是 local-first（本地優先）的 AI voice studio，同時做輸入與輸出，並用內建的本地 LLM 做語句潤飾與依聲音檔設定角色（persona），整體不依賴雲端。

🧩 **核心架構：把 7 套 TTS 引擎與聽寫包進同一個本地應用**

根據專案說明，Voicebox 設計為單一 app，整合以下功能：
- 語音克隆：從幾秒的參考音檔做 zero-shot cloning，或使用 50+ 個預設聲線（經由 Kokoro 與 Qwen CustomVoice）。
- 語音生成：橫跨 7 個 TTS 引擎，包含 Qwen3-TTS、Qwen CustomVoice、LuxTTS、Chatterbox Multilingual、Chatterbox Turbo、HumeAI TADA、Kokoro，支援 23 種語言。
- 全域熱鍵聽寫：可對任意文字欄位用快捷鍵直介面述輸入。
- 代理語音化：讓任何支援 MCP 的 AI agent 用你指定的聲音說話。
- 後處理效果：pitch shift、reverb、delay、chorus、compression、filters。
- 情緒語音標記：透過 Chatterbox Turbo 可使用 [laugh]、[sigh]、[gasp] 這類 paralinguistic tags。

💡 **完全本地執行換取隱私，而非仰賴雲端帳號**

作者宣稱，模型、語音資料與錄音內容都不會離開使用者的機器，這是相對於雲端語音服務的主要差異點。它也把輸入與輸出橋接起來，用 bundled local LLM 做 refinement 與 per-profile personas。

🎯 **實務啟示**

對重視資料隱私、想把語音輸入與輸出都自架的開發者，Voicebox 提供了一個免費且開源的整合選項，不必分別訂閱兩家雲端服務。若你的工作流需要讓本地 agent 用特定聲線回話，或要在不聯網環境做多語言語音生成，可直接評估其 7 引擎與 23 語言的覆蓋是否符合需求。

🔗 **來源**
- 標題：jamiepine/voicebox
- 作者／機構：jamiepine
- 連結：https://github.com/jamiepine/voicebox

#OpenSource #VoiceAI #TTS #VoiceCloning #LocalFirst #Privacy #MCP #SpeechToText #AIStudio #Voicebox
