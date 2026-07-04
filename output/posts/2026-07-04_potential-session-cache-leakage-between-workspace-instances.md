---
title: Potential session/cache leakage between workspace instances or consumer accounts
source: Hacker News
url: https://github.com/anthropics/claude-code/issues/74066
score: 64
model: google/gemma-4-31b-it:free
generated_at: '2026-07-04T19:26:46.524685'
---

📌 【安全性警訊】Claude Code 出現 Session 洩漏？企業使用者恐面臨快取隔離失效

TL;DR：Claude Code 疑似發生 Session/快取洩漏，導致企業使用者在對話中收到其他帳戶的 Minecraft 相關內容。

當你正在處理企業級機密專案時，AI 突然問你「Minecraft 神廟要用什麼磚塊」——這不僅是個幽默的 Bug，更是嚴重的安全性警訊。

🤔 **企業隔離機制疑似失效**

一名使用 Claude Code 2.1.199 版本的使用者回報，儘管他已通過 Enterprise ZDR（零信任）工作區的身分驗證，但 Agent 卻突然開始詢問關於 Minecraft 神廟的建築細節，並在總結中自信地聲稱正在建造一座神廟。

這項異常現象引發了對快取隔離機制的質疑：如果快取（Cache）沒有在不同工作區或消費者帳戶之間完全隔離，這意味著敏感的對話內容可能在不同使用者間發生洩漏。

🧩 **問題發生的環境細節**

根據 GitHub Issue 的回報，該問題發生在以下環境：
- 平臺：macOS (darwin)
- 終端機：Apple_Terminal
- 版本：2.1.199
- 具體現象：在企業工作區會話中，出現了與該使用者無關的第三方對話內容（Minecraft 建築相關）。

⚠️ **潛在的安全性風險**

使用者在回報中指出，若此現象是由於消費者方案（Consumer plan）與企業方案之間的快取洩漏引起，將對 Enterprise ZDR 的安全性提出嚴重質疑，因為這意味著企業的敏感對話內容可能被傳送到不正確的端點。

🎯 **實務啟示**

對於使用 AI CLI 工具處理敏感資料的工程師，此案例提醒我們：
1. 不要預設 AI 工具的 Session 隔離是絕對安全的，特別是在多帳戶切換或混合使用企業與個人帳戶時。
2. 在處理極高機密資料前，應密切關注工具的安全性更新與 Bug 回報（如 GitHub Issues）。
3. 定期檢查 AI Agent 的輸出是否出現不相關的「幻覺」，有時這可能是系統底層快取汙染的徵兆而非單純的模型幻覺。

🔗 **來源**
- 標題：Potential session/cache leakage between workspace instances or consumer accounts
- 作者／機構：chatmasta
- 連結：https://github.com/anthropics/claude-code/issues/74066

#ClaudeCode #Security #DataLeakage #EnterpriseSecurity #BugReport #AI #LLM #macOS #CacheIsolation #CyberSecurity
