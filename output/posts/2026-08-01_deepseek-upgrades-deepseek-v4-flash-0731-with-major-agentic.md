---
title: DeepSeek Upgrades DeepSeek-V4-Flash-0731 with Major Agentic and Coding Gains
source: MarkTechPost
url: https://www.marktechpost.com/2026/07/31/deepseek-upgrades-deepseek-v4-flash-0731-with-major-agentic-and-coding-gains/
model: tencent/hy3:free
generated_at: '2026-08-01T08:14:46.678933'
score: 81
---

📌 【DeepSeek 更新】V4-Flash-0731 正式版發布：透過重新訓練強化 Agent 與程式碼能力

TL;DR：DeepSeek-V4-Flash-0731 透過重新訓練（re-post-training）提升 Agent 與程式碼效能，並推出具備 DSpark 推測解碼能力的正式版本。

DeepSeek 於 2026 年 7 月 31 日正式發布了 DeepSeek-V4-Flash-0731，這是一個取代先前預覽版的正式版本。值得注意的是，這次的效能提升並非源於架構設計的改變，而是透過重新訓練（re-post-training）來實現。

🧩 **架構設計與技術細節**

根據 DeepSeek 技術報告，V4-Flash 採用 MoE（Mixture-of-Experts）架構，具備 284B 參數，每次 token 僅啟動 13B 參數。

- **MoE 結構**：每個 MoE 層包含 1 個共享專家與 256 個路由專家，中間維度為 2048，每次 token 會觸發 6 個路由專家。前三層 MoE 使用 hash routing。
- **Attention 機制**：採用混合注意力機制，結合了壓縮稀疏注意力（Compressed Sparse Attention, CSA）與高度壓縮注意力（Heavily Compressed Attention, HCA）。
- **連接方式**：使用流形約束超連接（Manifold-Constrained Hyper-Connections, mHC）取代傳統的殘差連接（residual connections），其擴展因子為 4，並包含 20 次 Sinkhorn-Knopp 迭代。
- **訓練設定**：預訓練使用超過 32T tokens，並採用 Muon 優化器。

📊 **DSpark 推測解碼帶來生成加速**

此版本在 Hugging Face 上的模型權重包含 DSpark 推測解碼模組（與 DeepSeek-V4-Flash-DSpark 結構一致），總參數達到 304B。

- **效能提升**：根據 DSpark 論文，在總體吞吐量相同的情況下，V4-Flash 的每用戶生成速度比 MTP-1 基準線快 60–85%。
- **部署方式**：使用 vLLM 時，只需透過 flag `--speculative-config '{"method":"dspark","num_speculative_tokens":7,"draft_sample_method":"greedy"}'` 即可啟用。

💰 **極具競爭力的 API 定價與部署建議**

DeepSeek 為 V4-Flash 提供了極具吸引力的價格，這對於需要執行大量 Agent 迴圈（agent loops）的開發者非常友善。

- **API 定價**：
  - 輸入（Cache Miss）：$0.14 / 1M tokens
  - 輸入（Cache Hit）：$0.0028 / 1M tokens
  - 輸出：$0.28 / 1M tokens
  - *註：輸出價格僅約 V4-Pro ($0.87) 的三分之一。*
- **部署限制**：API 提供 2,500 的並發限制（concurrency limit）。
- **自架構（Self-hosting）**：權重採用 MIT 授權且無限制。雖然每次僅啟動 13B，但所有專家仍需駐留在記憶體中。
  - 單機部署範例：使用 vLLM 可以在單臺 4×GB300 節點上運行。
  - 量化版本：Unsloth 的 8-bit 版本需 162 GB，3-bit 版本需 103 GB（需約 110 GB 組合 RAM 與 VRAM）。

💡 **開發者實務建議**

針對 Agentic（代理式）應用場景，DeepSeek 建議設定 `temperature = 1.0` 與 `top_p = 0.95`；其餘場景則建議 `top_p = 1.0`。此外，API 已原生支援 Responses API 格式並針對 Codex 進行了調整，且 `reasoning_effort` 參數可設定為 low、high 或 max（在 high 與 max 模式下，輸出 token 最高可達 384K）。

⚠️ **限制**

- 此更新僅針對 V4-Flash 版本，V4-Pro API 以及 App 與 Web 端模型並未進行更新。
- 目前模型未提供 Jinja chat template，需使用官方提供的 `encoding/` 資料夾中的函式進行訊息處理。

🔗 **來源**
- 標題：DeepSeek Upgrades DeepSeek-V4-Flash-0731 with Major Agentic and Coding Gains
- 作者／機構：Asif Razzaq @ MarkTechPost
- 連結：https://www.marktechpost.com/2026/07/31/deepseek-upgrades-deepseek-v4-flash-0731-with-major-agentic-and-coding-gains/

#DeepSeek #V4Flash #LLM #MoE #DSpark #MachineLearning #AI #Coding #AgenticAI #GenerativeAI
