---
title: "SurgTEMP: Temporal-Aware Surgical Video Question Answering with Text-guided Visual Memory for Laparoscopic Cholecystectomy"
source: ChatPaper/Computer Vision and Pattern Recognition
url: https://arxiv.org/abs/2603.29962
score: 91
model: gpt-4o-free
generated_at: 2026-04-01T12:37:48.963528
---

📌 【SurgTEMP】時間感知的手術影片問答系統  

你以為手術影片只要擷取幾張靜態畫面就能讓 AI 回答問題？研究指出，忽略影片的時間脈絡會讓模型在判斷關鍵手術步驟時頻繁失誤。  

🤔 **手術 VQA 需要時間感知，而現有方法多停留在靜幀分析**  
腹腔鏡膽囊切除術等手術過程充斥著快速變化的視野與細節，單幀 VQA 雖能辨識器官或器械，卻難以捕捉「何時發生」與「如何演變」的資訊，這限制了其在教學與術中協助上的實用性。  

🧪 **查詢導向的 token 選擇與層次視覺記憶 + Surgical Competency Progression 訓練**  
SurgTEMP 由兩個核心模組組成：  
1. **查詢導向 token 選擇模組**：根據問題動態挑選相關視覺 token，並將它們分別寫入空間記憶銀行（保留細節）與時間記憶銀行（保存幀間變化），形成階層化的視覺記憶。  
2. **Surgical Competency Progression (SCP) 訓練方案**：以手術技能的階段性進展為引導，讓模型在學習過程中逐步從感知任務過渡到評估與推理任務。  

為支援這些設計，團隊建構了 **CholeVidQA‑32K** 資料集：包含 32,000 筆開放式問答對與 3,855 段腹腔鏡膽囊切除術影片（約 128 小時），依照「感知 → 評估 → 推理」三層架構劃分 11 項任務，涵蓋器械/動作/解剖辨識、關鍵視野（CVS）、術中難度、技能熟練度以及不良事件評估。  

📊 **在多種開源多模態與視覺 LLMs（微調與零射）基線上，SurgTEMP 展現顯著提升**  
綜合評估顯示，SurgTEMP 在 CholeVidQA‑32K 上的表現優於現有最佳框架，證明將時間感知的階層視覺記憶與能力導向訓練結合，能更好建模變長手術影片並保留手術相關線索。  

💡 **層次記憶與能力導向訓練共同解決時間建模的瓶頸**  
空間記憶銀行保留每幀的細節特徵，時間記憶銀行則將不同時序的訊息串聯，使模型在面對跨時窗問題時仍能追溯關鍵事件。SCP 訓練則讓模型在易感知的任務上先打好基礎，再逐步挑戰需要時間推理的高階問題，這種階段性學習與記憶機制的協同，是效能提升的關鍵因素。  

⚠️ **資料集聚焦單一手術類型，泛化能力尚待驗證；計算成本較高**  
目前的 CholeVidQA‑32K 僅涵蓋腹腔鏡膽囊切除術，是否適用於其他手術（如結腸切除、子宮切除）仍需進一步驗證。此外，建構與查詢雙重記憶銀行會增加模型參數與運算負擔，在資源受限的環境下可能需要權衡。  

🎯 **未來手術 AI 應用應考慮時間層次與能力階梯**  
- 開發術中決策支援時，優先納入時間記憶機制，以避免僅依賴靜態幀產生誤判。  
- 在建構訓練資料時，可參考 SCP 的思路，依照手術技能的學習階段設計標註，使模型從感知自然過渡到評估與推理。  
- 若要擴展至其他手術類型，需先補充對應的影片與問答對，以驗證層次記憶的跨程式泛化潛力。  

🔗 **論文連結**  
📝 SurgTEMP: Temporal-Aware Surgical Video Question Answering with Text-guided Visual Memory for Laparoscopic Cholecystectomy  
👤 Shi Li, Vinkle Srivastav, Nicolas Chanel, Saurav Sharma, Nabani Banik  
🏫 University of Strasbourg; IHU Strasbourg; Fondazione Policlinico Universitario Agostino Gemelli IRCCS  
🔗 https://arxiv.org/abs/2603.29962  

你在手術影片分析上是否也曾因忽略時間脈絡而失誤？歡迎留言分享經驗或建議 👇  

#SurgTEMP #手術影片 #VideoQA #醫學AI #腹腔鏡 #CVS #機器學習 #ComputerVision #SurgicalAI
