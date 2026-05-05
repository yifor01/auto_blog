---
title: "Enhancing Judgment Document Generation via Agentic Legal Information Collection and Rubric-Guided Optimization"
source: ChatPaper/Information Retrieval
url: https://arxiv.org/abs/2605.02011
score: 110
model: tencent/hy3-preview:free
generated_at: 2026-05-05T19:51:25.320843
---

📌 【清華大學 x 泉城實驗室】Judge-R1：用 Agent 與強化學習解決法律 AI 的幻覺難題

當 AI 開始撰寫判決書，你最擔心什麼？不是它寫得不夠快，而是它引用了不存在的法條，或者邏輯推理出現致命漏洞。現有的標準 RAG（檢索增強生成）在面對嚴謹的司法場景時，往往因為證據召回不足和邏輯缺陷而顯得力不從心。

🤔 **標準 RAG 的瓶頸：光靠檢索還不夠，邏輯才是法律 AI 的痛點**

自動化判決書草擬是提升司法效率的關鍵，但目前的挑戰在於「雙重要求」。首先，模型必須精準檢索法條與判例；其次，必須具備嚴謹的法律推理邏輯。現有的監督微調（SFT）和標準 RAG 方法，常因為檢索來源單一、缺乏動態規劃，導致「幻覺」問題（Hallucination），甚至出現法律邏輯上的謬誤。

🧪 **Judge-R1 框架：Agentic 檢索結合 GRPO 強化學習**

清華大學與泉城實驗室的研究團隊提出了一個統一框架 Judge-R1。這個框架的設計相當講究，分為兩個核心階段：

1. **Agentic Legal Information Collection**：不同於傳統的一次性檢索，這裡採用動態規劃 Agent。Agent 會根據當前需求，主動從多個法律資訊源中精準撈取法條與判例，解決了證據召回不足的問題。
2. **Rubric-Guided Optimization**：這是論文的精華。團隊利用 **Group Relative Policy Optimization (GRPO)** 進行強化學習訓練。透過設計一個全面的法律獎勵函數（Reward Function），強制模型在生成過程中遵守司法標準與推理邏輯，而不僅僅是模仿訓練資料。

 **JuDGE 基準測試：法律準確度與生成品質雙雙超越 SOTA**

在專業的 JuDGE 基準測試中，Judge-R1 展現了顯著的性能提升。相比於現有的最先進（SOTA）基線模型，Judge-R1 在法律準確性（Legal Accuracy）和生成品質（Generation Quality）兩個維度上都取得了明顯優勢。這證明了將「動態檢索」與「邏輯約束優化」結合的有效性。

💡 **Rubric-Guided Optimization 的啟示：從「模仿」走向「合規」**

這篇論文最值得關注的技術亮點在於強化學習的應用。傳統的 SFT 讓模型學會「怎麼寫」，而 GRPO 加上法律獎勵函數則讓模型學會「為什麼這樣寫才合法」。這種基於規則（Rubric）的引導，讓模型在生成過程中能自我校正，減少邏輯謬誤。

⚠️ **研究聚焦特定司法場景，泛化能力待驗證**

論文目前主要基於 JuDGE 基準進行評估。雖然展示了強大的性能，但實際司法場景涉及不同法域、複雜的倫理判斷以及多變的判例引用規則。此外，強化學習的訓練成本與部署效率也是實務上需要權衡的考量。

🎯 **對 RAG 系統設計的實務啟示**

如果你正在開發垂直領域的 AI 應用（如金融、醫療或法律），Judge-R1 提供了一個優秀的架構範本：
- **不要只做靜態檢索**：嘗試引入 Agent 機制，讓模型具備動態規劃檢索路徑的能力。
- **引入領域獎勵函數**：在微調或對齊階段，利用強化學習（如 GRPO）來強化對「領域邏輯」的遵守，而不僅僅是文字流暢度。

🔗 **論文連結**
📝 Enhancing Judgment Document Generation via Agentic Legal Information Collection and Rubric-Guided Optimization
👤 Weihang Su, Xuanyi Chen, Yueyue Wu, Qingyao Ai, Yiqun Liu
🏛️ Tsinghua University; Quan Cheng Laboratory
🔗 論文：https://arxiv.org/abs/2605.02011

你認為在哪些專業領域，AI 的「邏輯合規性」比「生成速度」更重要？歡迎在留言區討論 👇

#AI #LegalTech #RAG #ReinforcementLearning #清華大學 #NLP #人工智慧 #法律科技
