---
title: 'Show HN: Mastra Factory, the open-source software factory we use to build
  Mastra'
source: Hacker News
url: https://news.ycombinator.com/item?id=50548660
model: claude-code/sonnet
generated_at: '2026-11-19T23:55:34.680160'
score: 79
---

📌 Mastra Factory:自家代理框架養出的軟體工廠,一週自動合併238個PR

TL;DR:Mastra 團隊開源了用來維護自己專案的 agentic kanban 系統 Factory,可直接在 Slack 用 @ 標註呼叫。

一個每週下載量逼近400萬次的開源專案,要怎麼跟上社群湧入的 PR 數量?Mastra 團隊給出的答案不是招募更多維護者,而是讓代理自己去 triage、去審、去合併。

🤔 **為什麼要自己造一座「軟體工廠」**

兩年前,Mastra 團隊在 Hacker News 上發布了他們開源的 TypeScript 代理框架 Mastra,如今每週下載量已接近400萬次。隨著專案規模擴大,團隊建了 Factory 來維護 Mastra 本身。上週,Factory 自動開啟並合併了238個 PR,同時人類貢獻者也合併了630個 PR。團隊坦言「軟體工廠」這個詞本身有很多爭論,對他們來說,Factory 就是一個「可在 Slack 中用 @ 標註呼叫的可配置 agentic 看板(kanban board)」。

🧩 **底層堆疊:durable agent、對話記憶、PR留言訂閱**

Factory 在底層組合了幾個 Mastra 自家的能力:
- Mastra 的 durable agents,支援長時間執行的 session
- 對話記憶系統(conversational memory)
- 基於 markdown 的 wiki,附帶來源引用,用來把公司知識餵進代理
- 訂閱 PR 留言的 signals 機制,串接進既有 session
- 可客製化的雲端 sandbox,搭配自家 coding harness(團隊表示正在擴充支援 Claude Code、Codex 等)

團隊一開始依照既有工作流程(triage、plan、build、review、shipped)去設計 Factory,但三個月後發現團隊主要透過 Slack 驅動它,而不是網頁 UI。更資深的工程師會平行開啟多個 session,例如直接丟一句「把最舊的20個 issue 都分級,我們來評估」。團隊也開始引入 bug 與漏洞掃描工具,並把 repo 關閉給外部貢獻者,改為要求提交詳細的 issue 重現步驟。

💡 **自動化規模化後的治理取捨**

這個案例有意思的地方在於,agentic 工具的實際使用方式,最後收斂到團隊原本就在用的溝通介面(Slack),而不是為它另外設計一套網頁工作流程。另一方面,把 PR 合併的決策權更多交給代理之後,團隊選擇收緊外部貢獻門檻,用詳細 issue 重現步驟取代直接提交程式碼,這是規模化自動化之後必然要面對的治理取捨。

🎯 **怎麼開始用**

執行 `npm create factory` 即可建立專案,完全開源,可以完整架設在自己的基礎設施上,官方也提供託管版本。素材沒有提供 Factory 與其他 agentic PR 自動化工具的直接對比,也沒有說明定價細節,這部分無法評論。

⚠️ **限制**

素材未提及 Factory 對模型供應商的具體支援清單(僅提到正在擴充 coding harness),也沒有說明託管版本的費用結構或安全性保證細節。

🔗 **來源**
- 標題:Show HN: Mastra Factory, the open-source software factory we use to build Mastra
- 作者/機構:codekarate(Shane、Sam、Abhi @ Mastra)
- 連結:https://news.ycombinator.com/item?id=50548660

#Mastra #OpenSource #AIAgent #SoftwareFactory #TypeScript #DeveloperTools #AgenticWorkflow #CodingAgent #PullRequest #AgentFramework
