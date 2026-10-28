---
title: 'Voice AI in vogue: Nvidia releases new open transcription model'
source: TechCrunch AI
url: https://techcrunch.com/2026/10/28/voice-ai-in-vogue-nvidia-releases-new-open-transcription-model/
model: claude-code/sonnet
generated_at: '2026-10-28T22:02:36.202461'
score: 80
---

📌 Nvidia 開源 Nemotron 3.5 Transcribe,單晶片跑 40 國語言轉錄

TL;DR：Nvidia 推出免費開源語音轉錄模型,主打多語言、長錄音與可單晶片部署,但不支援直播即時轉錄。

會議記錄與醫療轉寫是 AI 在職場少數已經站穩腳步的應用,而這次 Nvidia 選擇用一個「能塞進單張晶片」的開源模型來搶這塊地盤。

🤔 **瞄準會議與醫療轉錄這兩個成熟場景**

TechCrunch 報導,Nvidia 於週三發布 Nemotron 3.5 Transcribe,這是一個免費、開放權重的語音轉錄模型,能處理多達 40 種語言的錄音轉寫。Nvidia 同時發布了旗下開源語音資料集 Granary 的第二版,作為訓練與客製化的基礎。

🧩 **規格與架構重點**

根據 Nvidia 的說法,Nemotron 3.5 Transcribe 具備以下能力:

- 支援 **31 種語言**與英語互譯轉錄
- 能處理長達 **一小時**的錄音
- 可分辨最多 **八位講者**
- 模型規模為 **30B 參數**,但 Nvidia 宣稱能在單一晶片上運行,從 Jetson AGX Thor 機器人控制器、搭載 DGX Spark 晶片的新款筆電,到資料中心用的 Blackwell 晶片都能跑
- 在 Hugging Face 的 Open ASR Leaderboard 等基準測試上,Nvidia 宣稱表現優於對手

開發者可以搭配更新後的 Granary 資料集與 NeMo Speech 工具,針對特定產業的術語在各語言中做客製化訓練。

⚠️ **目前只吃得下錄音檔**

一個明顯的限制是:Transcribe 處理的是已錄製好的音訊,而非即時串流,所以暫時不適合用在需要livestream即時字幕的場景。

💡 **語音 AI 正處於密集發軍期**

這次發布也加入了 Nvidia 既有的開源語音模型陣容,包括體積極小卻依然強悍的 Parakeet（1.1B 參數）。報導同時提到,近期語音 AI 賽道相當熱鬧:Mistral 本月早些時候發布了 Voxtral 3,ElevenLabs 推出了用於語音代理的即時語音 Realtime,Salesforce 也發布了自家語音模型 Launa-Omni。

🎯 **實務啟示**

對要打造會議記錄、醫療轉寫或多語言客服工具的工程師來說,Nemotron 3.5 Transcribe 提供了一個可自行部署、支援邊緣裝置到資料中心的選項,免去依賴雲端 API 的延遲與成本考量;但如果產品需求是即時轉錄,目前仍需另尋方案。

🔗 **來源**
- 標題：Voice AI in vogue: Nvidia releases new open transcription model
- 作者／機構：Julie Bort（TechCrunch AI）
- 連結：https://techcrunch.com/2026/10/28/voice-ai-in-vogue-nvidia-releases-new-open-transcription-model/

#Nvidia #SpeechRecognition #OpenSource #ASR #VoiceAI #Nemotron #EdgeAI #MultilingualAI #SpeechToText #AIInfrastructure
