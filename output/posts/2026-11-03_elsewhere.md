---
title: Elsewhere
source: Simon Willison
url: https://simonwillison.net/elsewhere/
model: claude-code/sonnet
generated_at: '2026-11-03T22:45:31.622637'
score: 72
---

📌 Simon Willison 的兩個月雜記:AI 幫忙審 PR,也幫忙寫出一個「看不懂」的 SPARQL 引擎

TL;DR:LLM CLI 作者彙整兩個月的小更新,重點是用 Claude 處理社群 PR 的心得,以及一次失控生成滿滿 Rust 程式碼的實驗。

當很多開源維護者在抱怨 AI 生成的 PR 淹沒信箱時,Simon Willison 卻說這對他的 LLM 專案反而不是問題,原因很直接:他讓 Opus 5.5 或 GPT-6 Astra 先幫忙分類。

🤔 LLM CLI 工具兩個月來的小更新

這篇雜記彙整了 Simon 的 LLM CLI 工具與 Python library 近兩個月的累積功能與修正。新增了 gpt-6.1-sol 與 gpt-6.1-terra 兩個模型,以及一個新的 llm openai endpoint add 指令,方便設定使用 OpenAI 相容端點的其他模型。若使用者沒有自訂預設模型,系統預設模型從 gpt-5.6-luna 換成了 gpt-6-luna,價格只有前者的一半。embeddings 功能現在也接受不同的二進位內容可以有不同的 content-type,這是支援像 Gemini Embedding 2 這類可以對文字、音訊、圖片、影片做 embedding 的模型所必需的調整。

💡 AI 協作審查 PR 的心得:當成附範例的 bug report

Simon 提到,許多開源維護者抱怨 AI 輔助產生的 PR 大量湧入造成負擔,但 LLM 是他受影響最深的專案,他卻不覺得這是問題,主因是他讓 Opus 5.5 或 GPT-6 Astra 協助做初步分類,找出最有用的修正。這個版本收到了 12 位作者貢獻的修正,幾乎全部都是 AI 協助完成,但審查負擔遠低於他原本的預期。他形容自己其實是把這些 PR 當成「附帶範例的 bug report」來看:有時候直接採用,有時候則自己動手實作修正方案。

🧩 其他小專案:webframe、影像裁切工具、四人連線 Battledrones

文中也提到幾個相關小專案的進展。datasette-llm 外掛(支撐 Datasette Agent)現在會自動沿用 LLM 設定的預設模型,使用者不再需要額外指定模型才能開始使用。webframe 是 Jeff Lindsay 的專案,讓使用者可以「像執行程式一樣執行一個網頁」:指向一個 URL 或檔案,它會在隱藏的 headless 瀏覽器中執行,把 console.log() 輸出到標準輸出、例外訊息輸出到標準錯誤;它用 Go 搭配 glaze library 寫成,透過系統原生瀏覽器(macOS 上的 WKWebView、Linux 上的 WebKitGTK、Windows 上的 WebView2)運作,不需要內建自己的瀏覽器引擎。Simon 覺得這讓他想起自己做的 shot-scraper,但體積小得多,也不依賴 Playwright,他讓 Claude Opus 5.5 實測並寫了一份評估報告,把它拿來跟 shot-scraper 的使用模式做對照。另外還有一個很特定的小工具:在圖片上畫一條水平或垂直切線,再讓切線兩側相對滑動,藉此裁掉圖片中間的一段內容,他做這個工具是為了處理用 Tailor 在 iPhone 上拼接出的長截圖。遊戲專案 Battledrones 也新增了四人連線模式(先前地圖只支援兩人),Claude Opus 5.5 加了一張具有四向旋轉對稱性的新地圖「Compass Rose」,並修改了 WebSocket 連線的多人對戰網路程式碼以支援最多四名玩家,新增紫色與綠色機器人隊伍,加入原有的藍、紅兩隊。

⚠️ 一次「churn 超過 12 小時」的失控實驗

Simon 也記錄了一次用 Claude Code for web 在「Ultracode」模式(動態協調多個 subagent 的工作流)下跑的研究任務。他原本的提示是要寫一個用 Rust 實作、能直接操作資料列(他提到自己把「hit the rows directly」誤打成帶有 delete 字樣的句子)以加速查詢的 SQLite SPARQL 擴展,結果這個任務讓 Claude Code for web 持續運作超過 12 小時。隔天他只追加了一個後續提示,要求在 crates/ 目錄下每個資料夾加上 README,並附上教使用者安裝、在 SQLite CLI 中執行、學習 SPARQL 與擴展用法的 tutorial.md,以及一個產生範例資料的腳本。他形容這整個產出是「次世代的 vibe coding」:程式碼量大到完全不可能逐行審查,甚至連跟著文件操作一遍都是不小的工作量。他坦言自己現在手上有一個似乎是完整的、在 SQLite 裡用 Rust 實作的 SPARQL 引擎,但不確定該怎麼處理,因為這是一時興起做出來的,他也不打算投入足夠時間真正弄懂它的能力範圍。

🎯 實務啟示

這篇雜記提供的不是單一技術突破,而是一種對「AI 協作維護開源專案」與「長時間自主 agent 生成」現狀的第一手觀察:社群 PR 氾濫的問題,可以靠讓 AI 先做分類與摘要來緩解,把 PR 當成帶範例的 bug report 處理;但另一方面,放手讓 agent 長時間自主運作,也可能產出規模遠超過人力可審查範圍的程式碼,帶來「產出看似完整,卻無法驗證與真正掌握」的新風險。工程團隊若打算採用類似的長時間自主生成流程,應該提前想清楚審查與驗收的邊界在哪裡。

🔗 來源
- 標題:Elsewhere
- 作者／機構:Simon Willison
- 連結:https://simonwillison.net/elsewhere/

#LLMCLI #OpenSource #AIAssistedCoding #ClaudeCode #PromptEngineering #DeveloperTools #VibeCoding #SQLite #SPARQL #AIAgents
