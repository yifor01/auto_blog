---
title: 'Agent Lightning v1.0: A 3,500-Line Lightweight Agentic RL Framework for Training
  Agents with Real Harnesses'
source: Microsoft Research
url: https://www.microsoft.com/en-us/research/blog/agent-lightning-v1-0-a-3500-line-lightweight-agentic-rl-framework-for-training-agents-with-real-harnesses/
model: claude-code/sonnet
generated_at: '2026-10-07T22:14:29.853379'
score: 132
---

📌 Agent Lightning v1.0：3500 行程式碼,讓真實 Agent Harness 直接參與強化學習

TL;charge：Microsoft 開源輕量 RL 框架,訓練時不用重寫 Agent,SWE-bench Verified 直接拉高 14.6 個百分點。

訓練一個 coding agent 做強化學習,過去的代價是:你得先把它在訓練框架裡重寫一遍。重寫完的那個 agent,跟你實際部署的那個,往往已經不是同一個東西了。Microsoft Research Asia 這次直接把這個假設打掉重練。

🤔 **問題出在「訓練框架擁有互動迴圈」這個假設**

傳統 agentic RL 假設訓練框架自己掌控與環境互動的迴圈:模型產生 action,環境回傳 observation,接到 context 裡,再產生下一個 action,整個 rollout 對應到一條連續的 token 軌跡。verl、AReaL、slime 這些早期系統都是這樣設計的,代價是:想訓練一個 agent,就得把它的迴圈在 RL 框架裡重建一次。

但現實中的 harness 早就不是這麼簡單了。mini-SWE-agent、OpenHands、OpenCode、Claude Code、Codex,每一個都有自己的 context 管理、工具協定、執行邏輯與依賴套件。重建一次成本很高,重建完的 agent 行為也未必跟部署版一致。

🧩 **把 LLM Proxy 塞進 Agent 和模型之間**

Agent Lightning 的做法是在 agent 與模型之間插一層 LLM proxy。Agent 的執行方式不變,只要把原本呼叫模型 API 的 endpoint 指向 Agent Lightning,訓練框架就能觀察並記錄每一次模型呼叫。v1.0 把這個做法正式定義為 Harnessed Agentic RL:部署時用的那個 harness,直接參與訓練時的強化學習。

這樣一來,訓練系統只能看到一連串 LLM 的 request/response pair,一次 rollout 可能被拆成數量不固定的訓練樣本,這帶來了幾個系統設計上的挑戰。

整個框架約 3,500 行程式碼,核心是三個元件:
- **API Gateway**:存放 rollout、模型與事件資訊,同時是一個 OpenAI 相容的 LLM proxy,把每次模型呼叫對應回所屬 rollout,並記錄訓練需要的 prompt、response 與 log probability。
- **Rollout Controller**:負責啟動與管理 agent 執行,可以是本地行程,也可以是標準 Kubernetes job,讓 agent 執行與 trainer 分離。
- **Customized Trainer**:基於 verl 建構,建立 rollout、等待完成、收集樣本,再透過 sample adapter 組出最終訓練樣本。

對既有的 agent harness 而言,通常只要把模型 endpoint 指向 Agent Lightning proxy,就能快速接上 RL 訓練。

📊 **Collocated Async RL:少用 GPU,還快了近兩倍**

不同 agent 的 rollout 時間差異很大。同步 RL 要等批次裡最慢的 agent,GPU 閒置;全非同步 RL 利用率高,但需要為 rollout 與訓練分別配置 GPU 池。Agent Lightning v1.0 提出 Collocated Async RL,讓 rollout 與模型更新共用同一組 GPU:收集到足夠 rollout 後,API Gateway 暫停接受新請求,等進行中的請求完成,更新結束後 rollout 再恢復,整個狀態轉換對外部 agent harness 是透明的。實驗中,這個做法比同步 RL 達到約 2 倍的端到端加速,同時用的 GPU 比傳統非同步 RL 更少。

此外,為了不依賴 Modal Sandbox、E2B 等商業沙盒服務(成本隨規模快速攀升),Agent Lightning v1.0 把大量平行執行的 agent 跑成標準 Kubernetes job,重用既有的自管叢集、雲端 Kubernetes 或本機基礎設施,讓整條 pipeline 保持開源可復現。

研究團隊基於 SWE-smith、mini-SWE-agent 與 Qwen3.5-9B,建了一套完整 pipeline,涵蓋資料清理、環境構建、reward-hacking 防護與 RL 訓練,訓練集約 6,000 筆樣本,不需要大規模運算。純 RL 訓練就讓 Qwen3.5-9B 在 SWE-bench Verified 上從 41.8% 提升到 56.4%,漲了 14.6 個百分點。

💡 **Rollout 層級的 advantage 計算更穩定**

實驗也驗證了之前提到的兩個挑戰:advantage 計算與 loss normalization。相較於樣本層級的處理方式,採用 rollout 層級的 advantage 搭配 rollout 層級的 normalization,能取得更高的驗證 reward,訓練過程中的 policy entropy 也更穩定。

🎯 **對工程師的意義**

如果你手上已經有一套在生產環境運作的 agent harness,Harnessed Agentic RL 的價值在於:不需要為了做 RL 另外維護一套「訓練專用版 agent」。只要把模型呼叫導到 proxy,就能讓部署版本直接參與訓練迴圈,降低了訓練與部署行為不一致的風險。

🔗 **來源**
- 標題:Agent Lightning v1.0: A 3,500-Line Lightweight Agentic RL Framework for Training Agents with Real Harnesses
- 作者／機構:Microsoft — Zhiyuan He, Yuqing Yang
- 連結:https://www.microsoft.com/en-us/research/blog/agent-lightning-v1-0-a-3500-line-lightweight-agentic-rl-framework-for-training-agents-with-real-harnesses/

#AgenticRL #ReinforcementLearning #Microsoft #LLM #CodingAgent #SWEBench #OpenSource #MachineLearning #Kubernetes #AgentHarness
