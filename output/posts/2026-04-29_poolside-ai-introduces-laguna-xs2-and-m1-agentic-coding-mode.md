---
title: "Poolside AI Introduces Laguna XS.2 and M.1: Agentic Coding Models Reaching 68.2% and 72.5% on SWE-bench Verified"
source: MarkTechPost
url: https://www.marktechpost.com/2026/04/28/poolside-ai-introduces-laguna-xs-2-and-m-1-agentic-coding-models-reaching-68-2-and-72-5-on-swe-bench-verified/
score: 111
model: tencent/hy3-preview:free
generated_at: 2026-04-29T20:10:00.818631
---

📌 【Poolside AI】本地跑 Agentic 模型？Laguna XS.2 釋出

想在本地端 Mac 跑出 68.2% 的 SWE-bench Verified 成績嗎？Poolside AI 這波操作，讓「開源權重」與「高效能 Agentic Coding」不再是魚與熊掌。

🤔 **SWE-bench 分數新高，但部署門檻仍是痛點**

當各家大模型都在堆砌參數與算力時，真正的挑戰往往不在跑分，而在於能否讓開發者在本地環境中實際運行。Poolside AI 近期發布了 Laguna 系列的前兩款模型，不僅在 SWE-bench 系列測試中取得了頂尖成績，更釋出了可於 Mac 上運行的開源權重版本。

🧪 **225B 與 33B 的 MoE 架構設計**

Laguna 家族全數採用 Mixture-of-Experts (MoE) 架構，核心邏輯是「大腦袋、小算力」。

*   **Laguna M.1**：作為家族基石，擁有 225B 總參數，但每次僅激活 23B。它基於 6,144 張 NVIDIA Hopper GPU 訓練，30T tokens 的預訓練量讓它在 SWE-bench Verified 上達到 72.5%。
*   **Laguna XS.2**：這是重點。33B 總參數，每次僅激活 3B。這種極致的稀疏化設計，讓它能塞進僅有 36GB RAM 的 Mac 中透過 Ollama 運行。

 **M.1 72.5% vs. XS.2 68.2% 的驚人差距**

在 SWE-bench Verified 這個考驗真實軟體修復能力的基準上，兩個模型展現了極強的競爭力：

*   **Laguna M.1**：72.5% (SWE-bench Verified)、46.9% (SWE-bench Pro)
*   **Laguna XS.2**：68.2% (SWE-bench Verified)、44.5% (SWE-bench Pro)

值得注意的是，XS.2 雖然體積更小，但在多語言支援 (SWE-bench Multilingual) 上僅落後 M.1 不到 5 個百分點，展現了極佳的性價比。

💡 **Sigmoid Gating 與混合注意力機制**

XS.2 的技術亮點在於其架構優化。它採用了 Sigmoid gating 機制，並結合了**混合注意力佈局**：在總共 40 層中，以 3:1 的比例配置 30 層 Sliding Window Attention (SWA) 與 10 層 Global Attention。這種設計旨在平衡長序列處理的效率與全域資訊的捕捉能力，特別適合長視野 (long-horizon) 的編程任務。

⚠️ **Terminal-Bench 表現與開源授權**

雖然 SWE-bench 表現亮眼，但在 Terminal-Bench 2.0 上，M.1 為 40.7%，XS.2 則為 30.1%，顯示在複雜終端環境交互上仍有進步空間。此外，XS.2 雖標榜 open-weight，但具體的授權限制與商業使用條款仍需參考官方發布細節。

🎯 **本地部署與 Agent RL 環境的實務價值**

這次發布不僅是模型，還包含了一個輕量級終端 Agent 工具 **pool** 以及雙向 Agent Client Protocol (ACP)。這是 Poolside 內部用於 Agent RL 訓練的環境，現在作為研究預覽釋出。對於開發者來說，現在可以直接在本地用 Ollama 跑 XS.2，並參考 pool 的架構來訓練自己的 Agent 模型。

🔗 **相關連結**
📝 Poolside AI Introduces Laguna XS.2 and M.1
👤 Asif Razzaq @ MarkTechPost
🔗 全文：https://www.marktechpost.com/2026/04/28/poolside-ai-introduces-laguna-xs-2-and-m-1-agentic-coding-models-reaching-68-2-and-72-5-on-swe-bench-verified/

你會選擇在本地跑 XS.2，還是呼叫 API 用 M.1？歡迎討論 👇

#AI #MachineLearning #LLM #AgenticAI #Coding #PoolsideAI #MoE #SWEbench #開源模型
