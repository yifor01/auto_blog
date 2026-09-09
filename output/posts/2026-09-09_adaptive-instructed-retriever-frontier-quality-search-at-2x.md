---
title: 'Adaptive Instructed-Retriever: Frontier-Quality Search at 2x Lower Latency'
source: Databricks
url: https://www.databricks.com/blog/adaptive-instructed-retriever-frontier-quality-search-2x-lower-latency
model: claude-code/sonnet
generated_at: '2026-09-09T19:58:46.909698'
score: 100
---

📌 Databricks 新檢索模型：速度快兩倍卻不犧牲準確度

TL;DR：Adaptive Instructed-Retriever 用強化學習教模型「該多查幾步時才多查」，兼顧速度與準確率。

多數企業檢索系統得在「查得準」與「查得快」之間二選一。Databricks 的做法是乾脆讓模型自己學會判斷：這個問題值得多花幾步查，還是一步就該收工。

🤔 **企業資料代理面對的兩難：單步夠快，但多跳問題吃不消**

Databricks 稍早發布的 Instructed-Retriever-1，能結合企業資料 schema 與自訂指令，並用平行測試時擴展（parallel test-time scaling）在低延遲下提升檢索準確率，這種單步搜尋方式已能應付大部分使用者請求。但更複雜的多跳（multi-hop）問題,仍需要序列式搜尋:模型反覆蒐集證據、修正查詢,而這會犧牲延遲。這正是 Databricks 資料代理 Genie Code 所面對的檢索效率問題：如何在龐大、持續變動的工作區中,找到正確的資料表、筆記本、儀表板與文件，同時不浪費輪次做地毯式搜尋。

🧩 **用 CISPO 強化學習，教模型「按需搜尋」**

Databricks 因此推出 Adaptive Instructed-Retriever，設計上對序列搜尋步數設有固定上限，並訓練代理依請求難度自行決定要花多少運算：證據足夠時提早停止並回傳結果，判斷還需要更多搜尋時,則可以繼續搜尋直到步數上限。

訓練資料延續 Instructed-Retriever-1 的合成企業檢索環境與代理式資料生成流程(方法已發表於 KARL report)，並沿用原有訓練資料以保留模型快速單步搜尋的能力,同時加入更適合多步搜尋的合成多跳問題。訓練上,從基礎模型出發,使用線上強化學習(Online Reinforcement Learning, ORL),以 CISPO(Clipped Importance Sampling Policy Optimization)進行端到端最佳化。獎勵設計同時衡量軌跡品質與搜尋成本:高品質軌跡給予獎勵,而沒有帶來對應效能提升的額外搜尋步驟則會被懲罰。整套訓練透過 Databricks 的 AI Runtime(AIR)完成,該平臺也開放給 Databricks 客戶用於訓練自家領域的專用模型。

📊 **5.8 秒回答，比對照組快兩倍以上**

在混合多項企業內部與公開檢索基準(包含需要多跳推理的任務)的評測中，Adaptive Instructed-Retriever 的表現與 Claude Sonnet 5、GPT-5.6 Luna 等領先第三方模型,以及開源模型 DeepSeek-V4-Flash 相當，但端到端回應時間僅 5.8 秒,比上述三個模型都快超過兩倍。

💡 **透過調整步數懲罰，直接畫出品質—延遲前沿**

訓練過程中，Databricks 透過調整 ORL 訓練時步數懲罰的強度，得到一整組落在不同品質—延遲位置的 checkpoint：懲罰較輕，模型會多走幾步、拿到更高分數；懲罰較重，延遲更低。這條「前沿」上的每一個 checkpoint,相較未經訓練的 Instructed-Retriever 基礎模型，都在相近或更低延遲下取得更高品質，顯示效能提升確實來自「學會何時該搜尋、何時不必」，而非單純加大模型規模。在前沿頂端,模型分數可媲美其他領先模型,同時速度快上兩倍以上。

文中也舉了兩個具體例子：面對「Company X 是否在 FY2022 損益表中明確列出重組成本這個項目」這類問題，Adaptive Instructed-Retriever 比 Sonnet 提早一步、比 Luna 提早兩步就達到相同的獎勵分數;面對「哪些客戶在使用或考慮使用 LiteLLM Proxy」這類問題,模型會從廣泛探索轉為針對性帳戶搜尋，以最少步數之一(與 Sonnet 打平)拿下最高獎勵。

🎯 **實務啟示**

這套做法提供了一個可複製的思路：與其一味追求更大模型,不如針對「何時該多花運算」這個決策本身進行強化學習訓練。因為不同 checkpoint 對應不同的品質—延遲取捨，團隊可依生產環境的實際需求(互動場景重速度、離線高難度檢索重品質)直接挑選對應的 checkpoint，而不必重新訓練。

🔗 **來源**
- 標題：Adaptive Instructed-Retriever: Frontier-Quality Search at 2x Lower Latency
- 作者／機構：Databricks
- 連結：https://www.databricks.com/blog/adaptive-instructed-retriever-frontier-quality-search-2x-lower-latency

#Databricks #RAG #RetrievalAugmentedGeneration #ReinforcementLearning #LLM #EnterpriseAI #AIAgents #InformationRetrieval #MachineLearning #ModelTraining
