---
title: "Evolving-RL: End-to-End Optimization of Experience-Driven Self-Evolving Capability within Agents"
source: ChatPaper/AI
url: https://arxiv.org/abs/2605.10663
score: 117
model: tencent/hy3-preview:free
generated_at: 2026-05-12T20:29:42.817784
---

📌 **Evolving-RL：經驗驅動的自我進化**  

你以為讓大型語言模型自己從過去互動中提取經驗就能持續適應新任務？實際上，若模型的抽象、泛化與上下文學習能力不被同時提升，這種「自我進化」往往會停滯不前。  

🤔 **經驗萃取與利用需同步提升，單一環節優化不足以帶來真正的自我進化**  
Experience‑driven self‑evolving agents 試圖透過從過去互動中蒐集可重複使用的經驗，來克服大型語言模型的靜態特性。然而，多數現有研究聚焦於系統層面的設計（例如經驗如何表示與管理），而忽視了基礎模型自身在抽象、泛化與上下文學習方面的能力。如果這些內在能力不被同步強化，僅優化經驗的利用或萃取單一環節，無法實現真正的端到端自我進化。  

🧪 **以經驗萃取與評估為核心的聯合強化學習框架**  
Evolving‑RL 提出一個端到端的演算法框架，將經驗的萃取與利用視為一個統一的強化學習問題。學習過程以經驗萃取與評估為中心，從評估步驟中導出兩個監督訊號：一個用於優化經驗萃取器（extractor），另一個用於優化經驗利用者（solver）。這兩個訊號分別驅動兩個組件的更新，使它們能夠協同共演（co‑evolution），從而在不依賴額外系統設計的同時提升經驗的抽取與重用能力。  

🔑 **核心發現：經驗萃取與利用的協同進化帶來顯著的 OOD 性能提升**  
在 ALFWorld 與 Mind2Web 兩個 Agent 基準上的實驗顯示，Evolving‑RL 能有效提升大型語言模型萃取與重複使用經驗的能力。相較於 GRPO 基線，在 ALFWorld 的未見任務上實現最高 98.7% 的相對改善，在 Mind2Web 上達到 35.8% 的提升。這些收益僅在經驗萃取與利用兩端進行協同共演時才會被完全釋放。此外，Evolving‑RL 本質上是一種經驗增強的強化學習算法：它將可重複使用的經驗模式直接內化到模型參數中，因而即使在測試時不進行額外的經驗積累，也能在已見與未見任務上都獲得顯著的性能提升。  

💡 **深入分析：經驗的內部化使模型參數直接編碼可重用模式，減少對外部經驗庫的依賴**  
透過將經驗模式嵌入模型權重，Evolving‑RL 使模型在推論時能直接參考內化的知識，而不需要依賴外部的經驗檢索或存儲結構。這種內部化不僅提升了模型在新任務上的泛化能力，也降低了對經驗管理系統的複雜度需求，使得自我進化過程更為簡潔與高效。  

⚠️ **研究限制：僅在兩個 Agent 基準上驗證，未涉及更廣泛的任務或長期互動效果**  
目前的實驗僅限於 ALFWorld 與 Mind2Web 兩個基準。論文未報告在更多樣化任務或長時間互動情境下的表現，亦未探討模型在經驗內部化過程中可能出現的遺忘或干擾問題。  

🎯 **實務啟示：在構建自我進化 Agent 時，應同時強化經驗萃取與利用兩端，而非只優化經驗表示或管理**  
對於希望部署能夠持續適應新情境的語言模型代理，研究結果建議將經驗的萃取與利用視為一個整體來優化。在實務上，可將類似 Evolving‑RL 的聯合優化策略納入現有的強化學習流程，使模型在訓練階段就學會如何從經驗中抽取有用模式並在參數層面予以保存，從而在測試時無需額外經驗庫仍能保持較好的泛化表現。  

🔗 **論文連結**  
📝 Evolving-RL: End-to-End Optimization of Experience-Driven Self-Evolving Capability within Agents  
👤 Zhiyuan Fan, Wenwei Jin, Feng Zhang, Bin Li, Yihong Dong (Xiaohongshu Inc.; Peking University)  
🔗 https://arxiv.org/abs/2605.10663  

你在開發 AI 代理時，是否曾經只優化經驗的存儲或檢索，而忽略了模型本身的學習能力？歡迎在留言區分享你的經驗與思考 👇  

#AI #ReinforcementLearning #Agent #SelfEvolution #LLM #Xiaohongshu #PekingUniversity #MachineLearning #研究解讀
