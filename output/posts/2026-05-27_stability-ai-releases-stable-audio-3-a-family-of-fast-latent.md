---
title: "Stability AI Releases Stable Audio 3: A Family of Fast Latent Diffusion Models for Audio Generation and Editing"
source: MarkTechPost
url: https://www.marktechpost.com/2026/05/26/stability-ai-releases-stable-audio-3-a-family-of-fast-latent-diffusion-models-for-audio-generation-and-editing/
score: 93
model: tencent/hy3-preview:free
generated_at: 2026-05-27T21:15:04.639416
---

📌 【Stability AI】Stable Audio 3：高壓縮 latent diffusion 模型  

你以為生成 44.1 kHz 立體聲音須要強大 GPU？Stable Audio 3 透過 4096× 壓縮讓筆電也能跑長段音訊。  

🤔 **高壓縮讓消費級硬體也能玩長段音訊**  
Stable Audio 3 是一系列 latent diffusion 模型，能夠產生立體聲 44.1 kHz 音訊，支援變長輸出、基於 inpainting 的編輯以及快速推論。模型家族分為 small、medium、large 三種規模，其中 small 與 medium 的開放權重已在 Hugging Face 釋出，large 則採企業授權。  

🧪 **SAME 自編碼器：4096× 下採樣的關鍵設計**  
模型的核心是 Semantically‑Aligned Music autoEncoder（SAME），它把立體聲 44.1 kHz 音訊壓縮成低維序列，之後再由 diffusion transformer 在該 latent 上進行去噪生成。SAME 實現 4096× 的總下採樣分兩段：首先把聲音切成不重疊的 256‑sample patch（實現 256× 下採樣），接著透過可學習的 Transformer Resampling Block（TRB）再進行 16× 下採樣，最終得到約 10.76 Hz 的 256 維 latent 序列。這樣的高壓縮大幅縮短 latent 序列長度，使得長段音訊的產生能在消費級硬體上運行。  

💡 **即時可用的生成與編輯功能**  
因為採用 latent diffusion 框架，Stable Audio 3 同時支援：  
- 依照文字、時長與 inpainting mask 生成或編輯音訊  
- 變長輸出（可產生短片段也可延伸至數分鐘）  
- 快速推論（得益於較短的 latent 序列）  

這些特性讓模型適合音效設計、音樂創作以及互動媒體的即時編輯場景。  

⚠️ **目前可見的限制**  
- 開放權重僅涵蓋 small 與 medium 兩種規模，large 模型需企業授權才能取得  
- 文件中未詳細說明 diffusion transformer 的參數規模或具體推論速度基準  
- 未提供針對不同音訊類型（語音、環境聲、樂器）的定量評估結果  
- 模型訓練資料與授權條款尚未在摘要中說明，使用時需參考官方文件  

🎯 **對開發者的實務建議**  
- 若想在筆電或消費級 GPU 上實驗長段音訊生成，可優先下載 small 或 medium 權重  
- 需要更高容量或商業部署時，考慮申請 large 模型的企業授權  
- 在實際應用時，先以文字提示與 inpainting mask 測試模型的編輯能力，再根據結果微調推論參數以平衡品質與速度  

🔗 **論文連結**  
📝 Stable Audio 3: A Family of Fast Latent Diffusion Models for Audio Generation and Editing  
👤 Asif Razzaq (MarkTechPost 報導)  
🔗 https://www.marktechpost.com/2026/05/26/stability-ai-releases-stable-audio-3-a-family-of-fast-latent-diffusion-models-for-audio-generation-and-editing/  

你有試過在筆電上跑 44.1 kHz 音訊生成嗎？歡迎在留言區分享你的經驗或想法 👇  

#StableAudio #StabilityAI #AudioGeneration #LatentDiffusion #AI音訊 #GenAI #機器學習 #開放權重 #MarkTechPost
