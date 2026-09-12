---
title: 'google.com/goto: Google''s anti-scraping update'
source: Hacker News
url: https://www.autom.dev/blog/google-search-goto-links
model: claude-code/sonnet
generated_at: '2026-09-12T19:36:29.413152'
score: 57
---

📌 Google 搜尋悄悄換招:結果連結不再直接給網址

TL;DR：Google 將搜尋結果連結改寫成 /goto 中介頁,大幅提高大規模爬取 SERP 的成本。

如果你曾寫過程式去解析 Google 搜尋結果頁面,接下來這個改動可能會讓你的爬蟲直接失靈:結果連結裡看到的,不再是目標網站的網址。

🤔 **從明文網址到不透明代碼**

過去 Google 也用過重導向包裝,格式是 `google.com/url?q=[目標網址]`,查詢字串裡的目標網址是可直接讀出的明文。但根據 autom.dev 的觀察,新的格式改成 `google.com/goto?url=...`,其中的 `url=` 參數是 Google 自訂的不透明編碼,並非單純的 base64,更像是指向 Google 索引記錄的一個內部代碼。文章指出,這個變化在 2026 年 8 月底開始,於登出或無痕瀏覽狀態下的搜尋結果中「一致地」出現,不再只是小範圍實驗。

🧩 **要拿到真實網址,得反過來問 Google**

新機制下,結果連結的 `href` 本身就是 `/goto`,而非目的頁面;`url=` 這串代碼無法離線解碼;真正的目標網址,只存在於 Google 針對該連結回應的 HTTP `Location` header 中。也就是說,要取得目的地網址,必須對 `/goto` 發出請求並讀取 `Location`,但不能真的跟著重導向走到那個頁面。文章也提到,由於 Google 為了在搜尋結果頁上顯示網域、favicon 等資訊,仍需要保留網址的部分副本在頁面上,這與「讀取 Location」是兩回事。

💡 **劍指大規模 SERP 爬取**

作者將此舉放在 Google 近期一系列反爬蟲動作的脈絡下解讀,包括先前移除 `&num=100` 參數、加強 BotGuard/SearchGuard 等,認為這是針對 AI 爬蟲與 SEO 工具「批次擷取結果網址、自建索引」行為的持續加壓。過去爬蟲只需解析一次 HTML 就能拿到成千上萬個網址;現在每一個結果都得回頭再向 Google 發一次請求才能得知目的地,這讓爬取行為變慢、變吵雜,也讓 Google 更容易辨識出「同一個 client 短時間內密集解析大量連結」的異常模式。

⚠️ **仍可能是進行中的實驗**

文章作者也坦言,這個改動目前可能仍處於實驗階段,他們一開始只在小部分 SERP 上看到 `/goto` 格式,直到近期才變得普遍且穩定。這意味著格式本身未來仍有調整空間,依賴此機制的第三方服務需要持續追蹤。

🎯 **實務啟示**

如果你的產品依賴解析 Google 搜尋結果頁面來取得目標網址,現在的做法(直接從 HTML 讀網址)可能已經失效。務必改成對 `/goto` 連結發送 HEAD 請求、讀取 `Location` header 取得真實網址,且不要跟隨重導向,以免產生不必要的流量與延遲。

🔗 **來源**
- 標題：google.com/goto: Google's anti-scraping update
- 作者／機構：1e1a, Hacker News(原文出處 autom.dev)
- 連結：https://www.autom.dev/blog/google-search-goto-links

#GoogleSearch #WebScraping #SEO #SERP #AntiScraping #SearchEngineering #DataEngineering #WebCrawling #APIDesign #TechInfrastructure
