---
title: 'NVIDIA Releases Nemotron 3 Diarization: A 100M-Parameter Open-Weight Model
  That Tracks 8 Speakers in Real Time'
source: MarkTechPost
url: https://www.marktechpost.com/2026/09/23/nvidia-releases-nemotron-3-diarization/
model: claude-code/sonnet
generated_at: '2026-09-23T20:36:24.431636'
score: 97
---

📌 NVIDIA Nemotron 3 Diarization：一億參數開源模型即時追蹤 8 位講者

TL;DR：NVIDIA 開源可商用的語者分離模型，單一 checkpoint 同時支援離線與即時串流，最多追蹤 8 位講者。

會議記錄轉成逐字稿只是第一步，真正麻煩的是「誰說了這句話」。少了這層資訊，摘要工具無法判斷是誰做出承諾、誰提出異議。NVIDIA 這次釋出的 Nemotron 3 Diarization，就是專門解決這個問題的開源模型。

🤔 ASR 給你文字，但不告訴你是誰說的

自動語音辨識（ASR）只能產生文字內容，語者分離（diarization）則輸出每位講者發言的時間區間。兩者結合後才能產生「語者標註逐字稿」，這也是會議工具、通話分析、Podcast 處理流程與語音代理記憶系統共同依賴的底層能力。NVIDIA 先前的 Streaming Sortformer（diar_streaming_sortformer_4spk-v2.1）只能處理 4 位講者，Nemotron 3 Diarization 將上限提升到 8 位，目標鎖定多人交談、聲音重疊的混亂場景。

🧩 從 Mel-spectrogram 到 8 通道機率張量

模型接受 16kHz 單聲道音訊（.wav/.flac/.opus/.mp3），先轉換成 10ms 步長的 Mel-spectrogram 特徵，再以 8 倍堆疊產生 80ms 的 encoder frame。一個 31 層、搭配旋轉位置編碼（RoPE）的 Transformer encoder 處理這些 frame，之後由 Conv1D 層將預測結果上採樣回 10ms 解析度，最終輸出一個 [T, 8] 的逐講者發言機率張量。

這個設計讓重疊語音處理變得直接：若兩人同時說話，對應的兩個通道會同時被啟動。模型沿用 Sortformer 的做法，依講者出現的先後順序分配通道（第一個新聲音進入 channel 1，第二個進入 channel 2……），確保串流過程中的標籤穩定，不需要每個音訊區塊都重新配對講者與通道。串流推論則靠兩套記憶機制運作：保留先前區塊講者資訊的 Arrival-Order Speaker Cache（AOSC），以及提供近期上下文的 FIFO 佇列。輸出的標籤是匿名的，要對應到真實身分需由下游應用自行處理。

📊 對比 4 講者基準模型的表現

在 Voice Arena 的 Diarization-Bench 初步結果中，這個模型在 12 個系統、17 種設定中排名第一，測試涵蓋 139 段英語對話、共約 22 小時，DER（diarization error rate）為 14.72%，優於次名系統的 19.3%，相對降幅約 24%（NVIDIA 也提醒此結果可能隨 Voice Arena 完成正式版評測而變動）。

| 比較基準 | 表現 |
|---|---|
| 對比 4 講者基準（延遲 1.04s） | 8 項評測條件 DER 全數下降，相對降幅 9.0%（CALLHOME-Part2）至 65.2%（NOTSOFAR1 MHM），未加權平均降幅 41.0% |
| 唯一回退案例 | 2 講者 CALLHOME 於 30.4s 設定下 DER 由 5.68% 微升至 5.98%，但完整 CALLHOME-Part2 仍由 10.32% 改善至 9.10% |
| 吞吐量 | 30.4s 設定下達 15,113× RTFx，對比基準模型的 2,619×（BF16、RTX PRO 5000、torch.compile()，屬批次數字非單串流延遲） |

訓練資料結合約 10,000 小時真實對話與 82,611 小時模擬多人混合音訊，其中包含向 David AI 授權、涵蓋 21 種語言的多講者音訊；加入這批資料後，複合 DER 由 11.19% 降至 10.42%。

延遲公式為 (chunk + right context) × 80ms，技術上可用 80ms 緩衝區運行，但官方建議的最低設定是 0.32 秒。

⚠️ 超過 8 人與嘈雜環境仍是弱點

模型卡明確列出限制：講者數超過 8 人時可能出現漏判或誤判，強噪音、混響與遠場收音也會提高錯誤率。

🎯 實務啟示

安裝方式為透過 NVIDIA NeMo Speech（Python 3.12 以上），輸出格式為 `start end speaker_id`，若要同時取得文字內容，可搭配 Parakeet TDT 0.6B v3 使用官方 ASR 整合指南。NVIDIA 也提供了含合成對話、即時麥克風、多語即時麥克風與檔案上傳功能的 Demo Space；正式部署則可透過 Baseten、DigitalOcean，或用 Argmax Pro SDK 3 做裝置端部署。模型權重採用 OpenMDW License 1.1 授權、允許商業使用，是目前少數可直接落地的開源語者分離方案。

🔗 來源
- 標題：NVIDIA Releases Nemotron 3 Diarization: A 100M-Parameter Open-Weight Model That Tracks 8 Speakers in Real Time
- 作者／機構：Asif Razzaq, MarkTechPost
- 連結：https://www.marktechpost.com/2026/09/23/nvidia-releases-nemotron-3-diarization/

#NVIDIA #SpeakerDiarization #OpenSource #NeMo #SpeechAI #ASR #VoiceAI #Transformer #EdgeAI #MachineLearning
