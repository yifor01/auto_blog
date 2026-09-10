---
title: 'Google Open-Sources Mantis: A Modular Skills Toolkit That Lets Coding Agents
  Find, Reproduce and Patch Vulnerabilities'
source: MarkTechPost
url: https://www.marktechpost.com/2026/09/09/google-open-sources-mantis-a-modular-skills-toolkit-that-lets-coding-agents-find-reproduce-and-patch-vulnerabilities/
model: claude-code/sonnet
generated_at: '2026-09-10T20:02:51.114697'
score: 97
---

📌 Google 開源 Mantis：讓 Coding Agent 自己抓漏洞、寫修補

TL;DR：Google 開源 Mantis 技能鏈，讓 coding agent 自己抓漏洞、寫修補。

🎣 你的 AI coding agent 已經能幫你寫完一整個 PR，但它抓得出自己剛剛埋進去的漏洞嗎？Google 這次開源的 Mantis，賭的正是「讓同一個 agent 順便當自己的資安審查員」。

🤔 不是掃描器，是一套技能規則

Mantis 是一個 stack-agnostic（不綁定特定語言或框架）的安全審查技能工具包，設計理念是讓 AI coding agent 跑完整個漏洞生命週期：找出可疑瑕疵、過濾誤判、在沙箱中重現漏洞、寫出最小修補、對修補再次發動攻擊驗證，最後為殘餘風險打分數。它不是那種「對著 repo 掃一次就走人」的工具，而是一組你現有 coding agent 可以載入的 slash command，外加一套嚴格規定 agent 可以在哪裡執行程式碼的規則。素材指出，目前可部署於本機與內部評估，尚未用於正式產線。

🧩 從學習目標到證明漏洞的技能鏈

Mantis 把每個階段各自發布成獨立的 skill 目錄，以 slash command 呼叫並依序串接，一個名為 `/mantis-meta-agent` 的 supervisor skill 可以在長時間執行的 session 中驅動整條迴圈。

- 前期階段負責「認識目標」：`/mantis-history` 挖掘版本控制歷史中的過往安全修補，`/mantis-summarize` 寫出目錄地圖，`/mantis-architecture` 建立 Markdown 知識庫，`/mantis-threat-model` 推導信任邊界，`/mantis-plan` 產出鎖定目標的路線圖。
- 中期階段負責「找出並過濾」：`/mantis-researcher` 依照計畫掃描檔案，接著 `/mantis-dedupe`、`/mantis-review`、`/mantis-critic` 依序收斂重複項目、套用排除規則、剔除在正式版本中根本不可能發生的問題。
- 後期階段負責「證明並修補」：`/mantis-reproduce` 在 gVisor 或斷網的虛擬機中執行 payload 重現漏洞，`/mantis-chain` 把個別驗證過的發現組裝成多步驟攻擊鏈，`/mantis-patch` 套用並驗證修補，`/mantis-calibrate` 給出 1 到 10 的風險分數，`/mantis-reflect` 把學到的經驗寫回供下一輪使用，`/mantis-report` 產出人類可讀的審查報告。
- 較新的技能 `/mantis-advise` 則反過來運作：在你動手寫程式碼之前，先查詢累積下來的威脅模型、過往漏洞脈絡與已驗證的修補模式，避免同一類 bug 重蹈覆轍。

你可以直接 clone 下來，搭配 Gemini CLI、Antigravity CLI、Google ADK，或任何類似的 agent 框架執行。

💡 重現與再攻擊才是信任邊界

多數 agentic 安全工具做到「產生發現清單」就停了，Mantis 的特別之處在於把「重現」與「對修補再次攻擊」當成信任邊界本身，而且把各階段之間的接口（inter-stage contracts）公開發布，讓團隊可以把這些技能包進一套確定性的執行框架，而不是完全信任 LLM 自己去協調 shell 指令。

⚠️ 目前僅適合評估環境

素材明確指出 Mantis 「可部署於本機與內部評估，尚未適合正式產線」，代表現階段更適合拿來做安全審查流程的原型驗證，而非直接接上生產環境的 CI/CD。

🎯 實務啟示

如果你的團隊已經在用 coding agent 寫程式碼，Mantis 提供了一個現成的骨架，把「安全審查」也變成 agent 可以承接的一環工作，而不是完全另外一套人工流程。技能鏈公開、階段接口明確，代表你可以先挑幾個階段（例如 `/mantis-reproduce` 加 `/mantis-patch`）接進既有的 review 流程，逐步擴大採用範圍，而不必一次全盤導入。

🔗 來源
- 標題：Google Open-Sources Mantis: A Modular Skills Toolkit That Lets Coding Agents Find, Reproduce and Patch Vulnerabilities
- 作者／機構：Michal Sutter, MarkTechPost
- 連結：https://www.marktechpost.com/2026/09/09/google-open-sources-mantis-a-modular-skills-toolkit-that-lets-coding-agents-find-reproduce-and-patch-vulnerabilities/

#Mantis #GoogleAI #AgenticAI #AISecurity #CodingAgent #VulnerabilityResearch #OpenSource #GeminiCLI #DevSecOps #LLMSecurity
