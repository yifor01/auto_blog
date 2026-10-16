---
title: Code Review is now generally available
source: Claude Blog
url: https://claude.com/resources/articles/code-review-is-now-generally-available
model: claude-code/sonnet
generated_at: '2026-10-16T20:07:37.123060'
pinned: true
---

📌 【Anthropic 官方發布】Code Review 轉正式版，審查時間砍掉三分之二

TL;DR：Claude Code Review 正式開放給 Team／Enterprise，審查時間從約 20 分鐘降到 6-10 分鐘。

Coding agent 讓團隊寫程式碼的速度越來越快，但 code review 這道關卡卻沒有跟著變快，反而成了交付瓶頸。Anthropic 這次把自家的 Code Review 工具從 research preview 轉成正式版，直接針對這個瓶頸下手。

🤔 **審查跟不上寫 code 的速度**

Anthropic 指出，coding agent 持續拉高團隊寫程式碼的速度，review 的瓶頸卻沒有緩解。在 research preview 期間使用 Code Review 的團隊回報，它確實能在人類審查者看 PR 之前就抓出真正的問題，但他們希望審查結果更精簡、依變更大小調整、速度更快。Anthropic 也在自家工程團隊的 PR 上跑 Code Review，藉此觀察審查在哪些環節拖慢了自己的工程師。

📊 **這次正式版改了什麼**

- **速度**：多數審查現在快了約 3 倍，從先前的約 20 分鐘降到 6-10 分鐘。
- **品質**：找出更多真正重要的 bug，並用簡潔的文字說明問題、觸發條件與修法。
- **彈性**：管理員可依每個 repository 分別選擇 Quick、Standard（預設）或 Deep 三種審查強度，一般程式碼跑快速模式，關鍵程式碼跑深度審查，每個等級都維持高品質審查。

🧩 **怎麼開始使用**

Code Review 現已對 Team 與 Enterprise 方案正式開放。管理員只要在 Claude Code 設定中啟用 Code Review、安裝 GitHub App，並選擇要套用審查的 repository；開發者這邊則完全不需額外設定，啟用後新開的 PR 就會自動跑審查。

💡 **企業方案有額度優惠**

符合資格的 Claude Enterprise 組織，在 2027 年 1 月 15 日前申請，至少可取得 10,000 美元的 Code Review 額度，額度自申請日起 30 天內有效,詳細條款以官方說明為準。

🎯 **對工程團隊的實務啟示**

如果團隊已經在用 coding agent 加速開發，code review 很可能正在變成新的瓶頸；Code Review 這次把速度壓到 10 分鐘以內，又能依 repository 的重要性分級，對已經用 GitHub 做 PR 流程的 Team／Enterprise 組織來說,是值得直接啟用評估的現成工具,尤其 Enterprise 組織還有額度優惠可以把導入成本降低。

🔗 **來源**
- 標題：Code Review is now generally available
- 作者／機構：Anthropic
- 連結：https://claude.com/resources/articles/code-review-is-now-generally-available

#ClaudeCode #CodeReview #Anthropic #DevOps #AIforDevelopers #GitHubIntegration #SoftwareEngineering #CodingAgents #EnterpriseAI #DeveloperProductivity
