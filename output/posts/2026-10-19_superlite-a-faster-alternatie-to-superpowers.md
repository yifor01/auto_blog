---
title: 'Superlite: A Faster Alternatie to Superpowers'
source: Hacker News
url: https://contextfirst.blog/superlite-hand-an-agent-a-spec/
model: claude-code/sonnet
generated_at: '2026-10-19T21:49:42.233705'
score: 71
---

📌 Superlite：讓 Coding Agent 真正平行自主作業

TL;DR：一款 Claude Code 外掛，用任務圖把工作拆成可並行的區塊，減少人工核准次數來加快自動化開發。

你有沒有試過把 spec 丟給 agent，想說可以安心去做三明治，結果回來時它還卡在「請核准第一節設計」？Hacker News 上一篇熱門貼文，就是從這個挫折出發，寫出了一個專門解決「等待」問題的外掛。

🤔 **問題出在哪：太多人工關卡、太少平行度**

作者原本大量使用 superpowers，一款強調人類緊密參與每一步的協作式 workflow，並承認它在這方面做得很好。但當他已經明確知道自己要什麼時，大部分時間反而耗在「workflow 等自己」。作者自述分析後發現時間主要花在五個地方：每個功能平均 8 到 12 次人工核准關卡；嚴格序列化執行（一個實作者做完才輪到下一個，審查者才接手）；每個任務後都要重新審查並進入修正迴圈；完整測試套件被多個 skill 重複執行；以及放在關鍵路徑上、寫程式速度只有 Sonnet 一半的 Opus 子 agent。作者強調這些設計本身都是合理的安全網，只是疊加起來會讓「交出去就等著收成品」變得不可能。

🧩 **一次核准、任務圖、分級 agent、規則用程式碼鎖死**

Superlite 的運作方式是先把需求分類：單純的 typo 直接修，不寫設計文件；既有流程的變更在對話中簡短說明設計；全新專案則一次問完最多四個問題，產出一份設計與計畫文件，使用者只核准一次。核准之後，系統只在遇到破壞性、對外公開或資安敏感的操作時才會再次停下來詢問。

計畫本身是一張任務圖：每個任務列出它擁有的檔案、要消費與產出的介面、以及必須通過的測試。沒有共用檔案、也沒有相互依賴的任務可以同時執行，任務圖的寬度決定了並行規模；作者提到在其基準測試中曾經同時有 18 個 agent 在跑。

Agent 的分工類似一個小型組織：Opus 負責規劃與派工，但不被允許碰程式碼；Sonnet 負責大多數任務的實作；Haiku 只處理定義完整、不在關鍵路徑上的機械性小任務；Sonnet 負責審查交付包；另一個全新的 Opus 最終審查者只讀取由這次執行日誌產生的審查包、只回報問題，不允許動手修正；修正工作則依問題成因的明確程度，分成三個層級的「只修 bug」agent 處理。

作者特別提到一個教訓：光是在 prompt 裡用大寫加粗寫「協調者不準改程式碼」沒有用，agent 讀完照樣會動手改。因此這些規則最終都靠程式碼層級的 hook 強制執行，例如阻止協調者編輯專案程式碼、把直接執行的 pytest 或 npm test 自動轉成背景執行、禁止任何人按名稱砍掉行程，以及計畫必須先通過 `lint --stable` 才能開始執行。每次執行的 token、成本與時間都會被記錄，用來預測下一次執行，並在花費達到預算 70% 時提示使用者。

💡 **不是要取代 superpowers，是另一種場景的工具**

作者反覆強調 superlite 並非 superpowers 的競品，而是針對「想自主開發、追求速度」這種不同場景打造。如果想一步步掌控每個決策，仍該用 superpowers；如果只想交出 spec、拿回成品，才適合 superlite。兩者因為共用 skill 名稱、都會在啟動時注入 context，官方建議不要在同一個 session 裡同時啟用。

⚠️ **使用門檻與限制**

需要 Claude Code、git、Python 3.10 以上（供 superlite 自身工具使用，建置的專案本身可以是任何語言），以及 bash（Windows 上用 Git Bash）。文中提到的效能數字，像是 34 分鐘建置、12 分鐘花在審查迴圈、單檔佇列 21 次派工等，都是作者自己的基準測試結果，屬於作者宣稱，尚未見第三方驗證。

🎯 **實務啟示**

如果團隊已經很清楚要做什麼、只是卡在人機核准的等待時間，這種「先分類任務複雜度、再決定要不要停下來問」的設計思路值得參考；而用程式碼 hook 而非 prompt 文字去強制規則，是個值得借鏡的做法，因為 prompt 層級的約束對 agent 來說終究只是建議。

🔗 **來源**
- 標題：Superlite: A Faster Alternative to Superpowers
- 作者／機構：iheatuchriswogu（Hacker News 發文者）
- 連結：https://contextfirst.blog/superlite-hand-an-agent-a-spec/

#ClaudeCode #AIAgents #DeveloperTools #Automation #ParallelComputing #AgenticWorkflow #OpenSource #SoftwareEngineering #LLMOrchestration #HackerNews
