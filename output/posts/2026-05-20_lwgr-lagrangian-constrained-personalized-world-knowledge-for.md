---
title: "LWGR: Lagrangian-Constrained Personalized World Knowledge for Generative Recommendation"
source: ChatPaper/Information Retrieval
url: https://arxiv.org/abs/2605.18771
score: 115
model: tencent/hy3-preview:free
generated_at: 2026-05-20T21:01:30.419238
---

📌 LWGR：Lagrangian 約束的個性化世界知識  

你以為把世界知識直接塞進推薦模型就能讓效果飆升？實際上，這樣做可能反而傷害推薦。  

🤔 **固定指令難以捕捉使用者興趣的多維異質性**  
現有的 LLM 基礎生成式推薦（GR）多半依賴手動設計的固定指令來產生語意知識，然後直接併入模型。這種做法無法反映不同使用者的興趣細節，且知識融合過程難以控制，易與行為訊號衝突，導致推薦品質下降。  

🧪 **以行為為導向的個性化知識萃取與受控融合**  
LWGR 框架提出兩個改進軸：首先，它為每位使用者建構「軟指令」（soft instruction），讓 LLM 能萃取出與該使用者行為相關的世界知識；其次，它將知識融合形式化為一個帶有明確上限的最佳化問題，以 Lagrangian 原始-對偶法求解，從而只納入對推薦有益的知識，同時限制對行為訊號的潛在損害。  
針對不同 LLM 規模，研究團隊又設計了兩種訓練策略；在部署時，採用近線預計算與輕量級線上服務相結合的方案，以兼顧效能與延遲。  

 **在多個公共資料集與一個工業廣告平台上，LWGR 優於八種最強基線最高達 11.23%，並帶來 1.35% 的收入提升**  
實驗顯示，LWGR 在所有評測資料集上均顯著超越現有最佳方法；在大規模廣告場景中，該提升轉化為可觀的收入增長，證明其在真實產品中的實用價值。  

💡 **個性化知識的萃取必須與行為訊號保持平衡，受控融合是關鍵**  
研究指出，若知識萃取過於泛化或融合過度激進，將會掩蓋使用者的真實行為訊號；反之，透過 Lagrangian 約束明確界定允許的性能下降幅度，則能在保留行為信號的同時，有效注入與使用者興趣匹配的世界知識。這種「受控」而非「盲目」的融合機制，正是效能提升的核心所在。  

⚠️ **實驗主要聚焦於點擊率與收入等短期指標，長期使用者滿足度與模型穩定性尚需進一步觀察**  
雖然論文提供了豐富的離線與線上結果，但未詳細探討長期迭代對模型偏差的影響，亦未在多樣化的使用者族群上進行長期 A/B 測試。這些屬於未來工作的重要方向。  

🎯 **在實務上，可先嘗試使用軟指令來個性化知識萃取，並以 Lagrangian 原始-對偶法控制知識融合的幅度**  
對於工程師而言，這意味著：  
1. 為每位使用者或使用者群體建立可調的指令向量，而不是使用一套固定 prompt；  
2. 在知識併入推薦模型時，加入可調的拉格朗日乘數，以實時監控並限制對原始行為訊號的衝突；  
3. 依據模型大小選擇對應的訓練策略，並在服務端採用近線預計算以降低線上延遲。  

🔗 **論文連結**  
📝 LWGR: Lagrangian-Constrained Personalized World Knowledge for Generative Recommendation  
👤 Lingyu Mu, Hao Deng, Haibo Xing, Kaican Lin, Zhitong Zhu (Chinese Academy of Sciences; Alibaba International Digital Commerce Group)  
🔗 https://arxiv.org/abs/2605.18771  

你在推薦系統中是否也遇過「知識越多反而越不準」的困境？歡迎在留言區分享你的經驗與看法 👇  

#AI #推薦系統 #LLM #生成式推薦 #Lagrangian約束 #阿里巴巴 #中國科學院 #MachineLearning #廣告技術 #深度學習
