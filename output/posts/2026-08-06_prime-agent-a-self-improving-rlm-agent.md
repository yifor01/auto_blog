---
title: 'Prime Agent: A self-improving RLM agent'
source: Hacker News
url: https://www.primeintellect.ai/blog/prime-agent
model: tencent/hy3:free
generated_at: '2026-08-06T08:32:27.596413'
score: 98
---

📌 【Xeophon 開源專案】Prime Agent：透過 RLM 與持續性架構，實現自我改進的 AI Agent

TL;DR：Prime Agent 透過 RLM 與持續性架構，讓 Agent 能以程式化方式操作自身上下文與子代理。

目前的 AI Agent 架構設計往往受限於舊時代模型的技術瓶限：固定的工具呼叫（tool-calling）模式與上下文壓縮（context compaction）機制，迫使模型必須在既定的腳手架（scaffolding）中掙扎，而非真正利用這些工具。設計者通常在開發時就寫死了子代理、提示詞（prompt）與記憶體，這些設定無法隨著 Agent 在執行過程中的學習而動態調整。

Xeophon 提出的 Prime Agent 旨在打破這種靜態限制，透過兩大核心抽象概念，讓 Agent 能夠隨著能力的提升而演進。

🧩 **核心架構：RLM 與持續性架構 (Continual Harness)**

Prime Agent 的設計核心在於將 Agent 的行為從「被動接受指令」轉向「程式化控制」：

*   **遞迴語言模型 (Recursive Language Model, RLM)**：將上下文（context）視為變數，並將委派子代理（sub-agent delegation）視為 REPL（互動式解釋器）中的函式呼叫。這讓模型可以編寫「語言模型程式碼」來對自身的上下文進行操作，並透過持續性的 REPL 擁有對歷史紀錄、子代理與工具的程式化存取權，從而處理極長時程的對話而不會遺失資訊。
*   **持續性架構 (Continual Harness)**：將架構本身的狀態（包含提示詞、技能、記憶體與子代理）抽象化，讓 Agent 能夠透過 CRUD（增刪查改）操作來管理這些狀態。這使得 Agent 可以在執行過程中，根據自身學到的經驗來更新或建立新的技能與代理。

📊 **透過 A2A 通訊實現多代理協作**

結合上述機制，Prime Agent 實現了強大的代理間通訊（Agent-to-Agent, A2A）：

*   **代理編排**：Agent 可以啟動持久性的子代理，並在後續流程中再次傳送訊息給它們。
*   **跨會話溝通**：不同 Prime Agent 會話之間可以直接進行通訊，實現複雜的任務編排。
*   **遞迴式視圖**：透過背景守護進程（background daemon），使用者可以進入任何一個子代理的視圖，並在巢狀結構中不斷深入探索不同層級的代理。

🛠️ **實作細節：以 IPython 核心為中心**

Prime Agent 的設計理念是讓模型能直接進行程式化工具呼叫（Programmatic Tool-Calling, PTC）：

*   **唯一的工具是 IPython 核心**：模型使用一個持續存在的 IPython kernel 作為其 REPL。其他的架構功能（如子代理、技能）都被實作為 kernel 中的函式。
*   **非同步子代理呼叫**：透過 `rlm()` 函式，模型可以非同步地啟動子代理（例如使用 `await rlm(...)`），並在子代理完成任務後透過 `agent_message.send()` 接收回傳結果。這支援了並行處理（fan-out）任務，讓模型可以同時啟動多個專家代理進行獨立工作。
*   **記憶體與狀態管理**：
    *   **Session 紀錄**：完整的對話歷史儲存在硬碟的 append-only JSONL 檔案中，支援分支、分叉與複製。
    *   **自動壓縮**：當上下文達到閾值時，會透過另一個專門擔任「垃圾回收（garbage collector）」角色的 Agent 來非同步地進行壓縮與清理，以避免 REPL 記憶體堆積。
    *   **資源優化**：閒置 30 分鐘的代理會從記憶體移除，僅保留在磁碟中，一旦被存取便會立即重新載入。

🎯 **實務啟示**

對於開發者而言，Prime Agent 提供了一種全新的思考範式：不再僅僅是撰寫 Prompt，而是將 Agent 視為一個可以透過程式碼操控自身狀態與工具的執行環境。這種設計對於開發需要長期運作、具備自我演進能力或需要複雜多代理協作的自主評估（autonomous evaluation）與研究任務具有高度價值。

🔗 **來源**
- 標題：Prime Agent: A self-improving RLM agent
- 作者／機構：Xeophon
- 連結：https://www.primeintellect.ai/blog/prime-agent

#AI #Agent #MachineLearning #OpenSource #RLM #Python #IPython #MultiAgent #SoftwareEngineering #AutonomousAgents
