---
title: OthmanAdi/planning-with-files
source: GitHub Trending
url: https://github.com/OthmanAdi/planning-with-files
score: 87
model: google/gemma-4-31b-it:free
generated_at: '2026-07-05T19:32:20.416041'
---

📌 **讓 AI Agent 擁有記憶：用檔案持久化解決長任務的 Context 遺失問題**

TL;DR：透過在磁碟維護規劃檔案，讓 AI 編碼 Agent 能在崩潰或 Context 遺失後快速恢復進度。

當 AI Agent 處理複雜的編碼任務時，最令人沮喪的莫過於因為 Context 視窗滿了、執行 `/clear` 或程式崩潰，導致 Agent 突然「失憶」，忘記目前執行到哪裡以及接下來要做什麼。

🧩 **將規劃過程「實體化」為檔案**

`planning-with-files` 提出了一套持久化的檔案規劃技能 (file-based planning skill)，不再將任務進度僅依賴於對話記憶體，而是直接在磁碟上維護三個關鍵檔案：

- `task_plan.md`：記錄整體任務規劃。
- `findings.md`：記錄執行過程中發現的資訊。
- `progress.md`：追蹤目前的執行進度。

這種設計讓 Agent 能夠在面對 Context 遺失或系統崩潰時，透過讀取這些檔案來生存並恢復工作狀態。

💡 **v3.0.0 新增：自主模式與完成閘門**

在最新的 v3.0.0 版本中，作者引入了兩種新模式以應對長時程 (long-running) 的 Agent 執行：

- **自主與閘門模式 (Autonomous and Gated modes)**：提供可選擇開啟的執行選項。
- **完成閘門 (Completion gate)**：這是一個關鍵機制，會將 Agent 攔截並持有，直到計畫真正完成為止，防止 Agent 在任務未完時提前結束。

🧩 **標準化整合與社群擴充套件**

該專案透過 `SKILL.md` 標準，可安裝於超過 60 種不同的 Agent 中。由於其設計靈活性，社群已衍生出多種擴充套件版本：

- **工作流最佳化**：如 `devis` 引入面試優先 (Interview-first) 的工作流。
- **能力擴充套件**：`multi-manus-planning` 增加多專案支援與 Git 同步；`plan-cascade` 實現多層級任務編排與平行執行。
- **特定場景**：`agentfund-skill` 嘗試將里程碑託管引入 Agent 募資；`openclaw-github-repo-commander` 則將其用於七階段的 GitHub 倉庫審計與清理。

🎯 **實務啟示**

對於開發 AI Agent 的工程師來說，這提供了一個簡單且有效的「外部記憶」實作方案。與其嘗試不斷擴大 Context Window，不如將「狀態」與「邏輯」分離，將規劃狀態持久化在檔案系統中，能顯著提升 Agent 處理長任務的穩定性與可靠度。

🔗 **來源**
- 標題：planning-with-files
- 作者／機構：OthmanAdi
- 連結：https://github.com/OthmanAdi/planning-with-files

#AI #AIAgent #OpenSource #LLM #SoftwareEngineering #ContextWindow #Planning #CodingAssistant #GitHub #DeveloperTools
