---
title: Simplify and support your TorchServe workloads using Ray Serve Deep Learning
  Containers
source: AWS ML
url: https://aws.amazon.com/blogs/machine-learning/simplify-and-support-your-torchserve-workloads-using-ray-serve-deep-learning-containers/
model: claude-code/sonnet
generated_at: '2026-09-09T20:09:09.861120'
score: 74
---

📌 打一段文字描述，幾秒鐘生出全新語音：Gradium Voice Design

TL;DR：Kyutai 團隊衍生的 Gradium 用文字描述直接生成全新合成語音，免克隆、免版權，已上線 API。

語音 agent 團隊常撞到同一堵牆：語音庫裡有 400 種聲音，但需求單上要的是「蒙特婁經銷商的魁北克法語女接待員」或是「六十歲、帶點講堂權威感的旁白男聲」，這種聲音庫裡永遠沒有。過去要填這個缺口，只能靠 voice cloning 一個一個聲優補進來，每一個都牽扯到來源取得、當事人同意與授權合約，速度追不上需求單的數量。

🤔 **聲音庫永遠補不齊，那就別靠聲優了**

Gradium 是從 Kyutai 研究實驗室分拆出來的巴黎新創，這次推出的 Voice Design 給出不同答案：輸入一段文字描述，幾秒鐘內直接生出全新的合成語音，不需要參考音檔、不需要真人聲優、也沒有版權要清。Voice Design 已經在 Gradium API 與 Studio 上線，所有方案（包含免費層級）都能用，保留下來的語音走的是與聲音庫裡其他語音相同的 streaming TTS endpoint，延遲與輸出格式也一致。

🧩 **描述怎麼寫，API 怎麼串**

根據官方文件，模型會回應的描述屬性包括性別、年齡區間、口音或來源地、音高、語速、能量感、音色與共鳴、語域與說話方式，以及這個聲音要執行的任務，讀起來很像選角需求單。描述長度限制在 1 到 500 字元，支援英語、法語、西班牙語、葡萄牙語、德語五種語言，官方建議在描述結尾註明用途，因為這會影響語音的語調與語域表現，而不只是聲音本身的音色。

一次請求會回傳 1 到 5 個候選語音，通常 3 到 5 秒內就緒，這些候選是同一個「角色」的變體，要換角色就得換描述，而不是多產幾個樣本。整個流程分四步：`POST /voice-generator/generate` 產生候選 id（狀態是 `ready: false`）；`GET /voice-generator/embeddings` 輪詢直到就緒；用一般的 TTS endpoint 試聽，把候選 id 當作 `voice_id` 帶入；確定要留下的那個之後，`POST /voices/from-embedding` 把它轉正。候選語音在轉正前有三個限制：試聽文字上限 100 字元、只能走 REST（不支援 TTS WebSocket 與 Speech-to-Speech）、未轉正的候選會在 30 天後刪除。轉正是免費的，會清除到期時間，並佔用一個自訂語音名額（與 clone 共用），免費層級有 5 個名額，付費方案有 1,000 個。

值得注意的是採樣刻意設計成非決定性：Gradium 會先把描述做語意擴展，而這個擴展過程每次請求都不同，所以即使描述文字與 seed 固定，產出的語音仍會不一樣。

📊 **口音表現是最大差距所在**

Gradium 做了一場盲測，針對口音描述在五種語言下做配對比較，涵蓋六套可透過公開 API 存取的語音生成系統，母語者聽兩段未標示的音檔選出較貼近描述的那個，或投「平手」。7,627 次比較中，Gradium 的勝率是 72.6%（勝率計算方式為勝場加上平手場的一半，50% 為基準線），領先第二名 ElevenLabs 的 eleven_ttv_v3（59.0%）達 13.6 個百分點，其後依序是 Inworld（44.8%）、Fish Audio（36.7%）與 MiniMax（31.7%）。Gradium 在全部五種語言都拿下第一，差距最大的落在多數聲音庫容易「拉平」的地區口音上：魁北克法語 97%、拉普拉塔河西班牙語 86%、巴伐利亞德語 85%、哥倫比亞西班牙語與非洲葡萄牙語均為 83%。

另外用 Gemini 3.1 Pro 作為模型評審，對同一批未標示的單一音檔以 1 到 5 分評分，排名結果一致：Gradium 4.06 分、ElevenLabs 3.86 分、Inworld 3.64 分、Fish Audio 3.51 分。官方產品頁另外宣稱在學術指令遵循基準 InstructTTSEval 的英語子集上，prompt adherence 達到 83.4%。

⚠️ **這些數字是誰量的**

要提醒的是，以上所有比較數據都是 Gradium 自行設計與執行的測試，屬於廠商自評結果，尚未看到第三方獨立驗證。

🎯 **實務啟示**

對需要大量客製語音角色、又受限於聲音庫規模或克隆授權流程的語音 agent 團隊來說，Voice Design 提供了一條免版權疑慮的路徑：四支 API 呼叫就能從一段文字描述走到可上線的語音，而且轉正後與既有 catalog 語音共用同一套 streaming TTS 基礎設施，不需要額外接入成本。但因為採樣非決定性，若產品需要「同一描述穩定重現同一聲音」，仍得靠轉正後鎖定 voice_id 來保證一致性，而不能依賴描述文字本身。

🔗 **來源**
- 標題：Gradium Launches Voice Design: Write a Prompt, Get a Brand New Synthetic Voice in Seconds
- 作者／機構：Michal Sutter, MarkTechPost
- 連結：https://www.marktechpost.com/2026/09/09/gradium-launches-voice-design-write-a-prompt-get-a-brand-new-synthetic-voice-in-seconds/

#Gradium #TextToSpeech #VoiceAI #SyntheticVoice #Kyutai #SpeechSynthesis #VoiceCloning #API #GenerativeAI #MachineLearning
