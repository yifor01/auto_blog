---
title: 'Miso Labs Releases MisoTTS: An 8B Emotive Text-to-Speech Model with Open Weights'
source: MarkTechPost
url: https://www.marktechpost.com/2026/06/04/miso-labs-releases-misotts-an-8b-emotive-text-to-speech-model-with-open-weights/
score: 92
model: tencent/hy3-preview:free
generated_at: '2026-06-04T21:01:33.391772'
---

📌 【Miso Labs 開放權重】8B 參數的 MisoTTS 能同時做到富情感與 110ms 超低延遲？

你以為更大的語音模型必然意味著更慢的回應？Miso Labs 最近釋出的 MisoTTS 用 8B 參數卻宣稱僅需 110ms 推論延遲，比某些商業方案快上六倍，同時仍能根據文字與前一段語音產生富有情感的語音。

🤔 **語音合成的兩個核心瓶頸：詞彙大小與語境條件**

傳統 TTS 模型依賴固定詞彙表來離散表示音訊，當目標空間（音高、節奏、強調、情感、口音）非常寬闊時，這種做法會遇到「詞彙大小問題」——要擴大詞彙就需要額外參數。此外，多數模型只條件於文字，忽略說話者的語調與情感，這往往導致合成語音感覺機械，甚至落入所謂的「uncanny valley」。

🧪 **以 Llama 3.2 為骨幹、搭配小型音訊解碼器的 RVQ Transformer**

MisoTTS 採用 8B 參數的 Transformer 作為語言骨幹（結構類似 Llama 3.2），外接一個較小的音訊解碼器。模型同時接受兩個輸入：文字序列與可選的前段音訊（音訊條件）。透過殘餘向量量化（RVQ），每個音訊 token 不再是單一索引，而是由 32 個 codebook 的索引組成的向量；每個 codebox 大小為 2048，且每個向量位置對應獨立的 codebook。最終音訊透過對應向量的查表與求和重建。模型使用 Mimi 作為音訊 tokenizer，最大序列長度為 2048，預設採用 torch.bfloat16 進行推論。

🚀 **宣稱的 110ms 延遲與對比基準**

根據 Miso Labs 的說明，MisoTTS 在標準設備上的平均推論延遲為 110ms。為參考，他們同時列出了兩個商業方案的延遲：ElevenLabs 約 700ms、Sesame 約 300ms。這意味著在同等硬體條件下，MisoTTS 的回應速度顯著快於既有方案。

🔍 **RVQ 如何同時解決詞彙與條件問題？**

- **詞彙問題**：透過 RVQ，模型不需要為每種可能的音訊波形分配一個離散 token；而是將音訊分解為多個低維度 codebook 的組合，這樣在不增加參數數量的情況下擴大了可表示的聲音空間。
- **語境條件**：因為模型同時條化於文字與前段音訊，它能夠在生成過程中參考說話者的語調、停頓與情感，使合成語音更具表現力且與對話歷史保持一致。

⚠️ **目前僅提供架構與延遲數據，缺少詳細主觀評測**

公開資訊中僅含模型架構描述、參數規模、最大序列長度、推論延遲以及與兩個商業系統的對比數字。未見有人工評分（如 MOS）、跨語言測試或在不同情境下的表現數據，因此無法直接判斷其在真實應用中的自然度與穩定性。

🎯 **適合對延遲與情感表現有同時需求的場景**

- 實時對話系統、即時翻譯或語音助理，低延遲是關鍵。
- 需要根據使用者語調做出即時回應的情境（例如客服機器人、互動式故事）。
- 由於權重已開放，研究與開發團隊可在該基礎上進行微調、加入多語言支援或結合特定領域的語音風格。

🔗 **發布資訊**
📝 Miso Labs Releases MisoTTS: An 8B Emotive Text-to-Speech Model with Open Weights  
👤 作者：Asif Razzaq（MarkTechPost 報導）  
🔗 報導連結：https://www.marktechpost.com/2026/06/04/miso-labs-releases-misotts-an-8b-emotive-text-to-speech-model-with-open-weights/  

你對這種「低延遲＋富情感」的 TTS 模型有什麼看法？歡迎在留言區分享你的使用經驗或潛在應用場景 👇

#MisoTTS #TextToSpeech #RVQ #AI語音 #開放權重 #低延遲 #情感合成 #MachineLearning #AI開發 #聲音技術
