---
title: Graph-centric agentic intelligence
source: Amazon Science
url: https://www.amazon.science/blog/graph-centric-agentic-intelligence
model: claude-code/sonnet
generated_at: '2026-10-01T22:05:33.088564'
score: 86
---

📌 Amazon Science：用圖譜讓AI Agent看懂網路的因果關係

TL;DR：Amazon展示把網路建模成graph後，agent如何靠三階段cascade演算法在複雜拓樸中快速定位故障根因。

當網路故障牽涉數千個節點、數萬筆告警，人類維運人員要在客戶感受到影響前找出根因，幾乎是不可能的任務。Amazon這篇文章給的答案是：讓graph結構本身變成agent可以直接推理的基底。

🤔 背景：為何表格資料不夠，圖才是答案

文章主張，graph保留了真實系統的拓樸，也就是什麼連到什麼、影響如何流動，這對agent要做的因果推論、依賴追蹤、組合式推理而言是必要的骨架。對網路而言這不是比喻，每一臺裝置、每一條連結、每一個通訊通道與服務依賴，本身就是graph裡的vertex或edge，規模可達數百萬個元素。

傳統根因分析（root cause analysis）常依賴時序關聯：若告警A先於告警B發生，就推論A導致B。但在複雜拓樸中，故障會沿著多條平行路徑傳播，輪詢間隔（polling interval）讓時間順序變得不可靠，而真正的根因有時根本不會產生任何告警。文章指出，複雜的多層故障在傳統network operations center平均要花四到五小時才能修復，有時甚至拖到數天；瓶頸不是工程師的專業能力不足，而是人類沒辦法在客戶受影響累積之前，比系統更快地關聯數百個告警、設定檔與遙測資料。

🧩 方法：graph演化的三個世代，最終匯聚成agentic推理

文章回顧了graph用於網路的演進脈絡：最早只是拓樸表示，用來算路徑、秒級隔離故障。加入knowledge graph與ontology後，開始定義「什麼是cell」「什麼是SLA breach」等語意，讓跨廠牌、跨世代網路的操作變得machine-readable。Alarm correlation graph把網路告警之間的階層關係映射出來，能把數萬筆原始告警在幾分鐘內收斂成一條因果鏈，但需要預先定義好的告警階層。Dependency graph解決了這個限制：從SDN、NFV controller即時自動產生，讓貝氏故障定位（Bayesian fault localization）在30秒內達到95%準確率，且不需要人工撰寫規則。Causal subgraph進一步把即時告警轉成有向無環圖（directed acyclic graph），揭露KPI的傳播路徑，給維運人員的是證據而非預測。Graph neural network（GNN）則學到拓樸與因果結構單獨看不出來的東西：隱藏的cell間依賴、節點失效後本該出現卻沒被記錄到的資料模式，以及時空動態。

這些進展是逐步疊加的，如今已經匯聚成一套系統：同一個網路可以同時被表示成拓樸圖、用ontology語意標註、用時序KPI標記，並由GNN做推理，最後由一層agentic邏輯決定針對每種故障模式該用哪個graph工具。文章將此形容為graph從「被動的資料模型」變成「主動的agentic推理基底」。

📊 案例：三階段cascade演算法做根因定位

Amazon設計了一套結合cascaded graph演算法與agentic-AI執行的方法，並與NTT DOCOMO在今年稍早的Mobile World Congress上展示，在商用網路上於數分鐘內完成根因分析。整個方法建立在三根支柱上：graph建模、graph-centric分析、agentic orchestration。

數位雙生（digital twin）把網路表示成持續同步的graph，vertex是帶有屬性的裝置，edge代表連線關係，整合多個資料來源跨網路區段與層級的依賴、即時告警與KPI。在此之上，系統執行三階段cascade分析：Stage 1「分解」依連接數量與強度找出拓樸中連接最密集的部分，故障切斷連結後網路可能分裂成互不相連的子圖，這讓分析可以立刻聚焦在邊界節點，避免在未受影響的區域浪費運算，候選範圍從數千個節點收斂到數百個。Stage 2「分群」在受影響的元件內，用社群偵測演算法（Louvain或label propagation）把經常互動或共享依賴的節點分成一群，藉此分辨故障是侷限在單一群組還是跨群組傳播，候選範圍從數百個收斂到數十個。Stage 3「中心性排序」在已識別的群組內，用一組centrality演算法為候選節點排序根因可能性：標準的centrality演算法（PageRank、degree centrality、closeness）衡量的是結構重要性，這些答案是靜態的，故障發生與否都不會變；但根因分析問的是「相對於這次故障，哪個節點最重要」，告警節點定義了參考座標系，因此每一種centrality都必須針對告警集合重新計算，而非針對整個圖。例如Personalized PageRank從正在發出告警的節點開始做random walk，排序聚焦在告警節點的共同祖先上，沿著階層式拓樸往上追溯故障源頭；degree centrality的計算方式也改成只計算連到告警節點的邊，一個有50條連線但零條連到告警節點的gateway會得零分，而一個有五條連到告警節點的switch則得五分。

⚠️ 限制

素材偏向概念性闡述與方法論描述，並未提供演算法的程式碼，具體量化數據也僅限於dependency graph的95%準確率／30秒內，以及與NTT DOCOMO在MWC展示達成「數分鐘內完成根因分析」，更細節的內容素材指向另一篇文章「Beyond correlation: Finding root causes using a network digital twin graph and agentic AI」。

🎯 實務啟示

如果你負責維運大規模分散式系統（不限於電信網路），這套「先分解縮小範圍、再分群聚焦、最後用針對故障集合重新計算的centrality排序」的三階段思路，比單純依賴時序關聯更能應對平行故障傳播路徑的場景，值得在設計自己的根因分析系統時參考這套收斂邏輯。

🔗 來源
- 標題：Graph-centric agentic intelligence
- 作者／機構：Amazon Science
- 連結：https://www.amazon.science/blog/graph-centric-agentic-intelligence

#AmazonScience #GraphNeuralNetworks #AgenticAI #RootCauseAnalysis #NetworkOperations #DigitalTwin #KnowledgeGraph #GNN #AIOps #NetworkAI
