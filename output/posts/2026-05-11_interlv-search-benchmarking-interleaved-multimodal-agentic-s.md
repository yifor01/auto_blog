---
title: "InterLV-Search: Benchmarking Interleaved Multimodal Agentic Search"
source: ChatPaper/Information Retrieval
url: https://arxiv.org/abs/2605.07510
score: 118
model: tencent/hy3-preview:free
generated_at: 2026-05-11T20:24:22.155007
---

📌 【NTU、SDU、Alibaba Damo、SUSTech 聯合研究】InterLV‑Search：當多模態 Agent 需要「邊看邊搜」時，表現仍遠低於預期  

你以為多模態 AI 已經能夠像人一樣邊看邊搜索？實際上，當它必須在搜索過程中反覆使用文字與圖像證據時，現有系統的準確率仍低於 50%。  

🤔 **研究背景：視覺證據不應只作為輸入或答案的終點**  
現有多模態 Agentic 搜索基準多將視覺證據視為固定輸入或最終答案的端點，缺少在搜索軌跡中反覆條件化的「交錯」使用方式。這使得基準無法衡量 Agent 在真實複雜查詢中，如何動態調取與整合多模態證據的能力。  

🧪 **研究設計：三層級基準與標準化評估 Agent**  
我們提出 InterLV‑Search 基準，共收錄 2,061 個樣本，分為三個階段：  
- **Level 1**：主動視覺證據尋求（自動化 pipeline 建構）  
- **Level 2**：受控離線交錯多模態搜索（自動化 pipeline 建構）  
- **Level 3**：開放網路交錯多模態搜索（機器主導、人類監督的 pipeline）  

基準進一步包含多模態多分支樣本，用於在證據搜索過程中比較多個實體。為了統一評估，我們同時開發 InterLV-Agent，提供標準化的工具使用、軌跡紀錄與評估功能。  

🔬 **核心發現：目前最佳模型整體準確率仍低於 50%**  
在專有與開源多模態 Agent 上進行的實驗顯示，即使是表現最好的模型，整體準確率也未突破 50%。主要失敗點集中在視覺證據尋求、搜索控制以及多模態證據的整合三個環節。  

💡 **深入分析：交錯使用視覺證據對 Agent 的考驗更為嚴苛**  
基準設計強制 Agent 在每一步搜索決策時，必須根據先前取得的文字與圖像證據更新狀態。這意味著單靠「一次性」輸入視覺資訊或將圖像僅作為最終答案無法通過測試。實際表現顯示，現有 Agent 在以下方面仍有不足：  
- 未能有效辨識何時需要額外的視覺線索  
- 在多步驟搜索中難以保持對先前證據的條件依賴  
- 在需要比較多個實體時，無法同時整合來自不同模態的證據  

⚠️ **研究限制：基準仍在發展中，實際應用場景尚需驗證**  
- Level 3 依賴機器主導、人類監督的開放網路 pipeline，可能受網路內容變動影響  
- 基準聚焦於文字與圖像的交錯情境，其他模態（如音訊、影片）尚未納入  
- 評估僅針對現有 Agent 架構，未涵蓋未來可能的新型推理範式  

🎯 **實務啟示：建構真正具備交錯多模態推理能力的 Agent 仍需努力**  
- 研究者應該在 Agent 設計中納入「證據條件回饋」機制，而非僅在前端或後端使用多模態輸入  
- 工程團隊可參考 InterLV-Agent 的軌跡紀錄與標準化工具介面，以進行可重複的實驗與比較  
- 未來工作可擴充基準至更多模態與更長的搜索軌跡，以更貼近真實多步驟知識密集型任務  

🔗 **論文連結**  
📝 InterLV-Search: Benchmarking Interleaved Multimodal Agentic Search  
👤 Bohan Hou, Jiuning Gu, Jiayan Guo, Ronghao Dang, Sicong Leng  
🏫 Nanyang Technological University; Shandong University; Damo Academy, Alibaba Group; Southern University of Science and Technology  
🔗 https://arxiv.org/abs/2605.07510  
💻 基準與評估程式碼：https://github.com/hbhalpha/InterLV-Search-Bench  

你在開發多模態 Agent 時，是否曾遇到「看過圖卻忘記在下一步搜索中使用」的情況？歡迎在留言區分享你的經驗與解決方案 👇  

#AI #Multimodal #AgenticSearch #InterLVSearch #NanyangTechnologicalUniversity #ShandongUniversity #AlibabaDamo #SUSTech #InformationRetrieval #GenAI
