---
title: OpenBMB/VoxCPM
source: GitHub Trending
url: https://github.com/OpenBMB/VoxCPM
score: 108
model: google/gemma-4-31b-it:free
generated_at: '2026-06-16T21:08:30.617056'
---

📌 【OpenBMB 最新研究】擺脫 Tokenizer 限制，VoxCPM2 實現 48kHz 高保真多國語言語音合成

當前大多數的 TTS (文字轉語音) 系統通常依賴將音訊離散化為 Token，但這種做法往往在捕捉語音的細膩情感與自然度時產生損失。OpenBMB 團隊提出的 VoxCPM2 採取了完全不同的路徑：捨棄 Tokenizer，直接生成連續的語音表示。

🤔 **為什麼「Tokenizer-Free」對語音合成至關重要？**

傳統的離散化 Token 過程就像是將連續的波形「量化」成碎片，雖然方便模型處理，但卻容易導致合成語音缺乏靈魂，聽起來有機械感。VoxCPM2 透過端到端的擴散自回歸架構 (Diffusion Autoregressive Architecture)，直接生成連續的語音表示，從根本上解決了資訊流失的問題，讓合成出的聲音更具表現力且更接近真人。

🧪 **基於 MiniCPM-4 骨幹與 200 萬小時數據訓練**

VoxCPM2 並非從零開始的小實驗，而是一個擁有 20 億 (2B) 參數的大模型。其核心設計亮點包括：
- **強大骨幹**：建立在 MiniCPM-4 的基礎之上。
- **海量訓練**：使用了超過 200 萬小時的多國語言語音數據進行訓練。
- **高頻輸出**：支援 48kHz 的錄音室等級音質輸出，即使輸入參考音訊僅為 16kHz，也能直接提升至高保真品質。

🚀 **從「描述創造」到「極致克隆」的三種合成模式**

VoxCPM2 提供了極高的控制靈活性，將語音合成分為三個層次：

1. **Voice Design (語音設計)**：無需任何參考音訊，僅透過自然語言描述（如：年齡、性別、語調、情緒、語速）即可從無到有創造一個全新的聲音。
2. **Controllable Cloning (可控克隆)**：提供短暫的參考片段即可克隆音色，且可額外加入風格指導來調整情緒與表現力，同時保持原有的音色特徵。
3. **Ultimate Cloning (極致克隆)**：同時提供參考音訊及其對應文本，模型能無縫接續參考片段，精準還原音色、節奏、情緒與風格的所有細節。

🌍 **30 種語言原生支持，無需標記**

與許多需要指定語言標籤 (Language Tag) 的系統不同，VoxCPM2 支援 30 種語言的直接合成，模型能自動處理輸入文本，大幅降低了多國語言部署的複雜度。

⚠️ **開源模型與實作細節待進一步探索**

雖然 VoxCPM2 在音質與靈活性上有顯著突破，但作為一個 2B 參數的模型，其在端側設備的推理延遲 (Latency) 以及在極端雜訊環境下的克隆穩定性，仍需要開發者在實際部署中進一步驗證。

🎯 **對於 AI 工程師：TTS 進入「連續生成」時代**

VoxCPM2 的出現證明了「Tokenizer-Free」路徑在高品質語音合成上的潛力。對於開發者而言，這提供了一個強大的開源基底，可用於構建更具情感表現力的 AI 助手、虛擬主播或高品質的內容創作工具。如果你在尋找比傳統 TTS 更自然、且具備高控制力的方案，這是一個非常值得嘗試的方向。

🔗 **專案連結**
📝 VoxCPM: Tokenizer-Free TTS for Multilingual Speech Generation
👤 OpenBMB
🔗 GitHub: https://github.com/OpenBMB/VoxCPM

你認為「描述生成聲音」會取代傳統的採樣錄音嗎？歡迎在下方分享你的看法 👇

#AI #TTS #OpenBMB #VoxCPM #SpeechSynthesis #MachineLearning #開源模型 #語音合成
