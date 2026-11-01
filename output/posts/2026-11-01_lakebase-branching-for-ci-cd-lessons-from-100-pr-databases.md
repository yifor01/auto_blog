---
title: 'Lakebase branching for CI/CD: lessons from 100 PR databases'
source: Databricks
url: https://www.databricks.com/blog/lakebase-branching-cicd-lessons-100-pr-databases
model: claude-code/sonnet
generated_at: '2026-11-01T21:20:49.351990'
score: 68
---

📌 Databricks Lakebase：PR 資料庫從 20 分鐘縮到 1 分鐘內

TL;DR：Snorkel AI 用 Lakebase 的 copy-on-write 分支取代資料庫還原，CI 環境建置從 20 分鐘降到 1 分鐘內。

CI 測試最怕兩件事：資料不夠真實、環境準備太慢。Snorkel AI 的案例剛好同時踩中這兩個痛點，而他們的解法，是把資料庫當成 Git 一樣分支出去。

🤔 **每個 PR 都要一份真實資料庫，但還原一次要 20 分鐘**

Snorkel AI 打造給 AI 團隊使用的資料開發工具，CI pipeline 建構在 Kubernetes 上，每個開啟的 PR（以及臨時的 commit）都會拿到自己的 Kubernetes namespace，開發者在裡面部署分支並跑完整測試套件。這些測試只有在對照真實資料時才有意義，但 Snorkel 的正式環境資料庫是一個 Amazon Aurora PostgreSQL 叢集，每個 PR namespace 還原一份獨立拷貝要花大約 20 分鐘，在一天內會開出大量 PR 的團隊裡，這個速度完全跟不上需求。改用共享的 staging 資料庫、裁剪過的 fixture 或合成資料，又會把「用真實資料測試」原本要解決的問題帶回來：測試互相干擾、schema 過時、只有在真實資料形狀下才會出現的 bug。

🧩 **用 copy-on-write 分支取代「複製整份資料庫」**

Lakebase 是 Databricks 推出的 serverless Postgres，儲存與運算分離，並支援分支：可以從任何時間點建立一個獨立、可寫入的資料庫分支，概念上就像建立一個 Git 分支。分支採用 copy-on-write：建立分支只是一個 metadata 操作，當下不會複製任何資料，新分支會共用父分支既有的儲存頁面，只有分支本身修改到的頁面才會寫成新的儲存內容。Snorkel 的 CI 流程因此可以拆成四步：首先透過 AWS DMS，把正式環境的 Aurora 資料庫做一次完整載入，再持續進行 CDC（change data capture），讓 Lakebase 的 main 分支隨時維持在落後正式環境約 2 分鐘以內的狀態（搭配 full LOB mode 處理 10 到 20MB 大小的 JSONB 欄位）；接著每當有人開 PR，CI pipeline 就呼叫 Lakebase API 從 main 建立一個新分支並設定過期時間，在 1 分鐘內就能把連線資訊交給 PR namespace；測試在這個獨立分支上跑 migration、寫資料、改 schema，完全不影響正式環境、main 或其他 PR；PR 合併或關閉時刪除分支，若清理步驟沒有被觸發，分支也會因為 TTL 到期而自動失效。安全性方面，正式資料從 Aurora 到 Lakebase、再到 CI 叢集全程走私有網路，不經過公開網際網路；身份管理也依使用者類型拆開，互動除錯的開發者走 Okta SSO，而無人值守的 CI pipeline 則以 service principal 的身份運作。

📊 **為什麼這套做法能撐得住規模**

Copy-on-write 讓分支建立近乎瞬間完成：從一份約 1TB 的正式環境拷貝建立分支，與從一份 1GB 資料庫建立分支耗時差不多，都是以秒計算，而不是還原所需的 20 分鐘。這也讓分支變得便宜：每個分支只為自己修改的部分增加儲存空間，對 Snorkel 來說，每個 PR 分支額外佔用的儲存大約是 5 到 10GB；運算資源則依分支計費且閒置時會自動縮到零。長期維持低成本的關鍵在於 TTL：分支會保留它建立當下的資料版本，main 持續被正式環境的變動更新，分支存在越久，保留的舊頁面就越多，儲存量也隨之增加，而每個 CI 分支都設定 TTL，能確保用完即丟，讓整體儲存量維持在「正式環境大小加上活躍 PR 的變動量」左右。

💡 **同一套模式也能套用在 AI agent 身上**

文中也提到，需要一份可拋棄正式環境拷貝的，不只是 PR namespace。會寫 SQL、跑 migration、改資料的 AI agent 同樣需要一個安全的試驗場，而 copy-on-write 分支正好提供這個場所：每個 agent 任務都能拿到自己的 main 分支，讀寫甚至改 schema 都不會動到正式環境或其他 agent 的工作；因為建立分支耗時以秒計、儲存只隨變動量成長、運算閒置歸零，同時跑數十個 agent 的成本大約只等於它們實際改動的資料量，而不是數十份完整資料庫；團隊可以先檢視 agent 在分支上做了什麼，覺得不對就直接刪除分支，不需要額外的回滾流程；TTL 同樣能自動清掉被遺棄的 agent 分支；agent 也能比照 CI pipeline，以 service principal 搭配短期 OAuth token 運作，讓每一次查詢都能在稽核紀錄中被追蹤。

⚠️ **TTL 紀律仍是關鍵前提**

這套架構的效益高度仰賴 TTL 設定被確實執行：一旦分支因故長期存活，隨著 main 不斷同步正式環境的變動，分支會持續保留越來越多的舊頁面，儲存成本也會慢慢墊高，等於把 copy-on-write 原本該省下的成本吃回去一部分。換句話說，這不是一套「裝了就自動省錢」的機制，而是需要搭配明確的過期策略。

🎯 **實務啟示**

如果團隊的測試高度依賴真實資料形狀、又苦於共享 staging 環境互相干擾或資料庫還原太慢，Lakebase 這種支援 copy-on-write 分支的 serverless Postgres 架構值得評估；同樣的分支即試驗場模式，也是目前讓 AI agent 安全操作類生產資料、同時維持可追溯性與低成本的一種可行做法。

🔗 **來源**
- 標題：Lakebase branching for CI/CD: lessons from 100 PR databases
- 作者／機構：Databricks
- 連結：https://www.databricks.com/blog/lakebase-branching-cicd-lessons-100-pr-databases

#Databricks #Lakebase #PostgreSQL #CICD #DataEngineering #DevOps #CopyOnWrite #AIAgents #DatabaseBranching #Snorkel
