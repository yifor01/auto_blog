---
title: '[AINews] not much happened today'
source: Latent Space
url: https://www.latent.space/p/ainews-not-much-happened-today-cee
model: claude-code/sonnet
generated_at: '2026-10-03T20:02:24.614854'
score: 59
---

📌 一天之內，模型成本效能前沿被重畫了多少？

TL;DR：GPT-6.1 Sol 大降價逼近 Astra 水準，Anthropic 包辦 Agent Arena 前三，決策模型與長程控制研究同步升溫。

標題寫著「今天沒什麼大事」，但掃過一輪 12 個 subreddit 與 544 個 Twitter 帳號後，光是定價策略的調整，就足以重畫整個模型選型的成本效能地圖。

🧩 **GPT-6.1 Sol 用價格改寫成本效能前沿**

OpenAI 將 GPT-6.1 Sol 定價為每百萬輸入／輸出 token 2 美元／10 美元，相較之下，Astra 的定價是 10 美元／50 美元。據報導，Sol 在 DeepSWE v1.1 上比 GPT-6 Sol 高出 6.4 分，在 AutomationBench 上比 Opus 5.5 高出 2.2 分；OpenAI 內部員工將其定位為「好、便宜又快」。在 Agent Arena 排行榜上，Sol [Max] 以每任務中位成本 0.56 美元的表現擠進第 5 名（+11.23%），比 GPT-6 Sol 便宜 39% 但分數高出 1.52 分，比 Astra 便宜 81% 但分數只差 1.04 分。

與此同時，Anthropic 的 Sonnet 5.5 [Max] 以 +12.5% 的成績在 Agent Arena 排名第 3，並在 Chat 類別拿下第一，每任務成本為 2.74 美元，高於排名第 2、每任務 1.58 美元的 Opus 5.5，因此並未落在成本效能的 Pareto 前緣上。目前 Anthropic 的模型已包辦 Agent Arena 前三名。在 Code 與 Text 類競技場中，Sol 一度短暫進入 WebDev 第 3 名，後被 Sonnet 5.5 擠到第 4；Sonnet 在 WebDev 上落後 GPT-6 Astra [Max] 兩分，但成本低了 80%。另一方面，Gemini 4 Argon [High] 拿下 Text Arena 第一；開源模型中，MiMo-V2.6-Pro 與 Flash 則分別以第 5、第 9 名進入 Agent Arena。獨立評測 WeirdML v3 顯示 Sol 的 token 使用效率很高，接近 Astra 但峰值略低；同一基準下 Sonnet 5.5 勝過 Opus 5，Grok 4.7 勝過 Kimi-K3，不過這些結果尚不完整。另外，Design Arena 分析了 324 份模型思考摘要，發現 Astra 的「模稜兩可」（hedging）頻率約為 Opus 5.5 的 20 倍，而 Opus 有約五分之四的摘要會早早給出明確判斷。

📊 **決策模型與開源權重的動態**

StepFun 的 Step 5 Preview 在 Vals 開源權重模型排行榜上排名第 7，每任務成本 2.54 美元，平均每個任務耗時近兩小時，具備 1M token 的上下文窗口。另外有傳言稱 Claude Fable 5.5 將於下週發布，據稱表現優於一款因安全考量延後釋出的「Astra 6.1」，但發文者本人表示無法驗證這兩項說法；市場上也出現了「GPT-6 Astra Lite」的上架資訊，有評論推測這可能與 Sol 是同一款模型。

決策模型方面，llama.cpp 新增了 /v1/systemone 端點，用於本地執行「Jev 風格」的決策模型推論，可透過 llama serve -hf ggml-org/Kev-4B-GGUF 在本機啟動。Perplexity 宣稱其 pplx-decider-v1-27b 在 11 項基準測試上平均達到 85.7%，領先 Jev；Clef 的決策模型也已上架 Ollama。不過也有評論者認為，決策模型本質上只是零樣本分類器的重新包裝。另外，webAI 發布的 TwIL-LM3-Pro 是從 Granite 4.2 後訓練而來的 3.66B 模型，在該公司自己的測試中於形式邏輯任務上大致與 Qwen3-8B 相當，Q4 GGUF 版本大小為 2.09 GiB，採用非商業授權；Reka 則以 Apache 2.0 授權釋出了 RIDM，一款在遊戲資料上訓練、可泛化到真實影片、用於提取動作與鏡頭操作的逆向動力學模型。

💡 **代理程式訓練與長程控制的研究亮點**

Hugging Face 的一項多 harness 強化學習研究發現，同一組模型權重在不同 harness 下的表現可以從 33% 到 62% 不等；研究團隊透過一個能說 OpenAI、Anthropic、Gemini 三種 API 格式的代理層記錄採樣 token 與 logprob 進行訓練，不需改動 harness 本身，結果讓 LFM2.5-2.6B 在四個 harness 上的平均表現從 42% 提升到 54%，工具呼叫次數減少 31%；相較之下，在 3,189 筆 Qwen3.8-27B rollout 上做 SFT 的效果則停滯在 47.5%，相關訓練器、資料與全部七個訓練後模型皆已開源。另有研究提出 ProVer，讓一個判斷模型定位出決定勝負的關鍵軌跡片段，再用該片段前後的 rollout 來設定優勢值，相較 GRPO 分別在 Qwen3.5-2B 與 Qwen3.5-4B 上取得 9.91% 與 7.12% 的相對提升；AC2 則用一個學習型評論模型對 token 區塊打分，使訓練只需部分 rollout 即可進行。另一篇論文提出「Sharpening Tax」概念，量化後訓練（post-training）造成的 pass@K 可擴展性損失，並提出逐 prompt 調整溫度取樣的 PTGS 方法；還有研究發現 SFT 泛化較差的原因是資料本身是 off-policy，而非目標函式設計問題，把專家軌跡改寫成基礎模型自身的風格可以縮小這個差距。長程控制方面，Meta Superintelligence Labs 回報，在相同的 worker 與算力預算下，加入一個專門的控制器可以讓 GPT-5.5 在 ProgramBench 上的表現從 63.7% 提升到 71.5%，而 Codex 的對照成績則是 58.0%；微軟提出的免訓練上下文壓縮方法 FOCUS，則可將峰值上下文使用量降低最多 48%，同時任務成功率最多提升 8.9 分。

🎯 **實務啟示**

對正在評估模型選型的團隊，GPT-6.1 Sol 的定價策略說明了一件事：在能力差距縮小的階段，成本效能比（而非單純榜首分數）正成為決定選型的關鍵變數，值得把每任務成本一起放進評估指標。對做 agent 訓練的團隊，Hugging Face 的 harness 差異研究也值得警惕：同一組權重在不同工具呼叫框架下的表現落差可能高達近一倍，單一 harness 下的評測分數未必能反映模型在你自家系統中的真實表現。

🔗 **來源**
- 標題：[AINews] not much happened today
- 作者／機構：Latent Space
- 連結：https://www.latent.space/p/ainews-not-much-happened-today-cee

#LLM #AgentArena #GPT6 #Anthropic #OpenAI #ReinforcementLearning #AIAgents #ModelBenchmarking #OpenSourceAI #CostPerformance
