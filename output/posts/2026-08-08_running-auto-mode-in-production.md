---
title: Running auto mode in production
source: Claude Blog
url: https://claude.com/blog/auto-mode-in-production
model: tencent/hy3:free
generated_at: '2026-08-08T06:41:02.062167'
pinned: true
---

📌 【Anthropic】Claude Code 開啟 Auto Mode：在生產環境中取得速度與安全的平衡

TL;DR：Claude Code 預設開啟 Auto Mode，透過分類器自動判斷指令安全性，讓開發者能進行長時程任務並提升 9 倍效能。

在 Agentic Coding（代理編程）的發展過程中，開發者一直面臨一個兩難：是要讓人類介入每一個指令（確保安全但速度慢），還是完全跳過權限檢查（速度快但有風險）？Anthropic 透過 Claude Code 推出的 Auto Mode 試圖解決這個權限疲勞與安全性之間的衝突。

🧩 **核心機制：用分類器取代手動核准**

Auto Mode 不再要求開發者逐一核准 Agent 想要執行的每一個指令。其技術邏輯如下：
- **自動評估**：系統內建一個分類器（Classifier），會對每一項行動進行評估。
- **風險攔截**：如果動作看起來具備潛在危害，分類器會直接攔截該指令。
- **效能提升**：由於減少了人工干預，Claude 在使用過程中的平均執行時間比原本的預設設定增加了 9 倍。
- **安全性驗證**：內部測試顯示，該分類器捕捉危險動作的準確度，甚至比開發者手動點擊核准時更精準，且通過了第三方紅隊測試（Red-teaming）。

📊 **實務應用：從自動駕駛到醫療科技的案例研究**

不同產業的團隊正透過 Auto Mode 改變其開發工作流：

**1. Nuro（自動駕駛技術）**
- **長時程研究代理人**：工程師利用 Auto Mode 啟動需要執行數小時的任務。例如，Agent 可以在深夜自動研究測試失敗的案例、撰寫提案並進行實驗，並在清晨產出 Pull Request。
- **並行處理**：工程師可以同時開啟三到四個 Auto Mode 會話並行工作，無需全程監控。
- **安全護欄**：工程師會預先在設定中禁止最危險的指令（如遞迴刪除），分類器則在這些護欄內進行判斷。

**2. Gusto（SMB 技術公司）**
- **減少權限負擔**：工程師發現使用 Auto Mode 後，團隊整體的權限管理負擔明顯下降。
- **防止提示詞注入**：透過檢查指令是否符合原始需求，Auto Mode 能有效防止 Prompt Injection（提示詞注入）導致的錯誤操作。
- **風險分級**：在涉及生產環境基礎設施（如 Terraform、AWS 或直接對 API 發送 POST 請求）時，工程師仍會切換回互動模式進行人工驗證。

**3. Garner Health（醫療科技）**
- **標準化開發生命週期**：透過 Auto Mode，公司成功為整個工程組織建立了一套標準化的軟體開發生命週期（SDLC）。
- **自動化重複任務**：員工利用此模式將每週花在重複性工作上的時間大幅縮減，且無需長時間監控代理人。

🎯 **實務啟示**

對於正在導入 AI Agent 的工程團隊而言，Auto Mode 提供了一個「防禦縱深」（Defense-in-depth）的範例：
- **不要依賴單一層級**：結合「預設禁令（Skills/Guardrails）」、「自動分類器（Classifier）」以及「關鍵任務人工核准（Manual Review）」來構建安全網。
- **目標導向的自動化**：當任務具備清晰、可量化的指標（如測試通過率或記憶體佔用率）時，使用 Auto Mode 進行自主迭代（Hill-climbing）能發揮最大效能。

🔗 **來源**
- 標題：Running auto mode in production
- 作者／機構：Molly Vorwerck @ Anthropic
- 連結：https://claude.com/blog/auto-mode-in-production

#AI #ClaudeCode #Anthropic #SoftwareEngineering #AgenticAI #Productivity #LLM #DevTools #Automation #MachineLearning
