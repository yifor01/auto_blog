---
title: 'Introducing harness adapters: adapt your favorite model to your harness to
  improve performance and cost'
source: HuggingFace Blog
url: https://huggingface.co/blog/harness-adapters-at-scale
model: claude-code/sonnet
generated_at: '2026-11-20T23:17:20.773783'
score: 103
---

📌 RL 訓練專屬 LoRA，讓模型更懂你的 Agent Harness

TL;DR：RL 訓練專屬 LoRA，讓模型在你的 agent harness 裡更準更省。

同一個模型放進不同的 agent harness 裡，表現往往有落差，因為模型本身只針對「泛用」能力最佳化，不是針對你實際在用的那個 harness 與任務分佈。HuggingFace 這篇文章給出一個具體數字：凍住 Qwen3.8-27B 的權重，只加一個用 RL 訓練出來的 LoRA adapter，pi harness 下的 Terminal-Bench 2.1 分數就從 39% 衝到 55% pass@1，平均 token 用量還從 2.9K 降到 1.5K。

🤔 模型是泛用的，但你的任務與 harness 是固定的

模型訓練時瞄準的是廣泛場景下的通用效能，但實際使用時，你往往固定用某一種 agent harness 去跑某一類任務，這個落差代表效能與效率都被留在桌上沒有被榨乾。HuggingFace 團隊先前的研究（multi-harness RL、harness adapters）已經證明，在自己的 harness 裡直接對自己的任務分佈做 RL，能同時換來更準確、更有效率的模型，但那些實驗只涵蓋資料分析與程式碼建構類任務。這篇文章要驗證的是：這個方法能否在 27B 這個規模、更貼近真實世界的軟體工程任務上，跨三種 harness（Pi、OpenCode、Hermes Agent）依然成立，並把整套方法包裝成可重現的食譜。

🧩 直接在 harness 裡面訓練，而非重寫一套 agent loop

多數 RL 框架會重新實作一套 agent loop，讓 agent 照著框架自己的介面寫（例如 verl 的 AgentLoop、SkyRL-Gym 的環境、rLLM 的 agent/environment 類別、slime 的自訂 rollout 函式，或 ART 讓 client 包進自己的 Python agent）。這篇文章的做法不同：讓 harness 完全照原樣執行，訓練器直接從 harness 實際產生的 token 學習，這些 token 由一個架在 harness 與 vLLM 之間的 proxy 記錄下來。團隊提到這個方向與近期工作一致：Agent Lightning v1.0 透過 proxy 把部署時的 harness 留在訓練迴圈裡（稱為「harnessed agentic RL」），SkyRL 的 Harbor 整合則是把 Harbor 的試驗轉成 token 餵給訓練器。

實作上，團隊利用 OpenEnv 中的 Harbor 整合與 TRL 的 OpenEnv 指南在 harness 裡訓練模型，並事先建好把目標 harness 安裝好的 Docker 映像檔，最終訓練用的版本是 Pi 1.5.2、OpenCode 2.2.7 與 Hermes Agent v0.22.6。資料集、訓練與 agent 的 rollout 全部跑在 Hugging Face Hub 的 Jobs 上，使用 TRL 的 AsyncGRPOTrainer。

🧩 三個任務來源，加一層嚴格驗證

RL 訓練需要三件事：agent 可以嘗試的任務、能替每次嘗試打分的驗證器，以及證明這個驗證器真的可信的證據。驗證器若會接受錯誤答案，就會教出錯誤行為；任務若太簡單、模型早就會解，也學不到東西。團隊用三個來源建立任務集：SWE-smith（Python、Go）對真實專案注入 bug，方式是用 LLM 改寫或做出像翻轉運算子這類突變，抓到 bug 的測試就成為任務的測試，主要用來增加任務量；SWE-Gym（以 TaskTrove 包成 Harbor 任務）把真實的 GitHub issue 與對應的合併修復轉成任務，帶來真實世界的 bug；Tasksmith（Repo2RLEnv 中的一套管線）從已合併的 pull request 產生任務，讓 LLM agent 自己寫出任務指令與測試，再透過檢查把關：參考解與另一個有效解法必須通過，未修復的程式碼與一個已知錯誤的解法必須失敗。團隊用 Tasksmith 針對性地補強 Terminal-Bench 2.1、SWE-bench Pro 困難子集、DeepSWE 所測試的技能缺口，挑選像 HTTP streaming、檔案系統操作、序列化這類相關的 PR。從 30 個已合併的 PR，Tasksmith 在 10 個 Python 專案中產出 24 個通過檢查的任務，其中 17 個在第二次執行時依然通過。

所有任務還要再過一層 openenv validate 的篩選：先做 metadata 篩選（保留訓練用、授權寬鬆的任務，排除重複項、標記為不可訓練的任務、目標 benchmark 用到的 253 個任務，以及這些 benchmark 用到的任何專案中的任務），再跑語意檢查——參考解拿到最高獎勵（semantic.oracle_max）、什麼都不做的分數明顯較低（semantic.floor_gap）、沒有 canary 解法的分數會高於什麼都不做（semantic.canary_floor）、重播參考解會得到相同獎勵（runtime.episode_determinism）。每個試驗都跑成獨立的 Hugging Face Job，一次可以驗證幾十個任務，最終 1,127 個候選任務中有 858 個通過。這層驗證確實抓到了問題：包括一個接受不完整實作的 Tasksmith 任務，以及一個會把已知錯誤答案判為通過的 Terminal-Bench 2.1 驗證器（regex-log）。沒通過的任務會留在一個 rejected 分支裡，並記錄下是哪一項檢查失敗。

🎯 實務啟示

這套方法給出一個很具體的訊號：如果你已經固定用某個 agent harness 反覆跑同一類任務，花力氣針對那個組合做 RL、訓練一個 LoRA adapter，可能比換更大的底座模型更划算，效能提升之外，token 用量下降代表推理成本也會直接降低。文章也提到三個 harness 各自的 LoRA 最終被合併成一個「super adapter」，能在 pi、Hermes Agent、OpenCode 三種 harness 下不經修改直接使用，所有 adapter、GGUF、RL 任務與 safeagents plugin 都已整理成 Hugging Face collection，對想重現這套流程的團隊是現成的起點。

🔗 來源
- 標題：Introducing harness adapters: adapt your favorite model to your harness to improve performance and cost
- 作者／機構：HuggingFace（Younes B、ben burtenshaw、Nathan Habib、Lysandre、Amine Dirhoussi 等）
- 連結：https://huggingface.co/blog/harness-adapters-at-scale

#ReinforcementLearning #LoRA #AgentHarness #LLM #HuggingFace #TRL #OpenEnv #AgenticAI #SoftwareEngineering #FineTuning
