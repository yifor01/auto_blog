---
title: "Mutual Forcing: Dual-Mode Self-Evolution for Fast Autoregressive Audio-Video Character Generation"
source: ChatPaper/Computer Vision and Pattern Recognition
url: https://arxiv.org/abs/2604.25819
score: 118
model: tencent/hy3-preview:free
generated_at: 2026-04-29T19:55:42.983847
---

📌 【南開大學 x 通義實驗室】雙模式自進化，4 步生成高品質音影片

當大多數生成模型還在依賴複雜的蒸餾管線與雙向教師模型時，這篇來自南開大學、通義實驗室與北京大學的合作研究，直接把音訊與視訊的聯合生成推向了「原生自回歸」的新境界。

🤔 **流式音影片生成：效率與同步的兩難**

在 Audio-Video 生成領域，長期存在兩個痛點。首先是「聯合建模」，音訊與視訊的時序同步極難優化；其次是「生成速度」，傳統的自回歸模型往往需要數十步的迭代採樣，難以滿足即時應用需求。既有的流式生成方案通常得先訓練一個雙向模型，再經過多階段的蒸餾（Distillation）將其轉換為因果生成器，這不僅流程繁瑣，還受限於教師模型的品質。

🧪 **Mutual Forcing：雙模式共享權重的自蒸餾架構**

這篇論文提出了一個名為 **Mutual Forcing** 的框架。不同於以往追隨固定的教師模型，這個架構在同一個權重共享的模型中，同時整合了「少步生成（Few-step）」與「多步生成（Multi-step）」兩種模式。

💡 **雙模式互強：訓練與推理的一致性**

這是該研究最精妙的地方。在訓練過程中：
1. **多步模式** 透過自我蒸餾（Self-distillation）來改善少步模式的品質。
2. **少步模式** 則負責生成歷史上下文，讓模型在訓練時就能模擬推理時的狀態，大幅提升訓練與推理的一致性（Training-Inference Consistency）。

這兩種模式在單一模型中互相強化，消除了對額外雙向教師模型的依賴。

 **4 步勝過 50 步，效能與品質的雙贏**

實驗數據顯示，Mutual Forcing 在僅使用 **4 到 8 個採樣步驟** 的情況下，其生成品質就能媲美甚至超越那些需要約 **50 步** 採樣的強力基準模型（Baselines）。這意味著在長時程音視訊同步的任務上，它實現了顯著的效率提升與品質突破。

⚠️ **靈活度提升，但長序列訓練仍是挑戰**

相較於 Self-Forcing 等前作，Mutual Forcing 移除了額外的教師模型，支援更靈活的訓練序列長度，並直接從真實配對數據中學習。不過，作為一個基於自回歸的架構，在極長序列的穩定性與資源消耗上，仍需持續觀察。

🎯 **原生自回歸架構，多模態 Agent 的新基石**

對於致力於開發多模態 Agent 或即時互動內容生成的工程師來說，這項技術展示了如何在不犧牲品質的前提下，透過架構設計（而非依賴複雜的蒸餾管線）來解決流式生成的難題。這種「雙模式自進化」的思路，值得在設計下一代生成系統時參考。

🔗 **論文連結**
📝 Mutual Forcing: Dual-Mode Self-Evolution for Fast Autoregressive Audio-Video Character Generation
👤 Yupeng Zhou, Lianghua Huang, Zhifan Wu, Jiabao Wang, Yupeng Shi (Nankai University; Tongyi Lab; Peking University)
🔗 論文：https://arxiv.org/abs/2604.25819
🌐 專案頁面：https://mutualforcing.github.io

你覺得這種「雙模式互強」的設計，能解決目前多模態生成中的哪些痛點？歡迎在留言區討論 👇

#AI #Multimodal #VideoGeneration #AudioGeneration #MachineLearning #NankaiUniversity #TongyiLab #SelfDistillation #AIGC
