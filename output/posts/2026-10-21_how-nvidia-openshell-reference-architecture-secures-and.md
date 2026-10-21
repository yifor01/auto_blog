---
title: How NVIDIA OpenShell Reference Architecture Secures and Governs AI Agent Workloads
  at Scale
source: NVIDIA Developer
url: https://developer.nvidia.com/blog/how-nvidia-openshell-reference-architecture-secures-and-governs-ai-agent-workloads-at-scale/
model: claude-code/sonnet
generated_at: '2026-10-21T20:53:55.518429'
score: 103
---

📌 NVIDIA OpenShell 參考架構：agent 管不住自己，治理必須寫進基礎設施

TL;DR：開源執行時 OpenShell 把 agent 的安全邊界建在運算基礎設施裡，agent 本身無法逾越這道邊界。

自主 agent 能連續工作數小時，存取檔案、呼叫工具、連上網路，甚至衍生出其他 agent 協作完成任務。問題是，agent 是目標導向的，執行越久、碰觸的系統越多，風險就越會疊加,而且它不會自己優先考慮安全。

🤔 **Agent 越自主，風險越會隨時間疊加**

Agent 的行動路徑是邊做邊決定的：它在推理與執行步驟的過程中，可能下載程式碼、建立新工具、要求更多權限，接觸到底層基礎設施更深的地方。這種「邊走邊決定」的彈性正是 agent 強大的原因,但也意味著它不會自我設限。NVIDIA 團隊的立場很明確：agent 無法治理自己,安全與治理必須屬於它所運行的基礎設施，而不是寄望於 agent 本身。

🧩 **四個元件，把治理放在 agent 碰不到的地方**

OpenShell 把所有 agent 工作負載都視為不可信,只在需要的時候才給予需要的存取權限。它由四個核心元件組成：Gateway 是控制平面，管理 sandbox 的生命週期與政策；Supervisor 負責檢查對外請求是否符合政策，並中介憑證存取，它完全獨立於 sandbox 之外運行；Sandbox 隔離 agent 的執行環境，限制檔案系統與程序存取；Policy prover 加入形式化驗證，確認政策授予的權限沒有超出組織設定的上限。這套設計也支援擴充：Supervisor middleware 可以檢查、封鎖或修改 agent 透過網路傳送與接收的內容；Gateway interceptor 則讓維運團隊在不修改 Gateway 本身的前提下，加入部署特定的治理邏輯。

🧩 **底層跑在 NVIDIA Vera CPU 上：OpenShell 定義能做什麼，Vera 決定能多快**

在這套參考架構中，OpenShell 運行於 NVIDIA Vera CPU 之上。NVIDIA 把這種針對 agent 工作負載最佳化的設計稱為「max single-threaded CPU at scale」：88 顆 NVIDIA 自行設計的 Olympus 核心，搭配 10-wide 前端、神經分支預測器與深度亂序執行，在關鍵 agentic 工作負載上比 x86 快上 2 倍；第二代 Scalable Coherency Fabric 提供最高 3 倍的 core-to-core 頻寬，延遲比 x86 方案低 50%；整合 96 條 PCIe Gen 6 通道，供給 GPU、高速儲存與網路所需的 I/O 頻寬；最高 1.2 TB/s 的 LPDDR5X 記憶體頻寬，載入延遲比 chiplet 架構低 40%。LPDDR5X 同時帶來效能功耗比的提升：Vera 的每瓦效能是 x86 的 2 倍，記憶體子系統耗電量比同級 DDR5 方案低一個數量級。

📊 **CoreWeave 實測：sandbox 啟動快 3 倍以上，單機架可容納逾 11,000 個併發 agent 環境**

根據 CoreWeave 公開的實測數據，Vera 上的 sandbox 啟動速度比 x86 快超過 3 倍，單一機架可支援超過 11,000 個併發 agent 環境；在模擬真實 agentic 迴圈任務的 Terminal Bench 測試中（涵蓋從腳本編寫到資料庫復原等 20 項真實任務），Vera 的表現比 x86 快 1.8 倍。

🧩 **BlueField-4 與 NVIDIA Sentry：把政策執行下沉到硬體層**

對需要更高防護等級的部署，OpenShell 的邊界可以延伸到專用晶片。NVIDIA BlueField-4 DPU 在 I/O 路徑中建立一個 agent 碰不到的硬體隔離信任域，位於跑在 Vera 上的 agent 與它們所存取的模型之間。建構在 NVIDIA DOCA 之上的安全框架 NVIDIA Sentry 就運行在這個獨立域中，持續監控請求與回應、網路與檔案活動，驗證身分與被授權的權限，並分析選定的主機記憶體以偵測異常行為,整個過程不依賴 agent 自我回報。一旦偵測到威脅或違反政策，BlueField-4 會在硬體層強制執行政策，讓 Sentry 能在毫秒級的時間內隔離該 agent。

🎯 **實務啟示**

對於正在生產環境大規模運行 agent 的團隊，這篇文章給出的核心訊號是：不要指望用 prompt 或 agent 自律來做安全治理，應該把授權邊界建在 agent 無法觸及的基礎設施層。即便不採用 NVIDIA 的完整堆疊，Gateway、Supervisor、Sandbox、Policy prover 這四個職責的拆分，也是設計自家 agent 控制平面時值得參考的架構分工。

⚠️ 文中效能數據（Vera 對比 x86 的各項倍數、CoreWeave 的 sandbox 與 Terminal Bench 結果）均為 NVIDIA 與 CoreWeave 自行公布的測試結果，實際表現仍需在自身工作負載上驗證。

🔗 **來源**
- 標題：How NVIDIA OpenShell Reference Architecture Secures and Governs AI Agent Workloads at Scale
- 作者／機構：Elizabeth Goodman，NVIDIA Developer
- 連結：https://developer.nvidia.com/blog/how-nvidia-openshell-reference-architecture-secures-and-governs-ai-agent-workloads-at-scale/

#AIAgents #AISecurity #NVIDIA #Infrastructure #Governance #Sandboxing #Cybersecurity #AgenticAI #DataCenter #ZeroTrust
