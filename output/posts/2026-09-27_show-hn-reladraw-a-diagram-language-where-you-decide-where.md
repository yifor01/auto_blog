---
title: 'Show HN: Reladraw – A diagram language where you decide where to place things'
source: Hacker News
url: https://github.com/reladraw/reladraw
model: claude-code/sonnet
generated_at: '2026-09-27T20:13:46.524991'
score: 85
---

📌 Reladraw：讓你自己決定圖表長什麼樣子

TL;DR：一款兼顧「圖表語言」與「手動排版控制權」的新工具,對人類與AI agent都友善。

畫架構圖時你是不是也常卡在這個兩難：用Mermaid這類語言很快,但排版永遠不是你想要的樣子;改用Draw.io能完全掌控畫面,卻要一格一格手動拖,慢得讓人心累。

🤔 自動排版與手動繪圖之間,一直缺一個選項

作者在專案說明中提到,目前畫圖表的選項大致分成兩類：一類是像Mermaid、Graphviz這樣的自動排版語言,好處是能用語言定義內容,但排版結果由演算法決定,使用者無法自己決定圖表最終長相;另一類則是Draw.io這樣的軟體,雖然功能強大、排版自由,卻相當耗時,而且對agent來說也不容易操作。作者想做的是同時保留兩邊的優點：可以用類似圖表語言的方式定義內容,同時保有對排版位置的高度控制,並且讓這套工具對人類和agent都好用。

🧩 用語言定義內容,但位置自己說了算

Reladraw的核心設計理念,就是在「圖表語言」的框架下,把位置決定權交還給使用者,而不是像Mermaid、Graphviz那樣完全交由自動佈局演算法處理。

🧩 怎麼上手

專案的GitHub頁面提供了一個線上playground,不需要安裝就能直接試用;此外也附上了簡單的npm install安裝說明,以及一份可以搭配Claude或其他agent使用的skill安裝教學,方便把Reladraw整合進agent工作流程中。

🎯 實務啟示

如果你的工作流程裡常需要產生或修改架構圖、流程圖,而且不想每次都在Mermaid的自動排版結果上手動微調,Reladraw提供的「語言定義+手動排版」組合值得先在playground試一下手感,尤其是若你打算讓agent也參與繪圖與修改,這類對agent操作友善的設計會比傳統圖形化工具更方便串接。

🔗 來源
- 標題：Show HN: Reladraw – A diagram language where you decide where to place things
- 作者／機構：jpwalsh234／Hacker News
- 連結：https://github.com/reladraw/reladraw

#DiagramTools #DeveloperTools #OpenSource #AIAgents #Mermaid #Graphviz #DevEx #Productivity #ShowHN #SoftwareTools
