---
title: 'Projects redesigned: from folder to conversation'
source: Claude Blog
url: https://claude.com/blog/projects-redesigned
model: claude-code/sonnet
generated_at: '2026-09-17T20:27:54.650494'
pinned: true
---

📌 【Anthropic 官方發布】Claude Code Projects 大改版:從資料夾,變成一場對話

TL;DR:Claude Code 的 Projects 重新設計為「協調者 + 多執行緒」架構,讓 Claude 自己管理多工作業並行推進。

以前要同時開多個 session 做一個大專案,得自己拆工作、追進度、再手動把結果拼回去。現在在 Claude Code 的 project 裡,你只要說清楚目標,Claude 會自己拆解任務、分派給多個並行的 thread、審查產出,再把最終結果組裝起來。

🤔 從「管理多個視窗」到「交給一位協調者」

Anthropic 在 2026 年 9 月 17 日的部落格文章指出,過去管理跨多個 session 的建置工作,需要自己切分工作、處理交接、再把結果縫合。這次改版把 project 拆成兩層:負責執行的「thread」,以及負責調度的「coordinator」。你可以在手機上隨時介入調整進度,即使離開電腦,Claude 仍會持續工作。

文章給了兩個例子:設定一個目標是降低 checkout 流程的 p75 延遲,請 Claude 對每個 endpoint 做 profiling、測試最佳化方案,並在多個並行 thread 中開 PR;或是連接 API、網頁、行動裝置三個 repo,設定目標是淘汰一個已棄用的 v1 endpoint,Claude 會為每個 repo 各開一條 thread,負責搬移呼叫端、跑測試、開 PR,最後告訴你哪些該先合併。

🧩 Thread 做事,Coordinator 指揮

啟動一個 project 時,你要選定目標,以及要用的 repo 或情境資料。Claude 會先建議可以立即著手的工作。你可以設定這個 project 的雲端執行環境、connector、plugin、instructions 與使用的模型。日常你可以在主要的 project 對話中監看與引導整體進度,也可以深入個別 thread 檢視與調整細節。

文章形容,對 Claude 下 brief 的方式,就像對「幕僚長」交辦任務一樣,它會把工作路由到新開的或既有的 thread 上,並主動回報與追蹤進度。若專案連接了 repo,thread 會開 PR、跑測試;若連接的是文件,thread 會閱讀並起草內容。實際運作上,每個 thread 就是一個獨立的 Claude Code 雲端 session,在自己的分支與 repo 副本上工作。coordinator 負責維持整體秩序,但如果多個 thread 真的動到同一份程式碼,衝突就會像一般的 PR 一樣以 merge conflict 的形式呈現。每個 thread 還能再用 subagent、loop、workflow 把自己分配到的工作進一步拆解,讓大型任務更快完成。

💡 記憶會隨時間累積

Anthropic 表示,project 是為「長時間執行或具 agentic 特性的工作流程」設計的,也就是那些需要超過一次回覆、且包含多個部分的工作。隨著時間推進,Claude 會對這個 project 了解越多細節,並把這些細節套用到後續工作上。每一條 thread 現在都會往一個共享記憶庫寫入資訊,同時也會從裡面讀取,降低了複雜 prompt 工程的需求。文章舉例,Claude 能記住發布時程改到了星期五、為什麼某個 export 功能被拿掉,或是在動到帳務服務前該先找誰確認。

Claude 也會記住你的工作與溝通風格,你可以要求它調整多久回報一次進度、多常開新的 thread,以及每次更新要寫得多詳細。除了記憶之外,project 現在還附帶一個 library,收集你加入的檔案,以及 Claude 產出的成果,方便之後的新工作接續前面的成果。

⚠️ 目前的限制與後續規劃

因為 project 可以同時跑多條 thread,而每條 thread 都是一個完整的 Claude Code session,所以用量可能比以前更快觸及使用上限。文章提到,你可以查看該 project 的專屬用量,並分別為 coordinator 對話與各個 worker thread 選擇模型與 effort 等級。目前 thread 都是在雲端執行,Anthropic 表示「即將」推出可以在使用者自己的機器上執行、搭配本機工具與程式碼、並在自家網路環境內運作的版本。

這次更新目前以 beta 形式開放給部分使用 Claude Code 雲端 session、且在網頁版或桌面版尚未建立過 project 的 Claude Pro 與 Max 訂閱戶。接下來一週會擴大到更多同樣方案的 Claude Code 使用者,之後才會輪到 Claude 全體方案與 Team、Enterprise 方案。已經在使用舊版 project 的 Pro、Max 使用者仍可照常使用,等擴大 rollout 到 chat 與 Cowork 時會一併升級。尚未取得存取權的使用者可以加入候補名單。

🎯 實務啟示

對於習慣手動拆解大型重構或跨 repo 遷移任務的工程團隊來說,這個改版把「協調多個並行工作」的責任從人身上移到 Claude 身上。與其一次次手動開 session、追蹤誰做到哪,不如把目標講清楚,讓 coordinator 幫你分派、彙整。不過也要留意用量與 merge conflict 的處理,多線並行不代表可以完全放手不管。

🔗 來源
- 標題:Projects redesigned: from folder to conversation
- 作者／機構:Anthropic
- 連結:https://claude.com/blog/projects-redesigned

#ClaudeCode #Anthropic #AIAgents #DeveloperTools #SoftwareEngineering #AgenticAI #ProductivityTools #CloudCompute #LLM #DevOps
