---
title: "GLeVE: Graph-Guided Lesion Grounding with Proposal Verification in 3D CT"
source: ChatPaper/Computer Vision and Pattern Recognition
url: https://arxiv.org/abs/2605.22619
score: 106
model: tencent/hy3-preview:free
generated_at: 2026-05-22T20:47:45.406476
---

📌 GLeVE：圖引導病灶定位，連結放射報告與3D CT  

🎣 放射報告描述與CT體積如何精準對齊？這是臨床解讀可驗證的關鍵瓶頸。  

🤔 語意‑空間落差阻礙現有方法  
現有報告輔助或視覺‑語言定位多依賴詞彙層面對齊或密集像素監督，導致病灶層級的對應有限，定位精度不足。  

🧪 圖引導與八進樹細化的設計  
GLeVE 將每個病灶描述視為語義原子，透過關係感知圖推理編碼器官歸屬、屬性及病灶間關係，產生區別性病灶查詢；同時採用解剖先驗的區域級生成與驗證，確保一對一的文本‑病灶對應，並以八進樹遞迴細化逐步改善邊界。  

 在 AbdomenAtlas 3.0 上的表現  
實驗顯示 GLeVE 在分割準確度與病灶層級定位上，均優於傳統多模態基礎模型與報告監督基線，獲得一致的提升。  

💡 圖推理與階層細化的關鍵洞察  
圖結構能捕捉病灶之間的解剖與語義關係，使查詢更具區別性；八進樹的多分辨率遞迴則在保持全局解剖先驗的同時，逐步收斂病灶邊界，減少對密集像素標註的依賴。  

⚠️ 實驗資料來源與程式碼公開度有限  
評估僅在單一腹部 CT 資料集 AbdomenAtlas 3.0 進行，且目前未見完整程式碼公開，限制了直接復現與廣泛應用的評估。  

🎯 對醫療 AI 系統的啟示  
在需要將自由文字報告與三維影像對齊的場景中，結合圖推理與階層細化可提升定位可靠性；未來可探索在其他身體部位或多模態報告上的遷移潛力。  

🔗 論文連結  
📝 GLeVE: Graph-Guided Lesion Grounding with Proposal Verification in 3D CT  
👤 Shuo Jiang, Yuhao Hong, Chunbo Jiang, Weihong Chen, Huangwei Chen  
🏫 Zhejiang Key Laboratory of Space Information Sensing and Transmission; Hangzhou Dianzi University; Zhejiang University; Tsinghua University; Zhejiang University School of Medicine  
🔗 https://arxiv.org/abs/2605.22619  

#AI #MedicalImaging #ComputerVision #CT #GLeVE #AbdomenAtlas #深度學習 #醫療影像
