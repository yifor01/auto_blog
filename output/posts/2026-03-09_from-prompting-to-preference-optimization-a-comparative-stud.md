---
title: "From Prompting to Preference Optimization: A Comparative Study of LLM-based Automated Essay Scoring"
source: ChatPaper/Computation and Language
url: https://arxiv.org/abs/2603.06424
score: 106
model: arcee-ai/trinity-large-preview:free
generated_at: 2026-03-09T22:51:59.157131
---

📌 **從 Prompting 到 Preference Optimization：LLM 自動評分方法大亂鬥**

當 AI 老師開始批改英文作文，到底哪種方法最準確？最省錢？最穩定？

🤔 **為什麼 LLM 自動評分還要比較？**

大型語言模型重塑了自動評分 (AES) 領域，但過去的研究都只單獨測試一種方法，讓我們不知道：在英文為第二語言 (L2) 的寫作評分上，到底該選哪種 LLM 策略？

🧪 **四種方法的對決**

越南科學大學團隊設計了一個統一的 IELTS Writing Task 2 測試平台，比較四種主流 LLM 評分方法：

1. **Encoder-based 分類微調** - 傳統的微調方式
2. **零/少樣本 Prompting** - 直接用提示讓模型評分
3. **指令微調 + RAG** - 結合知識增強的指令學習
4. **SFT + DPO + RAG** - 結合監督微調、偏好優化和知識增強

 **準確度、成本、穩定性的權衡**

研究發現，不同方法在三個關鍵維度上呈現明顯取捨：

- **準確度**：DPO 組表現最佳，F1-Score 達到 93%
- **成本**：Prompting 最便宜，但準確度較低
- **穩定性**：RAG 整合能提升對不同題型的適應性

💡 **最佳組合浮現**

綜合表現最佳的配置是：**k-SFT + RAG**，達到最高的整體評分表現。

⚠️ **這不是單純的技術比較**

這是第一個針對英文 L2 寫作的統一比較研究，提供了實務應用時的決策依據。對於教育科技公司、線上學習平台，甚至是學校的 AI 評分系統建置，這份研究提供了重要的參考價值。

🎯 **實務啟示**

- 如果需要高準確度且預算充足，選擇 DPO 整合方案
- 如果追求成本效益，可以考慮 Prompting 加少量微調
- RAG 整合能提升對不同題型的適應性

🔗 **論文連結**
📝 From Prompting to Preference Optimization: A Comparative Study of LLM-based Automated Essay Scoring
👤 Minh Hoang Nguyen, Vu Hoang Pham, Xuan Thanh Huynh, Phuc Hong Mai, Vinh The Nguyen
🏫 University of Science, Ho Chi Minh City; Vietnam National University, Ho Chi Minh City
🔗 論文：arxiv.org/abs/2603.06424
💻 程式碼：github.com/MinhNguyenDS/LLM_AES-EnL2

你覺得 AI 評作文老師，準確度多重要？歡迎分享你的想法 👇

#AI #教育科技 #自然語言處理 #機器學習 #LLM #自動評分 #IELTS
