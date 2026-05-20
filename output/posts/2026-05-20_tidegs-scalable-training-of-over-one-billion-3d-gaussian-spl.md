---
title: "TideGS: Scalable Training of Over One Billion 3D Gaussian Splatting Primitives via Out-of-Core Optimization"
source: ChatPaper/Computer Vision and Pattern Recognition
url: https://arxiv.org/abs/2605.20150
score: 121
model: tencent/hy3-preview:free
generated_at: 2026-05-20T20:50:52.832473
---

📌 【HKUST 主導】TideGS：單卡 24 GB 訓練超過 10 億個 3D 高斯點  

你以為訓練 3D 高斯點（3DGS）必須吃掉巨顯存？研究發現，只要善用 SSD‑CPU‑GPU 階層，單張 24 GB 顯卡也能跑出十億級模型。

🤔 **記憶體瓶頸限制了規模**  
每個 3D 高斯點帶有較大的屬性向量，當 primitive 數上升時，參數表很快超出單卡 GPU 容量，過去的系統只能在商用單卡上處理幾千萬個點。這使得大場景的高保真重建受到硬體限制。

🧪 **以稀疏性與軌跡局部性為核心的外核框架**  
TideGS 把訓練視為「稀疏且依賴當前相機批次」的過程：每次迭代只需要當前視野可見的高斯點。基於此觀察，團隊提出三種協同技術：  
1. **Block‑virtualized geometry** – 以 SSD 對齊的空間塊管理幾何，提升讀取局部性；  
2. **Hierarchical asynchronous pipeline** – 將 I/O 與運算重疊，減少等待時間；  
3. **Trajectory‑adaptive differential streaming** – 只傳送兩次迭代之間的工作集增量，降低資料搬移量。  

這些機制讓 GPU 記憶體僅作為快取，而完整參數驻留在 SSD‑CPU 階層。

 **單卡 24 GB 即可突破十億 primitive**  
實驗顯示，TideGS 在單張 24 GB GPU 上成功訓練超過 1 000 000 000 個 3D 高斯點，且在多個大規模場景中重建品質優於所有評估過的單卡基線（包括傳統內存訓練約 11M 及既有外核基線約 100M）。  

💡 **稀疏與軌跡 locality 是關鍵加速點**  
因為訓練過程本質上只激活當前相機視角下的點，透過空間塊與增量傳送，系統避免了完整參數的頻繁載入。這意味著，只要場景的相機軌跡具有一定連續性，外核方案就能有效隱藏 I/O 延遲，將儲存帶寬轉化為可用的運算資源。  

⚠️ **依賴 SSD 頻寬與軌跡連續性，評估場景有限**  
框架的效能受限於 SSD 的讀寫速度；若軌跡高度跳變，工作集增量可能變大，減少 I/O 重疊收益。此外，實驗主要針對特定大規模場景進行，不同類型的幾何複雜度或極端稀疏情況仍需進一步驗證。  

🎯 **為大規模視覺與雙胞胎應用開闢新道路**  
- 使單卡工作站即可處理城市級或全景級 3D 重建，降低門檻；  
- 對 VR/AR、數位雙胞胎（digital twin）與大規模生成式內容產生直接影響；  
- 未來可結合更快的 NVMe 或計算儲存裝置，進一步推升規模。  

🔗 **論文連結**  
📝 TideGS: Scalable Training of Over One Billion 3D Gaussian Splatting Primitives via Out-of-Core Optimization  
👤 Chonghao Zhong, Linfeng Shi, Hua Chen, Tiecheng Sun, Hao Zhao  
🏫 Hong Kong University of Science and Technology; Great Wall Motor; Tsinghua University; Beijing Academy of Artificial Intelligence  
🔗 https://arxiv.org/abs/2605.20150  

你認為這種外核策略會成為未來大規模 3D 生成的標準嗎？歡迎留言討論 👇  

#3DGS #TideGS #OutOfCore #ComputerVision #HKUST #VRAR #DigitalTwin #GenerativeAI #ScenesReconstruction #GPUComputing
