---
title: 'Meet EverOS: An Open Source Markdown-First Agent Memory Runtime With Hybrid
  BM25 + Vector Retrieval and Self-Evolving Skills'
source: MarkTechPost
url: https://www.marktechpost.com/2026/06/29/meet-everos-an-open-source-markdown-first-agent-memory-runtime-with-hybrid-bm25-vector-retrieval-and-self-evolving-skills/
score: 97
model: google/gemma-4-31b-it:free
generated_at: '2026-06-29T20:25:57.528875'
---

📌 【開源專案】EverOS：將 Markdown 作為 AI Agent 的記憶基底，實現可編輯、可版本控制的記憶執行時

TL;DR：EverOS 透過 Markdown 儲存記憶並結合混合檢索，讓 AI Agent 的記憶視覺化且易於維護。

大多數 AI Agent 面臨的最大痛點是 LLM 的無狀態特性：對話一旦結束，上下文便隨之消失。雖然向量資料庫是常見解法，但將記憶「鎖」在黑盒子中讓開發者難以除錯與管理。

🤔 **用 Markdown 檔案取代傳統記憶黑盒子**

EverOS 提出了一種不同的設計理念：不再將記憶僅僅儲存在向量資料庫中，而是將記憶寫作純 Markdown (.md) 檔案。這些檔案成為 Agent 在不同對話 session 之間讀取、編輯與搜尋的「唯一事實來源 (Source of Truth)」。

這意味著開發者可以直接用文字編輯器開啟記憶、使用 grep 搜尋，甚至透過 Git 進行版本控制，或直接在 Obsidian 中檢視 Agent 記住了什麼。

🧩 **雙軌記憶設計與輕量化架構**

EverOS 並非僅記錄聊天紀錄，而是將記憶拆分為兩條獨立軌道，這在現有的記憶函式庫中較為少見：
- **使用者端記憶 (User-side)**：儲存個人檔案 (Profiles)、事件 (Episodes)、事實 (Facts) 與預見 (Foresights)。
- **Agent 端記憶 (Agent-side)**：儲存案例 (Cases) 與技能 (Skills)。

在實作層面上，EverOS 採用了極簡的儲存堆疊，大幅降低運維成本，不需要 MongoDB、Elasticsearch 或 Kafka 等重型元件：
1. **Markdown**：作為事實來源。
2. **SQLite**：管理狀態與佇列。
3. **LanceDB**：處理向量 (Vector)、BM25 以及純量過濾 (Scalar filters)。

⚙️ **開發者友好的整合方式**

EverOS 是一個 local-first 的 Python 函式庫，設計目標是讓開發者能直接將其「丟進」現有的 Agent 迴圈中，而不需要重構整個技術棧。

- **API 相容性**：採用 OpenAI 協定，僅需更改 base URL 即可連線 OpenAI, OpenRouter, vLLM, Ollama 或 DeepInfra。
- **執行模式**：以伺服器形式執行，提供 CLI 與 FastAPI HTTP API，且全程採非同步 (async-first) 設計。
- **演算法分離**：記憶提取演算法由獨立的無狀態函式庫 EverAlgo 處理，EverOS 則負責編排與持久化。

📊 **混合檢索與部署靈活性**

EverOS 採用混合檢索機制，透過單次 LanceDB 查詢同時結合 BM25 與向量檢索，提升記憶找回的精準度。

在部署方面，預設為本地優先 (local-first)，確保資料不離開環境且每一層都可被檢查。對於不想自行維運的團隊，官方也提供了 EverOS Cloud 託管選項，兩者共享相同的 SDK、檢索引擎與記憶格式。

🎯 **實務啟示**

對於開發 Agent 的工程師來說，將記憶轉化為 Markdown 檔案提供了一個巨大的除錯優勢。你可以直接手動修改 `.md` 檔案來「修正」Agent 的記憶，而不需要透過複雜的 API 去操作向量空間。這種「視覺化記憶」的設計，讓 Agent 的行為變得更可預測且易於調校。

🔗 **來源**
- 標題：Meet EverOS: An Open Source Markdown-First Agent Memory Runtime With Hybrid BM25 + Vector Retrieval and Self-Evolving Skills
- 作者／機構：Asif Razzaq
- 連結：https://www.marktechpost.com/2026/06/29/meet-everos-an-open-source-markdown-first-agent-memory-runtime-with-hybrid-bm25-vector-retrieval-and-self-evolving-skills/

#AI #OpenSource #LLM #AIAgents #Markdown #VectorDatabase #LanceDB #Python #MemoryRuntime #RAG
