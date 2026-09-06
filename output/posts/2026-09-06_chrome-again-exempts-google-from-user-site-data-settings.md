---
title: Chrome again exempts Google from user site data settings
source: Hacker News
url: https://lapcatsoftware.com/articles/2026/9/1.html
model: claude-code/sonnet
generated_at: '2026-09-06T19:21:50.252040'
score: 32
---

📌 Chrome 152 版重演舊症頭：Google 網站又躲過你的隱私清除設定

TL;DR：六年前修好的 Chrome bug 疑似死灰復燃，google.com 的 cookie 不受「關閉視窗自動清除」規則約束。

如果你把 Chrome 設定成「關閉所有視窗時清除網站資料」，理論上這條規則對所有網站一視同仁。但一位獨立研究者最近發現，Chrome 又出現了六年前同一位作者曾公開揭露、並促使 Google 修復過的老問題：google.com 的資料，再次成為例外。

🤔 **一個曾經修好的 bug，六年後又出現**

這位在 Hacker News 上以 ExMachina73 帳號分享的作者，曾在六年前發表過一篇文章，指出 Chrome 有個 bug 會讓 Google 自家網站豁免於「自動清除所有網站資料」的設定，該文章當時引來 Michael Tsai、Hacker News、The Register、The Verge、Gizmodo 等多方關注，Google 後來也確實修復了問題。如今作者表示，自己又在 Chrome 152.0.7977.83 版上，於兩臺不同的 Mac 上重現了類似的狀況。

🧩 **重現方式：關掉視窗，Google 的資料卻留下來了**

作者為了排除「預設搜尋引擎是 Google」這個變因，特地先把 Chrome 的預設搜尋引擎改成 DuckDuckGo。接著確認 chrome://settings/content/siteData 的預設行為是「關閉所有視窗時刪除網站儲存的資料」，同時他也沒有登入 Chrome 帳號，並且關閉了 Chrome 登入功能。此時檢查 chrome://settings/content/all，確認沒有任何網站資料存在。

接著他關閉 Chrome 唯一開啟的視窗，再次回到 chrome://settings/content/all，卻發現多出了 google.com 的網站資料。即使結束並重新啟動 Chrome，這份資料依然存在。他刪除該資料後重複整個流程，同樣的情況再次發生。

📊 **只有 google.com 被放過，資料類型包含 Cookie 與本機儲存**

根據作者的觀察，就他所測試的範圍而言，www.google.com 似乎是唯一被排除在清除規則之外的網站。他進一步檢查 ~/Library/Application Support/Google/Chrome/Default 資料夾，發現被保留下來的資料包含 Cookies、Local Storage 與 Session Storage。

💡 **無心之過，還是把關不嚴？**

作者表示自己傾向採用「Hanlon's razor」（能用無能解釋的，就不要訴諸陰謀論），並不認為這是 Google 刻意為之。不過他也直言，以 Google 的營收規模與工程團隊的資源來看，這樣的疏漏並無藉口，並半開玩笑地建議 Google 針對這項功能補上單元測試，戲仿 Facebook 那句「move fast and break things」，改說「move slower and don't break things」。他也提到自己平常主要使用 Safari，只有在測試時才頻繁開啟 Chrome 與 Firefox。

⚠️ **時間點與成因仍不明**

作者坦言不確定這個問題是何時被引入的，目前也只是基於自己在兩臺 Mac 上的重現結果做出的觀察，並未說明 Google 官方是否已經知情或著手調查。

🎯 **對工程師的提醒：隱私設定不能只信任 UI 顯示**

對於需要處理使用者隱私或資料清除邏輯的工程師來說，這類案例是個提醒：涉及第三方瀏覽器內建設定的行為，最好透過實測驗證，而不是單純相信設定頁面文字描述。若你的產品仰賴 Chrome 的「關閉視窗清除資料」機制來保護使用者隱私，值得自行測試是否有類似的例外狀況。

🔗 **來源**
- 標題：Chrome again exempts Google from user site data settings
- 作者／機構：ExMachina73
- 連結：https://lapcatsoftware.com/articles/2026/9/1.html

#Chrome #GoogleChrome #Privacy #WebPrivacy #Cookies #BrowserSecurity #BigTech #DataPrivacy #Google #TechNews
