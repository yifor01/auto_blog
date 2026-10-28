---
title: 'NVIDIA Nemotron 3.5 Transcribe and Granary v2: Intelligent Multilingual Transcription
  You Can Prompt and Adapt'
source: HuggingFace Blog
url: https://huggingface.co/blog/nvidia/nemotron-transcribe-granary
model: claude-code/sonnet
generated_at: '2026-10-28T21:57:09.799374'
score: 92
---

📌 NVIDIA Nemotron 3.5 Transcribe：一個模型同時搞定轉錄、辨識者分離與翻譯

TL;DR：開放權重語音模型以約 4B 啟用參數打贏多項轉錄與辨識者分離排行榜，還附完整資料管線可微調。

一份「逐字正確」的錄音轉文字稿,未必是使用者真正需要的東西。多語通話、快節奏會議、醫療口述,每一種場景需要的輸出形式都不同:有時要的是翻譯,有時要的是誰在哪一句發言,有時則需要正確拼寫的專業術語。NVIDIA 這次發布的 Nemotron 3.5 Transcribe,就是想用同一個 checkpoint 把這些需求一次打包。

🤔 **轉錄、辨識者分離、翻譯與問答,合一在一個 checkpoint**

Nemotron 3.5 Transcribe 是開放權重、可用自然語言下指令的模型,現已上架 Hugging Face 與 ModelScope。它能轉錄 40 種語言,支援其中 31 種語言與英文互譯,並能在 13 種語言中進行辨識者分離(diarization)。模型可處理長達一小時的錄音,並標記最多 8 位講者。開發者可以用自然語言引導輸出格式,決定音訊在哪裡處理,也能針對特定領域詞彙與口音進行調整。量化版本即將推出,屆時可在 RTX Spark、DGX Spark、Jetson AGX Thor 等裝置上本地執行,或在 Blackwell 資料中心 GPU 上擴展規模。

🧩 **Sortformer 講者線索直接進語言模型,混合 Mamba-Transformer MoE 架構**

同一段會議錄音,模型可依指令產生完全不同的輸出,例如「轉錄並標記每位講者」、「把這段音訊翻成英文」,或「這場會議做出了哪些決定」。架構上,Transcribe 把語音編碼器與一個混合 Mamba-Transformer 的 mixture-of-experts 語言模型搭配使用,30B 參數中每個 token 只啟用約 4B。Sortformer 產生的講者線索會與聲學特徵一起送進語言模型,讓模型在生成文字的同時就能標記發言輪次,而不是單純依賴後處理步驟把講者對應回文字。

📊 **多個排行榜拿下開放權重模型第一**

| 排行榜 | 項目 | Transcribe 成績 | 對比 |
|---|---|---|---|
| Hugging Face Open ASR Leaderboard | 英文 WER | 5.33%(開放權重第一) | — |
| 同上 | 多語(7 語言平均) | 4.62% | 開放權重模型最低 |
| 同上 | 長篇音訊 | 10.98% | 開放權重模型最低 |
| Artificial Analysis AA-WER | 整體 | 2.8%(並列開放權重第一) | 約 4B 啟用參數 vs. 對手 24B |
| Artificial Analysis AA-AgentTalk | 語音 agent 場景 | 1.8% WER | 次佳開放權重模型為 2.3% |
| David AI DAI-ASR-I18N(21 語言) | 綜合轉錄+辨識者分離 | 開放權重第一、整體第二 | — |
| 同上(辨識者分離子項) | DER | 18.26% | 14 個系統中最低,略勝 Nemotron 3 Diarization 的 18.38% |
| VoiceArena Diarization-Bench(英文) | cpWER | 32.4% | 14 系統中最低;刪詞率 8.32% vs. 中位數約 31% |

💡 **Granary v2 資料管線 + 微調,把 WER 再降 45.8%**

除了模型本身,NVIDIA 同時開放了 Granary v2 的多語資料與可重複使用的資料整理管線(Hugging Face 與 ModelScope 皆有提供),搭配 NeMo Speech 微調工具,讓開發者能把「prompt 層級的控制」延伸到訓練層級。文中提到的一個醫療案例研究顯示,針對未見過的講者進行微調後,word error rate(WER)比單純用最佳 prompt 的表現相對降低了 45.8%。這代表遇到特定術語或口音時,除了寫 prompt 提示詞彙(例如列出 HbA1c、metformin 等術語),更進一步的做法是直接微調模型。

⚠️ **任務對語言的支援程度不一,仍需人工覆核**

模型卡上提到,不同任務支援的語言範圍並不相同,而音訊問答(audio question answering)目前只在英文上訓練。NVIDIA 也提醒,無論哪種語音模型,都建議對人名、講者切換與問答結果進行抽樣核對。

🎯 **對工程師的啟示**

對於要做會議紀錄、客服逐字稿或多語內容分析的團隊,這個模型的價值在於「一個 checkpoint 換不同 prompt」就能切換任務,不必維護多套模型;而 Granary v2 的開放資料管線,則讓有特定術語或口音需求的團隊有機會自行微調,而不是只能依賴 prompt engineering。

🔗 **來源**
- 標題：NVIDIA Nemotron 3.5 Transcribe and Granary v2: Intelligent Multilingual Transcription You Can Prompt and Adapt
- 作者／機構：NVIDIA(Maryam Motamedi、Piotr Żelasko、Kunal Dhawan 等),Hugging Face Blog
- 連結：https://huggingface.co/blog/nvidia/nemotron-transcribe-granary

#NVIDIA #SpeechToText #ASR #Diarization #MultilingualAI #OpenWeightModels #NeMo #MachineLearning #VoiceAI #HuggingFace
