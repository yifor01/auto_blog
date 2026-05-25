---
title: "Good Token Hunting: A Hitchhiker's Guide to Token Selection for Visual Geometry Transformers"
source: ChatPaper/Computer Vision and Pattern Recognition
url: https://arxiv.org/abs/2605.23892
score: 106
model: tencent/hy3-preview:free
generated_at: 2026-05-25T20:52:09.745048
---

📌 【多校聯手】Good Token Hunting：視覺幾何Transformer減磅85%  

視覺幾何Transformer在多視圖3D重建中表現強大，但全域注意力的平方複雜度讓它在處理上百張圖像時變得緩慢且難以擴展。  

🤔 **一個簡單的兩階段策略就能突破瓶頸**  
論文提出先在幀層級進行互幀選擇（保留具多樣性的幀），再在所選幀內部進行 intra‑frame 選擇（根據全域注意力的entropy進行layer‑aware稀疏化），以減少每個query需要關注的key/value token數量。  

🧪 **專注於 token 數量的控制**  
研究設計圍繞「限制每個query在全域注意力中可交互的key/value token數量」展開，分兩個階段：  
1. **互幀選擇**：以多樣性為依據，挑選應該保留的幀，確保場景的廣泛覆蓋。  
2. ** intra‑frame 選擇**：在保留的幀內，根據全域注意力模式的entropy進行層級感知的稀疏化，進一步捨棄冗餘token。  

🔑 **速度提升超過85%，精度不降反增**  
在包含500張圖像的場景上，該方法使視覺幾何Transformer的運行速度提升超過85%，同時基線性能被維持甚至略微提升。這表明token選擇不僅是加速手段，也可能有助於提升代表力。  

💡 **多樣性與entropy是關鍵設計**  
分析顯示，互幀階段的多樣性策略能確保對場景的廣泛覆蓋；而 intra‑frame 階段則需要根據全域注意力的entropy來導向稀疏化，才能在不犧牲精度的前提下達到高效壓縮。  

⚠️ **僅證實於特定規模與場景，長期適用性待觀察**  
實驗主要針對500張圖像的多視圖場景進行；論文未提供更大規模或不同類型數據的結果，亦未探討該策略在其他Transformer變體或長序列任務中的泛化能力。  

🎯 **對工程師的直接啟發**  
- 在處理大量多視圖圖像時，可先嘗試以多樣性為準則篩選幀，再利用注意力entropy決定哪些內部token可被安全捨棄。  
- 專案網站已提供實作參考（https://zsh2000.github.io/good-token-hunting.github.io），方便直接移植到NeRF、MVS或其他視覺幾何管線。  

🔗 **論文連結**  
📝 Good Token Hunting: A Hitchhiker's Guide to Token Selection for Visual Geometry Transformers  
👤 Shuhong Zheng, Michael Oechsle, Erik Sandström, Marie‑Julie Rakotosaona, Federico Tombari  
🏫 University of Toronto & Vector Institute；Google；Technical University of Munich  
🔗 https://arxiv.org/abs/2605.23892  

你是否曾為處理上百張圖像的3D重建而頭疼？這種token選擇或許是下一步的加速關鍵。歡迎在留言區分享你的想法！  

#AI #ComputerVision #3DReconstruction #Transformer #Efficiency #UniversityOfToronto #Google #TUM #GoodTokenHunting
