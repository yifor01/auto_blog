---
title: cjpais/Handy
source: GitHub Trending
url: https://github.com/cjpais/Handy
score: 80
model: google/gemma-4-31b-it:free
generated_at: '2026-07-05T19:35:08.281761'
---

📌 **【開源工具】Handy：完全離線、隱私優先的跨平臺語音轉文字助手**

TL;DR：整合 Whisper 與 Silero VAD 的開源桌面應用，讓語音轉文字在本地完成並直接貼入任何文字欄位。

許多語音轉文字工具將資料傳送到雲端，這對重視隱私的開發者或對安全性有要求的使用者來說是巨大的隱憂。如果能讓轉寫過程完全留在本地，且能像快捷鍵一樣隨處可用，會如何？

🤔 **填補開源且可擴充的轉寫工具缺口**

Handy 的設計初衷並非追求成為「最強」的轉寫軟體，而是致力於成為「最容易被分叉（forkable）」的工具。它強調無須支付費用、完全開源且隱私至上，旨在將輔助工具交還給使用者，而非鎖在付費牆後。

🧩 **從語音到文字的本地處理流程**

Handy 提供簡單的「按下快捷鍵 $\rightarrow$ 說話 $\rightarrow$ 文字貼上」體驗，其技術實作流程如下：

1. **觸發錄音**：透過可配置的鍵盤快捷鍵啟動/停止錄音，或使用 Push-to-talk 模式。
2. **靜音過濾**：使用 Silero 的 VAD (Voice Activity Detection) 技術過濾掉無意義的靜音片段。
3. **本地轉寫**：利用本地模型將語音轉換為文字。
4. **直接輸出**：將轉寫後的文字直接貼入使用者目前正在使用的任何應用程式文字欄位中。

💡 **靈活的模型選擇與硬體加速**

為了在不同硬體環境下達到最佳效能，Handy 允許使用者根據需求選擇不同的轉寫模型：

- **Whisper 系列**：提供 Small、Medium、Turbo 及 Large 等多種模型，並在硬體支援時啟用 GPU 加速。
- **Parakeet V3**：針對 CPU 最佳化的模型，提供優異的效能表現。

🎯 **實務啟示**

對於需要處理敏感資料、不希望語音資料外流，或是希望在無網路環境下進行快速文字輸入的工程師來說，Handy 提供了一個輕量且可擴充的基礎。由於其高度可擴充的特性，開發者可以根據自己的特定需求對其進行修改或增加新功能。

🔗 **來源**
- 標題：cjpais/Handy
- 作者／機構：cjpais
- 連結：https://github.com/cjpais/Handy

#OpenSource #SpeechToText #Whisper #Privacy #OfflineAI #VAD #Silero #CrossPlatform #Accessibility #LocalLLM
