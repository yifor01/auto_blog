---
title: Anthropic launches free AI security scans for open-source projects
source: The Verge AI
url: https://www.theverge.com/ai-artificial-intelligence/1008521/anthropic-open-source-oss-scanner
model: claude-code/sonnet
generated_at: '2026-10-08T22:26:01.940639'
score: 87
---

📌 Anthropic 推免費開源安全掃描，但報告全由 AI 生成、沒人把關

TL;DR：Anthropic 推出 OSS Scanner，用旗艦模型免費幫開源專案找漏洞，但報告不經人工審核。

如果有人告訴你，漏洞報告可能是錯的、也可能根本不存在，你還會願意讓它免費幫你掃描整個程式碼庫嗎？Anthropic 剛剛用這個交換條件，向整個開源社群丟出了一個新服務。

🤔 **開源維護者早已被 AI 生成的 bug 回報淹沒**

根據 The Verge 報導，過去幾個月 AI 工具確實找出了一些重大的開源安全漏洞，例如今年五月影響幾乎所有 Linux 散布版的「Copy Fail」漏洞。但硬幣的另一面是，部分開源專案已經快被 AI 生成的洪水式 bug 回報壓垮，報導中點名 Linus Torvalds 與 Google 都正在面對這個問題。OSS Scanner 正是在這個背景下推出。

🧩 **選擇性加入、定期掃描、模型包含 Claude Mythos**

OSS Scanner 是一個 opt-in 服務：開源專案選擇加入後，會定期收到由 Anthropic「最強模型」執行的安全掃描報告，完全免費。報導引用 Anthropic 的說明指出，這些輸出「完全由模型生成，沒有人工審核或 triage」，目的是讓掃描能跑得更快、更頻繁，報告生成模型包含 Claude Mythos，用意是給開源專案最大的防禦優勢。

⚠️ **代價：報告可能是錯的或無效的**

Anthropic 自己也在說明中承認，少了人工審核這一關，報告有可能不正確或無效。這等於是把「掃描頻率與速度」和「報告品質與可信度」直接對調——對已經在為 AI 生成 bug 報告噪音所苦的專案來說，這未必是單純的利多，反而可能加重分辨真偽的負擔。

🎯 **實務啟示**

如果你維護的開源專案打算加入 OSS Scanner，建議先想清楚自己的 triage 流程能不能撐住額外的模型生成報告量，而不是把它當成「免費又零成本」的安全網。對工程團隊來說，這類工具更適合當作額外的訊號來源，搭配既有的人工覆核與 CI 安全檢查一起使用，而不是取代現有的流程。

🔗 **來源**
- 標題：Anthropic launches free AI security scans for open-source projects
- 作者／機構：Stevie Bonifield（The Verge）
- 連結：https://www.theverge.com/ai-artificial-intelligence/1008521/anthropic-open-source-oss-scanner

#Anthropic #OpenSource #AISecurity #VulnerabilityScanning #ClaudeMythos #Linux #CyberSecurity #DevSecOps #AITools #SoftwareSecurity
