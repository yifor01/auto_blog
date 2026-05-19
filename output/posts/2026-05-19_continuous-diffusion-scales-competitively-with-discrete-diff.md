---
title: "Continuous Diffusion Scales Competitively with Discrete Diffusion for Language"
source: ChatPaper/Computation and Language
url: https://arxiv.org/abs/2605.18530
score: 108
model: tencent/hy3-preview:free
generated_at: 2026-05-19T20:49:17.617675
---

📌 【NVIDIA 最新研究】連續擴散模型可與離散擴散競爭  

你以為連續擴散語言模型一定不如離散版嗎？最新研究顯示，只要改變訓練方式，它的擴展能力可以追上主流方法。  

🤔 **連續擴散被認為擴展性不足**  
近年來，離散擴散語言模型（Discrete DLM）在擴展法則與效能上佔據主導地位。相對地，連續擴散語言模型（Continuous DLM）常被視為在相同計算預算下難以匹敵，這讓研究團隊懷疑這種看法是否源於模型架構或訓練目標的不匹配，而非內在的擴展上限。  

🧪 **對齊 Plaid 架構並以似然訓練重建**  
研究團隊先取 Plaid（一種基於似然的連續擴散語言模型），將其架構對齊現代離散 DLM 的設計元素（例如 Transformer 块、嵌入方式），得到 RePlaid。在此統一的實驗環境下，他們首次測量了連續 DLM 的擴展法則，並與 autoregressive 模型、Duo、MDLM 等基線進行對比。  

📈 **RePlaid 的擴展表現與生成品質**  
- 在相同計算預算下，RePlaid 與 autoregressive 模型的效能差距僅約 **20×**，顯著縮小了此類模型與傳統自回歸方法的鴻溝。  
- 相較於 Duo，RePlaid 在使用更少參數的情況下仍能取得更好的 perplexity。  
- 在過訓練（over‑trained） regime 中，RePlaid 能超越 MDLM。  
- 在 OpenWebText 基準上，RePlaid 達成 **PPL 22.1**，為目前連續 DLM 的新州-of-the-art，且生成樣品在人工評估中表現更佳。  

💡 **似然訓練帶來的理論優勢**  
團隊進一步分析發現：  
1. 透過最小化 ELBO 的變異來優化噪聲排程，自然會產生隨時間線性增加的交叉熵（information loss），這使得去噪難度在整個過程中較均勻分布，無需額外的時間重新參數化。  
2. 以似然目標優化詞嵌入，會誘導嵌入空間形成更具結構的幾何形狀，這被認為是提升模型似然的主要動力。  

⚠️ **研究的主要限制**  
- 實驗主要集中在 OpenWebText 上，尚未在更大規模或多樣化的語料上驗證。  
- 模型規模與訓練步數的絕對數字僅在相對比較中給出，未提供完整的絶對計算成本基線。  
- 理論分析假設了理想的噪聲排程優化，實際訓練中可能受到優化器與批次大小的影響。  

🎯 **對工程師的實務啟示**  
- 若資源受限且希望避免離散化帶來的詞彙表開銷，連續擴散模型在經過架構對齊與似然訓練後，已具備具競爭力的擴展潛力。  
- 在設計新擴散語言模型時，可考慮先檢查噪聲排程的變異與嵌入的似然驅動，這兩個因素在實驗中帶來最顯著的提升。  
- 仍建議在目標任務上進行實證比較，因為不同領域的數據特性可能會影響理論優勢的落實。  

🔗 **論文連結**  
📝 Continuous Diffusion Scales Competitively with Discrete Diffusion for Language  
👤 Zhihan Yang, Wei Guo, Shuibai Zhang, Subham Sekhar Sahoo, Yongxin Chen (NVIDIA; Cornell; Georgia Tech; UW-Madison; MBZUAI-IFM)  
🔗 https://arxiv.org/abs/2605.18530  

你有在專案中嘗試過連續擴散語言模型嗎？歡迎在留言區分享你的經驗或疑問 👇  

#AI #DiffusionModels #LanguageModeling #NVIDIA #Research #MachineLearning #LLM #GenerativeAI
