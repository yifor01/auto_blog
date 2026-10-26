---
title: 'Nace AI Releases Drex for Search for AI Agents: 92.05% on BrowseComp-Plus
  With 12.6 Search Calls'
source: MarkTechPost
url: https://www.marktechpost.com/2026/10/26/nace-ai-releases-drex-for-search-for-ai-agents/
model: claude-code/sonnet
generated_at: '2026-10-26T21:48:01.280121'
score: 104
---

📌 Nace AI 發布 Drex for Search：把檢索變成逐步決策而非一次性排序

TL;DR：Drex for Search 用校準過的決策模型取代傳統 chunk-embed-top-k 流程，在 BrowseComp-Plus 上以 GPT-5 達 92.05% 準確率。

傳統 RAG 的套路大家都熟：切 chunk、embed、取 top-k、祈禱答案就在裡面。Nace AI 認為這條路線的根本問題在於「深度是固定的」—— 一百萬個檔案和一千個檔案要走的步數一樣多，這在文件量大、需要多跳推理的場景裡很容易失準。他們的解法是把 Drex for Search 的決策模型接到搜尋流程上，讓檢索本身變成一連串可以逐步決策的動作。

🧩 **把搜尋拆成決策，而不是一次性排序**

Drex for Search 延續 Nace 的 Drex 決策模型，核心做法是針對給定的選項，用一次前向傳播（forward pass）就輸出每個選項校準過的機率，使得在 agent 每一步都能便宜地呼叫。這套檢索層可以被人類或 agent 使用，Claude Code、Codex、Cursor、OpenCode 等 coding agent 可以透過 CLI、SDK、MCP 或 REST 呼叫它。

📊 **多個 benchmark 的表現**

Nace AI 公布了幾組評測結果（皆為 Nace AI 自行發布，讀取時間為 2026 年 10 月 20 日）：

| Benchmark | 任務場景 | 關鍵數字 |
|---|---|---|
| BrowseComp-Plus | 830 個多跳問題，約 10 萬份固定網頁文件 | GPT-5 搭配下達 92.05% 準確率，平均 12.6 次搜尋呼叫 |
| VisDocAgentBench | 在 2,375 頁 arXiv 論文中找出 1 個目標頁面 | 開源 Qwen 27B planner 搭配下 R@1 達 77.5%，優於目前公開最佳的 Claude Opus 5（67.5%） |
| MADQA | 針對 800+ 份 PDF 回答並標註引用頁面 | Gemini 3.5 Flash 搭配下準確率 94.7%，頁面歸因 F1 為 88.2，排名第一；換用開源 Qwen 27B 仍有 93.4% |
| EnterpriseRAG-Bench | 50 萬份以上的企業內部文件 | 總分 88.22，排名第三，比 OpenAI File Search（61.03）高 27.2 分 |

在 VisDocAgentBench 上，R@1 隨跳數拉遠而遞減：直接問題 97.5%、經過一次橋接推理 77.5%、兩次橋接 57.5%，顯示多跳檢索的難度仍會隨跳數增加而上升。

另外在 OfficeQA Pro（133 題，涵蓋美國財政部公告的基準測試）上，Nace AI 對 9 組 agent／模型組合測試後報告：答對率提升 6%、步數減少 62%、token 用量減少 56%、速度快 2.3 倍。

⚠️ **這是贊助內容，數字為廠商自行公布**

這篇原文由 Nace AI 贊助，所有排名與分數皆是 Nace AI 自行發布於其 leaderboard 的結果，並非第三方獨立驗證，讀者在評估時應留意這一點。

🎯 **實務啟示**

如果你的 agent 需要在大量文件（尤其是跨檔案多跳推理）中找證據，Drex for Search 提供了一個不同於「embedding + top-k」的切入點：用校準機率的決策模型逐步縮小搜尋範圍。對於已經在用 Claude Code、Cursor 等 coding agent 的團隊，透過 MCP 或 REST 接入的門檻也不高，值得在自己的資料集上實測評估。

🔗 **來源**
- 標題：Nace AI Releases Drex for Search for AI Agents: 92.05% on BrowseComp-Plus With 12.6 Search Calls
- 作者／機構：Asif Razzaq, MarkTechPost（贊助內容：Nace AI）
- 連結：https://www.marktechpost.com/2026/10/26/nace-ai-releases-drex-for-search-for-ai-agents/

#AIAgents #RAG #InformationRetrieval #LLM #SearchEngine #NaceAI #BrowseComp #AgenticSearch #MachineLearning #AIInfrastructure
