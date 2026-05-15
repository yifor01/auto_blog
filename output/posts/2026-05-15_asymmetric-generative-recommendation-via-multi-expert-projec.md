---
title: "Asymmetric Generative Recommendation via Multi-Expert Projection and Multi-Faceted Hierarchical Quantization"
source: ChatPaper/Information Retrieval
url: https://arxiv.org/abs/2605.14512
score: 113
model: tencent/hy3-preview:free
generated_at: 2026-05-15T20:24:55.213566
---

📌 **非對稱生成式推薦：雙瓶頸破解**  
【Tsinghua University × Tencent】  

你以為把商品當作文字來生成就能推薦準確？實際上，這種對稱設計藏著兩個隱形瓶頸——輸入端的資訊損失與熱門偏斜，以及輸出端的離散目標不精確。  

🤔 **對稱生成式推薦的雙階段瓶頸**  
現有 Generative Recommendation (GenRec) 模型把項目離散化為 Semantic ID，同時作為 Transformer 的輸入與預測目標。這種對稱方式在實務上會產生兩個問題：(1) 輸入瓶頸——離散量化導致細緻語義流失，且頻繁項目主導表示；(2) 輸出瓶頸——離散目標的不精準限制了監督訊號的品質。這兩個瓶頸共同制約了模型對少見項目的泛化與推薦的準確度。  

🧪 **非對稱綜合框架：MSP 與 MHQ**  
為了切斷這兩個瓶頸的耦合，論文提出 **AsymRec**，採用連續‑離散非對稱架構：  
- **Multi‑expert Semantic Projection (MSP)**：多個專家投射將連續嵌入映射到 Transformer 隱空間，各專家專注不同語義子空間，從而保留豐富細節並提升對尾部項目的泛化。  
- **Multi‑faceted Hierarchical Quantization (MHQ)**：透過多視角、多層次的離散量化並在其中加入語義正則化，構建高容量且結構化的離散目標空間，避免維度崩塌同時保留細粒度區分。  

這兩個模組分別負責輸入端的語義保存與輸出端的監督品質提升，使得模型能夠在不增加參數量的情況下獲得更好的表示與預測。  

🚀 **平均領先 15.8% 的實驗表現**  
在多個公開基準測試上，AsymRec 相較於目前最先進的生成式推薦模型，**平均提升 15.8%**。改善尤為顯著於長尾項目與冷啟動情境，說明非對稱設計確實緩解了輸入與輸出兩端的資訊瓶頸。  

💡 **關鍵洞察：將輸入與輸出分開才能各取所需**  
傳統對稱設計迫使同一套離散表示同時負責「理解項目」與「生成預測」，導致兩端需求互相衝突。AsymRec 透過 MSP 讓輸入端保留連續語義的豐富度，而 MHQ 則為輸出端提供更具區分力且訊號豐富的離散目標。這種「專業分工」的思路，也是未來處理類似序列生成任務時值得考慮的方向。  

⚠️ **研究限制：僅報告平均提升，細部實驗設定未透露**  
論文未提供具體的資料集名稱、基線模型版本或超參數細節，僅報告了平均性能提升。因此無法判斷改善在特定場景下的穩定性，亦未討論模型在極端穩疏或噪聲輸入下的行為。  

🎯 **對工程師的實務建議**  
- 若你的推薦系統正面臨長尾項目覆蓋不足或熱門偏斜問題，可嘗試將輸入嵌入透過多專家投射映射，而離散目標採用階層化、多視角量化策略。  
- 在等待官方程式碼發布前，可先參考現有的「專家混合」與「積樹量化」實作，逐步向非對稱連續‑離散架構過渡。  
- 持續監控離散目標的語義一致性，避免量化過度導致維度崩塌。  

🔗 **論文連結**  
📝 Asymmetric Generative Recommendation via Multi-Expert Projection and Multi-Faceted Hierarchical Quantization  
👤 Bin Huang, Xin Wang, Junwei Pan, Yongqi Zhou, Yifeng Zhou (Tsinghua University; Tencent)  
🔗 https://arxiv.org/abs/2605.14512  

你在推薦系統中是否也遇過「輸入理解」與「輸出預測」互相拖後腿的情況？歡迎在留言區分享你的經驗與想法 👇  

#AI #RecommendationSystem #GenerativeModel #Tsinghua #Tencent #MachineLearning #InformationRetrieval #AsymRec #MSP #MHQ
