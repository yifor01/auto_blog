---
title: "PDCR: Perception-Decomposed Confidence Reward for Vision-Language Reasoning"
source: ChatPaper/Computation and Language
url: https://arxiv.org/abs/2605.13467
score: 108
model: tencent/hy3-preview:free
generated_at: 2026-05-14T20:43:43.717088
---

📌 【PDCR】分解信賞提升視覺語言推理  

你以為讓模型在每一步都給予信心分數就能提升視覺語言推理？事實上，這種做法在視覺與文字混合的任務中可能反而讓訓練信號失真。  

🤔 **視覺語言推理的訓練困境**  
強化學習中的可驗證獎勵（RLVR) 過去多依賴稀疏的結果回饋。近期研究發現，若以模型內在的信心增長作為細粒度獎勵，能在純文字推理中提供步驟層級的引導，無需額外外部模型。然而，當任務同時包含稀疏的視覺感知與密集的文字推理時，直接使用這種全域信心獎勵會導致「混合誘導信號衰減」：視覺步驟的訓練訊號被大量的文字步驟統計上扭曲，從而降低學習效果。  

🧪 **未監督的技能分解與視覺依賴分數**  
本研究首先提出一種未監督的技能分解方法。透過模型內部的**視覺依賴分數（Visual Dependence Score）** 來量化每個解決步驟對視覺資訊的依賴程度。接著，利用聚類演算法將步驟劃分為感知（perception）與推理（reasoning）兩個技能群Cluster。這樣的劃分使得原本異質的任務結構變得可分別處理。  

🚀 **內群正規化的分解優勢**  
在獲得感知與推理兩個Cluster後，PDCR 分別在各自內部對信心增長進行優勢（advantage) 正規化。這種**群內正規化**確保了每種類型步驟都能獲得適切尺度的訓練訊號，避免了全域正規化所帶來的訊號稀釋問題。實驗顯示，PDCR 在多個視覺語言推理基準上均優於傳統的全域獎勵 formulation 與稀疏獎勵基線，提供了更穩定且具平衡性的訓練信號。  

💡 **關鍵洞察：視覺與文字需分別獎勵**  
研究指出，視覺感知步驟的信心變化通常較為稀疏且幅度較小，而文字推理步驟則較密集且變化較大。若將兩種步驟放在同一個分布中進行正規化，視覺訊號會被文字訊號掩蓋。透過先依視覺依賴分數劃分技能，再分別正規化，PDCR 讓模型在學習視覺特徵時不會被文字主導的梯度所干擾，從而提升整體推理表現。  

⚠️ **研究限制**  
- 目前的實驗主要聚焦在現有的視覺語言推理基準，長期或跨域的泛化能力尚未探討。  
- 視覺依賴分數的計算依賴於模型內部的特徵表示，不同架構可能需要調整。  
- 未在此工作中針對具體的 Agentic 或互動式視覺語言系統進行驗證。  

🎯 **實務啟示**  
- 在設計以信心為基礎的獎勵函式時，先檢查任務是否包含感知與推理兩種不同密度的子步驟。  
- 若存在顯著的異質性，可考慮使用未監督的聚類或依賴分數來分離訊號來源，再分別進行優勢正規化。  
- 此方法不需要額外的外部模型或標註，僅需透過模型自身的信心輸出即可實踐，適合直接納入現有的 RLVR 訓練管線。  

🔗 **論文連結**  
📝 PDCR: Perception-Decomposed Confidence Reward for Vision-Language Reasoning  
👤 Hee Suk Yoon, Eunseop Yoon, Ji Woo Hong, SooHwan Eom, Gwanhyeong Koo  
🏫 Korea Advanced Institute of Science and Technology (KAIST); University of Illinois at Urbana-Champaign (UIUC); Microsoft Research Asia (MSRA)  
🔗 https://arxiv.org/abs/2605.13467  

你在視覺語言模型的訓練中是否也遇過「視覺步驟學不起來」的情況？歡迎在留言區分享你的經驗或想法 👇  

#AI #VisionLanguage #ReinforcementLearning #KAIST #UIUC #MicrosoftResearch #MultimodalReasoning #PDCR #RLVR
