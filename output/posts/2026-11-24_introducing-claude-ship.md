---
title: Introducing Claude Ship
source: Claude Blog
url: https://claude.com/resources/articles/introducing-claude-ship
model: claude-code/sonnet
generated_at: '2026-11-24T03:29:54.300077'
pinned: true
---

📌 Claude Ship 公測上線：審查、修復、核准合併一次串接自動化

TL;DR：Claude Ship 把 PR 的審查、修 bug、合併核准接成自動化流程，目標是讓上線速度跟上寫程式碼的速度。

打開過 pull request 的人都懂這種節奏：寫完就跳到下一件事，結果審查意見回來了，只好停下來、挖回舊程式碼、推上修正，再等一次審查跑完，然後還要去找人核准。這個流程之所以行得通，是因為過去每一行程式碼都是人寫的，一個人審查得過來。但現在很多團隊已經用 agent 寫程式了——在 Claude Code 團隊內部，多數程式碼是 Claude 寫的，他們想讓 PR 之後的每一個步驟，也能跟上這個速度。

🤔 寫程式碼變快了，但 PR 之後的流程沒跟上

這正是 Claude Ship 要解決的問題。它今天以公測形式推出，能審查 PR、修復問題，並依照每個團隊自訂的政策決定什麼可以合併。團隊仍能完全控制它在哪裡運作、哪些變更一定要人核准。符合資格的 Claude Enterprise 組織，可在申請後 30 天內使用至少 10,000 美元的 Claude Ship 額度，申請期限到 2027 年 1 月 15 日為止（須符合條款）。

🧩 Code Review、PR Steward、Claude Approvals 三件套

Claude Ship 由已經正式推出（generally available）的 Code Review，加上兩個公測中的新 agent，PR Steward 與 Claude Approvals 組成。Code Review 會從多個角度深入審查 PR 與既有程式碼，收集發現、以對抗式方式驗證這些發現，再分類並發回 PR 留言，每個 repository 可以選擇 Quick、Standard 或 Deep 三種審查深度。PR Steward 負責讓 PR 保持「綠燈」狀態，但設計上不會自己核准或合併 PR，它會處理失敗的 CI 檢查、合併衝突，以及來自 Code Review、其他審查工具或團隊成員的意見，每次推送後都會留言說明改了什麼、如何還原。開發者可以用 @claude 加指令來引導它的工作，或用 @claude stop 讓它停下來。最後，Claude Approvals 會套用團隊寫在 repository 裡的一份核准政策檔案，運作方式類似「更聰明的 CODEOWNERS」：政策允許的話，Claude 可以自行核准常規變更，遇到特定情境則要求更深入的人工簽核。政策可以納入 Code Review 的發現，或團隊自己用自然語言寫的分類器作為判斷依據。Anthropic 建議多數客戶先以「僅觀察」模式啟用，等建立信心後再設定分支保護，要求必須有 Claude Approvals 的綠燈才能合併。

🧩 兩種啟用方式：開發者自己 /ship，或管理員整個 repository 開啟

開發者可以在 Claude Code 中直接對自己的 PR 跑新指令 /ship。準備好的變更一下指令，Claude 就會推送、開 PR、審查變更，並處理回饋與失敗的檢查，協助它更快準備好合併，至於最終能不能合併，取決於開發者的權限與 repository 的分支規則。對管理員與工程主管來說，可以逐個 repository 開啟 Claude Ship，交由整個團隊的 PR 自動套用，不需要每個人手動打 /ship。管理員能分別為每個 repository 開啟 Code Review 與 PR Steward，選擇審查深度、審查時機，並設定花費上限；Claude Approvals 則是在連接的 repository 的預設分支上出現政策檔案時自動啟動，管理員也能隨時關閉。既有的分支保護與必要檢查都能繼續沿用。

📊 Claude Code 團隊自己的數據：合併翻倍，回退少了四成

Claude Code 團隊內部大量使用 Claude Ship。報告指出，在 Claude 的審查只是整體流程一環的情況下，從 6 月到 9 月，他們的 PR 合併數量翻了一倍以上，而被回退（reverted）的比例則下降超過 40%。團隊也分享了一個實際案例：有客戶對 Analytics API 文件產生誤解，以為 Admin key 能拉取 Pro 與 Team 的用量資料，產品經理詢問 Claude Tag 是否已有修正在進行，它便直接開了一個 PR，Code Review 沒發現阻斷性問題，文件審查者簽核通過，Claude Approvals 也放行，這個修正當天晚上就合併了。工程總監 Vatsal Bhatt 表示，Code Review 曾多次在人工審查者接手前就抓到真正的問題，PR Steward 也協助貢獻者修正；高級工程與分析副總裁 Alex Devkar 則提到，PR Steward 讓試行團隊花更少時間處理審查回饋、把更多時間放回開發本身，且可依團隊流程客製化建議方式與回饋組織方式。

🎯 實務啟示

Claude Ship 目前支援 GitHub 上的 repository，適用於 Claude Team 與 Enterprise 方案，用量依 token 計費，帳單會隨 PR 數量與大小、審查深度、審查頻率，以及 PR Steward 的工作量而變動，管理員可以為 Code Review 與 PR Steward 各自設定花費上限；Claude Approvals 本身沒有基本費用，但政策中的分類器會依 token 計費，且只要政策用到 Claude 的審查，即使在觀察模式下也會觸發計費的 Code Review。值得注意的是，目前 Claude Ship 不支援已啟用零資料留存（Zero Data Retention）、HIPAA 設定或客戶自管加密金鑰的組織。如果你的團隊已經在用 agent 寫程式，但審查與合併仍是人工瓶頸，這是一個值得先在單一 repository、觀察模式下試跑的方向。

🔗 來源
- 標題：Introducing Claude Ship
- 作者／機構：Anthropic
- 連結：https://claude.com/resources/articles/introducing-claude-ship

#ClaudeCode #Anthropic #CodeReview #CICD #DevOps #SoftwareEngineering #AIAgents #PullRequest #GitHub #AIAutomation
