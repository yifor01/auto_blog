---
title: Revisiting ASR Error Correction with Specialized Models
source: Apple ML
url: https://machinelearning.apple.com/research/asr-error-correction
score: 88
model: google/gemma-4-31b-it:free
generated_at: '2026-07-06T20:33:53.892919'
---

📌 【Apple 研究】捨棄 LLM？用輕量化 seq2seq 模型更精準地校正 ASR 錯誤

TL;DR：Apple 提出專用 seq2seq 模型校正 ASR 錯誤，參數僅 LLM 的 1/15，且在低錯誤率情境下表現更佳。

當前自動語音辨識（ASR）的校正大多依賴純文字模型，但這些模型並不瞭解 ASR 特有的錯誤模式。雖然近期許多人嘗試用大型語言模型（LLM）來校正，但高延遲與幻覺（Hallucination）問題成了實務上的痛點。

🤔 **LLM 在語音校正上的兩大短板**

儘管 LLM 擁有強大的語言能力，但在處理 ASR 校正時面臨兩個核心挑戰：
1. 推論成本過高，導致延遲增加。
2. 在錯誤率較低的片段中，LLM 容易產生幻覺，反而將正確的文字改錯。

🧩 **用合成資料訓練輕量化 seq2seq 模型**

Apple 的研究團隊重新審視了小型 seq2seq 模型的潛力，透過以下方式提升校正效能：

- **合成語料庫構建**：為了擴大訓練規模，研究團隊採用「TTS（文字轉語音）$\rightarrow$ ASR（語音轉文字）」的級聯流程來產生合成資料。研究發現，關鍵在於讓合成資料的分佈與真實的 ASR 錯誤分佈保持一致。
- **校正優先解碼（Correction-first Decoding）**：提出一種新策略，先由校正模型生成候選結果，隨後利用 ASR 的聲學分數（Acoustic Scores）對這些候選結果進行重新評分（Rescore），以確保校正結果與原始音訊相符。

📊 **參數少 15 倍，效能卻超越 LLM**

實驗結果顯示，該專用模型在 LibriSpeech 測試集上的表現優於 LLM：
- **WER 表現**：在 test-clean 與 test-other 資料集上，字錯率（WER）分別降低至 1.5% 與 3.3%。
- **泛化能力**：該模型能跨不同的 ASR 架構（如 CTC, Seq2seq, Transducer）以及不同領域運作。
- **精準度**：在低錯誤率（low-error regime）的情境下，該模型能提供比 LLM 更精準的校正。

🎯 **實務啟示：專用模型勝過通用巨獸**

對於需要部署在端側或對延遲極其敏感的語音應用，不必強行使用 LLM 做後處理。透過「合成資料模擬錯誤分佈」搭配「聲學分數重新評分」的輕量化方案，可以在大幅降低計算成本的同時，避免 LLM 常見的幻覺問題。

🔗 **來源**
- 標題：Revisiting ASR Error Correction with Specialized Models
- 連結：https://machinelearning.apple.com/research/asr-error-correction

#ASR #SpeechRecognition #NLP #Seq2Seq #AppleML #ErrorCorrection #LLM #WER #MachineLearning #SpeechProcessing
