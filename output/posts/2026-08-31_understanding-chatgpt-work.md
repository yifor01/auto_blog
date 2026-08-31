---
title: Understanding ChatGPT Work
source: Simon Willison
url: https://simonwillison.net/2026/Aug/30/understanding-chatgpt-work/
model: claude-code/sonnet
generated_at: '2026-08-31T12:10:23.798343'
score: 72
---

📌 拆解 ChatGPT Work：雲端沙箱終於能連上全世界

TL;DR：實測顯示 ChatGPT Work 的程式碼執行環境已能自由連網，還多了瀏覽器代理與子代理能力。

OpenAI 在 7 月 9 日推出 ChatGPT Work 後,官方說明卻語焉不詳,連知名部落客 Simon Willison 都得自己動手拆解,才搞懂它跟原本的 Chat 到底差在哪。這篇文章記錄了他花費大量時間實測後的發現。

🤔 官方說法沒用,實測才知道差異在哪

OpenAI 官方對「何時該用 Chat、何時該用 Work」的回答是:想要答案、解釋、腦力激盪或短稿就用 Chat;想要 ChatGPT 完成有明確產出的任務,像是簡報、分析或可重複使用的工作流程,就用 Work。Willison 直言這個說法幾乎沒用,因為他多年來早就用一般 Chat 完成過這些任務。真正該問的問題是:Work 到底多了哪些 Chat 沒有的功能。

🧩 模型選項不同,計算額度也分開算

Work 目前提供 GPT-5.6 Sol、Luna、Terra 三種模型,搭配 Light 到 Ultra 共六級推理強度,也能選用 GPT-5.5。這些看起來與 OpenAI API 提供的是同一批模型。相對地,Chat 端提供的是 5.6 Instant、Medium、High、Extra High 與 Pro 的選擇(Extra High 與 Pro 僅限每月 100 美元以上的訂閱方案)。Willison 推測 Work 的 session 是計入 Codex 額度,而 Chat 則有獨立額度,這或許能解釋兩邊模型選擇為何不同。他也提到,Ultra 模式的特性是更積極地將任務委派給子代理。

🧩 程式碼直譯器終於能連上網路

這是 Willison 認為 Work Cloud 最令人興奮的功能:程式碼執行環境現在可以與網際網路通訊。Chat 的執行環境做不到這件事,若要求安裝額外套件或存取未經授權的網站與 API,都會被容器代理攔截。相較之下,Claude 的對應環境從去年 9 月上線起就有限制性的網路存取,可以從 PyPI、NPM 安裝套件、從 GitHub clone 專案,但白名單網域相當短。ChatGPT Work 則允許更多存取,雖然可以設定特定允許網域清單,但預設似乎是全部開放。這代表使用者可以直接複製 GitHub 專案、安裝依賴套件,再拿它去跟其他網路服務互動。

🧩 瀏覽器代理:能截圖、能填表單、能讓人類接手登入

另一個關鍵功能是瀏覽器工具,ChatGPT Work 可以啟動完整的 Chrome 執行個體,載入網站、填寫表單、截圖,甚至對已載入頁面的 DOM 執行 JavaScript。如果網站需要登入,瀏覽器可以提示使用者親自接手輸入密碼與雙因素驗證碼,不會讓憑證經過模型本身。Willison 實測時要求它「載入 simonwillison.net 並用 JavaScript 擷取標題」,結果它真的啟動瀏覽器實例並執行了程式碼。

🧩 持久化工作區與建站功能

Chat 每次對話都是全新的檔案系統,無法跨 session 存取。Work 則不同,每個 session 都有專屬的 scratch 資料夾(例如 /workspace/scratch/e00a0a017944),而且會跨 session 保留,Willison 表示自己已經累積了 171 個資料夾。這個 /workspace 磁碟區似乎掛載在所有正在執行的 Work session 上,一個 session 的檔案修改可以立即被另一個看見,但彼此並不共用行程空間,某個 session 執行的 localhost 伺服器無法被另一個存取。此外,Work 還能透過 Cloudflare Workers 建立並部署完整網站,搭配 D1 與 R2 做到具狀態的伺服器端功能,預設為私人,但可以公開或(在團隊方案下)分享給特定對象。除此之外,Work 也支援排程提示,例如每天早上 8 點自動執行一次搜尋,並可決定是否要通知使用者新資訊。

⚠️ 安全性仍是未解的問題

Willison 指出,他的「致命三重奏」(lethal trifecta)風險模型警告的正是這種同時具備私有資料存取、暴露於不受信任內容,以及能將竊取資訊回傳出去的代理系統。ChatGPT Work 三項條件全部具備。他希望 OpenAI 能更清楚說明如何防範針對 Work session 的 prompt injection 攻擊,並推測答案應該與 Codex 相同,是某種自動審查機制。他也坦言,搞懂這一切花的力氣遠超預期,主因是官方文件從未公開系統提示詞與工具描述。發文後他嘗試直接請 ChatGPT Work 建立一個列出自身所有工具的網站,結果得到一份包含 223 個註冊工具的清單(其中 6 個來自他個人透過 datasette-mcp 提供的 MCP)。

🎯 實務啟示

如果工作需要「連網執行程式碼 + 瀏覽器自動化 + 跨對話持久檔案系統」,ChatGPT Work Cloud 目前提供的組合相當罕見且強大。但正因為權限範圍如此之大,在導入內部工作流程前,務必比照高權限系統看待,並持續關注 OpenAI 是否公開更完整的 prompt injection 防護說明。

🔗 來源
- 標題:Understanding ChatGPT Work
- 作者／機構:Simon Willison
- 連結:https://simonwillison.net/2026/Aug/30/understanding-chatgpt-work/

#ChatGPT #OpenAI #AIAgents #CodeInterpreter #PromptInjection #LLM #AIsecurity #BrowserAutomation #Codex #AItools
