---
title: 'GUICrafter: Weakly-Supervised GUI Agent Leveraging Massive Unannotated Screenshots'
source: HuggingFace Daily Papers
url: https://huggingface.co/papers/2606.29705
score: 85
model: google/gemma-4-31b-it:free
generated_at: '2026-06-30T20:43:14.831192'
---

📌 GUICrafter：利用海量未標記截圖，以弱監督學習打造 GUI Agent

TL;DR：透過弱監督方法與兩階段課程學習，解決 GUI 代理人缺乏標註資料的訓練痛點。

訓練一個能操作介面的 GUI Agent，最困難的往往不是模型架構，而是高品質標註資料的匱乏。如果每一張截圖都要人工標記對應的操作指令，資料獲取成本將高得令人絕望。

🤔 **GUI 代理人的資料困境**

目前的 GUI Agent 在訓練上高度依賴標註資料，但現實中我們擁有海量的未標記截圖（Unannotated Screenshots）。如何利用這些「沒標籤」的資料來提升模型對介面的理解與操作能力，是 GUICrafter 試圖解決的核心問題。

🧩 **弱監督學習與兩階段課程框架**

GUICrafter 提出了一套弱監督（Weakly-Supervised）方法，不再強求精確的標註，而是透過兩階段的課程學習（Curriculum Learning）框架來逐步提升模型能力：

1. **視覺定位（Visual Grounding）**：第一階段專注於讓模型理解截圖中的元素與其空間關係。
2. **強化學習校準（Reinforcement Learning Calibration）**：第二階段則透過強化學習對模型的操作行為進行校準，最佳化最終的執行效果。

🎯 **實務啟示**

對於開發 GUI Agent 的工程師來說，GUICrafter 提供了一個重要的思考方向：當面對缺乏標記資料的場景時，不一定要追求完美的資料集，可以嘗試將任務拆解為「先學習視覺定位，再透過強化學習校準」的階段式訓練路徑，以降低對人工標註的依賴。

🔗 **來源**
- 標題：GUICrafter: Weakly-Supervised GUI Agent Leveraging Massive Unannotated Screenshots
- 連結：https://huggingface.co/papers/2606.29705

#GUI #Agent #WeaklySupervised #CurriculumLearning #VisualGrounding #ReinforcementLearning #ComputerVision #Automation #MachineLearning #HuggingFace
