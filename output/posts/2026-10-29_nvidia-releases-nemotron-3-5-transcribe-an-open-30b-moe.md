---
title: 'NVIDIA Releases Nemotron 3.5 Transcribe: An Open 30B MoE Model for 40-Language
  Transcription with ~4B Active Parameters'
source: MarkTechPost
url: https://www.marktechpost.com/2026/10/28/nvidia-nemotron-3-5-transcribe-open-speech-llm/
model: claude-code/sonnet
generated_at: '2026-10-29T22:03:32.041170'
score: 93
---

📌【NVIDIA】一個模型、五種指令，Nemotron 3.5 Transcribe 想取代整條語音工具鏈

TL;DR：NVIDIA 開源一個 340 億參數的語音 LLM，單一 checkpoint 涵蓋 40 語言、長達一小時錄音，靠文字指令切換五種輸出格式。

多語言語音辨識系統過去通常是拼出來的：一套 ASR 做轉錄、一套做 diarization 認出是誰在說話、再一套做時間對齊。NVIDIA 這次直接把這整條鏈塞進一個會聽指令的模型裡。

🤔 **背景：轉錄沒有「唯一正確答案」**

NVIDIA 在技術報告中的立場很明確：同一段錄音，數字該寫成阿拉伯數字還是文字、填充詞要不要留、專業術語要照術語還是口語，答案取決於誰在讀這份轉錄稿。因此 Nemotron 3.5 Transcribe 被定位為「轉錄專家模型」，而不是通用助手，靠一句文字指令就能切換輸出風格：逐字稿（verbatim）、書面體（written form）、標註說話者、帶上下文、或直接輸出翻譯結果。

🧩 **架構：SALM，把聲音變成 LLM 看得懂的嵌入**

這是一個 speech-augmented language model（SALM）：音訊編碼器把聲音轉成嵌入向量，再餵進 LLM 解碼器，讓轉錄這件事變成可以用自然語言指令控制的任務。模型名稱寫的是 30B-A4B（MoE 架構，約 40 億個啟用參數），但實際 checkpoint 大小約 340 億參數，多出來的重量來自一個 13 億參數的 MTP（multi-token prediction）模組以及音訊相關元件。

🧩 **訓練資料與設置**

訓練分兩階段：先在 256 張 H100 上跑了一輪 28,500 步的監督式微調（SFT），接著是一個較短的強化學習階段，共 400 次 GSPO 更新，獎勵訊號設計為「1 減去 WER（word error rate）」，也就是辨識錯誤率越低獎勵越高。整個訓練過程模型看過約 172 萬小時的不重複音訊，若把重複計算進去則達到 650 萬小時。

📊 **推論速度：有驚喜，但有但書**

權重同時提供 BF16、FP8、NVFP4 與 GGUF 格式，並附帶一個可選的 DFlash2 草稿模型（draft model）用於推測解碼，授權採用 OpenMDW-1.1，允許商業用途。推論可透過 vLLM 0.32.0（搭配 NeMo Speech 插件）、Transformers 或 SGLang-Omni 0.2.0 執行，vLLM 並提供 OpenAI 相容 API。

速度亮點來自 NVIDIA 自家的 Nemotron Transcribe NIM：在 NVFP4 加 DFlash2 的組合下，單張 RTX PRO 6000 Blackwell Server Edition 每秒可處理 2,238 秒的音訊，一段 30 秒的錄音只需 0.13 秒就能拿到結果。但但書是，這些推論最佳化目前還沒有開源，NVIDIA 自己估計發布當下可用的 vLLM 路徑速度大約慢了一半。作為對照，單張 H100 用 BF16 搭配 MTP2 的即時倍速（RTFx）大約是 410。微調方面，NVIDIA 測試了 17 個任務，每個任務在單張 GB300 上大約耗費 0.5 到 2.3 GPU-小時。

⚠️ **限制**

命名上的 30B-A4B 與實際約 34B 的 checkpoint 大小存在差異,使用者需留意顯存規劃上不能只看命名。NVIDIA 報告中引用的競品分數來自 2026 年 10 月的 Hugging Face leaderboard，但由於評測集後來有調整，報告也特別提醒其中兩列 WER 數據並不能直接互相比較，解讀排行榜分數時需謹慎。另外，真正讓這個模型跑得快的推論最佳化仍是閉源狀態，社群要等到相關程式碼釋出才能複現報告中最誘人的速度數字。

🎯 **實務啟示**

如果你的產品需要處理多語言、長錄音又要求不同輸出格式（例如客服逐字稿 vs. 會議摘要 vs. 多語翻譯），用一個可指令控制的模型取代多套獨立工具鏈，能省下不少整合與維運成本；但在正式評估前，應該用自己的資料實測 WER 與延遲，而不是直接套用官方報告中的跨模型比較。

🔗 **來源**
- 標題：NVIDIA Releases Nemotron 3.5 Transcribe: An Open 30B MoE Model for 40-Language Transcription with ~4B Active Parameters
- 作者／機構：Asif Razzaq，MarkTechPost
- 連結：https://www.marktechpost.com/2026/10/28/nvidia-nemotron-3-5-transcribe-open-speech-llm/

#NVIDIA #SpeechAI #ASR #OpenWeights #MoE #Transcription #SALM #LLM #SpeechRecognition #AIResearch
