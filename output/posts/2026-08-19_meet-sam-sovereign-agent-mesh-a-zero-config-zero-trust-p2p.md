---
title: 'Meet SAM (Sovereign Agent Mesh): A Zero-Config, Zero-Trust P2P Network for
  AI Agents'
source: MarkTechPost
url: https://www.marktechpost.com/2026/08/18/meet-sam-sovereign-agent-mesh-a-zero-config-zero-trust-p2p-network-for-ai-agents/
model: claude-code/sonnet
generated_at: '2026-08-19T06:29:48.019387'
score: 108
---

📌 零信任 P2P 網路，讓 AI 代理不必互相裸奔

TL;DR：Google 開源的 SAM 用 P2P overlay 讓 AI agent 安全共享工具，不必把內部 API 曝露到公網。

當 AI agent 開始跑在雲端伺服器、機房、筆電、樹莓派甚至 Android 裝置上，一個尷尬的問題浮現：要讓這些 agent 互相呼叫彼此的工具，多數人的做法是直接把內部腳本、LLM endpoint 或私有 API 開放到公網。google/sam（Sovereign Agent Mesh，非 Segment Anything）想解決的正是這件事。

🤔 **問題：agent 之間怎麼安全共享工具**

專案採 Apache-2.0 授權，репо 明確聲明這不是 Google 官方支援的產品，公開的 mesh 目前也標記為 beta testnet。SAM 提供的是零設定、零信任的 P2P overlay，概念上更接近私有 VPN，但範圍限定在透過 Model Context Protocol（MCP）進行 agent 對 agent 的工具共享。節點可自動互相發現、能穿越 NAT，且每次呼叫都經過加密授權。

🧩 **信任模型：Biscuit token 與離線授權**

一個節點以 `sam-node join` 加入網路，再用 `sam-node run` 啟動。底層的 libp2p 使用 5001/udp 與 5002/tcp，本地 MCP API 預設監聽 8080。

真正的核心在控制平面：它驗證使用者的 OIDC JWT，把 claim 轉譯成 Datalog facts 並封裝進 Biscuit token 中。`sub` 變成 `user(...)`，每個群組變成 `group(...)`，peer ID 則綁定為 `client_peer_id(...)`。結果是節點可以離線授權，也就是說每個節點只需要拿呈遞的 token 對照自己本地的規則做評估，不必回連控制平面確認。

授權策略是嚴格的預設拒絕（default-deny），存取必須有明確的能力事實，例如 `granted_service_exact(...)`；沒有任何內建例外，就連 discovery catalog `system://sam.catalog` 也必須被明確授權。服務命名採 `type://name` 的慣例，並支援萬用字元，例如 `mcp://*`、`mcp://build-runner.*`。

每個請求都會跑一個兩階段流程：第一階段先用封鎖與撤銷快取（ban/revocation cache）過濾連線；第二階段執行兩次 Biscuit authorizer：一次針對節點自身的身分 token（產生 `target_fact` 斷言），一次針對呼叫方的 token。另有一個基準檢查會要求連線的 peer ID 必須與 token 相符，藉此阻擋重放攻擊。

操作者可以在本地做進一步限縮（attenuate），例如晚上 9 點後禁止某個寫入工具、或封鎖特定承包商；但本地允許規則無法繞過控制平面的檢查條件。

🎯 **實際能拿來做什麼**

節點對外提供標準的 MCP 工具：`discover_remote_services`、`find_remote_tools`、`call_remote_tool`，官方指南涵蓋 Gemini、Claude Code、Claude Desktop、Google Antigravity 與 OpenClaw 的整合方式。`sam-node skill install` 會寫出一份 `SKILL.md`，讓 agent 自己就能把節點帶上線，但登入註冊這一步刻意保留給人類操作。

另一個亮點是 Secure Outbound Gateway。沙箱中的 `nano-init` 以 PID 1 執行並設定 proxy 環境變數；對於不理會這些變數的工具，它會透過 LD_PRELOAD 攔截 C 語言的 `connect()` syscall（針對 80/443 port），流量經由 Unix domain socket 送到 `sam-box`。閘道驗證 Biscuit token 後，從 `secrets.yaml` 注入真正的憑證並升級成 HTTPS，agent 沙箱本身從頭到尾不會持有金鑰。

repo 中的 code-reviewer pool 範例則示範用普通 MCP 服務把批次工作分散給多個相同的 worker：manager 透過 DHT 發現 peer，用 lease 追蹤忙碌狀態，正確性靠同步 lease 分配、fencing token、寬限退場（grace eviction）與 `POOL_BUSY` 兜底機制保障；worker 端則離線驗證短效 HMAC token，驗證失敗就回傳 `NO_LEASE`。

🔗 **來源**
- 標題：Meet SAM (Sovereign Agent Mesh): A Zero-Config, Zero-Trust P2P Network for AI Agents
- 作者／機構：Michal Sutter, MarkTechPost
- 連結：https://www.marktechpost.com/2026/08/18/meet-sam-sovereign-agent-mesh-a-zero-config-zero-trust-p2p-network-for-ai-agents/

#AIAgents #P2P #ZeroTrust #MCP #ModelContextProtocol #Biscuit #libp2p #AgentSecurity #OpenSource #GoogleAI
