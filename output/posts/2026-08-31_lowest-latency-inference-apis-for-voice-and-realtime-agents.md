---
title: 'Lowest-Latency Inference APIs for Voice and Realtime Agents: A Time to First
  Token TTFT-First Benchmark'
source: MarkTechPost
url: https://www.marktechpost.com/2026/08/30/lowest-latency-inference-apis-for-voice-and-realtime-agents-a-time-to-first-token-ttft-first-benchmark/
model: claude-code/sonnet
generated_at: '2026-08-31T12:04:58.404615'
score: 93
---

📌 語音 Agent 延遲測試：TTFT 為何是個陷阱指標

TL;DR：TTFT 只反映生成何時開始，選語音推論 API 前更該看 TTFS 與各段延遲分佈。

團隊挑 API 時最愛看的一個數字，往往是誤導他們的那個數字。Time to First Token（TTFT）標記的是生成開始的那一刻，但文字轉語音模型沒辦法把半個字唸出來，它得等到一整個子句到齊才能發聲。這中間的落差，就是一個對話感自然的 Agent 和一個老是被打斷的 Agent 之間的差距。

🤔 語音延遲是一整條預算，不是一個數字

LiveKit 把這個更貼近使用者感受的指標稱為 TTFS（time-to-first-sentence），並在其 Gemma 4 部署文章中主張 TTFS 才是使用者真正感受到的東西。這給了工程師兩個可調的旋鈕：TTFT 控制生成何時開始，每秒 token 數則控制第一個句子多快講完。只贏一項、輸掉另一項的供應商，體感依然不會快。

LiveKit 的語音 Agent 總覽把一輪對話拆成 STT 約 100–200ms、串流 LLM 約 300–500ms、TTS 約 100–200ms、WebRTC 網路約 50–150ms，端到端實務目標落在 700ms 到 1.2 秒。Pipecat 共同創辦人 Kwindla Hultman Kramer 建議把語音對語音的中位數延遲抓在 800ms，概念驗證階段可放寬到 1,500ms，並粗略拆成四等分、每段約 200ms：傳輸與媒體處理、STT 加斷句偵測、LLM 推論、TTS。Daily 的資料則提供人類基準：一般對話回應時間約 500ms，超過 800ms 的停頓就開始顯得不自然；其 2026 年 2 月的語音 Agent LLM 基準測試據此換算，文字模式 LLM 在轉錄轉語音的整條管線中，TTFT 預算大約只有 700ms。

⚠️ 讀數字前，先搞懂五個方法論細節

- 工作負載形狀決定一切：Artificial Analysis 在 2026 年 3 月把預設工作負載從 1k input token 改成 10k，更長的提示會同時拉高 TTFT 與拉低輸出速度；LiveKit 認為這更貼近真實情境，因為正式環境的 Agent 往往在提示前段就塞滿政策、人設、升級規則與工具 schema。
- 伺服器位置已內建在數字裡：Artificial Analysis 從 Google Cloud us-central1-a 的虛擬機發測，官方明講 TTFT 含網路延遲，可能因供應商的服務地點而有利或不利。
- 推理 token 也算：對推理模型而言，TTFT 指的是第一個推理 token，不是第一個答案 token，兩者分開列欄。
- 要從接收端量測：Daily 指出供應商有時只回報推論堆疊內部的 TTFT，Daily 自己是從送出請求量到 API 回傳的第一個可用 token 為止。
- 每次跑分都不一樣：Daily 直言 TTFT 在不同測試回合間變動很大，供應商也可能換推論堆疊甚至換權重卻不改模型名稱。

📊 LLM 層：吞吐量高不代表 TTFT 快

Artificial Analysis 的 API 供應商排行榜（10k input token、單一提示、72 小時中位數，2026 年 8 月 30 日擷取）顯示，晶片廠商優化的指標，跟語音 Agent 真正需要的指標常常對不上。擴散式語言模型 Mercury 2 每秒可生成 770 個 token，但首個 chunk 要等 3.07 秒，等於吃掉整條語音對話 LLM 預算的四倍。Cerebras 與 Groq 則是另一種組合：TTFT 中規中矩，吞吐量卻極高，這對 TTFS 特別有利，因為第一個 token 落地後，整句幾乎立刻講完。同一顆模型換主機也會不同：GPT-5.6 Luna（非推理版）在 Amazon Bedrock 上量得 0.59 秒，在 OpenAI 自家 API 上是 0.74 秒，代管與路由和權重本身一樣重要。

