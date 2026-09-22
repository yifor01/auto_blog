---
title: AI coding has made CI a bottleneck, so we reworked ours to keep up
source: Hacker News
url: https://linear.app/now/ci-bottleneck-reworked
model: claude-code/sonnet
generated_at: '2026-09-22T20:30:19.164636'
score: 91
---

📌 AI 衝太快，Linear 怎麼讓 CI 跟上腳步

TL;DR：Linear 重整 CI 管線，測試量增 4 倍下等待時間仍不增反減。

當 AI agent 把「寫程式碼」這件事的速度拉到極限，真正拖慢團隊的反而是驗證程式碼的那一關。Linear CTO Tuomas 直接把一張標題為「CI costs are high」的 issue 指派給工程師 Mufeez Amjad，順帶一句：也順便讓 CI 快一點。

🤔 **AI 讓出貨變快，驗證卻拖住整條線**

Linear 觀察到，agent 讓寫程式碼的速度呈指數成長，但驗證變更的流程並沒有跟上同樣的速度。每個 PR 仍然得通過 CI，開發越快，CI 就越容易變成瓶頸，同時推高基礎設施成本，讓工程師與 agent 都得等更久才能拿到回饋。Linear 的目標很明確：縮短 PR 在 CI 上的等待時間，並降低每次測試消耗的 runner 時間。即便測試套件從年初至今幾乎成長了 4 倍，PR 等待時間仍從超過 6 分鐘降到剛過 5 分鐘，每次測試的機器時間大約減半。

🧩 **四個切入點，從底層機器到重複設置都不放過**

Linear 的程式碼庫以 TypeScript 為主，但團隊表示多數最佳化思路可以套用到其他語言與工具鏈。整體改動分成四大方向：升級基礎設施與工具、最佳化「卡住」後續工作的關鍵任務、減少重複的環境設置，以及讓測試執行本身更有效率。

**換掉 runner 與編譯器，幾乎不用碰 CI 邏輯就先賺一波**
把工作負載從 GitHub Actions 搬到第三方 runner，換來 CPU 更快、儲存效能更高、快取基礎設施更好的機器。切換前後兩天的同類比較顯示，工作平均快了 34%，像 tsc 這種工作甚至掉了 52%。另外，改用原生 TypeScript 編譯器 tsgo 之後，tsc 檢查的每週中位數時間直接砍掉 73%，大到足以讓 typechecking 完全脫離瓶頸位置。

**Lint 拿掉型別檢查依賴**
Linear 有些自訂 lint 規則需要依賴 TypeScript 的型別資訊才能套用限制或自動修正，代表每次 lint 都得先建出完整的型別圖，讓 lint 成為最耗記憶體的 CI 工作之一。團隊把這些規則改寫成只在抽象語法樹（AST）上做靜態分析，讓 ESLint 完全不需要 TypeScript，API 的 lint 時間降低 68%，全倉庫 lint 時間降低 55%，記憶體用量也明顯下降。少了型別依賴後，後續改用 Oxlint 也變得容易許多，因為純語法規則移植起來相對直接，Oxlint 本身又進一步壓低了花在 lint 上的 runner 分鐘數。

**把守門工作挪出關鍵路徑**
底層設施和個別檢查都變快後，Linear 把視角拉高檢視整個 CI 系統，發現問題出在最前面那些看似不起眼的小工作。每次執行一開始都要判斷 PR 動到哪些路徑、這些測試是否已針對相同輸入跑過，這些檢查在 job 層級把關，跳過的工作不會佔用 runner，但也因此直接卡在關鍵路徑上——8 個 API 測試分片必須等它們跑完才能開始，一點延遲都會被放大。

change-detection job 原本會拉取完整的工作樹，即便只需要一小部分。限制 fetch 深度後，最慢的一個守門工作從 94 秒降到 20 秒；對完全不需要工作樹的工作直接移除 checkout，時間從 27 秒降到 7 秒；針對 commit push 與合併佇列事件，改用 sparse、無 blob、限制歷史深度的 checkout 也再省下約 11 秒。整體下來，change-detection job 的中位數時間從 26 秒降到 8 秒，p90 從 31 秒降到 12 秒，最慢的一次從 138 秒降到 37 秒。

