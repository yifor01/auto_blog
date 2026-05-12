---
title: "MaD Physics: Evaluating information seeking under constraints in physical environments"
source: ChatPaper/AI
url: https://arxiv.org/abs/2605.10820
score: 110
model: tencent/hy3-preview:free
generated_at: 2026-05-12T20:54:30.848072
---

📌 MaD Physics: 評估在物理約束下的資訊尋求能力

你以為 AI 只要看資料就能做科學？在真實實驗中，每次量測都有成本與品質限制，這才是真正的挑戰。

🤔 **科學發現本質是資源受限的量測決策**

現有基準多聚焦於靜態知識推理或無限制的實驗設計，忽略了科學家必須在有限的量測預算與品質下，決定何時、如何測量才能最有效地推導自然律。

🧪 **三個改變物理律的模擬環境與量測預算任務**

MaD Physics 建立了三個基於不同物理定律的環境，並故意改變定律以減少既有知識的干擾。每個回合中，代理人在耗盡預算前可以進行量測，預算限制了量測的數量與品質；結束後必須推導出潛在的物理定律並對未來系統狀態做出預測。

 **代理人在結構化探索與資料收集上顯示不足**

使用四個 Gemini 模型（2.5 Flash Lite、2.5 Flash、2.5 Pro、3 Flash）進行基準測試顯示，它們在需要有規律地選擇量測點以及在預算內收集足夠資訊方面表現不佳，導致模型推論的準確度受限。

💡 **受限環境下的量測規劃是科學代理人的關鍵瓶頸**

分析顯示，代理人傾向於要么過早耗盡預算、要么收集冗餘且無關的量測，缺乏能夠根據已得資料動態調整下一步量測策略的能力，這直接影響到從數據中推導正確物理模型的效能。

⚠️ **僅測試三個改變過的物理環境與 Gemini 模型族**

基準目前涵蓋三個物理場景、使用了人工改變的定律，並僅以 Gemini 系列模型進行評估；因此結果可能無法直接推廣至其他物理領域或不同架構的代理人。

🎯 **開發約束感知的探索策略與混合模型訓練**

未來工作可著重於設計能夠在有限預算下進行結構化量測的規劃演算法，或將強化學習與語言模型結合，讓代理人在實驗過程中學習何時該進行高品質量測、何時該儲存資源以備後續分析。

🔗 **論文連結**
📝 MaD Physics: Evaluating information seeking under constraints in physical environments
👤 Moksh Jain, Mehdi Bennani, Johannes Bausch, Yuri Chervonyi, Bogdan Georgiev @ Google DeepMind; Mila – Quebec AI Institute; Université de Montréal
🔗 https://arxiv.org/abs/2605.10820

#AI #ScientificDiscovery #AgenticAI #Gemini #MaDPhysics #DeepMind #Mila #ReinforcementLearning
