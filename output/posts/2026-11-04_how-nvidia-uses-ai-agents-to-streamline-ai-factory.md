---
title: How NVIDIA Uses AI Agents to Streamline AI Factory Operations
source: NVIDIA Developer
url: https://developer.nvidia.com/blog/how-nvidia-uses-ai-agents-to-streamline-ai-factory-operations/
model: claude-code/sonnet
generated_at: '2026-11-04T22:58:29.294125'
score: 79
---

📌 標題：NVIDIA 用一個 Chat 介面，把 GPU 叢集維運的多個 Dashboard 串起來

TL;DR：NVIDIA 用多代理架構打造內部維運工具，讓 SRE 不必輪流查看多個監控面板找根因。

GPU 叢集規模一旦擴大，運維範圍就橫跨運算、網路、硬體與排程四個層面。SRE 要抓到訓練效能下滑的原因，往往得在好幾個 dashboard 之間來回切換比對。NVIDIA 把這個流程交給一組彼此用 Model Context Protocol（MCP）溝通的 AI agent 來處理，這就是內部維運用的 AI Factory Operations Agent。

🤔 **問題：維運知識散落在不同系統裡**

NVIDIA 開發 AI Factory Operations Agent，目的是簡化內部 DGX SuperPOD 的維運流程，降低 SRE 的人工負擔。在正式環境中，這些 agent 負責偵測異常、跨層關聯根因，並透過 chat 介面給出明確建議，SRE 可以用自然語言切換不同調查任務，所有動作都會被記錄以供稽核。

🧩 **架構：NemoClaw blueprint 加上一群領域專用 agent**

整套系統以 NVIDIA NemoClaw blueprint 為核心，中間是面向使用者的 agent runtime，負責接收 SRE 查詢並呼叫對應的領域 agent 與工具。Agent 透過 OpenClaw 外掛與 MCP server 連接基礎設施，每個 MCP 只開放經過核准的一組操作工具，開發者可以直接用內建 Web UI，或透過 API 整合既有的 coding-agent 介面。整個框架建立在 NVIDIA OpenShell 上，可以完全在地端部署，支援資料主權需求。推理端使用地端部署的 NVIDIA Nemotron 開源模型，框架本身則跑在 NVIDIA DGX H100、DGX B200 與 DGX GB300 的正式叢集上。

系統以 Kubernetes control-plane 應用的形式運行，由 Helm 部署 UI、OpenClaw gateway、MCP 工具伺服器、推理端點與 OpenShell runtime。每次 SRE 在 chat UI 發出請求，都會先經過 NemoClaw 路由到對應的領域 agent。執行 shell 指令時，OpenShell 會為每個 session 建立獨立的 Kubernetes sandbox，而不是直接在主 gateway pod 裡跑指令，且不會更動既有服務或正式工作負載。

安全性則是分層把關：Kubernetes 層的檢查透過伺服端的 run_kubectl 工具執行，這個工具使用釘選版本的 kubectl 搭配已註冊的唯讀憑證，OpenShell 本身完全拿不到 kubectl 或 Kubernetes 憑證，agent 能看到、能動的資源範圍由 Kubernetes service account 與 RBAC 決定。素材中給出的實際權限檢查範例是：可以 get pods、可以 get configmaps，但不能 get secrets、不能 create pods、也不能 update pods。

內部部署目前已有六種領域 agent：負責偵測訓練失敗與 goodput 下滑、跨排程器／應用／硬體／網路層做根因分析的 Job Recovery Agent；負責定位 PCIe、ECC、GPU、NVMe 故障與異常發熱的 Hardware Agent；查詢歷史 Prometheus、telemetry 與 Grafana Loki 日誌並動態產生 dashboard 的 Observability Agent；搜尋 NVIDIA Mission Control 手冊與 DGX SuperPOD 參考架構文件（也可上傳自己的 runbook）的 Research Agent；提供 pod、服務、部署、GPU 資源、節點狀態等唯讀維運視角的 Kubernetes Agent；以及透過診斷用 MCP 工具呼叫 NVIDIA Base Command Manager API 的 Cluster Management Agent。框架之外還整合了網頁搜尋、程式碼執行、Grafana dashboard 等跨領域 MCP 工具，也能接上自己的 MCP server 與 API。

💡 **從實際運維中學到的五件事**

NVIDIA 持續用根因分析準確度與 SRE 的採信程度來檢驗這套框架，並歸納出五個心得：agent 的職責邊界要清楚，重疊的負責範圍只會製造噪音；先做到唯讀調查，用準確度建立 SRE 的信任後再談自動化；跨層關聯是關鍵，單一工具看不到的根因，要靠串連 workload、硬體與網路訊號才能找到；MCP 工具的定義要精確，才能提升路由準確度、減少選錯工具；以及 SRE 在採取行動前，必須能看到完整的工具呼叫、證據與推理過程。

⚠️ **目前仍是實驗性開源框架**

素材指出，這套協作框架目前以實驗性開源軟體形式提供，API、設定與部署需求可能隨版本更新而改變;NVIDIA 客戶可透過客戶經理申請存取 NVIDIA 自家開發的叢集維運 agent。

🎯 **實務啟示**

如果你的團隊也在管理大型 GPU 叢集，這個案例提供了一個可借鏡的落地順序：先把每個領域的 MCP 工具定義收斂清楚、權限限縮到唯讀，讓 agent 在正式環境裡先證明「診斷得準」，再逐步放開到可執行的維運動作；同時，把每一步工具呼叫與推理過程留痕，是讓運維團隊敢把 agent 放進生產環境的前提。

🔗 **來源**
- 標題：How NVIDIA Uses AI Agents to Streamline AI Factory Operations
- 作者／機構：Shara Tibken, NVIDIA Developer
- 連結：https://developer.nvidia.com/blog/how-nvidia-uses-ai-agents-to-streamline-ai-factory-operations/

#NVIDIA #AIAgents #MCP #GPUCluster #SRE #Kubernetes #AIOps #Nemotron #DataCenter #Observability
