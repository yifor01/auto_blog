---
title: DeepSeek Harness v0.2 Brings Official Desktop Apps to Its Open-Source Agent
  Harness
source: MarkTechPost
url: https://www.marktechpost.com/2026/10/03/deepseek-harness-v0-2-brings-official-desktop-apps-to-its-open-source-agent-harness/
model: claude-code/sonnet
generated_at: '2026-10-04T20:14:55.885514'
score: 90
---

📌 DeepSeek Harness v0.2：Agent 開發框架補上官方桌面版

TL;DR：DeepSeek 開源 agent harness「dsh」推出 macOS／Windows 桌面應用，省去自己裝 Node.js 的麻煩。

一個開源 agent harness 累積到 24 萬顆 GitHub star、2.9 萬次 fork 是什麼感覺？DeepSeek 的 dsh 做到了,而這次 v0.2 預覽版補上的,是一件聽起來很平凡,但對日常使用體驗很關鍵的東西：官方桌面安裝檔。

🤔 **Harness 是什麼，為什麼需要它**

Harness 是把一個模型變成 agent 的執行環境，負責讀檔案、跑指令、維護計畫。dsh 在 2026 年 8 月以 MIT 授權開源，底層跑在 Cordis 框架上（對應論文《A Programming Paradigm for Spatiotemporal Composability》），架構上把 model adapter、tool registry、agent loop 全部做成可替換的 plugin，所以 dsh 並不綁死 DeepSeek 自家模型，官方的 provider guide 也支援第三方與自訂 OpenAI 相容端點。

🧩 **v0.2 帶來什麼**

這次更新的重點是官方桌面應用，涵蓋 macOS（Apple silicon）與 Windows（64-bit），可從 deepseek.com/harness 下載，或用 `npx @deepseek-ai/dsh web` 直接跑。桌面版把 dsh 指令整合進去,使用者不再需要另外裝 Node.js 或 pnpm。登入方式可以用 DeepSeek 帳號，也可以自己填 API key；根據 rc.1 的release notes，用帳號登入的模型可以直接用網頁搜尋功能，不需要額外的 key。

DeepSeek 也拿 dsh 當自家的評測平臺用。API changelog 提到，Code Agent 的基準測試是在「DeepSeek Harness minimal mode」下跑的，DeepSeek-V4-Flash-0731 在 Terminal Bench 2.1 上拿到 82.7 分。

更新中的 v0.2.1-alpha.1 build 加了一層實驗性的 Claude Code Mods 相容層，DeepSeek 把它定位成一次測試：驗證 Mods API 是否大致是 dsh plugin 體系的子集，但並未承諾完全相容。同一個 build 還新增「讓 Agent 自己建立 plugin」的入口、一組可選的 Developer Tools，以及給反向代理用的 `--public-url` 旗標；同時移除了 runtime invariant plugin，對部分既有擴充功能來說是個 breaking change。

⚠️ **仍是預覽版，相容性會持續變動**

DeepSeek 自己也提醒，接下來還會有相容性破壞性的變更，這次移除 runtime invariant plugin 就是一個例子。想拿來做正式產品整合的團隊，得有準備隨版本升級調整程式碼。

🎯 **實務啟示**

對已經在用 Claude Code、Cursor 之類 agent 工具的工程師，dsh 的吸引力在於它整條 pipeline（model adapter、tool registry、agent loop）都是可替換 plugin，而且不綁定單一模型供應商；桌面版降低了上手門檻,值得拿來跟自己手上的 coding agent 工作流做個效能與相容性比較。但目前是 preview 階段,建議先在非關鍵專案試用,等 breaking change 頻率降下來再考慮正式導入。

🔗 **來源**
- 標題：DeepSeek Harness v0.2 Brings Official Desktop Apps to Its Open-Source Agent Harness
- 作者／機構：Michal Sutter, MarkTechPost
- 連結：https://www.marktechpost.com/2026/10/03/deepseek-harness-v0-2-brings-official-desktop-apps-to-its-open-source-agent-harness/

#DeepSeek #AgentHarness #OpenSource #AIAgents #DeveloperTools #dsh #PluginArchitecture #CodingAgent #LLMTooling #MIT
