---
title: 'Meta is back with Muse Glimmer: local, agentic, multimodal, and open source'
source: HuggingFace Blog
url: https://huggingface.co/blog/muse-glimmer
model: tencent/hy3:free
generated_at: '2026-08-11T06:58:52.178900'
score: 113
---

📌 【Meta 重磅發佈】Muse Glimmer：專為本地端設計的開源多模態 Agent 模型

TL;DR：Meta 推出的 Muse Glimmer 是一款 30B 參數的多模態模型，專為本地端 Agent 應用優化，支援開源且具備強大的推理與程式碼能力。

Meta 再次展現其在開源社群的影響力，正式推出 Muse Glimmer。這是一款專為「本地端代理（Local Agentic）」情境設計的多模態模型，透過從 Muse 模型蒸餾（Distilled）而來，將參數規模控制在 30B，旨在平衡效能與部署成本，是開發隱私敏感型應用（如個人助理、程式碼編寫、文件分析）的理想選擇。

🧩 **架構設計：高效能的混合注意力與視覺編碼**

Muse Glimmer 採用 dense 30B 參數架構，由兩個核心部分組成：

* **2B ViT 式視覺編碼器 (Perception Encoder)**：這是一個規模相當大的視覺編碼器，能同時處理圖像與影片。對於影片，它會以每秒 2 幀的速度進行採樣，並透過時間戳記佔位符（timestamped video placeholders）將文字與影格交錯處理。
* **28B 文字解碼器 (Text Decoder)**：
    * **混合注意力機制 (Hybrid attention)**：採用「SWA → SWA → SWA → Full」的循環模式（Sliding Window Attention 與 Full Attention 交替），重複 13 次共 52 層。這讓模型既能利用 RoPE 掌握相對距離，也能透過 NoPE 保留全域資訊。
    * **Gated Grouped-Query Attention**：每 16 個 Query heads 共用一個 Key-Value head，將 KV-cache 記憶體消耗降低了 16 倍，大幅提升生成速度與降低成本。
    * **Q-K Normalization**：在計算注意力前對 Query 和 Key 進行 RMS 歸一化，並配合額外的 Query 縮放（extra query scaling），確保 Attention logits 的穩定性。

💡 **進階功能：專為程式碼優化的投機採樣**

為了加速生成，Muse Glimmer 實作了基於 DFlash 的「投機解碼草稿器（Speculative decoding drafter）」。雖然這會消耗額外的記憶體，但作者發現這對於需要生成結構化內容（如程式碼）的任務特別有效，能顯著提升生成速度。

📊 **多維度評測：在 Agentic 任務中表現卓越**

根據 HuggingFace 提供的基準測試數據，Muse Glimmer-30B 在多項代理（Agentic）與多模態任務中展現了強大的競爭力：

| 評測類別 | 基準測試 (Benchmark) | Muse Glimmer-30B | 競爭對手 (Gemma4/Qwen3.6) |
| :--- | :--- | :--- | :--- |
| **Agentic Coding** | SWE-Bench Pro | **51.2** | 36.9 / 50.2 |
| **Agentic Coding** | SWE-Bench Verified | **76.0** | 66.6 / 77.2 |
| **Agentic Coding** | TerminalBench | 2.1 | 51.7 / 43.4 |
| **Multimodal** | Charxiv Reasoning | **78.8** | 77.7 / 78.4 |
| **Multimodal** | ScreenSpot Pro | 75.4 | 75.9 / 76.1 |
| **Reasoning** | AIME 2026 | **94.7** | 89.2 / 94.1 |

*註：數據依據原文報告，加粗表示該項對比中的最佳結果。*

🎯 **實務啟示：開源社群的即時支援**

對於工程師而言，Muse Glimmer 的優勢在於極高的整合度。它在發佈首日（Day-0）便已支援 `transformers`、`llama.cpp`、`vLLM` 等主流函式庫。這意味著開發者可以立即將其部署於 NVIDIA (CUDA)、AMD (ROCm) 或 Intel (XPU) 硬體上，並利用 `AutoModelForMultimodalLM` 輕鬆實現文字與圖像的混合推理。

🔗 **來源**
- 標題：Meta is back with Muse Glimmer: local, agentic, multimodal, and open source
- 連結：https://huggingface.co/blog/muse-glimmer

#Meta #MuseGlimmer #Multimodal #OpenSource #AgenticAI #MachineLearning #LLM #ComputerVision #HuggingFace #AIEngineering
