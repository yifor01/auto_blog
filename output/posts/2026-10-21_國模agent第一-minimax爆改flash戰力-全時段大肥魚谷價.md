---
title: 國模Agent第一！MiniMax爆改Flash戰力，全時段大肥魚谷價
source: 量子位
url: https://www.qbitai.com/2026/10/504517.html
model: claude-code/sonnet
generated_at: '2026-10-21T20:56:51.986869'
score: 96
---

📌 MiniMax M3.1 Flash：國產 Flash 模型打出 Agent 第一戰績

TL;DR：MiniMax 新模型 M3.1 Flash 在多項 Agent 基準拿下國產第一，價格壓到上一代三成，推理速度提升近 3 倍。

國慶期間在 OpenRouter 上匿名屠榜、代號「Space Bunny」的神秘模型，謎底終於揭曉：它正是 MiniMax 即將正式發布的 M3.1 Flash。比起匿名測試期的版本，正式版跑分不降反升，尤其是在 Agent 相關能力上，交出了一份國產模型中相當亮眼的成績單。

🤔 **MiniMax 的純文本模型，沉寂了一段時間**

在這次 M3.1 Flash 亮相之前，MiniMax 在多模態與影片生成上表現突出，但純文本大模型這條線一度缺乏動靜。M3.1 Flash 的發布，被視為其文本模型陣營的一次反彈。

📊 **從程式碼到金融工具鏈，全線進入全球第一梯隊**

MiniMax 公布的多項基準數據顯示，M3.1 Flash 在不同任務類型上都具競爭力：

| 基準測試 | 分數 | 對比 |
|---|---|---|
| Agents' Last Exam (ALE) | 29.6% | 國產模型第一 |
| Artificial Analysis 綜合榜單 | 43 分 | —— |
| DeepSWE v1.1（程式碼修 bug） | 73.7% | 超越 GPT-6.1 Sol、Claude Opus 5、Claude Fable 5；僅次於 DeepSeek V4.1 Flash 1017（77 分） |
| CyberGym（UC Berkeley 網路安全基準） | 82.2 分 | 與 GLM-5.3（84.5）、GPT-5.6 Sol（83.6）同列全球第一梯隊 |
| BankerToolBench（金融工具呼叫） | 76.2 分 | 與 Claude Opus 5 並列全球第一 |
| OSWorld V2（Computer Use 真實桌面操作） | 61.7 分 | 國產模型第一 |

在 Zapier 開源的 AutomationBench-AA 評測中，M3.1 Flash 位居前列，單任務成本可壓在 0.05 美元以下，就能串接橫跨銷售、營銷、客服、財務與 HR 的複雜跨 SaaS 工作流；社群在匿名測試期間的回饋也提到，它在 Three.js 等 3D 渲染與複雜前端任務上對細節的掌控相當細緻。

🧩 **稀疏注意力架構換來近 3 倍推理速度**

MiniMax 表示 M3.1 Flash 底層採用了較為激進的稀疏注意力（sparse attention）架構，使線上推理速度提升近 3 倍：輸出速度最快可達每秒 200+ token，中位數（P50）穩定維持在每秒 170+ token 的水準。對於需要在多個子 agent 之間反覆傳話、一次任務背後要呼叫數十次工具的企業級 agent 應用而言，輸出速度直接影響使用者是否會在等待中關閉頁面。

💡 **價格打到上一代的三成**

伴隨速度提升，M3.1 Flash 的計費也大幅下調：輸入每百萬 token 1 元，輸出每百萬 token 4 元，快取讀取每百萬 token 僅 0.1 元。輸入與輸出價格相較前代腰斬，快取讀取費用更下降 75%，綜合使用成本相比上一代 M3 下降約 70%，整體價位與 DeepSeek V4.1 Flash 相近。文中將這一波現象形容為「國產雙子星」：DeepSeek V4.1 Flash 先在純 coding 的價效比上立下標竿，MiniMax M3.1 Flash 隨後在跨 SaaS 企業工作流與金融工具鏈呼叫等綜合 Agent 維度上補位，兩者走出互補路線。

⚠️ **仍是 Flash 級模型，非旗艦替代**

儘管多項基準表現亮眼，M3.1 Flash 終究是定位為輕量、低成本的 Flash 級模型，文中呈現的對比對象多為各家旗艦模型中的特定基準分數，而非全面能力的對等比較，實際選型仍需依照具體任務場景驗證。

🎯 **對工程師的啟示**

如果你的 agent 系統正受限於呼叫延遲與 API 帳單，M3.1 Flash 這類低價高速的 Flash 模型值得納入路由策略：將高頻、對延遲敏感的任務導向這類模型，複雜或邊緣案例再升級到旗艦模型，是目前控制多 agent 系統成本的一種可行方向。

🔗 **來源**
- 標題：國模Agent第一！MiniMax爆改Flash戰力，全時段大肥魚谷價
- 作者／機構：Jay，量子位
- 連結：https://www.qbitai.com/2026/10/504517.html

#MiniMax #Flash #LLM #AIAgents #OpenRouter #CostEfficiency #SparseAttention #ComputerUse #CodeGeneration #ChineseAI
