---
title: Herdr has released native app
source: Hacker News
url: https://github.com/herdrdev/herdr-app
model: claude-code/sonnet
generated_at: '2026-10-30T21:51:25.962447'
score: 73
---

📌 Herdr：把終端機與 AI Agent 工作區搬進同一個桌面視窗

TL;DR：開源桌面應用 Herdr 讓你同時管理多個終端機與 coding agent，關閉視窗後工作仍在背景繼續跑。

在 Hacker News 上，一款乍看只是「終端機管理工具」的應用，拿下 344 個讚、231 則留言。驅動這波討論的，是現在工程師桌面上動輒同時開著好幾個 coding agent 的真實痛點：哪個 agent 卡住了？哪個已經做完等你確認？

🤔 **多 Agent 時代的視窗管理問題**

隨著 Claude Code 之類終端機原生的 agent 普及，一個人同時跑多個 agent、多個 repo、多臺機器已經是常態。但終端機視窗一多，追蹤「誰在等我」「誰還在跑」本身就變成額外負擔，而且常見的終端機工具一旦視窗關閉，裡面跑的程式也跟著結束。

🧩 **核心設計：視窗只負責顯示，核心負責執行**

Herdr 把「畫面」和「執行」拆成兩層：視窗（window）負責排版顯示，實際跑終端機的是背景的 core。關閉視窗不會中斷終端機，只有真的關掉分頁（tab）或窗格（pane）才會結束裡面的程序；就算重新開機或 core 當掉，保留下來的窗格也會在原本的資料夾重新開一個新殼層。

工作被組織成「space」：一個 space 對應一臺機器上的一份工作，通常是一個 repo，裡面可以開多個 tab，再把 tab 切成多個 pane 並排放終端機或 mod 面板。側邊欄的 agents 清單會把所有 space 裡的 agent（包含某個 agent 自己啟動的 worker）集中起來，標示四種狀態：Working（還在跑）、Blocked（在等你）、Done（你沒看著的時候做完了）、Idle（沒在工作，或你已經看過的完成項目）。

要連遠端機器，就在 Settings → Machines 加一臺 SSH 主機；該機器上的 space 會在對方的 core 上執行，不佔用本機資源，而且本機視窗關閉或筆電休眠都不影響遠端工作繼續進行。

🧩 **怎麼安裝與給 Agent 用**

Linux／macOS 用 `curl -fsSL https://releases.herdr.dev/app/install.sh | sh` 安裝（Linux 需要桌面環境與可用的 Vulkan 驅動），Windows 則在 PowerShell 執行 `irm https://releases.herdr.dev/app/install.ps1 | iex`。安裝程式會順便補裝缺少的 herdr-core。

針對 agent 自動化，`herdr-app --skill` 會印出驅動視窗用的 agent 指南，並搭配 `herdr-app ls`、`herdr-app status`、`herdr-app commands` 檢查目前視窗狀態；herdr-core 則負責實際跑程式與協調。介面外觀由「layout」排版、用 JavaScript 寫的「mod」繪製面板與選單，複製內建版本修改後就不會被更新覆蓋。

⚠️ **使用前的提醒**

Mods 是「受信任的程式碼」而非沙箱化擴展，安裝別人寫的 mod 前官方建議先讀過安全性文件；原始碼編譯版不會自動更新；預設開啟使用量 telemetry，可在 Settings → Privacy 關閉。

🎯 **實務啟示**

如果你的日常工作已經是「開很多終端機、跑很多 agent、還要連到遠端機器」，Herdr 示範了一種把「顯示層」和「執行層」拆開的思路，讓視窗關掉不等於工作中斷，值得在管理多 agent 工作流時參考。

🔗 **來源**
- 標題：Herdr has released native app
- 作者／機構：cherioo（Hacker News 發文者）
- 連結：https://github.com/herdrdev/herdr-app

#Herdr #CodingAgent #DeveloperTools #TerminalEmulator #ClaudeCode #AIAgent #DesktopApp #DevEx #OpenSource #HackerNews
