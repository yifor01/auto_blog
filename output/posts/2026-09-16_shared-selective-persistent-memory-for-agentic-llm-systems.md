---
title: Shared Selective Persistent Memory for Agentic LLM Systems
source: Apple ML
url: https://machinelearning.apple.com/research/shared-selective-persistent-memory
model: claude-code/sonnet
generated_at: '2026-09-16T20:15:39.941462'
score: 97
---

📌 Apple EMNLP論文：讓AI Agent記住該記的，忘掉該忘的

TL;DR：選擇性共享記憶架構讓agent任務完成率達96%，比完整保留對話記錄還高。

多數人直覺以為，AI agent記得越多對話歷史，表現應該越好。Apple這篇EMNLP論文卻發現：把完整對話歷史都餵給agent，任務完成率反而比完全不給記憶還要低。

🤔 **每次對話都從零開始，是agent系統的根本問題**

論文指出，透過多輪工具呼叫來生成程式碼的agentic LLM系統，面臨一個結構性問題：每個session都從零開始，先前session中累積的設定選擇、領域限制條件、資料schema與工具使用模式全部被丟棄。但作者也指出，單純把完整對話歷史都持久化保存，既浪費token，也適得其反——不相關的上下文會拉低生成品質。

🧩 **只留四種可重複使用的上下文，捨棄過程推理**

作者提出「shared selective persistent memory」（選擇性共享持久記憶）架構，只辨識並保留四類可重複使用的上下文：任務規格（task specification）、資料schema、工具設定（tool configuration）、輸出限制條件（output constraint），同時捨棄與特定session相關的推理過程紀錄。這份記憶還是「共享」的：封裝了選擇性記憶的workspace可以透過角色權限控制（role-based access control）在使用者之間傳遞，讓累積下來的上下文能被團隊協作重複使用，不必每次重新描述一遍需求。

這套架構被實作在一個已部署的協作workspace平臺上，LLM agent在其中產生、編輯並維護git版控的成品，包括互動式dashboard、結構化報告與資料驅動文件，資料來源涵蓋CSV上傳、SQL、REST API與MCP伺服器等多種連接器。git-backed版控搭配draft隔離機制，讓使用者可以無風險地嘗試修改，並能還原到任一先前狀態而不必重新呼叫模型。此外，論文提出一個互補的「zero-token資料刷新」機制，把生成的程式與執行期資料解耦，讓成品在資料更新時可以重複使用而不需要重新呼叫LLM。

📊 **96% vs 79% vs 71%：記憶不是越多越好**

在三個企業部署場景中，選擇性共享持久記憶達到96%的任務完成率，相較於完全不用記憶的79%，以及保留完整對話歷史的71%。zero-token資料刷新機制讓例行性的資料更新完全不需要重新呼叫LLM，任務時間縮短14倍；而摘要驅動（summary-driven）的生成方式，相較於直接注入原始資料，把每次呼叫的token成本降低了97倍。在四個公開資料集上的複製實驗也確認了這套方法的可推廣性，zero-token刷新機制在12次試驗中全數成功。作者特別強調，單純保留完整歷史反而會用過時的推理痕跡誤導agent、實際拉低任務完成率，而選擇性記憶則同時勝過「完全不記」與「全部都記」這兩個極端。

🎯 **實務啟示**

對於正在建構長期運作的agentic系統的工程師，這篇論文提供了一個明確的設計原則：記憶架構的重點不是「持久化多少」，而是「持久化什麼」。與其把整段對話歷史丟進context，不如明確定義哪幾類資訊（任務規格、schema、工具設定、輸出限制）值得跨session保留，並搭配版控與可還原機制，讓協作與重複使用建立在乾淨的上下文之上，而不是不斷累積的雜訊。

🔗 **來源**
- 標題：Shared Selective Persistent Memory for Agentic LLM Systems
- 連結：https://machinelearning.apple.com/research/shared-selective-persistent-memory

#AgenticAI #LLM #Apple #EMNLP #AIMemory #MultiTurn #AIAgents #NLProc #MachineLearning #CollaborativeAI
