---
title: "NVIDIA Introduces SANA-WM: A 2.6B-Parameter Open-Source World Model That Generates Minute-Scale 720p Video on a Single GPU"
source: MarkTechPost
url: https://www.marktechpost.com/2026/05/16/nvidia-introduces-sana-wm-a-2-6b-parameter-open-source-world-model-that-generates-minute-scale-720p-video-on-a-single-gpu/
score: 124
model: tencent/hy3-preview:free
generated_at: 2026-05-16T19:20:28.525936
---

📌 **NVIDIA SANA-WM：單 GPU 就能生成 720p 分鐘級影片的開源世界模型**

你以為生成逼真的一分鐘 720p 影片需要多張顯卡？SANA-WM 證明單顆 RTX 5090 就能做到。

🤔 **世界模型的瓶頂：長時程、高解析度還需大規模計算**  
World model 需要從初始影像與動作序列合成真實影像序列，但在生成分鐘級、高解析度影片時，傳統方法要麼依賴多顆 GPU 進行推理，要麼必須犧牲解析度以符合預算。這限制了具身 AI、模擬與機器人研究的實用性。

🧪 **SANA-WM 的架構與三種單 GPU 推理版本**  
基於 SANA-Video 的程式碼庫（NVlabs/Sana），SANA-WM 是一個 2.6B 參數的 Diffusion Transformer (DiT)，原生訓練以支援一分鐘長度、720p 解析度以及 metric‑scale 6‑DoF 攝影機控制。它提供三種可在單 GPU 上運行的推理變體：  
- 雙向產生器：適合離線高品質合成  
- Chunk‑causal 自回歸產生器：適合逐幀序列推播  
- Few‑step 蒸餾自回歸產生器：追求更快部署  

💡 **核心發現： distilled 版在 RTX 5090 上 34 秒完成 60 秒 720p 影片**  
在單顆 RTX 5090 上，使用 NVFP4 量化的蒸餾自回歸版本僅需 34 秒即可去噪生成一段 60 秒、720p 的影片。這意味著模型能在不額外擴展硬體的情況下，達到分鐘級、高解析度的視訊合成。

🔍 **深入分析：Frame‑wise Gated DeltaNet 解決線性注意力的漂移問題**  
標準 softmax 注意力的記憶與計算複雜度隨序列長度平方增長，對於 961 個潛幀（60 s @ 720p）而言是主要瓶頸。SANA‑Video 先前採用累積 ReLU‑based linear attention，雖然狀態大小固定，但缺乏衰減機制，導致過去幀等權重累積，隨時間產生漂移。SANA‑WM 將多數注意力塊替換為 **frame‑wise Gated DeltaNet (GDN)**：每個遞迴步驟處理一整個潛幀，更新規則包含一個衰減門控 γ（降低舊幀權重）以及 delta‑rule 校正（僅更新目標值與目前狀態預測的殘差），從而在保持常數狀態大小的同時，抑制長序列的漂移。

⚠️ **已知限制：基於 SANA‑Video、未公開詳細評估基準**  
該模型直接建構於 SANA‑Video 之中，文中未提供訓練資料規模、基準數據集或與其他最新開放模型的定量比較。此外，所述效能數據僅針對單一硬體 (RTX 5090) 與特定量化設定，不同 GPU 或精度下的表現尚未說明。

🎯 **實務啟示：開放原始碼與多樣化推理選項降低門檻**  
- 研究者與工程師可直接從 NVlabs/Sana 存儲庫取得程式碼，並在單顆消費級 GPU 上進行分鐘級 720p 視訊合成。  
- 三種推理變體讓使用者依需求在品質與速度間取得平衡：離線高品質、序列逐幀推播或快速部署。  
- 對具身 AI、機器人模擬與虛擬環境而言，能在本地工作站即時生成長時程、高解析度的視訊序列，將顯著降低實驗與開發的基礎設施成本。

🔗 **資訊來源**  
📝 **標題**：NVIDIA Introduces SANA-WM: A 2.6B-Parameter Open-Source World Model That Generates Minute-Scale 720p Video on a Single GPU  
🌐 **來源**：MarkTechPost (作者：Asif Razzaq)  
🔗 **連結**：https://www.marktechpost.com/2026/05/16/nvidia-introduces-sana-wm-a-2-6b-parameter-open-source-world-model-that-generates-minute-scale-720p-video-on-a-single-gpu/  
💻 **程式碼**：https://github.com/NVlabs/Sana  

你認為這種單 GPU 分鐘級視訊生成技術會對你的專案或研究產生什麼影響？歡迎在留言區分享你的看法 👇

#AI #WorldModel #VideoGeneration #NVIDIA #SANAWM #DiffusionTransformer #Robotics #Simulation #OpenSource #RTX5090
