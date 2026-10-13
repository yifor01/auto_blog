---
title: Redesigning source control at Anthropic
source: Anthropic Engineering
url: https://www.anthropic.com/engineering/redesigning-source-control
model: claude-code/sonnet
generated_at: '2026-10-13T21:56:54.563305'
pinned: true
---

📌 【Anthropic 工程部落格】Claude 寫太多程式碼，逼出一套新版本控制系統

TL;DR：Anthropic 自建 Scion 取代 git，五個月內完成monorepo 全面遷移，只因 agent 把程式碼合併量衝到每天三萬次。

🎣 2026 年 5 月，Anthropic 平均每天合併約 2,500 次程式碼變更；到了 9 月，這個數字變成超過 30,000 次。不是團隊變多了，而是 Claude 自己在寫程式。當 agent 的產出速度遠超人類開發基礎設施的負荷上限，瓶頸就從「寫程式」轉移到了「版本控制」。

🤔 **當 git 的設計假設不再成立**

Anthropic 在文章中指出，coding 已經不再是建構系統或做研究的瓶頸：Claude 能自主迭代研究迴圈、微調複雜程式、從零打造新服務。真正卡住團隊的,是為「人類開發速度」設計的基礎設施：source control、build 與 CI。

git 的核心設計是去中心化：每個 clone 都是完整、可離線運作的 repository。但 Anthropic 的 monorepo 主分支歷史已逼近 100GB，壓縮後的工作副本超過 25GB，單日光是 CI 就要執行約 2,500 萬次 checkout（還不含開發環境、agent sandbox 與研究任務）。若直接 fetch，等於每天產生超過 600 PB 的 git 流量。團隊雖然用了 shallow clone、sparse checkout、promisor remote，甚至曾經同時維運數百個內部 git mirror 來撐住負載，但 seed（存放在 blob storage 的 repo 快照）會隨著主幹更新而逐漸過時，依賴歷史紀錄的操作（如 diff、blame）在partial clone 上也愈來愈難維持。

🧩 **把「client 永遠在線」當成第一原則**

Anthropic 觀察到一個關鍵事實：幾乎所有的 client 都是 agent 與自動化任務，而這些 client 定義上就是「永遠在線」的。於是團隊重新設計了一套名為 Scion 的版本控制系統，核心原則包括：

- Client 永遠在線：不像 git 假設 client 需要離線運作與完整副本，Scion 的 client 只維護有限大小的本地 object 快取，資料由 server 隨需取得。
- Client-server 不對稱：git 的每個 client 都能充當完整 server；Scion 則由 server 負責歷史查詢、blame、建立 commit、merge 與 rebase，client 只負責本地快取、檔案系統監控與使用者互動。
- 完整的 API 化 source control 服務：許多內部工具（如自動化 bisect 與 revert pipeline）可以直接透過 API 查詢版本控制資訊，不需要本地 repo 副本。
- 一切都要能水平擴展：Scion 的資料是分散式的，沒有任何地方存有完整的 repo 副本（包括 server 端），也沒有 git packfile 這類需要維護的壓縮檔。
- Commit 必須便宜、增量、無鎖：所有 commit、rebase、merge 都發生在 server 端，操作成本只跟變更大小相關，而非整個 repo 的大小；除了主分支與 release 分支外，Scion 盡量避免使用 ref（分支、tag），以減少所有 server 必須同步的全域狀態。
- 工作副本是可選的，且預設為 sparse：CI job 可以直接向 server 詢問兩個 commit 之間的 diff，不需要先 checkout；Scion 的協議以 sparse checkout 與「虛擬化 checkout」（依需求才實體化檔案）為中心，真正需要讀取檔案時才會產生對應成本。

文章也提到，Scion 的設計參考了 Google Piper 與 Meta Sapling 這類大型 monorepo 版本控制系統的既有經驗。在實作上，Scion 的基本工作單位是「changeset」，以 write-ahead log 的形式記錄，涵蓋了 git commit 中大部分常見的資訊。除了 Scion 本身，Anthropic 同期也打造了程式碼審查介面 Antique、程式碼搜尋，以及一套 source control 專用的 IAM 系統。

💡 **問題本質不是「git 不好」，而是「人類規模 vs agent 規模」**

這篇文章最值得注意的觀點是：git 為離線、分散式協作設計的特性，在一個幾乎所有 client 都是「永遠在線的 agent」的世界裡，反而成了限制擴展的包袱。Anthropic 並不是說 git 設計有誤，而是指出當開發主體從人類轉移到大量自動化 agent 時，原本的假設不再成立。

🎯 **實務啟示**

對正在大量導入 AI coding agent 的團隊而言，即使暫時不需要重建整套版本控制系統，Scion 的設計原則仍值得參考：優先思考「API 化的 source control 查詢」能不能取代本地 checkout，以及現有 CI/CD pipeline 在 agent 產出量大幅成長後，哪個環節會最先撐不住。

🔗 **來源**
- 標題：Redesigning source control at Anthropic
- 作者／機構：Anthropic
- 連結：https://www.anthropic.com/engineering/redesigning-source-control

#Anthropic #Scion #VersionControl #SourceControl #AgenticCoding #DeveloperInfrastructure #Monorepo #Git #SoftwareEngineering #ClaudeCode
