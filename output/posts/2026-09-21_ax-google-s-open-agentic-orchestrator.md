---
title: AX – Google’s Open Agentic Orchestrator
source: Hacker News
url: https://agentexecutor.io
model: claude-code/sonnet
generated_at: '2026-09-21T21:14:19.263625'
score: 114
---

📌 AX：Google 開源的 Agent 專用執行環境

TL;DR：Google 團隊開源 AX，用宣告式 YAML 管理數十億規模的 agent 任務，如同 Kubernetes 之於容器。

Agent 已經不是新鮮事，但要讓成千上萬個 agent 同時運作、隨時暫停恢復、又不浪費運算資源，這件事至今沒有標準答案。Google 這次直接把答案做成一個開源專案，並在 Hacker News 拿下 626 個讚、285 則討論。

🤔 為什麼現有工具不夠用

Agent 不是 microservice，也不是 batch job：它們會累積狀態、需要嚴格隔離、要呼叫 model API 與工具伺服器，一旦沒人看著還可能在迴圈裡燒錢。傳統為無狀態服務或可預期批次工作設計的編排器，若要讓 sandbox 長時間閒置待命就會成本過高，卻又原生不支援秒級的 suspend/resume。

🧩 四個宣告式元件

- Task：隔離執行單元，跑在有 CPU 與記憶體限制的 sandbox 裡，建立、暫停、丟棄的成本都很低。
- Workspace：列出 agent 需要的 Git repo、MCP 伺服器與 skills，或直接用自然語言描述目標，AX 會在每個 sandbox 啟動前自動準備好環境。
- Gateway：網路政策管理，把流量鎖在明確的 host/port allowlist，並可為外送請求注入憑證。
- Model：把模型設定、參數與 secrets 集中管理，一次 apply 就能輪替金鑰或釘選新版本。

實際操作上，`ax apply -f task.yaml` 建立 workspace 與 task 後，可用 `ax watch`、`ax ssh`、`ax suspend`、`ax resume`、`ax delete` 等指令觀察與操控任務生命週期，體驗上很接近 kubectl。

📊 規模與效能設計

AX 建立在 Agent Substrate 這個運算執行環境之上，官方宣稱可讓每個 cluster 撐起數十億個並行的 agent session：每個任務是輕量 actor；閒置中等待模型回應、工具呼叫或人工回覆的 agent 會被 checkpoint、暫停，並在一秒內零冷啟動恢復；多個任務共享 worker 資源，把等待時間轉換成可用運算容量，只在 agent 真正思考與執行程式碼時才付費。

💡 生成式功能內建在平臺裡

Workspace 設定也可以完全用自然語言描述，例如「set up a Python 3 development environment」，AX 會在任務首次啟動時把這個目標交給 agent，自動安裝工具鏈並驗證相依套件，不需要手寫詳細設定檔。

⚠️ 定位與限制

官方將 AX 定位為研究與生產兩用：適合互動式 coding agent、長時間執行的 agent server、Jupyter notebook、headless 瀏覽器測試，以及蒐集強化學習訓練軌跡、大規模評測 agent 等場景。不過素材中並未提供效能實測數據或與其他編排系統的直接比較，這些仍待社群實際部署後驗證。

🎯 實務啟示

如果團隊已經在為 agent fleet 手刻排程、隔離與網路政策，AX 提供了一套現成的宣告式抽象，YAML 定義 workspace/task 的模式對熟悉 Kubernetes 的工程師幾乎零學習成本。專案已開源在 GitHub，值得先在小規模場景試跑，觀察 suspend/resume 的實際延遲與 sandbox 隔離是否符合自己的安全需求，再考慮是否用來取代自建的 agent 排程系統。

🔗 來源
- 標題：AX – Google's Open Agentic Orchestrator
- 作者／機構：blazarquasar（Hacker News 分享），Google
- 連結：https://agentexecutor.io

#AX #GoogleResearch #AgenticAI #AIAgents #Kubernetes #Orchestration #OpenSource #DeepMind #CloudInfrastructure #LLMOps
