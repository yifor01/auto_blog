---
title: 'Show HN: Run an 80B Qwen in 4.3 GB of RAM on a Mac, and a 35B on an iPhone'
source: Hacker News
url: https://github.com/leonickson1/Swiftlet
model: tencent/hy3:free
generated_at: '2026-08-04T08:30:47.114475'
score: 97
---

📌 【Swiftlet 開源專案】在 iPhone 上跑 35B 模型！透過專家流式傳輸實現超低記憶體佔用

TL;DR：Swiftlet 透過「專家流式傳輸」技術，讓 80B 規模模型僅需 4.3 GB RAM 即可在 Mac 執行。

隨著大型語言模型（LLM）規模不斷擴張，如何在行動裝置或記憶體有限的電腦上執行高參數模型，一直是工程師的挑戰。Swiftlet 透過創新的架構設計，讓 35B 規模的模型能在 iPhone 上以約 2.5 GB 的記憶體佔用順暢運作，實現了同等級模型在手機端原生運行的紀錄。

🤔 **解決記憶體與模型規模的矛盾**

傳統的大型模型需要將所有參數載入記憶體（RAM），這對行動裝置來說是不可能的任務。Swiftlet 針對 Qwen3 系列的混合架構（MoE, Mixture-of-Experts）進行了優化，核心策略是：**「只將模型中極小的密集核心（Dense Core）保留在記憶體中，並根據需求從儲存裝置即時串流（Stream）路由到的專家權重（Routed Experts）。」**

🧩 **核心技術：專家流式傳輸與混合架構**

Swiftlet 的設計精髓在於它如何處理 MoE 架構中的專家權重：

*   **記憶體中常駐權重**：僅保留 Attention、DeltaNet 投影、Router、共享專家（Shared Experts）與 Embedding 等核心層，這部分在 4-bit 量化下僅需約 1.3 GB (35B) 到 2.5 GB (80B)。
*   **專家權重串流（Expert Streaming）**：將成千上萬個專家權重打包成固定間隔（Fixed-stride）的 `.qpack` 容器。當模型需要特定專家時，直接透過 `pread` 從 SSD 讀取，避免了使用 `mmap` 可能導致的 page-cache 抖動（thrash）。
*   **高效緩存機制**：使用 LFU（Least Frequently Used）結合近期性（Recency）的機制，將熱門專家緩存在受限的池（Bounded Pool）中。
*   **線性注意力（Linear Attention）**：75% 的層使用 Gated DeltaNet 線性注意力，具有固定大小的遞歸狀態（Recurrent State），這意味著無論 Context 長度多長，都不會像傳統 Transformer 那樣導致 KV Cache 持續膨脹。

📊 **效能表現：低記憶體佔用，高參數質感**

雖然模型規模巨大，但由於每顆 Token 僅會激活約 3B 的參數，因此其表現具備「大模型的對話品質」與「小模型的反應速度」雙重特性。

| 模型類型 | 參數規模 | 磁碟佔用 | 峰值 RAM (M5 Mac) | 推論速度 (M5 Mac) |
| :--- | :--- | :--- | :--- | :--- |
| Qwen3.6-35B-A3B | 35B (4-bit) | 18 GB | 2.6 GB | 7 ~ 11 tok/s |
| Qwen3-Next-80B-A3B | 80B (4-bit) | 42 GB | 4.3 GB | 4.5 ~ 5 tok/s |

*註：35B 模型在 iPhone 17 上僅需約 2.5 GB RAM，速度約為 1 tok/s。*

💡 **深入分析：為什麼這對工程師很重要？**

Swiftlet 的成功在於它證明了「專家流式傳輸」在行動裝置上的可行性。它不僅僅是簡單的權重切分，還包含了一套完整的工程實踐：
1.  **Runtime-compiled Shaders**：在執行時編譯 Metal Shader，確保 iOS 與 macOS 程式碼的一致性。
2.  **驗證機制**：開發者對每一層的 Forward Pass（包含 Gated DeltaNet、Sparse MoE 等）都進行了與 `mlx-lm` 參考實作的逐層比對，確保量化後的精確度。
3.  **開發靈活性**：Swiftlet 提供 Swift Package 供 App 開發者整合，也提供 OpenAI 相容的伺服器模式，讓開發者可以輕鬆將本地模型整合進現有的 UI 介面中。

⚠️ **限制與注意事項**

*   **效能瓶頸**：目前的效能瓶頸在於 Decode 迴圈的 Dispatch Bound（派遣受限），而非 IO 受限，這表示未來仍有提升空間。
*   **硬體要求**：需要 Apple Silicon 晶片，macOS 14+ 或 iOS 17+。
*   **儲存空間**：雖然 RAM 佔用低，但仍需預留大量 SSD 空間來存放權重容器（35B 需 18 GB，80B 需 42 GB）。

🎯 **實務啟示**

如果你正在開發需要本地 AI 能力的應用程式（如 Priv AI），Swiftlet 提供的 `SwiftletCore` 提供了一套完整的解決方案，包括對話快取（Conversation Caching）、重複控制（Repetition Control）以及針對 iOS 的記憶體壓力協調（Memory-pressure coordination），這比從零開始處理 Metal 核心更具開發效率。

🔗 **來源**
- 標題：Show HN: Run an 80B Qwen in 4.3 GB of RAM on a Mac, and a 35B on an iPhone
- 作者／機構：leonickson
- 連結：https://github.com/leonickson1/Swiftlet

#AI #MachineLearning #LLM #Qwen #Metal #Swift #AppleSilicon #MoE #OnDeviceAI #EdgeAI #OpenSource
