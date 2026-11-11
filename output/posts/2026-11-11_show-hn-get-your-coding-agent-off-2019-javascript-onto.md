---
title: 'Show HN: Get your coding agent off ~2019 JavaScript, onto modern web primitives'
source: Hacker News
url: https://github.com/GoogleChrome/modern-web-guidance
model: claude-code/sonnet
generated_at: '2026-11-11T23:46:32.595178'
score: 102
---

📌 Google Chrome 團隊出手：讓 Coding Agent 甩開 2019 年寫法

TL;DR：開源 skill+RAG CLI 補齊 coding agent 的現代 web 知識，guided 通過率 55%→92%。

🎣 你的 coding agent 明明「認得」CSS.highlights、`<dialog>`、field-sizing 這些現代 web API 的名字，寫出來的程式碼卻還是一堆 `<div>` 加 JavaScript 事件監聽，活像在 2019 年除錯。這不是記錯了 API，而是模型的預設偏好出了問題。

**🤔 模型知道名字，卻不會預設使用**

瀏覽器原生已經接管了過去得靠 50 行 JS 或額外依賴才能做到的事：`CSS.highlights` 可以不靠一堆 `<span>` 就完成文字範圍標亮；`<dialog>` 搭配 `showModal()` 內建背景遮罩與理想的 focus 管理；`field-sizing` 讓 textarea 隨輸入自動長高。問題是，模型即使知道這些 API 的存在，寫程式碼時仍一致地回退到舊式 `<div>`+JS 的寫法。Google Chrome 團隊聯合 Firefox、MDN、Edge，針對這個落差做了一套領域知識補充方案，今天發布 1.0 版本。

**🧩 skill + 輕量 Agentic RAG，不吃爆 context window**

這個開源專案的核心是 200 多篇、合計約 1.7MB 的手寫實作最佳實踐指南，由 web 專家整理並隨著 web 標準演進持續更新。團隊把它包裝成一個 agent skill，外加一套 Agentic RAG CLI，刻意不把啟用機制交給 MCP 的 dynamic tool search，而是把 skill description 精雕細琢成能在相關前端任務上準確觸發。RAG 部分團隊花了九個月打磨：原型是 500MB 的 native stack，最終壓到約 7MB 的純 JS 套件，在一般 CPU 上搜尋只要約 10 毫秒。此外還新增了一個確定性的 `legacy-scan` 功能，用 3 萬個 GitHub 儲存庫訓練，能在既有程式碼庫中揪出過時寫法讓 agent 去現代化改寫，在保留測試集上平均精確率達 92%。

如何使用（官方提供的指令）：
```
DISABLE_TELEMETRY=1 npx modern-web-guidance@latest install
DISABLE_TELEMETRY=1 npx modern-web-guidance@latest search "animate dialog modal"
DISABLE_TELEMETRY=1 npx modern-web-guidance@latest legacy-scan ./src
```
`install` 把技能接上 agent 工作流，`search` 可以直接查詢某個 UI 行為該用哪個現代 API 實作，`legacy-scan` 則掃描既有專案找出該更新的舊寫法。

**📊 200 個任務、1700 條斷言的實測**

團隊建了一套評測基礎設施，用 codex、claude、agy 等 agent 跑 200 個前端任務，設計了約 1,700 條以 Playwright 與 AST 為基礎的自動化斷言。沒有這個技能時，agent 平均通過率是 55%；裝上技能後提升到 92%。團隊也坦言，過程中發現原本以為「AI 不懂」的某些知識其實模型早就會了，於是反過來修剪掉那些指南內容，保持套件精簡。

**⚠️ 仍在迭代中**

`legacy-scan` 的 92% 平均精確率是在保留測試集上測得，並非百分之百準確；團隊也公開徵求回報錯誤或奇怪的判斷結果，顯示專案本身還在持續修正。

**🎯 實務啟示**

如果團隊在用 coding agent 寫前端，裝上這個技能等於直接把「現代 web 平臺知識」注入 agent 的判斷依據，不用每次在 prompt 裡手動提醒它別用過時寫法。`legacy-scan` 也可以當成程式碼現代化稽核的起點，先掃一輪抓出候選項目再交給 agent 處理，比整包交給模型自由發揮更可控。

🔗 來源
- 標題：Show HN: Get your coding agent off ~2019 JavaScript, onto modern web primitives
- 作者／機構：paulirish
- 連結：https://github.com/GoogleChrome/modern-web-guidance

#WebDev #CodingAgent #ModernWeb #ChromeDevTools #AIAgent #FrontendEngineering #OpenSource #RAG #DeveloperTools #JavaScript
