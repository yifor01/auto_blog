---
title: Get ready for the game with new football features in Search
source: Google AI Blog
url: https://blog.google/products-and-platforms/products/search/football-features-google-search/
model: claude-code/sonnet
generated_at: '2026-09-09T19:53:52.347337'
pinned: true
---

📌 Google Search 導入 AI Mode，幫你操盤 Fantasy Football 陣容

TL;DR：Google Search 新增 Live Game Feed 與 AI Mode fantasy 建議，把即時賽事資訊與個人化決策整合進搜尋。

美式足球球季開打，你還在多個 App 之間切換戰況、陣容與數據？Google 打算把這件事一次收進 Search。

🏈 即時戰況直接進搜尋結果

素材指出，Google Search 推出 Live Game Feed（即時賽事動態），使用者搜尋正在進行的比賽，點選紅色「Live」圖示，就能看到比賽回顧、play-by-play 動態時間軸、社群熱門評論、精華影片，以及 AI 產生的洞察（AI-powered insights）。目前先在美國以英文於行動裝置上開放給職業球隊比賽，本月稍後才會擴大到大學球隊與更多地區。

🏆 一次看懂賽況、排名與數據

搜尋對戰組合時，新增的輪播（carousel）讓使用者不必逐一搜尋就能看到聯盟其他賽事的比分；同時上線的還有聯盟數據排行（如 passing touchdowns、rushing yards）以及更細的球員數據（sacks、fumbles、yards after catch）。官方表示稍後還會加入冠軍賠率預測與季後賽對戰圖（brackets）。這些更新將於行動裝置上全球開放。

🎯 AI Mode 接管你的 Fantasy 陣容決策

真正對 AI 工程師有意思的是 fantasy football 整合：使用者可以將 Yahoo Fantasy 或 Sleeper 帳號連結到 Search，透過 AI Mode 取得客製化建議。連結後，AI Mode 能讀取使用者的即時陣容與所有聯盟資訊，提供 start/sit 建議、waiver wire（自由市場）目標人選，甚至能評估選秀結果或提供每週聯盟動態摘要，不需要手動輸入資料或截圖。這項功能目前僅在美國以英文開放。

💡 觀察：把個人化資料接入對話式 AI 的實例

這個案例展示了一個典型模式：把使用者的私有結構化資料（fantasy 陣容、聯盟設定）透過授權連結接入 AI Mode，讓對話式助手能基於即時個人情境給出建議，而不只是回答通用問題。這種「連結帳號 → 授權讀取 → AI 生成個人化建議」的架構，值得做 agent 或個人化助理產品的工程師參考。

🎯 實務啟示

如果你正在打造需要串接第三方帳號資料的 AI 助理功能，這個案例提供一個現成的使用者體驗範本：先讓使用者以自然語言提出需求（「幫我看 fantasy 陣容」），再引導出安全連結帳號的選項，把授權流程嵌入對話而非另開設定頁面。

🔗 來源
- 標題：Get ready for the game with new football features in Search
- 作者／機構：Google — Denise Ho
- 連結：https://blog.google/products-and-platforms/products/search/football-features-google-search/

#GoogleSearch #AIMode #FantasyFootball #ConversationalAI #Personalization #GenerativeAI #ProductLaunch #SportsTech #GoogleAI #LLMApps
