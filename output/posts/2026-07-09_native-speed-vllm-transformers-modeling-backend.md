---
title: Native-speed vLLM transformers modeling backend
source: HuggingFace Blog
url: https://huggingface.co/blog/native-speed-vllm-transformers-backend
score: 101
model: google/gemma-4-31b-it:free
generated_at: '2026-07-09T09:52:24.662307'
---

📌 【HuggingFace】vLLM transformers 後端效能追平，模型部署不再需要手動移植

TL;DR：vLLM 的 transformers 後端效能已追平或超越原生實作，模型作者可直接利用 transformers 程式碼實現極速推論。

以往要讓新模型在 vLLM 上跑出最高效能，模型作者通常得將 transformers 的實作重新移植（port）成 vLLM 的原生格式。這種重複開發不僅耗時，也增加了維護成本。

🤔 **模型實作的重複勞動問題**

transformers 函式庫已成為機器學習的參考標準，支援超過 450 種架構且 API 一致。雖然開發者常參考 transformers 的程式碼來將模型移植到 vLLM、SGLang 或 llama.cpp 等框架，但這種「手動移植」的過程對模型作者來說是一道門檻。

🧩 **結合 transformers 建模與 vLLM 推論最佳化**

為了簡化流程，vLLM 整合了 transformers 作為建模後端（modeling backend）。其運作邏輯如下：
- **transformers**：提供模型建模程式碼（Modeling code）。
- **vLLM**：提供極其最佳化的推論技術，包含 continuous batching 與自定義的 attention kernels。

這意味著模型作者無需進行任何移植，即可在 vLLM 中執行 LLM 或 VLM 模型。

📊 **跨規模模型測試：效能追平原生實作**

HuggingFace 將 transformers 建模後端與 vLLM 的手寫原生實作進行對比，測試物件為三款不同型別的 Qwen3 模型（皆在 8×H100 節點上測試）：
- 4B 稠密模型（單 GPU）
- 32B 稠密模型（使用 Tensor Parallelism）
- 235B 參數 FP8 混合專家模型（使用 Data + Expert Parallelism）

測試結果顯示，transformers 建模後端的吞吐量（throughput）在上述所有測試中，均達到或超越了原生實作的表現。

🎯 **實務啟示：單一參數即可啟動極速推論**

對於工程師而言，這意味著部署新模型的門檻大幅降低。只要更新 vLLM 套件並使用特定參數，即可直接執行 Hugging Face 模型而無需等待原生移植版本。

安裝與更新指令：
`uv pip install --upgrade vllm --torch-backend auto`

執行時只需加上 `--model` 相關 flag 即可透過 transformers 後端執行。

🔗 **來源**
- 標題：Native-speed vLLM transformers modeling backend
- 作者／機構：HuggingFace
- 連結：https://huggingface.co/blog/native-speed-vllm-transformers-backend

#vLLM #HuggingFace #LLM #Inference #Transformers #Qwen3 #ModelDeployment #MachineLearning #OpenSource #DeepLearning
