---
title: Making global data easier to explore
source: Google AI Blog
url: https://blog.google/innovation-and-ai/technology/ai/google-un-data-commons-platform/
model: claude-code/sonnet
generated_at: '2026-09-17T20:26:06.520552'
pinned: true
---

📌 【Google】聯合國全球統計資料，變成一張可以直接問的知識圖譜

TL;DR：UN System Data Commons 用 AI-ready 知識圖譜整合聯合國各機構統計資料，查資料像聊天一樣簡單。

過去要拿到跨機構的聯合國統計數據，分析師往往得先花上好幾個月做格式清理與欄位比對，才能真正開始分析。Google 與聯合國系統合作，試圖用一張互聯的知識圖譜終結這個瓶頸。

🤔 資料散落在各自為政的系統裡

聯合國體系內各機構每年都會彙整用來追蹤公共衛生、貧窮、教育等議題的高品質統計資料，但這些數據長期分散在不同組織、甚至同一組織內部互不相容的格式中。要把不同資料集串起來做交叉分析，往往意味著大量人工整理工作。

🧩 建立在 Data Commons 之上的開放平臺

UN System Data Commons 是建立在 Google 的 Data Commons 之上的開放原始碼平臺，將指標、時間軸、地理邊界自動整合進同一個可互聯的環境，形成所謂的「AI-ready 知識圖譜」。這個專案由 Google.org 提供資金支持 UN Foundation 推動。

平臺提供自然語言查詢功能，使用者可以直接用一般語言提問，例如「乾淨飲用水的取得如何影響鄉村地區的就學率」「過去十年有多少人新獲得電力供應」「不同地區的預期壽命如何變化」，系統就會回傳對應的資料與互動式視覺化圖表。若偏好瀏覽，也可以透過 Explore 分頁依地區或健康、教育等主題篩選資料，Blog 區塊則提供把複雜趨勢整理成易讀報告的內容，例如運用 UNICEF 資料分析降低兒童貧窮的有效做法。

平臺也基於 Model Context Protocol（MCP）等開放標準，讓 AI agent 能自主從 UN System Data Commons 抓取權威數據，串接不同領域的資訊，並組合成圖表、資訊圖或報告草稿。

📊 資料是經過驗證的，但引用前仍要複查來源

每一份資料集都經過聯合國系統統計專家與技術人員驗證，確保回答立足於可信的官方事實。不過官方也提醒，即使數據已經過驗證，在引用關鍵數字前仍應複查原始來源。

未來一年，聯合國系統將持續加入更多機構的資料集，目標是在 2027 年前涵蓋 80% 的聯合國系統統計資料。

🎯 實務啟示

對開發 AI agent 或做資料密集型應用的工程師來說，這個案例展示了「知識圖譜 + MCP + 自然語言介面」的組合如何把散亂的權威資料變成可被 agent 直接消費的資源。若你的產品需要串接可信的公開統計數據，UN System Data Commons 值得列入資料來源評估清單。

🔗 來源
- 標題：Making global data easier to explore
- 作者／機構：Google — Prem Ramaswami
- 連結：https://blog.google/innovation-and-ai/technology/ai/google-un-data-commons-platform/

#GoogleAI #DataCommons #UnitedNations #KnowledgeGraph #OpenData #MCP #AIAgents #NaturalLanguageSearch #GlobalDevelopment #OpenSource
