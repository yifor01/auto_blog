---
title: 'Agent Harness vs Agent Framework vs MCP: Which Layer Owns the Loop, State,
  Tools, Permissions, and Recovery'
source: MarkTechPost
url: https://www.marktechpost.com/2026/09/14/agent-harness-vs-agent-framework-vs-mcp-which-layer-owns-the-loop-state-tools-permissions-and-recovery/
model: claude-code/sonnet
generated_at: '2026-09-15T20:37:22.211174'
score: 84
---

📌 Harness、Framework、MCP：誰真正管執行迴圈？

TL;DR：三者常被混用，但在迴圈、狀態、工具傳輸、權限、復原五個面向，各自扮演不同角色。

當你聽到「agent harness」「agent framework」「MCP」被交替使用時，很容易誤以為它們是同一件事的不同稱呼。實際上，這三層各自擁有不同的預設責任範圍，也在邊界處逐漸重疊，本文用一個問題把它們拆開：哪一層真正「擁有(owns)」執行迴圈、狀態、工具傳輸、權限與復原機制？「擁有」代表這一層定義並強制執行該行為；「暴露(exposes)」則代表這一層只提供掛鉤(hook)，但不決定政策。

🤔 每個agent都在跑同一個迴圈

不論是harness還是framework，執行的都是同一套基本迴圈：把上下文送給模型、讀取回應、執行工具呼叫、把結果餵回去、重複。兩者的差異在於你能控制這個迴圈到什麼程度，而不是迴圈本身的存在與否。

🧩 MCP：唯一由它自己完全擁有的一層

工具傳輸(tool transport)是文中唯一明確由MCP單獨擁有的一列。MCP定義了三種伺服器端原語：tools(模型可執行的函式)、resources(上下文與資料)、prompts(範本化的工作流程)。Client端可以選擇支援elicitation，讓伺服器能主動向使用者要求更多輸入。傳輸層則是JSON-RPC 2.0，跑在stdio或Streamable HTTP之上。

2026-07-28的規格修訂讓`Mcp-Method`與`Mcp-Name`這兩個HTTP header成為必填，讓gateway與rate limiter可以直接依header路由，不必解析請求本文；同時也讓`tools/list`的回應可以透過`ttlMs`與`cacheScope`快取，並宣告淘汰舊有的HTTP+SSE傳輸方式，給出12個月的下線緩衝期。原本由伺服器主動發起的sampling、roots、logging功能則被標示為已淘汰，替代方案是Multi Round-Trip Requests(MRTR)：伺服器回傳`resultType: "input_required"`，client端帶著答案重新呼叫原本的請求。

Harness與framework都是站在MCP之上的client。Claude Code與Claude Agent SDK會連接MCP伺服器，也能透過內建的in-process MCP伺服器自訂工具；Codex同樣連接MCP伺服器，OpenAI的Relay範例更把Codex與一個由應用程式自有MCP工具驅動的儀表板放在一起；Microsoft Agent Framework 1.0則同時支援MCP與A2A。採用數字也印證了MCP作為共通底層的地位：據MCP維護團隊表示，Tier 1 SDK每月下載量合計接近5億次，TypeScript與Python兩個SDK各自的總下載量都已經超過10億次。

🔐 權限：規格寫明「MCP自己無法在協定層強制執行」

MCP規格本身寫得很清楚：host必須在呼叫任何工具前取得使用者的明確同意，工具描述與標註除非伺服器可信，否則都應視為不可信。而關鍵的一句話是：「MCP itself cannot enforce these security principles at the protocol level」，也就是說權限歸屬於host這一層。

在Harness層面，Claude Code提供6種權限模式：default、acceptEdits、plan、auto、dontAsk、bypassPermissions，其中deny規則在除了bypassPermissions以外的所有模式下都會擋下動作(bypassPermissions會直接跳過整個權限層)；auto模式則會把每個工具呼叫送進一個背景分類器判斷。Hooks還能在`PreToolUse`與`PermissionRequest`兩個時間點加入自訂邏輯。Codex走的是類似路線，其app-server可以暫停一個turn，發出一個approval請求，client必須先回應才能繼續執行。

