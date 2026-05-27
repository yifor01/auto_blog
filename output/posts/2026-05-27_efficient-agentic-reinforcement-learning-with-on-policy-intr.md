---
title: "Efficient Agentic Reinforcement Learning with On-Policy Intrinsic Knowledge Boundary Enhancement"
source: HuggingFace Daily Papers
url: https://huggingface.co/papers/2605.26952
score: 100
model: tencent/hy3-preview:free
generated_at: 2026-05-27T21:01:37.285394
---

📌 **Efficient Agentic Reinforcement Learning with On‑Policy Intrinsic Knowledge Boundary Enhancement**  
（AKBE：讓 LLM agent 自行判斷何時該用工具、何時該靠內部知識）

你有沒有注意到，有些 AI agent 在解題時總是先呼叫外部工具，即使問題其實可以靠模型自身的知識回答？這種「工具過度依賴」不只浪費計算資源，也可能掩蓋模型真正的理解深度。

🤔 **工具過度使用隱形成本**  
當代 LLM‑powered agent 常被設計為隨時可查工具（如搜尋、程式執行、資料庫），但在許多任務中，內部知識已足夠。不必要的工具調用會增加延遲、成本，並降低系統的整體效率。

🧪 **AKBE：讓 agent 自己判斷何時需要工具**  
論文提出一種 **On‑Policy Intrinsic Knowledge Boundary Enhancement (AKBE)** 機制。在訓練過程中，AKBE 會動態偵測 agent 目前的內部知識是否足以支撐當前決策。若知識夠穩固，則給予 supervisory signal 鼓勵 agent 直接使用內部推論；反之，則允許或引導其呼叫外部工具。這整個過程是 on‑policy 的，意味著訊號直接來自當前策略的探索，不需額外的離線標註。

📌 **核心發現：提升正確度同時減少工具調用**  
透過上述機制，AKBE 能讓 agent 在保持或提升任務正確率的同時，**顯著減少不必要的工具呼叫**。具體而言，論文展示了在多個基準上，正確率沒有下降（甚至略有提升），而工具使用次數明確降低，證明了「知識邊界」辨識的實用性。

💡 **深入分析：訊號設計是關鍵**  
AKBE 的核心在於如何產生那個「targeted supervisory signal」。訊號不是簡單的獎懲，而是基於 agent 當前策略下對內部知識確信度的估計。當模型對自身預測的 entropy 低（表示高確信度）時，訊號會偏向獎勵內部決策；當 entropy 高（不確定）時，則允許工具介入。這樣的設計讓 agent 能在訓練中自發學會「何時該思考、何時該查詢」。

⚠️ **研究限制：僅提出方法論，實驗範圍尚待擴充**  
論文主要聚焦於方法的提出與概念驗證。具體實驗的環境、任務種類、基線模型規模等細節在摘要中未提及，因此尚不清楚該方法在更大規模或更異質任務中的表現。此外，作為 on‑policy 方法，其訓練效率相較於離線方式仍需實際評估。

🎯 **實務啟示：可直接落地的工具使用節流策略**  
對於正在構建 LLM agent 的工程師來說，AKBE 提供了一種 **無需額外標註資料、可直接掛在現有強化學習流程上的技巧**：  
1. 在訓練 loop 中追蹤 agent 對內部預測的確信度（例如使用 softmax entropy）。  
2. 依照確信度動態調整工具呼叫的獎勵權重。  
3. 觀察工具使用次數與任務正確率的變化，以驗證是否達成「少用工具、不降準」的目標。

這種方式特別適合那些希望降低 API 調用成本、減少延遲，同時又不願犧牲模型表現的場景。

🔗 **論文連結**  
📝 Efficient Agentic Reinforcement Learning with On‑Policy Intrinsic Knowledge Boundary Enhancement  
🔗 https://huggingface.co/papers/2605.26952  

你有在自己的 agent 系統中嘗試過類似「知識邊界」的判斷嗎？歡迎在留言區分享經驗或疑問 👇

#AI #AgenticAI #ReinforcementLearning #LLM #ToolUse #HuggingFace #AKBE #機器學習
