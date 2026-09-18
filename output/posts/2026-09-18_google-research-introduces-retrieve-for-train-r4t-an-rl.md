---
title: 'Google Research Introduces Retrieve-for-Train (R4T): An RL-Compiled Diffusion
  Retriever for 12× to 20× Faster Query Fan-Out'
source: MarkTechPost
url: https://www.marktechpost.com/2026/09/16/google-research-introduces-retrieve-for-train-r4t-an-rl-compiled-diffusion-retriever-for-12x-to-20x-faster-query-fan-out/
model: claude-code/sonnet
generated_at: '2026-09-18T19:45:27.818110'
score: 103
---

📌 【Google Research】RL 訓練一次，Diffusion Retriever 讓查詢擴展快 12 到 20 倍

TL;DR：R4T 用 RL 離線學會多樣化 query fan-out，蒸餾進 diffusion 模型後單次前向就能生成全部檢索方向。

搜尋一個「露營裝備」，你期待看到帳篷、睡袋、爐具、頭燈,而不是十頂長得幾乎一樣的帳篷。這正是 query fan-out（把一個籠統查詢拆成多個子查詢）要解決的問題,但 Google Research 發現,讓 LLM 在推論時即時做這件事,會撞上兩個結構性麻煩。

🤔 **paraphrastic collapse 與延遲,兩個推論時的陷阱**

研究團隊觀察到,zero-shot 的 Qwen3-4B 面對「Bohemian festival style」時,寫出的子查詢是「bohemian festival fashion」和「festival bohemian clothes」,這類近義詞彼此高度相似,檢索回來的結果自然也高度同質(paraphrastic collapse)。另一個問題是延遲:自迴歸生成加上多次檢索呼叫本身就慢,而 Best-of-N 取樣雖能提升品質,卻等比例放大推論成本。

🧩 **RL 練一次,蒸餾進 diffusion 模型跑一次**

R4T(Retrieve-for-Train)的做法是:用強化學習離線訓練一次,學出「好的 query fan-out」該長什麼樣子,再把這個行為蒸餾進一個小型 diffusion 模型,讓它一次前向就產生全部檢索方向,不必再迭代生成。

針對開放式抽象檢索(OAR),獎勵函數由三個加權項組成;針對弱監督組合式檢索(WSCR),獎勵則是 fan-out 檢索到參考集合中項目的比例。消融實驗說明了三項 OAR 獎勵為何都不可或缺:只用 groundedness 時,Gemma3-4B 收斂成「line ending line ending line ending」這種無意義字串;加入 alignment 反而讓 collapse 更快,策略開始不斷複述查詢本身的同義詞;只有同時加入 diversity,兩種走捷徑的行為才被堵住。

訓練採用 GRPO 搭配 soft PPO 正則化(加入前向與反向 KL 懲罰),關鍵設定為 group size 8、learning rate 1×10⁻⁷、global batch size 512。實驗分別在 Polyvore 時尚穿搭資料集(搭配 CLIP-based matryoshka encoder,128 維)以及一組專有的專家歌單音樂資料集(MuLan embeddings)上進行。每種 fan-out 方法都產生 k=10 個子查詢,Best-of-N 則設 N=5,OAR 品質由 LLM 裁判以 5 分制 Likert 量表評分。

📊 **多樣性提升,速度快一個數量級**

在 Polyvore 上,Gemma3-4B 搭配 R4T-FOLM 平均分數為 49.1,優於 Best-of-N 的 40.9 與 zero-shot 的 38.5;多樣性指標從 zero-shot 的 56.0 提升到 76.8,R4T-Diffusion 仍保留了大部分,達 74.3(diffusion 版不產生文字子查詢,因此 groundedness 未被回報)。在音樂資料集上,R4T-FOLM 平均 58.1,優於 Best-of-N 的 49.2。

WSCR 在 Polyvore 上則呈現覆蓋率與多樣性的取捨:R4T-FOLM(Qwen)拿下 Recall@5K 20.9、Hit@5K 64.6,超過 Gemini-2.5-Flash 的 15.7 與 52.1,但其 Vendi Score 掉到 27.5,作者將此歸因於高強度 RL 最佳化下輸出熵下降;R4T-Diffusion(Qwen)則保留較高的 Vendi Score 34.7,Recall@5K 為 16.5。

速度差異最直觀:batch size 8 時,自迴歸 fan-out 約需 1.46 秒,diffusion 只要 0.07 秒;batch size 1024 時,自迴歸逼近 50 秒,diffusion 僅 4.21 秒。作者總結為一致的 12 倍到 20 倍加速。

🎯 **實務啟示**

如果你的檢索或推薦系統需要輸出「一組」而非「一個」結果,而目前用 LLM 即時生成子查詢,R4T 的思路值得參考:把昂貴的探索行為(RL)放到離線訓練階段,線上服務用小而快的模型執行,是用推論成本換訓練成本的典型範例,也是 diffusion 模型在非影像生成任務上的一個有趣應用。

🔗 **來源**
- 標題:Google Research Introduces Retrieve-for-Train (R4T): An RL-Compiled Diffusion Retriever for 12× to 20× Faster Query Fan-Out
- 作者/機構:Asif Razzaq, MarkTechPost
- 連結:https://www.marktechpost.com/2026/09/16/google-research-introduces-retrieve-for-train-r4t-an-rl-compiled-diffusion-retriever-for-12x-to-20x-faster-query-fan-out/

#GoogleResearch #InformationRetrieval #DiffusionModels #ReinforcementLearning #QueryFanOut #GRPO #RecommenderSystems #MachineLearning #RAG #LLM
