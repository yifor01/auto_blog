---
title: Gemini-3.5-Transcribe
source: Hacker News
url: https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-3-5-transcribe/
model: claude-code/sonnet
generated_at: '2026-08-28T18:02:47.739535'
score: 95
---

📌 WER 降到 2.6%:Google 發表新一代語音轉文字模型 Gemini 3.5 Transcribe

TL;DR：Google 開放 API 讓開發者用新一代語音辨識模型打造即時語音助理與逐字稿工具。

你有沒有遇過語音辨識把「我們星期二——不對，星期三見」硬生生轉成一串語意錯亂的文字？Google 這次推出的新模型,號稱能像人類一樣理解你「說錯又改口」的過程,直接吐出乾淨的逐字稿。

🤔 **傳統語音辨識卡在噪音、術語與贅字**

Google 指出,一般語音辨識模型在背景噪音、複雜專業術語與口語贅字（filler words）清理上表現不佳。Gemini 3.5 Transcribe 的設計目標,是把原始音訊直接轉成精確、排版乾淨的文字,而不只是逐字照搬。

🧩 **兩套 API：即時串流與離線批次**

Gemini 3.5 Transcribe 分成兩種使用情境：
- 即時串流：透過 Live API 的 `gemini-3.5-transcribe-live`,提供次秒級延遲的雙向連續串流,適合互動式語音應用。
- 預錄音訊處理：透過 Interactions API 的 `gemini-3.5-transcribe`,可處理會議、通話紀錄等錄音,支援語者分離（最多三位語者,三位以上為實驗性功能）與詞級時間戳記。

模型還具備「智慧轉錄」能力,能處理自我修正、過濾贅字並自動排版；同時支援 function calling,可將圖片生成、檔案分析等工作委派給其他 Gemini 模型處理。此外,它能辨識使用者自訂的專有詞彙,並自動偵測、轉錄超過 85 種語言與各地口音方言。

📊 **WER 4.0%（串流）、2.6%（非串流）**

根據 Artificial Analysis 的測試,Gemini 3.5 Transcribe 在串流情境下平均字錯誤率（WER）為 4.0%,非串流情境為 2.6%,在嘈雜的真實環境中也能準確擷取郵遞區號、訂單編號等英數字組合。相較前一代 Chirp 3 模型,最終逐字稿產出時間改善了 70%。在 FLEURS 多語言基準測試中,該模型在串流模式達到 5.50% WER、非串流模式達到 5.04% WER,均優於 Chirp 3。

💡 **從 Gboard 到 Chrome,一路鋪進 Google 生態系**

除了開發者可透過 Google AI Studio 與 Gemini Enterprise Agent Platform 存取這個模型,Google 也已將其整合進多項自家產品：Android Gboard 的 Rambler 功能能把口語即時轉成排版整齊的文字並支援語音編修；Google Antigravity 會結合螢幕畫面與對話紀錄提升轉錄準確度；macOS 版 Gemini app 則能用語音指令搭配螢幕內容完成摘要、圖片生成等複合工作流程；Chrome 的語音輸入功能也即將推出。生態系夥伴方面,Agora、Fishjam、LangChain、LiveKit、Pipecat、Vercel、Vision Agents 等開發平臺已透過 Gemini Live API 打造語音互動介面。

⚠️ **部分功能仍在實驗或限定平臺**

三位以上語者的辨識仍屬實驗性質；部份進階語音互動功能目前僅限 macOS 版 Gemini app,Chrome 整合則尚未正式上線。

🎯 **對工程師的實務啟示**

若你正在打造語音代理人、即時字幕工具或通話後分析流程,可以評估用 Gemini 3.5 Transcribe 取代現有 STT 方案,特別留意其自訂詞彙與多語者時間戳記功能是否符合你的應用場景需求,並實測其在自家噪音環境下的表現是否貼近官方公布的 WER 數字。

🔗 **來源**
- 標題：Gemini-3.5-Transcribe
- 作者／機構：k9294（Hacker News）
- 連結：https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-3-5-transcribe/

#Gemini #GoogleAI #SpeechToText #VoiceAI #ASR #DeveloperTools #LiveAPI #NLP #VoiceAgents #AIProductivity
