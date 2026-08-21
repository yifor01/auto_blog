---
title: Binance now lets AI agents trade, but keeping them in check is largely up to
  users
source: TechCrunch AI
url: https://techcrunch.com/2026/08/20/binance-now-lets-ai-agents-trade-but-keeping-them-in-check-is-largely-up-to-users/
model: claude-code/sonnet
generated_at: '2026-08-21T06:37:04.472346'
score: 85
---

📌 幣安讓AI代理自主下單,風控主動權卻留給使用者

TL;DR：幣安推出Agent OS讓AI agent連上交易帳戶自主交易,但資產安全的把關主要仍要靠使用者自行設定權限。

當AI從「回答問題」走向「動手做事」,交易所的角色也悄悄改變。擁有超過3億註冊用戶的全球最大加密貨幣交易所幣安,這次選擇把AI agent直接接上使用者的真實資金,讓機器替人下單。

🤔 從聊天機器人到能執行交易的agent

幣安週四推出的Agent OS,讓開發者把AI應用與agent連接到幣安的金融基礎設施,涵蓋分析市場、查看帳戶資訊、執行交易等操作。

🧩 靠子帳戶(subaccount)把agent關進沙盒

Agent OS整合了既有的Binance APIs、Binance Wallet Agentic Hub、x402交易驗證與支付facilitator API,以及Binance Skill Hub,並新增對Model Context Protocol(MCP)的支援,可與OpenAI的ChatGPT和Codex、Anthropic的Claude Code,以及Cursor等工具相容。核心風控機制是「子帳戶」:使用者可將agent指定給特定子帳戶,並設定其能做現貨或期貨交易等特定活動,子帳戶預設封鎖提領功能。使用者可自行選擇agent每筆下單都要人工核准,還是設定好權限後就能自主執行交易。

📊 沒有交易上限,但代幣錢包操作每日有硬性額度

幣安對子帳戶的交易或虧損金額沒有另外設定上限,使用者轉入子帳戶的資金量,實質上就是風險上限。但透過Binance x402整合與Agentic Wallet,agent可以發送、結算支付並操作代幣與DeFi協議,這部分幣安設有每日額度:一般swap上限為5萬美元/日,DeFi交易預設上限為10萬美元/日,x402支付則僅限20美元/日。

💡 幣安看不到agent「為什麼」這樣決策

被問到幣安能否看見agent做出某筆交易背後的推理過程時,幣安產品副總裁Jeff Li表示推理是在幣安系統之外發生的,可能在使用者自己的電腦或所選的AI應用裡進行,「我們真的無法看到使用者行動背後的推理」。這意味著幣安能監控agent最終的交易結果,但對決策是否受到錯誤資訊或操縱影響的可見度有限。面對prompt injection攻擊或agent被入侵的情境,Li同樣把子帳戶隔離視為主要防線。幣安並非唯一走這條路的交易所:Kraken今年3月推出內建MCP server的開源命令列工具,Coinbase 6月推出Coinbase for Agents,OKX也已開放基於開源MCP工具包的agentic交易。

⚠️ 責任邊界清楚,但也代表風險轉嫁

由於幣安無法審視agent的推理過程,一旦agent因錯誤資訊或操縱做出異常決策,平臺能提供的保護主要就是子帳戶的資金隔離與每日額度上限,其餘的授權範圍與風險控管,實際上落在使用者自己身上。

🎯 把agent接進真金白銀系統前,先設計好隔離與稽核

對於正在把agent接入具金錢或高風險操作系統的工程團隊,幣安這套「子帳戶隔離+固定資金上限+可選人工核准」的模式,是值得參考的最小可行風控框架。但由於平臺端看不到agent的推理過程,建議在agent自身或應用層自行建立完整的決策日誌與稽核軌跡,不能假設平臺會替你做這件事。

🔗 來源
- 標題：Binance now lets AI agents trade, but keeping them in check is largely up to users
- 作者／機構：Jagmeet Singh, TechCrunch AI
- 連結：https://techcrunch.com/2026/08/20/binance-now-lets-ai-agents-trade-but-keeping-them-in-check-is-largely-up-to-users/

#Binance #AIAgents #AgenticAI #Crypto #MCP #FinTech #TradingBots #RiskManagement #AgentOS #Blockchain
