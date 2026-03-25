---
title: "Unleashing Spatial Reasoning in Multimodal Large Language Models via Textual Representation Guided Reasoning"
source: ChatPaper/Computer Vision and Pattern Recognition
url: https://arxiv.org/abs/2603.23404
score: 106
model: gpt-4o-free
generated_at: 2026-03-25T19:44:05.771536
---

📌 【清華&上海AI Lab】TRACE：讓多模態大模型懂 3D 空間  

你以為給影片加個字幕就能讓 AI 理解空間嗎？實際上，現有多模態模型在 3D 空間推理上仍屢屢失敗。  

🤔 **多模態模型在 3D 空間推理上的瓶頸**  
現有 MLLM 能夠從圖像或影片中捕捉外觀特徵，但在需要構建環境的抽象結構、進行 allocentric（以環境為中心）空間推論時，常因缺乏結構化的 3D 表示而導致答案錯誤。這限制了它們在機器人導航、增強實境等場景的實用性。  🧪 **TRACE：以文字表徵引導空間推理的提示法**  
受認知理論中 allocentric 空間推理的啟發，研究團隊提出 TRACE（Textual Representation of Allocentric Context from Egocentric Video）。TRACE 是一種 prompting 方法，它引導 MLLM 在回答空間問題前，先產生包含 meta‑context、相機軌跡與詳細物件實體的文字描述，作為中間推理鏈。整個過程僅依賴提示工程，無需重新訓練模型。  

 **在 VSI‑Bench 與 OST‑Bench 上的持續提升**  在兩個專門評估 3D 空間問答的基準測試 VSI‑Bench 與 OST‑Bench 上，TRACE 在不同參數規模與訓練策略的 MLLM 骨幹上均顯示出較先前 prompting 策略更好的表現。改善幅度在各模型間具有一致性，說明該方法具有較好的泛化潛力。  

💡 **為什麼文字中介能幫助空間理解？**  
透過將 egocentric 視訊轉換為結構化的文字表示，模型得以在語言空間中進行更清晰的關係推理（例如「物件 A 在物件 B 左前方」）。這種中間表示減少了直接在高維視覺特徵上進行空間推論的難度，同時保留了必要的幾何資訊。實驗中的消融研究進一步證實， meta‑context、相機軌跡與實體細節三個組件皆對最終表現有正向貢獻。  

⚠️ **僅針對特定基準測試，泛化能力仍需觀察**  
現有結果主要來自 VSI‑Bench 與 OST‑Bench，這兩個基準聚焦於特定類型的 egocentric 視訊與空間問題。是否同樣有效於更開放的場景（例如戶外導航、複雜機械操作）仍需後續驗證。此外，文中未涉及 TRACE 在極長視訊或低幀率條件下的行為。  

🎯 **工程師可直接採用的提示技巧**  
若你正在構建多模態系統，且需要模型回答有關空間關係的問題，可嘗試在 Prompt 中加入類似 TRACE 的指令：讓模型先輸出「環境描述」（包含相機移動與物件位置），再基於該描述回答問題。此方法不改變模型權重，僅提升推論階段的語言中介，適合快速驗證與線上服務。  

🔗 **論文連結**  
📝 Unleashing Spatial Reasoning in Multimodal Large Language Models via Textual Representation Guided Reasoning  
👤 Jiacheng Hua, Yishu Yin, Yuhang Wu, Tai Wang, Yifei Huang (Tsinghua University; Shanghai AI Lab; The University of Tokyo)  
🔗 https://arxiv.org/abs/2603.23404  

你有在多模態專案中遇過空間推論的瓶頸嗎？歡迎在留言區分享你的經驗或嘗試 TRACE 的心得 👇  

#AI #Multimodal #SpatialReasoning #PromptEngineering #Tsinghua #ShanghaiAILab #CVPR #MLLM #3DUnderstanding #GenAI
