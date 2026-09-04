---
title: Which tools do Claude, Codex and Cursor choose? We measured 17k runs to find
  out
source: Hacker News
url: https://armature.tech/blog/which-tools-coding-agents-install
model: claude-code/sonnet
generated_at: '2026-09-04T19:56:00.186376'
score: 83
---

📌 追蹤 1.7 萬次對話：Claude Code、Codex、Cursor 選工具的邏輯一致到嚇人

TL;DR：17k 次實測顯示，不同人設問法常得出相同工具推薦。

一個完全不懂程式的 vibe coder，和一位要求「成本可預期、全託管」的資深工程師，用完全不同的語言向 AI 詢問「該用哪個資料庫」，結果卻得到一模一樣的答案。這個現象促使 armature.tech 發起了目前已知規模最大的 coding agent 工具選擇實測。

🤔 為什麼這件事很重要

文章指出，隨著 agent 接手愈來愈多開發流程，「幫既有程式碼庫挑選要導入的服務」這件事幾乎每個人都會外包給 AI，從沒有軟體背景的 vibe coder 到資深工程師皆然。這不只影響開發者能不能信任 agent 的判斷，對服務供應商而言更是生死攸關：文章引用 Vercel 去年四月公開的資料，指出「超過 30% 的部署是由 coding agent 發起，六個月內成長了 1000%」。換句話說，被 agent「選中」正逐漸成為新的獲客管道。

🧩 怎麼測：17k 場實測、3 個 agent、75 個程式碼庫

團隊建立了兩個沙盒環境，讓不同 agent、不同程式碼庫、不同人設與提示詞交叉組合，觀察 agent 實際如何討論並選擇工具。作者先以資料庫選型做初步實驗：無論是要求「幫我把輸入的資料存下來，下次打開還在」的 vibe coder，還是明確要求「成本可預期、全託管」的資深工程師，Claude Code 與 Cursor 都不約而同推薦 Neon，理由是免費方案、安裝簡單，且不會像 Supabase 那樣在閒置時暫停服務。

看到這個結果一致到不尋常的程度後，團隊決定把測試規模擴大到其他工具類別：總計觀察近 1.7 萬場 session，涵蓋 vibe coder、新創初階工程師、企業資深工程師等不同人設，1,163 種提示詞變化，75 個程式碼庫，測試對象是 Claude Code、Codex、Cursor 三款 agent。與一般評測不同的是，這次是讓 agent 真的把解決方案實作出來，而不只是提出建議。

📊 結果全公開：排行榜與完整 trace

文章表示，團隊公開了每個類別的彙總結果與排行榜，也釋出了所有觀察紀錄，包括完整的使用者提示詞、模型的 thinking trace，以及 agent 實際套用的程式碼 diff。這篇貼文在 Hacker News 上引發熱烈討論，累積 286 點與 140 則留言。

💡 這件事對「工具選型」意味著什麼

如果不同 agent、不同人設在同一情境下持續收斂到相同答案，代表 agent 的工具推薦可能不只是隨機生成的建議，而是有一套相對穩定的判斷邏輯，這既提升了使用者對 agent 判斷的可信度，也讓工具／服務供應商必須開始正視「如何被 agent 選中」這個新的行銷戰場。

🎯 實務啟示

對工程師而言，這提醒你在接受 agent 的技術選型建議前，仍值得核對它給出的具體理由（例如免費方案、是否會被暫停服務），而不是照單全收；對正在打造開發者工具或基礎設施服務的團隊來說，被 coding agent「看見並選中」很可能會變成不亞於傳統 SEO 的新戰場。

🔗 來源
- 標題：Which tools do Claude, Codex and Cursor choose? We measured 17k runs to find out
- 作者／機構：screm（Hacker News；armature.tech）
- 連結：https://armature.tech/blog/which-tools-coding-agents-install

#CodingAgents #ClaudeCode #Codex #Cursor #AIAgents #DeveloperTools #ToolSelection #DatabaseTools #AIExperiment #SoftwareEngineering
