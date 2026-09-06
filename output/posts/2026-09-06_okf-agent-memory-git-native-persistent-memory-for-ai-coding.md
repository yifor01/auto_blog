---
title: OKF Agent Memory – Git-native persistent memory for AI coding agents
source: Hacker News
url: https://github.com/okf-memory/okf-agent-memory
model: claude-code/sonnet
generated_at: '2026-09-06T19:17:10.784510'
score: 87
---

📌 用Git取代向量資料庫：AI Agent的持久記憶新方案

TL;DR：OKF Agent Memory把AI coding agent的專案記憶存成純Markdown，靠本地BM25在微秒等級完成搜尋，零嵌入API成本。

AI coding agent每次關掉context window，架構決策、領域知識與操作事實往往就跟著蒸發——除非你把它寫進版本控制系統。OKF Agent Memory給的答案很直接：別用黑盒向量資料庫，直接存進git。

🤔 **CLAUDE.md不夠結構化，向量DB又太黑盒**

README指出，目前多數團隊的做法要嘛是CLAUDE.md、AGENTS.md這類非結構化的ad-hoc markdown檔案，要嘛是複雜的向量資料庫（如Mem0、Letta）。OKF Agent Memory想在這兩者之間搭一座橋：提供一個標準化、廠商中立的記憶層，以純Markdown加YAML frontmatter的形式，直接活在專案repo的`knowledge/`目錄下。

🧩 **建立在Google OKF v0.2規格上的五層架構**

這個專案基於Open Knowledge Format（OKF）v0.2，架構分五層：規範性的Markdown/YAML格式規格、行為層的Agent Memory Convention（規定搜尋、審查、信任等規則）、給LLM用的Agent Skill、Go語言撰寫的工具層（負責解析、驗證、搜尋、MCP），以及最底層的專案知識語料庫本身。

幾個核心設計理念：完全git-native，一切都是版本控制的純文字，可用標準的`git diff`與`git log`審查agent的記憶內容，不需要外部資料庫；本地BM25詞彙檢索取代向量embedding，省去持續性的API呼叫成本；每個知識概念支援provenance（來源標註）、trust tiers（generated對比verified的信任分級）與生命週期metadata（status、stale_after）；用Progressive Disclosure，也就是層級式的`index.md`與連結圖，讓agent只載入真正需要的概念，藉此解決README所稱的「context bloat」與「memory rot」問題；並強制「Search-Before-Write」原則，要求agent在寫入新知識前先搜尋既有記憶，避免概念重複與幻覺式的分歧內容。

📊 **README自報的效能基準**

README提供了一份與Python/向量DB方案（Mem0、Letta）以及Deno/Node.js工具鏈的效能對比：

| 項目 | Python/向量DB | Deno/Node.js | OKF Agent Memory (Go) |
|---|---|---|---|
| 概念搜尋延遲 | 150–800ms | 40–120ms | <300微秒 |
| 完整語料庫解析＋圖驗證 | 200ms–1.5s | 80–250ms | 約4.0ms |
| 程序冷啟動開銷 | 250–600ms | 80–180ms | <4ms |
| 每千次查詢檢索成本 | 約0.10–0.50美元 | 0美元 | 0美元 |
| 記憶體佔用 | 120–350MB | 60–140MB | <15MB |

需要說明的是，這些數字是專案自行提供的benchmark結果，README也附上了自動化的benchmark runner供使用者用自己的硬體（LM Studio／Ollama搭配Gemma、Qwen、Llama等）重現。

🧩 **怎麼用**

安裝方式是clone repo後執行`make build`，會產生獨立執行檔`bin/okf`。基本CLI指令包括`okf validate knowledge --strict --drift`驗證bundle一致性與圖連通性、`okf search "關鍵字" knowledge`做BM25搜尋、`okf show`檢視概念與其關聯、`okf create`／`okf update`建立或更新概念。README也提供一鍵指令`okf bootstrap /path/to/project --name "My Project"`，可把完整的記憶架構（`knowledge/`目錄、`.agents/skills/okf-memory/`、`AGENTS.md`、Makefile）直接建置進任何新舊專案。

工具內建原生的Model Context Protocol（MCP）伺服器，透過`okf mcp knowledge`啟動，可接進Claude Code、Cursor、Codex等平臺，設定方式與一般MCP server相同，在`claude_desktop_config.json`或Cursor設定中指定執行檔路徑與`mcp`參數即可。

⚠️ **仍是詞彙檢索，且缺乏第三方驗證**

README將自己定位為「domain-neutral」，並提供軟體工程、教練、科學研究、文獻回顧、營運等領域的範例bundle。不過目前所有效能與token節省數字（包括宣稱的「-80% token reduction」）都是專案方自行測得，尚未見到獨立第三方驗證。此外，這套方案採用的是本地BM25詞彙檢索，而非向量語意檢索，素材中並未說明兩者在語意相似度查詢上的表現差異，這是評估時需要自行留意的部分。

🎯 **實務啟示**

對已經在用CLAUDE.md或AGENTS.md管理agent上下文的團隊，這提供了一條可版本控制、免嵌入API成本、且能直接用git審查的記憶路徑；內建的MCP server也讓它能無痛接入現有的Claude Code、Cursor等工作流。如果你的專案本來就重視知識的可追溯性（provenance）與生命週期管理，OKF v0.2的trust tiers設計值得參考。

🔗 **來源**
- 標題：OKF Agent Memory – Git-native persistent memory for AI coding agents
- 連結：https://github.com/okf-memory/okf-agent-memory

#AIAgent #GitNative #OpenSource #MCP #KnowledgeManagement #DeveloperTools #AgentMemory #GoLang #BM25 #ContextEngineering
