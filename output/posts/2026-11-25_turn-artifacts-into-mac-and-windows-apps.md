---
title: Turn artifacts into Mac and Windows apps
source: Claude Blog
url: https://claude.com/resources/articles/install-as-app
model: claude-code/sonnet
generated_at: '2026-11-25T01:36:20.953735'
pinned: true
---

📌 Anthropic 官方發布：Claude Artifacts 現在能變成桌面 App

TL;DR：Claude 的 Install as app 讓 artifact 一鍵變成有獨立視窗的 Mac/Windows 應用程式。

你做的那個會自動抓行事曆、整理郵件的小工具，為什麼還要每次打開 Claude 才能用？Anthropic 這次的更新讓它可以像一般軟體一樣，有自己的圖示，自己的視窗。

🤔 Artifact 不再只是「輸出結果」

Artifacts 最初的用途是產生一次性的工作成果，像圖表或網頁，給人分享。但 Anthropic 觀察到，使用者現在把 artifact 當成日常工作的工具在用：例如一個會定期從行事曆與郵件抓資料的會議準備頁面，或是一個追蹤當天要出貨訂單的追蹤器。既然是每天要依賴的工具，它就該像其他應用程式一樣開啟，並在有事情需要留意時主動提醒使用者。

🧩 Install as app 怎麼運作

從今天開始，Claude for Mac 與 Windows 的使用者可以把 artifact 安裝成桌面 App。安裝後的 App 會有自己的圖示，並在獨立視窗中開啟，而不是嵌在 Claude 裡面。使用者可以把它分享給其他人，它要和電腦互動前也需要先取得使用者的授權，權限範圍由使用者自行決定。每個 App 都能使用 Claude 以及使用者的 connector，並在底層 artifact 被編輯時自動更新。App 向 Claude 發出的請求，會計入使用者方案的用量額度。

安裝後的 App 可以發送通知，或把項目加進選單列或系統匣。Anthropic 內部的員工已經用這個功能做出像 Linnet（一個完整的圖層式圖片編輯器）、Phosphor（一個質感像電影場景的檔案管理工具）、Sift（依規則整理資料夾、並用 Claude 協助分類）、Tern（搭配 Claude 協助解說的終端機）和 Vitals（放在選單列或系統匣裡查看電腦效能的小工具）等案例。

💡 三層權限設計，信任決定開放範圍

為了平衡方便與安全，Install as app 提供三個層級的權限：

- 預設：安裝後的 App 只能做瀏覽器裡能做到的事。
- App 權限：App 可以請求使用一些 Claude 能嚴格控管的常見功能，例如建立永遠置頂的視窗、監聽全域快捷鍵，或發送通知。
- 完整電腦存取權：App 可以請求執行程式，或是在不每次詢問的情況下讀取、修改、刪除使用者的檔案。

值得注意的是，使用者的授權只涵蓋 App 當前的版本，所以每次更新（即使是自己做的修改）Claude 都會再次詢問；但如果 App 的一部分來自其他網站，那部分的內容可以在不重新詢問的情況下改變。完整存取權也只能授予自己做的 App，或在 Team、Enterprise 方案中由同組織成員做的 App。Anthropic 並不會在安裝前審查這些 App，所以只該把完整存取權交給你信任的 App。

⚠️ 使用限制

Install as app 目前以 beta 形式在所有方案上逐步推出，但 HIPAA-ready 組織與混合部署環境無法使用。Team 方案預設開啟（完整存取權預設關閉），Enterprise 方案則預設關閉，需要 owner 手動開啟。使用時必須保持連線並登入 Claude 帳號才能開啟 App。另外，包括 Claude Docs、Slides、Sheets 等部分 artifact 類型目前無法被安裝成 App。

🎯 給開發者與知識工作者的實務意義

對經常用 Claude 搭建小工具的工程師來說，這代表你不再需要額外打包、簽署或維護一套獨立的部署流程，也不需要 API key 或另外登入，App 本身就直接沿用你的 Claude 帳號。只要更新 Claude for Mac 或 Windows，打開一個你每天都在用的 artifact，從分享選單選擇「Install as app」就能開始。

🔗 來源
- 標題：Turn artifacts into Mac and Windows apps
- 作者／機構：Anthropic
- 連結：https://claude.com/resources/articles/install-as-app

#Claude #Anthropic #Artifacts #DesktopApp #AIAgent #DeveloperTools #ClaudeForMac #ClaudeForWindows #ProductivityTools #NoCode
