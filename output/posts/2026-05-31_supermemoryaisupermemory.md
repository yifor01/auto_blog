---
title: "supermemoryai/supermemory"
source: GitHub Trending
url: https://github.com/supermemoryai/supermemory
score: 106
model: tencent/hy3-preview:free
generated_at: 2026-05-31T19:27:46.413827
---

🧠 **Supermemory：開源 AI 記憶與上下文引擎，基準測試奪冠**

你的 AI 每次對話都忘光？這個開源專案說它能讓 AI 長期記住你的偏好、專案與過往對話。

🤔 **AI 記憶的缺口與實務需求**  
大型語言模型在單次對話中表現優秀，但跨對話的上下文會隨即消失。這限制了個人助理、知識管理與多人協作等場景的應用。開發者需要一個能夠持續學習、自動更新且能即時提供正確資訊的記憶層。

🧪 **統一記憶與上下文架構的實作**  
Supermemory 提供一個單一的記憶結構與本體論，內含事實抽取、時間與矛盾處理、自動遺忘、使用者畫像維護、混合檢索（RAG + 記憶）、多種連接器（Google Drive、Gmail、Notion、OneDrive、GitHub）以及多模態抽取器（PDF、圖片 OCR、影片轉錄、程式碼 AST‑aware 分塊）。所有元件在同一系統內運行，單次查詢約 50 ms。

📊 **基準測試表現**  
在 LongMemEval、LoCoMo 與 ConvoMem 三個被廣泛引用的記憶基準上，Supermemory 目前排名第一，顯示在事實保留、時間一致性與對話上下文恢復方面具備領先能力。

💡 **使用方式與實務價值**  
- 個人使用：透過網頁或應用程式建立個人「超級記憶」，AI 能跨對話記住使用者偏好、專案進度與過往討論。  
- 團隊/企業：透過即時 Webhook 與雲端硬碟同步，知識庫與個人畫像自動更新，適合客服、法務或研發等需要長期知識追蹤的場景。  
- 開發友好：提供完整的 RAG 流程、連接器與多模態處理，皆為開源，可直接引入現有 AI 應用。

⚠️ **已知限制**  
- 現有評估主要集中在公開基準，長期真實世界部署的穩定性尚需更多案例驗證。  
- 系統依賴連接器的及時同步，網路或 API 變動可能影響實時性。  
- 多模態抽取器的效能取決於原始檔案品質，極端噪聲或低解析度輸入可能降低事實抽取準確率。

🎯 **給工程師的建議**  
若你正在構建需要狀態記憶的 AI 應用（如個人助理、知識庫聊天機器人或協作編輯工具），可先嘗試 Supermemory 的 Quickstart，觀察其在你的資料源上如何提升上下文一致性與減少重複說明。同時，注意監控連接器的 Webhook 狀態與設定適當的遺忘政策，以防止過時資訊誤導模型。

🔗 **專案資訊**  
📦 repo：supermemoryai/supermemory  
🔗 連結：https://github.com/supermemoryai/supermemory  
📚 文件、快速開始、儀表板與 Discord 社群均在頁面中提供。

你有試過讓 AI 長期記住你的使用習慣嗎？歡迎在留言區分享你的體驗或改進建議 👇

#AI #MemoryEngine #RAG #OpenSource #Supermemory #GitHubTrending #AI工程 #知識管理
