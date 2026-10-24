---
title: 'Stateful Agentic Engineering Copilots with Letta: Core Memory, Shared State,
  Semantic Retrieval, Custom Tools, Streaming, and Portable Agent Workflows'
source: MarkTechPost
url: https://www.marktechpost.com/2026/10/24/stateful-engineering-copilots-letta-tutorial/
model: claude-code/sonnet
generated_at: '2026-10-24T19:36:14.891162'
score: 88
---

📌 用 Letta 打造有記憶的工程助理：核心記憶、共享狀態與語意檢索全教學

TL;DR：MarkTechPost 教學示範如何用 Letta 建構一個能跨 session 保留記憶、跨 Agent 共享狀態的工程 Copilot。

多數 Agent 教學還停留在「每次對話都是一張白紙」，但這篇教學示範的是另一個方向：讓 Agent 真正記得工程師、專案與過去的決策,而且這份記憶可以被檢查、同步、匯出。

🤔 **為什麼要給 Agent 可檢查的記憶**

教學指出,傳統的 prompt 式對話把每次互動當成獨立事件,而 Letta 的設計理念是把持久狀態、檢索、工具呼叫與多 Agent 協作整合成一個完整的 Agentic 系統。核心思路是建立結構化的 core memory blocks,讓 Agent 可以自主更新,同時這些 block 也能被應用程式程式碼直接讀寫同步。

🧩 **架構拆解：從核心記憶到可攜式匯出**

依照素材描述,整個教學按以下架構逐步搭建：

- 設定 Letta client 與 SDK,並加入相容性輔助函式處理不同 Letta 版本間的 API 差異,動態選擇可用模型。
- 建立具有結構化 core memory blocks 的工程 Copilot,並檢視初始記憶狀態。
- 示範自我編輯記憶：讓 Copilot 記住工程師、專案、決策與已知失效模式等持久資訊,也能直接從應用程式碼更新專案狀態。
- 建立共享的唯讀與可寫 block,讓一個 reviewer agent 連接到相同的共享記憶,觀察兩個 Agent 如何交換持久的工作上下文。
- 填入帶標籤的工程知識到 archival memory,用語意搜尋（而非關鍵字比對）檢索相關資訊,並讓 Agent 自主查詢這些知識來回答操作性問題。
- 建立並附加一個自訂的 server-side 工具,用於做確定性的「發布風險」計算,並把結果記錄進記憶。
- 用 Letta 的串流介面即時觀察推理過程、工具呼叫與回應,並檢查 server-side 的對話紀錄,確認狀態不依賴本地 Python process,甚至可以用持久識別碼在全新的 process 中重新連線。
- 最後把完整的 Agent 狀態匯出成 .af 檔,做為記憶、工具與對話狀態的可攜式表示。

💡 **這不是新方法,是一套可直接套用的記憶架構示範**

教學本身並未提出新的演算法或模型,而是展示 Letta 既有功能如何組合成一套實用的記憶系統：core memory 維持高價值的上下文、archival memory 提供可擴展的檢索、共享 block 協調多 Agent、自訂工具擴充確定性運算、串流與 server-side 歷史提供可觀測性與持久性。

🎯 **實務啟示**

如果你的 Agent 專案一直卡在「重啟就失憶」或「多個 Agent 各自為政」的問題,這份教學提供的模式（結構化 core memory + 共享 block + archival 語意檢索 + .af 匯出）可以直接拿來作為工程 Copilot 的記憶層設計起點。

🔗 **來源**
- 標題：Stateful Agentic Engineering Copilots with Letta: Core Memory, Shared State, Semantic Retrieval, Custom Tools, Streaming, and Portable Agent Workflows
- 作者／機構：Sana Hassan, MarkTechPost
- 連結：https://www.marktechpost.com/2026/10/24/stateful-engineering-copilots-letta-tutorial/

#AIAgents #Letta #AgentMemory #LLM #SemanticSearch #MultiAgent #AgenticAI #SoftwareEngineering #VectorSearch #AITooling
