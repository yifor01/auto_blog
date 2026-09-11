---
title: OpenAI Agents API
source: Hacker News
url: https://developers.openai.com/api/docs/guides/agents-api/overview
model: claude-code/sonnet
generated_at: '2026-09-11T19:49:49.472352'
score: 107
---

📌 OpenAI 正式推出 Agents API：把 Codex 引擎搬進你的產品

TL;DR：OpenAI 開放 Codex 背後的 agent harness 給開發者直接呼叫，session、沙箱、多 agent 協作全部代管。

當大家還在自己拼湊 orchestration、context compaction、錯誤復原邏輯時，OpenAI 選擇把這套已經在 Codex 裡跑得很成熟的 harness 直接開放出來。這則消息在 Hacker News 上拿下 336 分、173 則留言，顯然戳中了不少開發者的痛點。

🤔 **開發者一直在重造的輪子**

打造 agent 應用時，session 管理、多輪對話的 context 壓縮、任務中斷後的復原，這些基礎設施每個團隊幾乎都要自己寫一遍。OpenAI 的做法是把應用程式的職責縮小到「提供工具＋選擇執行環境」，session 管理、orchestration、context compaction、recovery 全部交給 OpenAI 代管。

🧩 **四個核心概念撐起整個 API**

Agents API 圍繞四個概念設計：

- **Agent**：模型、指令、工具與可用的 MCP servers。
- **Environment**：可選的沙箱或運算環境，agent 在這裡存取檔案、載入 skills、執行指令。
- **Session**：一個持久化的 agent 實例，負責處理任務並回應輸入。
- **Events and items**：送進 agent 的輸入，以及一個 session 過程中產生的輸出。

一次完整的 session 生命週期大致是：建立 session → 設定 agent（OpenAI 會代為佈建環境）→ 交付任務 → 透過串流或 webhook 追蹤進度 → 對同一個 session 繼續下任務或即時引導 agent。

託管的 Codex harness 支援在沙箱中執行程式碼、套用相關 skills 與指令、透過工具或 MCP 連接外部資料、在 agent 工作時進行引導、自動摘要先前工作以管理 context window、把任務拆解給 subagent，以及在中斷處恢復 session。

從文件釋出的範例程式碼可以看到，建立 session 時可以直接設定 `multi_agent: { enabled: true, max_concurrent_subagents: 4 }`，讓 agent 依需要把獨立的研究任務分派給 subagent 平行處理；也可以掛上 `programmatic_tool_calling`、MCP server（例如官方文件的 MCP）與 `web_search` 等工具，並指定 `environment.type` 為自架或 OpenAI 代管的沙箱。

📊 **計費方式沿用既有標準**

模型使用量依所選模型的 API 費率計費，OpenAI 提供的工具依標準費率計費，OpenAI 代管的沙箱則依標準容器費率計費，沒有另外的「agent 稅」。

文件也列出了幾個完整應用範例，包括事件應變 agent（調查告警並請求核准修復動作）、Slack bot（透過連接的辦公工具調查請求）、資料分析師（用唯讀 SQL 回答資料倉儲問題）、GitHub issue 調查員（重現回報的 bug 並在 GitHub 上分享發現），以及文件審閱者（搭配政策 skills 與專家 agent 審閱文件）。

🎯 **實務啟示**

如果你的團隊一直在自建 agent 的 session 管理、context compaction 與多 agent 協作邏輯，這個 API 值得評估能否直接替換掉那層基礎設施，把心力放回工具與業務邏輯本身。啟用前建議先看清楚 quickstart 裡對 API key 權限與 SDK 版本的要求，以及自架環境（self_hosted）與 OpenAI 代管沙箱在功能與限制上的差異。

🔗 **來源**
- 標題：OpenAI Agents API
- 作者／機構：aquir（Hacker News 投稿者）
- 連結：https://developers.openai.com/api/docs/guides/agents-api/overview

#OpenAI #AgentsAPI #Codex #AIAgents #MCP #LLM #DeveloperTools #Orchestration #Sandbox #MultiAgent
