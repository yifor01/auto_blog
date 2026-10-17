---
title: Perplexity Open-Sources SPACE, a Firecracker MicroVM Sandbox for AI Agents
source: MarkTechPost
url: https://www.marktechpost.com/2026/10/16/perplexity-open-sources-space-firecracker-microvm-sandbox-ai-agents/
model: claude-code/sonnet
generated_at: '2026-10-17T19:31:27.825869'
score: 100
---

📌 Perplexity 開源 SPACE：用 microVM 把 AI Agent 關進籠子

TL;DR：Perplexity 把撐起 Computer 所有任務的 microVM 沙箱開源，Apache 2.0 授權，團隊可直接自架。

一套每天跑滿 Perplexity Computer 全部工作階段的沙箱系統，而且團隊自己找了 9 個前沿模型來「越獄」它——這樣的產品被開源出來，值得工程師仔細看一眼。

🤔 **Agent 要能執行程式碼，但不能摸到主機**

Agent 工作的本質是長時間執行、有狀態、會分支，還得在重啟後存活。要讓 Agent 以 root 權限安裝套件、執行指令、呼叫外部服務，又不讓這些動作波及主機本身，Perplexity 的解法是：每個任務都配一臺獨立的 Firecracker microVM，憑證與對外流量全部由 VM 外部控管。這就是 SPACE（Sandboxed Platform for Agentic Code Execution）的設計起點，應用程式透過 HTTP API 建立 Linux 環境、下指令、串流輸出，template 提供起始檔案系統，sandbox 則是該 template 的一個實例，擁有自己的 VM 與可寫入磁碟，一個 sandbox 內可以跑多個指令。

🧩 **四層架構：API、controller、worker、data plane**

系統拆成 PostgreSQL 驅動的 API、controllers、worker services 與 data plane 四個部分。worker services 負責管理 VM、網路、volume、template 與憑證；每個 sandbox 的根檔案系統由 btrfs 的 copy-on-write 機制建立；sandbox 的生命週期在 running、paused、suspended、deleted 四種狀態間轉換。為了加速建立速度，Kubernetes 部署會維持一批已開機的 warm pool，單節點部署則改用 base snapshot。安全性上，每個 sandbox 擁有獨立的 guest kernel，host 上的 per-sandbox 網路閘道器會對每一個對外連線執行 egress 政策，密鑰（secrets）從不進入 guest，而是依 Perplexity 七月發布的工程文章所述，在網路層注入憑證，憑證儲存庫還加上了分層授權範圍、速率限制與審計日誌。

📊 **延遲從 447ms 降到 89ms，紅隊測試揪出真實繞過手法**

生產環境數據顯示，sandbox 建立延遲的 90th percentile 從 447 毫秒降到 89 毫秒，目前 100% 的 Perplexity Computer 工作階段都跑在 SPACE 上。更值得注意的是團隊自己發起的紅隊測試「Escaping SPACE: Part I」：讓 9 個模型以 root 權限在 guest 內嘗試突破，共跑了 2 個任務、4 種設定、216 次測試，結果 Claude Opus 5.0、GPT-5.6 Sol、GPT-5.6 Cyber 與 Kimi K3 都找到了繞過方法，手法是 DNS 偽造與共用 CDN IP 位址。Perplexity 隨後透過 nftables 加入來源位址驗證，讓閘道器終止 TLS 連線並同時檢查 SNI 與 HTTP host 是否符合允許清單，重測後沒有任何模型再產生可驗證的繞過。同一團隊也測試了 10 個第三方沙箱平臺，其中 8 個出現至少一次網路政策繞過，並已將結果通報給所有受影響的廠商。

🎯 **自架門檻與既有 E2B 使用者的遷移路徑**

安裝指南把 SPACE 部署進本地 Kind cluster，host 需要具備 /dev/kvm、/dev/net/tun、loop device 與 btrfs；若要在 VM 內跑，則需要巢狀虛擬化（nested virtualization）支援。已經在用 E2B 的團隊可以透過 E2B Compatibility Wrapper 嘗試遷移，其測試基準版本是 Python 套件 e2b==2.21.1，repo 中也附上了一份 AWS EKS 的參考部署範例。對於自建 coding 或 browsing agent 的團隊來說，這是一套經過生產規模與紅隊實測檢驗的隔離層，值得評估是否能直接拿來用。

🔗 **來源**
- 標題：Perplexity Open-Sources SPACE, a Firecracker MicroVM Sandbox for AI Agents
- 作者／機構：Asif Razzaq, MarkTechPost
- 連結：https://www.marktechpost.com/2026/10/16/perplexity-open-sources-space-firecracker-microvm-sandbox-ai-agents/

#AIAgents #Sandbox #Firecracker #MicroVM #Perplexity #OpenSource #CloudSecurity #AgentSecurity #Kubernetes #DevOps
