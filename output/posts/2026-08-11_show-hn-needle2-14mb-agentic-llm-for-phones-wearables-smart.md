---
title: 'Show HN: Needle2: 14MB agentic LLM for phones, wearables, smart home and robots'
source: Hacker News
url: https://cactuscompute.com/needle
model: tencent/hy3:free
generated_at: '2026-08-11T07:00:10.374908'
score: 109
---

📌 【Cactus 研究】僅 14MB 就能跑 Agentic LLM：專為邊緣裝置設計的 Needle 2

TL;DR：Needle 2 是僅 14MB 的輕量化 Agentic LLM，專為手機、穿戴式裝置與機器人設計，以極低功耗實現高效能工具調用。

當我們討論 Edge AI 時，往往將目光鎖定在 Mac 或 PC，但全球超過 210 億臺的 IoT 裝置中，絕大多數是預算有限的行動裝置、微控制器與小型機器人。這些裝置通常缺乏強大的 NPU 或 GPU，如何在資源極度受限的情況下實現智慧化的工具調用（Tool Call）與結構化提取（Structured Extraction）？Cactus 推出的 Needle 2 給出了答案。

🧩 **極致輕量化與高效能架構**

Needle 2 採用 Simple Attention Networks 架構（詳見作者研究論文），透過 2-bit 壓縮技術，將 45M 參數的模型縮減至單一 14MB 的二進位檔。

- **記憶體佔用**：執行完整 Session 僅需 28MB RAM。
- **推論速度**：
  - Raspberry Pi 5：500 tokens/sec。
  - VR 裝置（Meta Quest 3S / Apple Vision Pro）：400–1,500 tokens/sec。
  - 低階手機（如 Samsung A-Series）：300–700 tokens/sec。
- **效能對比**：在工具調用與行動裝置使用測試中，Needle 2 的表現與 LFM2.5 230M 及 Apple Foundation Model 旗鼓相當，但其參數規模僅為後者的 5 倍至 70 倍，且 Needle 2 使用 2-bit 壓縮，而對手皆為 f16。

💡 **將智慧轉換為函式調用**

Needle 2 的核心設計理念在於：將消費級裝置的智慧定義為「帶有類型參數的函式」。

當任務被框架化為「將雜亂的句子映射到特定函式與參數值」時，模型不再需要龐大的世界知識或開放式文本生成能力。這解釋了為何僅需 45M 參數，就能精準處理結構化提取。

- **結構化輸出**：除了工具調用，開發者可以傳入 Schema 來進行結構化提取（Structured Extraction），例如將模型當作文本分類器（使用 enum 欄位）或摘要模型。
- **能效比極高**：傳統 Transformer 在同等寬度下每 token 消耗 164 MFLOPs，即使是縮減後的模型仍需 87 MFLOPs；而 Needle 僅需 70 MFLOPs。在行動裝置上，這意味著每消耗 1 毫瓦時（milliwatt-hours）能換取更高的運算量，其能耗比最小的效能型 LLM 高出 7 倍至 85 倍。

⚠️ **混合架構：信心值與雲端協作**

為了兼顧準確度與成本，Needle 2 引入了 Cactus Hybrid 技術，模型會為每個回應計算一個「學習到的信心分數」（Learned Confidence Score）：
- **高於閾值**：直接執行動作。
- **低於閾值**：將任務升級（Escalate）至雲端或更大型的模型（如 DeepSeek-v4-Flash）處理。

🎯 **實務啟示**

對於開發者而言，Needle 2 提供了一種低成本的解決方案，透過 Python package 即可在 Mac/PC 上於數分鐘至數小時內完成 Fine-tuning。開發者只需提供少量範例，即可透過自動化資料生成管線（Automated Data-generation Pipeline），讓模型在特定產品的工具語彙（Tool Vocabulary）上達到前沿等級的表現。

🔗 **來源**
- 標題：Show HN: Needle2: 14MB agentic LLM for phones, wearables, smart home and robots
- 連結：https://cactuscompute.com/needle

#AI #LLM #EdgeAI #MachineLearning #AgenticAI #IoT #EmbeddedAI #TinyML #ComputerVision #SoftwareEngineering
