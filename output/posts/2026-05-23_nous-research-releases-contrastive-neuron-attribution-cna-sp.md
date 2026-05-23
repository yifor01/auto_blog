---
title: "Nous Research Releases Contrastive Neuron Attribution (CNA): Sparse MLP Circuit Steering Without SAE Training or Weight Modification"
source: MarkTechPost
url: https://www.marktechpost.com/2026/05/23/nous-research-releases-contrastive-neuron-attribution-cna-sparse-mlp-circuit-steering-without-sae-training-or-weight-modification/
score: 110
model: tencent/hy3-preview:free
generated_at: 2026-05-23T19:30:46.356133
---

📌 【Nous Research 最新研究】Contrastive Neuron Attribution (CNA)：無需 SAE 訓練即可精準操縱模型拒絕行為  

你以為模型的「拒絕」是訓練時才產出的？研究發現，這種能力其實早已藏在基礎模型中——只需調整極少數神經元就能打開或關閉它。  

🤔 **對齊訓練並未創造新結構，只是重新利用既有的神經網路**  
Nous Research 觀察到，負責區分有害與無害提示的後期 MLP 結構在未經任何微調的基礎模型中已經存在。對齊訓練（alignment fine‑tuning）並未產生新的電路，而是將這些既有神經元的功能轉變為一個稀疏且可被精準操控的「拒絕閘門」。  

🧪 **僅用前向傳播即可定位關鍵神經元**  
研究團隊首先準備兩組提示：一組為有害請求，另組為無害請求。對每組提示分別進行前向傳播，記錄每個 MLP 層在最後 token 位置的下投影激活值。接著計算每個神經元在兩組之間的平均激活差異  
\[
\delta_j^{\ell}= \text{mean}(激活於有害提示) - \text{mean}(激活於無害提示)
\]  
根據這個差異排名，他們發現僅需將最顯著的 0.1% MLP 神經元的激活設為零（即消融），在 Llama 與 Qwen 系列（從 1B 到 72B 參數）的多個指令模型上，拒絕率即可下降超過 50%，而生成品質（以 perplexity 或人工評分衡量）始終維持在 0.97 以上。  

💡 **與現有方法相比，CNA 更輕量且梯度自由**  
- **Contrastive Activation Addition (CAA)**：雖能透過殘差流的平均差異產生操縱向量，但會修改整層訊號，導致高強度操縱時輸出品質下降（重複詞、 incoherent 文字）。  
- **Sparse Autoencoders (SAE)**：可將激活分解為可解釋特徵，但需要額外的外部訓練且對激活噪聲敏感。  
- **CNA**：僅需前向傳播，無梯度、無輔助訓練、無迭代搜尋，即可定位稀疏且具因果影響的 MLP 神經元，實現「零權重修改」的行為操縱。  

⚠️ **目前僅聚焦於拒絕行為，泛用性尚待驗證**  
文件中所述實驗專注於有害 vs 無害提示的拒絕機制，尚未報告在其他任務（例如事實正確性、風格控制）上的表現。此外，所報告的結果基於 Llama 與 Qwen 系列模型，是否在其他架構上具有相同效果尚未提及。  

🎯 **對工程師的直接啟示**  
若您需要在不修改模型權重或訓練額外 SAE 的情況下，快速調整模型的安全或風格行為，CNA 提供了一種可直接透過前向傳播實現的工具：  
1. 準備兩組對比提示（目標行為 vs 基線行為）。  
2. 透過模型獲取 MLP 層激活，計算 per‑neuron 差異。  
3. 消融頂部稀疏神經元（例如 0.1%），即可在推理時顯著改變模型行為，同時保持高品質輸出。  

🔗 **論文連結**  
📝 Contrastive Neuron Attribution (CNA): Sparse MLP Circuit Steering Without SAE Training or Weight Modification  
👤 Nous Research Team（MarkTechPost 報導，作者 Asif Razzaq）  
🔗 https://www.marktechpost.com/2026/05/23/nous-research-releases-contrastive-neuron-attribution-cna-sparse-mlp-circuit-steering-without-sae-training-or-weight-modification/  

你是否曾嘗試用微調或外掛模組來改變模型的「拒絕」行為？CNA 這種「開關」式的神經元操縱或許能讓你的調整更精準、更輕量。歡迎在留言區分享你的想法或實驗經驗！  

#AI #LLM #Interpretability #NousResearch #CNA #ModelSteering #Llama #Qwen #機器學習 #深度學習
