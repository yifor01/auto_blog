---
title: Reason Machines Open-Sources Aspen, a Git Server Built for AI Agents
source: MarkTechPost
url: https://www.marktechpost.com/2026/11/09/reason-machines-aspen-open-source-git-server-ai-agents/
model: claude-code/sonnet
generated_at: '2026-11-10T00:53:47.989653'
score: 96
---

📌 Aspen:專門給 AI Agent 大軍寫入的開源 Git 伺服器

TL;DR:Reason Machines 開源 Aspen,獨立實現 OpenAI Pando 的設計理念,讓數百個 agent 同時 push 不再互相卡住。

當幾百個 AI agent 同時對同一份原始碼 push commit,傳統 Git 伺服器的排隊機制會先撐不住——這正是 OpenAI 內部遇到的瓶頸,而現在有團隊把類似的解法做成了開源專案。

🤔 傳統 Git 伺服器的工作量,是跟著用戶端數量成長的

根據 Reason Machines 的說法,一般 Git 伺服器會把對同一個 repository 的每次 push 排在一起處理,而且每次 fetch 都重新打一份 pack。結果伺服器的負擔是隨著用戶端數量增加,而不是隨著新程式碼量增加。OpenAI 碰到這個瓶頸後打造了內部系統 Pando,據稱把 push 延遲的中位數降低了將近 5 倍,每天服務接近一個 petabyte 的流量。Aspen 跟隨 Pando 的設計,並放棄了多數 Git 伺服器仍保留的兩個假設。

🧩 以分支為單位擴展,而不是以整個 repository 為單位

Aspen 是 Reason Machines 推出的可自架 Git 伺服器,對外仍是標準的 Git over HTTPS 與 SSH,但內部把寫入規模化到「每個分支」而非「每個 repository」:pack 檔案存進 S3 相容的物件儲存,分支歷史則存進 PostgreSQL。

每個分支在 Postgres 裡是一行版本鏈,push 先把 pack 上傳,再用一次 compare-and-swap 移動分支指標。不同分支的 push 彼此永不等待;如果兩個 push 競爭同一個分支,一個會贏,另一個收到 Git 常見的「fetch first」錯誤,代價是分支可能在稍微不同的時間點被讀到。

Aspen 從不 unpack 收到的 push:只檢查 pack、補齊缺的 base object,然後原樣存起來;fetch 時直接串流用戶端缺少的已存 pack,不重新壓縮,甚至可以用 signed URL 讓 CDN 直接服務 pack。push 時只看得到 trunk 分支,讓 negotiation 在上百萬個分支的規模下依然維持精簡。背景的 compaction 會每 16 個 pack 合併一次,採用類似 log-structured merge tree 的分層方式,讓落後很多的用戶端只需要拿幾十個 pack,而不是幾千個;CI 常用的 depth-1 fetch,則讓 tip pack 只需打包一次,就能服務所有 job。

📊 單機測試跑出每秒 567 次 push

測試環境是一臺 8 核心伺服器、S3 Standard,以及一個 4 核心的 Postgres,目標 repository 是 git.git 的拷貝,約 4,500 個檔案、75,000 次 commit。Aspen 在 5 分鐘內維持每秒 567 次 push 且沒有錯誤,每次 push 在 Git 印出「ok」之前,都已經確實寫進 S3 與 Postgres。作為對照,Cursor 公開報告其 Origin 在 S3 Standard 上最高約每秒 120 次 push,在 S3 Express One Zone 上可超過 300 次(不過那是 Cursor monorepo 上的複寫叢集,設定條件不同)。README 也特別說明,這些數字屬於指標性質,不是正式的效能宣稱。

🧩 怎麼上手

Aspen 用 Rust 撰寫,可從原始碼直接 build;`aspen dev` 指令能用 SQLite 與本地目錄跑起整套環境做測試。團隊導入時可用 Docker Compose(搭配 PostgreSQL 與 MinIO)或 Helm chart 部署,Terraform 則涵蓋 AWS、Google Cloud、Azure 與 Hetzner。Mirror mode 可以前置既有的 GitHub 或 GitLab 倉庫,不必真的搬家就能先試用。官方提供的 live demo 是一塊 64x64 像素的畫布,每次點擊就會對應推送一個 commit。根據該公司說法,整個 Aspen 是由一個 Reason agent 從第一次 commit 到公開發布只花了 4 天,中間合併了 151 個 PR。

🎯 實務啟示

如果你的團隊已經或即將讓大量 agent 對同一個 repository 並行寫入,Aspen 提供了一個具體、可參考的架構模式:把分支當作擴展單位、延後 unpack、用 compaction 控制長尾成本。它給出的每秒 567 次 push 這個數字也可以當作評估自家 CI/CD 負載上限時的一個參考基準。

🔗 來源
- 標題:Reason Machines Open-Sources Aspen, a Git Server Built for AI Agents
- 作者／機構:Asif Razzaq(MarkTechPost)
- 連結:https://www.marktechpost.com/2026/11/09/reason-machines-aspen-open-source-git-server-ai-agents/

#Aspen #GitServer #OpenSource #AIAgents #DevOps #Rust #ReasonMachines #OpenAI #Pando #SoftwareInfrastructure
