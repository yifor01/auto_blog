---
title: How Warp builds self-improving agents on Claude
source: Claude Blog
url: https://claude.com/blog/how-warp-builds-self-improving-agents-on-claude
model: claude-code/sonnet
generated_at: '2026-08-27T17:24:09.188901'
score: 104
---

📌 Warp 如何用 Claude 打造「越用越聰明」的自我改進 agent

TL;DR：Warp 用 skills 架構把人類回饋沉澱成長期記憶，讓 code review agent 持續變聰明。

一個 code review agent 只做對 80% 的工作，看似及格，卻可能是團隊最惱人的存在：每次都要花時間分辨哪些留言有用、哪些是雜訊。這正是 Warp 工程團隊踩過的坑。

🤔 回饋為什麼留不住

Warp 是一款以 Rust、Golang 打造的 AI 終端機與 agentic 開發環境，建構在 Claude Platform 之上；團隊 2020 年創立，創辦人為 Zach Lloyd，累計募資 7,300 萬美元，目前有 80 萬名月活躍開發者使用、56% 的財星 500 大企業採用，累計已有 1,000 萬次 Claude Code session 在 Warp 中執行，每週超過 40 萬次，Warp Agent 對話總數達 4,000 萬次。

團隊內部的 code review agent 一開始問題不小：工程師抱怨它的留言沒幫助、輸出品質差。團隊先試了土法煉鋼的方式，像是根據觀察到的失敗案例手動改寫 prompt，這確實讓輸出變得可用一些，但無法規模化；改善 AGENTS.md 這類 context 檔案也有幫助，卻遠稱不上完整解方。他們最終發現真正的問題在於：任何 agent 收到的回饋，通常會在該次 session 結束後就消失，等於把 agentic loop 裡最關鍵的 context 給丟掉了。

🧩 兩個 skill 組成的自我改進迴圈

Warp 的解法是一套建立在 Agent Skills 之上的框架，讓回饋隨時間持續累積、精煉並強化 agent 的輸出。核心架構是兩個 skill 加上中間的人類回饋：

- 內層／base skill：承載該領域的功能性知識與指令。例如 PR 開啟時，Warp 的 code agent 就是用這個 base skill 加上 context 來產生 review。
- 人類回饋：對 code review 而言可以只是一個讚，但越具體越好。Zach Lloyd 舉例，人類除了肯定「這則留言很有用」，也可以說明「你建議改這個變數名稱，但我們的程式碼慣例是這種全域變數要用特定命名方式」，這種細節能直接告訴 agent 下次該怎麼做對。
- 外層／improver skill：以排程（而非逐任務）方式運作的觀察者 agent，拉取累積的人類回饋，比對 agent 當初的建議與人類實際的反應，再對 base skill 提出一個小而聚焦的修改。

由於 skill 只是純文字檔案，agent 很擅長更新它們；這些更新可審核、可核准、可合併，走一般的 PR／code review 流程，一旦合併，inner skill 下一次執行就會繼承這次改進。Warp 目前已把這個模式套用到整個開源 repo，分別為 spec 撰寫、review、issue triage 建立各自獨立的 agent 與自我改進迴圈。

💡 撰寫自我改進 skill 的實務建議

Warp 團隊整理出幾條心得：寫原則而非規則，Zach 說「要像在指導一個聰明人，而不是在對電腦寫程式」，例如「找出重複的程式碼」這種方向性指引，會比鉅細靡遺的命名規則更有效；解釋「為什麼」能讓 agent 用推理而非死板規則來類推到新情境；讓回饋零摩擦，直接在人們原本工作的地方（例如 PR 或 issue 留言）自動蒐集，不需要額外提交步驟，「門檻太高就收不到回饋，也就無法改進 skill」；skill 檔案要小，善用漸進式揭露（progressive disclosure），把細節放進參照的資源檔或腳本，而不是一次塞進 context；回饋品質比數量重要，但數量也有幫助，少量但具體的資深工程師回饋，價值可能超過大量籠統的讚／踩，因為單純的二元回饋說不出「為什麼」；最後，improver skill 值得投入額外心力，因為除了領域知識部分，它在不同用途間高度可重複使用。

🧪 案例：issue triage agent 的實際運作

Warp 的 issue triage agent 示範了整套機制：每當有人開新 GitHub issue，就會由 GitHub Action 觸發一個 agent，分析該 issue 的複雜度與可行性、標上標籤，並建議修復方向。這個 triage agent 依賴一份 inner skill 檔案，裡面記錄了每個標籤代表的意義，以及動手前該如何研究程式碼庫。

在某次案例中，第一階段的 inner skill 表現不錯，但漏標了一個「ready to spec」標籤，用來標示貢獻者可以開始針對這個 issue 撰寫產品與技術規格。Warp 團隊的一位維護者發現這個缺口，直接在該 issue 上留下回饋，說明他預期的結果以及背後原因，方便 agent 之後吸收。外層 improver skill 則以 Warp 的 agent 編排平臺 Oz 執行，是一個排程的「update triage」agent：登入 GitHub、執行 skill 內附的 Python 腳本拉取近期帶有回饋的 issue、整理成 JSON 摘要，再讀回 context 中。內附腳本本身也是一項最佳實務：skill 可以參照資源檔，而不必每次都重新產生程式碼。

🎯 實務啟示

如果你的團隊也在用 agent 做 code review、issue triage 或其他重複性任務，Warp 的模式給了一個可直接複製的骨架：把領域知識與「如何改進」拆成兩個 skill，讓回饋在使用者原本的工作場域自動被蒐集，並定期用一個 observer agent 把回饋轉成對 base skill 的具體修改。這個做法不需要複雜的訓練管線，重點在於把回饋的生命週期從「一次性、用完即丟」變成「可持續累積的資產」。

🔗 來源
- 標題：How Warp builds self-improving agents on Claude
- 作者／機構：Michael Segner, Anthropic (Claude Blog)
- 連結：https://claude.com/blog/how-warp-builds-self-improving-agents-on-claude

#Claude #Anthropic #AIAgents #AgentSkills #DeveloperTools #CodeReview #Warp #LLMOps #AgenticWorkflow #ContinuousImprovement
