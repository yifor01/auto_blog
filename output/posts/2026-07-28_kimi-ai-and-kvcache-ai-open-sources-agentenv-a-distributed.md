---
title: 'Kimi AI and kvcache-ai Open Sources ‘AgentENV’: A Distributed System that
  Powers Agentic Reinforcement Learning (RL) Training for Kimi K3'
source: MarkTechPost
url: https://www.marktechpost.com/2026/07/27/kimi-ai-and-kvcache-ai-open-sources-agentenv/
model: tencent/hy3:free
generated_at: '2026-07-28T08:25:07.697280'
score: 110
---

📌 【開源專案】AgentENV 解決 Agentic RL 訓練中，隔離性與啟動速度的兩難困境

TL;DR：AgentENV 利用 Firecracker microVM 提供可擴展的沙盒環境，支援 Kimi K3 的 Agentic RL 訓練。

當 LLM 從單純的文本生成轉向「Agentic Reinforcement Learning (RL)」時，模型不再只是預測下一個字，而是必須在真實的電腦環境中進行操作。這意味著每一次的 Rollout（模型試行）都需要一個具備檔案系統、網路堆疊與即時進程的隔離 Linux 環境。

🤔 **容器與虛擬機之間的效能與隔離權衡**

在開發 Agent 訓練環境時，工程師面臨著難以兼得的選擇：
- **容器 (Containers)**：啟動速度極快，但共用主機核心 (Host Kernel)，對於模型產出的程式碼而言，隔離性不足，存在安全風險。
- **完全虛擬機 (Full VMs)**：隔離性極佳，但啟動速度慢，且在閒置時會佔用大量記憶體。

🧩 **AgentENV 的架構設計：以 Firecracker microVM 為核心**

AgentENV (AENV) 透過整合 Firecracker microVM，精準填補了上述兩者的空白，讓大規模的沙盒運行變得可行：

- **沙盒機制**：每個沙盒都是一個擁有獨立 Linux 核心、檔案系統與網路命名空間 (Network Namespace) 的 Firecracker microVM。
- **請求流程**：請求透過 Axum HTTP API 進入，由編排器 (Orchestrator) 管理沙盒的生命週期。
- **高效儲存設計**：使用 ublk 使用者空間區塊裝置 (Userspace block device)，並透過 overlaybd 建立層疊映像檔。唯讀的基礎層 (Base layers) 可在不同沙盒間共享，而每個沙盒的寫入操作則紀錄在各自的層級中。
- **環境管理**：每個 Guest 內部運行一個名為 `envd` 的守護進程 (Daemon)，負責處理指令執行、檔案操作與健康狀態回報 (Port 49983)，並透過反向代理 (Reverse Proxy) 路由 HTTP 與 WebSocket 流量。

💡 **提升密度與擴展性的兩大機制**

為了支撐 Kimi K3（一個擁有 2.8 兆參數的 MoE 模型）的大規模訓練，AgentENV 引入了兩項關鍵技術：
1. **共享快取**：主機的 Page Cache 會同時被儲存與記憶體快照 (Memory-snapshot) 資料共用。
2. **記憶體氣球技術 (Memory Ballooning)**：將可回收的 Guest 記憶體歸還給主機，以支持隨時間演進的環境過度配置 (Overcommit)。

此外，AgentENV 採用增量方式對記憶體與檔案系統進行快照，而非每次都寫入完整的映像檔，大幅提升了效率。

🎯 **實務啟示**

對於需要進行 Agentic RL 或需要安全執行模型生成程式碼的系統，AgentENV 提供了一套成熟的解決方案，證明瞭透過微型虛擬機 (microVM) 與層疊檔案系統，可以在維持強隔離性的同時，達到足以支撐大規模訓練的擴展性。

🔗 **來源**
- 標題：Kimi AI and kvcache-ai Open Sources ‘AgentENV’: A Distributed System that Powers Agentic Reinforcement Learning (RL) Training for Kimi K3
- 作者／機構：Asif Razzaq @ MarkTechPost
- 連結：https://www.marktechpost.com/2026/07/27/kimi-ai-and-kvcache-ai-open-sources-agentenv/

#AI #AgenticRL #OpenSource #MicroVM #Firecracker #MoonshotAI #DistributedSystems #MachineLearning #ReinforcementLearning #SoftwareEngineering
