---
title: "FHAvatar: Fast and High-Fidelity Reconstruction of Face-and-Hair Composable 3D Head Avatar from Few Casual Captures"
source: ChatPaper/Computer Vision and Pattern Recognition
url: https://arxiv.org/abs/2603.23345
score: 100
model: gpt-4o-free
generated_at: 2026-03-25T19:52:29.570053
---

📌 【SJTU & Alibaba】FHAvatar：幾張照片即可重建高保真可分離面髮 3D 化身  你以為擁有影視級 3D 人頭化身必須依賴密集多視角掃描或長時間 per‑identity 優化？最新研究顯示，只有幾張隨機捕獲的畫面也能達成同等效果。  

🤔 **高保真化身通常需要密集掃描，但真的是必要的嗎？**  
現有方法多半將臉部與髮部耦合在統一的建模流程中，這意味著想要取得細節豐富的結果，往往需要大量視角或昂貴的個別優化過程。這種需求在實際應用中顯得尤為沉重，特別是對於希望快速生成個人化 avatar 的開發者而言。  🧪 **從幾張隨機照片學習跨視圖先驗**  
研究團隊提出一個「aggregated transformer backbone」，透過在多視覺資料集上學習幾何感知的跨視圖先驗與頭髮結構一致性，使得模型能從極少的隨機捕獲圖像中有效抽取與融合特徵。這個設計直接回應了「少量觀測也能獲得高品質重建」的目標。  

💡 **面髮分離表示：平面高斯 vs 絲狀高斯**  
FHAvatar 的核心創新在於將面部與髮部在紋理空間中明確解耦：臉部以平面高斯（planar Gaussians）建模，髮部則以絲狀高斯（strand‑based Gaussians）表示。這樣的分離不僅讓兩部分能各自保有高保真細節，也為後續的髮型轉移與樣式編輯提供了自然的介面。  

⚠️ **依賴預訓練Transformer，泛化能力仍待驗證**  
雖然方法在實驗中表現出狀態‑of‑the‑art 的重建品質與即時動畫能力，但其效果很大程度上取決於預訓練 transformer 在多視覺資料集上學到的先驗。對於極端罕見的髮型或臉部特徵，模型的泛化行為尚未在論文中給出定量保證。  🎯 **適用於即時動畫與髮型轉移，降低數字化身門檻**  
因為表示方式是可組合的（composable），使用者可以在保持面部不變的情況下快速更換髮型，或進行樣式風格化編輯。同時，該框架支援實時動畫，意味著從幾張隨機照片到可互動的 3D avatar 的整個流程可以在分鐘級內完成，這對於虛擬試妝、線上會議或遊戲角色創建等場景具有直接的實用價值。  

🔗 **論文連結**  
📝 FHAvatar: Fast and High-Fidelity Reconstruction of Face-and-Hair Composable 3D Head Avatar from Few Casual Captures  
👤 Yujie Sun, Zhuoqiang Cai, Chaoyue Niu, Jianchuan Chen, Zhiwen Chen (Shanghai Jiao Tong University; Alibaba Group)  
🔗 https://arxiv.org/abs/2603.23345  

你認為這種「少量輸入、高保真輸出」的趨勢會改變哪些產業的工作流程？歡迎在留言區分享你的看法 👇  

#AI #ComputerVision #3DAvatar #FHAvatar #ShanghaiJiaoTong #Alibaba #HairstyleTransfer #RealTimeAnimation
