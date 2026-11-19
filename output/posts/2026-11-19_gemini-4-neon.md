---
title: Gemini 4 Neon
source: Hacker News
url: https://blog.google/innovation-and-ai/models-and-research/gemini-models/introducing-gemini-4-neon/
model: claude-code/sonnet
generated_at: '2026-11-19T23:44:51.203993'
score: 103
---

📌 Google 親自揭底 Gemini 4 Neon:用 /swarm 重建圖靈書房的那個模型

TL;DR：Google 官方公布 Neon 在企業、科學與資安場景的完整戰績,外加一批互動式 demo。

與其只丟一張 benchmark 表,Google 這次選擇用一系列具體場景來說明 Neon 到底能做什麼——從重建艾倫·圖靈 1936 年的書房,到用五十萬條試算表公式做影像處理。這種展示方式,比單純的分數更能說明「frontier-level 智能」具體落地的樣子。

🤔 **官方給自己的定位:第三,但勝在好用**

Google DeepMind 的 SVP Koray Kavukcuoglu 將 Neon 定位為「帶來前沿級智能,並在複雜軟體工程、知識工作與科學工作流中快速完成端到端任務」。在 xhigh thinking 層級下,Neon 於 Artificial Analysis Intelligence Index 排名第三,得分 61,官方坦承是落後在更大、更慢的模型之後。但在 Vals Index 上排名第二,並落在 Pareto frontier 上;在新的 Agent Arena Index 的 steerability(中途修正任務的適應能力)項目也排名第二。官方還特別提到,Neon 在 Google Antigravity 的內部測試中,記錄到目前為止最低的虛構(fabrication)率。

🧩 **1M context 把試算表、PDF、圖表都收進同一個視窗**

企業工作散落在試算表、PDF、圖表、音訊與影片之間,Neon 可以在單一 100 萬 token 的 context window 中整合這些輸入,並輸出結構化的成果。在 Antigravity 中,Neon 也能作為 orchestrator,指揮多個並行的 Hydrogen 子代理,同時減少重複讀檔、即時分享進度,並在長時間 session 中可靠處理 context compaction。

📊 **逐類別的榜單戰績**

企業與分析類:Vals Index 排名 #2(70.9%),在 Legal Research Bench 與 Tax Agent Bench 上都拿下 #1;在 Surge AI 的財務、會計、試算表建模與複雜約束遵循等多項基準上排名第一;Chartography(密集專業圖表閱讀)得分 73.5%;Agents' Last Exam v1.1 得分 75.8%,與領先模型相當;Zapier 的 AutomationBench 拿下 #1(56.3%);Andon Labs 的 Vending-Bench 2(模擬長期經營一家企業)拿下 #1,成績 16,843 美元;在 Arena 的 Agent Arena Index(超過 4,200 個真實 agent session)中排名 #2,得分 1336。

科學與數學類:Terminal-Bench Science(70.5%)、RiemannBench(84.0%)、HLE-Diamond(71.3%)三項皆為同類最佳。

程式碼類:AA Coding Agent Index 排名 #1(58.6);Terminal-Bench 4.1 得分 65.2%;FrontierCode 2.0 在預設 high 設定下得分 46.2%;SWE-sweep 在 mini-SWE harness 上已經領先(12.8%),而在 Google Antigravity 的 harness 下更躥升到 39.0%,官方以此說明 Antigravity 環境能進一步釋放模型能力。

資安類:AutoBaxBench 的 hard 難度拿下 76% 的業界最佳成績;WebExploitBench v1.2 達到 51.26%,同時成本只有競爭大模型的一半;SEC-bench Pro(找漏洞)達 90.5%;ExploitGym(驗證漏洞可利用性)用 Carbon 一半的 token 就達到前沿水準;CWE-bench v2(修補漏洞)達到 70.7%,比 Carbon 提升 3.4%。Gemini 4 Neon for cyber 將透過 Fairwind Program 陸續開放給受信任的防禦方使用。

💡 **官方選擇用 demo 說故事**

幾個被官方特別點名的案例很有意思:在 Antigravity 中用 /swarm 指令驅動 Blender MCP,打造出一張還原元素特性的 3D 實驗桌;從零寫出一個第一人稱 WebGL2 滑雪模擬器,用真實的 Mont Blanc 與 Chamonix 地形資料,包含 10,200 行自訂 shader、120Hz 滑雪物理、六條高山雪道與動態空間音效;用 /swarm 重建艾倫·圖靈 1936 年在劍橋國王學院的書房,外部還原到國王學院禮拜堂,內部重現一臺運作中的通用圖靈機;以及把一張圖片轉換成十萬格的 Google Sheet,用超過 50 萬條即時公式(不靠圖片嵌入或 Apps Script)做邊緣偵測與 3D 深度映射。

定價上,Neon 在 high thinking(預設)下,每次任務成本比 Carbon 低 32%,在 Vals Index 與 Agent Arena 上都落在 Pareto frontier,比對手低約 50% 至 80%;xhigh thinking 則專供最難的工程、分析與科學任務,即使在此層級,成本仍比對手在最高設定下低 36% 以上。

⚠️ **這是一份官方自我展示的成績單**

必須提醒的是,上述所有分數與 demo 皆出自 Google 官方發布內容,未經第三方獨立驗證。Neon 在 AA Intelligence Index 上排名第三,官方也坦言落後於更大、更慢的模型,這點值得在評估時留意。

🎯 **實務啟示**

如果你的團隊工作集中在資安、企業知識工作或科學計算這幾類場景,上述逐項榜單可以作為挑選模型層級的參考依據;若要處理長 horizon 的 agentic 任務,Antigravity 的 orchestrator 模式與 /swarm 式多代理協作值得實際試跑看看落地效果。

🔗 **來源**
- 標題：Gemini 4 Neon(Introducing Gemini 4 Neon)
- 作者／機構：Koray Kavukcuoglu, Google DeepMind(經 Hacker News 使用者 yigitdemirag 提交)
- 連結：https://blog.google/innovation-and-ai/models-and-research/gemini-models/introducing-gemini-4-neon/

#GeminiNeon #GoogleDeepMind #GoogleAntigravity #AIAgents #Cybersecurity #LLMBenchmark #AgentArena #EnterpriseAI #AIForScience #MultimodalAI
