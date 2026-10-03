---
title: 'Prime Intellect Launches Prime Inference: Serverless and Reserved Serving
  for Frontier Open Models'
source: MarkTechPost
url: https://www.marktechpost.com/2026/10/02/prime-intellect-launches-prime-inference-serverless-and-reserved-serving-for-frontier-open-models/
model: claude-code/sonnet
generated_at: '2026-10-03T19:54:48.780040'
score: 96
---

📌 Prime Intellect 推出 Prime Inference，服務量先跑贏研發流程

TL;DR：Prime Intellect 把自家訓練用的推理基礎設施開放成服務,主打 agentic 工作負載的低延遲。

一個推理服務在正式對外開放之前,內部流量就已經達到每天近一兆 token,這不是行銷數字,而是 Prime Intellect 自己在強化學習 rollout、合成資料生成與長時間執行的程式設計 agent 上,日常就在消耗的流量規模。

🤔 **訓練與服務閉環**

Prime Intellect 推出 Prime Inference,是一個針對前沿開源模型的服務平臺,提供 serverless 端點與保留容量(reserved capacity)兩種模式,運行在 Prime 自家跨多個資料中心的 GPU 上。這是 Prime Intellect 開放訓練技術堆疊中的服務層,公司原本就提供 prime-rl、verifiers、sandboxes 等後訓練(post-training)工具,而服務層的補上,讓部署中的模型產生的生產環境軌跡(production traces)能回流到訓練流程中,形成閉環。Prime 表示其 GLM-5.3 端點在 OpenRouter 上名列最快之一,工具呼叫錯誤率接近零,上線以來維持 100% 正常運行時間。

🧩 **Prefill/decode 分離與快取感知路由**

整套技術堆疊結合了 NVIDIA Dynamo、vLLM、Mooncake 與 FlashInfer,由 Prime Intellect 與 Inferact、NVIDIA 共同打造,相關修復也回饋到上游專案。目標工作負載是 agentic 場景:一次典型的 agent 回合,會在一個 140K token 的 prompt 上再疊加約 6K token,團隊用 SemiAnalysis 的 AgentX 搭配注入的冷啟動(cold arrivals)請求來做基準測試。

架構上的第一個關鍵設計是 prefill/decode 分離:prefill 與 decode 分別在不同的 GPU 群組上執行,由 Dynamo 負責路由,vLLM 在每個群組上運行模型,decoder 透過 NIXL 拉取已算好的 KV。Prime 表示這讓 p90 的 inter-token latency 降低了近 40%。第二個設計是快取感知路由(cache-aware routing):Dynamo 的 KV-aware router 會權衡快取 prefix 重疊程度與目前排隊中的工作量,讓同一個 session 在多輪對話間盡量留在同一個 decoder 上,Mooncake 則在 host DRAM 上加了第二層 KV 快取。

📊 **每位使用者 100 token/秒的目標**

團隊設定的互動性目標是每位使用者每秒 100 個端到端 token。在這個標準下,1:4 的 prefill/decode 比例服務的使用者數量最多,每個 prefill 群組可以撐住 66 個 session,同時維持每位使用者 101 token/秒、每張 GPU 輸出 100 token/秒的水準。

💡 **工具呼叫正確性也是重點**

agent 最容易在工具呼叫的名稱或參數出錯時失敗。Prime Intellect 團隊為此替 Dynamo 貢獻了一個結構化標籤建構器(structural-tag builder),專門處理 GLM 的工具格式;vLLM 則使用 xgrammar,遮罩掉違反工具 schema 的 token。團隊同時修復了解析上的錯誤,包括程式碼區塊中的 `<` 被誤解碼的問題。

🎯 **對工程師的意義**

如果你的系統正好是長 prompt、多輪工具呼叫的 agentic 工作負載,Prime Inference 展示的 prefill/decode 分離與快取感知路由,是值得參考的服務架構設計思路,不論是否直接採用這個平臺,這套設計邏輯本身對自建推理服務也有借鏡價值。

🔗 **來源**
- 標題：Prime Intellect Launches Prime Inference: Serverless and Reserved Serving for Frontier Open Models
- 作者／機構：Michal Sutter, MarkTechPost
- 連結：https://www.marktechpost.com/2026/10/02/prime-intellect-launches-prime-inference-serverless-and-reserved-serving-for-frontier-open-models/

#PrimeIntellect #LLMInference #vLLM #NVIDIADynamo #AgenticAI #MLOps #OpenModels #GPUComputing #KVCache #AIInfrastructure