Framework這一層則只給掛鉤，不給政策：OpenAI Agents SDK提供input、output、tool三種guardrail，一旦觸發tripwire整個run就會中止；LangGraph用`interrupt()`在節點內暫停等待核準，再用`Command(resume=...)`繼續；Microsoft Agent Framework則加入`ToolApprovalAgent`中介層，支援「不用再問」規則。這些都需要開發者自己寫核准邏輯與UI。

MCP這一層現在能透過elicitation搭配MRTR把approval請求帶過協定本身，例如Supabase計畫用它讓工具在執行有成本或具破壞性的查詢前先確認。但伺服器只能「詢問」，真正「決定」的仍是host。

🔁 復原：Harness才是真正吃重的一層

在復原(recovery)這個面向，harness的角色最吃重。Claude Agent SDK能夠復原一個session，把檔案變更倒回到某個checkpoint，也會在context視窗填滿時自動壓縮；Claude Code的dynamic workflows即使終端機被關掉，也能接續之前的進度繼續跑。Anthropic在2026年3月的harness設計文章中特別把生成者(generator)與評估者(evaluator)拆成兩個agent，理由是讓agent自己批改自己的成果容易偏向過度樂觀。

OpenAI在2026年2月的harness文章中則報告了具體成果：Codex在5個月內產出約1,500個被合併的PR，程式碼庫規模來到約100萬行，團隊從3人成長到7人，平均每位工程師每天貢獻3.5個PR。OpenAI也提到harness對ARC-AGI-3成績的影響：靠保留推理內容與context壓縮，GPT-5.6 Sol的成績從13.3%提升到38.3%，輸出token數量卻減少到約六分之一，同一個模型，換了harness，成績完全不同。

Framework層面，LangGraph的durable execution機制明確指出復原能力依賴確定性(determinism)：把有副作用的操作包進task、保持節點冪等(idempotent)，這樣一個run才能在一週後被安全地接續執行。OpenAI Agents SDK則提供`error_handlers`，並在run失敗時保留已完成的guardrail結果，framework負責重播(replay)，但要讓重播安全，是開發者自己的責任。

MCP對長時間執行工作的答案，是由AWS貢獻的`io.modelcontextprotocol/tasks`擴充功能，透過輪詢式的`tasks/get`與`tasks/update`運作，但這只涵蓋單一個長時間執行的工具呼叫，並不涵蓋agent層級的復原機制。OpenAI對Relay的描述也呈現出幾乎一致的分工圖像：應用程式擁有產品情境、商業規則與工具，而Codex app-server提供的是agent迴圈與沙箱化的執行環境。

💡 A2A是唯一不重疊的一塊

文中特別點出一個不會與這三層重疊的名詞：A2A。Agent對agent的溝通是一個獨立的協定，目前也已併入Agentic AI Foundation。簡單區分：MCP負責把agent連接到工具，A2A負責把agent連接到其他agent。

🎯 實務啟示

在挑選或設計agent技術棧時，與其糾結「該用哪個框架」，不如先問清楚：這個迴圈由誰控制、狀態要不要跨session保存、權限決策要落在host端的哪一層、復原機制是要仰賴框架的確定性設計還是harness內建的checkpoint與context壓縮能力。把這五個問題想清楚，往往比比較各家框架的功能列表更快找到適合的架構分工。

🔗 來源
- 標題：Agent Harness vs Agent Framework vs MCP: Which Layer Owns the Loop, State, Tools, Permissions, and Recovery
- 作者／機構：Michal Sutter, MarkTechPost
- 連結：https://www.marktechpost.com/2026/09/14/agent-harness-vs-agent-framework-vs-mcp-which-layer-owns-the-loop-state-tools-permissions-and-recovery/

#AIAgents #MCP #AgentFramework #AgentHarness #LLMOps #AgentArchitecture #Codex #ClaudeAgentSDK #LangGraph #AIEngineering
