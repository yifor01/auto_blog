---
title: "WorldKV: Efficient World Memory with World Retrieval and Compression"
source: ChatPaper/Computer Vision and Pattern Recognition
url: https://arxiv.org/abs/2605.22718
score: 106
model: tencent/hy3-preview:free
generated_at: 2026-05-22T20:48:43.880571
---

📌 【KAIST AI & Naver AI Lab】WorldKV：雙倍吞吐、持久世界記憶  

你以為讓 AI 生成的虛擬世界「記得」過去景象，只能靠更大顯存或重新訓練模型？WorldKV 證明：不用額外訓練、不用擴大記憶體，就能在固定資源下獲得更長的歷史一致性，同時把推理吞吐提升約兩倍。  

🤔 **長期世界一致性與即時推理的矛盾**  
自回歸視訊擴散模型能即時依據動作生成世界，但要讓重新造訪的視角呈現完全相同內容，必須保存完整的 KV‑cache。這樣做會導致記憶體與注意力成本隨著 rollout 長度線性增長，破壞即時需求；滑動窗口則能恢復吞吐，卻會犧牲長期一致性。  

🧪 **無需訓練的檢索與壓縮框架**  
WorldKV 分為兩個獨立元件：  
1. **World Retrieval**：將被驅逐的 KV‑cache 塊保存在 GPU/CPU 中，透過鏡頭與動作的對應關係選取與當前場景最相關的塊，直接插回原生注意力窗口，避免重新編碼。  
2. **World Compression**：在每個塊內部，以關鍵向量間的相似度（以 anchor frame 為基準）進行修剪，冗餘 token 被移除，使每塊儲存需求減半，從而在相同預算下可容納約兩倍的歷史長度。  

🔬 **匹配或超越完整 KV‑cache，吞吐提升約兩倍**  
在 Matrix‑Game‑2.0 與 LingBot‑World‑Fast 基準上，WorldKV 在記憶保真度（即重新造訪時的內容一致性）上與完整 KV‑cache 持平甚至略勝，同時推理吞吐約為完整 KV‑cache 的兩倍。與需要額外微調的記憶訓練基線相比，WorldKV 在不進行任何 fine‑tune 的情況下仍具競爭力。  

💡 **透過選擇性檢索與結構壓縮實現效率**  
核心思想是：不是盲目保存所有過去 token，而是根據當前視角與動作的相關性，只把真正可能影響未來生成的資料調回注意力窗口；同時利用塊內關鍵向量的相似度移除重複資訊，大幅壓縮每塊的佔用空間。這種「取用＋壓縮」的組合讓長期歷史得以在固定資源窗口中循環使用，而不需要重新編碼或模型更新。  

⚠️ **僅針對特定推理設定驗證，未探討極端長序列**  
實驗限於 Matrix‑Game‑2.0 與 LingBot‑World‑Fast 兩個基準，且主要評估的是中等長度的 rollout。對於極端長序列（例如數千步）的行為、不同類型的世界生成任務，以及在不同硬體平台上的絕對記憶體消耗，仍需進一步研究。  

🎯 **直接適用於現有自回歸視訊擴散管線**  
- 無需修改模型權重或重新訓練，即可插入現有推理流程。  
- 適合對即時互動有需求的應用：虛擬現實、遊戲世界模擬、實時影像生成等。  
- 開放原始碼與專案頁面提供即時上手範例，工程師可直接參考實作。  

🔗 **論文連結**  
📝 WorldKV: Efficient World Memory with World Retrieval and Compression  
👤 Jung Yi, Minjae Kim, Paul Hyunbin Cho, Wooseok Jang, Sangdoo Yun (KAIST AI; Naver AI Lab)  
🔗 https://arxiv.org/abs/2605.22718  
🌐 Project Page: https://cvlab-kaist.github.io/WorldKV/  

你認為這種「檢索＋壓縮」的策略在其他生成模型（如語音、3D）上是否也有同樣的潛力？歡迎在留言區分享你的見解 👇  

#AI #VideoDiffusion #WorldModel #EfficientInference #KAIST #NaverAI #GenerativeAI #CVPR2026
