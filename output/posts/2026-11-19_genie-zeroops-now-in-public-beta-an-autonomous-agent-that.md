---
title: 'Genie ZeroOps, now in public beta: An autonomous agent that fixes data pipelines,
  with lessons from 80,000 customer issues'
source: Databricks
url: https://www.databricks.com/blog/genie-zeroops-now-public-beta-autonomous-agent-fixes-data-pipelines-lessons-80000-customer
model: claude-code/sonnet
generated_at: '2026-11-19T23:55:34.679986'
score: 80
---

📌 Databricks Genie ZeroOps 公測:從8萬起真實案例練出的資料管線修復代理

TL;DR:Databricks Genie ZeroOps 進入公開測試,自主代理能偵測、調查並修復資料管線問題,公測新功能來自8萬起真實客戶案例的回饋。

資料工程團隊每天要照看數千條 pipeline,失敗分成兩種:吵鬧的和沉默的。吵鬧的那種,工作排程出錯,工程師立刻被呼叫;沉默的那種,一張表悄悄停止更新,或是昨晚的載入只進來一半資料,直到某天儀表板上的數字明顯不對,才有人發現出事。無論哪一種,接下來的流程幾乎一樣:收到通知,工程師花上幾小時翻 log、查上游表、拼湊關聯資產,最後才生出一個修復的 PR。

🤔 **管線維運的真實痛點**

Databricks 在今年六月推出 Genie ZeroOps,一個能偵測、調查、解決資料管線問題(例如上游 schema 變更或資料品質異常)的自主代理。經過數百家企業參與的私測,官方表示這套流程涵蓋從初始警示到產出 PR 共五個核心步驟,目標是在維持安全性、治理與建議品質的前提下,自動化整套原本靠人力進行的調查修復流程。

🧩 **8萬起案例教會的事:一半以上的問題需要「公司特有知識」**

私測期間,ZeroOps 觀察了超過8萬起橫跨數百家企業的真實客戶問題,結果發現超過一半的問題需要組織特有的知識,才能正確分級、排序與解決。這直接指出通用型自動化很難單靠模型本身的常識就把問題處理好,客製化的上下文(context)是剛需。

因此,根據回饋,公測版本新增了幾項關鍵能力:收件箱共享(inbox sharing)、通知機制、一鍵建立 PR,以及讓團隊加入自訂業務指示,依照公司特定流程運作,也可以用自訂指示過濾不想要的通知,或把某個洞察標記為「不是問題」。

💡 **技術上怎麼做到**

ZeroOps 會在偵測到問題時自動觸發,不需要人工下 prompt,分析在有人注意到之前就已經準備好。它內建存取執行歷史(run history)、Unity Catalog lineage、Delta history 與 Data Quality Monitoring(DQM)訊號的能力,並在 Unity Catalog 的權限範圍內運作。DQM 用來標記提交時間異常延遲(freshness)或列數低於預期範圍(completeness)的表。根據官方文件,ZeroOps 會讀取執行 log、原始碼、上游表的 metadata 與樣本資料,同樣遵守 Unity Catalog 的權限設定。

模型呼叫使用 Databricks 安全邊界內自家主機代管的模型,呼叫範圍留在工作區所在的地區,模型供應商不會保留 prompt 或回應內容。

⚠️ **它不會自己改你的程式碼**

官方明確說明,ZeroOps 不會在未經直接核准的情況下更動程式碼或資料。目前它負責調查失敗原因、提出修復方案,並可以把修復推送到新分支產生 PR,但從不在沒有人工審查的情況下變更正式環境的程式碼或資料。

🎯 **實務啟示**

如果團隊維運的 pipeline 規模已經大到人力難以逐一巡查,可以請 workspace 管理員從 Previews 頁面啟用 ZeroOps,並在 pipelines 頁面頂端找到 ZeroOps 橫幅開始試用。考慮到超過半數問題仰賴組織特有知識,導入初期值得花時間把自訂業務指示補齊,這會直接影響分級與修復建議的準確度。

🔗 **來源**
- 標題:Genie ZeroOps, now in public beta: An autonomous agent that fixes data pipelines, with lessons from 80,000 customer issues
- 作者/機構:Databricks
- 連結:https://www.databricks.com/blog/genie-zeroops-now-public-beta-autonomous-agent-fixes-data-pipelines-lessons-80000-customer

#Databricks #DataEngineering #AIAgent #DataPipeline #UnityCatalog #DataQuality #MLOps #AutonomousAgent #DeltaLake #DataOps
