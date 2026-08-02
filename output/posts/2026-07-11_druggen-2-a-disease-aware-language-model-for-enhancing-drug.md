---
title: 'DrugGen 2: A disease-aware language model for enhancing drug discovery'
source: HuggingFace Daily Papers
url: https://huggingface.co/papers/2607.08404
score: 88
model: google/gemma-4-31b-it:free
generated_at: '2026-07-11T09:51:35.077094'
---

📌 **DrugGen 2：結合疾病 Ontology 與 GRPO 強化藥物發現**

TL;DR：透過 GPT-2 微調並引入 GRPO 強化學習，生成具備高多樣性且結合親和力更佳的藥物分子。

傳統自動藥物發現往往難以兼顧分子的化學多樣性與對特定疾病靶點的結合能力。DrugGen 2 嘗試將臨床疾病知識直接注入語言模型的生成過程中，讓 AI 不僅是「畫出分子」，而是「針對病因設計藥物」。

🧬 **將疾病語意轉譯為生成條件**

DrugGen 2 的核心在於「疾病感知」（Disease-aware）。模型並非隨機生成小分子，而是以兩個關鍵條件作為輸入引導：

1.  **疾病 Ontology（本體論）資料**：將疾病的分類與關聯知識結構化，作為生成的條件約束。
2.  **目標蛋白質序列**：明確指定藥物需要作用的生物標靶。

這種設計將現實中「針對某種疾病與靶點尋找候選藥物」的問題，形式化為條件式序列生成任務。模型需學習如何在滿足疾病分類與蛋白序列匹配的前提下，構造出有效的化學結構。

🤖 **GPT-2 基底與 GRPO 強化學習**

在架構上，DrugGen 2 並未採用最新的巨型 Transformer，而是選擇基於 GPT-2 進行微調。這種設計可能著重於效率與特定領域的適應性，而非單純堆疊參數量。

訓練過程分為兩階段：
1.  **監督式學習（Supervised Learning）**：首先使用已知藥物資料對 GPT-2 進行微調，建立基礎的分子生成能力。
2.  **強化學習（Reinforcement Learning）**：引入 **GRPO**（Group Relative Policy Optimization）演算法進行進一步最佳化。

GRPO 在此扮演關鍵角色，它透過獎勵機制引導模型生成具有更高「結合親和力」（Binding Affinity）與「分子多樣性」的結構。相較於傳統監督式微調容易陷入局部最佳解或生成重複結構，RL 階段能顯著提升生成藥物的實用價值。

📊 **超越基線的效能表現**

根據摘要指出，DrugGen 2 在關鍵評估指標上優於基準模型（Baseline Models）：

*   **分子多樣性（Molecular Diversity）**：生成的化合物結構更加多元，減少重複性。
*   **結合親和力（Binding Affinity）**：生成的分子與目標蛋白質的結合潛力更高，更接近潛在的有效藥物。

這意味著該模型不僅能產生「像藥物」的分子，還能產生「對特定疾病有效」的分子。

💡 **工程視角：舊架構的新應用**

雖然 GPT-2 在自然語言處理領域已非最新架構，但在藥物發現（Drug Discovery）這類需要高度結構化條件控制的任務中，小型且穩定的基底模型配合先進的 RL 演算法（如 GRPO），往往能展現極高的價效比。這提醒我們，領域特定的最佳化（Domain-specific Fine-tuning + RL）有時比單純追求模型規模更為重要。

⚠️ **資訊限制**

目前僅能提供摘要資訊，詳細的訓練資料集規模、具體的 GRPO 獎勵函式設計、以及與其他 SOTA 模型（如 Diffusion-based generators）的直接對照資料，尚待完整論文發布後確認。

🔗 **來源**
- 標題：DrugGen 2: A disease-aware language model for enhancing drug discovery
- 連結：https://huggingface.co/papers/2607.08404

#DrugDiscovery #MachineLearning #GPT2 #GRPO #ReinforcementLearning #Bioinformatics #ChemicalInformatics #NLP #AIforScience #DrugGen2
