---
title: Elsewhere
source: Simon Willison
url: https://simonwillison.net/elsewhere/
model: claude-code/sonnet
generated_at: '2026-08-23T06:23:26.348935'
score: 67
---

📌 Bun 1.4 悄悄把 Rust 重寫藏在新功能清單裡,Simon Willison 本週開發雜記

TL;DR:一次看懂 Bun 1.4 的 Zig 改寫 Rust 大工程、LLM 生態系的依賴斷裂修補,以及用 AI agent 做研究與寫程式的幾個實驗。

當 Bun 1.4 的 release notes 用「新增 1,517 個 Node.js 測試」「修復超過 2,900 個問題」「CPU 閒置用量降 5 倍」這些數字轟炸讀者時,真正值得注意的一句話反而被輕描淡寫地放在中間:整個 runtime 已經從 Zig 重寫成 Rust。Simon Willison 這篇彙整貼文,把這件事和一堆看似瑣碎的版本更新、AI agent 實驗放在一起,拼出他這陣子的開發日常。

🧩 Bun.WebView:瀏覽器自動化進了 runtime 核心
Bun 1.4 是 Rust 重寫後的第一個穩定版,新增了 Bun.Image、Bun.WebView、Bun.markdown、Bun.cron()、Bun.Terminal,以及 bun run --parallel、bun test --parallel、bun audit fix、bun dedupe、bun prune 等指令,官方同時宣稱記憶體用量最多減少 35%、Linux 上啟動速度快 50%。Simon 特別點名 Bun.WebView:它讓 Bun 核心直接支援瀏覽器自動化,可以用 macOS WebKit 或透過 Chrome DevTools Protocol 控制本機 Chromium。他找 Claude Code for web 做了一個原型,提供載入網頁並在其中執行 JavaScript 的 API(靈感來自他自己的 shot-scraper 工具),測試發現要跑得動複雜頁面的完整 Chrome,容器大約需要 192MB 到 256MB 的記憶體(用 cgroups 量測)。

🧩 LLM 生態系的依賴地雷:embedding key、httpx、Gemini 3.7 Flash
LLM 專案這陣子修了好幾個坑:embedding 模型現在改用和一般 LLM 模型相同的 key 命名模式,順勢解鎖了「把模型和一組預設參數包裝成模板」的用法。另一個問題比較尷尬:OpenAI 的 Python 函式庫拿掉了對 httpx 的依賴,而 LLM 其實是透過 openai 套件間接拿到 httpx,沒有直接宣告依賴,結果全新安裝直接壞掉,目前用 pin 住 openai<3 暫時解套,下一版會改用 httpx2。llm-gemini 外掛也終於更新,加入 Gemini 3.7 Flash、gemini-3.6-flash、gemini-3.5-flash-lite 以及兩個 embedding 模型 gemini-embedding-2 與 gemini-embedding-001,並升級相容 LLM 0.32,讓使用者能看到 reasoning trace、啟用 server-side tools。Simon 用 Gemini 3.7 Flash 在不同 thinking effort 下畫「騎腳踏車的鵜鶘」來測試效果。

🧩 sqlite-utils 的一次隱藏依賴 crash
sqlite-utils 4.2 引入的新程式碼用到了 typing-extensions,但這個套件其實只是透過 dev 依賴群組間接被裝進來的,並沒有正式列為專案依賴——所以透過 uvx sqlite-utils 直接執行時就會壞掉,得靠 4.2.1 修掉。Simon 也順手做了一個 smoke test 方法:用 uv run --no-default-groups --isolated 執行,確保就算沒有那些 dev 依賴、CLI 工具依然能跑。同一版本也強化了 table.transform() 功能,現在能保留更多邊界情況的 schema 定義,包括 check constraint、unique constraint,甚至是欄位註解。

🧩 拿 AI agent 做研究與寫程式的三個實驗
Simon 讓 Claude Fable 5(在 Claude Code for web 中)研究能否用 smolmachines.com 當沙盒,限制 CPU、記憶體與網路存取來執行不受信任的 Python/JavaScript 程式碼。結果卡在 Claude Code for web 環境本身跑不了 smol machines,於是它自己想出 Plan B:改裝 smolvm,直接在 GitHub Actions runner 上跑測試。另一個實驗是用 GPT-5.6-Sol xhigh 做出一個網頁 UI,用來測試在 LM Studio 上跑的 Qwen 3.8 27B(分別在 M5 MacBook Pro 和 NVIDIA DGX Spark 上),對話會存在瀏覽器裡並可匯出成 JSON,還會在串流過程中即時渲染生成中的 SVG 圖片。最後一個更大膽:他讓 Codex 和 GPT-5.6 Sol Ultra 做一次研究性衝刺,嘗試打造一個 API 設計沿用 sqlite-utils(insert、upsert、insert_all、upsert_all、create、update 與 table introspection),但底層改用 SQLAlchemy,同時支援 PostgreSQL、SQLite、DuckDB,用 uv init 起專案、紅綠 TDD 搭配 pytest,沒花幾輪追加提示就做出堪用的 alpha 版本。

🎯 實務啟示
這篇雜記背後有個共通脈絡:小型依賴斷裂(像 httpx 那次)往往來自「透過別的套件間接裝到」的隱性依賴,值得在自己的專案裡也做一次類似的 --no-default-groups --isolated smoke test。另外,用 AI agent 做研究性衝刺(research spike)來驗證架構可行性——不管是沙盒方案還是跨資料庫抽象層——正在變成一種低成本的原型驗證手段,值得在自己團隊裡試試看。

🔗 來源
- 標題:Elsewhere
- 作者/機構:Simon Willison
- 連結:https://simonwillison.net/elsewhere/

#Bun #LLM #OpenAI #Gemini #SQLite #DeveloperTools #AIAgents #ClaudeCode #WebAutomation #SoftwareEngineering
