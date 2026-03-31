---
title: "Zero-Shot Depth from Defocus"
source: ChatPaper/Computer Vision and Pattern Recognition
url: https://arxiv.org/abs/2603.26658
score: 118
model: gpt-4o-free
generated_at: 2026-03-31T00:21:38.329908
---

📌 Zero-Shot Depth from Defocus：新基準 ZEDD 與 Transformer 架構 FOSSA  

你以為景深估計只能靠大量標註資料？這篇研究證明，即使沒見過新場景，也能準確估算深度。  

🤔 **景深估計的零樣本挑戰**  
傳統 Defocus 深度估計（DfD）需要在特定資料集上大量訓練，難以直接泛化到未見過的環境。本論文聚焦於更具實用性的零樣本一般化設定，探討模型在全新場景中的表現。  🧪 **建構 8.3 倍場景的真實基準 ZEDD**  
研究團隊提出全新真實世界 DfD 基準 ZEDD。與先前基準相比，ZEDD 包含 8.3 倍更多的場景，圖像品質與 ground‑truth 深度圖也顯著提升，為零樣本評估提供更嚴謹的測試環境。  

📐 **FOSSA 架構：Transformer + 堆疊注意力層**  
提出的 FOSSA 是一種專為 DfD 任務設計的 Transformer 架構。其核心創新是堆疊注意力層，並加入焦距嵌入（focus distance embedding），使不同焦距圖像之間的資訊能高效交換，從而在不需大量場景特定訓練的情況下捕捉深度線索。  

🔬 **合成資料管線利用現有 RGBD**  
為了訓練模型，團隊設計了一套新的資料管線，能夠把現有的大規模 RGBD 資料集轉換成合成的焦堆疊（focus stack）。此管線讓模型得以利用已有的深度標註進行學習，而無需額外為 DfD 標註資料。  📊 **在 ZEDD 與其他基準上誤差降低最高 55.7%**  
實驗顯示，FOSSA 在 ZEDD 與若干公開基準上的深度估計誤差，相較於既有基線降低了最高 55.7%。這表明在零樣本設定下，該方法能夠顯著提升泛化能力。  

⚠️ **基準規模仍受限於合成資料真實度**  
雖然 ZEDD 提供了更多樣化的場景與高品質圖像，但其 ground‑truth 深度圖仍依賴於合成生成程序。實際感測器噪聲、非理想光線等因素對模型的影響尚未在此工作中完全探討。  

🎯 **工程師可直接使用開放程式碼與基準**  論文隨附發布了 ZEDD 基準（https://zedd.cs.princeton.edu）以及 FOSSA 的程式碼與預訓練模型（https://github.com/princeton-vl/FOSSA）。這使得電腦視覺、機器人與擴增實境等領域的開發者能夠快速 reproducing 或在此基礎上進行延伸應用。  

🔗 **論文連結**  
📝 Zero-Shot Depth from Defocus  
👤 Yiming Zuo, Hongyu Wen, Venkat Subramanian, Patrick Chen, Karhan Kayan @ Princeton University  
🔗 https://arxiv.org/abs/2603.26658  

你認為這種零樣本深度估計在實際系統中會有哪些潛在應用？歡迎在留言區分享你的想法 👇  

#CV #DepthEstimation #ZeroShot #Transformer #Princeton #CVPR #Robotics #AR #OpenSource
