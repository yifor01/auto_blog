---
title: GitHub's new Git storage architecture
source: Hacker News
url: https://github.blog/engineering/architecture-optimization/inside-githubs-new-git-storage-architecture/
model: claude-code/sonnet
generated_at: '2026-11-07T21:03:11.317536'
score: 83
---

📌 GitHub重打地基：單一Repo扛住每秒7200次Push

TL;DR：GitHub 重構 Git 儲存架構，內部測試證實單一 repo 可承受 5000 個並發 agent 同時寫入。

過去,GitHub 上最忙的 repo 一秒鐘也只收到幾十次寫入,還是短暴發型態。現在,這個數字正朝著「持續的高速率」演變,原因很簡單：寫程式碼的不再只是人。

🤔 **Agent 把「忙碌repo」的定義改寫了**

GitHub 觀察到,隨著更多開發工作轉移給全天候平行運作的 agent,原本短暴發的寫入高峰正變成常態的高速率。每一次 push 還會觸發 CI 執行、部署系統拉取新 commit、其他 agent 為取得上下文而 fetch,這種「讀取放大效應」讓整體流量隨寫入量同步暴增。文中附上的實際案例顯示,某個 repo 從今年 3 月到 5 月流量成長約 4 倍,且持續呈指數成長。基於這個趨勢,GitHub 沒有只規劃下一階段的小幅提升,而是直接把目標設在「比現在再多兩個量級」的規模。

🧩 **拆解寫入與讀取：只有 Reference Update 需要協調**

新架構代號「Rubicon」,建立在兩條設計原則上：**最小化協調**與**將儲存和運算解耦**。關鍵觀察是,Git 物件（object）是不可變的,且以內容命名,所以兩個 writer 可以同時各自寫入物件而不需要彼此同意任何事——真正需要協調的,只有體積小得多的 reference 更新。

整個架構由三塊拼起來：
- **Spokes** 維持原本的角色,處理請求路由、負載平衡、租戶隔離與公平性,屬於「橫向擴展」的部分,大致沿用過去已驗證過的做法。
- **Virtual replicas** 是新引入的一組可拋棄式運算單元,負責處理讀、寫或兩者,本地磁碟只是隨時可重建的快取。Spokes 會盡量把同一個 repo 的流量導到同一批 virtual replica 上以維持快取熱度,但正確性不依賴請求落在特定節點上——某個 replica 消失,其他 replica 照常服務,新的 replica 補位後再慢慢填滿快取。
- **Compaction nodes** 在背景直接對 Blob Storage 與 Ref-CAS 工作,合併每個 repo 的 pack、清除不可達物件,完全不佔用 virtual replica 的運算資源。

持久狀態分成兩處存放：Git 物件（pack 檔與輔助的讀取加速資料）存在 Azure Blob Storage；reference 與 pack manifest 則存在一個叫 Ref-CAS（Reference Compare-and-Swap）的複製式 log 服務裡。寫入流程是：virtual replica 索引新進的 pack、上傳到 Blob Storage,再對 Ref-CAS 送出一筆交易,把這個 pack 登記進 manifest 並更新 reference；之後再由 compaction node 把這個 pack 和其他 pack 合併。讀取流程則是:virtual replica 先向 Ref-CAS 確認 reference 版本,再把需要的 pack 拉進快取,從快取服務讀取。

📊 **內部測試：5000 個並發 Agent、每秒 7200 次 Push**

GitHub 透過內部測試證明,這套架構能支援單一 repo 上 5000 個並發 agent 同時工作,送出每秒 7200 次 push,同時維持讀取流量的低延遲。這整套架構是在 GitHub 既有服務持續運作的情況下,一邊重建底層一邊上線的。

🎯 **對開發者和團隊意味著什麼**

對日常使用者而言,push、fetch、branch 的操作方式和保護機制都沒有改變,改變的是底層能撐住多少並發寫入。對正在大規模導入 agentic 開發流程的團隊來說,這代表未來把更多 agent 同時丟到同一個 repo 上工作,不必擔心寫入成為瓶頸;而「物件不可變、只有 reference 更新需要協調」這個思路，也值得想要自建高並發版本控制或類似協調系統的工程團隊參考。

🔗 **來源**
- 標題：GitHub's new Git storage architecture
- 作者／機構：DAlperin（分享於 Hacker News；原文來自 GitHub Blog）
- 連結：https://github.blog/engineering/architecture-optimization/inside-githubs-new-git-storage-architecture/

#GitHub #GitArchitecture #AgenticDevelopment #DistributedSystems #CloudInfrastructure #SoftwareEngineering #AzureBlobStorage #DevOps #ScalableSystems #VersionControl
