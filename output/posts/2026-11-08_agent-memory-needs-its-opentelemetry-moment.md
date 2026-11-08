---
title: Agent memory needs its OpenTelemetry moment
source: Hacker News
url: https://www.lorekit.io/blog/open-agent-memory-format
model: claude-code/sonnet
generated_at: '2026-11-08T21:19:20.640742'
score: 82
---

📌 AGENTS.md、記憶體工具、MCP知識圖譜:Agent記憶格式正在重演2019年以前的可觀測性亂局

TL;DR:四種常見的agent記憶格式彼此互不相通,作者主張這個領域需要一次OpenTelemetry式的整合。

打開任何一個正在認真用coding agent的開發機器,你大概會同時數到四種「記憶」的存放方式:倉庫裡的AGENTS.md或CLAUDE.md、Anthropic memory tool寫進/memories資料夾的檔案、GitHub Copilot記在自家伺服器上的倉庫事實,還有某個MCP記憶伺服器維護的JSONL知識圖譜。這篇在Hacker News拿下156點、101則留言的文章問了一個直白的問題:為什麼CI agent學到的教訓,換一個編輯器agent就完全讀不到?

🤔 **問題不是少了工具,是少了共識**

作者(同時也是開源記憶工具LoreKit的開發者)指出,去Reddit的r/ClaudeAI、r/LocalLLaMA或r/cursor晃一圈,會看到源源不絕的「我幫agent做了一個記憶層」貼文,每一篇都有自己的儲存方式、schema與MCP工具。這恰好證明問題是真實存在的,但也代表每多一個方案,就多一種別人讀不懂的格式。

🧩 **九種記憶家族,各自回答同一組問題但答案不同**

文章把目前市面上的做法整理成一張表,每一種都用「記憶的單位是什麼」「靠什麼定址」「如何被遺忘」三個維度描述:

| 類型 | 代表例子 | 記憶單位 | 定址方式 | 遺忘機制 |
|---|---|---|---|---|
| 指令檔案 | AGENTS.md、CLAUDE.md、Cursor .mdc規則 | 整份Markdown檔案 | 檔案路徑(Cursor再加glob) | 永不遺忘,靠人編輯 |
| Agent自管檔案 | Anthropic的memory tool | /memories下的一個檔案 | 模型自己挑的路徑 | 永不遺忘,除非模型自己刪除 |
| 託管倉庫事實 | GitHub Copilot Memory | 附程式碼引用的一條事實 | 單一repository | 28天未使用後自動刪除 |
| Context區塊 | Letta core memory | 有字數上限的標籤區塊 | agent上的標籤 | 永不遺忘,常駐在context裡 |
| 擷取式事實 | Mem0 | 服務從對話中擷取的事實 | user_id/agent_id/run_id/app_id | 可設定到期日 |
| 命名空間儲存 | LangGraph BaseStore | 一個JSON值 | namespace tuple加key | 可設TTL,預設讀取時重置 |
| 知識圖譜 | MCP reference memory server | 實體、關係、觀察 | 實體名稱 | 永不遺忘 |
| 時序圖譜 | Graphiti/Zep | 圖邊上的一條事實 | 實體加邊 | 事實會在兩條時間軸上被標記失效,而非直接刪除 |
| 定址紀錄 | LoreKit | 含scope、key、生命週期的紀錄 | scope字串加key | 永不遺忘,除非設定TTL |

文章認為每種做法都有值得保留的地方:Copilot Memory把「可對照程式碼的引用」和「預設會過期」做對了,只是被鎖在單一產品裡;LangGraph證明核心介面可以小到只有put(namespace, key, value);Graphiti正確地把「事實何時為真」和「事實何時被記錄」拆成兩條時間軸;AGENTS.md則證明一個放在固定路徑的純文字檔,也能變成一種標準。

💡 **可觀測性領域已經走過這條路**

作者把這個局面類比成2019年之前的可觀測性(observability)市場:當時每家廠商都有自己的agent、自己的函式庫與自己的資料格式,換廠商就等於重新埋一次程式碼。OpenTracing與OpenCensus原本互相競爭,最後在2019年合併成OpenTelemetry,業界同意在四層東西上不再競爭:資料模型(span、metric、log record的定義)、語意慣例(像service.name、http.*這類共用命名)、傳輸協定(OTLP)與參考實作(共用SDK與Collector)。廠商繼續在「拿到資料之後怎麼儲存、查詢、分析」上競爭。作者認為agent記憶現在正處於可觀測性2019年以前的狀態:格式還年輕,改起來成本還不高,而且MCP與AGENTS.md都已經落在Linux Foundation的Agentic AI Foundation底下,算是有個中立的場地。

文章也點出,現有的幾個提案——MacPaw Research的Portable Memory(一種.mem封裝格式,有可重現序列化、刪除墓碑tombstone與可選簽章,但作者自承尚未被廣泛採用)、2026年4月的Open Memory Protocol草案(把對話與衍生記憶打包成帶manifest的ZIP),以及Cognee可以從Mem0、Letta、Zep匯入的COGX格式——大多解決的是「匯出」問題,也就是把一個人的記憶從A廠商搬到B廠商。但coding工具還有第二個尚未解決的問題:「即時定址」,也就是當CI job、編輯器agent與審查機器人同時在同一個倉庫工作時,要怎麼讀寫同一個位置並對這個位置的意義達成共識。文章認為完整的規格需要同時處理匯出與即時定址,而共用的定址欄位可以放進每一筆記錄裡。

文中示範了一筆記錄可能長什麼樣子(欄位名稱並非正式提案,只是示意資料模型):

```yaml
spec: agent-memory/0.1
id: 8f0c2a6e-4b1d-4c7a-9e2f-3a5b6c7d8e9f
address: { level: repo, value: github.com/acme/checkout }
key: tests-need-local-postgres
kind: lesson
written_by: { type: agent, name: claude-code }
content_type: text/markdown
lifecycle: { expires_at: null, extended_by: write }
attributes: { vcs.pr: 482, ci.run_url: "https://ci.example/runs/123" }
```

frontmatter負責定義這筆記憶在哪裡為真(address與key)、它的身分(id)、何時失效(lifecycle),以及誰寫的(written_by);下面的Markdown內容才是記憶本身。作者強調規格不需要替「誰來寫記憶」這件事選邊站——人、模型自己,或是從對話中擷取的服務都可以——重點是要記錄下來,讓讀的一方知道該多信任這條記憶。

🎯 **對工程師的意義**

如果你正在替自己的coding agent或內部工具設計記憶層,這篇文章給的提示是:先把「定址(address+key)、身分(id)、生命週期(lifecycle)、來源(written_by)」這四件事想清楚,比急著挑一個現成的儲存後端更重要,畢竟現在改格式的成本還低。也值得留意Linux Foundation旗下的Agentic AI Foundation未來是否會像OpenTelemetry當年那樣,出面促成業界在資料模型與協定上達成共識。

🔗 **來源**
- 標題:Agent memory needs its OpenTelemetry moment
- 作者/機構:mthines
- 連結:https://www.lorekit.io/blog/open-agent-memory-format

#AgentMemory #OpenTelemetry #LLMAgents #MCP #AGENTSmd #AIInfrastructure #KnowledgeGraph #DeveloperTools #OpenStandards #CodingAgents
