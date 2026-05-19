---
title: "Incantation: Natural Language as the Action Interface for Multi-Entity Video World Models"
source: ChatPaper/Computer Vision and Pattern Recognition
url: https://arxiv.org/abs/2605.18601
score: 121
model: tencent/hy3-preview:free
generated_at: 2026-05-19T20:22:54.566970
---

📌 **自然語言作為動作介面**  

你以為動作控制只能靠按鍵或ID？研究顯示，這種方式限制了多實體協同與跨世界遷移。  

🤔 **動作介面的瓶頸：標準協議綁死特定實體**  
現有互動式視訊世界模型在視覺保真度上表現出色，但其動作介面（如動畫ID、裝置輸入、場景級字幕）將語義鎖死在特定實體或引擎上，導致無法實現細粒度的多實體控制以及跨實體、跨世界的概念遷移。  

🧪 **以潛在幀為單位的自然語言條件蒸餾**  
論文提出 Incantation，採用預訓練雙向視訊骨幹幹架，搭配逐幀（0.25 s）文本交叉注意力，實現每個潛在幀都能被自然語言條件。為支援長時程串流，團隊使用 ODE‑初始化的 Self‑Forcing 蒸餾並採用 RoPE‑脫耦滑動 KV‑快取，使模型能即時生成。  

 **跨實體遷移與 OOV 提示的顯著提升**  
在跨實體遷移基準上，Incantation 達到 89% 準確率，遠超 Action‑Index 基線的 43%；在 OOV（out‑of‑vocabulary）提示上達到 90%，而基線為 0%。兩步驟學生模型在 480p 解析度下維持 19.7 FPS，且在兩小時的長時程滾動中 FVD 保持穩定。  

💡 **同一架構適用於不同遊戲：僅更換實體動作詞彙槽**  
研究團隊將相同架構與訓練配方直接遷移至《The King of Fighters》，僅更改每個實體的動作詞彙槽，即可獲得相應的互動視訊世界模型，顯示該方法的泛化能力。  

⚠️ **資料規模與實驗時間的限制**  
目前僅釋出 Incantation 數據集的預覽子集（包含手動收錄的 Elden Ring 玩家‑Boss 戰鬥片段及結構化動作導向元資料），完整的 Elden Ring 與 KOF 數據將隨後發布；實驗主要聚焦於短期生成品質與即時性，長期行為與更大規模訓練的影響尚未充分探討。  

🎯 **開發者可直接採用自然語言作為統一動作介面**  
- 將現有的按鍵或 ID 控制層替換為文本提示，即可獲得多實體同時控制與概念級遷移能力。  
- 開源的 HuggingFace 預覽數據提供即時實驗基礎，後續完整數據發布將進一步提升模型的泛化性。  
- 對於需要即時互動的應用（如遊戲、虛擬擬真），可參照 ODE‑Self‑Forcing 蒸餾與滑動 KV‑快取的實作路徑，達成約 20 FPS 的實時生成。  

🔗 **論文連結**  
📝 Incantation: Natural Language as the Action Interface for Multi-Entity Video World Models  
👤 Shangwen Zhu, Qianyu Peng, Zhao Pu, Zhilei Shu, Xiangrui Ke (SJTU; NVIDIA Research; USTC; UCAS; NUS; UWaterloo; HKUST; HKU; ZGCA)  
🔗 論文：https://arxiv.org/abs/2605.18601  
💾 數據集預覽：https://huggingface.co/datasets/zhush/incantation-elden-ring-scenes  

你是否已經開始用自然語言來驅動你的生成世界？歡迎在留言區分享你的想法與實驗經驗 👇  

#AI #VideoGeneration #WorldModel #NaturalLanguageProcessing #NVIDIA #SJTU #EldenRing #KOF #MultimodalAI
