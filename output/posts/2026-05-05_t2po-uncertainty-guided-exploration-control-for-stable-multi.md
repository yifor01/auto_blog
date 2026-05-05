---
title: "T^2PO: Uncertainty-Guided Exploration Control for Stable Multi-Turn Agentic Reinforcement Learning"
source: HuggingFace Daily Papers
url: https://huggingface.co/papers/2605.02178
score: 110
model: tencent/hy3-preview:free
generated_at: 2026-05-05T19:51:54.757726
---

📌 **T²PO：用不確定性解決多輪 Agent 訓練難題**

多輪 Agent 的強化學習訓練往往像在走鋼索，一不小心就會因為探索過度而崩潰。現在一個名為 T²PO 的新框架試圖從「不確定性」下手，把這種不穩定變成可控的過程。

🤔 **多輪 Agent RL 訓練的不穩定難題**

目前的 Agentic RL（強化學習）在處理多輪對話或決策時，常面臨訓練不穩定與難以擴展的挑戰。當 Agent 需要進行多步驟推理或與環境多次互動時，傳統的 RL 方法往往因為無法精細控制探索（Exploration）行為，導致模型性能震盪，甚至完全失效。這成為了許多開發者從原型邁向生產環境時的最大痛點。

🧪 **Token 與 Turn 雙層級的細粒度控制**

T²PO (Token- and Turn-level Policy Optimization) 提出了一種新的優化視角。不同於以往粗粒度的控制，它將策略優化細化到兩個層次：
1. **Token 層級**：在生成每個標記時進行微觀調控。
2. **Turn 層級**：在每一輪對話或決策點進行宏觀把控。

這種雙層架構的設計，旨在更精準地捕捉 Agent 在複雜任務中的行為模式。

💡 **不確定性引導的探索控制機制**

T²PO 的核心在於「不確定性監控」。研究團隊透過監測模型在生成過程中的不確定性，動態調整採樣策略。當模型對當前決策感到「猶豫」時，系統會介入並進行動態重採樣（Dynamic Resampling），從而抑制無效的探索，讓訓練過程更加平穩。這種機制讓 Agent 在面對複雜任務時，既能保持探索新路徑的能力，又不至於偏離目標太遠。

⚠️ **具體數據與細節有待論文完整公開**

目前公開資訊主要來自 HuggingFace Daily Papers 的摘要，缺乏具體的實驗數據（如各項基準測試的提升幅度）以及與其他 SOTA 方法的詳細對比。此外，T²PO 的計算開銷以及在不同規模模型上的泛化能力，也有待進一步確認。

🎯 **告別「碰運氣」式的 Agent 訓練**

對於正在開發複雜多輪 Agent 的開發者來說，這項研究提供了一個重要的啟示：穩定的 RL 訓練不應只靠調整獎勵函數，更需要從策略優化的粒度與不確定性管理入手。這或許是解決目前 Agent 訓練難以擴展的一把新鑰匙。

🔗 **論文連結**
📝 T^2PO: Uncertainty-Guided Exploration Control for Stable Multi-Turn Agentic Reinforcement Learning
🔗 https://huggingface.co/papers/2605.02178

你覺得在訓練多輪 Agent 時，最難穩定的部分是什麼？歡迎在留言區分享你的經驗 👇

#AI #MachineLearning #ReinforcementLearning #Agent #AIResearch #T2PO #HuggingFace
