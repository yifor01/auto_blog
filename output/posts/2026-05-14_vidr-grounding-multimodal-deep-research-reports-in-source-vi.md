---
title: "ViDR: Grounding Multimodal Deep Research Reports in Source Visual Evidence"
source: ChatPaper/Information Retrieval
url: https://arxiv.org/abs/2605.13034
score: 110
model: tencent/hy3-preview:free
generated_at: 2026-05-14T20:40:10.706315
---

📌 **ViDR：圖表證據深度研究**  

你以為 AI 撰寫長報告時，圖片只是點綴嗎？  
其實，來源圖表才是可驗證的關鍵證據。  
ViDR 把它當作可檢索、可解釋、可路由、可驗證的證據物件。  

🤔 **文字證據主導，圖像證據被弱化**  
現有的深度研究系統多依賴檢索與推理來產出長篇報告，但證據多以文字為主。 multimodal 系統往往只弱化地檢索圖像，或直接自行生成圖表，導致來源圖表作為證據的潛力未被充分利用。  

🧪 **構建證據索引大綱與圖像精煉流程**  
ViDR 首先建立一個以證據為索引的大綱，將報告中的每個主張與具體的文字或視覺證據連結。對於從網路爬取的雜訊圖像，ViDR 透過情境感知過濾、大綱感知重新排序以及視覺語言模型（VLM）的視覺分析，將其精煉為可用的來源圖證據原子。每個報告章節則在生成時調用對應的證據集，並最終對視覺引用進行驗證，以降低幻覺或錯誤放置的圖表。  

📊 **ViDR 在報告品質、來源圖整合與可驗證性上皆顯著提升**  
實驗中，ViDR 與強力的商業與開源基線進行對照。結果顯示，ViDR 在整體報告品質、來源圖的檢索與定位、以及證據的可驗證性方面都有顯著改善。為了系統化評估視覺證據的使用，論文同時提出了 MMR Bench+ 基準，涵蓋來源圖檢索、放置、解讀、可驗證性以及分析圖表生成五個維度。  

💡 **來源圖表作為可驗證證據強化了報告的視覺支撐與事實基礎**  
與其依賴模型自行編造的圖表，ViDR 直接使用經過嚴格篩選與解讀的來源圖像作為證據。這種做法不僅提供了更具體的視覺支撐，也讓報告的事實基礎更易被追溯與驗證，從而提升多模態深度研究的可信度。  

⚠️ **樣本與基準依賴於現有網頁圖像，代碼尚未公開**  
目前的實驗主要基於公開網頁上的圖像進行過濾與重排，且論文未提供開放原始碼或工具。這意味著雖然方法概念清晰，但在工程上直接落地仍需等待後續程式碼釋出或自行實作。  

🎯 **對多模態深度研究與可信 AI 報告生成具有啟發**  
ViDR 的思路表明，將來源圖像視為可驗證的證據物件，能有效彌合文字與視覺證據之間的鴻溝。對於正在興起的 AI Agent、多模態大語言模型以及可信任 AI 報告生成領域，這項工作提供了一個可參考的設計方向：在生成長篇報告時，優先檢索、解讀與驗證來源圖表，而非僅依賴模型自行合成的視覺內容。  

🔗 **論文連結**  
📝 ViDR: Grounding Multimodal Deep Research Reports in Source Visual Evidence  
👤 Zhuofan Shi, Peilun Jia, Baoqin Sun, Haiyang Shen, Sixiong Xie  
🏢 Peking University; National Key Laboratory of Data Space Technology and System; Beijing Jiaotong University; Hunan University  
🔗 https://arxiv.org/abs/2605.13034  

#AI #Multimodal #DeepResearch #VisualEvidence #ReportGeneration #TrustworthyAI #PekingUniversity #MMRBench+
