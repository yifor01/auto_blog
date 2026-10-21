---
title: 'Inside NVIDIA Sentry: Secure AI Agents at Runtime'
source: NVIDIA Developer
url: https://developer.nvidia.com/blog/inside-nvidia-sentry-secure-ai-agents-at-runtime/
model: claude-code/sonnet
generated_at: '2026-10-21T20:56:51.986779'
score: 98
---

📌 【NVIDIA】在 DPU 上築一道 Agent 碰不到的安全牆

TL;DR：NVIDIA Sentry 把 AI agent 的監控與政策執行搬到 BlueField-4 DPU 上，確保就算 agent 或主機被攻破也管得住它。

AI agent 完成任務的同時，也可能悄悄跨越了安全邊界——使用工具、憑證與服務去達成目標的過程中，agent 其實有能力繞過本該限制它的安全控制。如果監控機制跑在 agent 可以碰到的地方，agent 理論上就能改掉或關掉它。NVIDIA Sentry 想解決的正是這個問題。

🤔 **監控者不能活在被監控者的勢力範圍內**

NVIDIA Sentry 是一套安全軟體框架，負責監控 AI agent 並執行其存取模型、工具與資料的政策，是 GTC Berlin 上發布的 NVIDIA OpenShell 參考架構的一部分。它建構在 NVIDIA DOCA 之上，運行於 NVIDIA BlueField-4 DPU，提供與主機隔離的 runtime 保護。早先的一篇文章曾介紹 BlueField 如何在獨立於主機的硬體信任域中運行安全服務，Sentry 正是建立在這個基礎上，持續監控 agent 行為並獨立於主機軟體執行存取政策。

軟體層的 runtime 邊界依然重要：NVIDIA OpenShell 是自主 agent 的安全 runtime，決定 agent 能做什麼，並把政策執行與 agent 工作負載分離，使被攻破的 agent 無法更改自己的限制。Sentry 則在此之外，額外加上一層運行在 BlueField-4 上、處於 agent 認知與觸及範圍之外的獨立硬體防護。在 OpenShell 架構中，agent 執行於 NVIDIA Vera CPU，而 BlueField-4 則坐在節點通往模型的唯一路徑上——Sentry 藉此檢查 agent 與模型之間的通訊、執行存取政策，而不需要依賴 agent 自己回報行為。

🧩 **三個元件各司其職：Tower、Flow、Argus**

Sentry 的設計拆成網路層與行為層兩條線：

- **DOCA Tower**：Sentry 的 AI 安全閘道，建構在開源 Envoy proxy 之上，作為 agent 流量的透明雙向檢查層。Agent 的網路流量透過繞過主機 OS／hypervisor 封包處理的直接 I/O 路徑抵達 BlueField-4。
- **DOCA Flow**：在 BlueField-4 上以矽晶片加速、為每個 agent 建立 layer-4 防火牆，阻擋未授權目的地的連線，並將允許的流量轉交給 DOCA Tower 做 layer-7（應用層）檢查、授權與其他安全檢查。DOCA Tower 以內建的矽晶片層 TLS 加速進行 TLS 終止，對獲準檢查的連線解密，以檢查與控制 agent 的通訊內容。
- **DOCA Argus**：提供 agent 執行環境與運作狀態的即時可視性，透過對主機 volatile memory 特定區域的即時記憶體內省（memory introspection），取得系統運作狀態的獨立證據。Argus 完全獨立於主機運行，不需要在主機上安裝任何常駐 agent，屬於 agentless 設計，既保留主機運算資源，也因為運行在獨立信任域中，即使主機遭入侵也不受影響。Argus 能即時對映執行環境（例如 container 對應到 pod、sandbox 對應到 microVM），識別正在執行的處理程序及其屬性，並對映處理程序／執行緒、檔案存取、網路連線、已載入函式庫，以及 CPU、GPU、記憶體等系統資源之間的關係，並以 hash 追蹤 container、處理程序與已載入函式庫。

📊 **政策評估：OPA 在一毫秒內做決策**

Sentry 使用開源政策引擎 Open Policy Agent（OPA）評估存取請求，政策以宣告式語言 Rego 撰寫，用於評估複雜的階層式資料結構。OPA 在記憶體中本機運行，依政策複雜度與設定，可在一毫秒以內完成評估。DOCA Tower 與 OpenShell 的政策相容，透過 OPA 將網路存取政策與 runtime 控制延伸到 BlueField-4 及底層基礎設施。

💡 **把網路請求與執行環境的脈絡拼在一起**

Sentry 最關鍵的設計，是把 DOCA Tower 提供的網路連線資訊，與 DOCA Argus 提供的 runtime 脈絡做關聯比對來評估存取請求，而不只是看單一的資源存取政策。舉例來說，一條網路存取政策可以要求：發起連線的 container 的 hash 必須符合核准清單；發起連線的處理程序（以 hash 識別）必須出現在該 container 的軟體物料清單（SBOM）中，具備發起網路連線的權限，並使用核准的執行路徑與命令列參數。DOCA Tower 接著再判斷政策是否允許這次請求的存取，例如是否有權存取某個 API 並執行該動作。這些脈絡同時也會豐富化 agent 活動的防竄改紀錄,減少下游系統事後比對關聯的需要。

🎯 **對工程師的啟示**

如果你的團隊正在為 agentic 系統設計安全架構，Sentry 的思路值得參考：不要把監控邏輯和 agent 跑在同一個信任域裡，否則一旦 agent（或它所在的主機）被攻破，監控本身也會失效。把政策執行點放在 agent 通往模型與外部世界的唯一路徑上，並搭配獨立於主機的執行環境內省能力，是目前針對 agent runtime 安全較為紮實的防禦層次設計。

🔗 **來源**
- 標題：Inside NVIDIA Sentry: Secure AI Agents at Runtime
- 作者／機構：Ofir Arkin, NVIDIA Developer
- 連結：https://developer.nvidia.com/blog/inside-nvidia-sentry-secure-ai-agents-at-runtime/

#NVIDIA #AIAgents #AgentSecurity #BlueField #DPU #RuntimeSecurity #OpenPolicyAgent #ZeroTrust #OpenShell #CyberSecurity
