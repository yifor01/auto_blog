---
title: Path-Constrained Mixture-of-Experts
source: Apple ML
url: https://machinelearning.apple.com/research/path-constrained-mixture-experts
score: 95
model: google/gemma-4-31b-it:free
generated_at: '2026-07-06T20:26:35.997310'
---

📌 【Apple 研究】PathMoE：將 MoE 從「單層路由」轉向「路徑約束」提升效能

TL;DR：透過跨層共享路由參數來約束專家路徑，在減少統計低效的同時，提升模型困惑度與任務表現。

在傳統的 Sparse Mixture-of-Experts (MoE) 架構中，每個 token 在經過每一層時，都是獨立地選擇一組專家。但如果將這個過程視為一條「路徑」（Expert Paths），會發現一個有趣的現象：token 實際上只會集中在少數幾條符合語言功能的路徑上，而絕大多數可能的路徑根本沒被探索過。

🤔 **獨立路由導致的統計低效**

在一個擁有 $N$ 個專家且共 $L$ 層的模型中，理論上存在 $N^L$ 種可能的路徑組合。然而，研究發現 token 在實務上的分佈非常集中，這意味著目前的獨立路由設計存在統計上的低效（statistical inefficiency），因為模型在每一層重複做決定，卻忽視了跨層之間潛在的結構一致性。

🧩 **PathMoE：共享路由參數以約束路徑空間**

為了放大這種自然集中的路徑結構，Apple 提出了 PathMoE。其核心設計理念是：**不再讓每一層獨立路由，而是在連續的層塊（blocks of consecutive layers）之間共享路由參數**。

這種設計將 MoE 的計算視角從「單層選擇」提升到「路徑選擇」，其效果如下：
- **強化路徑叢集**：產生更集中的路徑分佈。
- **提升一致性**：增加跨層之間的路由一致性。
- **增強魯棒性**：對路由擾動（routing perturbations）具有更強的抵抗力。

📊 **0.9B 與 16B 模型的實驗結果**

研究團隊在 0.9B 與 16B 兩種規模的 PathMoE 模型上進行驗證，結果顯示：
- **效能提升**：在困惑度（perplexity）與下游任務上，表現一致優於傳統的獨立路由設計。
- **簡化訓練**：PathMoE 在提升效能的同時，消除了對輔助損失函式（auxiliary losses）的需求。

🎯 **實務啟示**

對於開發 MoE 模型的工程師來說，這項研究提供了一個新的設計維度：路由不一定要在每一層重新計算。透過引入「路徑約束」或「跨層共享路由」，可以在不增加計算開銷的前提下，利用 token 的語言功能特性來最佳化參數利用率，並簡化訓練過程（如移除 auxiliary loss）。

🔗 **來源**
- 標題：Path-Constrained Mixture-of-Experts
- 作者／機構：Zijin Gu, Tatiana Likhomanenko, Vimal Thilak, Jason Ramapuram, Navdeep Jaitly @ Apple ML
- 連結：https://machinelearning.apple.com/research/path-constrained-mixture-experts

#MoE #LLM #DeepLearning #AppleML #PathMoE #Routing #NLP #MachineLearning #ModelArchitecture #SparseModels
