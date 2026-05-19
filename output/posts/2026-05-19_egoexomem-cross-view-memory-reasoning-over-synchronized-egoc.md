---
title: "EgoExoMem: Cross-View Memory Reasoning over Synchronized Egocentric and Exocentric Videos"
source: ChatPaper/Computer Vision and Pattern Recognition
url: https://arxiv.org/abs/2605.18734
score: 117
model: tencent/hy3-preview:free
generated_at: 2026-05-19T20:28:43.306592
---

📌 EgoExoMem：跨視記憶推理  
你以為只看第一人稱視角就能記住空間嗎？  
研究顯示，單一視角的記憶在複雜任務中會遺失關鍵線索。  
但結合第三人稱視角會怎樣？接著看實驗如何揭示跨視角記憶的真正價值。  

🤔 **單一視角記憶不足以支撐完整時空推理**  
以往的具身智能研究多依賴第一人稱（egocentric）影像進行記憶與推理。然而，人類在回憶事件時會同時採用「參與者」與「旁觀者」兩種視角。這種雙視角的互補是否能提升空間‑時間推理的準確度，成為本文探討的核心問題。  

🧪 **2.6K 個跨視角選擇題與同步雙視角影像**  
研究團隊建構了 EgoExoMem 基準，包含 2.6K 道高品質選擇題，涵蓋八種時間、空間與跨視角問答類型。所有問題均基於同步的第一人稱與第三人稱視角影像。為支援雙視角檢索，他們提出訓練免費的 E²-Select 幀選擇方法：根據相關性分配預算，並對每個視角採用 k-DPP 抽樣，以處理視角不對稱與跨視角時間一致性的問題。  

📊 **雙視角互補，但現有多模態大語言模型表現仍遠低於人類水準**  
實驗顯示，第一人稱與第三人稱視角提供互補的記憶線索。然而，現有的多模態大語言模型在該基準上的最佳表現僅達 55.3%。相比之下，E²-Select 在幀選擇與檢索基線上達成 58.2% 的最佳狀態表現，顯示該方法能有效利用雙視角資訊。  

💡 **問題敘述與答案依據的視角偏好衝突凸跨視角推理的挑戰**  
進一步分析發現，問題的敘述方式與答案所依據的視角常存在系統性偏好衝突。例如，某些問題敘述偏向第一人稱視角，但正確答案則需要第三人稱視角的資訊才能驗證。這種視角不匹配正是跨視角記憶推理難點的重要指標。  

⚠️ **僅考慮同步視角與選擇題形式**  
該基準目前僅使用同步的第一人稱與第三人稱視角影像，且評估以選擇題為主。未涵蓋異步視角或更開放式的生成任務，長期效果及端到端模型的訓練潛力仍需後續工作探討。  

🎯 **對多模態視覚理解系統的實務啟示**  
- 在需要同時參考第一人稱與第三人稱視角的場景（如機器人導航、增強實境），可直接採用訓練免費的 E²-Select 進行幀選擇，提升記憶檢索效能。  
- 設計跨視角推理模型時，應注意問題敘述與答案依據的視角一致性，以減少偏好衝突導致的錯誤。  

🔗 **論文連結**  
📝 EgoExoMem: Cross-View Memory Reasoning over Synchronized Egocentric and Exocentric Videos  
👤 Ruiping Liu, Junwei Zheng, Yufan Chen, Di Wen, Shaofang Quan  
🔗 https://arxiv.org/abs/2605.18734  

你是否曾在使用第一人稱視角的設備時，感到缺少「全景」的理解？歡迎在留言區分享你的經驗與看法 👇  

#AI #ComputerVision #Egocentric #Exocentric #Multimodal #KIT #ETHZurich #Oxford #EgoExoMem #VideoUnderstanding
