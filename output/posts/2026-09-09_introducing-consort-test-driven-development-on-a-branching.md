---
title: 'Introducing Consort: Test-driven development on a branching database'
source: Databricks
url: https://www.databricks.com/blog/introducing-consort-test-driven-development-branching-database
model: claude-code/sonnet
generated_at: '2026-09-09T20:05:03.897029'
score: 82
---

📌 Consort:把 TDD 的紅綠燈,搬到可以分支的資料庫上

TL;DR:Databricks 開源 Consort 框架,讓多個 AI agent 分工協作,在 Lakebase Postgres 的分支資料庫上跑完整的 TDD 循環。

過去 25 年,軟體開發的每個環節幾乎都能被版本控制、容器化、當成程式碼一樣管理,唯獨資料庫是那個怎麼都不肯配合的龐然大物。團隊只能用 mock 取代真實資料庫、共用一臺 staging 機器,並把 schema 變更當成一場小心翼翼的儀式。Databricks 這次要解決的,正是這個長年的痛點。

🤔 為什麼資料庫測試一直被推到「外圈」

文章指出,對真實資料庫做整合測試過去屬於外圈(outer-loop)工作:每個單元測試都要重新建立資料庫、灌入 schema 與資料、處理版本控制,成本太高,所以沒人真的這麼做,團隊轉而用 mock 物件替代。但 mock 會隨時間 drift,越花力氣維護,越難反映資料庫真實行為。Lakebase Postgres 的 copy-on-write 分支能力改變了這個前提:建立一個隔離的真實資料庫分支,耗時幾乎是常數,不受資料量大小影響。這讓工程師寫下的第一個 TDD 測試,就能直接對著一份真實資料的分支跑,測試做完整個分支直接丟棄,不影響團隊其他人。

🧩 把 Scrum 角色變成 Agent,分兩條線協作

Consort 是開源的 agentic 開發框架,以 Lakebase 分支作為 test-driven build 的基礎。團隊裡的每個角色——product owner、spec author、architect reviewer、DBA、test strategist,以及 navigator/driver 配對——都變成一個 agent,由一個 conductor 領導,共同組成一個「consort」(合奏團)。

工作分兩條線進行:一條是 spec-first 的設計線,先把意圖談定並凍結;另一條是 build 線,對著真實資料庫的 live 分支,跑完整的紅/綠/重構循環。由於 schema 現在以版本化的 migration(依技術棲位選用 Alembic、Flyway 或 Knex)形式移動,schema 變更會與依賴它的程式碼一起移動、一起合併——合併的是 schema,不是資料本身。

搭配的還有一個 VS Code 外掛,能同時顯示配對的 Git 分支與 Lakebase 分支,把程式碼與 schema 的變更放進同一個 diff 畫面;另有一個可觀察性儀表板,即時顯示每一輪裡每個角色的 prompt,以及它產出的成品如何交給下一個角色使用。每個關卡,工程師都能親自檢視在自己分支上跑的真實軟體,再決定是否放行。

💡 讓多 agent 協作不失控的關鍵:限縮 context 範圍

文章特別強調,Consort 給每個 agent 的是一份範圍受限的 context package:要通過的測試、設計需求,以及這些東西存放的位置,而不是讓 agent 在整個程式碼庫裡漫無目的搜尋。文中直言,「沒有範圍限制的存取,正是 agent 會 drift 的原因」,agent 會在程式碼裡反覆摸索,直到忘了 DRY 是什麼。

Architect 角色會在任何程式碼寫出來之前先審查 spec,把跨功能需求、分層設計,以及 DRY、SRP、SOLID 等模式套進去,這也是為什麼最終成果不會全部塞進一個檔案。當團隊想探索多種做法時,Consort 還能針對同一個 story,在各自獨立的資料庫分支與 git worktree 上跑平行實驗,讓工程師嘗試多個方案後,保留較好的那一個。

⚠️ 開發期仍需綁定 Lakebase 分支能力

Consort 的 TDD 循環建立在 Lakebase 的 copy-on-write 分支能力之上。文章說明,完成後的應用程式本身可以在一般 Postgres 上運行,不需要保留分支工作流,但開發期間要跑這套流程,仍需要用到 Lakebase(可透過 Free Edition 取得)。Consort 本身是開源、社群支援的專案,而非附帶 SLA 的平臺內建功能,目前仍在尋找更多貢獻者與 codeowner。

🎯 實務啟示

若團隊已經在用 Lakebase Postgres,Consort 提供了一套現成的「AI agent 分工 + TDD + 資料庫分支」協作範本,值得評估能否取代目前用 mock 物件做整合測試的做法。即使暫時不導入整套框架,「用 copy-on-write 分支取代 mock,讓 schema migration 與程式碼一起在 PR 裡被審查」這個做法本身,也值得作為資料庫版本控制實務的參考方向,尤其適合正在苦於 staging 環境衝突或 schema 變更風險的團隊。

🔗 來源
- 標題:Introducing Consort: Test-driven development on a branching database
- 作者/機構:Databricks
- 連結:https://www.databricks.com/blog/introducing-consort-test-driven-development-branching-database

#Databricks #Consort #TDD #Postgres #Lakebase #AgenticAI #OpenSource #SoftwareEngineering #DevOps #DatabaseBranching
