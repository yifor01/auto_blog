---
title: "DeepSeek AI Releases DeepSeek-V4: Compressed Sparse Attention and Heavily Compressed Attention Enable One-Million-Token Contexts"
source: MarkTechPost
url: https://www.marktechpost.com/2026/04/24/deepseek-ai-releases-deepseek-v4-compressed-sparse-attention-and-heavily-compressed-attention-enable-one-million-token-contexts/
score: 107
model: tencent/hy3-preview:free
generated_at: 2026-04-25T19:03:15.601002
---

📌 **DeepSeek-V4 開源：百萬 Token 上下文的實惠解方**

標準 Transformer 跑百萬 Token 上下文，顯存與延遲往往讓人望而卻步。DeepSeek 最新發布的 V4 系列，試圖用架構創新打破這個僵局，而且模型權重已經直接開源。

🤔 **百萬 Token 不再是天價，但架構得大改**

大型語言模型（LLM）處理長上下文時，最頭痛的莫過於傳統注意力機制的 O(n²) 複雜度。當上下文長度來到一百萬，運算量與顯存需求會呈指數級飆升，導致推理成本變得難以負擔。DeepSeek-V4 的核心目標，就是在不犧牲性能的前提下，讓百萬 Token 的推理變得「實惠且可行」。

🧪 **1.6T 參數 Pro 版與 284B Flash 版的 MoE 架構**

DeepSeek-V4 系列包含兩款 Mixture-of-Experts (MoE) 模型：
*   **DeepSeek-V4-Pro**：總參數 1.6T，每個 Token 激活 49B，預訓練數據量達 33T tokens。
*   **DeepSeek-V4-Flash**：總參數 284B，每個 Token 激活 13B，預訓練數據量為 32T tokens。

兩者均原生支援 100 萬 Token 的上下文窗口。目前，包含 Base 版本在內的四個變體權重均已公開於 Hugging Face。

 **CSA 與 HCA：混合注意力機制是核心突破**

為了解決長上下文的效率問題，DeepSeek-V4 放棄了 vanilla attention，改採四項協同創新：混合注意力架構、新型殘差連接、優化器升級以及 FP4 量化感知訓練（QAT）。

最核心的亮點是 **Compressed Sparse Attention (CSA)** 與 **Heavily Compressed Attention (HCA)** 的混合架構：
*   **CSA**：利用可學習的壓縮器，將每 m 個 Token 的 KV Cache 壓縮為單一 Entry，再透過 **Lightning Indexer** 進行稀疏選擇（DSA），讓 Query 只關注最重要的壓縮 KV。
*   **HCA**：更為激進，將 m′ (m′ ≫ m) 個 Token 的 KV 合併為一個壓縮 Entry，進一步降低長距離依賴的計算負擔。
*   **局部依賴**：兩者皆保留了滑動窗口分支（Sliding Window），確保對最近 n win 個 Token 的局部建模能力。

💡 **不只是壓縮，還有 FP4 與優化器的協同**

除了注意力機制的革新，DeepSeek-V4 還透過 FP4 量化感知訓練大幅降低了推理解碼時的顯存佔用。搭配重新設計的殘差連接與優化器，這套組合拳旨在解決單一技術無法處理的百萬 Token 級別的系統性瓶頸。

⚠️ **實測數據與極限場景的細節尚待觀察**

目前公開的是 Preview 版本與模型權重。雖然架構設計看起來能大幅降低計算複雜度，但具體在真實業務場景下的吞吐量（Throughput）、延遲（Latency）以及長度超過一定閾值後的資訊保留率，仍需等待社群的進一步基準測試（Benchmark）回報。

🎯 **GenAI 工程師的新玩具，長上下文部署門檻降低**

對於需要處理超長文檔（如法律合同、程式碼庫分析）的開發者來說，DeepSeek-V4 提供了一個開源且具備商業可行性的選項。特別是 Flash 版本，在激活參數僅 13B 的情況下支援百萬上下文，非常適合對成本敏感的推理解決方案。

🔗 **相關連結**
📝 DeepSeek-AI Releases DeepSeek-V4 Series (Preview)
🔗 詳細報導：https://www.marktechpost.com/2026/04/24/deepseek-ai-releases-deepseek-v4-compressed-sparse-attention-and-heavily-compressed-attention-enable-one-million-token-contexts/
🤗 模型權重：Hugging Face (DeepSeek-V4-Pro / Flash 系列)

你會選擇嘗試 1.6T 的 Pro 版，還是更輕量的 Flash 版來跑你的長上下文任務？歡迎在留言區討論 👇

#DeepSeek #AI #LLM #MachineLearning #開源模型 #長上下文 #MoE #自然語言處理
