---
title: "CRAFT: Clustered Regression for Adaptive Filtering of Training data"
source: ChatPaper/AI
url: https://arxiv.org/abs/2604.22693
score: 108
model: tencent/hy3-preview:free
generated_at: 2026-04-27T20:10:31.331548
---

📌 【Google 最新研究】三千三萬句對挑一組，微調質感不崩壞的秘密在哪？

你以為從 3300 萬句對中「隨便抽樣」就能省下微調成本？研究顯示，不對齊資料分布的濾選，可能讓模型在 BLEU 上直接掉 2 個點以上。

🤔 **大語料微調不是越貴越好，而是越準越好**

隨著訓練語料衝擊數千萬甚至上億句對，完整微調不僅昂貴，還常帶來冗餘與干擾。如何在有限算力下鎖定高品質子集，已成為序列到序列模型落地不可迴避的工程命題。

🧪 **分群加權與迴歸濾選的聯合設計**

CRAFT 針對 3300 萬 NLLB 英印平行句對進行訓練資料篩選，並以 LoRA 微調 mBART。方法先將來源語句透過 k-means 分群，依驗證集來源分布按比例分配預算，再於每個來源群內根據目標嵌入最小化條件期望距離進行選取。整套流程向量化無關，可在 CPU 上運行。

☑️ **CRAFT 拿下 43.34 BLEU，比 TSDS 高 2.13，且快 40 倍**

- BLEU：CRAFT 43.34 勝 TSDS 41.21  
- 速度：完整篩選在 CPU 上低於 1 分鐣完成  
- 對比 TAROT（45.61 BLEU）：CRAFT 僅花 26.86 秒，達到 2.8 倍速度優勢  

這意味在相近資源下，質量損失極小，但決策週期大幅縮短。

💡 **用分群逼近分布，而非用暴力逼近最佳**

CRAFT 的核心在於將聯合源目標分布拆解：先透過比例分群配額控制來源域偏移，再以目標嵌入的條件期望距離約束內部選取。理論上，比例分配可限制連續 KL 散度，殘差則由群直徑控制。這讓選出來的子集同時具備「分布代表性」與「目標一致性」。

⚠️ **英印翻譯與 LoRA 設定下的初步驗證**

目前評估侷限於單一語對（英印）、特定模型（mBART）與輕量微調（LoRA）；長期微調穩定性與跨語言泛化仍需進一步檢驗。

🎯 **先用分佈驅動濾選，再用精算投入微調**

- 資料篩選應優先對齊驗證分布，而非追求單點損失最小  
- 分群加權與迴歸目標結合，可在 CPU 階段就完成成本質感雙控  
- 對於百萬至千萬級語料，這類框架有機會成為標準前置步驟  

🔗 **論文連結**  
📝 CRAFT: Clustered Regression for Adaptive Filtering of Training data  
👤 Parthasarathi Panda, Asheswari Swain, Subhrakanta Panda (Google; BITS Pilani)  
🔗 https://arxiv.org/abs/2604.22693

你在專案中會怎麼平衡微調資料的「量」與「質」？歡迎分享你的篩選策略 👇

#AI #MachineLearning #DataEfficiency #Translation #Google #CRAFT #NLP
