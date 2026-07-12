---
title: 'Ant Group’s Robbyant Unveils LingBot-VA 2.0: A Causal Video-Action Model Built
  Natively for Physical AI'
source: MarkTechPost
url: https://www.marktechpost.com/2026/07/11/ant-groups-robbyant-unveils-lingbot-va-2-0/
score: 98
model: google/gemma-4-31b-it:free
generated_at: '2026-07-12T07:59:43.797741'
---

📌 Ant Group Robbyant 發布 LingBot‑VA 2.0：首個原生因果影片‑動作模型，針對實體機器人操作打造  

TL;DR：LingBot‑VA 2.0 直接以因果 DiT 預訓練，讓未標註的網路影片也能提供動作資訊，解決傳統影片‑動作模型在速度與結構上的限制。  

🧩 **從「重建」到「因果」的模型演進**  
傳統的影片‑動作模型多半由兩個為數位內容設計的子模組組成：  
1. 以外觀重建為目標的 VAE（變分自編碼器）  
2. 雙向 video‑diffusion 骨幹，外加一個動作模組  

這樣的組合會產生三大問題：  
- **外觀保留，物理結構不足**：VAE 的畫素重建潛在空間只能儲存影像外觀，對於機械結構資訊的表徵很弱。  
- **迭代除噪過慢**：video‑diffusion 需要在影片 token 上多次除噪，無法滿足即時閉環控制的需求。  
- **目標不教會「動作如何改變世界」**：一般的視訊學習目標只關注畫面再現，無法指導機器人學會因果關係。  

此外，雙向注意力的骨幹結構與機器人控制只能「前向」時間展開的特性不匹配。  

🤔 **LingBot‑VA 1.0 的因果化嘗試**  
第一代 LingBot‑VA 透過微調（fine‑tune）將上述堆疊轉為因果模型，已能在一定程度上解決時間方向的衝突。  

🧩 **LingBot‑VA 2.0：從因果 DiT 原生預訓練**  
版本 2.0 直接在因果 DiT（Diffusion Transformer）上進行預訓練，核心改動包括：  

1. **取代僅壓縮的 VAE**：依照 RepWAM 思路，tokenizer 同時執行三項任務  
   - **重建**：保持影像外觀  
   - **語意對齊**：將視覺潛在向量拉向凍結的 Perception Encoder（教師模型）  
   - **潛在動作**：從相鄰潛在之間抽取緊湊的轉移變數  

2. **雙向動態模型**  
   - **逆向動力學模型**：預測每個潛在動作  
   - **前向動力學模型**：將潛在動作解碼成「傳輸對映 + 殘差」的形式  

   這樣世界狀態與動作共享同一潛在空間，使得未標註的網路影片也能提供與動作相關的監督訊號。  

3. **因果 DiT 架構**  
   - 保持 1.0 版的 Mixture‑of‑Transformers（MoT）版面。  
   - **影片專家**與**動作專家**共享同一個因果自注意力（causal self‑attention），但各自擁有獨立的前饋（feed‑forward）路徑。  
   - 影片專家的前饋層被換成稀疏 MoE（Mixture‑of‑Experts）路由層，內含 128 個 SwiGLU 專家，採 top‑8 路由，並共享一個專家以平衡負載。  

📊 **技術意涵**  
- **即時控制**：因果自注意力僅向前看，避免了雙向注意力在即時控制中的時間衝突。  
- **行為監督自動化**：未標註影片透過上述潛在‑動作目標自動獲得與動作相關的訊號，減少了資料標註成本。  
- **效能擴充套件**：影片與動作的兩條前饋路徑可非對稱擴充套件，影片專家使用稀疏 MoE 以提升大規模視訊特徵的處理效率。  

🎯 **實務啟示**  
- 若你的機器人平臺需要在真實環境中快速回應，考慮採用因果 DiT 之類的前向注意力模型，避免雙向結構帶來的延遲。  
- 未標註的網路影片可以直接作為預訓練資料，利用語意對齊與潛在動作目標自動獲得行為資訊，降低資料收集門檻。  
- 稀疏 MoE 前饋層提供了在保持效能的同時擴大模型容量的途徑，適合資源受限的機器人邊緣部署。  

🔗 來源  
- 標題：Ant Group’s Robbyant Unveils LingBot-VA 2.0: A Causal Video-Action Model Built Natively for Physical AI  
- 作者／機構：Asif Razzaq / MarkTechPost  
- 連結：https://www.marktechpost.com/2026/07/11/ant-groups-robbyant-unveils-lingbot-va-2-0/  

#LingBotVA #CausalModel #VideoAction #EmbodiedAI #DiffusionTransformer #MoE #Robotics #AntGroup #Robbyant #PhysicalAI #AIResearch
