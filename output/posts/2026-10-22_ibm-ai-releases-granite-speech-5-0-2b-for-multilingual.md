---
title: IBM AI Releases Granite Speech 5.0 2B for Multilingual Transcription and Translation
source: MarkTechPost
url: https://www.marktechpost.com/2026/10/22/ibm-granite-speech-5-0-2b-release/
model: claude-code/sonnet
generated_at: '2026-10-22T20:56:53.767842'
score: 88
---

📌 IBM 開源 Granite Speech 5.0 2B：WER 5.68%，僅次 Qwen3-ASR

TL;DR：IBM 以 Apache 2.0 授權開源 2B 參數語音模型，支援 6 語言轉錄與翻譯，在 Open ASR Leaderboard 排名第二。

🎣 在 Open ASR Leaderboard 上，IBM 新模型的平均英文 WER（word error rate，字詞錯誤率）是 5.68%，只輸給 Qwen3-ASR-1.7B 的 5.40%。對一個 2B 參數、Apache 2.0 授權的開源模型來說，這個名次值得工程師多看一眼。

🤔 多語音辨識不只是「準」，還要「快」與「可標註說話者」

IBM 這次一次更新三顆模型：新發布的 Granite Speech 5.0 2B，主打 6 語言轉錄與翻譯；邊緣裝置用的 Turbo CTC，做快速的 on-device 轉錄；以及專注語者分離（diarization）的 4.1 2B Plus，用於標註逐句是誰在講話。三者分工對應 README 列出的三種開發者需求：精確轉錄、裝置端快速轉錄，以及帶說話者標記的轉錄稿。

🧩 編碼器 + Q-former + LoRA 微調的 LLM

依模型卡揭露的資訊，Granite Speech 5.0 2B 由三部分組成：
- 語音編碼器：16 層 Conformer block，以 CTC（Connectionist Temporal Classification）訓練，並對 4 秒的音訊區塊做 block attention。
- 2 層 window Q-former：負責把聲學 embedding 投影並降採樣，總降採樣倍率達 10 倍，讓後端 LLM 看到的是 10Hz 的語音表徵。
- 語言模型主體：採用 granite-4.0-1b-base 的中間 checkpoint，用 YaRN 技術將上下文擴展到 16k token，再以 LoRA adapter 微調。

訓練資料用了 39 萬小時的公開語音，加上針對日文 ASR、關鍵字偏置（keyword biasing）與翻譯任務設計的合成資料。整套訓練在 8 張 H100 上跑了 40 天。

📊 單語與多語表現：日文最吃力，關鍵字偏置效果最明顯

需留意一個數字出入：模型卡顯示 Open ASR Leaderboard（涵蓋 9 個公開測試集與 2 個私有測試集，統計至 2026 年 10 月 21 日）平均英文 WER 為 5.68%；但 IBM 官方部落格另給出 5.06%，註明是非官方數字，日期為 10 月 15 日，且只平均公開的短語音測試集。兩者計算範圍不同，不是矛盾。

細看單一測試集，表現差異相當大：

| 測試集 | WER / 指標 |
|---|---|
| LibriSpeech Clean | 0.99% |
| LibriSpeech Other | 2.21% |
| 私有對話測試集 | 13.79% |
| FFASR（嘈雜環境，42 個模型中排第 4） | 14.80%（Qwen3-ASR-1.7B 為 13.41%） |
| CommonVoice 葡萄牙文 | 2.60% |
| CommonVoice 西班牙文 | 3.50% |
| CommonVoice 日文 | 10.74%（最弱語言） |

翻譯方向上，CoVoST X-to-English 的 BLEU 分數，葡萄牙文到英文達 53.6，德文到英文則是 40.1；英文到中文沒有被評估。

最明顯的提升出現在關鍵字偏置：在 Earnings-22 測試集上，給定正確關鍵字清單時，keyword F1 從 67.2 跳到 90.1；即便關鍵字清單混有 2,000 個正確與錯誤詞彙，仍能維持在 82.8。

另外兩個更新模型也有具體進步。Turbo CTC 維持 470M 參數規模，支援語言數擴展到 7 種，並加上原生標點與大小寫；IBM 透過編譯單一 Conformer block 並在整個堆疊中重複使用運算圖，把吞吐量從上線時約 12,600 RTFx 拉高到 19,870 RTFx。4.1 2B Plus 則是免重新部署的權重更新：平均時間戳偏移從 210.86 降到 98.54，長語音 WER 從 13.53 降到 10.22，關鍵字偏置 WER 從 11.79 降到 6.48。

⚠️ 量化精度在長音訊上要留意

IBM 的部署建議是：Granite Speech 5.0 2B 可在 Transformers、vLLM、llama.cpp 與 mlx-audio 上執行；若要用 GGUF 格式，官方建議 Q8_0，因為更低位元的量化在處理超過約 1 分鐘的音訊時會明顯掉準度。

🎯 實務啟示

對要自建語音轉錄或翻譯服務的團隊，這是少數同時公開架構細節（Conformer + Q-former + LoRA）與排行榜數字的開源選項，方便直接比較自家場景的語言分布（尤其是日文較弱這點要注意）再決定是否導入；若目標是邊緣裝置或高吞吐量場景，Turbo CTC 的 RTFx 提升也值得評估。

🔗 來源
- 標題：IBM AI Releases Granite Speech 5.0 2B for Multilingual Transcription and Translation
- 作者／機構：Asif Razzaq, MarkTechPost
- 連結：https://www.marktechpost.com/2026/10/22/ibm-granite-speech-5-0-2b-release/

#IBM #GraniteSpeech #SpeechRecognition #ASR #OpenSource #Multilingual #TextToSpeech #MachineLearning #Transformers #AIModel
