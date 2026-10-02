---
title: How to choose your first Genie Agents for maximum impact
source: Databricks
url: https://www.databricks.com/blog/how-choose-your-first-genie-agents-maximum-impact
model: claude-code/sonnet
generated_at: '2026-10-02T21:41:37.819535'
score: 73
---

📌 第一個 Genie Agent 選錯，後面全部跟著卡關

TL;DR：Databricks 用五項評分指標篩選第一批 Genie Agent，決定導入能否形成正向循環。

2026 年至今已經有超過 100 萬個 Genie Agent 被建立出來，但 Databricks 觀察到真正的問題從來不是「能不能做」，而是「先做哪一個」。選對了，一個被信任的 agent 會帶出下一個需求；選錯了，團隊得花一整季解釋這次試點為什麼不如預期。

🤔 萬能 agent 與花瓶 demo，兩種常見死法

根據 Databricks 在金融服務、能源、零售等領域數十個 Genie Agent 導入案例的觀察，最常讓試點卡住的原因不是準確率，而是一開始就選錯工作流程。第一種是「萬能 agent」：想用單一 Genie Agent 回答整個部門（財務、行銷、營運）的所有問題，範疇一拉大準確率就被拖垮，demo 裡第一個答錯的問題就足以讓信任崩盤。第二種是「花瓶 demo」：為了某次主管會議做出一個亮眼但範疇極窄的 agent，會後沒人有理由再回去用它。

🧩 五項指標打分，一個否決條件

Databricks 提出的篩選方式是針對每個候選工作流程，依 impact（影響力）、demand（需求頻率）、data readiness（資料就緒度）、scope（範疇大小）、governance（治理程度）五個準則各打 1 到 5 分，加總後對照分級：

- 20 到 25 分：可以直接開始建置
- 14 到 19 分：需要先做更多整形（shape it first）
- 14 分以下：目前還不是合適的對象（hold off）

另外有一個不計入分數、但會直接否決的條件：champion。如果沒有業務負責人或主管在積極支持這個工作流程，不管分數多高，都應該先別動手，因為由上而下的影響力才是把一個「表現好」的 agent 變成「被採用」的 agent 的關鍵。低分不代表失敗，而是一個「該先修哪裡」的訊號。

📊 四個案例：高分不保證贏，champion 能補分數

- 一家退休基金為投資團隊建置風險與投資組合問答 agent，五項指標幾乎都接近滿分：範疇侷限、指標經過認證、問題形狀是分析師每天會重複問的，上線前使用率就已經攀升。
- 一家全球工程公司的內部 IT support agent，分數落在「需要整形」的區間，但 CIO 親自開始使用後，採用率隨之跟上，說明一個積極的主管擁護者，能讓一個「夠好」的 agent 走得比「完美但沒有擁護者」的 agent 更遠。
- 一家財富管理公司想做自助分析 agent，看似是「應該要贏」的工作流程，但底層資料有 metadata 缺口，導致答案不一致、使用者信任流失，按評分框架屬於「高影響力但低就緒度」，落在 hold off，但並非永遠不能做，而是需要先補 metadata。
- 一家全國性零售商每天都要重複產出供應與庫存預測，資料本身已經治理良好，團隊用 AI functions 清理資料、用 Genie Code 寫預測邏輯，幾週內就做出可用的 agent，快速被採用，也激發了後續 agent 的靈感。

⚠️ 框架給方向，細節評分標準未揭露

文中沒有進一步說明五項指標各自的量化評分細則，只提供分級後的行動建議；文中提到的 Banco Bradesco、Unilever、Coty、The Trade Desk 等案例也只點出共通點（高頻、高影響力問題加上治理良好的資料基礎），沒有附上具體數據。

🎯 先選對兩個 agent，讓第三個由需求決定

在投入建置前，先用這五個問題快速替候選工作流程打分，並確認有沒有真正會用、會推廣這個 agent 的業務擁護者。團隊會複製前兩個 agent 建立起來的習慣，所以應優先把資源放在評分高、又有人真心想用的工作流程上，讓第三個 agent 的選擇交給真實需求去驗證，而不是提前規劃。

🔗 來源
- 標題：How to choose your first Genie Agents for maximum impact
- 作者／機構：Databricks
- 連結：https://www.databricks.com/blog/how-choose-your-first-genie-agents-maximum-impact

#Databricks #GenieAgents #AIAdoption #EnterpriseAI #DataGovernance #AgenticAI #MLOps #DataReadiness #ChangeManagement #AIStrategy
