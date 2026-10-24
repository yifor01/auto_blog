---
title: 'Meet Anthropic’s sandbox-runtime: OS-Level Sandboxing for AI Agents, No Containers'
source: MarkTechPost
url: https://www.marktechpost.com/2026/10/24/anthropic-sandbox-runtime-ai-agent-sandbox/
model: claude-code/sonnet
generated_at: '2026-10-24T19:34:39.873822'
score: 103
---

📌 【Anthropic 開源】免容器也能幫 AI Agent 建好沙箱

TL;DR：Anthropic 開源 sandbox-runtime，用作業系統原生機制限制檔案與網路存取，不需容器就能關住 agent。

Claude Code 的 sandboxed bash tool 背後，其實是一個獨立可拆出來用的專案——而且它不挑廠商，你自己寫的 agent、本機 MCP server，甚至一般命令列程式都能包進去跑。

🤔 approval fatigue 才是真正的安全漏洞

coding agent 不只改檔案，還會安裝相依套件、抓文件、呼叫 API。開發者整天按「approve」,久了根本不會細看自己核准了什麼。Anthropic 團隊指出,少了網路隔離,一旦 agent 被 prompt injection 誘導,SSH key 等機密就可能被外洩;少了檔案隔離,agent 又可能逃出沙箱換取網路存取權。兩道邊界缺一不可,這正是 sandbox-runtime（簡稱 srt）要補的洞。

🧩 一行指令包住任意程式

安裝方式是 `npm install -g @anthropic-ai/sandbox-runtime`,之後在任何指令前面加上 `srt` 前綴即可,它同時提供 CLI 與 TypeScript library 兩種用法。srt 直接呼叫各作業系統自帶的隔離原語,限制範圍涵蓋整個 process tree,包含其中的腳本與子程序。對外流量只能透過跑在 host 上的 HTTP 與 SOCKS5 proxy 離開：Linux 上這些 proxy 藏在 bind-mount 進沙箱的 Unix socket 後面;macOS 則靠 Seatbelt profile 只放行一個 localhost port,再由 proxy 套用你設定的網域允許清單與拒絕清單。

預設策略遵循「先限制、再開放」的邏輯：讀取預設全部允許,除非被明確拒絕;寫入預設全部拒絕,除非被明確允許;網路存取預設拒絕,除非網域在允許清單裡。要讓 MCP server 吃沙箱,只需把 `.mcp.json` 裡的指令從 `npx` 換成 `srt`,原始指令當參數接上去,規則統一寫在 `~/.srt-settings.json`。若是自己的 agent,library 提供 `SandboxManager`,呼叫 `initialize(config)` 啟動 proxy,再用 `wrapWithSandbox()` 拿到包裝好的指令字串直接 spawn。

📊 內部數字：permission prompt 少了 84%

Anthropic 表示,在內部 Claude Code 使用情境中,套用沙箱後 permission prompt 減少了 84%。這是自報數字,並非第三方 benchmark,但方向很直接：固定一道邊界,讓 agent 在邊界內自由行動,只在邊界之外才真正需要人介入。

⚠️ 鬆緊要自己調

允許清單設太嚴,`npm install` 之類的正常操作就會失敗;設太鬆,沙箱形同虛設。srt 為此提供了多個調整用的 knob,讓開發者在「可用」與「安全」之間找到中間地帶,但這個平衡仍需要針對自己的使用情境手動測試與調校。

🎯 實務啟示

這工具最大的價值是「不綁定 Claude Code」——任何自建 agent 框架或 MCP server 都能直接套用同一套檔案/網路邊界,不必自己重新設計 OS 層隔離機制,也不必為了安全性額外引入容器的部署負擔。

🔗 來源
- 標題：Meet Anthropic's sandbox-runtime: OS-Level Sandboxing for AI Agents, No Containers
- 作者／機構：Asif Razzaq（MarkTechPost）
- 連結：https://www.marktechpost.com/2026/10/24/anthropic-sandbox-runtime-ai-agent-sandbox/

#AnthropicAI #ClaudeCode #AIAgents #Sandboxing #AgentSecurity #OpenSource #MCP #PromptInjection #DevTools #AISecurity
