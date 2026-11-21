---
title: ClawDOS – An AI coding agent for DOS
source: Hacker News
url: http://ricapar.net/ClawDOS/
model: claude-code/sonnet
generated_at: '2026-11-21T22:26:11.032589'
score: 61
---

📌 用 Claude 在 1983 年的 IBM PC XT 上寫程式：ClawDOS 全紀錄

TL;DR：ClawDOS 是一個完全由 Claude 寫成、能在 8088/640K 原生硬體上運作的 DOS AI coding agent。

4.77MHz 的 8088 處理器、640K 記憶體、CGA 顯示卡、沒有長檔名支援——這聽起來完全不像能跑 AI agent 的環境,但作者 Ricapar 做到了,而且整個專案 100% 由 Claude 寫成。

🤔 **為什麼要在 40 年前的硬體上跑 AI agent**

作者小時候用的第一臺電腦就是 IBM PC,如今收藏了一臺滿配的 IBM PC 5160,搭配 PicoMEM 用 SD 卡模擬硬碟。他想測試的問題很單純：把 AI coding agent 推到現代常規之外的極端限制環境,它能造出什麼?而它造出來的東西,又能不能再去造別的東西?這是一個純粹出於興趣與娛樂的專案,不是商業或研究導向的工具。

🧩 **176KB 的 DOS 程式,自己說 Messages API**

ClawDOS 的核心是 HARNESS.EXE,一個 176KB 的 DOS 程式,直接在 PC 上實作 Claude Messages API 協定：自己組 request、解析串流回覆、執行工具呼叫,並把每段對話存成磁碟上的檔案。8088 處理器承擔除了 TLS 之外的所有工作,TLS 部分則交給一臺負責建立連線的「bridge」PC。

ClawDOS 擁有 18 個工具,可操作機器上的完整開發工具鏈:兩套組譯器（TINYASM、WASM）、Bruce's C、GW-BASIC、lDebug 除錯器,以及從使用者自己的 floppy image 安裝的 Turbo C 2.0,全都驗證過可在 8088 上運作。

它還有兩種持久化機制:memories 記錄與使用者合作學到的東西與偏好,skills 則是隨專案附帶的操作指南（例如開發工具用法、CGA 特效技巧）,兩者都是磁碟上的純文字檔,會列在每次對話的 system prompt 中,依任務需要被讀取。安全性設計上,Safe mode 預設開啟,任何變更檔案、記憶體或 port 的操作都會先詢問「Allow...?」。對話本身以 API 原生訊息格式存成磁碟檔案,可隨時恢復,即使被關機中斷也能重新接續;並支援在對話中途透過設定檔切換不同 provider 或 model。為了因應緩慢網路連線,API 快取機制讓第一次請求之後只需上傳新增內容,單次 tool result 約只需上傳 500 bytes 左右;連線中斷或 API 過載時會自動重試。CLAWDOS.LOG 則記錄每一輪對話的 time to first token、上傳大小與耗時、token 用量與快取讀取情況。

📊 **實際跑起來長怎樣**

作者展示了幾個案例：單句指令「寫 PRIMES.C 印出 100 以內的質數,用 Turbo C 編譯並執行」,ClawDOS 會先讀自己的編譯器使用指南,寫原始碼,再一次工具呼叫內完成編譯、連結、執行,整個過程 64 秒,其中 26 秒用於編譯連結與執行。另一個案例是重現 1983 年電影《WarGames》的畫面:向量世界地圖、飛彈弧線、井字棋終局,配上 PC speaker 或 AdLib 音效卡的配樂,僅用 5 個 Turbo C 原始檔、15KB 程式碼、不到 10KB 的執行檔完成。ClawDOS 甚至能透過 timer-interrupt hook 擷取當下 CGA 顯示記憶體,編碼成 PNG 傳回給 Claude 檢視畫面效果,並在被要求「讓 demo 自動結束」時,自己搜尋原始碼找到按鍵等待邏輯,修改其中一行完成任務。

⚠️ **侷限**

ClawDOS 仰賴一臺額外的「bridge」PC 來處理 TLS,8088 本身無法獨立完成完整的加密連線;專案採 GPLv3 授權,但建置出的磁碟映像檔若包含使用者自己安裝的 Turbo C 等第三方軟體,則不可重新散布。

🎯 **實務啟示**

ClawDOS 示範了把 agent harness 拆到最精簡的協定層(直接說 Messages API、自行處理 tool execution loop)可以多輕量,也展示了對話持久化與 API 快取機制在極端頻寬與運算限制下的實際價值。對正在設計邊緣裝置或低資源環境 agent 架構的工程師而言,這種「協定層自己握手、狀態全存本機」的做法值得參考。

🔗 **來源**
- 標題：ClawDOS – An AI coding agent for DOS
- 作者／機構：Ricapar
- 連結：http://ricapar.net/ClawDOS/

#ClawDOS #RetroComputing #AIAgent #DOS #Claude #VintageComputing #CodingAgent #Intel8088 #AnthropicAPI #TurboC
