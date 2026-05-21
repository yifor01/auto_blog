---
title: "Open-World Evaluations for Measuring Frontier AI Capabilities"
source: ChatPaper/AI
url: https://arxiv.org/abs/2605.20520
score: 100
model: tencent/hy3-preview:free
generated_at: 2026-05-21T20:56:41.964840
---

📌 **開放世界評估：量測真實 AI**  

傳統基準測試可能高估或低估真實部署能力  
本文提出開放世界評估，以長時程、雜亂的真實任務為核心  
首例讓 AI 代理自行開發並上架 iOS App，僅需一次可避免的人工介入  

🤔 **基準測試的雙刃劍：易優化卻可能誤導**  
現行的 benchmark‑based 評估偏好可精確指定、自動評分、易於優化且成本低、週期短的任務。這種設計雖利於追蹤進步，但同時可能因過度聚焦於「乾淨」問題而高估能力，或因忽略真實世界的雜亂與長期依賴而低估已具備的部署潛力。  

🧪 **開放世界評估的概念與 CRUX 案例**  
我們提出一種互補的評估類別——**open‑world evaluations**：長時程、混雜的真實任務，透過小樣本的質化分析而非大規模自動化來衡量。為落實此理念，啟動 **CRUX (Collaborative Research for Updating AI eXpectations)** 專案，定期進行此類評估。作為首次實例，研究讓一個 AI 代理負責開發並將一個簡易 iOS 應用程式發布至 Apple App Store。  

🚀 **AI 代理完成 iOS App 上架，僅需一次可避免的人工介入**  
在該任務中，代理成功完成了從程式撰寫、測試到提交審核的全流程，全程僅出現一次可避免的手動介入。這個結果顯示，即使在沒有大量自動化基準的情況下，開放世界評估仍能捕捉到即將廣泛普及的能力早期訊號。  

💡 **為何小樣本質化分析能揭露潛在能力**  
開放世界評估不依賴於可重複的自動化評分，而是由領域專家觀察代理在真實、開放情境中的行為與決策。這樣的質化方式能夠揭示代理在處理不確定性、跨階段規劃以及與外部系統（如 App Store 審核機制）互動時的真實表現，從而補足基準測試在「可度量」與「實用」之間的盲點。  

⚠️ **樣本小、依賴專家判斷，難以自動化大規模重複**  
目前的開放世界評估樣本規模有限（僅單一任務案例），結果較依賴評估者的專業判斷，缺乏大規模自動化重複的能力。這意味著無法直接得到統計顯著的分數，且難以快速於眾多模型上進行廣泛比較。  

🎯 **建議將開放世界評估作為基準的補充，定期執行 CRUX 項目**  
對於研究與工程團隊，建議在現有 benchmark 評估之外，納入開放世界評估作為常規檢核。具體做法可參考 CRUX 案例：設計長時程、具真實世界雜亂度的任務（例如 App 開發與發布），以小樣本質化方式追蹤代理的表現，並將結果作為預警指標，以判斷哪些能力正從研究實驗室邁向實務部署。  

🔗 **論文連結**  
📝 Open-World Evaluations for Measuring Frontier AI Capabilities  
👤 Sayash Kapoor, Peter Kirgis, Andrew Schwartz, Stephan Rabanser, J. J. Allaire 等 (Princeton University; Cornflower Labs; Meridian Labs; Stanford University; UK AI Security Institute; Johns Hopkins University; Adaption Labs; Australian National University; Golden Gate Institute for AI; UW Madison; Microsoft Research; AI Digest; Georgetown University (CSET))  
🔗 論文：https://arxiv.org/abs/2605.20520  

你認為在評估 AI 代理時，開放世界評估應該佔多大的權重？歡迎留言討論 👇  

#AI #AgentEvaluation #OpenWorld #CRUX #AIResearch #MachineLearning #FrontierAI #Princeton #MicrosoftResearch #TechBlog
