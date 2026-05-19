---
title: "Towards Sustainable Growth: A Multi-Value-Aware Retrieval Framework for E-Commerce Search"
source: ChatPaper/Information Retrieval
url: https://arxiv.org/abs/2605.17994
score: 119
model: tencent/hy3-preview:free
generated_at: 2026-05-19T20:26:03.137016
---

📌 【阿里巴巴最新研究】多價值感知檢索框架提升新品GMV  

你以為提升搜尋曝光就能帶來長期成長？實際上，熱門商品的馬太效應可能讓新品永遠被埋沒。  

🤔 **熱門商品壟斷曝光，新品成長受抑制**  
大型電商平台的搜尋系統傾向於呈現已經流行的商品，這種「馬太效應」使得新品難以獲得足夠曝光。現有的冷啟動模型在訓練目標與線上業務指標之間存在錯位，且缺乏有效衡量商品長期成長潛力的機制。  

🧪 **結構化樣本與搜索級聯訊號的多價值生成檢索**  
論文提出 **GrowthGR** 框架，包含兩個核心模組：  
1. **ItemLTV（Item Long‑term Transaction Value Prediction）** – 透過反事實推斷（counterfactual inference）量化單次使用者互動所帶來的長期價值增量。  
2. **MultiGR（Multi‑Value‑Aware Generative Retrieval）** – 建立在 semantic‑ID‑based 生成檢索架構之上，利用帶有搜索級聯訊號的結構化樣本，採用 **Multi‑Value‑Aware Policy Optimization (MoPO)** 訓練範式，使模型同時對齊短期交易價值與由 ItemLTV 提供的長期成長潛力。  

🔬 **核心發現：新品 GMV 提升 5.3%，整體搜索 GMV 增長 0.3%**  
在淘寶的線上環境進行 A/B 測試後，GrowthGR 相較於基線達成：  
- 新品 GMV（ Gross Merchandise Value ）提升 **5.3%**  
- 整體搜尋 GMV 提升 **0.3%**  
線上分析進一步顯示該框架對整體生態系統價值具有正向影響。  

💡 **深入分析：反事實推斷估算長期價值，多價值政策優化平衡短長期**  
ItemLTV 透過反事實推論 isolate 出單次點擊、購買等互動對未來交易的貢獻，使系統能夠在訓練階段「看到」商品的長期潛力。  
MultiGR 則將這些長期價值估計作為獎勵的一部分，透過 MoPO 同時優化多階段線上指標（曝光、點擊、轉換、長期成長），避免只追求短期轉換而犧牲新品的長期價值。  

⚠️ **研究限制：僅在單一平台驗證，長期效果尚需追蹤**  
- 實驗僅在淘寶／天貓的生產環境中進行，是否能推廣至其他電商平台或不同商品類別尚需驗證。  
- 本次線上測試主要關注短期 A/B 結果（數週至數月），對新品長期生命週值的持續影響仍需更長時間的觀測。  
- 文中未公開具體模型規模、訓練資料量等實作細節，限制了外部直接復現。  

🎯 **實務啟示：將長期價值估計納入檢索訓練，可同時提升新品曝光與整體收益**  
- 在搜尋或推薦系統中，納入基於反事實推斷的長期價值預估，有助於打破純粹以短期轉換為目標的馬太效應。  
- 採用多價值感知的政策優化（如 MoPO）能夠在訓練目標中顯式平衡短期交易與長期成長，從而在不犧牲整體收入的前提下提升新品曝光。  
- 對於電商或內容平台的工程團隊，這套框架提供了一種可落地的思路：先量值長期價值，再以多目標強化學習對齊多階段線上指標。  

🔗 **論文連結**  
📝 Towards Sustainable Growth: A Multi-Value-Aware Retrieval Framework for E-Commerce Search  
👤 Yifan Wang, Yixuan Wang, YiDan Liang, Qiang Liu, Fei Xiao @ Taobao & Tmall Group of Alibaba  
🔗 https://arxiv.org/abs/2605.17994  

你的電商搜尋策略是否也在考慮長期價值？歡迎在留言區分享你的看法與經驗 👇  

#AI #InformationRetrieval #Ecommerce #Alibaba #Taobao #SearchEngine #RecommendationSystem #GMV #ColdStart #MatthewEffect
