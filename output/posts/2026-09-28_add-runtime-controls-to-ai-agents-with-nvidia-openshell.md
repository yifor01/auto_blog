---
title: Add Runtime Controls to AI Agents with NVIDIA OpenShell
source: NVIDIA Developer
url: https://developer.nvidia.com/blog/add-runtime-controls-to-ai-agents-with-nvidia-openshell/
model: claude-code/sonnet
generated_at: '2026-09-28T22:40:33.834158'
score: 105
---

📌 NVIDIA OpenShell：把權限管控搬到 Agent 外面

TL;DR：開源 runtime OpenShell 0.1.0 不必重寫 agent 程式碼,就能在外部強制限制它能存取的系統與資料。

給 AI agent 一個目標,它就能自己寫程式、呼叫工具、隨著新資訊調整做法,連續工作好幾天甚至數週去追查軟體故障、跑實驗、執行業務任務。但問題也隨之而來:一個會「自己進化做法」的程式,你敢放心把 production 資料庫、機密資料和外部服務的存取權交給它嗎?

🤔 **廣泛存取權,帶來更嚴重的失敗模式**

Agent 要完成任務,通常需要 workspace、運算資源、資料、憑證與外部服務的存取權。但存取範圍越廣,一旦出錯代價也越大,從改動 production 資料、洩漏機密資訊,到執行超出被指派任務範圍的動作,都是實際可能發生的失敗情境。NVIDIA OpenShell 0.1.0 就是為了解決這個問題而生的開源 runtime,專門定義並強制執行「agent 能存取哪些系統與資料」的邊界。

🧩 **三個元件,把控管搬到 workload 之外**

OpenShell 由三個部分組成:

- **OpenShell Gateway**:管理大量 sandbox 的生命週期與政策。
- **OpenShell Supervisor**:與每個 sandbox 配對,運作在 agent workload 之外,檢查每一筆對外請求是否符合政策。
- **OpenShell Sandbox**:實際執行 workload,透過作業系統核心層級的控制限制檔案存取與行程權限,且除了透過 supervisor 之外沒有其他網路路徑。

Supervisor 能檢視設定好的 HTTP、GraphQL 與 MCP 流量,做到「允許讀取查詢、但擋下透過同一個 API 進行的寫入」這種細粒度控制。這些限制在 agent 開啟 shell、執行產生的程式碼、啟動子行程,甚至把任務委派給 sub-agent 時仍然有效。每一次政策判斷都會寫進 OCSF 格式的稽核紀錄,被擋下的請求也可以回傳描述性錯誤,協助 agent 決定下一步。

📊 **OpenShell 0.1.0 的核心能力**

| 能力 | 作用 |
|---|---|
| 多租戶平臺支援 | 在共用基礎設施上,為不同團隊或客戶提供各自獨立的 workspace、權限與服務存取 |
| 正式政策驗證 | 讓人類與 AI 審核者看清請求的權限是否落在安全邊界內 |
| 可擴充的安全與治理整合 | 串接第三方安全服務、治理系統與自訂檢查,執行點在 agent workload 之外 |
| 憑證保護的服務存取 | 真實憑證留在 agent workload 之外,只綁定給經授權的請求使用 |
| CPU 與 GPU 執行 | 可在容器、VM、Kubernetes 上以 CPU 或 GPU 執行實驗與資料處理 |

💡 **實際操作:一個看得到政策判斷的示範**

文章用 curl 搭配 GitHub REST API 的未驗證端點,示範政策如何生效。先建立一個完全沒有對外網路權限的 sandbox:

```
openshell sandbox create --name policy-demo \
  --no-auto-providers \
  --policy examples/no-network.yaml
```

在 sandbox 內嘗試 `curl https://api.github.com/zen` 會直接失敗,因為沒有對外網路權限;另開一個 host 終端機執行 `openshell logs policy-demo --since 5m` 就能看到是哪個程式發起請求、為何被擋。接著替換成允許唯讀存取 GitHub API 的政策(YAML 編譯成 OPA/Rego,由 OpenShell 逐筆請求評估):

```
network_policies:
  github_api:
    name: github-api-readonly
    endpoints:
      - host: api.github.com
        port: 443
        protocol: rest
    enforcement: enforce
    access: read-only
    binaries:
      - path: /usr/bin/curl
```

套用後不需要重啟 sandbox,再試一次:GET 請求通過,POST 請求被擋下,host 端的紀錄會確認這一點。文章同時指出,授權存取一項服務不代表憑證能用在別處——真實憑證由「provider profile」定義所綁定的端點與允許程式,即使 agent 把佔位憑證送到未經授權的目的地,請求也會被拒絕;而目標服務端仍然會依真實憑證的權限做二次把關,等於是多加了一層控制。

目前支援 Codex、Claude Code、Pi、Hermes 等 agent 框架,適用場景橫跨企業應用、前沿研究到機器人與邊緣運算。

🎯 **實務啟示**

如果你手上已經有一套在跑的 agent,不想為了加安全控管而重寫程式碼,OpenShell 提供了一條務實路徑:把權限管控整層搬到 agent workload 之外執行,既能保留 agent 自行選擇工具、調整策略的彈性,又能讓管理者用 YAML 政策檔案精確定義「能做什麼、不能做什麼」,並留下可審計的紀錄。

🔗 **來源**
- 標題:Add Runtime Controls to AI Agents with NVIDIA OpenShell
- 作者／機構:Alex Watson,NVIDIA Developer
- 連結:https://developer.nvidia.com/blog/add-runtime-controls-to-ai-agents-with-nvidia-openshell/

#NVIDIA #OpenShell #AIAgent #AgentSafety #Sandboxing #DevSecOps #MCP #OpenSource #RuntimeSecurity #AgenticAI
