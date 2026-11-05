---
title: Faster Retrieval for Better, More Efficient RAG
source: Apple ML
url: https://machinelearning.apple.com/research/faster-retrieval
model: claude-code/sonnet
generated_at: '2026-11-05T22:56:20.202311'
score: 99
---

📌 Apple新研究：讓神經網路學會「怎麼找」，加速RAG檢索

TL;DR：Apple提出用小型神經網路學習MIPS的support function，針對真實query分布最佳化檢索路由，兼顧速度與準確率。

RAG系統裡最常被忽略的一個假設是：你的檢索索引，是照著「key長什麼樣」建的，但實際打進來的，卻是「query長什麼樣」。這兩者如果長得不一樣，再聰明的索引結構也會系統性地找錯答案。

🤔 **MIPS的老問題：key的幾何，不等於query的幾何**

Maximum Inner Product Search（MIPS，最大內積搜尋）是推薦系統、搜尋與 RAG 的核心運算：給定一個 query 向量，要從數百萬候選 key 向量中找出內積最大的那一個，對應的原始資料（在 RAG 中通常是文件）會被接到 query 前面一起處理。當 key 數量達百萬、向量維度達數千時，窮舉比對的計算成本急劇上升，業界普遍用聚類（clustering）與量化（quantization）等近似方法做速度與準確率的取捨。

但這類基線方法有個共通假設：query 的分佈會跟 key 的分佈相似，或是根本不考慮 query 長什麼樣。在RAG場景下，這個假設並不成立——query 通常是使用者臨時打出的短問句，key 卻是經過策劃的長篇資訊性文字，兩者在幾何上差異明顯。而且多數生產環境的 MIPS 應用，面對的是一群既有、查詢分布相對穩定的使用者，這個訊號是通用、不針對 query 分布最佳化的方法沒有用到的。

🧩 **把MIPS看成一個support function，讓神經網路去學它**

傳統MIPS系統把 key 集合切成k個群（k遠小於總key數n），每群維護一個代表性的中心點（centroid）。新 query 進來時先跟k個centroid比對，被路由到最接近的那個群，再跟該群內所有key窮舉比對——理論上可帶來約k倍的加速。但這套路由機制並不精確：一個群裡可能存在一個離自己centroid很遠、卻離query很近的key，當query恰好接近這個「異類」key時，centroid路由會誤判該群分數低而跳過，導致漏掉真正的最佳匹配。

這篇發表於ICML 2026的論文《Amortizing Maximum Inner Product Search with Learned Support Functions》指出一個被忽略的數學結構：把query映射到「它跟集合內任一key的最大內積」這個函式，正是該集合在凸分析（convex analysis）中的support function。這個函式有兩個重要性質：一是它是凸函式，可以用專門處理凸函式的神經網路架構——input convex neural networks（ICNN）來逼近；二是這個support function在任一query處的梯度（gradient），直接就是最佳匹配的key本身。

研究團隊由此提出兩種模型，一次性、離線地在固定key資料庫上訓練：

- **SupportNet**：用（弱約束的）ICNN直接學習support function本身，數學上與問題的凸結構一致。研究發現，為每個聚類分別算一個support function、再用SupportNet學習這k個分數，能顯著改善路由品質——因為它回答的是「這個群裡最好的key，跟這個query到底有多匹配」，而不只是跟centroid的距離。
- **KeyNet**：直接學習在給定query時輸出最佳匹配的key向量，用源自Euler齊次函式定理的一致性損失（consistency loss）把預測結果錨定在底層support function的幾何結構上，即便沒有顯式強制凸性。

兩種模型都是用「實際重要的query分布」中取樣的範例訓練：對每個取樣的query，先用窮舉搜尋算出一次真實最佳匹配並存下來，構成一個捕捉該query分布下MIPS解空間的監督式資料集。

💡 **用學習到的路由取代硬centroid**

文中以一個四群的例子說明：若能拿到每個群的support function，就能依據query與每個群「最佳可能分數」的關係來路由，而非只看跟centroid的距離——這能避免因為異類key被漏判而錯過真正最佳匹配的情況。

🎯 **實務啟示**

對建置生產級 RAG 檢索系統的工程師，這篇研究提醒一個常被忽視的優化空間：如果你的使用者查詢分布相對穩定（多數生產場景確實如此），針對這個具體分布離線訓練一個輕量路由網路，可能比套用通用、query-agnostic 的聚類/量化方案更值得投資；這也呼應了現代機器學習的一個核心思路——針對「可能出現的輸入」而非「所有可能輸入」去最佳化，往往能把算力用在更該花的地方。

🔗 **來源**
- 標題：Faster Retrieval for Better, More Efficient RAG
- 連結：https://machinelearning.apple.com/research/faster-retrieval

#RAG #MIPS #VectorSearch #RetrievalAugmentedGeneration #Apple #MachineLearning #NeuralNetworks #ConvexOptimization #SearchAlgorithms #AppleML
