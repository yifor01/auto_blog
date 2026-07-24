---
title: 'Launch HN: Screenpipe (YC S26) – Record how you work and turn that into agents'
source: Hacker News
url: https://news.ycombinator.com/item?id=49024620
model: tencent/hy3:free
generated_at: '2026-07-24T08:22:06.354839'
score: 74
---

📌 【YC S26 新專案】Screenpipe：透過錄製螢幕與音訊，為 AI Agent 打造永不遺忘的「第二大腦」

TL;DR：Screenpipe 透過本地端錄製螢幕與音訊，將使用者的行為轉化為 AI Agent 可搜尋的記憶。

🎣 **讓 AI 真正理解你在電腦上做什麼**

目前的 AI 雖然強大，但它們往往缺乏「上下文」（context）——它們不知道你剛剛在瀏覽什麼、在對誰說話，或是你在哪個軟體中處理某個專案。雖然目前有 Fine-tuning 或 Tool calling 等技術，但前者成本太高，後者在自動化程度與操作複雜度上仍有不足。

Screenpipe 的核心理念是：如果 AI 能知道你每天在電腦上的一舉一動，它就能更精準地協助你處理重複性任務，甚至將工作流程轉化為標準作業程式（SOP）。

🧩 **從「耗電發熱機」到高效能的設計最佳化**

在開發初期，作者曾嘗試過最直覺的做法：持續錄製影片並對每一幀進行 OCR（光學字元辨識）。但這種做法會產生大量重複資料，且會消耗極高的系統資源（作者戲稱這會讓電腦變成「加熱器」）。

為了提升效能，Screenpipe 採用了更聰明的事件驅動架構：

- **事件觸發機制**：不再無差別錄製，而是監聽系統事件，例如：應用程式切換、點選、打字停頓、捲動，以及閒置狀態。
- **結構化資料整合**：當發生重要變化時，系統會將該時間點的螢幕截圖與作業系統的「輔助功能樹」（accessibility tree）進行配對。
- **OCR 補位**：只有在無法取得結構化輔助資料時，才會啟動 OCR。
- **音訊處理**：持續擷取音訊，透過 Parakeet、Whisper 或雲端模型進行本地端轉錄，並能識別說話者。
- **資料儲存**：所有資訊都索引在本地端的 SQLite 資料庫、mp4 檔案或 Markdown 檔案中。

📊 **輕量化與隱私保護的平衡**

為了確保不影響使用者日常工作，Screenpipe 在效能與隱私上做了嚴格限制：

- **極低資源佔用**：本地模型設計目標為使用率低於 1% 的 CPU 與低於 400 MB 的記憶體。
- **隱私保護**：內建 AI PII（個人識別資訊）模型，可於本地端（使用 Apple MLX 或 Windows DirectML）自動遮蔽敏感資訊。
- **靈活性**：支援過濾特定的 App、視窗或網址，並支援瀏覽器無痕模式。

💡 **如何將這些記憶轉化為行動？**

透過開放在 3030 埠的 AI 友善 API，你可以透過內建對話方塊或外部 Agent（如 Claude、ChatGPT 等）進行以下操作：

- **補充對話上下文**：「幫我收集關於專案 X 的所有背景資訊。」
- **檢索特定時間的任務**：「列出我今天早上 8 點到下午 4 點在做什麼，並總結完成的任務與剩餘事項。」
- **自動化維護知識庫**：「每小時將我的工作內容整理成 Markdown 檔案，存入我的 Obsidian 檔案庫中。」
- **發現自動化機會**：「看看我們團隊這週做過的所有事，列出可以自動化的清單。」

🎯 **實務啟示**

對於工程師或重度數位使用者而言，Screenpipe 提供了一種「被動式」的資料收集方式。它不依賴於手動輸入，而是透過捕捉系統層級的行為，為 RAG（檢索增強生成）提供最完整的 Context。這讓 AI Agent 從「工具」向「具備長期記憶的助手」邁進了一大步。

🔗 **來源**
- 標題：Launch HN: Screenpipe (YC S26) – Record how you work and turn that into agents
- 連結：https://news.ycombinator.com/item?id=49024620

#AI #Agent #Screenpipe #SecondBrain #RAG #Productivity #LocalAI #OpenSource #MachineLearning #Automation
