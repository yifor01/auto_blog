---
title: 'Meta AI Open-Sources Rebalancer: A C++ Assignment Solver That Runs About 40
  Million Placement Problems a Day'
source: MarkTechPost
url: https://www.marktechpost.com/2026/10/06/meta-ai-open-sources-rebalancer-a-c-assignment-solver-that-runs-about-40-million-placement-problems-a-day/
model: claude-code/sonnet
generated_at: '2026-10-07T22:23:57.186554'
score: 86
---

📌 Meta 開源九年內部驗證的分配求解器 Rebalancer

TL;DR：Rebalancer 是 Meta 內部用了 9 年多的 C++ 組合最佳化函式庫，如今以 Apache 2.0 開源並上架 PyPI，號稱每天處理約 4000 萬個配置問題。

機架要塞進哪個資料中心、伺服器要跑哪個服務、任務要分給哪臺機器、使用者流量要導到哪個機房——這些看似簡單的「分配」決策，背後都是 NP-hard 問題。Meta 把內部用了 9 年的解法開源了。

🤔 **機架、伺服器、流量，每天 4000 萬次的分配決策**

根據 Meta 工程部落格，Rebalancer 用來解決 Meta 內部大量的 assignment problem：在特定限制與目標下，決定哪些物件要放進哪些容器。Meta 指出推廣這類系統有兩大障礙：一是可用性，工程師很難把營運政策轉成精確的數學公式；二是規模，許多問題本質是 NP-hard，規模大到一般商用求解器無法負荷。

🧩 **先定義問題，再選怎麼解**

Rebalancer 的設計理念，是把「問題怎麼描述」與「問題怎麼求解」分開，這套做法詳述於 OSDI 2024 論文《Optimizing Resource Allocation in Hyperscale Datacenters》。其規格語言分為三層，以 Meta 自己的範例來說：任務是物件（object）、伺服器是容器（bin）、機架是範圍（scope）；`CapacitySpec` 限制每臺伺服器的 CPU 與儲存容量上限，`GroupCountSpec` 確保每個機架只容納一種工作類型，`BalanceSpec` 則讓每臺伺服器在兩個維度上的使用率保持平衡。Rebalancer 會把這份規格編譯成一張有向無環的運算式圖：葉節點存放使用率數值，聚合與轉換節點則建構在其上；使用者只需提供初始配置與停止條件，而初始配置中已違反的限制會自動被標記為高優先目標。

求解端提供兩種引擎：**精確解（Optimal solver）** 把運算式圖轉譯成混合整數規劃（MIP），交給 FICO Xpress、Gurobi 或 HiGHS 求解，並透過變數聚合與對稱性消除縮小模型規模，但最差情況下模型大小仍是物件數乘以容器數的量級；**區域搜尋（Local search）** 則直接在運算式圖上操作，嘗試把物件搬到其他容器，最差情況下的搜尋鄰域只跟物件數加容器數成正比，評估過程經過平行化，每秒可達數百萬次評估，並對搜尋空間做剪枝。Meta 對絕大多數大型問題使用區域搜尋，中小型問題則用 MIP，且常先用 MIP 做原型驗證。

為了解決模型除錯耗時的問題，Meta 也一併開源了 Rebalancer Explorer——一套 Docker 化的網頁介面，可以顯示哪些限制正在生效、放寬限制會有什麼影響，以及某個物件為何被分配到特定容器。

📊 **現在就能裝：pip install rebalancer**

套件以 Apache 2.0 授權釋出，附完整文件；`pip install rebalancer` 可安裝 v1.0.4，支援 Python 3.12 以上，提供 Linux x86-64 與 macOS 14+ ARM64 的預建 wheel，另有 .deb、.rpm 與 Homebrew 套件可選。不過 PyPI 上目前仍將此專案標示為 Alpha 版本。

與同類工具相比，OR-Tools 涵蓋的問題類型更廣，Timefold 則專攻 JVM 上的排程與路徑規劃；Rebalancer 的差異化在於同一套 assignment spec 可以同時餵給區域搜尋與 MIP 兩種引擎求解，不需為不同求解器重寫問題定義。

🎯 **實務啟示**

如果團隊正面對大規模資源分配問題（排程、裝箱、負載平衡），Rebalancer 提供了一條經過 Meta 近十年生產環境驗證的路徑，且開源授權寬鬆、可直接自架。但考量 PyPI 仍標示 Alpha，導入正式生產前建議先用現有的 MIP 原型路徑做小規模驗證。

🔗 **來源**
- 標題：Meta AI Open-Sources Rebalancer: A C++ Assignment Solver That Runs About 40 Million Placement Problems a Day
- 作者／機構：Asif Razzaq（MarkTechPost）
- 連結：https://www.marktechpost.com/2026/10/06/meta-ai-open-sources-rebalancer-a-c-assignment-solver-that-runs-about-40-million-placement-problems-a-day/

#OpenSource #CombinatorialOptimization #AssignmentProblem #MetaAI #CPlusPlus #ResourceAllocation #OperationsResearch #MIP #LocalSearch #DatacenterEngineering
