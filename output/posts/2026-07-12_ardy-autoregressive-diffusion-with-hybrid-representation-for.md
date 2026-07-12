---
title: 'ARDY: Autoregressive Diffusion with Hybrid Representation for Interactive
  Human Motion Generation'
source: HuggingFace Daily Papers
url: https://huggingface.co/papers/2607.08741
score: 84
model: google/gemma-4-31b-it:free
generated_at: '2026-07-12T08:09:36.085474'
---

📌 ARDY：即時文字與動作限制控制的自回歸擴散式 3D 人體動作生成框架  

TL;DR：ARDY 以混合表示與兩階段自回歸 Transformer 去噪，實現即時、高畫質的 3D 人體動作串流生成，支援文字指令與運動學約束。  

隨著虛擬角色、遊戲與沉浸式應用對即時高品質人形動作需求激增，傳統離線生成方法往往無法即時回應使用者指令。ARDY 針對這一痛點，提出一個全新的串流式生成框架，結合擴散模型的細緻表達與自回歸 Transformer 的高效推理，讓文字描述或關節限制能在毫秒級別內驅動 3D 動作產出。  

🤔 為什麼需要「混合表示」與「兩階段」去噪？  

- **混合表示**：ARDY 同時使用姿態向量（kinematic pose）與語義嵌入（text embedding）作為輸入，讓模型在保持運動學一致性的同時，能直接對文字指令做出對應。  
- **兩階段自回歸 Transformer 去噪**：第一階段在粗粒度上預測動作序列的全域性結構；第二階段在細粒度上細化關節細節與時間連貫性。這樣的設計在保證生成速度的同時，仍能達到高保真度。  

🧩 核心架構概覽  

1. **輸入層**：  
   - 文本指令 → 文字編碼器（如 BERT）取得語義向量。  
   - 初始關節姿態或使用者提供的 kinematic constraint → 位置編碼。  
2. **混合表示融合**：將兩者向量串接或加權融合，形成「Hybrid Token」供後續 Transformer 處理。  
3. **兩階段自回歸 Transformer**：  
   - **Stage‑1**：使用較少的 Transformer 層快速產生粗略動作序列，作為「草稿」。  
   - **Stage‑2**：在 Stage‑1 輸出的基礎上，加深 Transformer 深度或使用更細的時間步長，逐步去噪以提升細節與流暢度。  
4. **串流式輸出**：模型在每個時間步產生一段動作，立即回傳給前端，支援即時互動。  

📊 可能的實驗設定（ README 中未列出細節，僅根據摘要推測）  

- **資料集**：可能使用常見的 3D 動作庫（如 AMASS、Human3.6M）作為訓練來源。  
- **訓練目標**：最小化擴散過程的重建誤差，同時加入文字‑動作對應的對比損失。  
- **評估指標**：動作流暢度（如 MPJPE）、文字指令符合度（如 CLIP 相似度），以及即時性（每秒幀數）。  

💡 實務啟示  

- **即時應用**：如果你的產品需要根據使用者文字指令即時產生角色動畫（例如 VR 社交、遊戲 NPC 互動），ARDY 的串流式設計可直接嵌入現有渲染管線。  
- **可控性**：透過 kinematic constraint 輸入，你可以限制關節範圍或保留特定姿勢，避免生成不合理的動作。  
- **擴充套件性**：混合表示的概念允許未來加入更多控制模態，如聲音節拍或情緒標籤，只要把相應向量融合進 Hybrid Token 即可。  

🔗 來源  
- 標題：ARDY: Autoregressive Diffusion with Hybrid Representation for Interactive Human Motion Generation  
- 連結：https://huggingface.co/papers/2607.08741  

#ARDY #HumanMotion #DiffusionModel #Autoregressive #Transformer #3DAnimation #RealTimeGeneration #HybridRepresentation #AI #MachineLearning  
