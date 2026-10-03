---
title: 'Microsoft AI Releases MAI-Transcribe-2-Streaming: #1 Real-Time Speech-to-Text
  Model on Artificial Analysis'
source: MarkTechPost
url: https://www.marktechpost.com/2026/10/02/microsoft-ai-releases-mai-transcribe-2-streaming-1-real-time-speech-to-text-model-on-artificial-analysis/
model: claude-code/sonnet
generated_at: '2026-10-03T19:54:48.780129'
score: 85
---

📌 【Microsoft AI】語音辨識刷新第一，100 毫秒出字

TL;DR：Microsoft 推出串流語音辨識模型 MAI-Transcribe-2-Streaming,在 Artificial Analysis 排名第一。

對語音 agent 來說,慢半秒不是小事,是整段對話體驗的差異。Microsoft AI 這次直接把「等使用者說完才開始辨識」這個假設拿掉。

🤔 **即時辨識,邊聽邊出字**

Microsoft AI 於 2026 年 10 月 1 日發布 MAI-Transcribe-2-Streaming,這是該公司第一款串流語音辨識(speech-to-text)模型,同時一併推出兩款文字轉語音模型 MAI-Voice-2.1 與 MAI-Voice-2.1-Flash。Artificial Analysis 在 38 款模型的排行中,把它列為最終逐字稿與第一版部分逐字稿(partial transcript)準確率雙項第一。這款模型的目標場景是語音 agent、即時字幕與語音輸入,也就是延遲直接決定使用體驗的場合。

🧩 **先猜,再修正,最後定稿**

MAI-Transcribe-2-Streaming 是 9 月發布的批次版 MAI-Transcribe-2 的即時版本,支援 60 種語言並具備自動、連續的語言偵測能力。音訊持續串流進來,文字也在講者還在說話時同步串流輸出。模型在收到音訊後,僅約 100 毫秒就會給出第一版猜測(稱為 partial),之後隨著上下文增加持續修正,最終收斂成一份穩定的最終逐字稿。這代表 agent 可以在使用者話還沒說完時,就開始推理或呼叫工具。Microsoft 團隊表示,內部測試顯示文字出現的速度是最接近競品的兩倍。

📊 **怎麼測出來的**

AA-WER Streaming 這項指標使用約 8 小時的音訊,組成是 AA-AgentTalk(50%)、VoxPopuli(25%)與 Earnings22(25%);延遲則是從語音結束那一刻開始計算,偵測方式採用 SileroVAD。測試結果顯示,第一版 partial 的準確率已經和最終逐字稿相當,這一點對那些需要在講者說完前就採取行動的 agent 特別關鍵。Microsoft 也把這款模型標示在準確率與延遲的 Pareto frontier 上。

💡 **定價與整合方式**

MAI-Transcribe-2-Streaming 的費用是每小時音訊 0.54 美元,這是到 2026 年底為止的推出期優惠價,Artificial Analysis 將其換算為每千分鐘 9.00 美元。相比之下,批次版 MAI-Transcribe-2 每小時只要 0.10 美元。在串流這個項目上,Microsoft 的定價高於 xAI 與 Meta,大致與 Google 的估算費率相當。整合方式有兩條路徑:一是相容於 OpenAI Realtime WebSocket 的 Realtime API,適合既有架構已採用該協定的應用;二是 Azure Speech SDK,負責處理連線管理、重試與音訊串流,兩者都會回傳中間結果與最終結果。模型也已上架 MAI Playground,並可透過 Vercel 與 Azure Voice Live 取用,LiveKit 支援則標示為即將推出。若要組成完整的語音迴圈,Microsoft 建議搭配 MAI-Voice-2.1-Flash:45 秒音訊在 150 毫秒端到端延遲下生成,費用為每百萬字元 15 美元;MAI-Voice-2.1 則涵蓋 23 種語言、26 個地區,費用為每百萬字元 22 美元。

🎯 **對工程師的意義**

如果你在打造語音 agent 或即時字幕系統,第一版 partial 的準確率是否足以直接驅動後續動作,是比單純看最終逐字稿 WER 更值得關注的指標。串流版的定價明顯高於批次版,評估導入前,值得先確認自己的場景是否真的需要「邊聽邊反應」的即時性。

🔗 **來源**
- 標題：Microsoft AI Releases MAI-Transcribe-2-Streaming: #1 Real-Time Speech-to-Text Model on Artificial Analysis
- 作者／機構：Michal Sutter, MarkTechPost
- 連結：https://www.marktechpost.com/2026/10/02/microsoft-ai-releases-mai-transcribe-2-streaming-1-real-time-speech-to-text-model-on-artificial-analysis/

#MicrosoftAI #SpeechToText #VoiceAI #RealTimeAI #AzureSpeech #VoiceAgents #AIInfrastructure #SpeechRecognition #MachineLearning #ArtificialAnalysis
