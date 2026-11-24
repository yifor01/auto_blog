---
title: Anthropic launches Claude Ship, letting AI agents review, fix, and approve
  code changes
source: TechCrunch AI
url: https://techcrunch.com/2026/11/23/anthropic-launches-claude-ship-letting-ai-agents-review-fix-and-approve-code-changes/
model: claude-code/sonnet
generated_at: '2026-11-24T03:41:01.554306'
score: 84
---

📌 當 Agent 寫完 PR,核准鍵該由誰按?

TL;DR：Claude Ship 新意不在審查程式碼,而在把核准權限也交給依政策行動的 Agent。

多數團隊的直覺是「每一個改動都該有人核准」,這在人人手寫程式碼的時代很容易跟上。但當寫程式碼的主力變成 Agent,審核與核准反而成了新的瓶頸。Anthropic 這次推出的 Claude Ship,瞄準的正是這個卡點。

🤔 **瓶頸從「寫」轉移到「審」**

隨著 AI coding agent 能產出的程式碼量越來越大,上線前的審核與核准開始出現積壓。Claude Ship 的做法是把 PR 之後的更多工作自動化,其中最值得注意的一步,是把核准這件事的部分權限也委派給 Agent 本身,而不只是找問題、修問題。Anthropic 在部落格裡寫道:「多數團隊希望每個改動都有人核准,這在人人手寫每一行程式碼時很容易維持。但現在很多開發者是跟 Agent 一起開發。在 Claude Code 團隊裡,大部分程式碼是 Claude 寫的,我們希望 PR 之後的每一步也能跟上這個速度。」

🧩 **三個 Agent,各管一段**

Claude Ship 目前還在 beta 階段,讓早期採用者先用它審查 PR,再自己決定什麼該合併。它由三個 Agent 組成:已經正式上線的 Code Review,以及還在 beta 的 PR Steward 和 Claude Approvals。Code Review 負責找問題;PR Steward 處理失敗的 CI 檢查、合併衝突,以及 Code Review 提出的回饋,每次 push 之後都會留言說明自己改了什麼、以及如何回復;Claude Approvals 則套用團隊寫在 repo 裡的核準政策,這份政策可以用自然語言撰寫,並能納入 Code Review 的發現或 Anthropic 自家分類器的判斷。

💡 **beta 階段的安全網**

因為還在 beta,Anthropic 建議先用 observe-only 模式跑這套流程,先觀察、不授權它實際動作。團隊也可以先從一個 repo 開始,並設定每月的花費上限。更重要的是,團隊始終能控制 Claude Ship 在哪裡執行、要用哪種審查等級(Quick、Standard 或 Deep),以及哪些變更應該升級交給人類來決定。

🎯 **實務啟示**

Claude Ship 正在推展到 GitHub 上的 Claude Team 與 Enterprise 方案。對已經大量用 Agent 寫程式碼的團隊來說,這個產品給出的訊號是:解決審核積壓不是靠人看得更快,而是把一部分核准邏輯寫成可執行的政策,交給 Agent 去跑,同時保留 observe 模式與人工升級作為退路,這比單純的程式碼審查工具多了一層治理設計,值得在導入前先想清楚政策要怎麼寫。

🔗 **來源**
- 標題：Anthropic launches Claude Ship, letting AI agents review, fix, and approve code changes
- 作者／機構：Sarah Perez，TechCrunch AI
- 連結：https://techcrunch.com/2026/11/23/anthropic-launches-claude-ship-letting-ai-agents-review-fix-and-approve-code-changes/

#Anthropic #ClaudeShip #AIAgents #CodeReview #GitHub #DevOps #AgenticCoding #PullRequest #SoftwareDevelopment #AIAutomation
