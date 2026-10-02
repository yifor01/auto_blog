---
title: Fine-tune a search agent with multi-turn RL on Amazon SageMaker AI
source: AWS ML
url: https://aws.amazon.com/blogs/machine-learning/fine-tune-a-search-agent-with-multi-turn-rl-on-amazon-sagemaker-ai/
model: claude-code/sonnet
generated_at: '2026-10-02T21:28:37.562178'
score: 100
---

📌 【AWS 實測】多輪強化學習微調搜尋 agent,失敗率從 22.89% 砍到 0.68%

TL;DR：AWS 用 SageMaker AI 的多輪 RL 微調搜尋 agent,retrieval 品質與可靠性同步大幅提升。

你可能遇過這種情況:prompt 一個小模型做多輪搜尋,它永遠學不會「什麼時候該停」;換成前沿大模型,行為穩了,但帳單也跟著變重。AWS 這篇技術文章提供了第三條路。

🤔 **多輪決策,單輪 RL 抓不住**

搜尋 agent 要自主決定搜什麼、用什麼檢索策略、什麼時候該停,而且是跨多輪互動逐步修正。傳統的 supervised fine-tuning(SFT)需要高品質的多輪示範軌跡,這類資料通常根本不存在,蒐集成本也很高。單輪強化學習(例如 RLVR)則是一次只替一個回應打分,但搜尋 agent 的每一輪決策彼此相依,單獨最佳化某一步會漏掉這些跨輪依賴關係。AWS 的解法是用 multi-turn reinforcement learning(MTRL),把整條軌跡一起最佳化,reward 只需要反映最終結果好不好。

🧩 **Amazon SageMaker AI MTRL 怎麼設定**

這次微調的對象是 Qwen3.6-27B(目前在美西奧勒岡區域 us-west-2 支援),設定成擁有兩個搜尋工具的企業搜尋 agent,並限制每個問題可用的輪數(一輪即一次使用者與 agent 的互動),避免模型生成過長回應、同時鼓勵更有效率的搜尋行為。訓練分三個要素:資料集、reward 函式、MTRL 任務設定。評測主指標是 nDCG@10(Normalized Discounted Cumulative Gain at rank 10),衡量前 10 筆檢索結果與理想排序的吻合程度,1.0 代表完美排序,0.0 代表完全沒檢索到相關文件。這個指標直接拿來當 MTRL 的 reward,屬於軌跡層級(trajectory-level)的 reward——agent 走完整輪搜尋後,才依最終檢索結果打分。當 agent 用到最大輪數上限或單輪 token 上限時,會直接給 -1 的懲罰,用這種懲罰式設計明確教模型避開這類失敗模式,而不需要手刻複雜的中間 reward。整個設定只動了三個超參數,其他全部維持預設值——包括演算法、advantage estimator、off-policy staleness bounds 這些通常需要 RL 專業知識才會調整的項目。

📊 **四個基準裡贏三個,可靠性提升最明顯**

微調後的模型在四個held-out基準中的三個上有改善:BrowseComp-Plus 的 nDCG@10 提升 23.7%,WixQA 提升 18.4%,Wands 有較小幅度的提升;FreshStack 上則出現小幅退步。比起品質數字,更值得注意的是可靠性的變化——BrowseComp-Plus 的失敗率從 22.89% 直接降到 0.68%,代表模型不只搜得更好,也學會了在輪數與 token 預算內把任務收尾。訓練曲線顯示,訓練集與驗證集的 nDCG@10 都隨訓練步數穩定上升,並在訓練後期趨於飽和,意味著再延長訓練也不會有太多額外收益。

💡 **訓練可能跨好幾天,別忘了 checkpoint 續訓機制**

MTRL 訓練可能橫跨多天,而 MTRL 服務預設的時間上限是 24 小時(可透過 CreateJob 的 JSON schema 調整)。如果任務因超時或基礎設施錯誤而中斷,可以用 resume 機制從既有 checkpoint 繼續訓練,不必從頭來。

⚠️ **並非每個基準都有進步**

FreshStack 上出現了輕微的效能退步,說明 MTRL 微調不是萬用解方,仍會因資料集特性不同而有差異;文中數字也都是 AWS 自家評測跑出來的結果,尚無第三方複測。

🎯 **實務啟示**

如果你的 agent 任務有清楚的 reward 訊號(像 retrieval 品質)、明確的多輪互動迴圈,以及定義清楚的工具環境,MTRL 微調值得一試——而且照 AWS 這次的經驗,大部分 RL 超參數都能維持預設,不需要堆疊複雜的中間 reward 設計。

🔗 **來源**
- 標題：Fine-tune a search agent with multi-turn RL on Amazon SageMaker AI
- 作者／機構：Huibin Shen, AWS Machine Learning Blog
- 連結：https://aws.amazon.com/blogs/machine-learning/fine-tune-a-search-agent-with-multi-turn-rl-on-amazon-sagemaker-ai/

#ReinforcementLearning #SearchAgent #AmazonSageMaker #MultiTurnRL #AgenticAI #LLMFineTuning #Qwen #InformationRetrieval #AWS #AIAgents
