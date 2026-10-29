---
title: 'AssemblyAI Ships AssemblyAI-TTS-1: A $15 per 1M Character Text-to-Speech API
  for Voice Agents'
source: MarkTechPost
url: https://www.marktechpost.com/2026/10/29/assemblyai-tts-1-text-to-speech-api-voice-agents/
model: claude-code/sonnet
generated_at: '2026-10-29T22:11:05.307360'
score: 79
---

📌 AssemblyAI推出TTS-1：每百萬字元15美元的語音代理用TTS

TL;DR：AssemblyAI首款TTS模型主打即時通話語音代理,用連續音訊表示法換取更快首字發聲。

當語音代理在真實電話裡回話,決定使用者會不會掛電話的往往不是模型多聰明,而是第一個字發聲前的那段延遲。AssemblyAI這次補上的,正是這塊。

🤔 補齊語音迴圈的最後一塊

AssemblyAI原本是做語音轉文字(STT)的公司,現在推出AssemblyAI-TTS-1作為第一款文字轉語音模型,正式開放使用,目標場景是即時電話通話中的語音代理。對已經在用AssemblyAI做STT的開發者來說,等於能用同一家供應商把語音迴圈從頭串到尾。

🧩 連續音訊表示,而非離散token

多數TTS模型把音訊編碼成離散token,AssemblyAI表示TTS-1改用連續音訊表示(continuous audio representations),並宣稱這樣能提升真實感、縮短「首字發聲時間」。模型訓練資料是數百萬小時的音訊,其中包含真實對話錄音。

產品面提供4,000多種聲音庫與即時語音克隆功能,發布文章示範的克隆只用了24秒錄音完成,且需要說話者確認授權。目前支援六種語言：英語、西班牙語、法語、德語、義大利語、葡萄牙語。對外介面有三種：HTTP API、WebSocket API(每段對話維持單一連線,並接受cancel訊息來實現搶話/barge-in),以及一條OpenAI相容路由。輸出格式支援mono PCM、mu-law或A-law,取樣率8kHz到48kHz,原生格式是24kHz PCM,電話系統可以直接要求8kHz mu-law;輸出也附帶word timestamps。AssemblyAI同時公開了LiveKit與Pipecat的參考agent實作。

📊 自報數字亮眼,獨立測試有落差

AssemblyAI在自家4組英文測試集、50個配對克隆聲音上,拿TTS-1跟5個模型比較,這份評測日期為2026年10月28日,是自我報告的數字。獨立評測結果則更保守：

| 來源 | 指標 | AssemblyAI TTS-1 | 對照模型 |
|---|---|---|---|
| Cekura(27個模型基準) | 讀誤準確率 | 81.5% | Inworld TTS-2 Flash 93.2% |
| Cekura | 自然度 | 4.50 | — |
| Cekura | 中位串流延遲(從最後一字送出算起) | 159 ms | Inworld TTS-2 Flash 45 ms |
| Coval leaderboard | 字詞錯誤率 | 1.7% | — |
| Artificial Analysis「可控聲音競技場」 | 排名 | 首次進前十 | — |

價格方面,AssemblyAI按輸入字元計費(含空格與標點),統一$15/每100萬字元,不論用哪個聲音、是否克隆、要不要word timestamps或EU資料處理都是同一價,沒有per-voice費用、併發費用或最低用量門檻。AssemblyAI稱這是語音代理用frontier TTS模型中最低價。但文章也指出Inworld TTS-2 Flash在on-demand情況下同樣是$15/1M,付費方案甚至降到$7,而且Inworld的on-demand層級允許5個併發請求——這是比價格更明顯的差異點。

⚠️ 價格優勢被同價競品追平

從獨立測試看,TTS-1的延遲(159ms)與準確率(81.5%)都不是對照組裡最好的,Inworld TTS-2 Flash在同樣$15/1M的價位下延遲只要45ms、準確率93.2%。素材中也沒有提到TTS-1本身的併發上限數字,這點值得在正式選型前向AssemblyAI確認。

🎯 實務啟示

如果團隊已經在用AssemblyAI做STT,TTS-1能用單一供應商簡化整合,也省去跨廠商對接的麻煩。但在真正要上線延遲敏感的語音代理之前,建議優先參考像Cekura這類獨立基準,而不是只看廠商自己發布的評測貼文,同時把併發限制這類容易被忽略的隱藏成本也納入選型考量。

🔗 來源
- 標題：AssemblyAI Ships AssemblyAI-TTS-1: A $15 per 1M Character Text-to-Speech API for Voice Agents
- 作者／機構：Michal Sutter，MarkTechPost
- 連結：https://www.marktechpost.com/2026/10/29/assemblyai-tts-1-text-to-speech-api-voice-agents/

#TTS #VoiceAI #AssemblyAI #VoiceAgents #SpeechSynthesis #ConversationalAI #LiveKit #Pipecat #TextToSpeech #AIVoice
