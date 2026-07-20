---
title: 'Perplexity AI Releases WANDR: An Open Benchmark Evaluating Research Agents
  That Must Search Wide And Deep'
source: MarkTechPost
url: https://www.marktechpost.com/2026/07/19/perplexity-ai-releases-wandr-an-open-benchmark-evaluating-research-agents-that-must-search-wide-and-deep/
score: 96
model: tencent/hy3:free
generated_at: '2026-07-20T08:51:33.837004'
---

📌 【Perplexity AI 發布】WANDR：評測研究代理「廣而深」搜尋能力的開放基準

TL;DR：Perplexity 推出 WANDR 開放基準，用 500 項任務考驗代理廣搜與深證據能力。

多數研究代理基準只要求產出「單一答案」，但真實知識工作往往要蒐集一大堆有證據支撐的專案。當團隊已經把競品盤點、盡職調查、文獻回顧交給 agent 處理，我們卻還在用錯誤的尺來量它們。

🤔 **現有基準只測單點，漏掉知識工作的本質**

研究代理（research agents）現在已實際承擔真實知識工作，例如競品對映、盡職調查（due diligence）、文獻回顧等。但多數基準測的是「一題一答」，而非大規模、需證據背書的資料集合。Perplexity 針對這個缺口，釋出了一個開放基準與評測框架（evaluation harness）。

🧩 **WANDR 與 DRACO 的互補定位**

WANDR 全名為 Wide ANd Deep Research，是 Perplexity 先前 DRACO 基準的「廣度版」兄弟專案。
- DRACO：測 agent 能否產出準確、完整、客觀的長篇報告（deep research）。
- WANDR：測 agent 能否建構出一個大規模、附證據的資料集合。

WANDR 核心同時考驗兩個需求：
- Wide（廣）：發現大量、常是開放式的一組合格實體。
- Deep（深）：對每個實體進行足夠調查，讓每項宣告都有證據支援。

只給幾個亮眼範例不夠，靠不完整研究堆出的精美敘事也達不到要求。

🧩 **可組合的資格鍵階層設計**

為捕捉上述特性，WANDR 使用可組合的資格鍵階層（composable qualification key hierarchy）。例如一個任務可表示為：
company(n) → employee(m) → url(k)
代表要找出 n 家合格公司、每家 m 名員工、每人 k 個支援頁面。樹狀結構中每一條完整路徑都會獨立驗證；同一結構可表達扁平清單、巢狀搜尋或矩陣。

📊 **實際任務範例：ceo_cfo_appointments**

釋出的 ceo_cfo_appointments 任務要求：
- 至少 70 家美國公司。
- 每家需在 2026 年 3 月 1 日至 4 月 30 日間首次公佈 CEO 或 CFO 任命。
- 每家公司由 agent 提供一則權威任命頁面。
- 子任務另要求每家公司附一則 listing-authority 頁面。
合計需提交 140 筆有來源背書的紀錄。

🎯 **對工程師的實務意義**

若你在評估或開發研究代理，WANDR 提供了一個不同於「單回答正確率」的視角：代理能否同時「搜得廣」又「查得深」。在匯入 agent 做競品盤點或盡職調查前，可先用此類開放基準檢視其證據蒐集完整性，而非只看產出報告流不流暢。

🔗 **來源**
- 標題：Perplexity AI Releases WANDR: An Open Benchmark Evaluating Research Agents That Must Search Wide And Deep
- 作者／機構：Asif Razzaq @ MarkTechPost
- 連結：https://www.marktechpost.com/2026/07/19/perplexity-ai-releases-wandr-an-open-benchmark-evaluating-research-agents-that-must-search-wide-and-deep/

#ResearchAgents #Benchmark #WANDR #PerplexityAI #DRACO #KnowledgeWork #Evaluation #OpenBenchmark #AgentEval #DeepResearch
