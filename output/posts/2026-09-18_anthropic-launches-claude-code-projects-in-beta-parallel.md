---
title: 'Anthropic Launches Claude Code Projects in Beta: Parallel Cloud Sessions That
  Keep Running After You Close Your Laptop'
source: MarkTechPost
url: https://www.marktechpost.com/2026/09/17/anthropic-launches-claude-code-projects-in-beta-parallel-cloud-sessions-that-keep-running-after-you-close-your-laptop/
model: claude-code/sonnet
generated_at: '2026-09-18T19:47:11.499181'
score: 98
---

📌 拆解Claude Code Projects:協調器怎麼把工作拆給雲端Thread

TL;DR:Anthropic重新設計的Claude Code Projects用「協調器+雲端Thread」兩層架構,讓工作在你關上筆電後依然繼續跑。

一個對話,自己分裂成多個平行的雲端session,還能各自開PR、自己修CI失敗——這是MarkTechPost對Claude Code Projects新架構的描述。

🤔 舊版Project只是資料夾,新版是一段持續進行的對話

舊版的Project本質上是一個資料夾:放一些檔案加一段對話。新版則變成一段持續進行的對話,由Claude擔任協調器(coordinator)角色。你描述要做的工作,由Claude決定哪些內容應該變成一個獨立的thread。每個thread都是一個完整的Claude Code雲端session,執行在自己的分支與自己的一份程式碼庫副本上,平行執行、向對話回報進度,並且在你關上筆電後仍會持續執行。

🧩 兩層架構:協調器負責統籌,Thread負責幹活

Project conversation是協調器層,負責讀取你傳來的內容,就地回答簡單問題,並啟動thread去做實際的工作;它看得到的是thread回報的結果,而不是thread執行的每一個步驟。Thread則是實際幹活的工作單位,工作需要時會開出pull request,並在開啟auto-fix的情況下持續盯著這個PR——CI失敗就推送修正,檢查通過就回覆。每個thread還能再往下拆:透過subagent、loop與workflow把自己的任務進一步分派下去。官方舉的例子包括:設定「降低結帳頁p75延遲」這個目標,讓Claude對每個端點做profiling、測試最佳化方案,並在平行的thread裡分別開PR;另一個例子是跨API、網頁、行動裝置三個repository汰換已棄用的v1端點,每個repository各自一個thread,由Claude回報哪個PR先合併。當兩個thread改到同一段程式碼,衝突會以一般的git merge conflict形式浮現。

專案層級會設定一次「standing context」,並傳遞給每一個新啟動的thread,包括專案的repository與上傳檔案、最多16,000字元的專案說明,以及Claude透過MEMORY.md索引讀寫的專案記憶——例如「發布時間改到週五」或「碰觸帳務系統前要先問誰」。每個thread也會複製專案裡的每一個repository,並載入所有repository裡的CLAUDE.md、skills與plugin。權限規則、hook與環境變數的行為則有差異:它們只作用於thread啟動所在的目錄,因此單一repository的專案能正常套用,多repository的專案則不會。MCP工具透過你claude.ai帳號上的connector接入,project conversation本身沒有connector,因此涉及connector的工作必須交給thread執行。

📊 從Overview面板到200個thread的每日上限

Overview面板依狀態把thread分組:Ready for review、Waiting on you、Working、Landing、Idle與Resolved;Library分頁則彙整上傳的檔案以及thread產出的檔案。一個新專案預設在所有地方使用Opus模型,thread採高努力(high effort)、對話則採低努力(low effort),Anthropic也提供每個專案獨立的Usage分頁,以及分別給協調器與thread設定的模型與努力程度選項。系統設有硬性上限:每個帳號旗下所有專案每天最多能啟動200個新thread,若某個thread用完額度會自動等待並在額度恢復後接續執行。

⚠️ 一個專案吃額度的速度比單一session快

因為每個執行中的thread都是一個完整的session,一個專案消耗方案額度的速度會比單一session快得多。閒置中的thread也不是完全沉睡:一旦CI失敗或有人留下review comment,它們就會重新喚醒並繼續消耗額度。

🎯 實務啟示

在真正把大範圍重構丟給多個並行thread之前,值得先確認你的repository結構是否適合「單一thread對應單一目錄」的權限與hook套用邏輯,並在Usage分頁盯緊額度消耗,避免多個thread同時甦醒時把當月額度提前用完。

🔗 來源
- 標題:Anthropic Launches Claude Code Projects in Beta: Parallel Cloud Sessions That Keep Running After You Close Your Laptop
- 作者/機構:Michal Sutter,MarkTechPost
- 連結:https://www.marktechpost.com/2026/09/17/anthropic-launches-claude-code-projects-in-beta-parallel-cloud-sessions-that-keep-running-after-you-close-your-laptop/

#ClaudeCode #Anthropic #AIAgent #CloudComputing #DevTools #SoftwareEngineering #CodingAgent #MCP #GitWorkflow #Automation
