---
title: "OpenMOSS/MOSS-TTS"
source: GitHub Trending
url: https://github.com/OpenMOSS/MOSS-TTS
score: 93
model: tencent/hy3-preview:free
generated_at: 2026-05-28T21:26:39.879360
---

📌 **OpenMOSS 釋出 MOSS‑TTS v1.5 與 SoundEffect v2.0**  

你以為 TTS 只能說中英文？MOSS‑TTS 最新版直接產出 48 kHz 雙語音效，而且還能用 `[pause 0.5s]` 控制停頓。  

🤔 **開源語音合成需要更高保真與即時串流的原因**  
隨著語音助手、遊戲聲效與雙語內容需求激增，單一語種、低取樣率或無法即時產出的模型已難以滿足實際場景。OpenMOSS 團隊因此推出 MOSS‑TTS Family，目標是在高保真、高表達力與複雜實時場景之間取得平衡。  

🧪 **模型架構與關鍵更新**  
- **MOSS‑SoundEffect‑v2.0**：採用 DiT（Diffusion Transformer）骨幹搭配 Flow Matching 目標，能在 48 kHz 下產出最長 30 秒的雙語音效（環境聲、角色語音等）。  
- **MOSS‑TTS‑v1.5**：在語標籤（language tag）下提升多語種合成穩定性；聲音複製更穩健；長參考‑短文本複製品質提升；遵守標點符號的韻律；新增明確的暫停控制語法 `[pause X.Ys]`。  
- **MOSS‑TTS‑Nano**：約 100M 參數，支援多語聲音複製、48 kHz 立體聲輸入/輸出，且僅需 4 顆 CPU 核心即可進行即時串流輸出。  
- **mlx‑audio 支援**：MOSS‑TTS 與 MOSS‑Audio‑Tokenizer 現在皆可透過 Apple 的 mlx‑audio 框架在蘋果晶片上運行，降低部署門檻。  
- **技術報告**：MOSS‑TTSD 與 MOSS‑VoiceGenerator 的技術細節已於 arXiv 發布（2026‑03‑31），並提供 fine‑tuning 教學（2026‑03‑26）。  

🔥 **核心發現：這些更新帶來什麼實用能力**  
- 雙語音效模型可直接用於遊戲、短片或 AR/VR 場景中的環境聲與角色語音，無需額外後處理。  
- 語標籤與 `[pause X.Ys]` 讓開發者在合成腳本中精確控制語言切換與停頓，適合雙語客服或語言學習應用。  
- MOSS‑TTS‑Nano 在資源受限的邊緣設備（如 Raspberry Pi、行動裝置）上仍能提供即時回應，滿足離線語音助手的需求。  
- 透過 mlx‑audio，Mac 開發者可在本機利用蘋果神經引擎加速推理，減少雲端依賴。  

💡 **深入分析：為何這些技術選擇值得關注**  
- **DiT + Flow Matching** 傳統上用於圖像生成，移至音訊領域表明在高保真、長序列聲音合成上具備潛力；相較於自回聲學模型，它在平行度與訓練穩定性上有優勢。  
- **明確暫停 token** 是一種可控制的符號層級干預，避免了只依賴模型內隱學習停頓的不確定性，對於語音對話系統的自然度提升有直接幫助。  
- **Nano 模型的設計** 展示了在參數量大幅下降時，仍可透過較高取樣率與立體聲保留基本聲音品質；這種 trade‑off 對於需要低功耗與低延遲的場景尤為重要。  
- **mlx‑audio 支援** 代表開源社群開始更緊密地與硬體供應商的加速框架合作，未來類似的移植預計會擴展到其他平台（如 Qualcomm Hexagon、Google Edge TPU）。  

⚠️ **已知限制與需要注意的地方**  
- 公開資訊中未提供客觀評估指標（如 MOS、WER、聲音相似度分數），因此實際表現仍需社群自行基準測試。  
- MOSS‑TTS‑Nano 因參數量較小，在極端情感表達或非常長的參考語音上可能會出現細節遺失。  
- 即時串流的具體延遲數值未在說明中給出，實際部署時需根據硬體與網路條件進行調適。  
- 目前的多語言提升依賴於明確的語標籤，若未提供標籤則模型可能回退至預設語言。  
- 專案仍處於快速迭代階段（MOSS‑TTS 2.0 正在收集需求），部分功能可能在後續版本中變更。  

🎯 **給開發者的實務建議**  
- 若需要製作遊戲聲效或短片環境聲，優先嘗試 **MOSS‑SoundEffect‑v2.0**，利用其 48 kHz 雙語輸出直接切換中英文場景。  
- 建置雙語語音助手時，在合成腳本中加入 `[pause 0.8s]` 等標記，搭配語標籤可讓系統在語言切換時自然停頓，提升使用體驗。  
- 對於邊緣設備或離線場景，部署 **MOSS‑TTS‑Nano** 並透過 **mlx‑audio**（Mac）或對應的 CPU 推理庫，可在不犧牲太多音質的前提下達到低功耗運作。  
- 若有特殊聲音克隆需求，參考 arXiv 上的 **MOSS‑VoiceGenerator** 技術報告進行 fine‑tuning，並利用官方提供的教學快速上手。  

🔗 **資源連結**  
- GitHub 專案：https://github.com/OpenMOSS/MOSS-TTS  
- 技術報告（arXiv）：MOSS‑TTSD、MOSS‑VoiceGenerator（2026‑03‑31）  
- mlx‑audio 說明：請參考 mlx‑audio 儲存庫（連結已在專案 README 中提供）  

你目前在專案中是怎麼使用 MOSS‑TTS 系列的？歡迎在留言區分享你的實作經驗與改進建議 👇  

#OpenMOSS #MOSS-TTS #TextToSpeech #SoundEffect #DiT #FlowMatching #mlx-audio #開源語音 #AI音訊 #聲音合成 #邊緣運算 #語音助手 #語音克隆 #雙語合成 #即時串流 #聲音設計 #AI開發 #GitHubTrending #2026 #MOSI.AI #OpenMOSSTeam
