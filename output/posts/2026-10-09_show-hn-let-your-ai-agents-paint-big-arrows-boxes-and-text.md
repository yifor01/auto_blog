---
title: 'Show HN: Let your AI agents paint big arrows, boxes and text on your screen'
source: Hacker News
url: https://github.com/franzenzenhofer/big-arrow-on-the-screen
model: claude-code/sonnet
generated_at: '2026-10-09T22:01:09.403917'
score: 76
---

📌 讓AI Agent在你螢幕上畫箭頭：HN熱門工具bigarrow

TL;DR：一個macOS CLI讓agent直接在畫面上指出按鈕，而不是在終端機裡乾著急。

AI agent 可以幫你重構整個 monorepo、寫完一份資料庫搬移腳本，還能解釋清楚 monad 是什麼，但遇到一個只有人類能按的「允許」按鈕時，它能做的往往只是在你根本沒在看的終端機裡印一行「請點擊允許」。這個在 Hacker News 拿下 349 points、149 則留言的小工具，想解決的正是這個落差。

🤔 **Agent能找到按鈕，但不能、也不該去按**

big-arrow-on-the-screen（簡稱 bigarrow）是一個 macOS 命令列工具，同時附帶給 Claude Code 與 Codex 使用的 skill。它會在所有視窗最上層畫出一個箭頭與一塊文字牌，滑鼠點擊可以穿透它，你的鍵盤焦點不會被搶走，箭頭用完後會自己消失。作者列出的典型場景包括：權限提示（OAuth 同意、「使用...打開？」）agent 找到按鈕卻不能按；2FA、CAPTCHA、passkey、付款與簽名這類必須由人類完成的步驟，agent 指出位置後交給人決定；還有「我需要你，但你正在泡咖啡」的情境，可以搭配 --say 把文字牌唸出來，把人喊回電腦前；以及單純的操作教學，像在 Blender 裡一步步指出控制項位置。

🧩 **設計上刻意做到「無害、無痕」**

整個工具是一個 Swift 編譯出的二進位檔，沒有 daemon、沒有選單列圖示、不需要帳號、不收集任何 telemetry，作者特別強調「我們檢查了兩次，裡面沒有 AI」，單純就是一個箭頭。繪製箭頭這個動作本身不需要任何 macOS 權限。箭頭的生命週期管理也做得很小心：可以用 --duration 設定自動消失時間（point 預設 8 秒、start 預設 300 秒，0 表示不限時）；用 start 和 stop 手動控制；當畫箭頭的 agent 行程本身結束時（透過 CLAUDE_PID 或 BIGARROW_OWNER_PID），箭頭也會跟著消失；在 Claude Code 裡可以把 --hook 接到 UserPromptSubmit hook，讓使用者一送出下一句話就清掉該 session 的箭頭；也可以選配 --close-button 讓人類自己手動關掉。MIT 授權。

🧩 **安裝與最小使用方式**

安裝方式是 `brew install franzenzenhofer/tap/bigarrow`，再執行 `bigarrow install-skill` 讓 Claude Code（寫入 ~/.claude/skills）與 Codex（寫入 ~/.agents/skills）學會使用這個工具；也可以用 Swift 原始碼自行建置（需要 Xcode 16+、macOS 14+）。核心指令只有三個：`bigarrow point --element "Allow" --app "System Settings" --text "..."` 依元件標籤指向目標；`bigarrow point --at 760,500 --text "..."` 依座標指向；以及 `bigarrow start ... && bigarrow stop` 讓箭頭持續顯示直到手動停止。目標可以用 --at、--rect、--mouse、--window App[:title]、--element Label --app App 等方式指定，`--app App[:window或tab標題]` 會先把對應視窗或 Chrome／Safari 分頁帶到前景。另外 `bigarrow elements --app X` 可以列出該 app 底下能被 --element 匹配到的元件，`bigarrow doctor` 可以檢查權限與顯示器狀態，所有指令都支援 --json 輸出，並定義了清楚的 exit code（0 成功、2 輸入錯誤、3 找不到目標、4 權限缺失）方便 agent 判斷結果。

💡 **外觀選項做得比預期中講究**

視覺風格上支援 --shape（bend／straight／zigzag／spiral）、--style（arrow／ring／box）、--size、--corners、多種 --color 以及 --border 樣式，還有 --follow 讓箭頭跟著視窗或元件移動、--until-click 讓箭頭在目標被點擊後自動結束。作者甚至寫了一個 gallery 腳本去渲染所有造型組合，檢查箭身與文字牌交接處的視覺細節。

⚠️ **定位明確但範圍也刻意受限**

作者明確劃清這不是螢幕標註工具、不是自動點擊機器人、也不是截圖工具——它只負責「指」，不負責點擊、輸入或擷取畫面。這個克制的範圍設計是刻意的：一旦工具開始代替人類做決定性的操作（如點擊允許、輸入密碼），風險性質就完全不同了。

🎯 **實務啟示**

如果你的 agent workflow 常常卡在「需要人類介入才能繼續」的節點，尤其是權限授予、2FA 或需要人工確認的關鍵步驟，bigarrow 提供了一個比純文字提示更直覺的溝通介面，而且因為不執行任何點擊或輸入動作，引入它的安全風險相對可控。對於需要遠端教學或螢幕分享除錯的場景，用箭頭取代「上面那個，不是，另一個上面」式的語音指引，也是個實用的巧思。

🔗 **來源**
- 標題：Show HN: Let your AI agents paint big arrows, boxes and text on your screen
- 作者／機構：franze（Franz Enzenhofer）
- 連結：https://github.com/franzenzenhofer/big-arrow-on-the-screen

#AIAgent #macOS #DeveloperTools #ClaudeCode #Codex #CLI #HumanInTheLoop #OpenSource #Automation #HackerNews
