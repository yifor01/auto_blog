---
title: "deepseek-ai/DeepSeek-V3"
source: GitHub Trending
url: https://github.com/deepseek-ai/DeepSeek-V3
score: 137
model: tencent/hy3-preview:free
generated_at: 2026-04-25T19:00:58.054093
---

📌 【DeepSeek 最新】671B MoE 模型，訓練成本僅 280 萬小時

大家都還記得訓練一個頂級大模型需要燒掉多少錢嗎？當外界普遍認為千億級別模型的訓練門檻已高不可攀時，DeepSeek 再次用數據證明，架構設計的巧思比單純堆疊算力更重要。這次，他們做到了全程訓練無回滾、無損失飆升。

🤔 **MoE 架構的痛點：負載平衡與訓練成本**

混合專家模型（MoE）雖然能在推理時只激活部分參數，達到「小而美」的效果，但如何在訓練時讓專家們均衡工作（Load Balancing），一直是個大難題。傳統方法通常依賴輔助損失函數（Auxiliary Loss），但這往往會犧牲模型性能。此外，高昂的訓練成本總是讓開源社群望而卻步。

🧪 **671B 參數，每次僅激活 37B**

DeepSeek-V3 延續了 V2 的高效架構，採用 Multi-head Latent Attention (MLA) 和 DeepSeekMoE。這次的核心技術亮點在於：

1. **無輔助損失策略（Auxiliary-Loss-Free）**：這是該模型在架構上的最大創新，直接解決了負載平衡的難題，而不依賴傳統的損失函數。
2. **多 Token 預測（Multi-Token Prediction）**：改變了訓練目標，讓模型一次預測多個 Token，顯著提升了推理速度與效能。

 **14.8T Token 預訓練，效能直逼閉源頂級模型**

經過 14.8 兆個高品質 Token 的預訓練，加上監督微調（SFT）與強化學習（RL）階段，DeepSeek-V3 在評測中擊敗了所有開源對手，並在性能上與領先的閉源模型（如 GPT-4o、Claude 3.5）並駕齊驅。

💡 **2.788M H800 GPU 小時，且全程零回滾**

這是工程師最該關注的數據。DeepSeek-V3 的完整訓練僅耗費 2.788M H800 GPU 小時。更令人驚訝的是，在整個漫長的訓練過程中，團隊沒有遇到任何不可恢復的損失飆升（Loss Spikes），也沒有進行任何訓練回滾（Rollbacks）。這顯示了其架構設計的極高穩定性。

⚠️ **開源模型的算力挑戰**

雖然 DeepSeek 公開了模型與論文，但對於一般開發者來說，2.788M H800 GPU 小時的訓練成本依然不是小數目。此外，目前公開的資訊主要集中在模型架構與效能，對於特定垂直領域的細微表現，仍需社群進一步驗證。

🎯 **工程師可以直接部署與微調**

DeepSeek-V3 已經在 GitHub 開源，並提供了詳細的本地運行指南與 API 平台。對於正在研究 Agent 或複雜推理任務的開發者來說，這是一個兼具成本效益與強大推理能力的開源選擇。

🔗 **論文與資源連結**
📝 DeepSeek-V3
👤 deepseek-ai
🔗 GitHub: https://github.com/deepseek-ai/DeepSeek-V3
📄 Paper Link: (詳見 GitHub README)

你覺得這種「無輔助損失」的設計會成為下一代 MoE 模型的標配嗎？歡迎在留言區討論 👇

#AI #DeepSeek #MoE #LLM #OpenSource #MachineLearning #大模型 #AI工程
