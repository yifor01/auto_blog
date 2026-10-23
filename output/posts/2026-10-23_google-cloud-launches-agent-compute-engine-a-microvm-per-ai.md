---
title: 'Google Cloud Launches Agent Compute Engine: A MicroVM per AI Agent'
source: MarkTechPost
url: https://www.marktechpost.com/2026/10/22/google-cloud-agent-compute-engine-microvm-ai-agents/
model: claude-code/sonnet
generated_at: '2026-10-23T20:42:18.297717'
score: 94
---

📌 【Google Cloud 新服務】讓每個 AI Agent 住進專屬 MicroVM

TL;DR：Google Cloud 推出 Agent Compute Engine，用硬體隔離的 microVM 包住每個 agent，沙箱內不放任何憑證。

如果你的 AI agent 被 prompt injection 攻破，攻擊者能拿到什麼？Google Cloud 給出的答案是：什麼都拿不到。這正是本週在 AGNTCon + MCPCon 發表的 Agent Compute Engine（ACE）想解決的問題。

🤔 **Agent 的攻擊面，從「程式碼」變成「自然語言」**

傳統應用程式的攻擊面相對可控，但 AI agent 會讀取不受信任的網頁、文件、第三方工具回應，等於隨時暴露在 prompt injection 之下。Google 的因應策略很直接：假設沙箱內的一切都已被攻陷，讓「拿下沙箱」這件事本身變得沒有意義。根據 Google 的技術文章，ACE 目前已用於支援 Gemini 作為工作任務的 agent，以及 Antigravity 和內部的評估、RL 訓練管線。

🧩 **把 Agent 拆成「大腦」與「手」**

Google 將每個 agent 拆成兩部分：harness（大腦）負責呼叫模型並做決策，完全在沙箱之外運行；sandbox（手）則負責實際執行程式碼、shell 指令與瀏覽器操作。Harness 只會把明確的指令下發給沙箱，兩者之間有清楚的邊界。

每個 session 都在單租戶的 microVM 中執行，背後是 Cloud Hypervisor 提供的隔離邊界。Host 本身是無狀態的 appliance，根檔案系統唯讀且以 dm-verity 強制驗證；Titanium 則把 attestation 金鑰保存在 guest 之外，避免被沙箱內的程式碼窺探。

在身分設計上，Google 為每個 agent workload 定義了 4 種身分，其中 workload identity 即使被外洩也無法直接呼叫 API，它只能用來標識「這個封包是哪個沙箱送出的」——等於把身分和權限徹底脫鉤。

效能與密度方面，Google 觀察到 agent 大多數時間其實在等待模型回應或等待使用者，因此沙箱會在工具呼叫結束時發出訊號，host 便能把閒置的 microVM checkpoint 到零資源佔用，下次呼叫再恢復。密度則來自 copy-on-write 記憶體共享：預先暖機的 snapshot 映像以 DAX 方式掛載，讓同一臺 host 上的多個 microVM 共享基礎 OS 與函式庫頁面，只有每個 agent 自己修改過的頁面才會佔用私有記憶體。Harness 也因此獲得 clone、snapshot/fork、rewind、rollback 等能力。儲存則分成三層：可拋棄的 scratch overlay、共享唯讀 volume，以及建立在 Hyperdisk 上的持久化使用者工作區。

📊 **開源的 Kubernetes 版本已經可用**

與 ACE 對應的開源、Kubernetes 原生版本叫 Agent Substrate，自 2026 年 9 月 15 日起已在 GKE 上提供，可選擇 Cloud Hypervisor microVM 或 gVisor 沙箱，並支援 Claude Code、OpenClaw、Hermes 等 harness。原始碼公開在 github.com/agent-substrate/substrate。目前它開放給所有 GKE 客戶做非正式環境測試，正式環境 GA 則僅限白名單客戶。Google 同時把既有的 Gemini for business agent governance 能力延伸到 Agent Runtime、Cloud Run、Agent Sandboxes、GKE 與 ACE，整套 stack 還包含 Agent Gateway、Agent Registry、Agent Identity，以及基於 OpenTelemetry 的可觀測性。

⚠️ **目前仍處於預覽階段**

ACE 的客戶預覽計畫在「未來幾個月」才會開放，正式環境的 GA 也僅限白名單客戶，意味著多數團隊短期內還無法直接在自己的生產環境中使用。

🎯 **實務啟示**

對正在建置 agent 平臺的工程團隊來說，ACE 的「零憑證沙箱＋身分與權限脫鉤」思路值得借鏡：與其在沙箱裡做更多防護，不如假設沙箱必然會被攻破，從架構上讓攻陷沒有意義。若你已經在用 GKE，Agent Substrate 是現在就能動手試的開源入口。

🔗 **來源**
- 標題：Google Cloud Launches Agent Compute Engine: A MicroVM per AI Agent
- 作者／機構：Michal Sutter, MarkTechPost
- 連結：https://www.marktechpost.com/2026/10/22/google-cloud-agent-compute-engine-microvm-ai-agents/

#GoogleCloud #AIAgents #MicroVM #CloudSecurity #AgentCompute #Sandboxing #CloudHypervisor #Kubernetes #GKE #AgentSubstrate