換到第三方 runner 之後，團隊也發現用 actions/checkout 的 checkout 時間變長，偶爾還會卡住。因為第三方 runner 在 GitHub 網路之外，得靠一條直連 IP 的線路連回 GitHub，供應商追查後發現是那條線路間歇性劣化所致。Linear 因此自己寫了一個 composite action 取代 actions/checkout，加入重試與退避機制，並設定 GIT_HTTP_LOW_SPEED_LIMIT 與 GIT_HTTP_LOW_SPEED_TIME，讓連線卡住時大約 30 秒就中止，而不是無限期掛著，同時搭配保留在 sticky disk 上的持久化 git mirror 快取。結果是關鍵路徑上因等待 checkout 而閒置的 job 大幅減少。

另外，原本合併前的最後一個檢查會順便寫入快取標記，這代表 PR 就算測試已全部通過，也得在合併佇列裡多等一輪。Linear 把這個寫入動作搬到測試分片跑完之後、但不卡任何工作的 job 裡，每個 API PR 與合併佇列項目因此省下 42 秒。加總起來，API PR 在快取未命中時的必要檢查時間縮短了大約一分鐘，同時也減少了 runner 啟動次數。

**減少每個 job 的重複開銷**
Linear 接著把焦點轉向每個 job 都要重複付出的設置成本：開機、安裝套件、準備建置依賴。這些開銷代表一個只做幾秒鐘實際工作的 job，可能要耗掉好幾分鐘的基礎設施時間。團隊把每個 API 測試分片都要用 apt 安裝一次的 Postgres client 直接內建進 CI 映像檔，讓每個分片一開機就能直接用；後來又把必要的原生建置標頭檔一併加進映像檔，因為設置階段下載這些檔案偶爾會卡住。

Linear 的程式碼庫是用 pnpm workspace 管理的 monorepo，原本 API 測試流程會安裝整個 workspace，但實際上只需要 API package 及其依賴。把安裝範圍限縮到 API package 後，pnpm install 從 44 到 73 秒降到 16 到 18 秒，同樣做法也套用到其他 API 相關的 job 上，這些 job 原本會安裝整個倉庫並上傳一份幾乎用不到的依賴快取。

團隊也測試過快取 node_modules，結果發現重新安裝反而更快：快取的 key 依賴一個經常變動的 lockfile，就算快取命中，還原也要花約 28 秒，相較之下經過篩選的全新安裝只要約 7.5 秒。快取只是增加了儲存時間與不確定性，卻沒有帶來實質好處。這三項改動加起來，讓每個分片的設置時間減少約 44%，從 110 到 140 秒降到 67 到 73 秒。

📊 **測試量翻 4 倍，等待時間反而更短**

綜合以上調整，Linear 在測試套件幾乎成長 4 倍的情況下，把 PR 等待 CI 的時間從超過 6 分鐘壓到剛過 5 分鐘，每次測試消耗的 runner 時間大約減半。文章也提到後續還有其他重複設置可以繼續消除，顯示這是一個持續進行中的最佳化過程。

🎯 **實務啟示**

這篇分享的價值在於它把「CI 變慢」拆成了具體、可量測的環節：底層機器、卡在關鍵路徑上的守門工作、每個 job 重複付出的設置成本，缺一不可。對正在用 agent 加速開發、卻發現 CI 排隊越來越長的團隊來說，先量測 change-detection、checkout、依賴安裝這幾個「看起來很小卻卡在最前面」的步驟，往往比一頭栽進測試平行化更快見效。快取也不是萬靈藥，Linear 拿掉 node_modules 快取反而更快的案例，值得任何正在最佳化 CI 的團隊重新檢視自己的快取策略是否真的划算。

🔗 **來源**
- 標題：AI coding has made CI a bottleneck, so we reworked ours to keep up
- 作者／機構：Mufeez Amjad @ Linear
- 連結：https://linear.app/now/ci-bottleneck-reworked

#CI #DevOps #SoftwareEngineering #TypeScript #Linear #ContinuousIntegration #DeveloperProductivity #AICoding #BuildPerformance #EngineeringBlog
