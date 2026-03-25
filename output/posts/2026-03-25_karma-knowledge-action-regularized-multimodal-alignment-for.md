---
title: "KARMA: Knowledge-Action Regularized Multimodal Alignment for Personalized Search at Taobao"
source: ChatPaper/Information Retrieval
url: https://arxiv.org/abs/2603.22779
score: 115
model: gpt-4o-free
generated_at: 2026-03-25T19:28:25.991708
---

📌 **KARMA：知識行動雙贏**  

你以為把大型語言模型直接塞進個性化搜尋就能提升點擊率？實際上，這樣做可能讓模型的語義知識「崩解」，反而傷害效果。  
研究團隊發現，單純用 discriminative 目標微調 LLM 會導致 Semantic Collapse，例如出現 attention 「sink」現象，使模型失去泛化能力。  
他們提出 KARMA 框架，以語義重建作為僅在訓練時的正則化項，同時保留動作目標與語義知識。  
在 Taobao 上線實驗中，KARMA 不僅降低了語義崩解，還帶來可量測的點擊與排名提升。

🤔 **知識與行動的衝突是個性化搜尋的瓶頸**  
LLM 擁有豐富的語義先驗，但直接將其用於下一項預測等個性化任務時，預訓練知識與特定動作對齊的目標會產生對抗。經驗顯示，僅以動作為目標的訓練會導致語義崩解，削弱模型的泛化能力，進而無法提升個性化搜尋效果。

🧪 **以 Taobao 搜尋系統為實驗平台的 ablation 研究**  
團隊在真實的 Taobao 搜尋流程中，將 KARMA 與僅動作目標、僅語義重建等基線進行對比。他們設計了兩個互補的訓練目標：  
1. **history‑conditioned semantic generation** —— 讓模型的輸出貼近其原始的 next‑token 分佈，以保住預訓練語義；  
2. **embedding‑conditioned semantic reconstruction** —— 強制興趣向量必須能被解碼回有意義的語義，防止向量退化為無意義的點。  
透過這兩個目標的聯合優化，KARMA 同時 optimizes next‑interest embedding（Action）並維持 semantic decodability（Knowledge）。

📊 **KARMA 顯著改善動作指標與語義保真度**  
- 在消融實驗中，單純加入語義解碼性（semantic decodability）即可帶來最高 **+22.5 HR@200** 的提升。  
- 完整的 KARMA 框架在線上排名階段達成 **+0.25 CTR AUC**，預排名階段 **+1.86 HR**，召回階段 **+2.51 HR**。  - 部署後僅增加極少的推論開銷，帶來 **+0.5%** 的 Item Click 提升。  
此外，透過 attention‑sink 分析確認，KARMA 有效減輕了語義崩解現象。

💡 **語義重建是橋接知識與行動的關鍵**  
KARMA 的核心思想是把語義重建當作僅在訓練時的正則化項，而不是另一個獨立的目標。這樣的設計讓模型在學習個性化動作時，仍必須保持能夠重建出有意義語義的能力，從而避免知識被「覆寫」而產生泛化失靈。實際上，高分使用者傾向於先讓 LLM 產生候選再追問理解（即用 AI 建立理解），而低分使用者則較可能直接讓 AI 取代思考。這與 KARMA 所強調的「知識‑行動平衡」形成呼應。

⚠️ **僅在 Taobao 排名階段驗證，長期效果與其他平台尚待探索**  - 實驗主要基於 Taobao 的搜尋流程，未報告在其他電商或內容平台的表現。  
- 主要評估指標為點擊率與 Hit Ratio，長期使用者滿意度或行為變化未在文中涉及。  
- KARMA 目前僅在排名階段部署，前階段（如預篩選、召回）的開銷與適配性仍需進一步評估。

🎯 **工程師可嘗試以語義重建作為訓練正則化，平衡 LLM 知識與個性化目標**  
- 在將 LLM 微調用於排序或推薦時，可加入類似「embedding‑conditioned semantic reconstruction」的項，確保興趣向量仍可解碼為有語義的表示。  
- 若資源允許，可採用「history‑conditioned semantic generation」讓模型輸出貼近其原始語言分佈，進一步減少知識遺失。  
- 線上服務時，監控 attention 分布是否出現 sink 現象，可作為語義崩解的早期警訊。  
- 最後，務必在真實流量上做 A/B 測試，觀察點擊率、HR 以及可能的長期使用者行為變化，才能確認改善是否具備持續性。

🔗 **論文連結**  📝 KARMA: Knowledge-Action Regularized Multimodal Alignment for Personalized Search at Taobao  
👤 Zhi Sun, Wenming Zhang, Yi Wei, Liren Yu, Zhixuan Zhang @ Taobao&Tmall Group of Alibaba  🔗 https://arxiv.org/abs/2603.22779  

你在個性化搜尋或推薦系統中，是否也遇到過「知識‑行動」的張力？歡迎在留言區分享你的經驗與看法 👇  

#AI #LLM #個性化搜尋 #推薦系統 #Taobao #KARMA #InformationRetrieval #機器學習 #Alibaba #CTR提升
