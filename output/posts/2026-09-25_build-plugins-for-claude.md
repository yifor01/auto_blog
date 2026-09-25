---
title: Build plugins for Claude
source: Claude Blog
url: https://claude.com/blog/build-plugins-for-claude
model: claude-code/sonnet
generated_at: '2026-09-25T20:38:30.292600'
pinned: true
---

📌 Claude 開放外掛送審，開發者迎來新上架管道

TL;DR：Anthropic 推出外掛送審入口網站，開發者可包裝 MCP 連接器與 Agent Skills 正式上架 Claude 目錄。

每天有數百萬人把 Claude 接進自己的應用程式、工作工具與資料來源，但第三方開發者若想把自己的整合正式推廣出去，過去缺乏一個清楚的送審與追蹤流程。9 月 25 日，Anthropic 補上了這一塊。

🤔 **Plugin 是什麼、為誰而做**

Anthropic 說明，Plugins（外掛）會打包 MCP 連接器、Agent Skills，或兩者兼具，是目前建立 Claude 第三方擴充功能的主要方式。開發者完成外掛後，透過新推出的「目錄送審入口網站」提交，經審核通過即可上架 Claude 目錄。這個入口網站目前開放給付費 Claude 方案的開發者使用。

🧩 **兩種送審路徑，一套審核流程**

送審方式分兩種：一是「單一 MCP connector」，直接指向自己的遠端 MCP 伺服器；二是「Plugin bundle」，把 MCP 伺服器與 Skills 組合在一起，放上 GitHub，再提交該 repo 送審。若是在 Claude Code 中使用，外掛還可以包含 LSP、commands、hooks 與 agents。

整個入口網站提供三個環節的支援：
- **自動驗證**：每次提交都會立即進行檢查與安全掃描，方便提早抓到問題。
- **審核狀態追蹤**：可看到目前審核進度、安全掃描結果，以及建議的修改項目。
- **自主決定上架時間**：審核通過後，開發者自行決定何時正式發佈。

📊 **上架後的營運資料**

外掛上線後，開發者可透過使用分析，依「產品介面」與「版本」查看安裝數，藉此決定優化與新功能的優先順序。在被發現的層面，也能看到自己的上架頁面被查看次數，以及使用者是透過哪些搜尋字詞找到它，用來優化上架資訊的呈現方式。

🧩 **靠 MCP 2.0 打造更豐富的體驗**

Claude 已支援最新的 MCP 規格，也就是常被稱作「MCP 2.0」的版本，其核心採無狀態（stateless）設計。開發者可以透過兩項 MCP 延伸功能提升外掛體驗：**MCP Apps**（在對話中嵌入互動式 UI）與 **Enterprise Managed Auth**（企業使用者的零接觸 OAuth）。Anthropic 表示未來會支援更多 MCP 功能與延伸規格。

🎯 **實務啟示**

對已經在維護 Skill 或 MCP 連接器的開發者來說，不需要做任何改動，既有上架內容會持續保留在目錄中；Anthropic 表示未來幾週會在 Claude 與 Claude Code 上統一發現體驗，未來也計畫讓現有的連接器上架內容轉換為正式外掛。如果你正打算把自己的整合推廣給更多使用者，現在是透過官方送審流程正式上架、並取得使用數據回饋的好時機。

⚠️ **尚未說明的部分**

官方公告未提及審核所需時間、上架費用或具體的安全掃描標準，這些細節仍需開發者實際送審後才能掌握。

🔗 **來源**
- 標題：Build plugins for Claude
- 作者／機構：Anthropic
- 連結：https://claude.com/blog/build-plugins-for-claude

#Anthropic #Claude #MCP #PluginDevelopment #AgentSkills #DeveloperTools #ClaudeCode #AIEcosystem #OAuth #DeveloperPortal
