---
title: "Task-Aware Automated User Profile Generation for Recommendation Simulation Using Large Language Models"
source: ChatPaper/Information Retrieval
url: https://arxiv.org/abs/2605.13497
score: 103
model: tencent/hy3-preview:free
generated_at: 2026-05-14T20:57:12.859273
---

📌 【RMIT 大學最新研究】Task‑Aware 自動使用者檔案生成，讓推薦系統模擬更貼近真實  

你以為推薦系統的模擬只要優化記憶與行動模組就夠？研究指出，忽略使用者檔案的生成會讓模擬結果與真實使用者行動產生明顯偏差。  

🤔 **現有模擬過度依賴手動檔案，限制了擴展性**  
大型語言模型驅動的代理模擬通常分為 profile、memory、action 三個模組。然而，過去的工作多聚焦於改進 memory 與 action，而 profile 生成仍多依賴人工編寫的檔案。這樣的做法不僅費時費力，也使得模擬難以跨不同資料集或不同 LLM 保持一致，進而影響評估的可靠性。  

🧪 **提出 APG4RecSim：任務感知的自動檔案生成框架**  
本文提出 APG4RecSim，透過最小監督下的自動化流程，為推薦系統模擬建立具備一致性與穩健性的使用者檔案。實驗在三個基準資料集上進行，檢視框架在判別、排序與評分三個任務上的表現。  

📊 **排序品質提升最高 7%，評分分布偏差降低 8%**  
- 在 nDCG@10 指標上，APG4RecSim 比現有的檔案生成基線最高提升 7%。  
- 在 JSD（Jensen–Shannon divergence）上，評分分布的偏差減少了 8%。  
此外，產出的檔案對熱度與位置偏差具備韌性，且在不同資料集與不同 LLM 上均保持穩定表現。  

💡 **任務感知是關鍵：讓檔案與下游目標對齊**  
APG4RecSim 的「任務感知」設計意味著檔案生成會根據後續的排序或評分任務進行調整，使得產出的使用者行為更能反映真實的互動模式，而非只是統計上的平均特徵。這種對齊正是效能提升的主要原因。  

⚠️ **實驗範圍有限，需進一步驗證泛化能力**  
目前的結果僅基於三個基準資料集，雖然顯示出跨資料集與跨模型的穩定性，但在更大規模、更多樣化的真實世界環境中仍需進一步驗證。此外，框架的效果仍受底層 LLM 品質影響，極端模型可能會導致檔案品質波動。  

🎯 **工程師可直接採用，降低人工成本並提升模擬忠實度**  
- 將 APG4RecSim 推薦為建立可擴展推薦系統測試床的起點。  
- 減少手動編寫使用者檔案的需求，加快實驗迭代速度。  
- 透過任務感知機制，獲得更貼近真實使用者分布的模擬結果，從而做出更可靠的演算法決策。  

🔗 **論文連結**  
📝 Task-Aware Automated User Profile Generation for Recommendation Simulation Using Large Language Models  
👤 Xinye Wanyan, Chenglong Ma, Danula Hettiachchi, Ziqi Xu, Jeffrey Chan @ RMIT University  
🔗 https://arxiv.org/abs/2605.13497  

你在推薦系統模擬中是否也遇過手動檔案的瓶頸？歡迎在留言區分享你的經驗或對自動化檔案生成的看法 👇  

#AI #RecommendationSystems #LLM #Simulation #RMIT #MachineLearning #DataScience
