---
title: "Open source memory layer so any AI agent can do what Claude.ai and ChatGPT do"
source: Hacker News
url: https://alash3al.github.io/stash?_v01
score: 105
model: tencent/hy3-preview:free
generated_at: 2026-04-25T19:05:27.797631
---

📌 開源記憶層 Stash：讓任何 AI Agent 不再「每週一」

每次切換工作視窗、開啟新對話，AI 就忘了你是誰、專案走到哪、上次為什麼這樣決定。RAG 給了你更精準的答案，卻沒給你「記性」；它像一個極速圖書館員，隨叫隨到，但永遠不會主動記住你喜歡哪種解法。

🤔 **RAG 讓搜尋更快，但 Agent 依舊「每週一」**

Retrieval-Augmented Generation 提升的是「檔案內容的取用效率」，而非「對話與決策的累積理解」。你交出的文件越多，答案越貼近既有知識，但它不記得上次對話的上下文，也無法把「經驗」轉化為「模式」。這正是當前 Agent 架構的隱形天花板：上下文再長，也只是長一點的「一次性」視窗。

🧪 **開源認知層，以命名空間分層記住你、專案與自己**

Stash 並不取代你的模型，而是在 Agent 與世界之間插入一層持續性記憶。透過類似檔案系統的階層式命名空間（/me、/projects、/projects/cartona），它將多輪對話、決策、成功與失敗轉化為可遞歸索引的事實：

- 片段變事實，事實變模式，模式累積成穩定的傾向與偏好  
- 讀取 /projects 時，自動涵蓋其下所有子專案，Agent 無需手動拼接  
- 實作上不依賴更大上下文視窗，而是把「跨對話狀態」外部化與持續化  

這讓同一個 Agent 在兩次獨立對話之間，不再從零開始解釋自己。

☀️ **用 AI 的那組，從「解釋自己」變「繼續思考」**

在 Stash 示範的真實對話循環中，兩次不同 session 的 Agent 直接沿用上輪脈絡：決策依據、已知限制、偏好風格。差別不只是省下開場白，而是讓 Agent 從「響應式工具」邁向「具備延續性的協作者」：記憶越久，推理基礎越穩，錯誤重覆率越低。

💡 **RAG 回傳文件 vs. 記憶層累積理解**

- RAG：給一堆檔案 → 搜尋 → 回傳片段 → 對話結束後歸零  
- 記憶層：持續觀察對話與行為 → 合成結構化事實 → 跨 session 遞歸可用  

關鍵不在「資訊量」，而在「狀態的可重用性」。當記憶可被命名空間劃分，Agent 就能分別更新「關於你的偏好」「關於專案進度」「關於自身能力邊界」，而不讓它們互相污染或遺忘。

⚠️ **仍依賴外部狀態管理，長期演化與隱私尚待驗證**

- 此架構將「記憶」外部化，需額外的同步、版本控制與清理策略  
- 階層式命名空間在跨專案重用時，可能帶來過度泛化或殘留干擾  
- 缺乏對長期記憶衰減、權重校正與隱私邊界的內建機制  
- 實戰效果取決於觀察品質與合成邏輯的穩定性，非單靠儲存本身

🎯 **把記憶當成可版本化的基礎建設，而非一次性上下文**

- 將 Agent 狀態外部化，跨 session 持續可讀可寫  
- 用命名空間劃分記憶類型，避免策略與偏好互相干擾  
- 結合 RAG 檔案庫與記憶層觀察庫：前者給知識、後者給脈絡  
- 定期對記憶庫進行重構與修剪，避免陳年雜訊干擾新決策

🔗 **論文與實作連結**
📝 Stash: Open source memory layer so any AI agent can do what Claude.ai and ChatGPT do
👤 alash3al
🔗 專案頁：https://alash3al.github.io/stash?_v01
🔗 Hacker News 討論：https://news.ycombinator.com/item?id=（請自行補上討論編號）

你的 Agent 現在還是「每週一」嗎？你如何處理跨對話的狀態與偏好持續性？歡迎分享你的架構選擇 👇

#AI #Agent #Memory #RAG #OpenSource #LLM #軟體架構 #Claude #ChatGPT
