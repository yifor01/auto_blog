---
title: rivet-dev/agentos
source: GitHub Trending
url: https://github.com/rivet-dev/agentos
score: 98
model: tencent/hy3:free
generated_at: '2026-07-19T08:03:16.388021'
---

📌 【rivet-dev 開源】agentOS：跑在程式內的 AI 代理作業系統

TL;DR：近零冷啟動的開源 AI agent OS，號稱比 sandbox 便宜至多 32 倍且可嵌入後端。

當大多數 AI 代理還在等 VM 開機、等容器拉取映像檔時，有沒有辦法讓 agent 在幾毫秒內就開始幹活，還能直接呼叫你後端的函式？

🤔 **AI 代理的冷啟動與隔離難題**

傳統 sandbox 提供完整 Linux 環境，代價是開機慢、成本高，且 agent 與你的後端之間往往得繞一層網路與複雜的認證。rivet-dev 推出的 agentOS 想把這件事翻轉：它是一套可攜式的開源 AI agent 作業系統，標榜近零冷啟動（約 6 ms），且成本比 sandbox 低至多 32 倍。

🧩 **跑在程式內的輕量 VM 與直接繫結**

README 指出，agentOS 是一個跑在你程式內的輕量 VM（lightweight VM），不需要開 VM、也不用拉容器，agent 以極小記憶體負擔在毫秒級啟動。它可嵌入你的後端，agent 透過 bindings 直接呼叫你的函式，沒有網路跳點、也不需要服務間的複雜 auth。

內建 ACP agents 包含 Pi、Claude Code 與 OpenCode。安全性採 deny-by-default：檔案系統、網路、程式存取皆預設拒絕，並使用與瀏覽器同源的隔離技術。

📊 **agentOS 與 Sandbox 的定位差異**

- agentOS：輕量 VM，跑在程式內；用 bindings 與細粒度許可權把 agent 整合進後端。
- Sandbox：完整 Linux 環境，適合瀏覽器、原生二進位制檔、dev server。
- 兩者不互斥：agentOS 可透過 sandbox extension 按需開出完整 sandbox，並在 workload 需要時掛載其檔案系統。

🎯 **部署彈性與實務啟示**

對工程師來說，agentOS 只是一個 npm 套件，能跑在筆電、Rivet Cloud、Railway、Vercel、Kubernetes 或任何容器平臺。若你在評估把 LLM agent 接進現有後端，又不想被 sandbox 的冷啟動與成本綁住，可先從 npm 安裝試跑最小範例：

```
npm install @rivet-dev/agentos-core @agentos-software/common @agentos-software/pi
import { AgentOs } from "@rivet-dev/agentos-core";
import common from "@agentos-software/common";
```

需注意 README 宣稱的 ~6 ms 冷啟動與 32x 成本優勢，實際數字會依部署環境與 workload 而異，建議以自身場景基準測試驗證。

🔗 **來源**
- 標題：rivet-dev/agentos
- 作者／機構：rivet-dev
- 連結：https://github.com/rivet-dev/agentos

#AI #AgentOS #OpenSource #Rivet #LLM #Sandbox #ACP #Backend #Bindings #DevOps
