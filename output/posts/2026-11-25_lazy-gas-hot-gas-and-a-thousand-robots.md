---
title: Lazy gas, hot gas, and a thousand robots
source: Amazon Science
url: https://www.amazon.science/blog/lazy-gas-hot-gas-and-a-thousand-robots
model: claude-code/sonnet
generated_at: '2026-11-25T01:38:43.193358'
score: 108
---

📌 把物流機器人路徑規劃，拆解成一坨氣體物理問題（Amazon ICML 論文）

TL;DR：Amazon 用「冷氣體／熱氣體」物理類比，把 NP 難的多機器人路徑規劃問題，轉成可在數百秒內求解的線性規劃。

倉庫裡有上千臺機器人同時搬貨，每一步都要決定往哪走、要不要停下來等，一旦沒協調好就會互相卡住。這種看似單純的「交通管制」問題，數學上卻是不折不扣的 NP-hard，連中等規模都可能算到天荒地老。Amazon Robotics 在今年 ICML 發表的論文給出了一個意外的解法：把機器人想像成氣體分子。

🤔 **一千臺機器人、數百萬種組合的惡夢**

論文把倉庫地圖抽象成 W×H 的網格，每臺機器人在每個時間步有五種選擇：往北、東、西、南移動，或原地等待。把規劃視野設為 T 個時間步，整個系統大約會有 n = 5WHT 個二元決策變數，也就是最多 2^n 種組合——這還沒算上避免碰撞的限制。這類多機器人路徑規劃（MAPF, multiagent pathfinding）問題在一般情況下是 NP-hard，即使機器人數量只是中等規模，也可能讓最佳化求解器算不出結果。

🧩 **從 1781 年的法國工程師到 1931 年的氣體物理**

作者團隊從最佳傳輸（optimal transport）理論出發重新形式化這個問題。這個理論最早可追溯到 1781 年法國數學家 Gaspard Monge，他想找出搬運挖掘土方到軍事工事的最有效方式，但他的原始形式要求每個來源的質量只能送往單一目的地，本質上是個難解的非線性問題。約 150 年後，蘇聯數學家 Leonid Kantorovich 放寬了這個限制，允許一個來源的質量分散送到多個目的地，把問題轉化成線性規劃（LP），這項貢獻也讓他拿到諾貝爾經濟學獎。

然而經典最佳傳輸只描述「起點分布」與「終點分布」之間的傳輸方案,沒有刻畫中間時刻的位置與碰撞。Amazon 團隊因此採用多重邊際最佳傳輸（multimarginal optimal transport, MMOT），把每個時間步的機器人位置都當作一個邊際分布，讓模型同時涵蓋空間與時間上的移動軌跡。論文證明了一個關鍵性質：只要仔細保留約束矩陣的「全單模性」(total unimodularity, TU),這個 MMOT 形式化就能把原本組合爆炸的匿名 MAPF 問題,轉成在多項式時間內可解的 LP,且解保證是整數解,不會出現「機器人分一半走左邊、一半走右邊」這種不可執行的碎片解。

接著團隊把目光轉向物理學。1931 年 Erwin Schrödinger 曾提出一個問題:已知氣體粒子在兩個時間點的分布,最可能的演化路徑是什麼?熱氣體粒子會透過布朗運動隨機擴散,這與經典最佳傳輸的「冷氣體」圖像——粒子只花最小力氣抵達目的地——恰好形成光譜的兩端。團隊構造出一個介於初始與最終機器人配置之間的 Schrödinger 橋,本質上是 MMOT 問題的熵鬆弛(entropic relaxation),添加的熵量就對應氣體溫度,溫度越低就越接近最佳的冷氣體解。這個鬆弛讓他們能套用高效率的 Sinkhorn iterations 來快速求解。

📊 **478 秒解出 340 萬個決策變數,對手 12 小時算不出一個解**

在一個 150×150 的網格、1,125 臺機器人、規劃視野 T=30 的場景下,系統共有約 340 萬個決策變數。保留 TU 性質的 MMOT 方法在 478 秒內求出最佳機器人軌跡；相較之下,不具 TU 性質的 NP-hard 原始形式化,在 12 小時內往往連一個可行解都找不到。團隊也指出,匿名 MAPF 問題透過這種 MMOT 形式化可以達到最佳解,實測執行時間約為 O(n^1.68) 秒,理論上界約為 O(n³)。

⚠️ **機率的「影子」不能直接執行**

Schrödinger 橋給出的是機率性的解,也就是把每臺機器人的質量,依機率分散到不同的目的地與時間點上。但實體機器人不能真的分裂成一半一半同時走兩條路,因此這個機率性的「影子」規劃無法直接拿來執行,團隊在文中點出了這個待解決的落差,但素材並未提供後續如何把機率解轉回可執行的確定性路徑的細節。

🎯 **給工程師的啟示**

當一個問題在組合層面是 NP-hard,不妨先檢查約束矩陣是否具備全單模性這類結構性質——有時候重新形式化問題本身,比硬上啟發式演算法更有效。同時,「用熵鬆弛換取速度」是一個通用技巧:透過調整單一參數(這裡是溫度/熵),就能在最佳解與計算速度之間連續地找到想要的平衡點,而不是只能二選一。

🔗 **來源**
- 標題：Lazy gas, hot gas, and a thousand robots
- 作者／機構：Amazon（Amazon Robotics / Amazon Science）
- 連結：https://www.amazon.science/blog/lazy-gas-hot-gas-and-a-thousand-robots

#MAPF #OptimalTransport #RoboticsResearch #AmazonRobotics #ICML #LinearProgramming #SchrodingerBridge #WarehouseAutomation #AlgorithmDesign #AppliedMath
