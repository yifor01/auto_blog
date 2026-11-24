---
title: A more tailored Google Search that’s uniquely yours
source: Google AI Blog
url: https://blog.google/products-and-platforms/products/search/google-search-personal-intelligence-apps/
model: claude-code/sonnet
generated_at: '2026-11-24T03:25:14.645817'
pinned: true
---

📌 Google 搜尋接上錢包與雲端硬碟,答案開始懂你的生活細節

TL;DR：Google Search 的 Personal Intelligence 新增 Wallet、Drive 與 Gemini app 串接,授權後答案能貼合你的真實情境。

過去問 Google「這個月該怎麼省錢」,得到的大概是一篇通用理財文章。如果你同意把 Google Wallet 的消費紀錄授權給 Search,它能不能直接根據你實際的花費習慣給建議?Google 這次的更新,就是朝這個方向邁進。

🤔 **個人化情境一直缺了財務與文件這兩塊**

Google Search 的 Personal Intelligence 原本已經能串接 Gmail、Calendar 與 Photos,但使用者的財務狀況與散落在各處的文件,一直沒有被納入這套個人情境系統。Robby Stein（Google Search 產品副總裁）指出,最有幫助的搜尋體驗需要同時結合全球資訊與「專屬於你」的情境,而這正是這次更新要補上的缺口。

🧩 **從今天開始,陸續開放三項串接**

從今天起,使用者可以選擇在 AI Mode 中把 Google Wallet 安全地串接到 Personal Intelligence,Drive 與 Gemini app 的支援則會在未來幾週跟進:

- **Google Wallet**:串接後可以梳理財務目標、找出日常可以省錢的地方,並根據已連結的信用卡最佳化現金回饋、旅遊優惠與點數累積。官方特別說明,AI Mode 只能讀取帳戶資訊,無法代為轉帳、管理或投資資金。
- **Google Drive**:把散落在文件、試算表、PDF 裡的資訊整合起來,產生像是「報稅季節前的個人化準備計畫」這類回應,不用自己手動把資料拼在一起。
- **Gemini app**:未來幾週開始,在 Gemini app 探索過的想法可以延續到 AI Mode 裡繼續發展,反過來也一樣。使用者原本就能選擇把 Search 歷史接進 Gemini app 的 Personal Intelligence,之後則可以反向把 Gemini app 接進 AI Mode。

啟用方式很直接:打開 Search Personalization 設定,選擇「Connected Apps」,再勾選要連結的 App 即可,使用者自行決定是否、何時開啟,也能隨時關閉。

📊 **搜尋串也能接續上次的情境**

這次更新也讓 AI Overviews 與 AI Mode 的回答更貼近使用者近期的搜尋情境,例如先前在規劃一趟旅行,之後開新的搜尋串時可以直接接續上次的進度,不用重新描述一次背景。

💡 **可視化情境來源,也能隨口糾正**

官方提到,接下來使用者將能透過每則個人化回答下方的「Personalization」圖示,查看這次回答實際用了哪些個人情境資料;如果資料已經過時,例如「我已經不吃素了」,也可以直接在對話串裡告訴 AI Mode 修改,不需要跑到設定頁翻找。這種「來源可視化 + 隨時可修正」的設計,一定程度回應了個人化系統常被質疑的黑箱問題。

⚠️ **目前仍是逐步開放中**

目前只有 Google Wallet 正式開始推出串接,Drive 與 Gemini app 的支援都還是「未來幾週內跟進」,尚未全面上線。此外,Wallet 的串接明確限定為「只能讀取、不能操作資金」,這是官方畫出的安全邊界。

🎯 **實務啟示**

對開發個人化助理或 RAG 系統的工程師來說,這次更新示範了一套值得參考的個人情境資料治理模式:採 opt-in 制、把所有連結集中在一個設定頁管理,並讓使用者看得到、改得動系統實際用了哪些資料。這些細節往往比模型本身的能力更決定一個個人化產品能不能被使用者信任。

🔗 **來源**
- 標題：A more tailored Google Search that's uniquely yours
- 作者／機構：Google — Robby Stein
- 連結：https://blog.google/products-and-platforms/products/search/google-search-personal-intelligence-apps/

#GoogleSearch #AIMode #PersonalIntelligence #GoogleWallet #GoogleDrive #Gemini #Personalization #SearchAI #PrivacyByDesign #ProductUpdate
