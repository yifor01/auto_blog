---
title: "How and What to Imagine? Visual Thinking in Unified Multimodal Models for Cross-View Spatial Reasoning"
source: arXiv
url: http://arxiv.org/abs/2605.27310v1
score: 97
model: tencent/hy3-preview:free
generated_at: 2026-05-27T21:07:48.242346
---

📌 全景思考+VDrop  

你以為讓模型「想圖」就能解決跨視角空間推理嗎？實際上，它們常常直接忽略那些中間圖像，只靠文字推理。這篇論文提出了一個簡單的訓練技巧，強制模型真的去看它自己畫的圖。  

🤔 **跨視角空間推理對視覺語言模型仍是薄弱環節**  
現有的視覺語言模型 (VLM) 在需要跨視角幾何推理的任務上表現不佳，因為它們傾向於純粹在語言空間中推論，因而遺失了細緻的幾何資訊。先前的「思考圖像」做法嘗試透過產生中間圖像來補充這些幾何線索，但後續工作發現模型經常忽略這些視覺證據，導致預測仍依賴輸入視圖而非思考圖像。  

🧪 **在統一多模態模型中引入 View Dropout (VDrop) 並比較三種思考圖像風格**  
研究聚焦於統一多模態模型 (UMM)，這類模型原生支援交錯的圖像‑文字生成。為了讓模型在回答時必須使用思考圖像，作者提出了訓練時的介入手法 **View Dropout (VDrop)**：在預測答案的 token 範圍中隨機遮蔽一個輸入視圖的部分，但在生成思考圖像的 token 時保持該部分完整。這樣的設計迫使模型在預測答案時必須參考它自己生成的思考圖像。  
接著，作者將思考圖像的形式視為一個可學習性與資訊量的 trade‑off 問題，比較了三種渲染方式：  
- **top‑down**（俯視）  
- **panoramic**（全景）  
- **point‑matching**（點對應）  

所有模型在合成場景上進行訓練，之後在五個真實世界的跨域基準測試上進行評估。  

📊 **全景思考圖像 + VDrop 是唯一同時具備可學習性與資訊量的配置**  
實驗結果顯示，只有 **panoramic 視覺思考 + VDrop** 同時達到高資訊量（能提供足夠的幾何線索）與高可學習性（模型能有效利用該線索），並在所有五個跨域基準上取得最佳泛化表現。其他兩種思考圖像要麼資訊不足（模型仍忽略），要麼難以學習（訓練不穩定），因而無法在未見場景上持續提升性能。  

🔍 **為何全景視角更有效？**  
全景渲染保留了輸入視圖之間的更廣泛空間關係，因而提供了更完整的幾何上下文。配合 VDrop，模型被迫在答案預測階段參考這個完整的視覺 trace，從而減少對純語言推論的依賴。這種「資訊豐富且易於被模型利用」的組合正好落在作者提出的 learnability‑informativeness 平衡點上。  

⚠️ **研究限制**  
- 訓練資料僅限於合成場景，真實世界的複雜紋理與光照變化可能未被完全涵蓋。  
- 評估僅基於五個已有的跨域基準，是否適用於其他空間推理任務或更大規模的基準尚需進一步驗證。  
- 未探討 VDrop 在不同模型規模或不同訓練時長下的穩定性。  

🎯 **對實務的啟示**  
對於致力於提升空間推理能力的研究團隊，這項結果提供了一個明確且易於實施的食譜：在統一多模態模型的訓練流程中加入 View Dropout，並使用全景風格的思考圖像作為中間表示。此做法不需要額外的結構改動，僅是一個訓練時的遮蔽策略，即可在跨視角推理任務上獲得顯著的泛化提升。  

🔗 **論文連結**  
📝 How and What to Imagine? Visual Thinking in Unified Multimodal Models for Cross-View Spatial Reasoning  
👤 Qian Yang, Ankur Sikarwar, Huy Le, Le Zhang, Zhuan Shi  
🔗 http://arxiv.org/abs/2605.27310v1  

你在開發多模態系統時，是否也曾嘗試讓模型「思考圖像」？歡迎在留言區分享你的經驗或疑問 👇  

#AI #Multimodal #SpatialReasoning #VDrop #UnifiedMultimodalModels #Research #CVPR2025 #arXiv
