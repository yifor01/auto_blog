---
title: The components of agent memory
source: Anthropic Engineering
url: https://www.anthropic.com/research/components-of-agent-memory
model: claude-code/sonnet
generated_at: '2026-11-06T22:13:16.512131'
pinned: true
---

📌 【Anthropic 研究】Claude 如何學會「做夢」整理記憶

TL;DR：Anthropic 拆解 agent 記憶的運作方式，讓 Claude 透過離線「夢境整理」學會判斷哪些經驗值得留下。

哲學家 Kierkegaard 說，人生只能回顧地理解，卻必須向前地活。Anthropic 在設計 AI agent 的記憶機制時，遇到了幾乎一樣的難題：agent 要怎麼在事情發生的當下，就判斷這段經驗未來會不會有用？

🤔 **人腦怎麼決定什麼該記住**

人類的海馬迴（hippocampus）會在經驗發生的當下快速編碼記憶，但真正被鞏固成長期知識的,只是其中一部分。這個鞏固過程主要發生在睡眠與安靜休息時：海馬迴會重播（replay）近期經驗，逐漸將其蒸餾、整合進儲存大部分知識的新皮質（neocortex）。Letta 與加州大學柏克萊分校的研究者提出的 sleep-time compute（睡眠運算）概念,也就是模型利用互動之間的閒置時間重新整理既有的 context，啟發了 Anthropic 對 agent 記憶的設計。

🧩 **從記錄日誌到「做夢」整理**

Agent 在工作時會把過程留在 log 或 transcript 裡，Claude 可以在事件發生當下，先標記 session log 中「顯著」的片段,或是直接寫進記憶檔案（例如一個記憶筆記資料夾）,方便之後查找。但更進一步的做法,是讓 Claude 利用離線時間反思這些 log，修正錯誤、產出新筆記或建立新的記憶表徵，這個過程被稱為「dreaming（做夢）」。Anthropic 發現，dreaming 已成為讓 Claude 擁有有效記憶的實用工具。

此外，寫下記憶本身往往是一種「預測」：記下一條驗證過的事實，等於預測未來的某次 session 會需要直接信任這個事實，不必重新查證。

📊 **從亂猜到建立學習迴圈：CL-Bench 的世代差異**

在 Continual Learning Bench（CL-Bench）1.0 的資料庫問答任務中，Claude 每次以全新 session 開始作答，只能透過一個持續存在的記憶資料夾取得上一輪留下的檔案。不同世代模型展現出明顯差異：Claude Sonnet 4.6 只走到「產生猜測理論」這一步，記憶資料夾裡散落著幾份未經驗證的猜測；Claude Opus 4.7 開始把筆記整合成單一參考文件，並標記哪些事實已確認、哪些還存疑；Claude Sonnet 5 則會在答案被判定後標記「已確認」，答錯時寫下修正。真正「閉環」的是 Claude Opus 5,它的記憶條目通常同時包含規則、該規則被驗證的依據、先前答案，以及明確的陷阱警告。Claude Opus 5.5 與 Claude Sonnet 5.5 同樣能閉環，並用記憶捕捉經驗證的規則，表現與 Opus 5 相近，但這兩者在沒有記憶輔助時的基礎表現本來就略高一些。

📊 **寶可夢實測：413 份筆記 vs. 9 份筆記**

Anthropic 也用《Pokémon Red》遊玩任務測試 Claude 判斷「顯著性」的能力。比較 Claude Sonnet 3.7 與 Claude Fable 5 在遊戲進行到約一萬步時的記憶資料夾，兩者策略截然不同：Sonnet 3.7 假設什麼都可能重要，幾乎每場戰鬥、每個道具、每個 NPC 都寫一個檔案,最終寫出 413 份記憶檔案、分散在 225 個資料夾裡,但只拿到一個徽章。Fable 5 則只在兩個資料夾裡寫了九份檔案，再加一份頂層的 global.md，卻拿到四個徽章。

💡 **問題不在記得多，而在記得對**

Sonnet 3.7 的困境在於：遊戲狀態持續變化，它詳細記錄的內容很快就過時，agent 因此得花愈來愈多時間和資源翻找舊記憶,而不是真正推進遊戲。像是在第一萬步附近,它甚至連續開了四個「master」記憶資料夾，在接下來 17 步裡新建六份檔案、刪掉九份,卻完全沒有在遊戲裡採取任何行動。相對地，Sonnet 3.7 記下的許多資訊（例如玩家身上多少錢、所在地圖位置）其實每個回合螢幕上都讀得到,屬於冗餘資訊；而 Fable 5 把力氣花在「遊戲不會主動告訴你」的東西上,例如策略、計畫與驗證過的規則,這些內容唯有 Claude 主動寫下才會存在。

🎯 **實務啟示**

對正在設計 agent 記憶系統的工程師來說，這個案例給出一個清楚的判準：值得寫進記憶的,應該是「螢幕讀不到、下次還得重新推導」的判斷與規則，而不是隨手可得的狀態資訊。與其讓 agent 無差別記錄一切,不如讓它在離線時間反思、整併、驗證已有的記憶,這正是 dreaming 機制想解決的問題。

🔗 **來源**
- 標題：The components of agent memory
- 作者／機構：Anthropic
- 連結：https://www.anthropic.com/research/components-of-agent-memory

#Anthropic #Claude #AIAgents #AgentMemory #LLM #SleepTimeCompute #ContinualLearning #AIResearch #MemoryManagement #AIEngineering
