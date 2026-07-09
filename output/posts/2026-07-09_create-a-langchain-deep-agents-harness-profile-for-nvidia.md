---
title: Create a LangChain Deep Agents Harness Profile for NVIDIA Nemotron 3 Ultra
  to Improve Performance
source: NVIDIA Developer
url: https://developer.nvidia.com/blog/create-a-langchain-deep-agents-harness-profile-for-nvidia-nemotron-3-ultra-to-improve-performance/
score: 98
model: google/gemma-4-31b-it:free
generated_at: '2026-07-09T09:53:07.171392'
---

📌 【NVIDIA】不靠微調，用 Harness Profile 工程提升 Nemotron 3 Ultra 的 Agent 準確率

TL;DR：透過建立 LangChain Harness Profile 並匯入迭代最佳化迴路，讓開源模型在 Agent 任務中接近頂尖私有模型的效能。

在開發 Agentic AI 時，工程師常陷入兩難：使用頂尖的私有模型雖然準確率高但成本昂貴；而使用高效能的開源模型雖然成本低，但初始準確率往往不足。傳統解決方案是進行 fine-tuning，但這需要極高的硬體資源與專業技術。

🤔 **微調成本高，如何在不重新訓練的情況下提升效能？**

NVIDIA 提出了一種「Harness Profile 工程」的方法。透過在 LangChain 等框架中建立針對特定模型的自定義設定（Harness Profile），可以在不更動模型權重的前提下，最佳化 NVIDIA Nemotron 3 Ultra 等開源模型的表現，使其準確率趨近於領先的私有模型。

🧩 **建立迭代最佳化迴路：從分析失敗到自動修正**

為了確保 Agent 的效能提升且不產生過擬合（overfitting），作者提出了一套機械化的最佳化流程：

1. 執行評估 (Run Evaluation) $\rightarrow$ 分析失敗原因。
2. 提出 Harness Profile 修改方案 $\rightarrow$ 例如修改 Prompt 或插入中介軟體（如 `ReadFileContinuationNoticeMiddleware`）。
3. 驗證修正結果 $\rightarrow$ 重新執行完整測試集以確保沒有迴歸（regression）。

💡 **利用 Agentic Proposers 實現自我修正**

為了進一步自動化這個過程，可以匯入如 LangSmith Engine 或 ralph loop 等 agentic proposers。這種機制允許系統自我修正 Harness Profile，其核心在於：
- 限制 Agent 的編輯範圍，避免隨意修改。
- 驗證測試案例是否重複通過。
- 確保解決方案具有通用性，而非僅針對單一測試案例過擬合。

這種方法讓 NVIDIA Nemotron 3 Ultra 能更靈活地適應不同的 Agent 框架，在維持低成本的同時提升任務成功率。

🎯 **實務啟示**

對於 AI 工程師而言，在考慮昂貴的 fine-tuning 之前，應優先嘗試「Harness Profile 工程」。透過建立「評估 $\rightarrow$ 修改 $\rightarrow$ 驗證」的閉環，並利用中介軟體（Middleware）處理特定邊界案例，可以用更低的成本達成接近頂尖模型的效能。

🔗 **來源**
- 標題：Create a LangChain Deep Agents Harness Profile for NVIDIA Nemotron 3 Ultra to Improve Performance
- 作者／機構：Sean Lopp, Matthew Penn and Sukrit Rao @ NVIDIA
- 連結：https://developer.nvidia.com/blog/create-a-langchain-deep-agents-harness-profile-for-nvidia-nemotron-3-ultra-to-improve-performance/

#AI #AgenticAI #NVIDIA #Nemotron3Ultra #LangChain #PromptEngineering #LLM #LangSmith #ModelOptimization #OpenSourceAI
