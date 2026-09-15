---
title: Your Agent Aced the Task. Will It Do It Again?
source: HuggingFace Blog
url: https://huggingface.co/blog/ibm-research/altk-evolve-consistency
model: claude-code/sonnet
generated_at: '2026-09-15T20:32:13.513676'
score: 91
---

📌 同樣的任務，Agent下次還會成功嗎

TL;DR：IBM Research 發現 agent 平均成功率高但重複執行常失敗，並提出縮小落差的方法。

一個 agent 這次把任務做對了，不代表它下次還會走同樣的路。在正式場合這只是尷尬，但在生產環境裡，這是可靠性問題:對帳、合約條款檢查這類任務，同一個請求換一次執行結果就不同，可能是無法接受的。

🤔 大家都只報告平均值

標準的 agent 評測方式是 Mean@k：把 benchmark 跑 k 次取平均成功率，這就是排行榜上「77% 準確率」的意思。但 Mean@k 回答的是「這個 agent 平均有多好」，不是使用者真正關心的「我再問一次同樣的問題，它還會成功嗎」。要回答後者，需要看 Pass^k：k 次執行全部成功的任務比例。文中特別提醒 Pass^k 不是常見的 Pass@k——Pass@k 是樂觀版本，問的是「k 次裡至少一次成功」;Pass^k 則是悲觀鏡像，要求每一次都成功。三者關係恆為 Pass^k ≤ Mean@k ≤ Pass@k。

在 AppWorld 的 test_normal 上，一個以 GPT-4.1 為底的 ReAct agent 五次重複執行的 Mean@5 高達 77.4%，看起來相當不錯;但 Pass^5 只有 53.0%。也就是說，將近四分之一的任務屬於「agent 有時候解得出來、有時候解不出來」，而任務本身完全沒變。這個 Mean@k 減去 Pass^k 的落差，文中稱為「一致性缺口（consistency gap）」，在困難任務上這個缺口甚至擴大到 30 個百分點。

🧩 尖銳分佈 vs. 扁平分佈：agent 為什麼會「翻牌」

每次 agent 決定要呼叫哪個 API、傳什麼參數，這個決定都來自一個 next-token 的機率分佈。分佈「尖銳」時，機率大量集中在單一 token，其餘候選遠遠落後，同一個決定會一次次重複出現，對雜訊有韌性;分佈「扁平」時，好幾個 token 的機率互相接近,誰勝出接近擲硬幣,一點點雜訊（例如 GPU 浮點運算非結合性、請求批次處理等平臺端效應）就可能讓結果翻盤。一條軌跡串接數十個決策，每個決策一點點翻盤機率累積起來，就會變成整體很大的失敗機率——這正是 24 個百分點落差的來源。文中也特別說明，這個問題不是靠固定 seed 或貪婪解碼（greedy decoding）就能解決的：這些設定只決定「怎麼把分佈轉成 token」，不改變分佈本身的形狀，因此即使 ReAct agent 全程用 temperature 0.0 執行，上述變異依然存在，並非一般取樣雜訊造成。

延續先前提出的 ALTK-Evolve（把 agent 自己過去的軌跡蒸餾成可重用指引，並在推論時注入）,這篇文章加入名為 Consistency Analyzer 的診斷工具，衍生出新的「一致性指引（consistency guidelines）」。做法分兩階段:第一階段「偵測」,對一條已記錄的軌跡,在每個決策步驟用同一個 context 重新取樣 k 個候選（預設 k=5),藉此量化該步驟的輸出變異程度，寫成一張標出「哪些決策容易翻牌」的計分卡。這個過程完全黑箱操作,不需要模型內部的 logits，也不必真的重跑整個任務。第二階段「生成」,把被標記的高風險步驟轉成標準 ALTK-Evolve 格式的候選指引。文中舉了一個從 AppWorld 任務「How many activities are done in my bucket list as per my SimpleNote note?」的真實軌跡生成的例子:一條指引提醒計算 checkbox 標記時要用行錨定的正規表示式而非單純字串計數(因為筆記標題常在圖例列重複符號)；另一條提醒查詢筆記時要先確認是否有多筆符合結果再繼續。

📊 落差從 24.4 縮小到 12.0 個百分點

導入一致性指引後，同樣任務的一致性缺口從 24.4 個百分點降到 12.0 個百分點:同任務的 Pass^5 提升 16.0 個百分點，類似任務提升 13.0 個百分點,而且沒有犧牲平均準確率。完整方法與評測細節發表於 arXiv 上的技術報告。

💡 一致性是獨立於能力的另一個維度

文中強調，一致性缺口不是靠換更大的模型就能解決的能力問題,而是一個正交的軸線:一個 agent 可以同時「很強」又「不穩定」。Consistency Analyzer 鎖定的是「不穩定」本身，而不是「失敗」——它專門抓那些這次剛好做對、但下次很容易做錯的決策點。

⚠️ 限制

該分析需要一條已記錄的軌跡作為輸入才能運作,屬於事後診斷而非預先預防；縮小後的一致性缺口（12.0pp）仍然存在，並未完全消除。

🎯 實務啟示

對於對帳、合約審查這類任務相同就該得到相同結果的場景,只看 Mean@k 排行榜分數是不夠的,應該額外用 Pass^k 衡量重複執行的穩定度,並考慮用類似 Consistency Analyzer 的方法找出 agent 決策鏈中「容易翻牌」的環節,針對性地補強而非整體重新訓練。

🔗 來源
- 標題：Your Agent Aced the Task. Will It Do It Again?
- 作者／機構：Evelyn Duesterwald 等人（IBM Research）
- 連結：https://huggingface.co/blog/ibm-research/altk-evolve-consistency

#AIAgents #LLM #Reliability #Benchmarking #IBMResearch #HuggingFace #AppWorld #AgenticAI #MachineLearning #Consistency
