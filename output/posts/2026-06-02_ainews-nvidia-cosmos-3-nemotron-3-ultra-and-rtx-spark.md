---
title: "[AINews] NVIDIA Cosmos 3, Nemotron 3 Ultra, and RTX Spark"
source: Latent Space
url: https://www.latent.space/p/ainews-nvidia-cosmos-3-nemotron-3
score: 115
model: tencent/hy3-preview:free
generated_at: 2026-06-02T21:29:52.464775
---

📌 【AINews】NVIDIA Cosmos 3、Nemotron 3 Ultra 與 RTX Spark 一次看  

你以為開源模型已經達到極限？NVIDIA 這次直接把語言、圖像、影片、聲音和行動統一進一個模型，同時釋出全球最大的開放權重 LLM 與一顆 1 PFLOPS 超級晶片——這波發佈到底意味著什麼？  

🤔 **為何這三項發佈成為 AI 開發者的焦點**  
近一年來，生成式模型正從單一模態（純文字或純圖像）向「全模態」邁進，實體機器人、虛擬場景與多感官互動的需求急速上升。開發者不只想要更強的生成品質，更需要模型能夠開放權重、提供完整程式碼與資料集，以便在自家硬體上進行微調與部署。NVIDIA 本週的 announcements 正好回應了這三個關鍵需求。  

🧪 **Cosmos 3：語言‑圖像‑影片‑聲音‑行動的統一架構**  
根據 Latent Space 的報導，Cosmos 3 採用 Mixture‑of‑Transformers 結構，將一個自回歸的「reasoner tower」與一個擴散的「generator tower」配對：  
- **Nano**：16B 參數（8B reasoner + 8B generator）  
- **Super**：64B 參數（32B reasoner + 32B generator）  
此外，針對 Text2Image 與 Image2Video 的微調版本目前已成為開放權重的 SOTA，僅次於先前發表的 Nano Banana 2。NVIDIA 同時釋出模型權重、訓練程式碼、資料集以及微調食譜，並宣布與 Runway 等夥伴共同成立「Cosmos Coalition」，以構建開放的世界模型生態系統。  

🚀 **Nemotron 3 Ultra：美國領先的開放權重 LLM**  
同樣在 Latent Space 報導中提到，Nemotron 3 Ultra 是一個 550B‑A55B（實際激活參數規模）的開放權重大語言模型，被形容為「remarkably efficient/fast」，並且目前是美國境內最強的開放權重 LLM（新 US SoTA）。模型同樣提供完整的訓練與推論程式碼，方便研究者在自有硬體上進行實驗或微調。  

💻 **RTX Spark：個人電腦層級的 1 PFLOPS 超級晶片**  
在 Computex 上，NVIDIA 與 Microsoft、OpenClaw 以及 Hermes Agent 合作預展了 RTX Spark——一顆能夠達到 1 petaflops 運算效能的個人電腦級超級晶片。此晶片設計用於支援大規模生成模型（如 Cosmos 3 與 Nemotron 3 Ultra）在本地端的推理與微調，縮小了雲端與邊緣之間的效能鴻溝。  

💡 **技術啟示：開放與全模態將成為未來基礎設施**  
- **開放權重 + 完整食譜**：讓研究者不只能使用模型，更能瞭解其訓練流程，進行公平比較與客觀改進。  
- **全模態統一架構**：透過將 reasoner 與 generator 分離，未來可依需求替換或擴充單一模態（例如加入觸覺或力回饋），而不必重新訓練整個模型。  
- **硬體‑軟體協同設計**：RTX Spark 的推出顯示，單靠模型演進不足；提供匹配的運算平台才能讓這些巨型模型在真實產品中落地。  

⚠️ **已知限制與未答問題**  
- 報導未提供具體基準數據（例如圖像生成的 FID、影片生成的 VSFA 等），因此無法直接量化其與閉源模型的差距。  
- Cosmos 3 的「開放」範圍是否包括所有訓練資料的細節尚未說明，僅確認權重、程式碼與微調食譜已公開。  
- RTX Spark 目前僅為預展版本，實際出貨時間、功耗與軟體堆疊的完整支援度仍待後續資訊。  

🎯 **給開發者的實務建議**  
1. 若你正在從事多模態生成（文字到圖像、圖像到影片），優先評估 Cosmos 3 Super 或其微調版本，利用官方提供的微調食譜在自己的資料集上進行實驗。  
2. 對於需要巨型語言模型但又希望避免雲端鎖定的團隊，Nemotron 3 Ultra 提供了一個可在本地高端伺服器或工作站上運行的開放選項。  
3. 若你的產品需要即時、低延遲的生成能力，可關注 RTX Spark 後續的開發者套件（SDK），評估其在本地工作站上的推理表現。  

🔗 **資訊來源**  
- Latent Space 播客新聞：https://www.latent.space/p/ainews-nvidia-cosmos-3-nemotron-3  
- NVIDIA 官方開放週公告（含 Cosmos Coalition 與模型下載連結）可於 NVIDIA 網站尋找「Cosmos 3」與「Nemotron 3 Ultra」相關頁面。  

你對這三項發佈最期待哪一方面？是想試玩 Cosmos 3 的影片生成，還是測試 Nemotron 3 Ultra 在本地推論的速度？歡迎在留言區分享你的想法與實驗計畫 👇  

#AINews #NVIDIA #Cosmos3 #Nemotron3Ultra #RTXSpark #開放模型 #全模態 #生成式AI #LatentSpace #AI開發者 #機器學習 #深度學習 #AI硬體 #AI軟體 #AI創新
