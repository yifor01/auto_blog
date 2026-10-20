---
title: 'DeepInfer: High-performance inference framework for DeepSeek models'
source: Hacker News
url: https://github.com/deepseek-ai/DeepInfer
model: claude-code/sonnet
generated_at: '2026-10-20T20:44:32.554713'
score: 117
---

📌 DeepSeek 開源自家生產推理引擎 DeepInfer

TL;DR：DeepSeek 把支撐自家大規模服務的推理框架開源，技術細節完整可直接復現。

一款在 Hacker News 上拿下 1991 點讚、778 則留言的開源專案，通常代表的不只是熱度，而是工程師真的在意「這東西能不能直接拿來用」。DeepInfer 正是這樣的專案：它不是一篇論文式的概念驗證，而是 DeepSeek 自家生產服務實際在跑的推理框架。

🤔 **為誰而做：想要大規模部署 DeepSeek 模型的工程師**

README 開頭就講得很直白：DeepInfer 是支撐 DeepSeek 大規模生產服務的高效能推理框架，這次開源release提供的是離線推理（offline inference），涵蓋服務大規模部署所需的核心能力。目前支援的模型是 DeepSeek-V4.1-Flash，預設checkpoint為 deepseek-ai/DeepSeek-V4.1-Flash-1017，首次執行會自動下載到 Hugging Face cache，也可透過環境變數指向本地路徑。

🧩 **核心架構：從 kernel 到排程全面客製化**

DeepInfer 的效能優化堆疊在幾個層次上：

- **Optimized kernels**：FlashMLA、DeepGEMM、DeepEP、TileKernels、DeepSelect，以及自製的 TileLang kernels。
- **Parallelism（平行化策略）**：Attention 採 DP（data parallel）/ balanced CP（context parallel），MoE 則用 EP（expert parallel）+ EPLB（expert parallel load balancing）。
- **DSpark 與信心排程驗證（confidence-scheduled verification）**：用草稿 token（draft tokens）加速解碼，再依信心估計排程驗證步驟，對應環境變數 DEEPINFER_ENABLE_MTP_VARLEN=1，DEEPINFER_USE_NEXTN_DECODE 控制最大草稿長度（預設 5）。
- **SWA（sliding window attention）bounded replay**：只重放有界的尾段內容來減少 decoder prefill 的運算量，V4.1 預設設定為 DEEPINFER_YOCO_PREFILL_TRUNCATION_MODE=compact、DEEPINFER_YOCO_PREFILL_KEEP_TOKENS=140，保留的尾段必須覆蓋 SWA 視窗加上最大回溯長度。
- **非同步排程（預設啟用）**：讓 CPU 的批次排程與裝置端執行重疊，達到零額外負擔的批次排程。
- **Batch-invariant inference 與 Deterministic sampling**：前者保證不同批次組合下模型結果一致（DEEPINFER_BATCH_INVARIANT=1，僅限 NVIDIA），後者則在固定 seq_seed 下對相同輸入 token 與取樣參數產生完全相同的輸出。
- **Structured outputs**：可透過 SamplingParams 傳入 so_args={"schema_type": ..., "schema": ...}，將生成結果限制在 regex、JSON schema 或 EBNF grammar 之內。

📊 **怎麼跑：環境與效能基準**

建置需求為 Linux、GCC 13 以上、Python 3.12，NVIDIA 平臺需 CUDA 13，Ascend 平臺需 CANN 9.2。流程是先建立乾淨的 Python 3.12 環境，設定 DEEPINFER_ACCELERATOR=nvidia（或 ascend），執行 ./build.sh，再用 python examples/offline_inference.py 跑離線推理。效能基準方面，README 說明 prefill 是在 4 張 SM100 GPU 上量測，decode 則用 64 張，皆在單一 scale-up domain 內完成，並提供 run_sweep.sh 供復現。

⚠️ **這不是完整的服務堆疊**

README 明確列出這次開源「不包含」的部分：KV cache 系統、VE/Prefill/Decode 的完整服務化分離（雖然大部分引擎功能已實作）、以及跨 data-parallel replica 的 prefill 與 decode 負載平衡。換言之，DeepInfer 提供的是推理引擎本體，要搭出一個完整的生產服務，仍需自行補上周邊的服務化元件。硬體支援目前也限定在 NVIDIA SM100 GPU 與華為 Ascend 950 NPU。

🎯 **實務啟示**

對於正在評估自建推理服務的團隊，DeepInfer 的價值在於它把 DeepSeek 自家生產環境驗證過的優化手法（MoE 平行化、推測解碼、批次不變性等）用環境變數的形式直接開放出來，省去從零摸索的過程。但要注意它站在 vLLM 的基礎上建構，並參考了 SGLang、TensorRT-LLM 的設計，若團隊既有堆疊已深度整合其中一方，整合成本需要納入評估。

🔗 **來源**
- 標題：DeepInfer: High-performance inference framework for DeepSeek models
- 作者／機構：DeepSeek-AI（Hacker News 貼文者：ggcr）
- 連結：https://github.com/deepseek-ai/DeepInfer

#DeepSeek #DeepInfer #LLMInference #OpenSource #MoE #GPUOptimization #vLLM #StructuredOutputs #InferenceEngine #AIInfrastructure
