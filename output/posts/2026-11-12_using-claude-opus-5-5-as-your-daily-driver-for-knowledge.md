---
title: Using Claude Opus 5.5 as your daily driver for knowledge work
source: Claude Blog
url: https://claude.com/resources/articles/using-claude-opus-5-5-as-your-daily-driver-for-knowledge-work
model: claude-code/sonnet
generated_at: '2026-11-12T22:51:34.510541'
pinned: true
---

📌 Anthropic 官方建議：Opus 5.5 該是你每天開的那個模型

TL;DR：Anthropic 建議把 Opus 5.5 設為日常知識工作主力，因為它常能用更少步驟完成任務，抵銷掉更高的單位 token 價格。

如果你或團隊一直把 Sonnet 當成預設選項，只有遇到「重要分析」才切到 Opus，Anthropic 這次的建議是：這個習慣該重新檢討了。Claude Opus 5.5 現在已是 Pro、Max、Ultra 與 Team 方案中 Claude 的預設模型。

🤔 **四個模型，分工越來越細**

Anthropic 目前的模型陣容依用途分層：

| 模型 | 適合場景 | 價格（每百萬 token，輸入/輸出） | 相對速度 |
|---|---|---|---|
| Claude Haiku 5.5 | 快速查找、高量級的重複性工作 | $0.10 / $0.50 | 最快 |
| Claude Sonnet 5.5 | 需求明確、範疇清楚的任務，產出成品文件/簡報/表格 | $2 / $10 | 快 |
| Claude Opus 5.5 | 多數知識工作：研究、分析、需要判斷力的成品 | $4 / $20 | 中等 |
| Claude Fable 5.2 | 最具野心、開放式的技術工作，如程式開發、金融、科學 | $8 / $40 | 中等 |

值得注意的是 Haiku 5.5 是該系列第一個具備「effort 控制」的 Haiku 模型，可以先要求它多想一輪，再決定要不要換大模型；而 Sonnet 5.5 若被拉到 Extra high 或 Max effort，單次任務成本會逼近 Opus 5.5，這時 Anthropic 建議直接換模型，而非把 Sonnet 往上硬推。

🧩 **Opus 5.5 在文件、研究、金融與圖表上的表現**

Anthropic 描述 Opus 5.5 會「精確遵循指令、不偏離範疇」，產出的表格、簡報、文件往往不需要太多修改，對數字與來源也更謹慎。在一項內部研究測試中，Opus 5.5 僅憑一份網頁快照（其中財報頁面不易找到）撰寫公司季度績效報告，自動評分機制會逐一核對報告中每個數字與引述是否出現在該快照頁面中，只要捏造一個數字或引述就判定失敗。結果是在 18 份不同 effort 設定下產出的報告中，16 份通過。

在財務分析上，Opus 5.5 能準確讀取密集的財報文件、財務模型與圖表，並在整個專案或交易過程中維持上下文。Anthropic 舉的內部測試案例，是分析兩家虛構人資軟體公司的合併案：Opus 5.5 建立 Excel 財務模型並轉成高階主管簡報，耗時 63 分鐘（相較 Opus 5 同一任務的 93 分鐘），成本減半，分析更周全，簡報也更易讀。

投資公司 Walleye Capital 的量化研究工程負責人 Frank Corrao 表示，在較高 effort 設定下，Opus 5.5「發現我們自己的指示中分鐘索引少算了一位，並主動修正，還提到這樣做可能會因此在評分上被扣分。它是對的，而過去沒有任何模型抓到並處理過這個問題」。Ramp 的資深軟體工程師 John Ruelas 則說它「寫得像個好同事，會遵守我們的寫作規則」。

在視覺理解上，Anthropic 稱 Opus 5.5 是目前最擅長視覺的 Opus 模型，即便在最低 effort 設定下，讀取密集圖表數值的準確度也超過 Opus 5 在最高 effort 下的表現。

💡 **該丟掉的舊提示習慣**

Anthropic 給出幾項具體建議：直接要求「完成的檔案」而非「大綱」；把長文件、長計畫交給它找錯誤與不一致；拿不確定答案的研究問題讓它整理來源並寫成報告；把 Claude 接到工作檔案與系統（connector），而不是手動貼上內容；在第一句話就說清楚目標、成品樣貌與何時該停下來詢問。另外，由於 Opus 5.5 的思考過程預設一直開著，Anthropic 建議刪掉「think hard」「think carefully」這類提示詞，並從 Medium effort 開始嘗試，因為在內部的程式與知識工作評測中，Opus 5.5 的 Medium 已能匹配甚至超越 Opus 5 的 High。

🎯 **實務啟示**

對工程團隊而言，這次更新的重點不是「Opus 比較強」，而是「單次任務總成本可能更低」，因為更強的模型常能少走幾步就完成任務。建議團隊重新評估目前把哪些工作留給 Sonnet、哪些留給 Opus 的分工規則，並優先在研究、財務分析、圖表密集的工作流程中試跑 Opus 5.5，再視結果決定是否要全面調整預設模型。

🔗 **來源**
- 標題：Using Claude Opus 5.5 as your daily driver for knowledge work
- 作者／機構：Anthropic
- 連結：https://claude.com/resources/articles/using-claude-opus-5-5-as-your-daily-driver-for-knowledge-work

#Anthropic #ClaudeOpus #LLM #KnowledgeWork #AIProductivity #PromptEngineering #AIModels #EnterpriseAI #ClaudeAI #GenerativeAI
