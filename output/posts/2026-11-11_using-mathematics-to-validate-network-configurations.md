---
title: Using mathematics to validate network configurations
source: Amazon Science
url: https://www.amazon.science/blog/using-mathematics-to-validate-network-configurations
model: claude-code/sonnet
generated_at: '2026-11-11T23:53:54.574266'
score: 89
---

📌 用數學證明網路分段正確，而不是靠抽樣測試

TL;DR：AWS 用自動化推理工具 Tiros，把網路設定轉成邏輯命題，窮舉驗證分段是否符合政策，取代傳統的抽樣封包測試。

一次分段設定的失誤,就可能讓測試環境的封包跑進正式營運環境，或讓敏感資料跨越組織邊界。問題是，現代網路規模與複雜度早已讓「完整測試」變得不切實際,絕大多數組織只能依賴抽樣,也就意味著網路分段幾乎從未被真正徹底驗證過。

🤔 **抽樣測試驗證不了分段**

企業、銀行、醫院與學術機構都仰賴廣域網路（WAN）跨地理區域連接各地的本地網路。在 WAN 內部,常常需要將不同運算資源彼此隔離,例如用來測試新網站功能的開發環境,必須與正式上線的網站完全分離。傳統驗證網路分段的方式是透過送封包來描繪網路地圖,但現代網路規模龐大,這種方式只能透過抽樣送封包來檢測部分路徑,導致分段驗證長期處於「抽樣而非窮舉」的狀態。

🧩 **把網路設定變成邏輯命題**

AWS 的解法是使用 Tiros，一個原本用於分析網路連通性的自動化推理工具，過去已應用在 Amazon Inspector、VPC Reachability Analyzer、Network Access Analyzer 等客戶服務中,這些服務聚焦於「可達性」：判斷是否存在一串合法請求,能從某個網路資源到達另一個。這次應用的關鍵洞察是：如果能判定網路中哪些路徑可達，也就同時能判定哪些路徑不存在。分段驗證本質上是靜態分析，不需要依賴動態封包流量，因此可以頻繁到每小時分析一次已部署網路的拓樸。

具體流程是：先收集客戶的 Cloud WAN 設定（路由表、attachment、政策文件），再透過專門軟體將這些設定轉換成邏輯命題；接著向 Tiros 提問「哪些 attachment 可以用哪些目的地 IP 到達哪些 attachment」，Tiros 會推導出所有滿足條件的指派，每一個指派對應一條路徑；系統再檢查政策中規定不應互通的分段之間,是否真的不存在任何路徑。如果實際可達性與預期分段相符,驗證就通過；若不符,系統會提醒維運人員。

📊 **案例：正式環境與開發環境共用同一段位址**

設想一家使用 Cloud WAN 連接全球資源、同時維運銷售與支援網站的公司。更新網站時,會從開發環境內的一份正式網站複本進行，而正式環境必須被嚴格限制,確保尚未準備好上線的測試與變更不會波及真正的正式網站。公司因此撰寫一套政策，定義了跨兩個區域（us-east-1 與 us-west-2）的兩個分段：production 與 development。Attachment 政策透過標籤將 VPC-prod-use1 與 VPC-prod-usw2 歸入 production 分段，VPC-dev-use1 歸入 development 分段。

特別值得注意的是，VPC-prod-use1 與 VPC-dev-use1 恰好落在同一個位址空間 10.0.0.0/16 內。在這種情況下,分段就變得至關重要：如果這兩個 VPC 被部署在同一分段,或分段設定有誤,一個發往該位址空間的封包的目的地就會變得不確定（可能是 VPC-prod-use1 也可能是 VPC-dev-use1），實際後果可能是客戶流量誤送進了開發環境的 VPC。Tiros 會把這套核心網路設定建成由規則（條件性命題）與事實（無條件命題）組成的邏輯模型，再針對這個模型查詢分段情況：只要找不到任何一種指派能讓 production VPC 到達 development VPC，或反向成立,結果就證明核心網路的分段與政策聲明一致。

💡 **不只用在 Cloud WAN**

這套「把設定轉成邏輯、再檢查性質是否成立」的方法，在 AWS 內部已被廣泛用於分析規模過大、難以窮舉測試的系統屬性。例如 IAM Access Analyzer 使用名為 Zelkova 的推理引擎，協助判斷某項政策是否可能讓帳戶外的人取得資源存取權，同樣的推理方式也用來識別公開分享或跨帳戶共用的 S3 儲存貯體；VPC Reachability Analyzer 則用來判斷網路中某資源能否到達另一資源。這些工具共享同一套基礎：把設定轉換成邏輯命題,再檢查你關心的屬性是否成立。

🎯 **實務啟示**

對於管理大型分段網路的工程師而言,自動化推理工具能補上抽樣測試天生留下的盲區：與其依賴「測了幾次都沒事」的經驗性保證,不如取得「所有模型化路徑都符合政策」的數學證明。對需要合規稽核、且必須證明「絕不可能發生」而非「抽樣沒發現」的場景，這類方法尤其有價值，也值得工程團隊關注自家雲端廠商是否提供類似的靜態驗證能力。

🔗 **來源**
- 標題：Using mathematics to validate network configurations
- 作者／機構：Amazon（AWS）
- 連結：https://www.amazon.science/blog/using-mathematics-to-validate-network-configurations

#NetworkSecurity #AutomatedReasoning #AWS #CloudWAN #FormalVerification #NetworkSegmentation #CloudSecurity #VPC #IAM #CloudComputing
