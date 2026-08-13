---
title: Databricks Network Configuration delivery to Tens of Millions of Serverless
  VMs
source: Databricks
url: https://www.databricks.com/blog/databricks-network-configuration-delivery-tens-millions-serverless-vms
model: claude-code/sonnet
generated_at: '2026-08-13T07:36:05.709849'
score: 81
---

📌 每天千萬臺 VM 開機，Databricks 用預先計算解掉網路設定瓶頸

TL;DR：把同步聚合網路設定改成非同步事件驅動加快照儲存，開機查詢只剩一次讀取。

當一臺 serverless VM 要啟動時，它得先知道「我能連到哪些儲存空間、要不要走 private link、Unity Catalog 是否剛授權了新權限」，而這個問題的答案，原本分散在好幾個上游服務裡，得在叢集啟動的關鍵路徑上即時湊齊。

🤔 **問題：關鍵路徑上的同步聚合，撐不住規模成長**

Databricks 的 serverless 運算平臺每天在 AWS、Azure、GCP 上啟動數千萬臺 VM，支撐 SQL 倉儲、notebook、ML 服務端點等幾乎所有資料與 AI 產品。網路設定並非存在單一位置，而是要從多個上游服務組裝而成。原始架構是每次叢集啟動時，網路設定服務同步呼叫所有上游服務、聚合回應、計算出該工作區的網路設定，再回傳給 serverless 資料平面，整個過程發生在叢集建立的關鍵路徑上。這套架構在小規模時運作良好，但隨著 serverless 用量快速成長，每一次同步呼叫都會在所有工作區上觸發昂貴運算，且經常重複計算，負載隨租戶數與其設定的資源數量成正比成長，逐漸變得難以為繼。

🧩 **架構重構：把「算」和「讀」拆開**

Databricks 對整套網路設定交付機制做了從頭重構，核心是把兩條路徑徹底分離：

- **管理路徑（非同步、背景執行）**：上游服務將變更事件送進訊息佇列，事件處理器（event processor）消費事件後，判斷哪些工作區受影響並分派逐工作區的更新通知；本地事件管理器接著向上遊取得相關細節、重新計算該工作區的網路設定，並存入預先計算好的快照儲存（snapshot store）。系統另外還有一個週期性協調器（reconciler），在背景重新同步所有工作區，確保即使事件遺漏也能達到最終一致性。
- **服務路徑（關鍵、快速）**：當 serverless 叢集啟動並需要網路設定時，網路設定服務直接從快照儲存做單次讀取即可回應，完全不需呼叫任何上游服務，大幅降低對上游服務的負載。

以實際流程為例：當客戶新建一個 Unity Catalog 連線時，Unity Catalog 會向訊息佇列發出變更事件；事件處理器接收事件、判斷哪些工作區掛在受影響的 metastore 下，並分派逐工作區的更新通知；在每個工作區的分區內，事件管理器收到通知後，取得最新的連線細節、重新計算該工作區的網路設定，並以新的版本標記存入快照儲存。從此之後，任何 serverless 叢集要求網路設定時，都直接從快照儲存取得，不再需要任何上游呼叫。

📊 **上線後的規模：每天服務數十億次請求**

重構後的系統目前每天服務數十億次網路設定請求，延遲約 125 毫秒，可用性達 99.99%。

💡 **三個工程教訓**

- **預先計算讓關鍵路徑解耦**：把昂貴的聚合運算搬到背景執行，服務路徑因此變得極其簡單快速，這是整個專案中影響最大的架構決策，把一條多服務依賴鏈變成單一次儲存讀取。
- **事件驅動用一致性換取可擴展性，協調器則是安全網**：事件推播處理常見情境已經很有效率，週期性協調器則負責補上任何漏掉的變更。
- **從第一天就為可擴充性而設計**：模組化、分階段的架構意味著新增一個上游資料來源，只需要新增一個階段實作，核心管線完全不用修改，讓網路設定系統能隨 Databricks 產品版圖擴張持續延伸。

🎯 **實務啟示**

對於設計多租戶控制平面的工程師，這是一個值得借鏡的模式：與其在熱路徑上同步聚合多個服務的狀態，不如把昂貴的聚合運算搬到背景，透過「快照儲存＋週期性協調器」提供快速且具最終一致性保證的讀取路徑，同時保留模組化的階段設計，方便日後擴充新的資料來源。

🔗 **來源**
- 標題：Databricks Network Configuration delivery to Tens of Millions of Serverless VMs
- 作者／機構：Databricks
- 連結：https://www.databricks.com/blog/databricks-network-configuration-delivery-tens-millions-serverless-vms

#Databricks #ServerlessComputing #DistributedSystems #EventDrivenArchitecture #CloudInfrastructure #SystemDesign #UnityCatalog #ScalableArchitecture #DataEngineering #SoftwareArchitecture
