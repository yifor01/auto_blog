---
title: DeepSeek Harness外掛一夜燃爆GitHub：長期記憶、電子寵物、4399小遊戲全來了
source: 量子位
url: https://www.qbitai.com/2026/08/473597.html
model: claude-code/sonnet
generated_at: '2026-08-16T06:11:22.720352'
score: 57
---

📌 DeepSeek Harness外掛狂潮：700+ repo一夜爆量

TL;DR：開源Agent框架DeepSeek Harness喊出「萬物皆外掛」，社群短時間內衝出700多個外掛倉庫。

從多 Agent 團隊、跨會話長期記憶，到電子寵物與 18 款小遊戲，DeepSeek Harness 才剛開源沒多久，GitHub 上掛著 dsh-plugin 標籤的倉庫已經衝破 700 個，社群把「Everything is a Plugin」這句口號活生生實現成了一場全民裝修運動。

🤔 一句口號引爆的裝修潮

DeepSeek Harness 是官方釋出的開源 Agent Harness（agent 執行框架），核心設計理念只有一句話：「Everything is a Plugin（萬物皆外掛）」。這句口號一出，社群幾乎是立刻照字面全力執行，才剛發布沒多久，GitHub 上標記 dsh-plugin 標籤的公開倉庫數量就已經衝上 700 多個，社群也自發整理出「Awesome DeepSeek Harness Plugins」精選清單，橫跨開發工具、Agent 編排、效率協作、資料研究、DevOps、AI 設計與媒體等多個類別。

🧩 讓 Harness 變成迷你 IDE 的實用外掛

在這波外掛熱潮中，真正瞄準幹活效率的作品不少：

- dsh-agent-teams：讓使用者一句「用 AgentTeams 調研某件事」，就能讓當前對話中的 Agent 就地升級為隊長，再拉起數個子 Agent 組隊，自動拆解任務、設定依賴關係、彼此互相溝通，Web 介面右上角還能即時檢視每個成員的工作狀態。
- DSH Better Sidebar：把檔案管理、程式碼編輯器、終端機、Git 面板、背景任務與子 Agent 全部塞進側邊欄，讓側邊欄本身變成一個迷你 IDE 工作臺，減少在多個視窗間來回切換的次數；終端機是真正的 Shell，Git 面板也能看 diff、暫存與提交。
- dsh-at-file：補上類似 Codex 的 @file 能力，可以直接在輸入框中搜尋工作區檔案，把指定檔案內容一併塞進 Prompt，省去手動尋找、複製、貼上的步驟。
- dsh-memory-evolve：為 DeepSeek Harness 補上跨會話的長期記憶，能持續記錄專案約定、架構決策、踩過的坑與目前進度，並可感知 Git 分支、在背景進行 Skill 演化，記憶太多時也能歸檔、需要時再調出。

🧩 從 Claude Code 搬家與讀圖能力

針對想從 Claude Code 轉換陣營的使用者，社群也做出了對應的遷移外掛：dsh-plugin-claude-bridge 可以把 Claude Code 累積的記憶、Skill 與設定（如 CLAUDE.md）搬進 DeepSeek Harness；而 dsh-claude-move 搬得更徹底，連 Session、Memory、Skills、CLAUDE.md 都能整體遷移，甚至能在 DeepSeek Harness 裡直接接續先前在 Claude Code 的對話往下聊。

另外，ModLens 這個外掛解決了 DeepSeek 原生不擅長讀圖的問題，使用者可以直接把圖片貼進聊天框，外掛會先呼叫視覺引擎，把圖片中的文字、佈局、實體與語義資訊整理成結構化證據，再交給 DeepSeek 進行推理。

其他被作者點名的實用外掛還包括：dsh-github-connector（在對話中直接管理 GitHub context）、context-vista（檢視上下文 token 被哪些內容佔用）、dsh-undo（Agent 改壞東西時可回滾上下文）、dsh-record-replay（記錄一次操作流程，讓 Agent 之後照樣重現）、dsh-obsidian-export（把對話一鍵匯出到 Obsidian）與 dsh-share（一鍵分享完整對話紀錄）。

💡 當工程外掛玩到失控：電子寵物、懷舊廣告、18 款小遊戲

往 GitHub 深處翻，畫風開始失控。dsh-TUI 把整個 Web 介面改造成類似 Claude Code 風格的全螢幕終端機介面，鯨魚圖示頂欄、即時工作狀態、思考過程展開、雙擊 Esc 回滾、上下文進度條與 TPS 儀表一應俱全；dsh-web-ui 則直接塞進二次元風格的電子寵物、任務看板、Git 圖譜、行動裝置遠端操作、即時 token 統計與換膚中心。

更誇張的是 dsh-ads，這個外掛唯一的功能，就是替 DeepSeek Harness 的 Web UI 加上 2005 年那種中文網站風格的廣告，側欄廣告、對話中的資訊流廣告、角落彈窗廣告一應俱全。還有 dsh-minigames，塞進了整整 18 款小遊戲，從俄羅斯方塊、坦克大戰、貪食蛇、2048、掃雷、五子棋、黑白棋、數獨到吃豆人都有，讓使用者在等待模型回覆或 Agent 跑完任務時可以順手玩一把。

最後還有一個叫 deepseek-manners 的外掛，功能單純到近乎行為藝術：每次 AI 回覆結束後，自動補上一句「謝謝你，鯨魚大人」，除此之外什麼都不做。

🎯 對工程師來說，這波熱潮代表什麼

這波爆量現象某種程度上驗證了「Everything is a Plugin」這個架構決策的威力：當外掛系統的介面設計得夠簡單、夠開放，社群就會用比官方預期快得多的速度去填補生態，從真正解決痛點的 Agent 編排、長期記憶、IDE 化側邊欄，到單純圖一樂的電子寵物與小遊戲都會出現。如果你也在設計 Agent Harness 或開發工具的外掛系統，這份清單是個現成的參考範本：先看哪些外掛解決了「切換視窗」「重複給上下文」「記憶遺失」這類真實的工作阻力，那些通常就是外掛生態裡最先被做出來、也最多人在用的類型。

🔗 來源
- 標題：DeepSeek Harness外掛一夜燃爆GitHub：長期記憶、電子寵物、4399小遊戲全來了
- 作者／機構：夢瑤 @ 量子位
- 連結：https://www.qbitai.com/2026/08/473597.html

#DeepSeek #AgentHarness #OpenSource #GitHub #LLMTooling #DeveloperTools #PluginEcosystem #AIAgents #DevTools #ClaudeCode
