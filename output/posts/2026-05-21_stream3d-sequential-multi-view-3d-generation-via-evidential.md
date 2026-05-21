---
title: "Stream3D: Sequential Multi-View 3D Generation via Evidential Memory"
source: ChatPaper/Computer Vision and Pattern Recognition
url: https://arxiv.org/abs/2605.21472
score: 105
model: tencent/hy3-preview:free
generated_at: 2026-05-21T20:49:58.256361
---

📌 【World Mind Lab/HKUST × MIT/Harvard】Stream3D：讓凍結的單視角 3D 生成器變成一致的串流模型  

你有試過讓 AI 從連續單眼影像中生成 3D 模型嗎？直接套用現有的單視角 3D 生成器會導致畫面跳動、形狀不一致。  

🤔 **單眼影像流是常見輸入，但現有 3D 生成器缺乏時間一致性**  
視角條件的 3D 生成器（如 SAM 3D、TRELLIS、Hunyuan3D）能從一張圖片產出高品質重建，卻是在每幀獨立運算。當輸入變成長單眼視訊時，這種「逐幀處理」會產生嚴重的時間不一致，使得連續幀之間的幾何與外觀跳動明顯。  

🧪 **凍結的視角條件 3D 生成器 + 證據記憶機制**  
Stream3D 提出一種免訓練的串流機制：在不改動原始生成器權重、結構或額外損失函數的前提下，維護一個緊湊的「證據記憶」。該記憶根據所提出的證據分數（evidence score）選擇性地快取最具資訊量的歷史幀，並隨著串流進展動態更新，以固定數量的幀為上限，避免記憶體隨序列長度線性增長。  

 **Stream3D 在真實與合成串流基準上優於 latent‑transport 基線**  
在兩種基準（寫實與合成）上的評估顯示，Stream3D 在光度（photometric）與幾何（geometric）兩個維度上均優於既有的 latent‑transport 方法，包括 KV‑cache 重用與流式特徵編輯。這些提升是在不重新訓練或修改基礎生成器的情況下達成的。  

💡 **證據分數機制如何選擇最具資訊幀**  
證據分數衡量每幀對記憶內容的貢獻程度：分數高的幀被視為更具資訊值，優先保留；分數低的幀則被逐出。這樣的選擇機制使得記憶始終聚焦於能最有效約束後續生成的幀，從而在不增加計算開銷的情況下維持時間一致性。  

⚠️ **仍需進一步驗證極長序列與不同生成器的泛化能力**  
雖然 Stream3D 已證明能防止記憶體線性增長並抑制長序列退化，但實驗範圍仍限於所測試的基準與特定視角條件生成器。極長視訊或其他類型的 3D 生成器（例如基於扩散的模型）是否同樣受益，尚需後續工作探討。  

🎯 **對於處理長單眼視訊的工程師，可直接採用免訓練的記憶模組**  
- 無需重新訓練或改動現有 3D 生成器，即可插入 Stream3D 的記憶模組。  
- 記憶體佔用固定，適合資源受限的邊緣或即時應用。  
- 開發者可專注於選擇合適的視角條件生成器，讓證據記憶負責維持時間一致性。  

🔗 **論文連結**  
📝 Stream3D: Sequential Multi-View 3D Generation via Evidential Memory  
👤 Kaichen Zhou, Zeyang Bai, Xinhai Chang, Mengyu Wang, Paul Liang  
🏛️ World Mind Lab (HKUST), Media Lab & EECS (MIT), Harvard University  
🔗 https://arxiv.org/abs/2605.21472  
🌐 專案頁面：https://anonymous-submission-20.github.io/streaming3D.github.io/  

你是否已在專案中遇到單視角 3D 生成器在視訊串流上的不一致問題？歡迎在留言區分享你的經驗或想法 👇  

#AI #3DGeneration #Streaming #ComputerVision #MIT #HKUST #Harvard #WorldMindLab #GenAI #TechSharing
