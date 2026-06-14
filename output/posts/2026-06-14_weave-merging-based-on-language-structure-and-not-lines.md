---
title: 'Weave: Merging based on language structure and not lines'
source: Hacker News
url: https://ataraxy-labs.github.io/weave/
score: 93
model: google/gemma-4-31b-it:free
generated_at: '2026-06-14T19:36:53.529501'
---

📌 【Weave】別再讓 Git 衝突毀掉開發體驗：從「行級合併」進化到「語義級合併」

當兩個 AI Agent 同時修改同一個檔案的不同函數時，你還在面對 Git 那種令人頭痛的 `<<<<<<< HEAD` 衝突嗎？雖然修改的位置不同，但只要行數重疊，Git 的行級（Line-level）合併機制就得請人類出來手動解決。

🤔 **Git 的行級合併，已無法跟上 AI 協作的節奏**

傳統 Git 的合併邏輯非常簡單：比對每一行的變動。這種設計在人類協作時尚可，但在 AI Agent 時代，一個 Agent 可能在 1 秒內重構整個類別，導致大量行級衝突。即使邏輯上並不衝突（例如 A 改了 Function 1，B 改了 Function 2），Git 仍會因為行號變動而判定為衝突。

這種「行級依賴」成了多 Agent 並行開發的最大瓶頸。

🧪 **利用 Tree-sitter 實現實體級（Entity-level）解析**

Weave 提出了一個核心方案：將 Git 的合併驅動程式（Merge Driver）從「比對行」升級為「比對結構」。

其技術實現路徑如下：
1. **語義解析**：利用 `tree-sitter` 解析程式碼，將檔案拆解為函數（Function）與類別（Class）等語義實體（Entities）。
2. **實體級合併**：合併時不再看行號，而是看哪個實體被修改。如果兩個 Agent 分別修改不同的函數，即便在同一個檔案中，也能實現 100% 的 Clean Merge。
3. **跨語言支持**：目前已在 7 種程式語言的 31 種合併場景中完成驗證。

💡 **透過 MCP 協議，讓 AI Agent 在編輯前先「佔位」**

Weave 不僅僅是一個合併工具，它還整合了 Model Context Protocol (MCP)，將合併邏輯前移到「編輯前」：

- **實體聲明（Claiming Entities）**：AI Agent 在編輯前可以先「聲明」它要修改的實體。
- **衝突預測**：在衝突發生前就偵測到潛在衝突，而非在 `git merge` 時才發現。
- **工具整合**：提供 15 種透過 MCP 的工具，讓 Claude 等 AI Agent 能直接調用，實現更精準的協作流。

⚠️ **目前聚焦於實體級合併，複雜邏輯衝突仍需關注**

Weave 解決了結構性的合併問題，但對於「同一個函數內」的邏輯衝突，仍需依賴其定義的合併策略或人工介入。此外，其效能表現與對極端邊緣案例的處理能力，在更大規模的專案中仍有待實測。

🎯 **AI 團隊領袖與工程師的實務啟示：從「事後解決」轉向「事前協調」**

如果你正在建構多 Agent 的自動化開發工作流（Multi-agent workflows），Weave 提供了兩種應用路徑：
- **純合併驅動**：直接替換 Git 的 merge driver，減少無謂的行級衝突。
- **協調工作流**：利用其 MCP 工具讓 Agent 在編輯前進行協調，將「衝突解決」從合併階段提前到開發階段。

對於追求極致自動化的 AI 工程團隊來說，將合併邏輯從「行」提升到「語義實體」，是實現真正無縫 AI 協作的關鍵一步。

🔗 **專案連結**
📝 Weave: Merging based on language structure and not lines
👤 作者：rohanat
🔗 官網：https://ataraxy-labs.github.io/weave/

你認為 AI 時代的版本控制應該如何演進？你會願意將 Git 的合併權限交給語義解析工具嗎？歡迎在下方討論 👇

#AI #Git #SoftwareEngineering #TreeSitter #MCP #MultiAgent #LLM #開發工具
