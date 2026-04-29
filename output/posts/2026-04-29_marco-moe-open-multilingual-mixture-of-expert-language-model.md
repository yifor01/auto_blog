---
title: "Marco-MoE: Open Multilingual Mixture-of-Expert Language Models with Efficient Upcycling"
source: ChatPaper/Computation and Language
url: https://arxiv.org/abs/2604.25578
score: 120
model: tencent/hy3-preview:free
generated_at: 2026-04-29T19:52:04.948158
---

📌 【Alibaba 最新研究】5% 參數激活，效能超越 14 倍規模的競品

當大家都在追求模型參數越大越好時，Alibaba International Digital Commerce 團隊卻反其道而行。他們最新的 Marco-MoE 證明，透過極致的稀疏架構設計，僅需激活約 5% 的參數，就能在多語言任務上打敗那些激活參數多達 3 到 14 倍的競爭對手。這不僅是效能的勝利，更是成本與效率的降維打擊。

🤔 **多語言擴展的痛點，稀疏架構來解**

在傳統的密集模型（Dense Model）中，每增加一種新語言，往往會導致現有語言的效能衰退，這種「干擾效應」讓全球化 LLM 的擴展變得極其昂貴。Alibaba 團隊提出的 Marco-MoE 正是為了解決這個問題，實現低成本、高品質的多語言落地。

🧪 **Upcycling 策略與 5T Tokens 的極致訓練**

這不是從零開始的蠻力訓練。研究團隊採用了 Upcycling（升級循環）技術，將預訓練好的密集模型轉換為稀疏專家混合模型（MoE）。這種設計結合了兩大優勢：極高的稀疏度（每個 Token 僅激活約 5% 參數）與高效的訓練流程，最終在 5 兆（5T）Tokens 的規模上完成了預訓練。

 **極致效能比，小參數也能贏大巨人**

Marco-MoE 在英語及多語言基準測試中展現了同類最佳的效能運算比（Performance-to-Compute Ratio）。特別值得注意的是，經過後訓練（Post-training）優化的 Marco-MoE-Instruct 版本，其表現甚至超越了那些激活參數量高達 3 到 14 倍的競品模型。這意味著在推理成本大幅降低的同時，智慧水準並未打折。

💡 **專家活化模式，語言家族的結構化智慧**

研究團隊深入分析發現，Marco-MoE 學會了一種結構化的專家激活模式。對於語系相近的語言，模型會共享專家知識；對於語言學上較為孤立的語言，則會啟用高度專用的專家。這種機制不僅提升了效率，更解釋了為何它能實現無干擾的語言擴展。

⚠️ **全開放資源，但落地仍需評估推理架構**

雖然論文未明確提及特定限制，但對於工程團隊而言，MoE 模型雖然計算量（FLOPs）低，但通常需要載入全部參數（或大部分參數）到顯存中，這對推理基礎設施的顯存管理提出了不同於 Dense 模型的要求。此外，5T 級別的預訓練數據集雖已開源，但清洗與維護的品質仍需根據具體業務場景進行二次驗證。

🎯 **全開放資源，加速多語言 Agent 落地**

這篇論文最具吸引力的一點在於「完全開放」。Alibaba 團隊開源了完整的訓練數據集、訓練配方（Recipes）以及模型權重。對於正在開發多語言 Agent 或推理系統的團隊來說，這是一個可以直接拿來微調或部署的寶貴資產，大幅降低了全球化應用的門檻。

🔗 **論文連結**
📝 Marco-MoE: Open Multilingual Mixture-of-Expert Language Models with Efficient Upcycling
👤 Fan Jiang, Yu Zhao, Chenyang Lyu, Tianqi Shi, Yichao Du @ Alibaba International Digital Commerce
🔗 https://arxiv.org/abs/2604.25578

你認為在實際部署中，MoE 的顯存佔用與計算效率之間該如何取捨？歡迎在留言區討論 👇

#AI #LLM #MoE #多語言模型 #Alibaba #開源模型 #MachineLearning #AI研究
