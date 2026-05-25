---
title: "Geo-Align: Video Generation Alignment via Metric Geometry Reward"
source: ChatPaper/Computer Vision and Pattern Recognition
url: https://arxiv.org/abs/2605.23903
score: 113
model: tencent/hy3-preview:free
generated_at: 2026-05-25T20:44:43.482722
---

📌 **幾何對齊提升影片控制**

你以為只要有足夠的合成資料，AI 就能完美複製真實世界的鏡頭運動？最新研究指出，單靠監督式微調在真實場景下仍會失準，而一種基於幾何度量的強化學習卻能讓模型自行校正。

🤔 **研究背景**  
合成資料稀缺導致模型難以忠實遵循真實相機軌跡  
現有的視訊到視訊重繪方法多依賴合成資料進行監督式微調。然而，同步、多視角的真實世界視訊資料極度稀少，這使得模型在處理分布外的真實影片時，常見無法精準遵守實際尺度與相機軌跡的問題。

🧪 **研究設計**  
以先訓練模型為基礎，加入尺度感知的感知獎勵與 metric 3D 估測器  
Geo-Align 是第一個專為相機控制視訊重繪設計的強化學習框架。它在一個預訓練模型之上，引入一個尺度感知的感知獎勵機制。具體而言，團隊設計了一個 metric 3D 估測器，從生成的視訊中提取精確的相機軌跡，並明確懲罰旋轉與平移的偏差。此外，研究團隊還構建了一套資料管線：利用真實世界的條件視訊與由合成資料推導出的目標相機軌跡，從而減少對成對 (paired) 合成‑真實資料的依賴。

🔍 **核心發現**  
Geo-Align 在相機可控性與視覺保真度上均優於現有監督學習基線  
廣泛的實驗顯示，Geo-Align 在精確的相機可控性與視覺保真度兩個維度上，持續優於既有的監督學習方法。這表明，以幾何度量作為獎訊的強化學習能夠有效縮小合成資料與真實世界之間的落差。

💡 **深入分析**  
幾何獎勵直接懲罰旋轉與平移偏差，使模型學會自動校正軌跡  
透過在獎勵函數中直接納入 metric 3D 估測器的誤差，Geo-Align 能讓模型在生成過程中持續感知並修正相機姿態的偏離。這種「即時回饋」的機制使得模型不僅學會生成視覺上合理的影片，更能在缺乏真實標註的情況下保持對實際相機軌跡的忠實遵循。

⚠️ **研究限制**  
仍需合成資料產生目標相機軌跡，且依賴預訓練模型的品質  
雖然該方法減少了對成對合成‑真實資料的需求，但目標相機軌跡仍然來自合成資料的模擬。此外，Geo-Align 的表現與所使用的預訓練視訊生成模型的品質息息相關，若基礎模型本身在某些場景下表現不佳，可能會限制最終效果。

🎯 **實務啟示**  
未來影片生成管線可考慮以 RL 取代或補強監督微調，降低對昂貴多視角實景資料的需求  
對於需要精準相機控制的視訊生成應用（如虛擬製作、增強實境或影像特效），Geo-Align 提供了一條不依賴大量昂貴多視角實景資料的可行路徑。工程師可在現有的預訓練模型上，加入類似的幾何度量獎勵，以提升模型在真實世界中的軌跡忠實度與視覺品質。

🔗 **論文連結**  
📝 Geo-Align: Video Generation Alignment via Metric Geometry Reward  
👤 Zizun Li, Haoyu Guo, Runzhe Teng, Chunhua Shen, Tong He (USTC; Shanghai AI Lab; ZJU)  
🔗 https://arxiv.org/abs/2605.23903  

#AI #VideoGeneration #ReinforcementLearning #CameraControl #GeoAlign #USTC #ShanghaiAILab #ZJU #CVPR #GenAI
