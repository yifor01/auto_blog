---
title: "DeepSeek V4—almost on the frontier, a fraction of the price"
source: Simon Willison
url: https://simonwillison.net/2026/Apr/24/deepseek-v4/
score: 87
model: tencent/hy3-preview:free
generated_at: 2026-05-02T19:35:57.752715
---

📌 DeepSeek V4：逼近邊緣效能，成本卻只有零頭  

才剛 12 月釋出 V3.2 系列，中國 AI 實驗室 DeepSeek 就在四月直接端出兩款 V4 預覽模型。當大家還在討論推理成本與上下文長度的極限時，DeepSeek 用 Mixture-of-Experts 架構與百萬級上下文，給出了一張明確的價效比路線圖。  

🤔 **逼近前沿效能，但價格壓到極限**  
在大型語言模型持續膨脹的現階段，成本與部署門檻往往決定了技術能否落地。DeepSeek V4 的誕生時機，正踩中產業對「高效推理」與「開源可用性」最敏感的痛點：不只是跑得更快，而是用更少的成本達到邊緣與企業級的可用標準。  

🧪 **兩款預覽模型，百萬級上下文與 Mixture-of-Experts**  
DeepSeek 一出手就是兩款預覽模型：  
- DeepSeek-V4-Pro：總參數 1.6T，活躍參數 49B  
- DeepSeek-V4-Flash：總參數 284B，活躍參數 13B  

兩者皆採用 1 百萬 Token 上下文與 Mixture-of-Experts 架構，並使用標準 MIT 授權。這不僅讓工程師能快速評估與部署，也大幅降低實驗與生產化的門檻。  

💡 **用更少的活躍參數，換取可負擔的推理成本**  
V4 的設計策略很明顯：在不犧贈上下文長度與整體容量的前提下，透過稀疏啟動機制壓縮單次推理的計算負擔。這意味即便在邊緣或成本敏感環境中，也能以較低延遲與較小記憶體需求運行具備深層推理能力的模型。  

💡 **MIT 授權與預覽節奏，改變開源模型升級的預期**  
標準 MIT 授權加上雙模型並行的預覽策略，讓開發者不必在「強大但封閉」與「開源但落後」之間二選一。這種釋出節奏也壓縮了產業適應新架構的學習週期，推動大型模型更快進入可測試、可部署、可量產的階段。  

⚠️ **仍是預覽模型，長期穩定性與生態尚未定調**  
目前發布仍屬預覽階段，長期穩定性與更新路線尚不明確；同時，百萬級上下文對工程實踐中的檢索、排程與記憶管理提出更高要求，未必適合所有現場環境直接導入。  

🎯 **低成本高效能已成可測試的選項，評估門檻大幅降低**  
- 先以 Flash 測試邊緣與成本敏感場景的可行性  
- 以 Pro 評估高品質推理與長期上下文的需求配對  
- 將 MIT 授權納入合規與二次開發的考量  

🔗 **論文連結**  
📝 DeepSeek V4—almost on the frontier, a fraction of the price  
👤 Simon Willison  
🔗 https://simonwillison.net/2026/Apr/24/deepseek-v4/  

你的團隊在評估大型模型時，最在意成本、上下文還是授權條款？歡迎分享你的實戰經驗 👇  

#DeepSeek #AI模型 #MixtureOfExperts #開源AI #邊緣運算 #MIT授權
