---
title: "JURY-RL: Votes Propose, Proofs Dispose for Label-Free RLVR"
source: ChatPaper/AI
url: https://arxiv.org/abs/2604.25419
score: 123
model: tencent/hy3-preview:free
generated_at: 2026-04-29T19:47:47.009189
---

📌 【通義實驗室/浙大】JURY-RL：投票提答案、證明決獎勵，無標註逼近監督級表現

你還在為 RLHF 或 RLVR 需要大量人工標註答案而苦惱嗎？在數學與程式碼這類「機器可驗證」的領域，我們或許不再需要昂貴的 Ground Truth 了。

🤔 **RLVR 的瓶頸：標註成本與偽陽性風險**

強化學習結合可驗證獎勵（RLVR）是提升 LLM 推理能力的關鍵技術，但標準流程高度依賴人工標註或精心設計的獎勵函數。雖然多數投票（Majority Voting）或 LLM-as-a-Judge 能省去標註，但它們容易引入「偽陽性」（False Positives），導致模型學到錯誤的共識，反而讓訓練不穩定。

🧪 **JURY-RL：解耦提案與驗證的雙軌制設計**

來自通義實驗室與浙江大學的研究團隊提出 JURY-RL，核心概念是將「答案生成」與「獎勵判定」解耦。

1. **Votes Propose（投票提答案）**：透過模型多次 Rollout 進行多數投票，選出得票最多的候選答案。
2. **Proofs Dispose（證明決獎勵）**：利用形式化驗證器（如 Lean）對候選答案進行檢驗。只有當候選答案通過驗證，該投票組的 Rollouts 才能獲得獎勵。

💡 **ResZero 機制：解決驗證死角的梯度穩定劑**

如果驗證器無法確認候選答案（Inconclusive），JURY-RL 引入了 ResZero (Residual-Zero) 機制。它會捨棄無法驗證的多數共識，並將一個「零均值、保留方差」的獎勵訊號重新分配給剩餘的回答。這樣做能維持優化梯度的穩定性，避免模型在無法驗證的共識上過度強化。

 **Pass@1 追平監督學習，泛化能力更勝一籌**

在數學推理基準測試中，JURY-RL 的表現令人驚艷：
- **Pass@1 表現**：達到了與使用真實標註（Supervised Ground-truth）訓練相當的水準。
- **泛化能力**：在 pass@k 指標與回應多樣性上，展現了更強的泛化能力。
- **跨域遷移**：不僅在數學推理上有效，在程式碼生成與通用基準測試中，也展現了具競爭力的遷移能力。

⚠️ **形式化驗證的邊界與依賴**

雖然 JURY-RL 解決了標註問題，但其效能高度依賴於「形式化驗證器」（如 Lean）的可用性。這意味著目前主要適用於數學證明、程式碼等機器可檢查的領域，對於開放式問答或主觀任務，仍需搭配其他機制。

🎯 **無標註時代的訓練新範式**

對於從事 Agent 訓練或推理模型開發的團隊來說，JURY-RL 提供了一個極具參考價值的技術路徑：
- 善用形式化工具（Lean/Z3）來構建無標註的獎勵信號。
- 在設計獎勵時，考慮引入「殘差機制」來處理不確定性，避免模型陷入局部最優。

🔗 **論文連結**
📝 JURY-RL: Votes Propose, Proofs Dispose for Label-Free RLVR
👤 Xinjie Chen, Biao Fu, Jing Wu, Guoxin Chen, Xinggao Liu (Tongyi Lab, Alibaba Group & Zhejiang University)
🔗 論文：https://arxiv.org/abs/2604.25419

你覺得這種「讓模型自己投票、讓證明器打分」的模式，會是未來訓練推理模型的主流嗎？歡迎留言討論 👇

#AI #LLM #ReinforcementLearning #RLVR #Reasoning #Alibaba #通義實驗室 #MachineLearning #數學推理
