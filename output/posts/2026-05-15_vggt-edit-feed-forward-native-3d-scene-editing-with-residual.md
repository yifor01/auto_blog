---
title: "VGGT-Edit: Feed-forward Native 3D Scene Editing with Residual Field Prediction"
source: ChatPaper/Computer Vision and Pattern Recognition
url: https://arxiv.org/abs/2605.15186
score: 106
model: tencent/hy3-preview:free
generated_at: 2026-05-15T20:35:47.953477
---

📌 【VGGT-Edit】Feed‑forward 原生 3D 場景編輯  

你以為編輯 3D 場景一定要先改單張圖片再投射回去？這種 2D‑lifting 流程常產生模糊紋理與幾何不一致，卻是目前多數方法的默認做法。  

🤔 **直接在 3D 空間裡編輯才能保持結構穩定**  
現有的 feed‑forward 重建模型雖能一次前向生成複雜環境，但對人類文字指令的反應仍然有限。若只在 2D 圖像上編輯再抬升，缺乏空間感知，易導致跨視圖的紋理散失與形狀扭曲。  

🧪 **深度同步文字注入 + 殘差位移頭**  
VGGT‑Edit 在骨幹網路中加入 depth‑synchronized text injection，使語義指令與空間姿勢對齊。接著經過一個 residual transformation head，直接預測 3D 幾何位移，在 deform 場景的同時保持背景穩定。訓練使用多項目標函數，同時強幾何精度與跨視圖一致性。為驗證方法，團隊構建了 DeltaScene Dataset——一個經過自動化管線與 3D 一致性過濾以確保 ground‑truth 品質的大規模資料集。  

🚀 **較 2D‑lifting 基線更銳利、更一致、近乎即時**  
實驗顯示 VGGT‑Edit 在物件細節銳利度、多視圖一致性上明顯優於既有方法，且保持近乎即時的推論速度，適合互動式編輯場景。  

💡 **關鍵在於「以殘差場引導變形」而非「完全重新生成」**  
該框架不嘗試從零重建整個場景，而是學習一個微小的殘差位移場。這樣的設計讓編輯操作聚焦於使用者指定的區域，同時保留未被編輯部分的幾何與紋理，因而能避免傳統 2D‑lifting 帶來的跨視圖漂移。  

⚠️ **僅針對靜態場景編輯，動態物件與長時序一致性尚未探討**  
目前的研究聚焦於單幀靜態場景的文字驅動編輯，未涵蓋會隨時間變形的物體或長視頻編輯的穩定性，這也是未來可延伸的方向。  

🎯 **工程上可先嘗試殘差場預測的思路，優先保證背景不受影響**  
若需快速、可控的 3D 場景編輯，可參考 VGGT‑Edit 的做法：先將文字指令與深度資訊同步注入，再利用殘差頭預測位移場進行局部變形。這種「最小修改」的策略在需要即時回饋的 AR/VR 或內容創作管線中具備實用價值。  

🔗 **論文連結**  
📝 VGGT-Edit: Feed-forward Native 3D Scene Editing with Residual Field Prediction  
👤 Kaixin Zhu, Yiwen Tang, Yifan Yang, Renrui Zhang, Bohan Zeng (Peking University; Tencent; CUHK; Shanghai AI Lab; NTU; Zhongguancun Academy; Beijing Key Lab of Data Intel. & Security)  
🔗 https://arxiv.org/abs/2605.15186  
📚 發表於 CVPR (Computer Vision and Pattern Recognition)  

你有嘗試過直接在 3D 空間裡用文字編輯場景嗎？歡迎在留言區分享你的經驗或想法 👇  

#3D编辑 #VGGTEdit #FeedForward #CVPR #ARVR #深度学习 #Tencent #北京大学 #香港中文大学 #上海人工智能实验室 #NTU #DeltaSceneDataset #残差场 #即时推理 #内容创作 #AI研究
