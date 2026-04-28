---
title: "Towards Lawful Autonomous Driving: Deriving Scenario-Aware Driving Requirements from Traffic Laws and Regulations"
source: ChatPaper/AI
url: https://arxiv.org/abs/2604.24562
score: 106
model: tencent/hy3-preview:free
generated_at: 2026-04-28T20:46:03.163154
---

📌 【情境感知LLM：從法規到自駕】

你以為自駕車只要避開行人就算合規？研究顯示，在沒有情境 grounding 的情況下，LLM 讀取交通法規時易漏掉或錯用條文，導致衍生的駕駛規則不準確。

🤔 **法規遵守是基本要求，卻難以自動編碼**  
對人類司機來說，遵守交通法規是最基本的義務；但對自駕車（AV）而言，將條文轉換為可執行的行為約束既費時又難以擴充。傳統做法靠形式語言手動編寫，維護成本高，且難以覆蓋真實世界的千變萬化場景。

🧪 **基於情境分類樹的節點錨點，讓 LLM 在特定場景中推導法規**  
研究團隊提出一個管道：先建立交通場景的分類樹（taxonomy），在樹的每個節點上嵌入「節點錨點」來編碼層次語義。此錨點讓大型語言模型（LLM）在面對具體場景時，能聚焦於相關的法條，避免檢索到無關規定或漏掉適用條文。實驗使用中國交通法規以及 OnSite 場景資料集（共 5,897 個場景）進行驗證。

🔍 **情境感知管道使法規‑場景匹配提升 29.1%，強制與禁止規則準則分別提升 36.9%、38.2%**  
- 法規與場景的匹配度較基線提升 29.1%  
- 衍生的**強制性**要求正確率提升 36.9%  
- 衍生的**禁止性**要求正確率提升 38.2%  
這些提升意味著，在複雜路況下，LLM 所產出的駕駛規則更貼近真實法規，減少誤判或遺漏。

💡 **節點錨點提供層次語義，使 LLM 能在複雜路況中精準定位適用法條**  
透過將法規與場景的語義層級對齊，系統不再只是「關鍵字匹配」，而是能理解例如「在學區內的左轉」與「一般道路左轉」適用的不同條文。這種結構化的 grounding 是準則提升的關鍵機制。

⚠️ **僅驗證中國交通法規與靜態場景集合，未測試跨國法規或動態Agentic 場景**  
實驗限於中國法規與靜態的 OnSite 場景；是否同樣適用於其他國家的法規、或是需要即時決策的動態 Agent（例如與其他車輛協商）仍需後續研究探討。

🎯 **可將此管道作為法規合規層，搭載即時監控模組，提升自駕系統的可驗證性與監管友善度**  
團隊已將該方法實作為 AV 導航的「法規合規層」，並開發出車載、即時的合規監控器，可在實測環境中持續檢查車輛行為是否符合當前場景的法規要求。這為未來的自駕開發、部署以及監管提供了可直接參考的工具鏈。

🔗 **論文連結**  
📝 Towards Lawful Autonomous Driving: Deriving Scenario-Aware Driving Requirements from Traffic Laws and Regulations  
👤 Bowen Jian, Rongjie Yu, Hong Wang, Liqiang Wang, Zihang Zou (Tongji University; The Key Laboratory of Road and Traffic Engineering; Tsinghua University; University of Central Florida; Optixway AI)  
🔗 論文：https://arxiv.org/abs/2604.24562  

你認為自駕車的法規合規該怎麼提升？歡迎留言討論 👇  

#自駕車 #LLM #交通法規 #AI安全 #Tongji大學 #OptixwayAI #法規合規 #機器學習 #AV #智慧交通
