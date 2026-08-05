---
title: Deploy local agents everywhere with LFM2.5-2.6B
source: HuggingFace Blog
url: https://huggingface.co/blog/LiquidAI/lfm2-5-2-6b
model: tencent/hy3:free
generated_at: '2026-08-05T08:36:27.870846'
score: 102
---

📌 【LiquidAI 新作】LFM2.5-2.6B 登場：在手機與筆電上，跑出媲美 4 倍大模型的 Agent 能力

TL;DR：LFM2.5-2.6B 專為邊緣設備設計，在指令遵循與工具使用上可與大 4 倍的模型競爭。

當開發者追求 AI 代理（Agent）的反應速度與資料隱私時，雲端推論的延遲與成本往往是最大的阻礙。LiquidAI 推出的 LFM2.5-2.6B 旨在打破這個僵局，讓具備工具調用（tool calling）與多步工作流（multi-step workflows）能力的代理，能直接在筆電甚至手機等個人裝置上運行。

🧩 **四階段訓練流程：打造可靠的邊緣端代理**

LFM2.5-2.6B 的核心競爭力來自於其精密的後訓練（post-training）流程，將基座模型轉化為強大的代理模型：

1. **監督式微調 (SFT)**：進行兩輪 SFT，重點強化工具使用、網路搜尋與任務軌跡（trajectories）等代理相關數據。
2. **教師專門化 (Teacher Specialization)**：針對數學、程式碼、工具使用等不同領域，各訓練一位專家級的教師模型。
3. **多領域在策略蒸餾 (MOPD)**：將這些專家教師的能力，蒸餾到單一的學生模型中。
4. **代理強化學習 (Agentic RL)**：在真實的代理框架中進行多輪強化學習，讓模型學習如何在不同的工具、系統提示詞（system prompts）與多輪任務環境中協作。

💡 **效能驚人：小體積卻能挑戰 4 倍大的對手**

LFM2.5-2.6B 雖然參數僅 2.6B，但在多項關鍵指標上展現了極高的效率，甚至在某些測試中超越了參數規模大其 4 倍的模型：

📊 **關鍵基準測試表現**

| 測試項目 | LFM2.5-2.6B (2.6B) | Gemma-4-E2B-it (5.1B) | Qwen3.5-9B (9.7B) |
| :--- | :--- | :--- | :--- |
| **指令遵循 (IFBench)** | 59.17 | 34.08 | 56.47 |
| **工具使用 (ToolSandbox)** | 77.83 | 52.40 | 76.44 |
| **數學能力 (AIME25)** | 51.87 | 26.33 | 56.07 |

*註：LFM2.5-2.6B 在指令遵循與工具使用方面表現卓越，僅在 BFCLv4 與編寫程式碼（Coding）領域略遜於超大型模型。*

🚀 **極速推論：裝置端運行的最佳解**

得益於 LFM2 架構，該模型在各種硬體上皆有極佳的表現，且記憶體佔用低於 2.5 GB：

- **Apple M5 Max**：解碼速度達 220 tokens/s。
- **AMD Ryzen CPU**：解碼速度達 113 tokens/s。
- **行動裝置**：在 30 tokens/s 的速度下，仍能運行具備能力的代理。
- **高併發 GPU**：在單張 H100 上，高併發情況下每秒可輸出近 15K tokens。

🎯 **實務啟示**

如果你正在開發需要高頻率執行、且對隱私敏感的應用程式（例如個人助理、本地文件處理、自動化工作流），LFM2.5-2.6B 提供了一個極具成本效益的選擇。它讓開發者無需支付昂貴的雲端推論費用，就能在使用者裝置上直接部署強大的 Agent。

🔗 **來源**
- 標題：Deploy local agents everywhere with LFM2.5-2.6B
- 作者／機構：LiquidAI @ HuggingFace
- 連結：https://huggingface.co/blog/LiquidAI/lfm2-5-2-6b

#AI #Agent #LiquidAI #EdgeAI #OnDeviceAI #MachineLearning #LLM #HuggingFace #LocalAI #ReinforcementLearning
