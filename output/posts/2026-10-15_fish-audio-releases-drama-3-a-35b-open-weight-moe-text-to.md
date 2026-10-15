---
title: Fish Audio Releases Drama 3, a 35B Open-Weight MoE Text-to-Speech Model
source: MarkTechPost
url: https://www.marktechpost.com/2026/10/14/fish-audio-drama-3-open-weight-tts-model/
model: claude-code/sonnet
generated_at: '2026-10-15T20:41:33.850441'
score: 98
---

📌 Fish Audio Drama 3：35B MoE 架構的開源語音模型，讀得懂「演技指令」

TL;DR：35B MoE 模型支援括號式表演指導與 83 種語言，可自架部署，單串流首音延遲僅 88.9 毫秒。

當劇本裡寫著「[咬著牙忍住]」，一般的 TTS 只會把文字唸出來，不會懂語氣——這正是 Fish Audio 這週發布的 Drama 3 想處理的落差。

🤔 從唸字到演戲：方括號裡的指示要怎麼「演」出來

Drama 3 是 Fish Audio 推出的 text-to-speech 模型，接受純文字腳本搭配方括號式的表演指示。例如在臺詞前加上「[barely holding it together]」，或用成對標籤如 <whisper> 只改變被包住的那段文字的語氣。這些指示可以用任何語言撰寫，與臺詞本身使用的語言無關，模型支援 83 種語言。透過 <|speaker:0|> 到 <|speaker:15|> 的角色標籤，單次請求最多可以安排 16 個角色，每位角色對應一個 voice ID，整場戲可以在一次 API 呼叫內完成渲染，適合用在劇本對白、有聲書與配音場景。

🧩 從 Qwen3.5-35B-A3B 到 Codebook-MTP：拆解 Drama 3 的架構

Drama 3 是一個 35B 參數的 mixture-of-experts 模型，每個 token 只啟用約 3B 參數。根據發布文章，其骨幹模型從 Qwen3.5-35B-A3B 語言模型出發，共 40 層，每 4 層中有 3 層是 Gated DeltaNet，1 層是 gated full-attention——也就是每 4 層才有 1 層保留 KV cache，其餘的 DeltaNet 層改用固定大小的狀態來儲存歷史資訊。

解碼端引入新的 Codebook-MTP decoder，取代前代 S2 使用的逐幀 Fast AR decoder：4 個共享層之後接上 9 層，每層對應一個 acoustic codebook，但只有 codebook 0 與 1 的結果會回饋進骨幹模型（S2 則是全部 10 個 codebook 都回饋）。音訊 tokenizer 沿用 S2 版本，基於 Descript Audio Codec，輸出 44.1kHz 音訊，運作速率約每秒 21.5 frames。

訓練流程分為 3 個預訓練階段，接著是指令微調，最後用強化學習收尾。RL 階段採用不含 KL 懲罰項的 GRPO，搭配單一學習到的人類偏好 reward model。

📊 發音準確度拿下第一，但整體品質仍落後對手

在 Artificial Analysis Pronunciation Robustness 測試中（針對 4 類困難英文單字由真人評審判斷發音），Drama 3 整體得分 93.2%，排名第一，高於前代 S2.1 Pro 的 88.1%。不過這項測試量的是發音，不是情感演繹，Fish Audio 對情感表現只給出質化描述。在 Artificial Analysis 的品質排行榜上，「Drama 3 Preview」的 Elo 為 1242，勝過 S2.1 Pro 的 1190，但仍落後 Eleven v4 Turbo 的 1328。

延遲方面，模型卡報告在單張 H200 上的串流表現：單一串流時，首個音訊片段的中位延遲為 88.9 毫秒，real-time factor 為 0.131；16 個串流同時進行時，吞吐量可達每秒 927.6 frames。推論透過 SGLang-Omni 服務，其融合 kernel 僅在 Hopper GPU 上驗證過。

⚠️ 自架門檻與授權限制

Fish Speech 的安裝指南要求至少 48GB NVIDIA GPU 記憶體（FP8），不支援 CPU、Apple MPS 或 AMD ROCm；MoE 專家層以 FP8 存放，其餘權重為 bf16。若使用 Hosted API，呼叫 POST /v1/tts 時要把 model header 設成 drama-3，文件特別警告：header 缺漏或打錯會「靜默」退回成 s2.1-pro。官方牌價為每 100 萬字元 50 美元，到 2026 年 11 月 12 日前有每 100 萬字元 10 美元的上市優惠價。

權重採用 Fish Audio Community License v1.0：研究與非商業用途免費；商業用途在年營收低於 50 萬美元時也免費，但要以第三方 API 方式提供服務需另外取得授權，產品上須標示「Built with Fish Audio」，且禁止未經同意複製真人聲音。

🎯 實務啟示

如果你要做的是有角色、有情緒張力的語音內容（有聲書、劇本朗讀、多角色配音），Drama 3 把「表演指導」直接做進 prompt 介面，省去另外設計情緒控制系統的工夫；但自架需要一張 48GB 以上的 Hopper 等級 GPU，商業授權門檻也要先盤清楚，中小規模試用前建議先用 hosted API 評估效果再決定是否自建。

🔗 來源
- 標題：Fish Audio Releases Drama 3, a 35B Open-Weight MoE Text-to-Speech Model
- 作者／機構：Asif Razzaq
- 連結：https://www.marktechpost.com/2026/10/14/fish-audio-drama-3-open-weight-tts-model/

#TextToSpeech #FishAudio #OpenWeight #MixtureOfExperts #TTS #SpeechSynthesis #AIAudio #Qwen #GRPO #VoiceAI
