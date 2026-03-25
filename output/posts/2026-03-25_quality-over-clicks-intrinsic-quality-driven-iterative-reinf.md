---
title: "Quality Over Clicks: Intrinsic Quality-Driven Iterative Reinforcement Learning for Cold-Start E-Commerce Query Suggestion"
source: ChatPaper/Computation and Language
url: https://arxiv.org/abs/2603.22922
score: 101
model: gpt-4o-free
generated_at: 2026-03-25T19:51:15.214144
---

📌 【Alibaba 最新研究】冷啟動電商查詢建議，點擊率不是唯一答案？

你以為提升點擊率就是提升用戶體驗的關鍵嗎？在沒有任何點擊記錄的全新商品或新市場裡，傳統的 CTR 驅動模型往往失效——這時候，查詢的「品質」才是真正的勝負手。

🤔 **點擊率驅動在冷啟動場景中失靈**

現有對話系統普遍依賴大型語言模型搭配點擊率（CTR）預測模型來產生 Query Suggestion（QS）。然而，CTR 模型需要大量線上點擊資料才能有效訓練，當系統面臨全新商品、新類目或新地區時，這些點擊訊息稀少甚至不存在，導致建議品質無法得到保證。作者提出：是否可以直接用查詢本身的內在品質作為導向，繞過對點擊的依賴？

🧪 **以 answerability、事實性與資訊增益作為獎勵的迭代強化學習框架**

研究團隊設計了 **Cold-EQS**，一種專為冷啟動電商查詢建議而設的迭代強化學習（RL）方法。他們將三個內在品質指標作為獎勵函式：  
- **Answerability**（查詢是否能被正確回答）  
- **Factuality**（查詢所涉及的資訊是否符合事實）  
- **Information Gain**（查詢能帶來多少新的有用資訊）  

在每次迭代中，模型先產生一組候選查詢，透過不確定度估計從缺乏點擊訊息的線上用戶查詢中挑選出「難樣本」與「樣糊樣本」，再利用上述品質獎勵對 QS 模型進行優化。為支援離線訓練與評估，他們同時發布了 **EQS‑Benchmark**，收錄了 16,949 條真實線上用戶查詢。

🚀 **線上實驗顯著提升 chatUV +6.81%**

離線基準上的實驗顯示，使用內在品質獎勵的 Cold-EQS 在多項評估指標上優於傳統 CTR 驅動基礎模型。更值得關注的是，線上 A/B 測試結果表明，該框架使 **chatUV（每日活躍聊天用戶數）** 提升了 **6.81%**，顯示離線品質優化能夠正向轉化為線上使用者參與度的實質增長。

💡 **品質導向比點擊導向更適合冷啟動情境**

結果表明，當點擊訊息稀缺時，直接優化查詢的 answerability、事實性與資訊增益，能夠在不依賴大規模點擊資料的情況下，持續產出更具使用價值的建議。這意味著，在電商搜尋或對話系統的早期階段，投資於「查詢本身的品質」可能比盲目追求點擊率更具長期價值。

⚠️ **論文未詳細說明長期穩定性與跨語言適用性**

雖然離線與線上實驗均顯示正向相關，但文中未特別探討 Cold-EQS 在長期使用中的表現穩定性，亦未說明該方法在多語言或多區域電商場景中的直接適用性。這些方面仍需後續工作進一步驗證。

🎯 **對工程師的實務建議**

- 在冷啟動或點擊訊息稀少的場景，考慮將內在品質指標（如 answerability、事實性、資訊增益）納入強化學習的獎勵函式。  
- 利用不確定度採樣策略，從無點擊的真實用戶查詢中挑選難樣本，可有效提升模型對邊界案例的適應力。  
- 建構類似 EQS‑Benchmark 的離線評估集，有助於在上線前先驗證品質導向的改善效果。

🔗 **論文連結**  
📝 Quality Over Clicks: Intrinsic Quality-Driven Iterative Reinforcement Learning for Cold-Start E-Commerce Query Suggestion  
👤 Qi Sun, Kejun Xiao, Huaipeng Zhao, Tao Luo, Xiaoyi Zeng @ Alibaba International Digital Commercial Group  
🔗 https://arxiv.org/abs/2603.22922

你在電商搜尋或對話系統中，是否也曾因缺點擊數據而苦惱？歡迎留言分享你的看法或實作經驗 👇

#AI #強化學習 #電商搜尋 #QuerySuggestion #Alibaba #ColdStart #CTR #ChatUV #NLP #機器學習
