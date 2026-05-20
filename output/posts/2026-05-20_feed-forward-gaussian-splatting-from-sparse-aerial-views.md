---
title: "Feed-Forward Gaussian Splatting from Sparse Aerial Views"
source: ChatPaper/Computer Vision and Pattern Recognition
url: https://arxiv.org/abs/2605.19949
score: 112
model: tencent/hy3-preview:free
generated_at: 2026-05-20T21:04:38.060269
---

📌 【HKUST(GZ) 最新研究】AnyCity：從稀疏航拍圖像重建城市 3D 高斯 splatting  

你以為用無人機拍幾張鳥瞰圖就能完整重建一座城市？實際上，建物立面常被遮住，導致傳統方法產生鬼影與扭曲。  

🤔 **航拍視角偏頂導致觀測不均衡，立面與遮蔽區域缺乏多視角支撐**  
稀疏航拍因為俯視與淺斜角度較多，屋頂與開放區域被重複觀測，而立面、遠方建築與被遮擋結構則缺少足夠的多視角資訊。現有的 feed‑forward 高斯 splatting 直接從稀疏輸出確定性表示，常產生鬼影、立面融化與紋理拉伸的問題。雖然有些方法引入偽視圖或影像生成先驅來補強，但它們難以明確區分可觀測的幾何與先驅產生的內容，易產生看似合理但彼此不一致的模型。  

🧪 **觀測驅動的幾何潛變量與腳手條件補全標記結合生成先驅**  
研究團隊提出 AnyCity 框架：首先預測一個由觀測支撐的幾何潛變量，以穩固可信的結構；接著使用腳手條件的航空補全標記，在弱約束區域產生一個經閘控制的殘差更新，最後進行高斯解碼。訓練階段透過 dense‑to‑sparse distillation 從密集視角重建傳遞結構線索，並採用航空適配的視訊擴散先驅提供細緻的城市外觀線索，透過同樣的閘控標記進行條件化。觀測保留目標確保最終表示仍與輸入支撐的幾何保持一致。推論時，AnyCity 能在單次前向傳遞中從稀疏航拍圖像直接重建最終的 3D 高斯場景。  

📊 **單次前向傳遞即可產生連貫的城市新視角合成，優於既有 feed‑forward 基線**  
在合成資料集、航拍領域資料集、UAV 紋理資料集以及真實場景上的實驗顯示，AnyCity 在新視角合成上相比先前的 feed‑forward 高斯 splatting 方法具有明顯提升，並能在秒級時間內完成推論。  

💡 **將可靠幾何與弱約束內容分離，避免先驅產生的不一致結構**  
核心貢獻在於將「觀測支撐的幾何」與「先驅驅動的內容」明確分離。透過幾何潛變量穩固可信結構，再以閘控的殘差更新處理缺乏多視角支撐的區域，這種設計減少了純生成先驅導致的空間不一致，使重建結果在保持視覺合理的同時也更符合實際幾何約束。  

⚠️ **目前實驗主要集中在合成、航拍領域、UAV 紋理及真實場景，對其他類型影像的表現尚未詳細說明**  
論文未提供針對極端稀疏、夜間或惡劣天氣影像的具體評估，因此該方法在更廣泛條件下的穩定性仍需後續工作進一步驗證。  

🎯 **適合無人機航拍快速重建城市模型，可用於虛擬現實、城市規劃與遙感應用**  
AnyCity 的單次前向推論特性使其適合於需要即時回饋的無人機作業流程；同時，幾何與外觀的分離設計也為後續編輯或半自動化的模型精練提供了明確的介面。  

🔗 **論文連結**  
📝 Feed-Forward Gaussian Splatting from Sparse Aerial Views  
👤 Dongli Wu, Zhuoxiao Li, Tongyan Hua, Yinrui Ren, Xiaobao Wei  
🏫 The Hong Kong University of Science and Technology (Guangzhou); Peking University; The Ohio State University  
🔗 https://arxiv.org/abs/2605.19949  

你認為此類觀測驅動的生成重建在未來的遙感或數位孿生應用中會有哪些潛力？歡迎在留言區分享你的見解 👇  

#AI #ComputerVision #GaussianSplatting #DroneMapping #HKUST #3DReconstruction #AnyCity #SyntheticData #UAV #SceneUnderstanding
