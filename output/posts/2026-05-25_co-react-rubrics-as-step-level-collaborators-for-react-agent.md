---
title: "Co-ReAct: Rubrics as Step-Level Collaborators for ReAct Agents"
source: ChatPaper/AI
url: https://arxiv.org/abs/2605.23590
score: 118
model: tencent/hy3-preview:free
generated_at: 2026-05-25T20:30:40.943308
---

📌 【Co-ReAct】讓評分規則成為 ReAct 代理的即時夥伴，步驟級導引提升多步驟推理品質  

你以為讓 AI 自己決定下一步搜尋或推理就夠聰明？實際上，沒有外部指引的 ReAct 代理在搜尋密集、多步驟推理任務中，常常產出淺層、重複或偏離目標的軌跡。  

🤔 **當 ReAct 代理只靠自己判斷時，容易產出冗餘或偏離目標的推理路徑**  
傳統 ReAct 依賴模型內部判斷來決定何時尋證、何時推理或何時停止。缺乏逐步的外部品質信號，使得代理在複雜任務上易陷入低效循環。  

🧪 **以步驟為單位的評分規則作為即時導引**  
Co-ReAct 提出一種框架：在每個決策步驟，將一段評分規則（rubric）注入代理的上下文，明確告訴代理在證據搜尋、推理或自評時應該聚焦什麼。這把評分規則從事後評估或訓練獎勵轉換為即時的行動指引。  

💡 **透過 list‑wise Spearman 相關獎勵訓練判別力強的評分規則生成器**  
為了讓這些規則具備區辨力而非僅僅「看起來合理」，研究團隊採用 GRPO 訓練專門的規則生成器。目標函式最佳化的是 list‑wise Spearman 排名相關獎勵，對應多位專家的共識排名，鼓勵生成能夠正確區分好壞步驟的規則。  

🔑 **在 DeepResearchBench 與 SQA‑CS‑V2 上，Co-ReAct 在開源與閉源模型上均帶來持續提升**  
實驗顯示，無論是 8B/14B 的開源基礎模型，還是前端閉源模型，搭配 Co-ReAct 後，搜尋型 ReAct 代理在兩個基準上的表現都優於原始 ReAct 與各種測試時間計算基線。  

⚠️ **訓練好的評分規則生成器可作為即插即用元件，無需改變原有代理決策邏輯**  
因為規則只在推理時被注入上下文，基礎代理的內部決策機制保持不變。這意味著現有的 ReAct 實作可以直接採用訓練好的規則生成器作為 plug‑in 元件，獲得效能提升而無需重新訓練核心模型。  

🎯 **樣本依賴人類專家共識，長期泛化能力尚待驗證**  
目前的規則生成器是基於專家對步驟品質的共識進行訓練。雖然在評測基準上表現佳，但對於未見任務或更長 horizon 的推理行為，仍需進一步驗證其穩定性與適應性。  

🚀 **工程師可直接將評分規則生成器 plug‑in 到現有 ReAct 流程，提升多步驟推理品質**  
如果你正在構建搜尋導向的 AI 代理，只需把訓練好的規則生成器作為上下文注入層加入推理管線，即可在每一步獲得更具導向性的指引，從而減少無效搜尋與重複推理。  

🔗 **論文連結**  
📝 Co-ReAct: Rubrics as Step-Level Collaborators for ReAct Agents  
👤 Jiazheng Kang, Bowen Zhang, Zixin Song, Jiangwang Chen, Xiao Yang (Qwen Applications Business Group of Alibaba; Tsinghua University)  
🔗 https://arxiv.org/abs/2605.23590  
💻 程式碼：https://github.com/ZBWpro/Co-ReAct  

你會在自己的 AI 代理流程中嘗試這種「規則即時導引」的做法嗎？歡迎在留言區分享你的想法與經驗 👇  

#AI #ReAct #Co-ReAct #多步驟推理 #評分規則 #阿里巴巴 #清華大學 #開源模型 #閉源模型 #GenAI #代理框架
