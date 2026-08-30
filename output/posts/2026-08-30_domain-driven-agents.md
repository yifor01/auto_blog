---
title: Domain-Driven Agents
source: Hacker News
url: https://coldtake.dev/blog/domain-driven-agents
model: claude-code/sonnet
generated_at: '2026-08-30T10:58:36.302264'
score: 70
---

📌 LLM寫程式碼變便宜了，貴的是「決定改什麼」

TL;DR：一位工程師分享如何用 DDD manifest 讓 agent 看懂舊系統的既有語言，而不是在裡面瞎猜。

在全新專案裡叫 LLM 加一個「應徵狀態」欄位，它秒懂交卷。但換成一套已經上線四年的系統，同樣的需求丟下去，模型可能會生出這個概念的第四種拼法，因為那三種既有拼法從來沒有人替系統做過取捨。它會在該直接呼叫的地方硬包一層 adapter，或是在該有 adapter 的地方直接穿透呼叫。每一次錯誤選擇，背後都是一個系統本身從未回答過的問題，模型只能用猜的，而且經常猜錯。

🤔 舊系統的問題不是技術債，是缺乏共同語言

作者指出，brownfield 專案的深度不只在技術層面，底下還藏著第二層：概念混亂、意義缺失、沒有共同語言可以拿來釐清。這正是 LLM 會失足的地方。傳統做法是把 10 到 20% 的工程預算撥給還技術債，但這筆預算其實一直被分成兩半：決定要改什麼，以及把決定敲成程式碼。過去兩者成本相近，但 LLM 讓「敲程式碼」這一半的成本大幅下降，「決定要改什麼」的成本卻沒有變。

🧩 把工作拆成 strategic 與 tactical 兩種角色

作者借用 John Ousterhout《A Philosophy of Software Design》裡 tactical／strategic 的說法，把它用在「誰來動手」的分工上。strategic 的部分是自己做：讀懂系統、判斷什麼該改、確認這個改動真的服務要交付的功能，輸出成一則則 GitHub issue。tactical 的部分交給 AI 系統：透過 skill（一份寫死流程的 markdown 指令，確保「處理一則 issue」每次都用同一套做法執行，而不是取決於當天怎麼描述）與 sub-agent（各自帶著獨立、乾淨的 context，只做一件窄範圍的事，例如實作、資安審查、對照規格審查，最後只回報結果）完成實作，產出可以直接審查的 PR。作者的角色因此變成協調與規劃，審查時仍會留意測試覆蓋率，以及改動會不會傷到下游依賴這段程式碼的其他部分。

🧩 用 DDD manifest 當作 agent 與系統對話的共同語言

支撐這套分工的是 Domain-Driven Design：以 ubiquitous language 與 bounded context，把業務需求直接翻譯成技術語言，讓業務與技術用同一套詞彙溝通。作者讓每個 repository 根目錄放一個 `.workflow.json`，宣告這個 repo 用什麼語言、agent 該先讀哪些目錄、上線前要過哪些檢查，其中一塊專門描述 domain：專案名稱、所屬 bounded context、glossary 的位置、subdomain 型別，以及跟鄰近 context 的每一條邊。以他自己的專案 job-offer-box 為例，前端 repo 的 manifest 會宣告一條邊：對方是誰（`to`）、誰呼叫誰（`direction`）、模型衝突時聽誰的（`owner`）、以及兩者之間的關係型態（`pattern`，從封閉詞彙表挑選，若同時存在兩種模式就標成 `unclassified` 並用 `note` 說明清楚，而不是硬套一個不準確的單一標籤）。每個 context 旁邊還配一份 `CONTEXT.md`，記錄每個詞彙的精確定義與刻意捨棄的同義詞。組合出全部 context 與邊的 `CONTEXT-MAP.md` 則是由腳本掃描所有 repo 自動產生，不是手寫維護的第二份登記表。

💡 為什麼是 DDD，而不是別的方法論

作者強調，這套語言值多少錢，取決於它被寫得多精確：一旦 agent 進入工作流程，這份共同語言不只是給人看的文件，而是我們對模型下需求、以及讀懂模型推理過程時仰賴的介面。manifest 只需要註冊一次、沒有第二份會漂移的登記表，context map 完全是衍生產物而非手寫，這讓「系統該用哪個詞、邊界在哪裡」這件事變得可驗證、可持續更新，而不是隨著時間又腐化成一堆各自表述的命名。

🎯 實務啟示

在把 agent 導入舊系統之前，值得先花力氣把 bounded context 與詞彙表寫清楚，而不是急著把重構任務丟給模型。把「決定改什麼」留給人、把「敲成程式碼」交給 skill 與 sub-agent，同時用一份可驗證、可自動衍生的 domain manifest 當作雙方溝通的基礎，是這篇文章給的具體可複製做法。

🔗 來源
- 標題：Domain-Driven Agents
- 作者／機構：AlarQ
- 連結：https://coldtake.dev/blog/domain-driven-agents

#DomainDrivenDesign #AIAgents #LegacyCode #SoftwareEngineering #TechDebt #LLM #AgenticCoding #SubAgents #SoftwareArchitecture #Refactoring
