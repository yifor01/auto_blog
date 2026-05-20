---
title: "A Methodology for Selecting and Composing Runtime Architecture Patterns for Production LLM Agents"
source: ChatPaper/AI
url: https://arxiv.org/abs/2605.20173
score: 106
model: tencent/hy3-preview:free
generated_at: 2026-05-20T21:20:41.584555
---

📌 【Stanford 最新研究】LLM Agent 的穩定性，真正取決於這個被忽略的架構邊界

你以為讓 LLM 更可靠只需要調參數或換模型？其實，模型輸出與系統動作之間的「邊界」才是決定長期穩定性的關鍵。

🤔 **隨機與決定論的界限才是 Agent 運行的承載點**

論文提出 **stochastic‑deterministic boundary (SDB)**，將 LLM 輸出成為系統動作的過程抽象為四個合約環節：proposer、verifier、commit step 與 reject signal。作者認為 SDB 是 production LLM agent 運行時的 load‑bearing primitive，所有運行設計都應該以此為基礎來思考。

🧪 **以協調、狀態與控制為三大關切組織運行設計**

圍繞 SDB，作者把 agent runtime 設計分為三個關注面：Coordination（如何協調多個隨機或決定性元件）、State（如何管理跨步驟的狀態）與 Control（如何控制流程與決策）。在此基礎上，他們歸納出六種運行模式，分別對應不同的 agent 類型（對話式、自主式、長時程）：  
- hierarchical delegation  
- scatter‑gather plus saga  
- event‑driven sequencing  
- shared state machine  
- supervisor plus gate  
- human in the loop  

每種模式都可追溯到傳統分散系統的概念，並指出當「worker」變為隨機的 LLM 時會有什麼變化。

🔑 **五步選型流程、失效診斷與一個新失效模式**

論文貢獻包括：  
1. 一個 **五步驟的方法論**，幫助工程師在特定工作負載下選擇與組合適當的 runtime 模式。  
2. 一個 **診斷程序**，能將 production 中觀測到的失敗映射到特定模式的弱點。  
3. 新提出的失效模式 **replay divergence**：當以決定性事件記錄為輸入的 LLM‑based 消費者，因模型版本或 prompt 改變而產生不同的下游輸出。  
4. 一種 **靠講分解**，把每次呼叫的模型變異與架構動能分開，說明當模型變異減少時，模式選擇與 SDB 的強度會變成提升長期可靠性的主要杠桿。

💡 **方法論已在五個工作負載上驗證，並提供可執行的參考實作**

作者將上述方法論應用於五個具體 workload，並針對一個 90 天合約續約的 agent 提供了一個可運行的參考實作。這意味著該框架不僅是概念性的，也能直接落地到實際系統中。

⚠️ **目前僅在五個工作負載上驗證，需更廣泛的實證**

雖然方法論與模式目錄提供了具體指引，但論文的評估仍限於所提及的五個 workloads。未來需要更多樣化的真實產品環境進行驗證，才能確認其在不同規模與複雜度下的普遍適用性。

🎯 **工程師可直接運用的設計思路**

- 在設計 LLM agent 時，先明確 SDB 的四個合約環節，這樣能讓隨機與決定論的交互點可視化。  
- 根據協調、狀態、控制三個關切，查看六種模式目錄，選擇最符合當前工作負載特性的組合。  
- 使用五步驟選型流程快速原型；若觀測到輸出不一致，先檢查是否為 replay divergence，再考慮模型版本控制或 prompt 鎖定。  
- 隨著模型品質提升（變異減少），將更多精力放在加強 SDB 設計與選擇合適的 runtime 模式上，而非僅靠模型本身的改進。

🔗 **論文連結**  
📝 A Methodology for Selecting and Composing Runtime Architecture Patterns for Production LLM Agents  
👤 Vasundra Srinivasan @ Stanford School of Engineering  
🔗 https://arxiv.org/abs/2605.20173

你在設計 LLM Agent 時，是否曾經顧慮過模型輸出與系統動作之間的「邊界」？歡迎在留言區分享你的經驗或疑問 👇

#LLM #Agent #AIArchitecture #Stanford #GenAI #RuntimePatterns #SDB #ReplayDivergence #AIEngineering
