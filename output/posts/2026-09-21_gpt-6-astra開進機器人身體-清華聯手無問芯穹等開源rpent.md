---
title: GPT-6 Astra開進機器人身體！清華聯手無問芯穹等開源RPent
source: 量子位
url: https://www.qbitai.com/2026/09/493218.html
model: claude-code/sonnet
generated_at: '2026-09-21T21:17:58.372936'
score: 95
---

📌 清華聯手無問芯穹開源RPent：讓GPT-6 Astra指揮機器人身體幹活

TL;DR：具身智慧體基礎設施RPent開源，LIBERO-PRO成功率92.6%，Flash Mode加速7倍以上。

Codex、Claude Code這類數字世界的智慧體，已經證明了「理解任務→拆解計劃→呼叫工具→依結果調整」這套工作方式很有效。但機器人面對的是無法回滾的物理世界，環境會變、狀態看不全、動作做錯很難撤銷。清華大學、無問芯穹與正行創新聯合發起的RPent,想把這套智慧體範式真正搬進機器人身體裡。

🤔 純VLA與純大模型Agent,各自卡在哪裡

素材指出,具身智慧目前有兩條技術路線:純VLA端到端模型精細操作做得好,但任務一長、場景一擾動就容易退化;純大模型Agent(如CAP-X)理解任務能力強,但在亞釐米級精度、執行時延與「越用越強」這幾件事上有明顯短板。RPent不打算讓單一模型包辦一切,而是拆解成不同層級的能力分工。

🧩 四層架構,讓通用大模型與VLA各司其職

RPent將系統分為使用者層、智慧層、介面層、環境層。使用者層提供類似Claude Code/Codex的互動式CLI與Web Dashboard;智慧層由Agentic Planner(結合基礎模型、Memory、Tool Library)與Action Primitive(把VLA、WAM等專家模型和程式化技能封裝成標準工具)組成,形成「規劃→執行→反饋→記憶更新」的Agentic Loop;介面層把智慧決策轉譯成機器人可執行指令,統一了不同裝置的呼叫方式;環境層目前已支援LIBERO-PRO、RoboCasa、RoboTwin、RoboDojo等模擬環境,以及Franka、雙臂Franka、YAM、SO101等真實裝置。

在連接方式上,RPent用MCP統一描述可呼叫能力、用RPC連接工具與機器人環境使各模組可獨立部署、用MHS提供面向更廣泛物理裝置(未來包括實驗儀器、家庭裝置、工業系統)的統一讀寫控制抽象。這意味著新增一種機器人,理論上只需在robots/目錄接入標準介面,而不必重新開發整套Agent。

💡 Memory讓試錯不再從零開始,Flash Mode讓大模型跟上物理節奏

物理世界的試錯成本遠高於數位環境,一次失敗抓取可能要重新佈置場景。RPent的Memory系統把經驗按複用範圍組織成三層記憶,記錄適用範圍、型別、可信度與支撐證據,新經驗需驗證後才能提升可信度。素材提到,在LIBERO-Pro Goal實驗的位置交換任務中,引入記憶機制後成功率從31.0%提升至87.0%。

大模型推理速度遠慢於機器人動作執行速度,是另一個現實瓶頸。RPent的解法不是追求更快的大模型,而是把驗證過的成功流程壓縮成「任務卡」(Task Card),之後進入Flash Mode時優先照任務卡執行,只在檢查失敗或環境偏離時才重新呼叫規劃器。在LIBERO Object的200次評測中,開啟Flash Mode把平均執行時間從283.6秒降到40.9秒,成功率僅下降3.5個百分點,實現約7倍加速。

📊 Leaderboard:GPT-6 Astra搭配RPent的長程任務成績

RPent同步推出Leaderboard,對比不同基座模型在效能與延時上的表現。在強調指令變化、佈局變化與長程執行的LIBERO-Pro上,RPent/GPT-6 Astra達到92.63%,比第二名RPent/Opus-4.7的82.4%高10.23個百分點,比π_RLinf的50.0%高42.63個百分點。在RoboCasa365 Target50的廚房長程任務中,RPent/GPT-6 Astra以59.20%位列第一,高於RPent/GPT-5.5的57.1%。此外RPent/Opus-4.7在LIBERO達96.0%,RPent/GPT-5.5在RoboTwin達62.4%,均處於榜單前列。

🎯 實務啟示

RPent的核心價值不在於證明某個模型能包辦全部控制,而是展示了通用大模型、VLA專家模型、工具與記憶系統可以在同一開放框架內協同分工。對於想探索具身智慧體的工程師,這套模組化架構與開源程式碼提供了一個可直接參照的落地範本,尤其是任務卡與記憶分層的設計,值得在自己的Agent系統中借鑑。

🔗 來源
- 標題:GPT-6 Astra開進機器人身體!清華聯手無問芯穹等開源RPent
- 作者/機構:思邈,量子位
- 連結:https://www.qbitai.com/2026/09/493218.html

#EmbodiedAI #RobotLearning #VLA #AgenticAI #GPT6Astra #OpenSource #Robotics #LLMAgent #Tsinghua #RoboticsFramework
