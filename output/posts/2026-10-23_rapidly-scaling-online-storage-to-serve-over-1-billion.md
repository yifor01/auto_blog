---
title: Rapidly scaling online storage to serve over 1 billion ChatGPT users (Part
  II)
source: OpenAI Blog
url: https://openai.com/index/scaling-storage-one-billion-users-part-two
model: claude-code/sonnet
generated_at: '2026-10-23T20:31:49.144853'
pinned: true
---

📌 OpenAI 揭露 Habitat 儲存架構，ChatGPT 讀取速度衝 12 倍

TL;DR：OpenAI 公開內部儲存系統 Habitat 如何靠多租戶機制與全域快取撐住 10 億使用者流量，讀取效能提升 12 倍。

當一個產品要同時服務超過 10 億名使用者，最先喊救命的往往不是運算資源，而是儲存層。OpenAI 在官方部落格的第二篇文章中，說明了他們如何處理 ChatGPT 背後這道難題。

🤔 **為何儲存會先撐不住**

隨著 ChatGPT 使用者突破 10 億，OpenAI 內部的線上儲存系統 Habitat 必須同時服務大量租戶（multi-tenancy），任何單一租戶的異常流量都不能拖垮整體服務的穩定性。

🧩 **靠多租戶隔離與全域快取撐起規模**

OpenAI 表示，他們為 Habitat 強化了可靠的多租戶（multi-tenancy）架構，並導入全域快取（global caching）層，同時採用 Azure Cosmos DB 作為底層資料庫服務。

📊 **讀取效能提升 12 倍**

這套組合讓 ChatGPT 的讀取速度達到原本的 12 倍，直接反映在終端使用者的回應延遲上。

🎯 **實務啟示**

當系統要擴展到十億級使用者規模，光靠加機器未必有效；多租戶隔離與快取策略的設計，往往才是決定能否撐住流量尖峰的關鍵。對正在設計高併發後端的工程師來說，這是一個值得參考的真實案例。

🔗 **來源**
- 標題：Rapidly scaling online storage to serve over 1 billion ChatGPT users (Part II)
- 作者／機構：OpenAI
- 連結：https://openai.com/index/scaling-storage-one-billion-users-part-two

#OpenAI #ChatGPT #DatabaseScaling #AzureCosmosDB #Multitenancy #DistributedSystems #Caching #SoftwareEngineering #Infrastructure #Scalability
