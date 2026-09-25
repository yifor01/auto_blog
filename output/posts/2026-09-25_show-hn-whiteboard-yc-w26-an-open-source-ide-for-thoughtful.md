---
title: 'Show HN: Whiteboard (YC W26) – An open-source IDE for thoughtful software
  design'
source: Hacker News
url: https://github.com/devdotfast/whiteboard
model: claude-code/sonnet
generated_at: '2026-09-25T20:51:30.986580'
score: 93
---

📌 Whiteboard：讓人類與AI Agent一起畫架構圖的開源IDE

TL;DR：YC新創打造開源桌面應用，讓人類與coding agent在同一個畫布上共同設計軟體架構。

當agentic coding讓PR速度暴增，四個曾任技術主管的工程師卻發現一個副作用：越來越多程式碼合併進系統時，團隊已經看不懂agent做了什麼決定。這種「看不懂自己系統」的感覺，他們稱之為「認知債務」。

🤔 agentic coding的甜蜜與代價

Whiteboard的四位創辦人Sid、Alex、Ketan、Milan都是在agentic coding成為業界標配前夕辭去技術主管職位的工程師。他們在打造前一個產品的MVP時發現，一邊享受agent帶來的開發速度，一邊卻難以維持一個「可理解」的程式碼庫；當愈來愈多PR在他們沒有完全理解的情況下被合併，這種認知債務逐漸累積，最後連他們自己都難以再對系統做出貢獻。

🧩 從HTML artifact到基於VSCode重建

團隊最初以HTML artifact做出MVP，但很快遇到限制，於是重新設計出三個核心能力：

- **底層基於CodeOSS（即VSCode核心）打造**：純HTML工具很難把規格書或架構圖與程式碼連結起來。在Whiteboard中，點擊循序圖（sequence diagram）、實體關聯圖（ER diagram）或agent執行軌跡中的一句話，都能直接跳轉到對應的程式碼；瀏覽程式碼時也能沿用VSCode原生的快捷鍵與LSP支援。團隊認為這點格外重要，因為許多技術取捨往往要等第一版實作完成後才會浮現。
- **用Rust寫的語意diff檢視器**：這是一個具備AST感知能力的diff工具，讓使用者只看到與自己相關的程式碼變更。系統預設會把大型新增函式摘要成虛擬碼（pseudocode），並自動摺疊或隱藏單元測試與大量文件異動；整個行為可透過一套WASM外掛系統自訂。
- **決策紀錄（Decision Log）**：團隊發現很難掌握agent自主做出的一連串決策，因此打造工具讓agent能查詢並將自己的執行軌跡連結回Whiteboard，方便使用者理解自己設定的需求如何被實作，以及agent中途自主做了哪些判斷。

🧩 怎麼用

Whiteboard可整合現有的coding agent工具，例如Claude Code、Codex等，並提供一套SDK讓agent能在應用內的畫布上繪圖說明自己的工作內容。目前提供macOS與Linux版本的桌面應用安裝，整個專案以MIT授權開源。

📊 誰在用

README指出，Salesforce、Modal等公司的團隊已將Whiteboard用作架構或規格層級異動的審查工具，主要有兩種使用情境：一是審查自己agent的工作成果，讓agent先產出原型與對應的Whiteboard session，再據此討論設計；二是審查他人的異動，團隊發現Whiteboard與Greptile這類工具搭配使用效果不錯，先用自動化程式碼審查工具處理小型異動，再把需要人類判斷的變更升級到Whiteboard session中討論。

💡 深入分析

Whiteboard的價值主張不是憑空造新工具，而是把VSCode既有的LSP、跳轉、快捷鍵能力，疊加上一層diff可視化與決策追溯機制，讓agent的產出重新變得「可審查」。這種選擇務實：與其重造一套編輯器基礎設施，不如站在CodeOSS的肩膀上，專注在agent協作這個新問題上。

⚠️ 限制

目前釋出的是桌面應用，安裝僅支援macOS與Linux；團隊規劃未來推出付費的託管網頁版，加入session建立管理、執行軌跡儲存與多人協作審查等功能，但強調核心功能會維持可自架（self-hostable）。

🎯 實務啟示

如果你的團隊已經大量採用coding agent，卻開始感受到PR審查跟不上產出速度、或愈來愈難解釋系統為何長成這樣，Whiteboard提供的「diff只看相關變更＋決策可追溯」思路值得參考：與其事後補審查，不如把架構討論搬到agent產出程式碼的同一個工作流程裡。

🔗 來源
- 標題：Show HN: Whiteboard (YC W26) – An open-source IDE for thoughtful software design
- 作者／機構：sidharthkmenon（Whiteboard團隊）
- 連結：https://github.com/devdotfast/whiteboard

#OpenSource #DeveloperTools #AIAgent #CodingAgent #IDE #VSCode #SoftwareArchitecture #YCombinator #AST #CodeReview
