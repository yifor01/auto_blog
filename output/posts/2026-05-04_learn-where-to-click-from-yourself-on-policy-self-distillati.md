---
title: "Learn where to Click from Yourself: On-Policy Self-Distillation for GUI Grounding"
source: ChatPaper/AI
url: https://arxiv.org/abs/2605.00642
score: 107
model: tencent/hy3-preview:free
generated_at: 2026-05-04T20:24:51.031608
---

📌 【中科院最新研究】單次訓練勝過多輪強化學習，GUI-SD 讓 AI 精準點擊

訓練一個能看懂螢幕並準確點擊的 GUI Agent 往往耗資巨大。現行的強化學習方法（如 GRPO）為了追求高準確度，必須進行昂貴的多輪嘗試（rollouts），且面對困難樣本時常常因為獎勵訊號稀疏而卡關。有沒有辦法用更少的資源，達到更好的效果？

🤔 **GUI Grounding 的痛點：多輪嘗試太燒錢，難樣本學不動**

GUI Grounding（將自然語言指令映射到螢幕座標）是自主 Agent 的核心能力。雖然基於 GRPO 的強化學習方法表現強勁，但其依賴多次採樣來優化策略，這在實際訓練中意味著巨大的算力成本。此外，當任務變難，模型得不到明確回饋，訓練效率便會大幅下降。

🧪 **GUI-SD：首個專為 GUI 設計的 On-Policy Self-Distillation**

由中國科學院、南開大學等團隊提出的 GUI-SD 框架，採用了 On-Policy Self-Distillation (OPSD) 路線。不同於 GRPO 的多輪次路徑，GUI-SD 僅需單次 rollout，就能提供密集的 token 級別監督訊號。

💡 **視覺增強與熵引導：不洩漏座標的精準教學**

這項研究有兩個關鍵設計。首先，它利用目標邊界框（Bounding Box）與高斯軟遮罩（Gaussian Soft Mask）構建「特權上下文」，讓作為老師的模型能獲得豐富的視覺引導，卻又不會直接洩漏精確座標。其次，透過「熵引導蒸餾（Entropy-guided Distillation）」，根據數字的重要性與老師的信心值自適應地加權 token，將優化重心集中在最關鍵的位置。

📊 **六項基準測試：準確度與效率的雙贏**

在六個具代表性的 GUI Grounding 基準測試中，GUI-SD 展現了顯著優勢。它不僅在準確度上超越了基於 GRPO 的方法，也優於樸素的 OPSD 方法。更重要的是，由於擺脫了多輪 rollout 的束縛，其訓練效率得到了實質提升。

🔍 **為什麼單次訓練能贏？因為監督更密集**

強化學習依賴最終結果的獎勵（稀疏訊號），而 GUI-SD 的蒸餾機制則是在每一步生成中提供細緻的 token 級反饋。這種從「結果導向」轉向「過程導向」的監督方式，特別適合 GUI 這種需要精確座標生成的任務，避免了模型在困難樣本上盲目探索。

⚠️ **目前聚焦單步 Grounding，多步 Agent 整合待驗證**

這篇論文主要聚焦於單步的 GUI Grounding 任務優化。雖然實驗證明了其在視覺定位上的有效性，但將其整合進需要多步驟決策的複雜 Agent 系統中，仍需進一步的實務驗證。此外，雖然開源了程式碼與數據，但不同 UI 風格的泛化能力仍依賴基礎模型的視覺理解能力。

🎯 **工程師的機會：開源框架可直接用於降低成本**

對於正在開發 GUI Agent 的團隊，GUI-SD 提供了一個高效的替代方案。相較於調整複雜的 RLHF 或 GRPO 參數，直接採用 On-Policy 蒸餾或許能以更低的算力成本快速迭代模型。特別是「熵引導加權」的機制，對於提升座標生成的精準度非常有借鑒意義。

🔗 **論文連結**
📝 Learn where to Click from Yourself: On-Policy Self-Distillation for GUI Grounding
👤 Yan Zhang, Daiqing Wu, Huawen Shen, Yu Zhou, Can Ma
🏛️ Chinese Academy of Sciences; Nankai University; University of Chinese Academy of Sciences
🔗 論文：https://arxiv.org/abs/2605.00642
💻 程式碼與數據：https://zhangyan-ucas.github.io/GUI-SD/

覺得 GUI Agent 的訓練成本太高嗎？不妨看看這篇論文的蒸餾策略，或許能為你的下一個專案省下不少 GPU 小時數 👇

#AI #GUIAgent #MachineLearning #ComputerVision #ReinforcementLearning #開源 #中科院 #技術落地
