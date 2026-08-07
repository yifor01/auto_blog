---
title: 'Inside vLLM: Anatomy of a High-Throughput LLM Inference System (2025)'
source: Hacker News
url: https://www.aleksagordic.com/blog/vllm
model: tencent/hy3:free
generated_at: '2026-08-07T07:49:08.668900'
score: 82
---

📌 【深度解析】拆解 vLLM 架構：高吞吐量 LLM 推論系統的核心設計

TL;DR：深入剖析 vLLM 如何透過 PagedAttention 與 Continuous Batching 實現高效能推論。

在 LLM 推論領域，vLLM 已成為實現高吞吐量（High-throughput）的關鍵技術。然而，這個系統內部究竟是如何運作，從 Request 的進入到最終 Output 的產出，中間經歷了哪些複雜的調度與記憶體管理？

🎣 **從離線執行到線上服務的演進**

雖然我們常使用 vLLM 來提供 Web 服務，但其最基礎的構建塊是「LLM Engine」。在最簡單的離線（Offline）設定下，它能處理一組固定的 Prompts，並在單一 GPU 上以同步方式執行。然而，現代推論系統需要的是「非同步（Async）」且「多 GPU」的線上服務能力，這正是 vLLM 複雜架構發揮作用的地方。

🧩 **LLM Engine 的核心組成元件**

一個完整的 vLLM Engine 由以下幾個關鍵部分組成：

*   **vLLM Config**：包含模型設定、快取（Cache）與並行（Parallelism）等所有參數的控制開關。
*   **Processor**：將原始輸入（如 Text）轉換為 EngineCoreRequest，包含驗證與 Tokenization（斷詞）流程。
*   **Engine Core Client**：負責與核心引擎溝通，從單機的 InprocClient 演進到可擴展的 DPLBAsyncMPClient。
*   **Output Processor**：將引擎輸出的原始資料轉換為使用者可讀的 RequestOutput。

🤔 **Engine Core 的內部運作機制**

引擎核心（Engine Core）是系統的大腦，其內部包含三個關鍵子系統：

1.  **Model Executor**：驅動模型的 Forward Pass（前向傳播）。
2.  **Structured Output Manager**：負責 Guided Decoding（引導式解碼）。
3.  **Scheduler（調度器）**：決定哪些請求進入下一個執行步驟。
    *   **策略設定**：支援 FCFS（先來先服務）或 Priority（優先級）策略。
    *   **隊列管理**：包含 Waiting Queue（等待隊列）與 Running Queue（執行隊列）。
    *   **KV Cache Manager**：這是 **PagedAttention** 的核心，維護著一個龐大的 `free_block_queue`（可用快取塊池），透過索引結構將 Token 映射到計算好的 KV Cache 區塊。

📊 **KV Cache 的計算與記憶體配置**

對於標準的 Transformer 層，一個 Block 的大小計算公式如下：
`2 (key/value) * block_size (預設 16) * num_kv_heads * head_size * dtype_num_bytes`

在初始化 Worker 時，系統會執行以下關鍵步驟：
*   **分配 VRAM**：根據 `gpu_memory_utilization`（例如 0.8，即 80%）檢查可用顯存。
*   **初始化 Model Runner**：持有 Sampler、KV Cache 以及 InputBatch（包含 CPU 端的 Forward-pass 緩衝區與 Block Tables）。
*   **CUDA Graphs 捕捉**：若未指定 `--enforce-eager`，系統會對 Warmup Batch 進行 Dummy Run 並捕捉 CUDA Graphs，透過重放（Replay）預先編譯好的圖形來減少 Kernel Launch 的開銷，提升延遲（Latency）表現。

💡 **從 Request 到生成的生命週期**

當一個 Prompt 進入系統後，流程如下：
1.  **封裝**：建立唯一 Request ID，進行 Tokenization 並包裝成 EngineCoreRequest。
2.  **排隊**：請求被標記為 `WAITING` 並加入 Scheduler 的等待隊列。
3.  **執行**：引擎不斷呼叫 `step()` 函式。
4.  **連續批處理 (Continuous Batching)**：在非同步引擎中，系統在每一步都會同時考慮新舊請求，利用自定義 Kernel 高效處理扁平化後的 Batch。

⚠️ **技術限制與版本說明**

*   本分析基於 2025 年 8 月的 Commit (42172ad) 進行。
*   隨著 V0 引擎被棄用（Deprecated），具體的類別名稱（Class names）與細節可能會隨版本更迭而改變，但核心設計理念（如 PagedAttention）仍具參考價值。

🎯 **實務啟示**

對於需要優化推論效能的工程師來說，理解 vLLM 的架構有助於掌握兩大關鍵：**記憶體管理（KV Cache）**與**調度策略（Scheduling）**。如果你追求極致的延遲，關注 CUDA Graphs 的應用；如果你追求吞吐量，則需深入研究 PagedAttention 如何減少記憶體碎片化。

🔗 **來源**
- 標題：Inside vLLM: Anatomy of a High-Throughput LLM Inference System (2025)
- 連結：https://www.aleksagordic.com/blog/vllm

#vLLM #LLM #Inference #MachineLearning #DeepLearning #PagedAttention #ContinuousBatching #GPU #MachineLearningEngineering #AIInfrastructure
