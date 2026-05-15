---
title: "Video2GUI: Synthesizing Large-Scale Interaction Trajectories for Generalized GUI Agent Pretraining"
source: ChatPaper/Computation and Language
url: https://arxiv.org/abs/2605.14747
score: 129
model: tencent/hy3-preview:free
generated_at: 2026-05-15T20:10:13.363069
---

📌 Video2GUI：從影片中學習 GUI 操作  

你是否曾想過，為什麼 GUI 代理在新軟體上總是笨手笨腳？答案可能藏在網路上數以億計的教學影片裡。  

🤔 **影片資料庫龐大卻標註稀少，成為 GUI 代理訓練的瓶頸**  
多模態大語言模型的進步讓 GUI 代理成為熱門研究方向，但真實世界的應用場景極其廣泛，現有資料集依賴昂貴的人工標註，範圍往往局限於少數領域，難以支撐模型的泛化能力。  

🧪 **粗到細過濾策略：從 5 億影片中挑出高品質 GUI 教學**  
Video2GUI 採用先粗後細的過濾管線，先透過影片元數據與關鍵詞篩選出可能的教學影片，再利用視覺與語言線索辨識其中的 GUI 操作步驟，最終將這些片段轉換為結構化的 agent 軌跡。整個流程全程自動化，無需人工標註。  

📊 **WildGUI 資料集：1200 萬軌跡、超過 1500 款應用與網站**  
將上述管線應用於 5 億條影片元數據，研究團隊建構了 WildGUI 資料集。該資料集包含超過 1200 萬個互動軌跡，涵蓋 1500 多種不同的應用程式與網站，為 GUI 代理提供了前所未有的規模與多樣性。  

🚀 **預訓練 Qwen2.5‑VL 與 Mimo‑VL：在多個基準上提升 5‑20%**  
以 WildGUI 進行預訓練後，Qwen2.5‑VL 與 Mimo‑VL 在多項 GUI 基礎與動作基準上均表現出 5% 到 20% 的提升，部分基準甚至追平或超越目前的最佳成績。這表明大規模、無標註的影片資料能有效彌補傳統資料集的不足。  

🔓 **開源釋出：資料集與管線將公開，供社群繼續建造**  
論文作者宣布將同時開放 WildGUI 資料集與 Video2GUI 完整處理管線，方便後續研究者在不同模型與任務上進行實驗，進一步推動 GUI 代理的發展。  

⚠️ **樣本來源僅限網路影片、未涵蓋特殊企業內部介面，長期泛化能力尚待驗證**  
由於資料完全來自公開網路影片，可能無法覆蓋所有專業內部或高度客製化的 GUI 介面，且目前僅驗證了短期預訓練效果，長期泛化與穩定性仍需後續工作檢驗。  

💡 **對工程師的啟示：利用影片資料擴充訓練，可降低標註成本並提升代理適應力**  
若您正在建造或調整 GUI 代理，可考慮將大規模教學影片納入資料管線，透過類似 Video2GUI 的過濾與對齊步驟，取得標註成本低但規模龐大的互動軌跡，從而在不犧牲人力的前提下提升模型對新應用的適應能力。  

🔗 **論文連結**  
📝 Video2GUI: Synthesizing Large-Scale Interaction Trajectories for Generalized GUI Agent Pretraining  
👤 Weimin Xiong, Shuhao Gu, Bowen Ye, Zihao Yue, Lei Li (Peking University; LLM-Core, Xiaomi; Renmin University of China; The University of Hong Kong)  
🔗 https://arxiv.org/abs/2605.14747  

#Video2GUI #GUIAgent #MultimodalLLM #WildGUI #Pretraining #OpenSource #AIResearch #Xiaomi #PekingU #HKU
