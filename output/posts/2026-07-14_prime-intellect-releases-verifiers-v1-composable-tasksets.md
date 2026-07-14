---
title: 'Prime Intellect Releases Verifiers v1: Composable Tasksets, Harnesses, and
  Runtimes for Agentic RL Training and Evaluations'
source: MarkTechPost
url: https://www.marktechpost.com/2026/07/13/prime-intellect-releases-verifiers-v1/
score: 105
model: tencent/hy3:free
generated_at: '2026-07-14T07:47:07.283759'
---

📌 【Prime Intellect】Verifiers v1：解耦任務、Harness 與 Runtime

TL;DR：Verifiers v1 把 agentic RL 環境拆成可組合元件，助大規模訓練評估。

過去一個環境把資料、代理邏輯與基礎設施綁在一起，當現代評估需要讓 coding agent 使用工具、壓縮上下文與子代理時，這種繫結顯得笨重。Prime Intellect 現在把這團繫結拆開了。

🤔 **verifiers 是什麼，為何需要 v1 重寫**

Prime Intellect 推出 verifiers 0.2.0，預覽重寫核心並以新 verifiers.v1 名稱空間釋出。它原本是該機構的 environment stack for agentic reinforcement learning and evaluations。先前環境將 data、agent logic、infrastructure 打包成一體；而現代評估會跑具備 tools、compaction、subagents 的 coding agents，因此 v1 重建環境來規模化執行這類 agentic workloads。

🧩 **環境拆分為 taskset、harness、runtime 三塊**

v1 將原本繫結的環境拆成三個可組合部分。taskset 定義工作內容：包含資料、工具與評分。harness 負責解題並產生 rollout，可以是 ReAct loop、CLI agent 或使用者自訂邏輯。rollout 接著在 runtime（local 或 sandbox）中執行。因為元件解耦，任何 taskset 都能跑在任何相容的 harness 之下。

🧩 **中央 interception server 統管通訊與防作弊**

架構核心是 verifiers 管理的 interception server，它位於 agent 的 runtime 與 inference server 之間。具體而言，它代理往返 inference 的請求與回應，同時記錄 trace、設定取樣引數，並能重寫工具回應來減緩 reward hacks。規模化方面，每個 server 多工固定數量的 rollouts（預設 32），pool 則依觀察到的併發量彈性擴縮。評估時 EvalClient 充當盲 HTTP proxy；訓練時 TrainClient 包裝 renderers 以提供忠實的 token-in RL 訓練。

🧩 **三種方言適配讓評分邏輯獨立於代理**

由於 harness 說不同的 dialects，v1 目前支援 OpenAI Chat Completions、OpenAI Responses 與 Anthropic Messages。dialect adapter 將各種線路格式標準化為 canonical vf.types，因此你的 scoring logic 能保持獨立於受測代理之外。

🎯 **實務啟示**

對從事 agentic RL 的工程師，這套解耦設計意味換代理或改評分邏輯時不必重寫整個環境堆疊；中央攔截與工具回應重寫提供內建防 reward hack 機制，適合大規模訓練佈建。評估與訓練客戶端分離，也讓同一套元件兼顧兩種場景，降低維運複雜度。

🔗 **來源**
- 標題：Prime Intellect Releases Verifiers v1: Composable Tasksets, Harnesses, and Runtimes for Agentic RL Training and Evaluations
- 作者／機構：Michal Sutter
- 連結：https://www.marktechpost.com/2026/07/13/prime-intellect-releases-verifiers-v1/

#Verifiers #PrimeIntellect #AgenticRL #ReinforcementLearning #Tasksets #Harness #Runtime #LLM #EvalClient #TrainClient
