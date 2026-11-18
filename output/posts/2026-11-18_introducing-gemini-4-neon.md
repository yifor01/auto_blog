---
title: Introducing Gemini 4 Neon
source: Google DeepMind
url: https://deepmind.google/blog/introducing-gemini-4-neon/
model: claude-code/sonnet
generated_at: '2026-11-18T23:30:29.004969'
pinned: true
---

📌 Gemini 4 Neon 登場：agent 推理排名第 2，成本大砍 50% 起

TL;DR：Google DeepMind 推出 Gemini 4 Neon，主打長時程 agent 工作流與高性價比，多項第三方 benchmark 奪冠。

當各家模型榜單愈來愈拼智慧分數時，Neon 打出的是另一張牌：接近頂尖的智慧表現，但單位任務成本只要競品的一半甚至更低。

🤔 **定位：軟體工程、知識工作與科學運算的全能 agent**

Google DeepMind 表示 Neon 在 Artificial Analysis Intelligence Index 以 xhigh thinking 等級拿下 61 分，排名第 3，僅落後更大、更慢的模型；在 Vals Index 排名第 2，並落在 Pareto frontier 上。在新推出的 Agent Arena Index 中，Neon 的 steerability（任務中途接受使用者修正的能力）排名第 2，且在內部 Google Antigravity 測試中創下目前最低的「幻覺」（fabrication）比率。

🧩 **為長時程 agent 工作流而設計**

Neon 被設計用來在複雜、工具密集的任務中維持端到端表現，無論是獨立運作，或作為高判斷力的 Orchestrator 去指揮 Google Antigravity 中並行的 Hydrogen subagent。它能減少重複讀取檔案、邊執行邊回報進度，並在長對話中穩定處理 context compaction（上下文壓縮）。

📊 **跨領域 benchmark 成績**

| 領域 | Benchmark | Neon 成績 | 排名／備註 |
|---|---|---|---|
| 綜合智慧 | Artificial Analysis Intelligence Index | 61 | #3（xhigh） |
| 綜合智慧 | Vals Index | 70.9% | #2 |
| Agent | Agent Arena Index | 1336 分 | #2（4,200+ 真實 agent session） |
| 企業知識工作 | Legal Research Bench / Tax Agent Bench | — | 皆 #1 |
| 企業知識工作 | Chartography（讀圖表） | 73.5% | — |
| 企業知識工作 | Agents' Last Exam v1.1 | 75.8% | 與頂尖模型相當 |
| 自動化 | Zapier AutomationBench | 56.3% | #1 全球 |
| 自動化 | Vending-Bench 2（長時程模擬經營） | $16,843 | #1 全球 |
| 科學／數學 | Terminal-Bench Science | 70.5% | 同級最佳 |
| 科學／數學 | RiemannBench | 84.0% | 同級最佳 |
| 科學／數學 | HLE-Diamond | 71.3% | 同級最佳 |
| 程式碼 | Artificial Analysis Coding Agent Index | 58.6 | #1 |
| 程式碼 | Terminal-Bench 4.1 | 65.2% | — |
| 程式碼 | FrontierCode 2.0（高設定） | 46.2% | — |
| 程式碼 | SWE-sweep（mini-SWE harness → Antigravity harness） | 12.8% → 39.0% | Antigravity harness 下三倍提升 |

網路安全方面，Neon for cyber 在 AutoBaxBench 困難題達到 76%（同級最佳），WebExploitBench v1.2 達 51.26%（同級最佳，成本為競品一半），SEC-bench Pro 達 90.5%（成本約減半），CWE-bench v2 達 70.7%（比前代 Carbon 提升 3.4%）。

💡 **定價與效率設計**

Neon 定價為每百萬輸入 token 3 美元（快取輸入每百萬 0.15 美元，折扣 95%）、每百萬輸出 token 15 美元，具備 1 百萬 token 的上下文窗口。官方指出，預設 high thinking 等級下，Neon 的單位任務成本比前代 Carbon 低 32%；在 Vals Index 與 Agent Arena 的 high 等級上，成本比頂尖競品低約 50% 至 80%；而在 xhigh thinking 等級衝最高智慧分數時，成本仍比競品在各自最高設定下低 36% 以上。官方也展示了多個能力演示，包括用 Blender MCP 搭配 /swarm 建立 3D 元素實驗桌、從零寫出一套含 10,200 行自訂 shader 的 WebGL2 滑雪模擬器，以及用超過 50 萬條 Google Sheet 公式重現影像邊緣偵測與光照效果。

⚠️ **限制**

Neon 在整體智慧指標上仍排名第 3，落後於更大、更慢的模型；Neon for cyber 目前僅透過 Fairwind Program 逐步開放給受信任的防禦團隊使用，尚未全面公開。

🎯 **實務啟示**

對需要長時程、工具密集 agent 工作流（多檔案除錯、跨庫重構、企業文件彙整）的團隊，Neon 的四個 thinking 等級提供了明確的「智慧／成本」旋鈕，可依任務難度調整花費；而其在 cyber 防禦相關 benchmark 的表現，也值得安全團隊關注其作為程式碼安全強化與弱點掃描輔助工具的潛力。

🔗 **來源**
- 標題：Introducing Gemini 4 Neon
- 作者／機構：Google DeepMind
- 連結：https://deepmind.google/blog/introducing-gemini-4-neon/

#Gemini4Neon #GoogleDeepMind #AgenticAI #LLM #CodingAgent #AIBenchmark #CyberSecurity #GoogleAntigravity #AIAgents #FrontierModel
