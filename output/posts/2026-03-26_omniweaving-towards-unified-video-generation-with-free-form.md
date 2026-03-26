---
title: "OmniWeaving: Towards Unified Video Generation with Free-form Composition and Reasoning"
source: ChatPaper/Computer Vision and Pattern Recognition
url: https://arxiv.org/abs/2603.24458
score: 114
model: gpt-4o-free
generated_at: 2026-03-26T19:36:27.609017
---

📌統一開源視訊生成  
你以為開源視訊模型只能做簡單剪接？OmniWeaving 卻能在同一框架下理解文字、多圖與影片的交織意圖，進行複雜推論。  🤔 **開源視訊模型仍然零散，缺乏統一的多模態與推論能力**  
現有的學術模型多半專注於單一任務（如文字到視訊或圖像到視訊），即使嘗試統一也難以在同一框架下同時處理交織的文字、多張圖片與影片輸入，且缺乏對複雜使用者意圖的推論能力。這正是像 Seedance‑2.0 這類封閉系統領先的地方。  

🧪 **大規模多樣化預訓練配合 IntelligentVBench 評估**  
OmniWeaving 建構ueix龐大的預訓練資料集，涵蓋各種組合式與推論增強的場景，使模型學會在時間上綜合交織的文字、多圖與影片輸入。同時，研究團隊提出 IntelligentVBench——首個專門用來嚴格評估「下一級智慧統一視訊生成」的綜合基準，以此驗證模型的多任務與推論表現。  🔬 **在開源統一視訊生成中達到 SoTA**  
根據實驗結果，OmniWeaving 在開源的統一視訊生成模型中達到目前最佳狀態（SoTA），顯示其在同時處理多種輸入模態與執行推論任務方面具備競爭力。  

💡 **多模態組合與推論增強讓模型能理解複雜使用者意圖**  模型的關鍵在於它不僅是單純的生成器，更能作為「智慧代理」：透過對輸入的時序綁定與推論，它能夠推斷使用者在給出交織式指令時的深層意圖，進而產出符合預期的視訊內容。這種「組合+推論」的設計是它能在統一框架下表現出色的核心原因。  

⚠️ **僅報告開源模型表現，未與封閉系統直接比較；程式碼尚未公開**  
本研究的評估主要聚焦於開源模型間的比較，並未直接與如 Seedance‑2.0 等封閉系統進行對照實驗。此外，雖然論文表明程式碼與模型將會公開，但目前尚未釋出，讀者無法立即複現結果。  

🎯 **開發者可利用此框架進行統一的多任務視訊合成，期待程式碼開放後進一步實驗**  對於希望在一個模型中完成文字、圖片與影片混合輸入的視訊生成任務的工程師而言，OmniWeaving 提供了一個可行的起點。待程式碼與預訓練權重開放後，可在 IntelligentVBench 或自行設計的基準上進行微調與應用探索。  

🔗 **論文連結**  📝 OmniWeaving: Towards Unified Video Generation with Free-form Composition and Reasoning  
👤 Kaihang Pan, Qi Tian, Jianwei Zhang, Weijie Kong, Jiangfeng Xiong (Zhejiang University; Tencent Hunyuan; Nanyang Technological University)  
🔗 論文：https://arxiv.org/abs/2603.24458  
🌐 Project Page：https://omniweaving.github.io  

#OmniWeaving #視訊生成 #多模態學習 #開源模型 #TencentHunyuan #ZhejiangUniversity #NTU #AI研究 #ComputerVision #MachineLearning
