---
title: "Efficient Generative Retrieval for E-commerce Search with Semantic Cluster IDs and Expert-Guided RL"
source: ChatPaper/Information Retrieval
url: https://arxiv.org/abs/2605.14434
score: 120
model: tencent/hy3-preview:free
generated_at: 2026-05-15T20:15:48.953375
---

📌 【阿里巴巴】電商搜尋新法：語義Cluster ID＋專家導向RL  

你以為生成式檢索只能在實驗室跑？阿里巴巴的最新研究證明，它已成為電商搜尋的主力軍，貢獻超過七成的購買行為。  

🤔 **電商搜尋的瓶頸：規模巨大、延遲嚴格、需與排名目標對齊**  
傳統多階段檢索在面對龐大且頻繁更新的商品目錄時，難以同時滿足低延遲與與下游排名目標的一致性。生成式檢索雖能將多階段統一為端到端模型，但在真實電商場景中仍面臨計算複雜度與稀疏獎勵的挑戰。  

🧪 **層次語義ID + 專家導向RL：讓生成式檢索在電商場景中落地**  
研究團隊提出兩個核心組件：  
- **CQ‑SID（Category‑and‑Query constrained Semantic ID）**：結合類別感知與查詢‑商品對比學習，利用剩餘量編碼變分自編碼器（Residual Quantized VAE）將商品編碼為階層語義簇標識，顯著壓縮 beam search 空間。  
- **EG‑GRPO（Expert‑Guided Group Relative Policy Optimization）**：在稀疏獎勵環境下，透過注入真實樣本（expert samples）來穩定群體相對策略優化的訓練，使生成式召回能更好地對齊下游排名目標。  

📊 **實驗數據：離線提升兩成以上，線上GMV破點一五**  
- 在 TmallAPP 搜尋日誌的離線實驗中，CQ‑SID 相較於 RQ‑VAE 基線，語義點擊命中率提升 **26.76%**，個人化點擊命中率提升 **11.11%**，同時 beam search 大小減少 **50%**。  
- 加入 EG‑GRPO 後，多目標表現進一步提升。  
- 線上 A/B 測試顯示，GMV 增長 **+1.15%**，UCTCVR 增長 **+0.40%**。  
- 生成式召回渠道在實際流量中佔比：**曝光 50.25% 點擊 58.96% 購買 72.63%**，顯示其已成為搜尋系統的重要組成。  

💡 **語義層級減少搜索空間，專家樣本穩定RL訓練**  
透過階層語義標識，相似商品被映射到相近的簇，使得 beam search 需要探索的候選集大幅縮小；同時，專家樣本的注入提供了有梯度的反饋信號，緩解了稀疏獎勵導致的訓練不穩問題，使策略學習更有方向性。  

⚠️ **實驗主要基於單一平台、特定時間窗**  
離線結果僅基於 TmallAPP 搜尋日誌；線上增益來自特定期間的 A/B 測試。跨平台適用性與長期穩定性仍需進一步驗證。  

🎯 **給工程師的實務啟示**  
- 在大型動態商品庫中，考慮使用類別‑查詢對比學習與残差量化 VAE 生成階層語義 ID，以減少生成式檢索的計算開銷。  
- 在獎勵稀疏的場景下，可嘗試透過少量真實標註樣本來導引強化學習訓練，提升策略與下游目標的一致性。  
- 此框架已證明可同時提升點擊率與交易額，適合作為電商搜尋的召回補充模組。  

🔗 **論文連結**  
📝 Efficient Generative Retrieval for E-commerce Search with Semantic Cluster IDs and Expert-Guided RL  
👤 Jianbo Zhu, Xing Fang, Jing Wang, Mingmin Jin, Bokang Wang (Taobao & Tmall Group of Alibaba)  
🔗 https://arxiv.org/abs/2605.14434  

你的電商搜尋系統是否已嘗試過生成式召回？歡迎在留言區分享經驗或疑問 👇  

#AI #檢索技術 #電商搜尋 #生成式檢索 #阿里巴巴 #強化學習 #SemanticID #RL #GMV提升 #UCTCVR
