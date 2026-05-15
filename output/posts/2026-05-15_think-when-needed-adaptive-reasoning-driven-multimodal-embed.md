---
title: "Think When Needed: Adaptive Reasoning-Driven Multimodal Embeddings with a Dual-LoRA Architecture"
source: ChatPaper/Information Retrieval
url: https://arxiv.org/abs/2605.14448
score: 114
model: tencent/hy3-preview:free
generated_at: 2026-05-15T20:19:51.177728
---

📌 自適應推理驅動的多模態嵌入  

你以為每次都要讓 AI 多思考才能得到好嵌入？其實對簡單輸入，額外推理反而會拉低效果。  

🤔 **簡單輸入已經足夠，額外推理反而有害**  
研究發現，對於易辨識的多模態樣本，判別式嵌入本身就能表現良好；盲目為每筆資料產生鏈式思維（CoT）不僅增加計算負荷，甚至可能誤導模型，導致檢索品質下降。  

🧪 **雙 LoRA 架構 + 自適應閘門**  
為解決此問題，團隊提出 Think When Needed (TWN)。在一個凍結的多模態主幹上，分別掛載推理適配器與嵌入適配器，形成雙 LoRA 結構；在兩適配器的介面處斷開梯度，以減少聯合優化時的梯度衝突，同時參數量僅比主幹多 3‑5%。此外，設計一個自我監督的路由閘門，根據每個輸入的特徵動態決定是否產生 CoT，從而在不需要推理時直接跳過，降低推理開銷。  

📊 **在 MMEB‑V2 78 任務上實現 SOTA，參數開銷僅增 3‑5%，推理 token 最多減半**  
實驗顯示，TWN 在 MMEB‑V2 的 78 個多模態嵌入基準上達到最新狀態（SOTA）的嵌入品質；與傳統全生成式 CoT 方法相比，其推理階段所需的 token 數最多可減少 50%。  

💡 **透過嵌入導向的 RL 優化推理品質，超越監督訓練**  
除了監督學習外，作者進一步探索以嵌入為回饋的強化學習（embedding‑guided RL），以提升所生成 CoT 的質量，使得在需要推理時的效果更優於純監督訓練的基線。  

⚠️ **僅驗證於公開基準，尚未在真實大規模檢索系統上長期測試**  
目前結果僅基於公開的 MMEB‑V2 基準；論文未說明該方法在真實產業級檢索服務（如億級圖文庫）上的長期穩定性與資源消耗。  

🎯 **對檢索系統工程師的啟示：只在需要時啟用推理，可同時提升品質與效率**  
若你正在構建多模態檢索管線，可考慮採用類似自適應閘門的機制：在簡單查詢上直接使用判別式嵌入，只有當模型不確定時才啟用推理適配器。這樣既能保持或提升檢索準確率，又能顯著降低推理成本與參數開銷。  

🔗 **論文連結**  
📝 Think When Needed: Adaptive Reasoning-Driven Multimodal Embeddings with a Dual-LoRA Architecture  
👤 Longxiang Zhang, Weilong Dai, Guanghao Zhang, Hao Jiang, Pipei Huang @ Alibaba Group  
🔗 https://arxiv.org/abs/2605.14448  

#AI #MultimodalEmbedding #LoRA #Reasoning #Alibaba #MMEB #檢索系統 #ParameterEfficientFineTuning
