---
title: "FlexDraft: Flexible Speculative Decoding via Attention Tuning and Bonus-Guided Calibration"
source: ChatPaper/Computation and Language
url: https://arxiv.org/abs/2605.20022
score: 126
model: tencent/hy3-preview:free
generated_at: 2026-05-20T20:50:04.712574
---

📌 【FlexDraft】靈活推測式解碼：透過 Attention Tuning 與 Bonus-Guided Calibration 提升大模型吞吐  

你以為推測式解碼只能在小批次時發揮效果？研究顯示，當批次變大時，傳統平行方案的吞吐反而會崩塌——這正是 FlexDraft 想要突破的瓶頸。  

🤔 **推測式解碼的批次擴展瓶須**  
傳統的序列式推測式解碼在起草與驗證之間會產生互相等待；平行式則嘗試在一次前向傳播中同時完成兩者，但在大批次情況下，因「獎勵 token」與「接受長度」的不確定性導致起草與驗證不匹配，吞吐提升難以持續。  

🧪 **透過三種輕量設計實現彈性適應**  
FlexDraft 在不重新訓練完整模型的前提下，提出三個關鍵機制：  
- **Attention Tuning**：僅對最後幾層的注意力投影進行微調（針對 mask token），保持自回歸路徑凍結，以極少可訓練參數產出高品質草稿。  
- **Bonus-guided Calibration**：以一個輕量 MLP 根據已解出的獎勵 token 對草稿 logits 進行校準，減少因獎勵 token 不確定性造成的驗證錯配。  
- **Flex Decoding**：依據批次大小動態切換——小批次時採用平行起草‑驗證，大批次時改為序列式起草然後驗證，並根據草樣信心度調整驗證長度，避免重複計算。  

🔥 **在不同批次下保持品質與吞吐的平衡**  
實驗表明，FlexDraft 能在小批次維持高接受率的同時，在大批次場景下避免吞吐隨批次增大而崩塌；因僅微調注意力投影並使用輕量校準網路，對原始模型的分布無損失（lossless）。  

💡 **關鍵在於「可調式」而非「固定方案」**  
與需要額外頻繁預訓練或導致品質下降的既有平行方法不同，FlexDraft 的彈性來自於：  
1. 只調整極少數參數的注意力模組，保留目標模型的原始分布；  
2. 以獎勵 token 為條件的校準，直接對應不確定性來源；  
3. 依實際批次大小與草樣信心切換執行模式，從根本上消除冗餘的等待與狀態交換。  

⚠️ **樣本與實驗範圍僅限於論文所報告的設定**  
論文未提供具體資料集大小、基線模型具體版本或長期部署穩定性等細節；因此，對於極端規模（如超大型 MoE）或特殊硬體平台的適用性仍需進一步驗證。  

🎯 **工程師可直接將其納入推論服務管線**  
- 無需重新訓練巨量模型，只需針對最後幾層注意力投影進行微調並加入少量 MLP 校準模組。  
- 透過 Flex Decoding 的動態切換，可在流量波動大的線上服務中自適應調整吞吐與延遲。  
- 適合已經使用推測式解碼（如 Speculative Sampling、Medusa 等）的系統，作為低成本的升級路徑。  

🔗 **論文連結**  
📝 FlexDraft: Flexible Speculative Decoding via Attention Tuning and Bonus-Guided Calibration  
👤 Yaojie Zhang, Jianuo Huang, Junlong Ke, Yuhang Han, Yongji Long (EPIC Lab, SJTU; UESTC; HUST; Tsinghua University; HKUST(GZ); Shanghai AI Laboratory)  
🔗 https://arxiv.org/abs/2605.20022  

你在大模型服務中是否遇過批次增大時吞吐變慢的問題？歡迎在留言區分享你的經驗或對此類彈性解碼方案的看法 👇  

#AI #LLM #SpeculativeDecoding #AttentionTuning #FlexDraft #推論優化 #生成式AI #SJTU #上海AI實驗室 #機器學習
