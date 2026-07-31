---
title: '[AINews] GPT 5.6 price cut by 20%-80%: Cost of GPT 5.4 Intelligence dropped
  13x in 4 months due to GPT 5.6 recursive self-optimization'
source: Latent Space
url: https://www.latent.space/p/ainews-gpt-56-price-cut-by-20-80
model: tencent/hy3:free
generated_at: '2026-07-31T08:48:24.372621'
score: 73
---

📌 【AINews】GPT 5.6 成本大幅下降 20%-80%：透過遞迴自我優化，實現智慧成本驟降

TL;DR：OpenAI 透過 GPT 5.6 進行自我優化，讓相同智慧水準的成本在 4 個月內降至 1/13。

隨著模型能力持續進化，一個令人驚訝的趨勢正在發生：在模型智慧水準（LMSys Elo）保持不變的情況下，模型成本正在呈斷崖式下跌。

🤔 **智慧成本正持續大幅下降**

一年前的研究觀察到，在 18 個月內，GPT-4 等級的智慧成本曾下降了 1000 倍。當時業界尚不確定這是否僅是從「未優化」到「已優化」（例如從 Dense 轉向 MoE 架構）的初步紅利。然而，根據 OpenAI 的最新發現，即使是在智慧水準保持恆定的情況下，成本仍持續大幅度降低。

🧩 **GPT 5.6 透過遞迴自我優化降低成本**

OpenAI 揭露了 GPT 5.6 如何透過系統性升級來優化其服務流程，目標是在不犧牲品質的前提下，於相同硬體上處理更多 token：

*   **自主核心優化 (Self-Optimization)**：利用 GPT-5.6 Sol 分析生產環境流量、調整負載平衡，並自主改寫 OpenAI 內部的 Triton 與 Gluon 語言生產核心 (kernels)。此舉讓端到端 (end-to-end) 的服務成本降低了 20%。
*   **投機解碼 (Speculative Decoding)**：透過對模型架構進行數百次實驗（測試規模、結構與特徵變化），並在訓練過程中自主介入處理硬體故障或訓練不穩定等問題，成功設計出更佳的草稿模型 (draft model)，將 token 生成效率提升超過 15%。
*   **KV 快取 (KV Caching) 優化**：針對不同工作負載（主要是 Codex 中的 Sol）優化批次處理 (batching)、分片 (sharding) 與快取管理，從現有硬體中榨取更多推論效能。
*   **編排層優化**：為了簡化 Codex 與 ChatGPT Work 等工具中的複雜多步驟任務，OpenAI 優化了其 Rust 編排層 (orchestration layer)，以減少重複性的運算成本。

⚠️ **避免上下文膨脹與重複運算**

除了底層架構，OpenAI 在應用層也採取了策略來控制成本：
*   **延遲發現 (Deferred Discovery)**：工具、技能與外掛僅在需要時才會顯示，避免上下文膨脹。
*   **限制輸出**：工具輸出預設上限為 10,000 tokens，以防止上下文視窗不必要地擴張。
*   **提示詞快取 (Prompt Caching)**：避免重複處理相同的指令與歷史紀錄。

🎯 **實務啟示**

模型成本的下降不再僅依賴硬體進步，更依賴於「用 AI 優化 AI」的遞迴過程。對於工程師而言，理解模型如何透過自主優化來降低成本，對於預估未來大規模部署的運算成本具有重要的參考價值。

🔗 **來源**
- 標題：GPT 5.6 price cut by 20%-80%: Cost of GPT 5.4 Intelligence dropped 13x in 4 months due to GPT 5.6 recursive self-optimization
- 作者／機構：Latent Space
- 連結：https://www.latent.space/p/ainews-gpt-56-price-cut-by-20-80

#AI #OpenAI #GPT5 #MachineLearning #LLM #SpeculativeDecoding #SelfOptimization #SoftwareEngineering #InferenceOptimization #TechNews
