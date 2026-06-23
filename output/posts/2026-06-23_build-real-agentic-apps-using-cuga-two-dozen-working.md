---
title: 'Build real agentic apps using CUGA: two dozen working examples on a lightweight
  harness'
source: HuggingFace Blog
url: https://huggingface.co/blog/ibm-research/cuga-apps
score: 100
model: google/gemma-4-31b-it:free
generated_at: '2026-06-23T20:25:14.235844'
---

📌 【IBM Research】用 CUGA 快速建構 Agentic Apps：擺脫繁瑣的基礎設施開發

TL;DR：IBM 推出的開源工具 CUGA 簡化 Agent 開發，讓工程師只需定義工具與提示詞即可快速部署。

大多數 Agent 應用在真正發揮作用前，往往需要花上一週時間處理「水管工程」：選擇框架、對接模型客戶端、撰寫工具介面卡，以及建立 UI 的狀態串流。開發者往往在處理這些基礎建設後，才開始思考 Agent 實際上要做什麼。

🧩 **將開發重心從「基礎建設」轉向「核心邏輯」**

CUGA (Configurable Generalist Agent) 採取了相反的開發邏輯。作為一個輕量級的 Agent Harness，它將規劃 (planning)、執行迴圈 (execution loop)、工具呼叫 (tool calls) 以及狀態管理 (state plumbing) 等繁瑣過程自動化。

對於工程師而言，開發流程被簡化為僅需定義兩項內容：
1. Agent 可以呼叫的工具列表 (Tool list)
2. 給予 Agent 的指令 (Prompt)

🛠️ **透過 24 個單一檔案範例證明開發效率**

為了證明 CUGA 的實用性，IBM 團隊建構了 `cuga-apps` 專案，包含 24 個實際運作的小型應用。這些應用的特點在於：
- **極簡結構**：每個應用僅為一個單一的 FastAPI 檔案，並封裝一個 `CugaAgent`。
- **多樣化場景**：範例涵蓋從「電影推薦系統」到「IBM Cloud 架構顧問」等不同用途。
- **低學習門檻**：不需要學習複雜的新框架，只要會寫 FastAPI 路由，就能讀懂所有程式碼。

🚀 **從開發到生產環境的無縫接軌**

CUGA 的設計目標是讓同一套程式碼在開發階段與生產環境之間輕鬆遷移。開發者可以使用 `pip install cuga` 快速開始，而同一套邏輯在進入生產環境時，可以在無需重新撰寫程式碼的情況下，直接在受治理 (governed) 且主權獨立 (sovereign) 的環境中執行。

🎯 **實務啟示**

對於需要快速驗證 Agent 想法的工程師，CUGA 提供了一種「範本導向」的開發路徑。與其從零開始搭建框架，不如直接參考 `cuga-apps` 的單一檔案範例進行複製與修改，將開發時間從基礎設施的對接，轉移到工具定義與提示詞的最佳化上。

🔗 **來源**
- 標題：Build real agentic apps using CUGA: two dozen working examples on a lightweight harness
- 作者／機構：HuggingFace / IBM Research
- 連結：https://huggingface.co/blog/ibm-research/cuga-apps

#AI #Agent #IBMResearch #CUGA #FastAPI #OpenSource #LLM #AgenticAI #SoftwareEngineering #DeveloperProductivity
