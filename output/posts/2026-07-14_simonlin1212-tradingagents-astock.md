---
title: simonlin1212/TradingAgents-astock
source: GitHub Trending
url: https://github.com/simonlin1212/TradingAgents-astock
score: 89
model: tencent/hy3:free
generated_at: '2026-07-14T08:04:36.575817'
---

根據您提供的資訊，這是一個開源專案（GitHub Project），我將依照開源專案的架構進行轉寫。

---

📌 【開源專案】TradingAgents-astock：專為 A 股設計的多 Agent 投研框架

TL;DR：基於 TradingAgents 進行 A 股特化，整合 7 種分析師角色與 A 股交易規則的開源工具。

🎣 雖然多 Agent 投研框架已非新鮮事，但大多數開源專案仍是針對美股市場設計，面對 A 股獨有的交易制度與資料源，往往難以直接落地。

🧩 **從美股框架到 A 股深度特化**

本專案是基於知名開源框架 `TauricResearch/TradingAgents` 的深度特化 fork 版本。作者並非進行簡單的語言翻譯，而是從資料層、Agent 角色、以及交易規則三個維度進行了重構，以解決原版框架無法處理 A 股特有制度的問題。

核心改造對照如下：

| 維度 | 原版 TradingAgents | TradingAgents-astock |
| :--- | :--- | :--- |
| **資料來源** | Yahoo Finance / Alpha Vantage | mootdx + 東財 + 新浪 + 同花順 |
| **Analyst 角色** | 4 個（市場/情緒/新聞/基本面） | 7 個（新增政策/遊資/解禁） |
| **交易規則** | 美股（T+0、無漲跌停） | A 股（T+1、漲跌停、最小手數、交易時段） |
| **輸出語言** | 英文 | 中文報告（內部辯論保持英文以保證推理質量） |
| **Alpha 基準** | SPY | 滬深 300 (CSI 300) |

📊 **七大分析師角色驅動的辯論架構**

專案採用多 Agent 協作機制，透過不同專業背景的角色進行資訊蒐集與辯論：

1.  **分析師層級**：包含市場 (Market)、社群情緒 (Social)、新聞 (News)、基本面 (Fundamentals) 分析師，並特別新增了 **政策分析師 (Policy)**、**遊資追蹤 (Hot Money)** 與 **解禁監控 (Lockup)** 三個針對 A 股設計的深度角色。
2.  **辯論機制**：由 Bull Researcher（看多研究員）與 Bear Researcher（看空研究員）進行最多 N 輪的投研辯論。
3.  **決策層級**：最終由 Research Manager 進行綜合研判並生成研報。

🛠️ **快速上手與開發細節**

- **部署方式**：支援 `pip install` 即可快速執行。
- **資料整合**：透過 HTTP 直連 mootdx、東財、新浪與同花順，實現 A 股資料的全免費直連。
- **授權協議**：採用 Apache 2.0 許可證。

⚠️ **免責宣告**
本專案僅供學習研究與技術演示，不構成任何投資建議。投資決策請諮詢持牌專業機構。

🎯 **實務啟示**
對於研究多 Agent 協作（Multi-Agent Collaboration）的工程師來說，此專案展示瞭如何透過「領域知識（Domain Knowledge）」將通用型 AI 框架轉化為具備特定市場邏輯的專業工具。

🔗 **來源**
- 標題：simonlin1212/TradingAgents-astock
- 連結：https://github.com/simonlin1212/TradingAgents-astock

#AI #MultiAgent #TradingAgents #AStock #OpenSource #MachineLearning #QuantitativeTrading #Python #LLM #FinancialAI
