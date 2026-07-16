---
title: vllm-project/vllm
source: GitHub Trending
url: https://github.com/vllm-project/vllm
score: 108
model: tencent/hy3:free
generated_at: '2026-07-16T08:09:38.607482'
---

📌 【vLLM】高吞吐 LLM 推論與服務的開源利器

TL;DR：vLLM 提供高效能 LLM 推論與服務，支援多種量化與排程技術，易於整合。

你家的 LLM 推論服務是不是卡在吞吐量上？一個由 UC Berkeley 實驗室發源、現有超過 2000 位貢獻者的開源專案，正試圖讓每個人都能輕鬆、快速且便宜地部署大語言模型。

🤔 **從伯克利實驗室到全球開源社群**

vLLM 最初在 UC Berkeley 的 Sky Computing Lab 開發，如今已成長為活躍的開源 AI 專案，由來自 200 多個學術機構與公司的數十個單位、超過 2000 名貢獻者共同維護。專案定位為「快速且易用的 LLM 推論（inference）與服務（serving）函式庫」。

🧩 **靠 PagedAttention 與連續批次擠出吞吐量的設計**

README 指出，vLLM 在「快」這件事上靠以下機制：

- 使用 PagedAttention 有效率地管理 attention 的 key 與 value 記憶體
- 連續批次（continuous batching）處理進來的請求，並支援 chunked prefill 與 prefix caching
- 透過 piecewise 與完整 CUDA/HIP graph 達成快速且靈活的模型執行
- 最佳化的 attention kernel 包含 FlashAttention、FlashInfer、TRTLLM-GEN、FlashMLA、Triton
- 各種精度的 GEMM/MoE kernel 使用 CUTLASS、TRTLLM-GEN、CuTeDSL 最佳化
- 推測解碼（speculative decoding）支援 n-gram、suffix、EAGLE、DFlash
- 用 torch.compile 做自動 kernel 生成與圖級轉換
- 支援 disaggregated prefill、decode、encode

在量化（quantization）方面，vLLM 支援 FP8、MXFP8/MXFP4、NVFP4、INT8、INT4、GPTQ/AWQ、GGUF、compressed-tensors、ModelOpt、TorchAO 等多種格式。

⚙️ **無縫接軌 Hugging Face，降低匯入門檻**

除了效能，vLLM 強調靈活與易用：可與熱門的 Hugging Face 模型無縫整合，並提供高吞吐量的多樣服務能力（README 於此處截斷，細節未完整列出）。專案也建置了官方網站 vllm.ai 與活動頁面，協助使用者上手。

🎯 **實務啟示**

對於需要自建 LLM 服務的團隊，vLLM 是值得評估的開源選項：它把 PagedAttention、連續批次、多種量化與推測解碼打包成一套函式庫，且能直接吃 Hugging Face 模型。在匯入前，建議依自身 GPU 架構與精度需求，確認所列 kernel 與量化格式是否吻合。

🔗 **來源**
- 標題：vllm-project/vllm
- 作者／機構：vllm-project
- 連結：https://github.com/vllm-project/vllm

#vLLM #LLM #inference #serving #PagedAttention #quantization #open-source #HuggingFace #throughput #GPU
