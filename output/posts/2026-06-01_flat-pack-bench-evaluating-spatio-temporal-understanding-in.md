---
title: "Flat-Pack Bench: Evaluating Spatio-Temporal Understanding in Large Vision-Language Models through Furniture Assembly"
source: HuggingFace Daily Papers
url: https://huggingface.co/papers/2605.21625
score: 88
model: tencent/hy3-preview:free
generated_at: 2026-06-01T22:29:30.990738
---

📌 **Flat‑Pack Bench 評估 VLM 時空推論**  

你以為多模態大模型已經能看懂圖片和文字的互動？新基準顯示，它們在家具組裝的時空推論上仍顯著落後。  
這意味著，即使模型能描述靜態場景，也難以追蹤物體隨時間的移動與變形。  

🤔 **時空推論是多模態理解的瓶頸**  
現有的 VLM 評估多聚焦於靜態圖像問答或簡單的影像描述，卻缺乏對物體在時間序列中如何移動、旋轉或組裝的細緻測試。隨著機器人、AR/VR 與智慧製造等應用對動態空間推論的需求增加，這個缺口成為限制模型實用性的關鍵因素。  

🧪 **以家具組裝為基準的細粒度評估**  
Flat‑Pack Bench 透過一組家具組裝的影像序列（或影片）設計任務，要求模型判斷在每一步驟中，哪些零件應該如何移動、旋轉或連接，以及預測後續的組裝狀態。此基準提供了明確的評估協議與對應的資料集，專門針對「空間變化」與「時間依賴」兩個維度進行檢驗。  

📊 **VLM 在細粒度時空推論上顯著落後**  
在該基準上的實驗顯示，目前主流的大型視覺語言模型在細粒度 spatio‑temporal reasoning 與 tracking 能力上皆有顯著限制。具體來說，模型在預測後續組裝步驟或辨識錯誤的零件定位時，準確率遠低於人類基準，凸顯其在動態空間理解上的不足。  

💡 **為什麼靜態理解不等於動態追蹤**  
分析發現，模型在該任務上較依賴靜態特徵（如零件的形狀與顏色），而缺乏有效的時間建模機制來捕捉零件間的相對運動與因果關係。此結果說明，單靠強化靜態視覺語言對齊並不足以提升模型在需要推論時間演變的任務中的表現。  

⚠️ **基準僅涵蓋家具組裝場景，泛化性有待觀察**  
目前的評估集中在特定的家具組裝情境，資料規模與場景多樣性仍有限。因此，模型在此基準上的表現未必能直接推廣至其他時空推論情境（例如人體動作、車輛交通或工業機械臂）。未來工作需要擴充更多領域的時空資料集，以全面檢驗模型的泛化能力。  

🎯 **改進時空建模是提升 VLM 實用性的關鍵**  
- 在模型架構中加入明確的時間模組（如 3D CNN、Transformer 時間注意狀態或狀態空間模型）  
- 以影片或序列資料進行多任務預訓練，強化空間與時間的聯合表示  
- 在下游應用（機器人規劃、AR 指導、智慧製造）中優先考慮能同時處理靜態與動態線索的模型  

🔗 **論文連結**  
📝 Flat‑Pack Bench: Evaluating Spatio‑Temporal Understanding in Large Vision-Language Models through Furniture Assembly  
👤 作者：未詳  
🔗 論文：https://huggingface.co/papers/2605.21625  

你在使用多模態模型時，是否也遇到過「看得懂圖片，卻跟不上動作」的情況？歡迎在留言區分享你的經驗與看法 👇  

#AI #VisionLanguage #SpatioTemporalReasoning #FlatPackBench #HuggingFace #多模態學習 #時空理解 #機器視覺 #技術研究
