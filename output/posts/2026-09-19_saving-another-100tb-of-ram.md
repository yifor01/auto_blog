---
title: Saving another 100TB of RAM
source: Hacker News
url: https://blog.cloudflare.com/saving-100-tb-of-ram-with-math/
model: claude-code/sonnet
generated_at: '2026-09-19T19:33:36.392865'
score: 54
---

📌 Cloudflare靠一點機率數學，省下100TB記憶體

TL;DR：Cloudflare發現負載平衡服務的consistent hashing用太多記憶體，用機率統計重新檢視了雜湊點數量的設計。

當你的服務跑在數千臺伺服器、動用數PB記憶體與數百萬CPU核心時，1%的節省聽起來微不足道，但實際換算下來可能是上百TB的等級。Cloudflare最近的一篇工程部落格，就記錄了他們如何靠重新審視一個經典演算法，省下超過100TB的全球記憶體。

🤔 **一張工單，牽出的記憶體超額使用問題**

故事起點是Cloudflare的Performance團隊成員Ivan提交的一張工單：內部負載平衡服務Pingora Backend Router（簡稱PBR）中，與pingora-ketama（Cloudflare開源的consistent hashing函式庫）相關的結構，記憶體用量遠超預期。PBR的作用是把可快取的請求依URL路由到伺服器，確保每個檔案在每個資料中心只需保存一份副本，並提供穩定的定位方式。

🧩 **Consistent Hashing是什麼，為什麼會吃記憶體**

Consistent hashing是一種常見的任務分派方法：把伺服器與任務（例如以IP位址、cache key）都透過雜湊函式映射到同一個數字線（或想像成一個環）上，每個任務會被指派給數字線上離它最近的伺服器。這個設計的好處是伺服器增減時，只需重新調整少量任務歸屬，不需要大搬風。

但問題在於：雜湊值本質上接近隨機數，所以每臺伺服器在數字線上分到的區間大小並不平均，有的伺服器可能分到特別長的一段區間，處理的請求量也會遠高於其他伺服器。

📊 **用統計量化「不公平」有多嚴重**

文章用期望值（Expected value）與標準差（Standard deviation）來描述這個問題。對於N臺伺服器中的其中一臺，其負責區間佔全體的比例，統計上可以算出：

- 期望值 Exp = 1/N
- 標準差 SD = (1/N) × sqrt((N-1)/(N+1))

以100臺伺服器為例，Exp = 1%，SD約等於0.99%。乍看還算合理，但如果換算成「相對於目標值的誤差比例」（也就是變異係數 CV = SD/Exp = sqrt((N-1)/(N+1))），在N=100時CV約達99%，意味著某些伺服器實際負擔可能比預期多出將近一倍，處理的請求量是「應得」份量的兩倍，而另一些伺服器則幾乎閒置。

💡 **解法只能是：加更多雜湊點**

Consistent hashing的簡單性是把雙面刃：因為所有東西都被壓縮成數字線上的一個點，任何改善方案也只能透過「加更多雜湊點」來實現——為每臺伺服器產生多個雜湊值，而不是只有一個。文章用大數法則的直覺解釋：單一區間的標準差雖大，但把許多小區間加總起來，忽長忽短的區間彼此抵消，整體就會趨於平均。NGINX把每臺伺服器預設雜湊點數硬編碼為160個，Pingora沿用了相同的預設值。以100臺伺服器的例子計算，把雜湊點從1個增加到160個，變異係數會從約99%大幅降至約8%。

⚠️ **素材未完整揭露的部分**

原文在探討「如果再加更多雜湊點會怎樣」時被截斷，Cloudflare團隊最終如何權衡雜湊點數量與記憶體用量、具體採用了什麼調整方案來達成100TB的節省，素材並未提供細節，有興趣的讀者建議查閱原文全文。

🎯 **實務啟示**

如果你的系統也用了consistent hashing做負載平衡或cache路由，這篇文章提醒了一件常被忽略的事：像「每臺伺服器160個雜湊點」這種預設值，往往是套用主流函式庫（如NGINX）的慣例，而非針對自身規模重新算過的結果。在大規模部署下，雜湊點數量與記憶體使用量之間的權衡值得用機率統計重新檢視,而不是照抄預設值。

🔗 **來源**
- 標題：Saving another 100TB of RAM
- 作者／機構：Cloudflare（經 Hacker News 用戶 f311a 分享）
- 連結：https://blog.cloudflare.com/saving-100-tb-of-ram-with-math/

#Cloudflare #ConsistentHashing #Rust #SystemsEngineering #Pingora #LoadBalancing #PerformanceEngineering #DistributedSystems #MemoryOptimization #BackendEngineering
