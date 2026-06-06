---
title: 'NVIDIA Releases Nemotron 3.5 ASR: A 600M-Parameter Cache-Aware Streaming Model
  Transcribing 40 Language-Locales in Real Time'
source: MarkTechPost
url: https://www.marktechpost.com/2026/06/06/nvidia-releases-nemotron-3-5-asr-a-600m-parameter-cache-aware-streaming-model-transcribing-40-language-locales-in-real-time/
score: 97
model: google/gemma-4-31b-it:free
generated_at: '2026-06-06T19:57:52.770347'
---

📌 【NVIDIA 最新開源】600M 參數一次搞定 40 種語言的即時語音辨識  

你以為要同時支援多語言就得部署多個模型、切換模型、甚至犧牲即時性？NVIDIA 只用了 **一個 600M 參數的 checkpoint**，就讓 40 個語言‑Locale 同時即時轉寫，且自帶標點與大小寫，真的讓人懷疑「多語言」與「低延遲」必須是對立的兩端。

---

🤔 **為什麼多語言即時辨識長期卡關？**  
傳統的語音辨識系統通常為每個語言訓練獨立模型，或在推論時動態切換模型。這樣不僅佔用大量記憶體，還會因為模型切換產生額外延遲，難以滿足「直播」或「即時會議」的需求。

🧪 **Nemotron 3.5 ASR 的核心設計：Cache‑Aware FastConformer‑RNNT**  
- **FastConformer Encoder (24 層)**：在 Conformer 基礎上採用線性可擴展的注意力，提升計算效率。  
- **RNNT Decoder**：逐框輸出文字，天然支援流式輸出，不需要後處理的標點恢復。  
- **Cache‑Aware 機制**：傳統的緩衝式流式會重複計算重疊音訊窗口，導致延遲與算力浪費。Nemotron 3.5 直接快取 encoder 的 self‑attention 與卷積激活，隨新音訊到來即時重用，確保每個音框只算一次，降低計算與端到端延遲，且不犧牲準確度。

 **單一 checkpoint 覆蓋 40 種語言‑Locale**  
模型在基礎的 `nvidia/nemotron-speech-streaming-en-0.6b` 上加入 **prompt‑based language‑ID conditioning**，只需在推論時提供語言提示，即可在同一個 600M 參數模型內切換 40 種語言，完全不需要額外的語言專屬模型或模型交換。

⚡ **兩大使用情境：低延遲直播 vs. 高吞吐量批次轉寫**  
- **低延遲串流**：適用於直播、會議、客服等即時應用。  
- **高吞吐量批次**：一次性處理大量錄音檔，仍能保持生產級的標點與大小寫。  

💡 **靈活的延遲‑準確度權衡**  
唯一的調整參數是 `att_context_size`（注意力上下文大小），對應的 chunk 大小分別為 80 ms、160 ms、320 ms、560 ms。縮小上下文可更快產出文字，放大則提升辨識準確度，全部由同一 checkpoint 完成。

⚠️ **研究與實務的限制**  
- 目前僅在 40 個語言‑Locale 上驗證，未說明對於低資源語言的表現。  
- 文章未提供詳細的字錯誤率（WER）或延遲數值，實際部署仍需自行測試。  
- 模型仍依賴 Prompt‑based language ID，若提示錯誤可能影響辨識品質。

🎯 **對工程師的實務建議**  
1. **直接使用開源權重**：模型已上傳至 Hugging Face，採用 OpenMDW‑1.1 授權，可自由下載與微調。  
2. **根據應用需求調整 `att_context_size`**：直播場景建議 80‑160 ms，批次轉寫可選 320‑560 ms 以提升準確度。  
3. **利用 Prompt‑based 語言條件**：在多語言服務中，只需在 API 呼叫時傳入語言代碼，即可避免部署多模型的複雜度。  
4. **結合現有音訊前處理管線**：模型已內建標點與大小寫，省去後置的 punctuation‑restoration 步驟，簡化生產流程。

🔗 **論文與資源**  
📝 NVIDIA Releases Nemotron 3.5 ASR: A 600M‑Parameter Cache‑Aware Streaming Model Transcribing 40 Language‑Locales in Real Time  
👤 作者：Asif Razzaq (MarkTechPost)  
🔗 文章連結：https://www.marktechpost.com/2026/06/06/nvidia-releases-nemotron-3-5-asr-a-600m-parameter-cache-aware-streaming-model-transcribing-40-language-locales-in-real-time/  
🤗 Hugging Face 開源權重：https://huggingface.co/nvidia/nemotron-3.5-asr  

你有在語音辨識系統中遇到多語言或低延遲的挑戰嗎？試試這個「一次搞定」的模型，或分享你自己的實作經驗吧！👇

#NVIDIA #ASR #SpeechRecognition #FastConformer #RNNT #MultilingualAI #OpenSource #MachineLearning #AIEngineering #RealTimeTranscription
