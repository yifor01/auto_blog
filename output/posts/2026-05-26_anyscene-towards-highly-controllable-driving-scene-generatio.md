---
title: "AnyScene: Towards Highly Controllable Driving Scene Generation at Anywhere and Beyond"
source: arXiv
url: http://arxiv.org/abs/2605.26113v1
score: 97
model: tencent/hy3-preview:free
generated_at: 2026-05-26T20:54:32.284767
---

📌 【AnyScene】任意 BEV 佈局即可生成高度可控駕駛場景  

你是否曾想過，只要畫出鳥瞰圖，就能讓模型產出對應的多視角駕駛影片？AnyScene 正是這樣的能力。  

🤔 **高保真可控合成資料是自駕進階的關鍵**  
端到端自駕系統需要大量罕見安全關鍵情境的訓練資料。現有以占用圖為導向的方法多半依賴淺層條件機制與參考框架相關的影片合成，這限制了從任意 BEV 佈局進行細粒度控制，也阻礙了可擴充模擬的應用。  

🧪 **AnyScene：以占用圖為核心的統一框架**  
論文提出 AnyScene，採用 Spatial‑Temporal Occupancy Diffusion Transformer，將 BEV 特徵與占用序列以自回歸方式聯合標記。這使得模型能直接從跨資料集或使用者自訂的 BEV 佈局產生精準的占用序列，並支援長視野生成。基於產生的占用圖，Geometry‑Grounded View Expansion 模組將占用視為空間的標準表示，以參考自由且自回歸的方式合成時間上一致的多視角駕駛影片，推論時可靈活切換相機配置。  

🚀 **在占用與影片生成上達到最先進表現**  
實驗顯示 AnyScene 在占用序列與多視角影片兩項任務上均達到 SOTA。模型對未見過且客製化的 BEV 佈局具備強烈的泛化能力，並能為下游任務（如稀疏視角 3D 重建）帶來可量化的提升。  

💡 **占用作為標準表示帶來的設計優勢**  
將占用圖視為空間的標準表示，使得影片合成不需要參考影片或固定相機軌跡，這種參考自由的設計自然支援任意相機參數的推論。同時，BEV 與占用特徵的聯合標記讓模型在生成過程中保持對鳥瞰布局的精準控制，解決了先前僅能依賴粗略條件的限制。  

⚠️ **摘要中未詳述模型的計算成本與極端罕見情況穩定性**  
根據目前可見的摘要，作者未在此處詳細論述模型的推論延遲、記憶體需求，亦未提及在極端罕見場景下的行為表現。這些方面將是後續研究與工程落地時需要關注的方向。  

🎯 **對自駕模擬與合成資料工程的啟示**  
- 可直接從任意 BEV 佈局（包括手繪或來自不同資料集的布局）生成符合預期的駕駛場景，大幅提升資料管線的靈活性。  
- 參考自由的多視角影片合成方式讓工程師在測試不同感測器配置時無需重新訓練或額外對齊步驟。  
- 對稀疏視角 3D 重建等下游任務的正向影響顯示，高品質可控合成資料不只能用於感知模型訓練，亦能幫助映射與規劃模組的演進。  

🔗 **論文連結**  
📝 AnyScene: Towards Highly Controllable Driving Scene Generation at Anywhere and Beyond  
👤 Haiming Zhang, Junfei Zhou, Feng Jiang, Jingzhong Li, Zhenglong Guo  
🔗 http://arxiv.org/abs/2605.26113v1  

你有試過根據鳥瞰圖生成駕駛影片嗎？歡迎在留言區分享你的想法或使用經驗 👇  

#AI #自動駕駛 #場景生成 #Occupancy #DiffusionTransformer #AnyScene #arXiv #模擬資料 #3D重建 #端到端 #自駕技術
