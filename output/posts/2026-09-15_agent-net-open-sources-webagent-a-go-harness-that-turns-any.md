---
title: 'Agent-net Open Sources Webagent: A Go Harness That Turns Any Website into
  a Guarded AI Agent'
source: MarkTechPost
url: https://www.marktechpost.com/2026/09/14/agent-net-open-sources-webagent-a-go-harness-that-turns-any-website-into-a-guarded-ai-agent/
model: claude-code/sonnet
generated_at: '2026-09-15T20:37:22.210988'
score: 86
---

📌 一份JSON把你的網站變成受Guard保護的AI Agent

TL;DR：Agent-net開源Webagent，用Go打造的agent harness，靠declarative spec與action.Guard機制讓網站快速變身AI agent。

假設你不想寫一整套agent orchestration程式碼，只想填一份設定檔，就讓自己的網站能被其他AI agent找到、溝通、甚至完成交易，這正是Agent-net開源Webagent想解決的問題。

🤔 從網站到能對話的Agent

Agent-net本身在打造一個「agent對agent」的市場，讓AI agent之間可以互相發現、建立信任並付款。Webagent則是這個生態系底下開源出來的基礎建設：企業只需要填寫一份宣告式(declarative)JSON設定檔，在9個可插拔的slot中，每個slot挑選1個provider，執行`webagent serve`，就能讓自己的業務對外變成一個agent。

專案採Apache 2.0授權，目前程式碼建置正常(builds green)，也已經能實際跑在Slack、WhatsApp與HTTP等通道上，並由MCP工具支援。不過目前仍標示為v0版本，瀏覽器動作provider、OAuth-gated MCP、OTel輸出，以及AgentNet的身分與計費層，都還未完成。

🧩 一個Brain，多個可替換Slot

Webagent以Go語言撰寫，架構上一個agent等於1個Brain(一個LLM加上指令)，搭配一組定義在`core/`中的slot。每個slot都是一個Service Provider Interface，在`spi/`底下有一份provider註冊表與一個預設值。這個設計同時服務三種對象：靠選單設定的企業、靠註冊自訂provider延伸功能的企業，以及提供adapter的合作夥伴公司，沒有人需要fork核心程式碼。每個provider都必須通過該slot的一致性測試(conformance suite)才能被認證。

其中最重要的架構決策是`action.Guard`：無論工具來自action provider或是由host注入，每個agent持有的工具都會被包裝起來，讓選定的guardrail在動作真正執行前先過一次關卡，模型本身無法繞過這道防線。專案的DESIGN.md文件引用了一篇研究(arXiv 2511.19477)指出，決定agent任務成功與否的是架構而非模型能力本身，同一批模型在不同架構下的任務成功率可以相差到85%對50%，這也是Webagent把guardrail做成架構層強制項的理由。

🔌 從範例到接上真實MCP服務

預設的echo brain不需要任何憑證，因此`webagent validate`與`webagent serve`在兩份範例設定zomato.json、bakery.json上可以直接跑起來。要接上真實模型，可以透過`webagent keys set openrouter`把金鑰存進作業系統設定目錄，權限設為0600；金鑰不會寫進設定檔本身，且已匯出的環境變數永遠優先。openrouter與gateway都是相容OpenAI介面的client，內建tool-calling迴圈。

如果企業本來就有MCP伺服器，只要在設定檔中加入一個spec區塊，就能把它變成一個能主動行動的agent。內建的mcp action provider透過Streamable HTTP(支援JSON與SSE)連線，可用bearer或API key驗證，在建置階段就完成握手，並把每個工具交給agent，同時掛上前述的guard防線，因此`validate`指令回報的工具數量會是真實數字。

Slack與WhatsApp的通道adapter會驗證每個進來的webhook簽章、立即回應、透過平臺API回覆訊息、忽略自己發出的訊息，並對重試送達的訊息做去重。Slack的callback指向`/slack/events`，Meta的callback則指向`/whatsapp/webhook`。

密鑰管理則遵循一個命名規則：任何設定欄位名稱以`Secret`結尾，就會在建置階段透過所選的vault解析成實際憑證，因此設定檔本身可以安全地提交進版控；如果某個secret參照無法解析，建置會直接失敗，而不是在缺少憑證的情況下悄悄啟動通道。可觀測性方面，每一輪對話都會產生一個對齊OpenTelemetry GenAI規範的TurnTrace，另外還有一個`eval/`測試套件可以跑帶檢查點的情境測試。

🎯 實務啟示

對想快速把既有業務系統包裝成能與其他agent互動的工程師來說，Webagent提供了一個「不用重寫orchestration邏輯、只填設定檔」的路徑，而`action.Guard`把guardrail做成架構層強制而非選配的設計，也值得在自建agent系統時參考。不過v0階段仍缺OAuth-gated MCP與身分計費層，正式導入前得先評估這些缺口是否卡住你的場景。

🔗 來源
- 標題：Agent-net Open Sources Webagent: A Go Harness That Turns Any Website into a Guarded AI Agent
- 作者／機構：Michal Sutter, MarkTechPost
- 連結：https://www.marktechpost.com/2026/09/14/agent-net-open-sources-webagent-a-go-harness-that-turns-any-website-into-a-guarded-ai-agent/

#AIAgent #OpenSource #GoLang #MCP #AgentHarness #Guardrails #AgentToAgent #WebAgent #LLMTooling #AgentArchitecture
