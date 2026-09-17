---
title: OpenSpec – A lightweight and configurable AI spec framework
source: Hacker News
url: https://openspec.dev/
model: claude-code/sonnet
generated_at: '2026-09-17T20:37:37.660098'
score: 85
---

📌 OpenSpec:讓 Coding Agent 照規格做事,不再自由發揮

TL;DR:OpenSpec 是一套輕量規格框架,用五步驟工作流讓團隊與 coding agent 對齊需求。

當 coding agent 能力越來越強,新的痛點浮現:agent 寫出來的東西,常常不是你真正想要的。OpenSpec 這個在 Hacker News 拿下 186 點讚、GitHub 累積 6.8 萬顆星的專案,試圖用「規格先行」的方式解決這個問題。

🤔 建構正確的東西,並且正確地建構它

OpenSpec 是一套輕量且可配置的框架,用來建立與管理軟體規格。核心理念是把「你想做什麼」寫成一份 spec,讓團隊與 coding agent 在整個開發過程中保持對齊——先協助釐清需求,驗證規格描述的是「對的東西」,再驗證實作是否真的符合規格。

🧩 五個指令構成的規格生命週期

OpenSpec 的工作流以一組斜線指令呈現:

- `/opsx:explore`:探索問題、理解現有程式碼庫
- `/opsx:propose`:草擬 proposal.md、specs/、design.md、tasks.md
- `/opsx:apply`:依照規格實作任務
- `/opsx:verify`:檢查實作是否符合規格
- `/opsx:archive`:封存已完成的變更

這套流程並不綁定單一工具,官方相容清單涵蓋 Claude Code、Codex、Cursor、GitHub Copilot、Gemini CLI、OpenCode、Amazon Q Developer 等三十多種 coding agent 與編輯器整合。

🧩 安裝與使用

安裝方式很單純,用 npm、pnpm、bun、yarn 或 nix 皆可:

```
npm install -g @fission-ai/openspec@latest
```

安裝完成後,在相容的 coding agent 環境中呼叫上述 `/opsx:` 系列指令,即可依序完成探索、提案、實作、驗證與封存的循環。

🎯 實務啟示

如果團隊同時使用多種 coding agent、或多人協作同一個專案,規格容易在對話與工具切換間流失。OpenSpec 把「規格是什麼」與「實作是否符合規格」明確拆成獨立步驟,對於需要在多個 agent 工具間保持一致工作流程的團隊,是值得評估的輕量選項。

🔗 來源
- 標題:OpenSpec – A lightweight and configurable AI spec framework
- 連結:https://openspec.dev/

#OpenSpec #AICodingAgent #SpecDrivenDevelopment #DeveloperTools #ClaudeCode #OpenSource #SoftwareEngineering #AIWorkflow #CLI #CodingAssistant