LiveKit 公布自家推論產品的數字：Gemma 4 31B 在 LiveKit Inference 上 TTFT 為 192ms，對照 Gemini 2.5 Flash 911ms、GPT-5.5 966ms、GPT-4.1 1,006ms，同一顆 Gemma 4 31B 走 OpenRouter 則要 1,876ms。LiveKit 也交代了機制：把 Gemma 跑在 SGLang 之上搭配推測解碼（speculative decoding），並刻意讓每張 GPU 少塞一點負載以壓低排隊延遲，一個熱請求大約 100ms 就開始吐 token，代價是每百萬輸出 token 1.20 美元。同一篇文章也公布整段對話的 TTFS：LiveKit 上的 Gemma 4 31B 為 354ms，Gemini 2.5 Flash 1,034ms，GPT-4.1 1,088ms，Gemini 3.0 Flash 1,267ms，GPT-5.5 1,404ms。能力面，Gemma 4 31B 在 IFBench 拿 75.6%，逼近 GPT-5.5 的 75.9%，遠高於 GPT-4.1 的 43% 與 Gemini 2.5 Flash 的 39%；但在 τ²-bench 上 GPT-5.5 以 93.9% 領先 Gemma 4 31B 的 76.9%。

📊 STT 與 TTS：斷句偵測和緩衝，比模型推論本身更關鍵

語音辨識的延遲重點不是轉錄速度，而是使用者停止說話後，系統多久才「知道」使用者說完了。Artificial Analysis 的串流 STT 排行榜從 SileroVAD 偵測到的語尾開始計時，量測首個部分轉錄與最終轉錄兩個時間點，其 AA-WER Streaming 指標取約 8 小時音訊，AA-AgentTalk 佔 50%、VoxPopuli 佔 25%、Earnings-22 佔 25%。Deepgram Flux 把語尾偵測直接融進辨識模型，而非在外面另外掛一個 VAD，官方宣稱這比傳統 STT 加 VAD 的組合能砍掉 200–600ms 的 Agent 回應延遲，並開放 eot_threshold（0.5–0.9）、eager_eot_threshold（0.3–0.9）與 EagerEndOfTurn 事件，讓開發者能提早啟動 LLM。AssemblyAI 的 Universal-Streaming 反過來直接輸出不可變轉錄，官方 2025 年自測中位數字詞輸出時間為 307ms，對照 Deepgram Nova-3 的 516ms；準確度數字（皆為供應商自報、存在爭議）方面，Universal-3.5 Pro Realtime 在公開的 Pipecat 語音 Agent 基準上錄得 6.99% WER，優於 Google Chirp3 的 9.04%、ElevenLabs Scribe v2 的 9.76%、Deepgram Flux 的 15.58%。LiveKit 另外記載了「預先生成」（preemptive generation）技巧，即在部分轉錄上就先啟動 LLM，但若最終轉錄出爐後答覆得重新生成，就等於白燒 token。TTS 端，ElevenLabs 宣稱 Flash v2.5 模型推論本身約 75ms，但官方也坦言這僅指模型推論時間，網路往返依地理位置通常還要 20–200ms，而多數音訊播放器在播放前會緩衝，常見緩衝時間是 500ms。

🎯 實務啟示

挑語音推論 API 不能只看 TTFT 排行榜，要把 TTFS、STT 斷句延遲、TTS 首音節時間與網路/緩衝加總起來看整條管線；同時留意測試的工作負載長度與伺服器位置是否貼近你的真實場景，否則排行榜前段不等於你的 Agent 感覺快。

🔗 來源
- 標題：Lowest-Latency Inference APIs for Voice and Realtime Agents: A Time to First Token TTFT-First Benchmark
- 作者／機構：Asif Razzaq／MarkTechPost
- 連結：https://www.marktechpost.com/2026/08/30/lowest-latency-inference-apis-for-voice-and-realtime-agents-a-time-to-first-token-ttft-first-benchmark/

#VoiceAI #LLM #RealtimeAI #TTFT #Latency #VoiceAgents #SpeechToText #TextToSpeech #AIInfra #Benchmark
