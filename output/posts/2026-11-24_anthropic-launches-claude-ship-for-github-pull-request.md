---
title: Anthropic Launches Claude Ship for GitHub Pull Request Review and Fixes
source: MarkTechPost
url: https://www.marktechpost.com/2026/11/23/anthropic-claude-ship-pull-request-agents/
model: claude-code/sonnet
generated_at: '2026-11-24T03:41:01.554194'
score: 88
---

📌 【Anthropic 發布】Claude Ship:三個 Agent 接棒 PR 審核到核准

TL;DR：Claude Ship 用三個 Agent 分管審核、修復、核准,核准政策寫成 YAML 檔,合併仍由 GitHub 分支規則把關。

如果有一個 Agent 可以自動核准你的 Pull Request,你的第一個反應會不會是「這樣不會出事嗎」?Anthropic 這次把答案寫進一份放在 repo 裡的政策檔。

🤔 **三個 Agent,各自只管一步**

根據 Claude Ship 文件,這套工具把 GitHub PR 從審核到核准拆成三個 Agent:Code Review、PR Steward、Claude Approvals,每個 Agent 只負責一步。Code Review 已經正式上線(generally available),另外兩個還在公開 beta。無論哪個 Agent 做了什麼,最終能不能合併,仍由你的 GitHub 分支規則決定。

🧩 **審核 → 修復 → 核准的實際流程**

Code Review 負責找問題。PR Steward 負責推修復,而一次修復還能觸發另一輪審核。Claude Approvals 則套用你寫的政策來核准。PR Steward 被設計成不會自己核准或合併 PR;每次 push 之後,它會留言說明自己改了什麼、以及怎麼復原,開發者用 `@claude` 下指令操控它,用 `@claude stop` 讓它停下。

Claude Approvals 讀取 repo 裡的 `.claude/approvals.yml` 政策檔,Anthropic 稱它是「更聰明的 CODEOWNERS 檔」。規則可以要求 billing 相關程式碼需要 2 個人核准、test fixtures 只需要 1 個人;規則能讀取 PR 的事實與分類器(classifier)的判斷結果,但讀不到 CI 結果。

開發者在 Claude Code 裡執行 `/ship`,它會自動 commit、push、開 PR;Claude 審核之後會「watch」後續的意見回饋與失敗的檢查項目,但合併這個動作仍由人類自己按下。使用需求是 Claude Code v2.1.330 以上、GitHub CLI 2.63 以上、git 2.38 以上;一次 watch 會在 7 天後、或 PR 被合併、關閉時結束,`/steward` 可以跳過某個開啟中 PR 的審核。當 Claude 單獨行動時,Claude Code 會封鎖 merge、approve、auto-merge、force-push 這幾個指令,但 watch 期間用的仍是你自己的 `gh` 和 `git` 登入身分。

📊 **目前沒有公開第三方 benchmark**

Anthropic 沒有公布任何公開的 benchmark,只在發布文與工程部落格分享內部自報的結果,且沒有說明 precision 或 recall。這點值得提醒:這些數字是 Anthropic 自己量測、自己公布的。

💡 **怎麼收費、怎麼開始用**

Claude Ship 是 Claude Team 與 Enterprise 方案在 GitHub 上的功能,Owner 需要逐個 repo 開啟,建議一次只開一個。計費是透過 usage credits 用 token 計算,和方案本身的用量分開算:Code Review 的成本會隨 PR 數量、大小、審查等級與頻率變動,管理員可以設定花費上限;PR Steward 在 Owner 設定前沒有上限;Approvals 沒有基本費用,但分類器的執行與政策要求的審查都會計費,即使是在 observe mode 下也一樣。執行 `/ship` 則算一般的 Claude Code 用量。符合資格的 Enterprise 組織可以在 2027 年 1 月 15 日前申請至少 1 萬美元的 Claude Ship 額度,額度在申請後 30 天內到期。

🎯 **實務啟示**

想導入的團隊可以先用 observe-only 模式跑單一 repo,並設好花費上限,觀察政策檔判斷得準不準再逐步放手;設計 `.claude/approvals.yml` 時要記得它看不到 CI 結果,代表 CI 是否通過仍需要另一道規則去把關,不能全部託付給核准政策。

🔗 **來源**
- 標題：Anthropic Launches Claude Ship for GitHub Pull Request Review and Fixes
- 作者／機構：Asif Razzaq，MarkTechPost
- 連結：https://www.marktechpost.com/2026/11/23/anthropic-claude-ship-pull-request-agents/

#Anthropic #ClaudeCode #ClaudeShip #CodeReview #GitHub #AIAgents #DevOps #PullRequest #SoftwareEngineering #CICD
