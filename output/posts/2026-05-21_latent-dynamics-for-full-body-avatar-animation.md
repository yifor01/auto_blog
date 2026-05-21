---
title: "Latent Dynamics for Full Body Avatar Animation"
source: ChatPaper/Computer Vision and Pattern Recognition
url: https://arxiv.org/abs/2605.21478
score: 98
model: tencent/hy3-preview:free
generated_at: 2026-05-21T21:10:16.490133
---

📌 **潛在動態改善衣物 Avatar**  

同一姿勢，寬鬆衣物卻能呈現無數種擺動——因為它的運動取決於歷史、慣性與接觸。  

🤔 **姿勢驅動無法解釋寬鬆衣物的變形**  
現有的神經渲染全身 Avatar 能根據姿勢產出高品質的新視角，但寬鬆衣物、褶皺等動態細節往往僅憑姿勢無法預測。同一姿勢可能對應多種衣物狀態，因為衣物的運動還受到過去姿勢的慣性、與身體或環境的接觸影響。  

🧪 **在九段日常運動序列上學習殘餘動態**  
研究團隊在九段捕捉到的日常運動（涵蓋多種寬鬆服飾）上，將姿勢條件的 3D 高斯 Avatar 與一個 Transformer‑based 解碼器結合。他們引入一個「殘餘 latent」，用以捕捉姿勢驅動訊號之外的時間外觀與幾何變化。在推理時，一個學得的 latent dynamics 模型根據短暫的姿勢歷史與前一個 latent 狀態來演化該殘餘 latent。每次更新被分解為驅動力、恢復力與耗散力三個分量。  

💡 **歷史相關、時間連貫的衣物運動**  
該模型能從不同的初始狀態產出多樣且合理的衣物運動軌跡，並因力的分解而暴露出如剛度等可控參數。實驗結果（量化指標與感知使用者研究）表明，相較於近期的資料驅動基線，所提出的方法在動畫品質上有明顯提升，且額外運算成本可忽略不計。  

⚠️ **僅驗證日常運動、未探索極端服裝或長時間序列**  
評估範圍限於九段捕捉到的日常運動，未涉及更複雜的服裝結構（如多層、厚重材質）或較長時間的動作序列。模型對極端姿勢或快速變化的環境接觸仍需進一步驗證。  

🎯 **適用於即時 VR/AR 與遊戲場景的輕量化方案**  
因為潛在動態模型只需少量額外運算，可直接嵌入現有的姿勢驅動 Avatar 系統，適合對即時性與視覺保真度皆有需求的應用。開發者可透過調整恢復力與耗散力的參數，快速調整衣物的「柔軟度」或「阻尼」效果，而無需重新訓練完整的物理模擬。  

🔗 **論文連結**  
📝 Latent Dynamics for Full Body Avatar Animation  
👤 Shichong Peng, Chengxiang Yin, Fei Jiang, Zhongshi Jiang, Lingchen Yang (Simon Fraser University; Codec Avatars Lab, Meta)  
🔗 https://arxiv.org/abs/2605.21478  

你認為這種「力分解」的潛在表示方式，是否能在你的專案中取代傳統的布料模擬？歡迎留言討論 👇  

#Avatar #衣物動態 #NeuralRendering #Transformer #VR #AR #Meta #SimonFraserUniversity #ComputerGraphics #CVPR2026
