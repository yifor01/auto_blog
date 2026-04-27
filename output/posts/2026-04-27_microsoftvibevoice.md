---
title: "microsoft/VibeVoice"
source: GitHub Trending
url: https://github.com/microsoft/VibeVoice
score: 128
model: tencent/hy3-preview:free
generated_at: 2026-04-27T19:36:53.789612
---

📌 【Microsoft 開源】一次處理 60 分鐘音訊，VibeVoice 重新定義 ASR

還在為會議錄音、長篇訪談的語音轉文字（ASR）切割片段而苦惱嗎？微軟最新開源的 VibeVoice 直接打破了長度限制，單次就能處理長達一小時的音訊，並自動幫你整理好誰在什麼時候說了什麼。

🤔 **長音訊處理一直是 ASR 的痛點**

傳統的語音識別系統在面對長時間音訊時，往往需要複雜的切片與後處理，不僅容易丟失上下文，也難以精準標註說話者與時間戳。隨著遠端工作與多媒體內容爆發，產業急需一種能夠原生支援長上下文、且具備結構化輸出的解決方案。

🧪 **微軟開源的統一語音框架**

VibeVoice 不僅是一個模型，更是一個開源研究框架。其核心亮點包括：
- **VibeVoice-ASR**：單次處理 60 分鐘音訊，直接輸出包含 Speaker（誰）、Timestamps（何時）、Content（說什麼）的結構化轉錄。
- **多語言支援**：原生支援超過 50 種語言，並允許使用者自定義上下文（User-Customized Context）。
- **VibeVoice-Realtime-0.5B**：0.5B 參數的輕量級即時語音合成（TTS）模型，支援流式輸入與長篇生成。

 **從訓練到推論，工程落地性極高**

這個專案不僅開源了模型，還提供了一條龍的工程支援：
- **無縫整合**：已正式納入 Hugging Face Transformers 庫，幾行程式碼即可呼叫。
- **極速推論**：支援 vLLM 加速，解決語音模型常見的推論瓶頸。
- **完整工具鏈**：微調程式碼（Finetuning code）已公開，並提供 Playground 與 Colab 實作環境。

💡 **結構化輸出將改變語音流水線設計**

VibeVoice 的關鍵創新在於它不再只輸出純文字，而是輸出「結構化資訊」。這意味著開發者不再需要額外的 NLP 模型來識別說話者或對齊時間軸，大幅簡化了語音應用的後處理架構。此外，Realtime-0.5B 提供的多風格、多語言音色（包含 9 種語言及 11 種英文風格），也為語音合成社群提供了高品質的實驗基礎。

⚠️ **實驗性質與持續更新中**

雖然專案已具備高度可用性，但部分功能仍處於實驗階段。例如 Realtime-0.5B 中的多語言音色目前仍標註為「實驗性（Experimental）」，且隨著專案處於快速迭代期，API 或功能可能會隨之調整。

🎯 **GenAI 工程師的新玩具**

如果你正在建置多語言客服系統、自動會議摘要工具或長篇內容分析平台，VibeVoice 值得加入你的技術棧。
- 直接透過 Transformers 庫快速驗證 ASR 效果。
- 利用 vLLM 支援嘗試高併發的語音推論場景。
- 關注其技術報告（Technique Report），了解其處理長上下文的架構設計。

🔗 **專案連結**
📝 microsoft/VibeVoice
👤 Microsoft
🔗 GitHub: https://github.com/microsoft/VibeVoice
📑 技術報告：請參考 GitHub 頁面 Technical Report 連結

你最近有在處理長音訊轉錄的需求嗎？覺得 60 分鐘一次的處理能力夠用嗎？歡迎留言討論 👇

#Microsoft #VibeVoice #ASR #TTS #OpenSource #AI #SpeechRecognition #HuggingFace #vLLM #GenAI
