---
title: "ATLAS: Agentic or Latent Visual Reasoning? One Word is Enough for Both"
source: ChatPaper/Computer Vision and Pattern Recognition
url: https://arxiv.org/abs/2605.15198
score: 109
model: tencent/hy3-preview:free
generated_at: 2026-05-15T20:29:36.108093
---

📌 【Meta AI】ATLAS：一個詞同時當作「工具」與「隱藏狀態」的視覺推理新框架  

你以為視覺推理必須先生成中間圖像或呼叫外部工具？一個單一的離散詞卻能同時兼具兩種優勢。  

🤔 **視覺推理的兩條路徑各有短板**  
直接在推理過程中生成圖像雖直觀，但計算成本高且架構複雜；另一種做法是透過程式碼或工具呼叫的「agentic」推理，雖靈活卻會因外部執行而產生上下文切換延遲；最後是「latent」推理，透過可學習的隱藏嵌入進行推理，雖免除圖像生成，但泛化能力有限且在自回歸並行訓練上難以穩定。這些限制促使研究者尋求一種能同時取其長、避其短的方案。  

🧪 **單一離散詞即可兼具 agentic 與 latent 功能**  
ATLAS 提出「functional token」的概念：每個 token 都內化了一種視覺操作，卻不需要額外的視覺監督，且仍是標準詞彙表中的普通離散詞，可透過一般的 next-token prediction 生成。這意味著在推理過程中，模型不必產生冗長的中間圖像，也不必依賴外部工具呼叫，僅透過 token 本身即可完成既具代理行為又具隱藏狀態特徵的視覺推理。為進一步解決 functional token 在強化學習階段出現稀疏的問題，論文提出 Latent‑Anchored GRPO（LA‑GRPO），以靜態加權的輔助目標「錨定」這些 token，提供更強的梯度更新，使訓練更穩定。  

📊 **在具有挑戰性的基準測試上表現優於既有方法**  
實驗顯示，ATLAS 在多個視覺推理基準上達成了更好的成績，同時保持了模型決策的可解釋性——每一步推理都可以追溯到對應的 functional token，讓研究者能清楚看到模型究竟在執行哪種視覺操作。  

💡 **功能統一帶來的啟示**  
此設計表明，agentic 與 latent 兩種視覺推理範式其實可以透過同一種離散符號來統一，無需改動現有的監督微調（SFT）或強化學習（RL）管線，也無需新增額外的架構模組。對於未來的視覺推理研究，這種「一詞多用」的思路或許提供了一條更簡潔、更易於擴充的道路。  

⚠️ **目前仍屬探索階段，實際影響有待觀察**  
論文強調 ATLAS 的概念新穎且與現有訓練流程相容，但其真實世界的應用效果與社區接受度仍在發展中，後續需要更大規模的驗證才能判斷其長遠價值。  

🔗 **論文連結**  
📝 ATLAS: Agentic or Latent Visual Reasoning? One Word is Enough for Both  
👤 Ziyu Guo, Rain Liu, Xinyan Chen, Pheng‑Ann Heng (Meta AI & The Chinese University of Hong Kong)  
🔗 https://arxiv.org/abs/2605.15198  

你認為這種「一詞雙役」的設計會在未來的多模態模型中扮演什麼角色？歡迎在留言區分享你的看法 👇  

#AI #VisualReasoning #MetaAI #ATLAS #MachineLearning #ComputerVision #RL #SFT #技術趨勢
