---
title: 'Meta Superintelligence Labs Releases Muse Voice Transcribe: One Real-Time
  Model for Streaming ASR, Diarization, and Endpointing'
source: MarkTechPost
url: https://www.marktechpost.com/2026/09/01/meta-superintelligence-labs-releases-muse-voice-transcribe-one-real-time-model-for-streaming-asr-diarization-and-endpointing/
model: claude-code/sonnet
generated_at: '2026-09-02T10:05:06.522895'
score: 101
---

📌 【Meta Superintelligence Labs】ASR、分聲、斷句三合一，但只租不賣

TL;DR：Meta 用單一自回歸解碼器同時做即時語音辨識、講者分離與斷句，目前僅開放付費 API。

多數語音辨識產品背後其實是三套系統硬接在一起：一個模型轉錄文字，另一個負責分辨誰在說話，第三個判斷使用者何時說完。每一次交接都多一分延遲，也多一種可能出錯的地方。Meta Superintelligence Labs 這週發布的 Muse Voice Transcribe，把這三件事塞進同一顆模型裡完成。

🤔 **三套系統接起來，等於三倍的失敗點**

Meta 稱這是自家第一個即時音訊感知模型，來自 Muse Spark 系列。它在一次推論中同時完成串流 ASR、支援 20 人以上的講者分離（diarization），以及斷句偵測（endpointing），不需要額外的後處理步驟。目前它以 muse-voice-transcribe-1.0 的名義上架 Meta Model API，定價每千分鐘音訊 3 美元（換算每小時 0.18 美元），已經用在 Meta AI for Mac 與 Muse Code 的口述輸入功能中。

🧩 **一顆解碼器，同時負責「聽」和「寫」**

架構上，音訊以 80 毫秒為一個區塊、12.5Hz 的頻率送入模型，每個區塊會被轉成一個 soft token。模型在每個區塊之後只做一個二元選擇：預測 `<|next_audio|>` token 繼續聆聽,或是輸出文字 token。當模型選擇繼續聆聽,`<|next_audio|>` 這個位置就會被實際的下一段音訊取代;當音訊串流結束時,系統插入 `<|empty_audio|>` token,模型不再要求更多音訊,而是把剩餘文字一次輸出完。因為聆聽與輸出共用同一個解碼迴圈,不需要額外的對齊階段來同步兩者。

由於模型自己決定何時繼續聽、何時輸出文字,它也就控制了每個字背後有多少音訊上下文,Meta 把這個差距稱為「delay」。delay 越長,轉錄越準,但延遲也越高。Meta 沒有把這個取捨寫死,而是用強化學習訓練:把字詞錯誤率(WER)獎勵與 delay 獎勵以相乘的方式結合,讓模型針對不同難度的字詞動態調整 delay。

分聲同樣不是額外接一個模型,而是在同一串輸出中加入特殊 token:`<|start_of_turn|>` 標記可能的講者切換,`<|speaker_{A-Z}|>` 標記講者身份。切換 token 一旦可能發生就立刻觸發,講者標籤則延遲到區塊結束才輸出;同一位講者的音訊即使被切成多個片段,也會被解析回同一個標籤。斷句部分則用 `<|speech_onset|>` 標記語音起點、`<|speech_endpoint|>` 標記語音結束點,這兩項任務與串流 ASR 一起聯合訓練,在 ASR 獎勵之上疊加額外獎勵。

模型訓練涵蓋 70 多種語言,其中 25 種在發布時經過充分驗證並推薦使用,同一句話中或句子之間切換語言(code-switching)是原生支援的能力,對雙語使用者很實用。準確度還可透過語言、關鍵字與情境偏置(biasing)進一步提升。Meta 也指出模型原生支援超過一小時的音訊輸入與 20 人以上的講者,不需要額外的後處理步驟。

📊 **速度與準確度的帕雷托前緣**

根據 Meta 於 2026 年 9 月 1 日引用的 Artificial Analysis 數據,Muse Voice Transcribe 在串流語音轉文字與公開分聲基準測試上排名第一。

| 模型 | 最終轉錄 WER | 語音結束後延遲 |
|---|---|---|
| Muse Voice Transcribe | 3.1% | 0.16s |
| Cartesia Ink-2(語意端點) | 3.4% | 0.43s |
| ElevenLabs Scribe v2 Realtime | 3.6% | 0.14s |
| Cartesia Ink-2(外部端點) | 4.0% | 0.07s(最快但最不準) |

在首次部分轉錄(first partial transcript)上,Muse Voice Transcribe 的 WER 為 3.6%,延遲 0.13 秒。分聲部分,Meta 報告在 AMI-IHM、AMI-SDM、VoxConverse 三個資料集上的平均分聲錯誤率(DER)為 17.5%,同一張圖表中其他五套系統的區間為 21.1% 至 28.6%。價格方面,每千分鐘 3 美元低於 Cartesia Ink-2 的 4 美元,也不到 ElevenLabs Scribe v2 Realtime 與 Deepgram Flux 6.5 美元的一半。

⚠️ **沒有權重,只能透過 API 使用**

目前 Meta 並未釋出模型權重,因此沒有自架(self-hosted)的部署路徑,想用只能透過 Meta Model API。

🎯 **實務啟示**

對於正在拼接 ASR、diarization、endpointing 三套系統的語音產品團隊,Muse Voice Transcribe 展示了「用特殊 token 統一多任務輸出」是可行方向,但目前只能以託管 API 形式評估,無法整合進需要自架或離線推論的場景。

🔗 **來源**
- 標題:Meta Superintelligence Labs Releases Muse Voice Transcribe: One Real-Time Model for Streaming ASR, Diarization, and Endpointing
- 作者／機構:Michal Sutter, MarkTechPost
- 連結:https://www.marktechpost.com/2026/09/01/meta-superintelligence-labs-releases-muse-voice-transcribe-one-real-time-model-for-streaming-asr-diarization-and-endpointing/

#Meta #SpeechRecognition #ASR #Diarization #RealTimeAI #AudioAI #MuseVoiceTranscribe #MetaAI #VoiceTech #StreamingAI
