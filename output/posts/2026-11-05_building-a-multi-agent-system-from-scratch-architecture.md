---
title: 'Building a Multi-Agent System from Scratch: Architecture Patterns'
source: Hacker News
url: https://kadhar.dev/blog/multi-agent-systems-from-scratch
model: claude-code/sonnet
generated_at: '2026-11-05T23:05:25.902365'
score: 84
---

📌 多代理系統的三種架構與四個地雷

TL;DR：單一agent好demo，多代理系統真正的工程挑戰在協調，不在推理。

一個agent五分鐘就能demo成功，但把它變成兩個agent，你多出來的不是能力，而是一個全新的協調問題。而這正是多數工程精力消耗的地方，只是demo從來不會告訴你這件事。

🤔 **背景：為什麼要拆成多個agent**

作者先提到自己之前寫過一個單一agent的案例，把自然語言的餐廳查詢轉成結構化搜尋條件的agent，之所以運作良好，是因為問題形狀單一：理解查詢、呼叫工具、格式化答案。但多代理系統是不同的動物，一旦超過一個agent，就同時疊加了協調問題與推理問題，而協調正是幾乎所有真正工程力氣投入的地方。拆成多個agent的理由，類似於把程式碼拆成函式：一個agent同時處理檢索、領域推理、驗證、格式化四件事，通常每件事都做得比專門負責單一任務的四個agent差一點；責任越窄，system prompt越短，行為也越可預期、越好評估。

🧩 **三種架構模式**

- **Orchestrator-Worker**：最多人第一個想到的模式，對應人類主管分派工作的直覺。一個orchestrator agent接收任務、拆成子任務，分派給各自專精的worker agent，worker之間互不對話，只對orchestrator回報，最後由orchestrator彙整結果。流程大致是：Task → Orchestrator → 分派給Worker A（研究）、Worker B（程式碼生成）、Worker C（驗證） → Orchestrator彙整 → 最終答案。這適合「任務拆解在事前就很清楚」的情境，orchestrator只負責規劃與彙整，prompt小、行為可預期，代價是orchestrator會變成瓶頸：所有context都要經過它，一旦拆解判斷錯誤，下游所有worker都會繼承這個錯誤。
- **Blackboard**：拋開嚴格的層級關係，agent們對一個共享狀態（「黑板」）進行讀寫，各自判斷自己何時該貢獻什麼，通常有個輕量排程器根據黑板當下內容決定下一個該行動的agent，但沒有任何單一agent擁有「整體計畫」。適合解法路徑事前根本不知道的情境，例如除一個隱晦的production問題：一個agent提出假設，另一個收集證據支持或反駁，第三個再批判整個推理過程。代價是這類系統很難推理與測試，沒有單一地方存放「計畫」，除錯一個壞結果等於要事後重建整串讀寫序列，更接近除race condition而不是除function call stack的bug。
- **Pipeline**：三者中最簡單，也是作者在工作流程本身已知且可重複時預設採用的模式。固定順序的專職agent鏈，每個agent把輸出交給下一個：Input → Retrieve Agent → Extract Agent → Validate Agent → Format Agent → Output，沒有分派邏輯、沒有共享暫存空間。這是三種模式中最容易評估的，因為每個階段都有明確定義的輸入輸出契約，可以獨立測試與版本化每個agent。限制是僵化：如果任務不能拆成固定序列，例如第三步有時需要回頭重做第一步——pipeline會直接失敗，或是你會不斷在上面補綴ad hoc的分支邏輯，最後悄悄變成一個多了幾步的orchestrator。

挑選原則很直接：如果能在開始前就把拆解寫成checklist，用pipeline；如果拆解本身可知但細節取決於輸入，用orchestrator-worker；如果在agent開始找答案前根本不知道解法路徑，用blackboard，並預留更多時間做評估。

📊 **demo看不到的四種失效模式**

- **無限委派迴圈**：兩個都能判斷「這不是我的工作，退回去」的agent，有時會把任務無限次來回丟給對方——orchestrator分給worker，worker覺得需要澄清就丟回orchestrator，orchestrator收到不清楚的請求又丟出去。單獨測試每個agent時完全看不出這個問題，因為迴圈只存在於系統層級。
- **重複呼叫導致的失控成本**：每一次agent對agent的呼叫都是一次model call，都要花錢花時間。一個三個agent的blackboard系統，如果每次寫入後都重新檢查整個黑板，一個任務可能變成數十次model call，開發時單筆單筆盯著transcript看不出來，帳單上卻看得很清楚。
- **並發寫入衝突**：兩個agent同時對共享狀態動作時，兩個worker同時更新同一筆紀錄，兩個blackboard agent同時想「解決」同一個開放問題——會出現跟不受保護的race condition同類的bug，只是這次寫入者是語言模型而不是執行緒，重現難度更高。
- **錯誤在agent之間擴散**：作者認為這是最陰險的一種。如果Agent A產生幻覺並把輸出傳給Agent B，Agent B沒有辦法分辨這是幻覺還是已驗證的事實，它只看到context window裡的文字並當作真的來推理。單一agent系統裡，一次幻覺只是一個錯答案；多代理系統裡，一次幻覺會變成每個信任它的下游agent都疊加放大的輸入。

💡 **真正有效的防護：寫進程式碼裡的硬限制**

作者強調，上述失效模式都不是靠「寫更好的prompt」解決的，而是靠程式碼層面、agent無法繞過的硬限制：對委派深度設定硬上限（他的經驗是3到5次跳轉），超過就升級處理而不是繼續迴圈；對每個任務設定集中追蹤（不是分散在各agent）的token或金錢預算上限，一旦碰到上限，任務就停止，不給「再試一次」的機會。

⚠️ **這是一人之見，但在HN引起共鳴**

這篇文章在Hacker News上獲得60點與23則討論，反映出不少工程師在多代理系統上踩過類似的坑，但內容終究是作者個人實戰經驗的整理，沒有量化對照數據，採用時仍需依照自己系統的實際情況驗證。

🎯 **實務啟示**

在設計多代理系統之前，先問自己任務的拆解能不能寫成checklist：能就用pipeline，拆解可知但細節看輸入就用orchestrator-worker，完全不知道解法路徑才上blackboard。無論選哪種模式，委派深度上限與集中式的token/成本預算都該在上線前就寫進程式碼，而不是等帳單或無限迴圈出現後才補。

🔗 **來源**
- 標題：Building a Multi-Agent System from Scratch: Architecture Patterns
- 作者／機構：kadharmfn
- 連結：https://kadhar.dev/blog/multi-agent-systems-from-scratch

#MultiAgent #AgentArchitecture #AIEngineering #Orchestration #LLMOps #SoftwareArchitecture #AgenticAI #SystemDesign #AIAgents #Production
