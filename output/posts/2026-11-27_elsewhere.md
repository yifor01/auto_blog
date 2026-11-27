---
title: Elsewhere
source: Simon Willison
url: https://simonwillison.net/elsewhere/
model: claude-code/sonnet
generated_at: '2026-11-27T01:22:21.709669'
score: 46
---

📌 Datasette 新圖表外掛：SQL 聚合百萬行資料後再畫圖

TL;DR：datasette-charts 外掛讓任意資料表或 SQL 查詢都能自動建議圖表,並交給 Datasette Agent 用自然語言生成標註圖。

以前的 Datasette 圖表外掛只能畫出「目前這一頁」最多 100 列的資料;這次 Simon Willison 想解的,是讓整個結果集,哪怕上百萬列,都能被畫進一張圖裡。

🤔 **背景或問題**

Willison 在自己的 Elsewhere 連結彙整中提到,過去像 datasette-vega 這類視覺化外掛,只會對目前分頁顯示的資料畫圖,通常就是前 100 列。這對只想快速看一眼資料全貌的使用者並不夠用,他形容這是自己想了「一年多」的問題。

🧩 **核心架構**

新外掛 datasette-charts 可以對 Datasette 裡任何資料表或任意 SQL 查詢運作。它內建多種圖表類型(底層 vendor 了 D3、Observable Plot 與 topojson-client),並為每種類型定義一套啟發式規則,用來判斷目前這組資料列適合哪種圖。畫面最上方出現的建議縮圖本身就是依據真實資料算出來的視覺化結果,點選後會進入完整圖表與調整工具,也可以手動從零建立圖表。

最關鍵的設計是：圖表會把整個結果集納入計算,而不只是目前頁面。做法是把每張圖編譯成一條 SQL 查詢,用 GROUP BY、時間分桶與 window function 對整個結果集(可能是數百萬列)做聚合,回傳結果上限設為 5,000 列供顯示;對於大型資料表的圖表建議,則用取樣方式避免要掃過整份資料。圖表目前的狀態會持久化在網址的 #fragment 裡,因此可以直接加入書籤或分享給別人。這次更新還加入了圖表標註功能,可以疊加線條、色塊區域、文字標籤,三者也能組合使用。

🧩 **怎麼用**

外掛已經整合進 Datasette Agent,使用者可以直接用自然語言請 agent 畫圖,例如在 agent.datasette.io 的 demo 上輸入「比較我標記為 LLM 的內容和標記為 Datasette 的內容,畫成圖並加上標註」,agent 就會呼叫同一套圖表建議與生成工具產出結果。這次也改進了 Datasette Agent 的聊天側邊 iframe 導覽機制,讓它可以透過 fragment hash 跟其他會改變 URL 狀態的外掛做更深的整合。

💡 **深入分析**

Willison 提到這個 prototype 是用 Claude Fable 5.2 一次做出來的,效果好到直接從原型變成正式外掛。這也呼應他在其他幾篇筆記中的做法——例如用同一個模型做了一個比較 HTML `<select>` 樣式在不同瀏覽器下的展示頁,以及幾乎一次成功做出 Apache Arrow 串流匯出外掛(datasette-arrows),都是先有 Datasette 核心的外掛機制(如新的 register_output_renderer() streaming 支援),再用 coding agent 快速落地成可用工具。

⚠️ **限制**

作者自己標註這仍是 alpha 版本(0.2a0);目前主分支雖然已經把 Arrow 這類串流格式歸到「全部列」匯出選項裡,但最新正式發布版尚未把它跟 CSV、TSV 分到同一群組,要等下一個 alpha 才會加上;大型資料表的圖表建議仍依賴取樣,而非真正算過全部資料。

🎯 **實務啟示**

如果你自己在做內部資料視覺化工具,「把聚合邏輯下推到 SQL(GROUP BY、時間分桶、window function),只把有限列數的聚合結果送到前端」是避免大資料集撐爆瀏覽器記憶體的實用模式;把圖表狀態存進 URL fragment,則是讓視覺化結果可以被書籤、分享、甚至被其他外掛透過 hash 導覽整合的簡單做法。

🔗 **來源**
- 標題：Elsewhere
- 作者／機構：Simon Willison
- 連結：https://simonwillison.net/elsewhere/

#Datasette #DataVisualization #SQL #OpenSource #D3 #ClaudeFable #AIAgents #WebDev #DataEngineering #Python
