---
title: MCP servers can now ship skills, run tasks, and more with Claude
source: Claude Blog
url: https://claude.com/resources/articles/skills-over-mcp-tasks-and-more
model: claude-code/sonnet
generated_at: '2026-11-25T01:36:20.953671'
pinned: true
---

📌 Anthropic 更新 MCP：伺服器也能像另一個 agent 跟 Claude 合作

TL;DR：MCP 新增 Skills、Tasks、Elicitation、File Uploads，讓伺服器能做更長、更互動的工作。

工具名稱和描述能告訴 Claude「伺服器會做什麼」，卻說不清楚「遇到特定情境該怎麼做」。這正是 Anthropic 這次更新要補上的缺口。

🤔 從工具呼叫，到真正的協作

兩年前，Anthropic 推出 Model Context Protocol（MCP），作為連接 AI agent 與資料所在系統的標準。隨著 agent 在生產環境中承擔越來越長、越來越重要的工作，這次更新讓 Claude 能用更像「與另一個 agent 合作」的方式跟伺服器互動：向它學習、把工作委派給它，並在過程中交換輸入與檔案。

🧩 四項新能力

- Skills over MCP（公開 beta）：伺服器可以把 skill 和工具一起發布，讓 Claude 承接更長、多步驟的工作。Claude 只在需要時才載入 skill，維持低 context 用量；skill 會隨伺服器更新，使用者不需要額外安裝。Shopify 用它協助 Claude 端到端設計與更新商家的線上商店；HubSpot 用它幫新客戶完成 onboarding 並在 Claude 中建立好帳號；Atlassian 用它讓 Claude 取得組織內部的深層脈絡以支援分析與工作。
- Tasks（正式發布）：過去工具呼叫必須執行完才能讓 Claude 繼續動作。有了 Tasks，伺服器可以在背景執行耗時的操作，甚至整個 agent loop，Claude 可以繼續做其他事，等結果準備好再接續處理。ZoomInfo 用 Tasks 執行過去需要多輪提示才能完成的更深入帳戶與聯絡人研究。
- Elicitation（正式發布）：像花錢或刪除資料這類需要使用者簽核的動作，伺服器現在可以暫停，透過表單或連結向使用者要輸入，再接續原本的流程。Supabase 用它在建立付費專案或執行有破壞性的 SQL 前先確認費用；Railway 用它在進行可能具破壞性的變更（例如移除一個 service）前先詢問；GitHub 則要求使用者在 agent 刪除 repository 前輸入該 repository 的名稱。
- File Uploads（即將推出）：Claude 將能把檔案而不只是文字傳給 MCP 伺服器。這個擴充功能能在不經過 context window 的情況下，把 PDF、表格與圖片送到伺服器。

📊 生態系的規模

Anthropic 提到，MCP 目前每月有超過 7 億次 SDK 下載，Claude 上也有超過 10,000 個 MCP connector。過去一年，MCP 在 Claude 中變得更有效率：Tool search 讓工具定義只在需要時載入，在多伺服器環境下可減少超過 85% 的 context 用量；最新的 spec 採用 stateless 設計，讓伺服器更容易建置與維護擴充性；Enterprise Managed Auth 擴充讓管理員能一次性授權支援的伺服器，使用者就能自動連線；MCP Apps 擴充則能把完整介面帶進 Claude，顯示在對話旁或全螢幕。

💡 這些都是開放標準的延伸

Skills over MCP、Tasks、Elicitation、File Uploads 都是開放 MCP spec 與其擴充功能的一部分，支援這些功能的伺服器可以在任何相容的 client 上運作，不只限於 Claude。Skills over MCP 與 Tasks、Elicitation 目前已在 Claude 與 Claude Code 的 Pro、Max、Ultra 方案中可用，並逐步推展到 Team 與 Enterprise 組織。

🎯 給正在開發 MCP 伺服器的工程師

如果你的 MCP 伺服器只靠工具名稱與描述讓 agent 猜該怎麼做，現在值得評估是否該用 Skills over MCP 補上操作手冊與最佳實務；如果伺服器有耗時的操作或需要使用者確認的敏感動作，Tasks 和 Elicitation 分別提供了背景執行與中途詢問的標準做法，不必自己手搭一套輪詢或 webhook 機制。

🔗 來源
- 標題：MCP servers can now ship skills, run tasks, and more with Claude
- 作者／機構：Anthropic
- 連結：https://claude.com/resources/articles/skills-over-mcp-tasks-and-more

#MCP #ModelContextProtocol #Claude #Anthropic #AIAgent #DeveloperTools #AgenticAI #APIDesign #ClaudeCode #OpenStandard
