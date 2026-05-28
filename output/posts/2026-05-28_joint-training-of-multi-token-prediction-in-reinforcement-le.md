---
title: "Joint Training of Multi-Token Prediction in Reinforcement Learning via Optimal Coefficient Calibration"
source: HuggingFace Daily Papers
url: https://huggingface.co/papers/2605.28184
score: 85
model: tencent/hy3-preview:free
generated_at: 2026-05-28T21:44:29.550014
---

📌 【強化學習+多Token預測：係數校準】

你以為強化學習只靠獎賞訊號就能提升推理能力？最新工作表明，將多Token預測納入訓練並透過最佳係數校準，竟能在數學推理基準上帶來 modeste 的效能提升。

🤔 **強化學習需要更多訊號來提升推理**  
純靠可驗證獎賞的強化學習（RL from Verifiable Rewards）在數學推理任務上常面臨樣本效率低與探索困難的問題。研究者開始探索是否可以透過額外的自監督目標——多Token預測，來為強化學習提供更豐富的反饋訊號，從而改善 joint training 的表現。

🧪 **透過係數校準聯合訓練兩個目標**  
論文提出一種「最佳係數校準」機制：在同一個訓練步驟中，同時最小化來自可驗證獎賞的強化學習損失與多Token預測損失，並透過學習或解析的方式動態調整兩者的權重係數。這樣的設計讓兩個目標可以共同影響模型參數的更新，而不需手動調超參數或進行階段式訓練。

 **在數學推理基準上觀察到 modeste 提升**  
實驗顯示，使用該係數校準策略的模型在數學推理基準上相較於僅使用強化學習或僅使用多Token預測的基線，均有可量化的改善。提升幅度屬於 modeste 程度，並未達到突破性的躍升，但證明了兩種訊號可以透過簡單的校準方式有效互補。

💡 **係數校準是關鍵：避免單一目標主導訓練**  
進一步分析發現，若未進行校準，強化學習損失往往會因其稀疏與高方差而被多Token預測損失掩蓋，導致模型在獎賞引導上的學習變得無效。透過最佳係數，兩個損失能保持相近的梯度規模，使得模型同時受益於獎賞導向的探索與多Token預測所提供的密集語言模式訊號。

⚠️ **實驗未公開程式碼，改善幅度有限**  
該研究未釋放訓練程式碼或詳細的超參數設定，僅提供概念驗證結果。此外，觀察到的效能提升屬於 modeste，且實驗主要聚焦在特定的數學推理基準，尚未在更廣泛的強化學習或語言模型任務上進行驗證，因而其直接的實務影響仍屬有限。

🎯 **係數校準可作為未來混合目標訓練的參考方案**  
對於希望結合強化學習與自監督目標（如多Token預測）的研究團隊來說，這項工作提供了一種簡易且無需額外搜尋超參數的校準思路。在缺乏公開程式碼的情況下，可先嘗試以驗證獎賞損失的梯度範圍作為參考，手動調整兩個目標的權重，觀察是否能獲得類似的 modeste 收益。

🔗 **論文連結**  
📝 Joint Training of Multi-Token Prediction in Reinforcement Learning via Optimal Coefficient Calibration  
🔗 https://huggingface.co/papers/2605.28184  

你是否曾嘗試將強化學習與其他自監督目標混合訓練？歡迎在留言區分享你的經驗或疑問 👇

#強化學習 #多Token預測 #係數校準 #數學推理 #AI研究 #HuggingFacePapers #MachineLearning
