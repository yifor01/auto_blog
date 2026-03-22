---
title: "$x^2$-Fusion: Cross-Modality and Cross-Dimension Flow Estimation in Event Edge Space"
source: ChatPaper/Computer Vision and Pattern Recognition
url: https://arxiv.org/abs/2603.16671
score: 115
model: gpt-4o-free
generated_at: 2026-03-18T21:13:29.767203
---

📌 【Tsinghua/HKU/HIT 最新研究】$x^2$-Fusion：以事件邊緣空間統一多模態流估計  

你以為把相機、雷達與事件感測器的資料直接拼湊就能得到更好的流估計？其實，缺乏一個共同的「語言」，反而讓融合變得更複雜。  

🤔 **多模態特徵空間各自為政，融合效果打折**  
現有的 2D/3D 流估計方法常將影像、LiDAR 與事件相機的特徵分別處理，然後再進行粗糙的拼接。因為每種模態都有自己的表示方式，缺乏一個所有感測器都能對齊的潛在空間，導致跨感測器的不匹配難以消除，融合過程顯得冗餘且不穩定。  🧪 **以事件邊緣作為統一表示的基礎**  
論文指出，事件相機本質上提供的是時空邊訊號，可視為一種固有的邊場。作者將這個邊場定義為 **Event Edge Space**，在此空間中，影像與 LiDAR 的特徵被顯式地對齊到同一個以邊為中心的齊次表示。在此基礎上，他們提出 $x^2$-Fusion 框架，透過可靠性感知的自適應融合來估計各模態在惡化條件下的穩定度，並利用跨維度對比學習緊密耦合 2D 光流與 3D 場景流的估計。  

🚀 **在標準與挑戰場景下均表現優異**  
在合成與真實基準上的廣泛實驗顯示，$x^2$-Fusion 能達到目前最佳的準度（SOTA），且在較具挑戰性的情境（如低光、快速運動或感測器噪聲）中帶來顯著的提升。具體改善幅度未在摘要中給出，但作者強調該方法在極端條件下的穩定性是其主要貢獻。  

💡 **關鍵在於「共享語言」而非簡單拼湊**  
研究團隊認為，真正的多模態融合不應是把各自的特徵向量堆疊起來，而是要先找到一個所有模態都能自然表達的表示空間。事件邊緣正好提供了這樣一個共同的幾何基礎，使得後續的對齊與融合變得更為直接，也減少了因特徵空間不匹配而引入的額外參數與複雜度。  

⚠️ **實驗主要聚焦於合成基準與有限真實序列**  
摘要未詳細說明使用的具體資料集規模或多樣性，僅提到合真兩種基準。因此，方法在更廣泛的真實世界場景（例如不同天氣、不同 LiDAR 點密度）中的表現仍需進一步驗證。  

🎯 **對工程師的啟示：先統一表示，再做自適應融合**  
- 若系統同時使用事件相機與傳統影像／LiDAR，可考慮先把事件資料轉換為時空邊場，作為特徵對齊的錨點。  
- 在融合階段，加入可靠性估計（例如基於事件密度或影像對比度）能讓模型在惡化條件下自動降低不可信模態的權重。  
- 透過對比學習讓 2D 與 3D 流的預測相互約束，有助於提升一致性，尤其在稀疏點雲或運動模糊的情境下。  

🔗 **論文連結**  
📝 $x^2$-Fusion: Cross-Modality and Cross-Dimension Flow Estimation in Event Edge Space  
👤 Ruishan Guo, Ciyu Ruan, Haoyang Wang, Zihang Gong, Jingao Xu  
🏫 Tsinghua University; Harbin Institute of Technology; The University of Hong Kong  
🔗 https://arxiv.org/abs/2603.16671  

你目前的多模態流估計 pipeline 是否已經嘗試以事件邊緣作為共同表示？歡迎在留言區分享你的經驗與疑問 👇  

#ComputerVision #EventCamera #MultiModalFusion #OpticalFlow #SceneFlow #Tsinghua #HKU #HIT #SOTA #ARXIV
