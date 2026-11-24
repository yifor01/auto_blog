---
title: Zero data retention with Enterprise Frontier Safeguards is now in beta
source: Claude Blog
url: https://claude.com/resources/articles/zero-data-retention-with-enterprise-frontier-safeguards
model: claude-code/sonnet
generated_at: '2026-11-24T03:29:54.299860'
pinned: true
---

📌 Anthropic 開放 Enterprise Frontier Safeguards 公測：資料零留存，也能抓到跨請求的攻擊

TL;DR：EFS 讓企業資料完全不離開自己的雲端環境，同時仍能偵測橫跨多次請求的複雜濫用行為。

今年 9 月，Anthropic 的威脅情報報告揭露一起針對約 50 個組織的攻擊：攻擊者操作一個 AI 代理，把攻擊工作拆成多個並行執行的子任務，還把竊取到的憑證保存下來，方便之後繼續行動。如果只看單一一次請求，每個任務看起來都平凡無害。這正是傳統零資料留存（zero data retention, ZDR）方案的盲點——逐筆檢查看不出跨請求的攻擊模式。

🤔 單筆請求看起來乾淨，不代表整個行動是乾淨的

依賴傳統 ZDR 的客戶，原本就受到 Claude 的 classifiers 保護：這是即時安全防護層，會逐筆評估單一請求是否可能造成傷害。但複雜的攻擊通常橫跨多次查詢，單獨看任何一次請求都可能顯得無害。Enterprise Frontier Safeguards（EFS）因此引入第二層防禦：自動化安全監控（automated safety monitoring），專門尋找橫跨大量請求的濫用模式。

🧩 資料留在你自己的雲端，偵測交給 Anthropic

EFS 的關鍵設計是：自動化安全監控分析的資料，完全存放在客戶自己控制的基礎設施上，而不是 Anthropic 的伺服器。當系統偵測到風險，會產生一份 Safety Case 供企業自行審閱，可以從自己的雲端儲存或透過 API 讀取，並整合進既有的 SIEM（安全資訊與事件管理）系統，且 Safety Case 本身不包含原始的輸入與輸出內容。這套機制能協助團隊偵測蓄意濫用（例如攻擊性網路行動），以及代理行為超出使用者本意的情況，例如在極端案例中，代理利用漏洞存取內部資料庫或外部系統。

在 ZDR 的保證下，企業需要自行準備儲存空間存放輸入與輸出內容，資料寫入後 Anthropic 與雲端供應商都不會留存副本；企業自行設定存取政策、稽核紀錄，並用自己的金鑰加密安全資料；Anthropic 與雲端供應商的人員都不會人工檢視輸入輸出內容，只有自動化安全監控系統能存取；輸入輸出也絕不會被用於模型或分類器的訓練。EFS 可透過 Claude Platform、Claude Platform on AWS、Amazon Bedrock，或 Google Cloud 上的 Claude 使用；若透過 Bedrock 或 Google Cloud（Google Managed）使用，整套流程會由雲端供應商運作，資料流也完全留在該雲端的邊界內。

📊 超過 100 家客戶參與打磨，四分之一的 Fortune 100 已在評估

自 9 月公開宣布以來，Anthropic 已與超過 100 家客戶一起打磨 EFS，其中包含四分之一的 Fortune 100 企業，以及醫療、金融服務、法律等對資料可見性有嚴格規範的產業。Bridgewater、Salesforce、Stripe 等企業已在私測階段評估 EFS。Stripe 安全主管 Matthew Kemelhar 表示，EFS 讓他們能把對話紀錄留在 Stripe 自己的 AWS 環境中，存取與審查則由 Stripe 自己的安全控管機制決定。Cisco 的 Distinguished Engineer Omar Santos 則指出，EFS 讓客戶能把敏感資料留在自己的環境、用自己的加密金鑰保護，同時仍保有前沿模型所需的專門安全機制。現在，EFS 正式從私測進入公開測試階段。

🎯 實務啟示

對身處高度監管產業（醫療、金融、法律）的團隊而言，EFS 提供了一個過去難以兩全的組合：一邊是零資料留存的合規要求，一邊是偵測跨多輪互動的複雜攻擊所需的可見性。如果你的組織過去因為資料留存政策而不敢放行前沿模型處理敏感工作流程，現在可以評估透過 Claude Platform、AWS 或 Google Cloud 加入這項公測。

🔗 來源
- 標題：Zero data retention with Enterprise Frontier Safeguards is now in beta
- 作者／機構：Anthropic
- 連結：https://claude.com/resources/articles/zero-data-retention-with-enterprise-frontier-safeguards

#Anthropic #Claude #AISecurity #DataPrivacy #ZeroDataRetention #EnterpriseAI #CyberSecurity #AIGovernance #CloudSecurity #ThreatIntelligence
