---
title: Agent Skill to Force Docs in ASD-STE100 Simplified Technical English
source: Hacker News
url: https://github.com/AminBlg/SimpleEnglish
model: tencent/hy3:free
generated_at: '2026-07-31T08:47:45.884981'
score: 76
---

📌 【開源專案】拒絕 AI 廢話：用 Agent Skill 強制 LLM 寫出波音等級的技術文件

TL;DR：這是一個輕量級 Agent Skill，強制 LLM 使用 ASD-STE100 標準撰寫技術文件，避免 AI 生成過於口語或冗長的內容。

🎣 你的 AI 寫出來的東西像 LinkedIn 貼文，還是像波音公司的維修手冊？

當我們習慣了 LLM 產出的流暢、但有時過於囉唆且充滿修飾語的文字時，對於需要極高精準度的工程領域來說，這可能是一場災難。一個新的開源專案 `SimpleEnglish` 提出了解決方案：透過 Agent Skill 規範，讓 LLM 嚴格遵守 ASD-STE100 標準。

🧩 **讓技術文件回歸精準的 ASD-STE100 標準**

在航太領域，為了避免疲憊的維修人員誤讀指令，自 1983 年以來便採用了 ASD-STE100 簡化技術英語（Simplified Technical English）。

這個專案的核心設計理念是：
- **強制規範**：將 LLM 的輸出限制在受控語言（Controlled Language）範圍內。
- **消除 AI Slop**：透過嚴格的語言規範，從根本上減少 AI 生成內容中常見的冗餘與廢話（Slop）。
- **輕量化設計**：單一資料夾、零依賴（no dependencies），採用 MIT 授權。

🤖 **支援多種主流 Agent 架構**

該工具並非侷限於單一工具，而是採用 Agent Skills 標準，可以無縫整合進各種開發環境與 Agent Harness 中，包含：
- Claude Code
- Cursor
- VS Code Copilot
- OpenAI Codex
- Gemini CLI
- Goose
- OpenCode
- 以及其他約 25 種支援該標準的工具。

📊 **從「流暢口語」轉向「精準指令」**

根據專案提供的範例對比：
- **未載入 Skill 時**：AI 會產出如「為了避免在後續過程中遇到令人沮喪的權限問題，您應該確保 AWS 憑證已正確配置」這類過於口語且冗長的敘述。
- **載入 Skill 後**：輸出會變得極度精簡且指令明確，符合技術手冊的嚴謹要求。

🎯 **實務啟示**

對於需要撰寫維修手冊、操作指南或高度精密技術文件的工程團隊來說，這種「強制規範語言」的 Agent Skill 提供了一種低成本且高效的方法，能在生成階段就從源頭控制文件品質，降低人工審核與修正的成本。

🔗 **來源**
- 標題：Agent Skill to Force Docs in ASD-STE100 Simplified Technical English
- 連結：https://github.com/AminBlg/SimpleEnglish

#AI #AgentSkills #LLM #ASDSTE100 #TechnicalWriting #OpenSource #SoftwareEngineering #Aerospace #AIProductivity #SimplifiedEnglish
