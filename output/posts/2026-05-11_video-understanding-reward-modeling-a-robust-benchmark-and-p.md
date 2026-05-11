---
title: "Video Understanding Reward Modeling: A Robust Benchmark and Performant Reward Models"
source: ChatPaper/Computer Vision and Pattern Recognition
url: https://arxiv.org/abs/2605.07872
score: 117
model: tencent/hy3-preview:free
generated_at: 2026-05-11T20:25:51.451562
---

📌 **影像理解獎勵模型新基準**

你以為 AI 已經能看懂影像並給出正確回饋？事實上，缺乏可靠的評估基準讓這項技術停滯不前。

🤔 **影像理解獎勵模型的空白點**  
多模態獎勵模型在文字與圖像領域已有顯著進展，但影像理解方面卻因缺乏穩定的評估基準與高品質偏好資料而進展緩慢。這意味著研究者無法以一致的方式衡量模型的好壞，也難以大規模訓練出可靠的獎勵函式。

🧪 **統一框架：基準、資料與模型三管齊下**  
論文提出一個涵蓋基準設計、資料建構與獎勵模型訓練的統一框架。具體包括：  
- **Video Understanding Reward Bench (VURB)**：包含 2,100 組偏好對，每組附帶平均 1,143 token 的長鏈思考推理追蹤，採用多數決評估，涵蓋一般、長片段與導向推理的影像任務。  
- **Video Understanding Preference Dataset (VUP-35K)**：透過完全自動化的管線建構，提供 35,000 筆高品質偏好樣本，作為獎勵模型的監督訓練資料。  
- **VideoDRM 與 VideoGRM**：分別為判別式與生成式獎勵模型，在 VURB 與既有的 VideoRewardBench 上均達到最新狀態（SOTA）。進一步分析顯示，VUP-35K 不僅提升獎勵模型的表現，也增強模型的推理能力；在 best-of‑N 測試時擴容下，兩種模型都帶來顯著增益。

💡 **關鍵洞察：資料品質決定模型上限**  
實驗證明，大規模、自動產出且具備長鏈思考追蹤的偏好資料（VUP-35K）是提升獎勵模型效能與推理深度的關鍵。缺乏這樣的資料時，即便模型架構先進，也難以在複雜影像理解任務上獲得穩定的回饋信號。

⚠️ **研究限制**  
- 基準與資料目前聚焦於特定類型的影像任務（一般、長片段、導向推理），其他影像領域的適用性尚待驗證。  
- 偏好資料是經完全自動化管線產出，雖然規模大，但可能仍含有自動化標註的偏差。  
- 本文主要報告判別式與生成式兩種獎勵模型的表現，其他形式的獎勵函式（例如基於對比學習的變體）未在此探討。

🎯 **實務啟示**  
- 從事影像理解、生成或具代理能力（agentic）系統的工程師，可直接採用 VURB 作為評估標準，以獲得可比較且具說服力的結果。  
- 利用 VUP-35K 或類似的自動化偏好資料管線，可快速為自身的獎勵模型建立高品質監督訊號。  
- 在部署階段，考慮採用 best-of‑N 測試時擴容策略，以進一步放大 VideoDRM/VideoGRM 帶來的效能提升。

🔗 **論文連結**  
📝 Video Understanding Reward Modeling: A Robust Benchmark and Performant Reward Models  
👤 Yuancheng Wei, Linli Yao, Lei Li, Haojie Zhang, Hao Zhou (South China University of Technology; Peking University; The University of Hong Kong; Tencent)  
🔗 https://arxiv.org/abs/2605.07872  

你目前在影像理解專案中是否也遇過評估不一致的問題？歡迎在留言區分享你的經驗與看法 👇

#AI #影像理解 #RewardModeling #RLHF #VURB #VUP-35K #多模態 #Tencent #科技研究
