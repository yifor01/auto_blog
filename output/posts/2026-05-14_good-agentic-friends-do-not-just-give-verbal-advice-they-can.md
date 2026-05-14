---
title: "Good Agentic Friends Do Not Just Give Verbal Advice: They Can Update Your Weights"
source: ChatPaper/Computation and Language
url: https://arxiv.org/abs/2605.13839
score: 121
model: tencent/hy3-preview:free
generated_at: 2026-05-14T20:26:03.931710
---

📌 Good Agentic Friends Do Not Just Give Verbal Advice: They Can Update Your Weights  
University of Central Florida • Westlake University • Snap Inc. • UT‑Austin • Tencent  

你以為多個 AI 代理之間只能靠聊天來合作？研究顯示，它們其實可以直接「改寫」彼此的權重，省下超過八成的運算成本。  

🤔 **自然語言訊息傳遞雖簡單但會產生大量 token 開銷與記憶體負擔**  
現有多-agent LLM 系統多半透過交換自然語言訊息來協作。這種介面雖易於理解與除錯，但每個發送者的中間計算必須先序列化為 token，再被接收者重新處理，導致生成的 token 數、前置填充開銷以及 KV‑cache 記憶體使用顯著增加。  

🧪 **TFlow：以低階 LoRA 權重擾動取代文字訊息的權重空間通訊框架**  
針對已知且固定的接收者架構，TFlow 凍結角色提示的發送者代理，讓它們先處理輸入；隨後一個學習得到的參數生成器將發送者的內部激活映射為針對接收者模組的低階 LoRA 擾動。這些擾動僅在接收者生成階段被融合並套用，實現層級適配而不永久改變模型或擴充接收者的文字內容。實驗採用三個 Qwen3‑4B 代理進行驗證。  

 **單獨接收者準則提升最高 8.5 點，同時 token 處理量下降最高 32.69%**  
在五個基準測試上，TFlow 比單獨運作的接收者準確率最高提升 8.5 個百分點，而處理的 token 數最多可降低 32.69%。  

 **相較於文字訊息三代理基準，總處理 token 減少最高 83.27%，牆上時間加速最高 4.6 倍**  
與以自然語言訊息溝通的三代理基準相比，TFlow 能將總處理的 token 數削減最高達 83.27%，牆上推理時間最快可達 4.6× 的加速，並在四個五個基準中保持具有競爭力的準確率。  

💡 **暫時性低階權重擾動可作為可執行的溝通媒介，實現例層適配而不付出永久模型成本**  
結果顯示，透過權重空間而非 token 空間傳遞訊息，不僅能大幅節省計算與記憶體資源，還能在不修改基礎模型的前提下，針對每個查詢提供特定的適應。這種方式將「溝通」從文字訊息轉移為可直接執行的權重調整，為未來多-agent 系統的效率提升提供了新方向。  

⚠️ **需要知道固定的接收者架構；實驗僅限於 Qwen3‑4B 與五個基準；低階擾動的秩與參數生成器的設計未在摘要中詳述**  
該方法假設接收者的結構已知且不變，且目前的驗證集中在特定模型與任務上。關於最適合的 LoRA 秩或參數生成器架構的細節，尚未在公開摘要中說明，這限制了直接移植到其他模組的即時適用性。  

🎯 **在 token 成本或延遲敏感的場景中，可考慮採用權重空間訊息取代傳統文字協議**  
對於需要大規模多-agent 協作且受推理成本限制的應用（例如即時對話系統、邊端設備上的代理網路），TFlow 提供了一種可顯著降低 token 處理與牆上時間的替代方案，同時不犧牲任務表現。未來工作可探索將此框架擴充至異質模型架構或動態調整的接收者。  

🔗 **論文連結**  
📝 Good Agentic Friends Do Not Just Give Verbal Advice: They Can Update Your Weights  
👤 Wenrui Bao, Huan Wang, Jian Wang, Zhangyang Wang, Kai Wang  
🔗 https://arxiv.org/abs/2605.13839  

你目前的多-agent 系統是否仍在靠「聊天」來傳遞資訊？歡迎在留言區分享你的看法或實作經驗 👇  

#AI #MultiAgent #LLM #EfficientInference #TFlow #WeightSpace #Qwen3 #研究分享
