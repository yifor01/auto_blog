---
title: 'Alibaba Qwen Releases Qwen-Audio-3.1-Realtime: A Full-Duplex Voice Model Trained
  to Think, Act, and Decide When to Speak'
source: MarkTechPost
url: https://www.marktechpost.com/2026/09/28/alibaba-qwen-releases-qwen-audio-3-1-realtime-a-full-duplex-voice-model-trained-to-think-act-and-decide-when-to-speak/
model: claude-code/sonnet
generated_at: '2026-09-29T21:40:21.886849'
score: 96
---

📌 Qwen-Audio-3.1：能自己決定何時開口的全雙工語音模型

TL;DR：阿里 Qwen 推出全雙工語音代理模型 Qwen-Audio-3.1-Realtime，能自主判斷聆聽、插話與沉默的時機，同時大砍 API 價格。

多數語音助理仍是「你說完、我才開始想」的半雙工邏輯，打斷、搶話、該閉嘴時卻硬要插嘴的尷尬並不少見。Qwen-Audio-3.1-Realtime 想解決的正是這個問題：讓模型自己判斷什麼時候該聽、該說、該停、該接續。

🤔 背景：一套 5 模型的音訊堆疊

Alibaba 的 Qwen 團隊發布 Qwen-Audio-3.1，涵蓋 ASR、TTS 與即時互動的 5 模型組合，主力是為會呼叫工具的語音代理設計的全雙工模型 Qwen-Audio-3.1-Realtime。同時大幅調降價格：Realtime 降約 85%、TTS 降約 70%、ASR 最高降 95%。目前僅提供受管理的 API 服務，qwen-audio-3.1-realtime-plus 透過 WebSocket 在 QwenCloud 上線，官方未釋出開源權重。

🧩 三個模型接力完成一次對話

系統由兩個共用 Audio Encoder 與 LLM 設計的模型組成：一個全雙工決策模型持續判斷「該繼續聽、該開口、該停止，還是該接續」；一個語音轉文字模型把回應內容寫成文字；接著一個具備上下文感知能力的語音渲染器，把文字轉成串流語音，同時參考對話歷史、聲音線索與聲學情境。

模型規格上，文字與語音都可作為輸入與輸出，context 視窗達 26.2 萬 tokens（最多 24.5 萬輸入、1.6 萬輸出），預設限制為每分鐘 60 次請求、10 萬 tokens。功能涵蓋 function calling、網頁搜尋、結構化輸出、context cache 與 fine-tuning。另一款搭配模型 Qwen-Audio-3.1-ASR-Flash-Filetrans 則專攻離線長音訊轉錄，支援熱詞、語者分離、標點符號，以及多語言與中文方言辨識。

📊 訓練分三層：Think、Act、Speak and Coordinate

官方將訓練拆成三層。第一層 Core-Cocktail SFT，用百萬小時等級的配對資料，把 audio 模型重新錨定回其文字 LLM 的能力基礎。第二層是 Multimodality OPD（on-policy distillation）：由一個 Text Teacher 與一個凍結的 Audio Reference，針對學生模型自己產生的軌跡逐 token 評分，而不是模仿預先寫好的標準答案。第三層則針對同理心、語用意圖、聲學場景訓練出各自的 domain expert，以 GRPO 訓練，再透過 Multi-Teacher OPD 合併成單一可部署模型。

每個訓練領域都綁定一組工具池、一個具狀態的 JSON 資料庫，以及一份自然語言業務政策，領域本身則是從開源工具與 MCP 伺服器定義中取樣而來。每個任務只有三種結局：完成寫入、合理拒絕，或判定請求無法支援。評分邏輯先檢查最終狀態，再檢查是否有權限進行的寫入操作，最後才看行為層面的判斷，也就是說回應說得再流暢，只要狀態檢查沒過關也拿不到分；GRPO 的獎勵則分別在對話、里程碑、輪次三個層級給出。

在搜尋訓練上，官方設計了一個懲罰重複查詢的獎勵機制：當模型發出的查詢數量超過參考查詢數量時，獎勵會按比例被打折。結果是平均每次搜尋呼叫的查詢數從 4.37 降到 1.05，但觸發搜尋的 F1 分數也從 60.87% 微幅降到 58.61%。

📊 全雙工判斷的進步與代價

這一層決定模型何時、是否、如何開口。在 Full-Duplex-Bench v1.5 上，模型誤把「別人在跟第三方講話」當成該回應的比例，從 0.13 降到 0.03；v3.0 上的填充語（filler）出現率從 0.7590 降到 0.2960。但也有取捨：被打斷之後，模型「不該恢復卻恢復說話」的比例從 0.035 上升到 0.130，打斷後的停止延遲是 1.116 秒，相較 GPT-Realtime-2 的 0.383 秒明顯較慢。

其他評測上，對比 3.0 版本，Audio MultiChallenge 分數從 47.12 提升到 52.21，14 種語言的 BBA 平均分從 81.7% 升到 88.1%，FLEURS 的詞錯誤率從 9.01 降到 3.98（官方註明 τ-Voice 的數字是用半雙工的語音轉文字方式量測，不能直接與正式全雙工結果比較）。在 50 場人類 red-team 對話測試中，GPT-Realtime-2 仍以 96.00% 對 92.00% 領先。

💡 定價

Qwen-Audio-3.1-Realtime 的價格為每百萬 audio input tokens 6.4 美元、每百萬 text input tokens 0.8 美元，輸出（文字加語音）每百萬 tokens 24 美元，純文字輸出不收費。官方也提醒，不同供應商對音訊的 tokenize 方式不同，跨廠牌價格不能直接類比。Qwen-Audio-3.1-ASR-Flash-Filetrans 的價格則是輸入 0.15 美元、輸出 0.47 美元（每百萬 tokens）。

⚠️ 限制

打斷後「不當恢復說話」的比例上升，加上停止延遲慢於 GPT-Realtime-2，顯示全雙工判斷的擬真度與反應速度目前仍有妥協；人類 red-team 評測也顯示整體表現尚未超越 GPT-Realtime-2。此外目前沒有開源權重，只能透過 QwenCloud 的受管理 API 使用。

🎯 實務啟示

如果你正在打造會呼叫工具的語音代理（客服、語音下單、多輪任務型助理），Qwen-Audio-3.1-Realtime 把「何時該說話」做成獨立的決策層，而不是單純的靜音偵測，有助於降低搶話與尷尬沉默。正式導入前，建議針對你的實際打斷場景測試延遲與誤判率，並留意目前只能透過 API 使用、無法自行部署的限制。

🔗 來源
- 標題：Alibaba Qwen Releases Qwen-Audio-3.1-Realtime: A Full-Duplex Voice Model Trained to Think, Act, and Decide When to Speak
- 作者／機構：Asif Razzaq，MarkTechPost
- 連結：https://www.marktechpost.com/2026/09/28/alibaba-qwen-releases-qwen-audio-3-1-realtime-a-full-duplex-voice-model-trained-to-think-act-and-decide-when-to-speak/

#Qwen #Alibaba #VoiceAI #FullDuplex #SpeechAI #AIAgents #TTS #ASR #GRPO #ConversationalAI
