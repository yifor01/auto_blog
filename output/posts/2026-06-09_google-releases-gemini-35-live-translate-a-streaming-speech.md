---
title: Google Releases Gemini 3.5 Live Translate, a Streaming Speech-to-Speech Audio
  Model Covering 70+ Languages Across Meet, Translate, and the Live API
source: MarkTechPost
url: https://www.marktechpost.com/2026/06/09/google-releases-gemini-3-5-live-translate-a-streaming-speech-to-speech-audio-model-covering-70-languages-across-meet-translate-and-the-live-api/
score: 111
model: google/gemma-4-31b-it:free
generated_at: '2026-06-09T20:27:44.430310'
---

📌 【Google 最新發佈】Gemini 3.5 Live Translate：打破「輪替式」翻譯，實現真正的連續語音流翻譯

你是否發現目前的 AI 翻譯工具總是得等對方「說完一句話」才開始翻譯？這種 turn-by-turn（輪替式）的互動模式，在快節奏的對話中總有一種明顯的遲滯感，讓溝通變得不自然。

Google 最新推出的 Gemini 3.5 Live Translate 試圖解決這個痛點，將翻譯從「句子級別」提升到「串流級別」。

🤔 **從「等對方說完」到「同步翻譯」的範式轉移**

傳統的語音翻譯系統通常依賴於：說話者結束 $\rightarrow$ 偵測停頓 $\rightarrow$ 處理翻譯 $\rightarrow$ 輸出語音。這種模式在正式演講中可行，但在自然對話中會造成嚴重的中斷感。

Gemini 3.5 Live Translate 採取的是「連續串流處理 (Continuous Stream Processing)」。它不再等待句子結束，而是在音訊輸入的過程中同步生成翻譯，讓翻譯內容僅落後說話者數秒，大幅提升了溝通的即時性。

🧪 **核心設計：在「上下文理解」與「低延遲」之間取得平衡**

這款模型（`gemini-3.5-live-translate-preview`）的核心挑戰在於處理一個經典的 Trade-off：
- **等待更多上下文** $\rightarrow$ 翻譯品質更高、更準確。
- **立即輸出翻譯** $\rightarrow$ 延遲更低，能與說話者保持同步。

Google 的解決方案是透過優化串流處理，讓模型在維持高品質翻譯的同時，將延遲控制在極低水準，並在輸出時保留原說話者的**語調 (Intonation)、語速 (Pacing) 與音高 (Pitch)**，讓翻譯後的聲音聽起來更像原說話者，而非生硬的機器合成音。

💡 **專注於翻譯管線，而非通用 AI Agent**

值得工程師注意的一個關鍵設計決策是：Gemini 3.5 Live Translate 是一個**專門的音訊模型**，而非一個通用聊天助手。為了追求極致的即時延遲，Google 採取了以下限制：

- **純音訊路徑**：翻譯模式僅接受音訊輸入，不支援文字輸入。
- **捨棄通用功能**：在翻譯模式下，模型會捨棄「工具調用 (Tool use)」與「系統指令 (System instructions)」。

這種設計將其從一個複雜的 Agent 簡化為一個高效的「翻譯管線 (Translator Pipeline)」，確保資源全部投入在即時翻譯的效能上。此外，該模型具備強大的抗噪能力 (Noise robustness)，使其能在嘈雜且不可預測的現實環境中穩定運作。

⚠️ **功能定位明確，不支援文字輸入與 Agent 功能**

這款模型並非用來取代 Gemini 的對話能力，因此它不具備對話代理人的特質（如意圖偵測或中斷處理）。如果你需要的是一個能執行任務的 AI Agent，這不是正確的選擇；但如果你需要的是一個高效的即時翻譯引擎，它則是目前最頂尖的選擇。

🎯 **開發者與企業如何開始嘗試？**

目前 Google 已將此模型部署於三個主要入口：
1. **開發者**：可透過 Gemini Live API 與 Google AI Studio 進入公開預覽 (Public Preview)。
2. **企業用戶**：本月起於 Google Meet 開啟私人預覽 (Private Preview)。
3. **一般用戶**：透過 Android 與 iOS 的 Google Translate App 使用。

對於產品團隊而言，這意味著我們可以用於構建更自然的多語言即時通訊應用，而不再受限於傳統的「對話輪替」邏輯。

🔗 **詳細資訊**
📝 Google Releases Gemini 3.5 Live Translate, a Streaming Speech-to-Speech Audio Model
👤 Asif Razzaq via MarkTechPost
🔗 文章連結：https://www.marktechpost.com/2026/06/09/google-releases-gemini-3-5-live-translate-a-streaming-speech-to-speech-audio-model-covering-70-languages-across-meet-translate-and-the-live-api/

你認為「同步翻譯」會讓跨國遠端協作變得像面對面溝通一樣自然嗎？歡迎在評論區分享你的看法 👇

#Google #Gemini #LiveTranslate #SpeechToSpeech #AI #即時翻譯 #API #GoogleAIStudio #技術分享
