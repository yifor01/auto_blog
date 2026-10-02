---
title: 'Show HN: Audionaut – an open-source cross-platform multitrack audio editor'
source: Hacker News
url: https://github.com/kvoltmer/Audionaut
model: claude-code/sonnet
generated_at: '2026-10-02T21:41:37.819222'
score: 77
---

📌 開源多軌編輯器 Audionaut：讓 Claude 動手剪你的音軌

TL;DR：開源跨平臺多軌音訊編輯器導入 MCP，讓 AI agent 能直接下指令剪輯、匯出成品。

想像不用打開任何音訊編輯軟體，只要跟 Claude 說「把這段錄音剪到一分鐘並匯出」，剪輯就完成，還能一鍵復原回上一步。這不是概念demo，而是一套已經在 Hacker News 拿下 131 點讚、45 則討論的開源工具。

🤔 多軌錄音剪輯不需要整套 DAW 的重量

無論是做音樂、podcast 還是多軌錄音，傳統做法往往得打開一整套功能齊全但笨重的 DAW。Audionaut 的定位是「effortless audio editing」：提供精準剪切、每軌獨立的 playlist、彈性多聲道支援與乾淨匯出，目標是在不帶上全功能 DAW 複雜度的前提下滿足這些日常需求。

🧩 C++／JUCE 打底，MCP 讓 agent 直接動手

Audionaut 用現代 C++ 搭配 JUCE framework 開發，原生支援 Windows、macOS、Linux。它的特別之處在於原生支援 MCP：安裝好 Node.js 18+ 後，一行 `claude mcp add audionaut -- npx -y audionaut-mcp` 就能讓 Claude 或其他 agent 操作你開啟中的專案，而且每一次編輯都會被記錄成一個可復原的 undo 步驟。

專案裡還整合了兩個子模組：負責音訊分析（BIC segmentation、onset detection、beat tracking）的 Essentia，以及用來做人聲／樂器分離的 demucs.cpp，這是 Meta Demucs 的 C++ 移植版本，模型權重不隨原始碼附帶，而是首次使用時自動下載。

📊 從 CLI 指令看 agent 怎麼剪一首歌

專案另外提供一支 `audionaut-cli`，讓腳本、CI 或 AI agent 能在沒有 GUI、沒有音訊裝置的情況下操作 `.audium` 專案。每個指令都能加上 `--json`，在 stdout 吐出單一的機器可讀結果（`{"ok": true, "result": ...}` 或 `{"ok": false, "error": ...}`），所有 log 則留在 stderr，退出碼也分得很細：0 成功、1 操作失敗、2 用法錯誤、3 此 build 不支援該功能。

典型的 agent 工作流程是：

- `create` 建立新專案
- `import` 匯入素材並指定位置
- `analyze` 跑分析（如 beat 偵測）
- `auto-edit` 或 `assemble` 做自動剪輯或隨機拼接
- `separate` 視需要做人聲樂器分離
- `export` 輸出成品檔

每一步都檢查 JSON envelope 裡的 `ok` 欄位，而且用 CLI 寫出來的專案檔可以直接在 GUI 開啟，反之亦然。

⚠️ 建置門檻不低，主要仍是小眾工具

自行編譯並不輕鬆：需要用 `--recursive` clone 子模組，Essentia 的建置要求 Python 3.11 以下（因為它內建的 waf 仰賴 Python 3.12 已移除的 distutils），還需要 pkg-config 與建議用 3.x 版的 CMake。macOS 上的 app 處於沙盒環境，內建 CLI 只能存取 `~/Music` 這類有 entitlement 的位置，真正要無限制的腳本化操作得用獨立編譯的 `audionaut-cli`。授權採 GPL3（或更新版本）與商業授權雙授權模式。整體而言，這類工具的目標族群仍偏向需要客製化、自動化音訊工作流的開發者或工作室，而非一般使用者。

🎯 給正在做 agent 自動化工作流的工程師

Audionaut 示範了一個 MCP 在「非程式碼」領域的具體應用：把一個垂直領域工具（音訊剪輯）包裝成 agent 可操作的介面,並用標準化的 JSON envelope 與退出碼讓結果可被腳本判讀。這個「GUI app 同時支援 headless CLI、兩者共用同一份專案格式」的設計模式，值得其他想讓自己工具被 agent 驅動的開發者參考。

🔗 來源
- 標題：Show HN: Audionaut – an open-source cross-platform multitrack audio editor
- 作者／機構：vltmrkls
- 連結：https://github.com/kvoltmer/Audionaut

#OpenSource #MCP #AudioEditing #Claude #AIAgent #JUCE #CPlusPlus #Podcasting #MusicProduction #DeveloperTools
