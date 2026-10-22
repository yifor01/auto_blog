---
title: AI agent fixed the bug, but what else did it change?
source: Hacker News
url: https://blog.trailofbits.com/2026/10/21/your-ai-agent-fixed-the-bug-but-what-else-did-it-change/
model: claude-code/sonnet
generated_at: '2026-10-22T21:01:34.686901'
score: 85
---

📌 AI 修好 Bug，但它還改了什麼？Trail of Bits 用兩款插件抓回歸

TL;DR：Trail of Bits 發布 patching-bugs 與 regression-hunt 兩款 Agent 插件，假陽性比基準 Agent 少 25%。

讓 AI Agent 修補安全漏洞聽起來很美好，直到你發現它修完之後，順手破壞了原本正常運作的功能。這正是 Trail of Bits 在今年九月的檢討報告中發現的狀況，而這篇十月的文章，就是他們針對這個問題交出的具體解法。

🤔 **一百三十個已合併的修補，二十一個回歸**

Trail of Bits 與 OpenAI 合作的 Patch the Planet 計畫，已經為廣泛使用的開源專案共同撰寫了數百份安全修補。文章提到，團隊回頭檢視了所有由 Trail of Bits 工程師撰寫、且已被上游維護者合併的修補，在超過 130 個 PR 中確認了 21 個回歸（regression）：16 個功能性、1 個效能、4 個建置／測試相關，沒有一個破壞了安全防護本身。這裡的「回歸」指的是一項變更破壞了原本正確且受支援的行為，而這條路徑是真實使用者或攻擊者可以觸及的。

🧩 **兩款插件的設計原則**

團隊從兩個來源歸納設計原則：一是對所有已合併修補的覆盤，二是工程師撰寫這些修補時留下的數千個 Codex session 紀錄。由此訂出四個原則：盡量用最少的指示把 Agent 導向期望結果；兩款插件都拆成可獨立使用的模組化步驟；每一步都有明確定義的輸入輸出 schema，讓後面的步驟可以驗證前一步的結果而不是只相信摘要；以及最關鍵的一條，每個結論都必須有針對真實部署跑出來的 proof of concept，否則就視為不確定。

regression-hunt 的流程是：沿著變更的 diff 往呼叫端追到真實介面，列出候選回歸，在真實部署上重現每個候選回歸，用一個全新 context 的 agent 重播這個 PoC，最後由一個「仲裁 agent」判斷證據是否足夠證明這真的是回歸，而不是誤報、不完整的修補或原本就存在的 bug。只要有任何一關沒通過，就不會被報出來。若有威脅模型文件，orchestrator 也會把它當作全域上下文傳給每一個步驟，要求各步驟回頭參照威脅模型再下結論。

patching-bugs 則強調三個做法：三臂證明（同一個重現測試要跑三種情境：原始程式碼必須失敗、修補後的程式碼必須通過、把修補完全還原後必須再次失敗，以證明是修補本身而非環境或測試變動修好了問題）；針對違反的安全不變量本身做修補，而非只處理單一個案，讓修補對同類 bug 的變種也有效；以及強制在最後跑一次 regression-hunt，確保每個修補都經過同一套標準流程檢查。

📊 **假陽性少了 25%**

用同一組 21 個已確認回歸的案例，拿 regression-hunt 跟「直接提示 Codex agent 去 review PR 找回歸」的基準比較，regression-hunt 的假陽性少了 25%（95% 信賴區間 14% 到 38%）。另外在一次單輪執行中，58 個候選回歸裡最終確認了 21 個，精確率約 36%。

⚠️ **嚴格證據的代價**

嚴格的證據要求也帶來代價：有些已知的回歸被 regression-hunt 標記為「證據不足」的邊界案例,也就是抓到了可疑訊號卻無法確認。團隊表示下一步會研究為什麼這些案例停留在邊界，並改善蒐證策略，目標是在確認更多真實回歸的同時，給維護者更清楚的「證據不足」資訊。

🎯 **實務啟示**

對正在用 LLM Agent 做程式碼修補或 code review 的團隊，這篇文章給出一個可複製的教訓：光靠「review 這個 PR 有沒有問題」這種開放式提示，雜訊會很大；把「什麼叫回歸」「什麼叫證明」寫成固定的 schema 與通過關卡，才能讓同一套流程跑出可比較、可重複的結果。

🔗 **來源**
- 標題：AI agent fixed the bug, but what else did it change?
- 作者／機構：Trail of Bits
- 連結：https://blog.trailofbits.com/2026/10/21/your-ai-agent-fixed-the-bug-but-what-else-did-it-change/

#AISecurity #BugBounty #CodeReview #AIAgents #TrailOfBits #OpenSource #SoftwareSecurity #RegressionTesting #Codex #DevSecOps
