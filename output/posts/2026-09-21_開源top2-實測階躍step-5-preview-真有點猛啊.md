---
title: 開源Top2！實測階躍Step 5 Preview，真有點猛啊…
source: 量子位
url: https://www.qbitai.com/2026/09/493179.html
model: claude-code/sonnet
generated_at: '2026-09-21T21:19:53.746256'
score: 80
---

📌 600B 總參數、27B 啟用，階躍 Step 5 Preview 殺回開源 Top 2

TL;DR：階躍星辰新旗艦 Step 5 Preview 用「窄但深」架構壓低成本，實測 Agent 能自己搭建 3D 場景與網站。

一個模型自己操控 Blender 建模、渲染出帶著 VHS 錄影質感和腳步聲的後室影片，這聽起來不像是 27B 啟用參數模型該做到的事，但這正是階躍星辰最新旗艦模型 Step 5 Preview 交出的成績單之一。

🤔 **久違的第一梯隊：階躍在 Benchmark 上殺回來了**

階躍星辰近日發布最新一代旗艦基座模型 Step 5 Preview，採用 MoE 架構，總參數 600B、啟用參數僅 27B，支援 1M 上下文。在 Artificial Analysis 最新評測中，Step 5 Preview 取得 44 分，衝上全球開源模型 Top 2；報導指出，其他達到這個分數的大模型大多是萬億參數級別，相比之下 Step 5 Preview 的規模明顯更小。定價方面，百萬輸入 token 1 美元、百萬輸出 token 2.7 美元，單一任務成本僅為 Opus 5 的 12.5%。在 AA 榜單的 Intelligence Index 與單任務成本權衡圖上，Step 5 Preview 位於帕累托前緣（Pareto frontier）。文章也提到，階躍前兩代模型主要聚焦在 Flash 這個較輕量的檔位，這次重新站上旗艦位置算是相對突然的躍進。

🧪 **實測：讓它自己操作 Blender 建後室、搓一個樂高賽車遊戲**

作者實際串接 API，讓 Step 5 Preview 操作 Blender 自主建模。模型花了一個多小時自行折騰後，交出的渲染成品讓作者直呼意外：不只建模完成，還自己加上了 VHS 錄影質感、鏡頭噪點、昏黃燈光，甚至配上人物走路的腳步聲等後製效果。

第二個任務是仿照 1999 年遊戲《LEGO Racers》製作一個樂高賽車遊戲，成品包含賽道、賽車、AI 車手與即時排名系統，甚至配上了發動機音效，唯一的問題是賽道修得偏窄。作者接著測試了 2D 任務：一個霓虹跑酷小遊戲（作者特意套用與階躍上一代官網 Demo 類似的 Prompt，發現本代在道路兩側加了高樓、視覺層次更完整，Game Over 時邊框還會變紅，補上了不少 Prompt 未明確要求的細節），以及一個寫作網站（作者特別稱讚其視覺審美與完整度，形容「基本能直接拿來用」）。作者也坦言，第一輪產出偶爾仍有模組溢位等小 bug，需要人工 review 並經過兩三輪修正才能到可用狀態，距離「完全零介入」的體驗仍有差距。

🧩 **窄但深：把算力花在 Agent 真正需要的地方**

文章分析，Step 5 Preview 能在較小啟用參數下拿到高分，關鍵在於團隊採用「Narrow but Deep」（窄但深）的網路設計，用 92 層 Transformer，在控制啟用規模的同時讓資訊經過更多層連續變換，這對需要大量 multi-hop 依賴的複雜 Agent 任務特別有幫助，因為前面搜集到的資訊往往要經過很多步之後才會真正派上用場。

為了因應長上下文（幾十輪工具呼叫後上下文可能滾到上百萬 token）帶來的計算量爆炸，團隊在架構上做了稀疏化設計，包括 Sparse MoE、Hybrid Sparse、Sparse GQA，並在硬體層面透過底層運算元與資料訪問最佳化，讓理論上的稀疏化真正轉換成實際吞吐量的提升。在此基礎上，團隊圍繞 Agent 進行訓練，把模型的基本工作單位從「一次回答」轉變成「一個 Loop」：規劃、執行、呼叫工具、檢視結果、發現問題、修正，再進入下一輪 Loop。透過 Long-horizon RL 與 Context Compaction 等方法，讓模型在經過幾十輪工具呼叫後仍能記住任務目標。

📊 **前段模型的 Elo 差距正在收窄**

文章引用 Stanford 2026 AI Index 的資料指出，截至 2026 年 3 月，Anthropic、xAI、Google 與 OpenAI 各自最頂尖的模型在 Arena 上的差距已經壓縮到 25 個 Elo 以內，遠小於 GPT 剛發布時的差距。這也呼應了文章對整體格局的判斷：Frontier 門檻越來越高，內部競爭也越來越擁擠，單一 Benchmark 排名已經很難定義一家模型公司的長期位置，各家模型正轉而在不同面向（如前端開發、性價比、Computer use 等）尋找差異化定位。

⚠️ **仍需人工把關，體驗與頂尖水準有落差**

作者也直言，Step 5 Preview 的產出離「AI 做的完全看不出破綻」的癱軟級體驗還有差距，第一輪成品常有細節不到位或小 bug，通常需要指出兩三輪問題後模型自行修正，才能達到可用狀態。

🎯 **實務啟示**

對於評估開源模型做 Agent 應用的工程團隊而言，Step 5 Preview 的案例提供了一個訊號：與其一味堆參數規模，透過「窄但深」的架構設計搭配針對長程 Agent Loop 的強化學習訓練，也能在成本大幅壓低的情況下逼近甚至超越更大規模模型的 Agent 表現。實際導入前，仍建議針對自身任務場景做多輪迭代測試，評估模型自我修正所需的輪數與人工 review 成本，而不只是看單一 Benchmark 分數。

🔗 **來源**
- 標題：開源Top2！實測階躍Step 5 Preview，真有點猛啊…
- 作者／機構：Jay，量子位
- 連結：https://www.qbitai.com/2026/09/493179.html

#StepFun #Step5Preview #MoE #OpenSourceLLM #AgenticAI #LLMBenchmark #ArtificialAnalysis #AIAgents #ChinaAI #LLM
