---
title: How iFood scales coding agents across 15,000 repositories
source: OpenAI Blog
url: https://openai.com/business/customer-stories/ifood
model: claude-code/sonnet
generated_at: '2026-11-25T01:33:09.944001'
pinned: true
---

📌 iFood 如何用 Remote Agents Platform 管理 1.5 萬個 repo

TL;DR：iFood 把工程任務變成一支 API，讓 coding agent 在沙盒裡非同步跑完 15,000 多個程式碼庫的重複工作。

單一個程式碼庫要做依賴套件修復或規範檢查並不難，難的是把同一件事在 15,000 個程式碼庫上重複做，還要做得穩定又便宜。這正是巴西外送平臺 iFood 工程團隊遇到的問題。

🤔 不是任務難，是規模大

iFood 維運超過 15,000 個程式碼庫，每個都需要定期跑一些工作，像是驗證程式碼是否符合內部規範、修復有漏洞的依賴套件，或做各種分析。iFood 資深軟體工程師 Victor Coelho 表示，在這之前，各團隊各自想辦法解決，但最終都撞上同一個瓶頸：沒有一層共用的 agent 執行環境可用。

🧩 把工程任務變成一支 REST API

Remote Agents Platform 的運作分三步：使用者透過 REST API 送出提示詞與環境需求；平臺把任務丟進一個獨立沙盒裡的專屬 remote runner 執行；結果稍後被取回。整個流程中，決定性的步驟（clone 程式碼庫、匯入 agent 可用的技能、建立工作分支，以及最後發布 merge request、產出成品）包在兩端，中間真正的 agent 執行則交給在沙盒裡運作的 GPT-5.6 Luna。Coelho 形容這是「確定性步驟」與「agent 執行」兩種步驟的組合，讓整個流程可預期。

沙盒執行環境是 Ubuntu，內建 iFood 生態系需要的工具鏈，包括 Python、Java、Kotlin、C#、TypeScript、Rust、JavaScript 與 Go。除了沙盒本身，agent 還能存取 Nexus、GitLab、Docker、Snyk、Kubernetes 與 AWS。

💡 為什麼選 GPT-5.6 Luna，以及把成本當成架構問題

Coelho 表示，團隊比較同一個檢查點下的多個模型後，選擇 GPT-5.6 Luna，原因是它在智慧程度、效率與執行速度三者之間取得不錯的平衡。這個平衡在要擴展到大規模使用情境時特別重要：平臺單次執行平均要耗掉數萬個 token，平均每次執行成本約美金 0.04 元，這個數字在大規模運作下，已經從細節變成架構層面必須納入考量的事。

平臺用 OpenAI 的 Structured Outputs 來判定 agent 到底有沒有把任務做完：要求輸出必須符合預先定義好的格式，這樣團隊才能穩定從 agent 的 session 裡抓到預期的結果，無論任務成功與否都能拿到一致的回應。

📊 上線後的數字

| 指標 | 數值 |
|---|---|
| 覆蓋程式碼庫數 | 15,000+ |
| 累積完成任務數 | 25,000+ |
| 累積消耗 token 數 | 270 億以上 |
| 平均每次執行成本 | 美金 0.04 元 |
| 安全平臺修復準確率與修復數提升 | 2 倍以上 |

平臺最早、也是最大的使用者是 iFood 內部的安全平臺，用來掃描 15,000 個程式碼庫裡有漏洞的依賴套件並嘗試修復。遷移到 Remote Agents Platform 後，修復的準確率提高了一倍以上。Coelho 指出，這個案例的重點是，安全團隊不需要自己打造一套 agent 執行環境，也不需要變成 agent 編排的專家，只需要呼叫一支 API。

由於任務是非同步委派、不需要即時盯著，開發者可以在開會的同時丟出一個修 bug 或效能分析的任務，讓例行工作不再佔用注意力，把時間留給真正需要判斷力的問題。

Coelho 也提到，這個平臺的介面設計、資源組織方式與非同步執行、延後取回結果的做法，很大程度參考了 OpenAI 的 Batch API 與更新的 Agents API。

🎯 實務啟示

對要把 coding agent 導入大規模工程組織的團隊來說，這個案例指出一個常被低估的瓶頸：缺的往往不是想法或模型能力，而是一層可靠的執行基礎設施。把「確定性步驟」與「agent 執行」分開設計、用 Structured Outputs 強制結果符合契約，並把每次執行成本當成架構決策，而不是上線後才檢討的細節，這三點是 iFood 這個案例裡最值得其他團隊借鏡的地方。

🔗 來源
- 標題：How iFood scales coding agents across 15,000 repositories
- 作者／機構：OpenAI
- 連結：https://openai.com/business/customer-stories/ifood

#OpenAI #CodingAgent #GPT5 #DevOps #EnterpriseAI #Automation #SoftwareEngineering #API #StructuredOutputs #AIatScale
