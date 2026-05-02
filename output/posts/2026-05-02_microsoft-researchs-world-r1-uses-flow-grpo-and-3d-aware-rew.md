---
title: "Microsoft Research’s World-R1 Uses Flow-GRPO and 3D-Aware Rewards to Inject Geometric Consistency Into Wan 2.1 Without Architectural Changes"
source: MarkTechPost
url: https://www.marktechpost.com/2026/04/30/microsoft-researchs-world-r1-uses-flow-grpo-and-3d-aware-rewards-to-inject-geometric-consistency-into-wan-2-1-without-architectural-changes/
score: 113
model: tencent/hy3-preview:free
generated_at: 2026-05-02T19:15:49.998605
---

📌 【Microsoft Research】不改架構，用 RL 注入 3D 幾何一致性

你生成的影片畫面很美，但鏡頭一移動，牆壁就扭曲、物體也變形了嗎？這正是目前多數 Text-to-Video (T2V) 模型的致命傷，它們本質上只是在擬合 2D 像素，而非理解 3D 場景。

🤔 **美麗的畫面，脆弱的幾何結構**

目前的影片生成模型（如 Wan 2.1 或 CogVideoX）在單幀生成上表現驚人，但一旦涉及鏡頭移動或時間維度的連續性，往往會出現幾何崩壞。這是因為模型缺乏對三維空間的內在理解。過去要解決這個問題，通常需要昂貴的 3D 資產監督或重新設計模型架構，這對多數開發團隊來說門檻極高。

🧪 **World-R1：基於 Wan 2.1 的強化學習後訓練**

Microsoft Research 與浙江大學的團隊提出 World-R1，一個不需要修改基礎模型架構（Base Architecture）的對齊框架。該研究建立在一個關鍵發現上：現有的影片基礎模型內部其實已經編碼了豐富的 3D 幾何資訊，只是沒有被「激發」出來。

World-R1 透過兩個版本進行實證：World-R1-Small (基於 Wan2.1-1.3B) 與 World-R1-Large (基於 Wan2.1-14B)。

 **Flow-GRPO-Fast：為 Flow-Matching 量身打造的 RL**

這篇論文的技術核心在於訓練方法。團隊採用了 Flow-GRPO，這是將 GRPO (Group Relative Policy Optimization) 適配到 Flow-matching 擴散模型的一種變體：

1. **隨機性注入**：將確定性的 ODE 採樣器轉換為反向時間 SDE，讓策略具備足夠的隨機性以進行優勢估計（Advantage Estimation）。
2. **效率優化**：Flow-GRPO-Fast 版本僅在隨機選取的中間步驟注入 SDE 噪聲，大幅降低了 Rollout 成本。
3. **穩定性控制**：透過 KL 正則化（KL Regularization）約束參考策略，確保訓練穩定。

💡 **3D-Aware Rewards：用 3D 模型當評審**

World-R1 最巧妙的地方在於其獎勵機制。它不依賴昂貴的人工 3D 標註，而是利用預訓練的 3D 基礎模型作為 Critic：

*   **3DGS 重建**：使用 Depth Anything 3 為生成的影片重建 3D Gaussian Splatting (3DGS) 表示。
*   **相機軌跡估計**：恢復估計的相機軌跡。
*   **複合獎勵函數**：綜合評估元數據（S_meta）、重建品質（S_recon）與軌跡一致性（S_traj）。

這種設計讓模型在推理時（Inference）完全不增加任何額外成本，保持了 Wan 2.1 原本的推論效率。

⚠️ **運算資源需求與依賴預訓練模型**

雖然推理零成本，但訓練端的消耗不容小覷。World-R1-Small 使用了 48 張 NVIDIA H200 GPU，Large 版本則需要 96 張，且 GRPO 群組大小為 8。此外，該方法高度依賴預訓練 3D 模型（如 Depth Anything 3）的準確性，若底層幾何估計有偏差，獎勵信號也會受到影響。

🎯 **產業落地的可行性路徑**

對於工程團隊而言，World-R1 提供了一條極具吸引力的路徑：在不更動現有大型 T2V 模型架構的前提下，透過後訓練（Post-training）直接提升影片的幾何穩定性與可控性。這種「借用 3D Foundation Model 作為評價標準」的設定，非常契合目前業界對於模型可控性與 Agent 化推理的關切。

🔗 **論文連結**
📝 Microsoft Research’s World-R1 Uses Flow-GRPO and 3D-Aware Rewards to Inject Geometric Consistency Into Wan 2.1 Without Architectural Changes
👤 Michal Sutter @ Microsoft Research & Zhejiang University
🔗 詳細內容：https://www.marktechpost.com/2026/04/30/microsoft-researchs-world-r1-uses-flow-grpo-and-3d-aware-rewards-to-inject-geometric-consistency-into-wan-2-1-without-architectural-changes/

你覺得這種「不改架構只改獎勵」的後訓練方式，會是未來多模態模型優化的主流嗎？歡迎留言討論 👇

#MicrosoftResearch #AI #VideoGeneration #Wan21 #3DGS #ReinforcementLearning #WorldR1 #TechBlog
