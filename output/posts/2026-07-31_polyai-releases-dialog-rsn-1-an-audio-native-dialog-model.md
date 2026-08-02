---
title: 'PolyAI Releases Dialog-RSN-1: An Audio-Native Dialog Model That Fuses Turn-Taking,
  Speech Recognition, Function Calling, And Response'
source: MarkTechPost
url: https://www.marktechpost.com/2026/07/30/polyai-releases-dialog-rsn-1-an-audio-native-dialog-model-that-fuses-turn-taking-speech-recognition-function-calling-and-response/
model: tencent/hy3:free
generated_at: '2026-07-31T08:38:35.362089'
score: 94
---

📌 【PolyAI 新技術】Dialog-RSN-1 登場：直接「聽」聲音而非讀逐字稿的對話模型

TL;DR：PolyAI 推出音訊原生對話模型 Dialog-RSN-1，將語音辨識與對話生成整合，解決傳統串聯架構丟失語氣資訊的問題。

🎣 傳統的語音助手在對話時，往往像是「聽完、轉成文字、再讀文字」的過程，這導致對話中細微的語氣、猶豫與情緒完全消失。PolyAI 提出的 Dialog-RSN-1 正試圖打破這個僵局。

🤔 **傳統架構的權衡與困境**

目前主流的語音對話架構主要分為兩大類，但各有其致命傷：

- **串聯式堆疊 (Cascaded Stack)**：將 ASR（語音辨識）的最佳預測結果傳給 LLM。缺點是語氣、猶豫與辨識不確定性在進入 LLM 前就已消失，且需要手動調整 endpointing 與 ASR 偏置參數，難以跨場景通用。
- **語音對語音模型 (Speech-to-speech)**：如 GPT Realtime 或 Gemini Live。雖然保留了音訊，但將聲音直接編碼進模型，限制了對發音的控制，且全雙工 (full-duplex) 版本會導致整通電話都佔用 GPU 資源。

🧩 **Dialog-RSN-1 的設計理念：音訊感知但非全音訊生成**

Dialog-RSN-1 採取了一種折衷但高效的架構：它在輸入端是「音訊感知 (audio-aware)」的，模型直接對原始音訊進行推理，但將生成端交給獨立且可透過提示詞 (promptable) 控制的 TTS 系統。

其運作流程如下：
1. 使用高召回率的 VAD (語音活動檢測) 搭配計時器來決定何時執行模型。
2. 模型接收原始音訊並進行推理，並根據模型產生的第一個 token 來決定代理人 (agent) 是否應該說話。
3. 決定對話輪次 (turn-taking) 是由具備完整上下文的模型做出，而非僅靠廉價的聲學線索。
4. 轉錄 (Transcription) 流程會在回應產生後才執行。

📊 **針對極低延遲進行的效能最佳化**

為了在 A100 GPU 上達成低於 300ms 的延遲目標，PolyAI 針對候選模型（預估在 8B 密集模型至 30B 稀疏模型之間）進行了一系列工程實踐：

- **預填 (Prefilling)**：在使用者說話時同步預填 attention cache。
- **提示詞優化**：使用 append-only 的提示詞模板以減少 cache 失效。
- **路由策略**：將每位來電者路由至同一臺 GPU。
- **投機採樣 (Speculative Drafting)**：使用經過微調的投機草稿模型，平均接受度為 3.9 個 tokens。
- **自動推理**：在 RFT (Reinforcement Fine-Tuning) 過程中學習自動推理能力。

⚠️ **目前僅限現有客戶使用**

雖然 Dialog-RSN-1 已應用於實際生產環境，但目前並未開放權重或公開 API。現有客戶可以直接啟用，新客戶則需申請早期存取權。

🎯 **實務啟示**

對於開發語音 AI 的工程師來說，Dialog-RSN-1 證明了「音訊感知輸入 + 獨立 TTS 輸出」可能是平衡「語氣理解」與「發音控制」與「計算成本」的最佳實踐路徑。

🔗 **來源**
- 標題：PolyAI Releases Dialog-RSN-1: An Audio-Native Dialog Model That Fuses Turn-Taking, Speech Recognition, Function Calling, And Response
- 作者／機構：Michal Sutter @ MarkTechPost
- 連結：https://www.marktechpost.com/2026/07/30/polyai-releases-dialog-rsn-1-an-audio-native-dialog-model-that-fuses-turn-taking-speech-recognition-function-calling-and-response/

#AI #MachineLearning #PolyAI #SpeechRecognition #LLM #AudioNative #ConversationalAI #NLP #DeepLearning #TechNews
