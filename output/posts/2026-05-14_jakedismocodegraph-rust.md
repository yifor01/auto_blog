---
title: "Jakedismo/codegraph-rust"
source: GitHub Trending
url: https://github.com/Jakedismo/codegraph-rust
score: 105
model: tencent/hy3-preview:free
generated_at: 2026-05-14T20:56:24.720124
---

📌 【個人專案】CodeGraph 讓 AI 認識程式碼  

你有沒過感覺，AI 輔助編程總是像在黑暗中摸索？每次對話都要從頭告訴它你的專案結構，浪費大量 token 還是只能靠簡單的 grep？  

🤔 **AI 輔助編程的盲點**  
現有的 AI 助手往往只能逐檔案查看、靠關鍵字匹配，難以快速掌握整個代碼庫的依賴與架構。這導致每次對話都要從零開始說明上下文，效率受限。  

🧪 **CodeGraph 的核心設計**  
CodeGraph 透過以下步驟把整個程式碼庫轉換為可供 AI  reasoning 的知識圖：  
1. 解析原始碼產生 AST  
2. 透過 FastML 與 LSP 取得型別與定義資訊  
3. 建立套件、節點與邊（函式呼叫、依賴、資料流等）  
4. 同時產生混合嵌入（Graph + Embeddings）  
5. 提供結合圖形遍歷與語義搜尋的混合查詢介面  

 **結合圖與嵌入，提供關係完整的語義搜尋**  
與僅產生向量的傳統 semantic search 不同，CodeGraph 的圖結構保留了程式碼間的呼叫、依賴與模組關係。搜尋時，你不僅能找到「相似程式碼」，還能得到該程式碼的上下文：被誰呼叫、依賴什麼、在架構中的位置。這使 AI 助手能在一次查詢中獲得完整的依賴鏈與模組視圖，減少重複說明上下文的需求。  

💡 **為什麼圖+嵌入比純嵌入更有用**  
純嵌入只能捕捉語義相似性，卻難以區分「同名但功能不同」的函式或說明兩段程式碼是否真的在同一條調用鏈上。圖結構補足了這種關係資訊，讓搜尋結果不僅相關，而且在結構上是可追溯的。這正是作者認為「真正讓 AI 能 reasoning about your codebase」的關鍵。  

⚠️ **專案尚早期，社群反饋有限，實際效果待驗證**  
目前 CodeGraph 是個人開源專案（作者 Jakedismo），雖然在 GitHub Trending 上獲得 261 個星標（今日），但尚未有大規模實務案例或效能基準報告。使用者需自行評估其在不同語言與建置系統上的適配度。  

🎯 **適合想讓 AI 助手快速掌握大型代碼庫的開發者**  
如果你正在尋找方法讓 AI 編程助手不僅是「快速寫 Code」，更能理解專案架構，CodeGraph 提供了一種可即時安裝的方案。安裝與使用指南已在 repo 中提供，適合先在偏好 Rust 的環境中試驗，再根據需求擴展至其他語言。  

🔗 **論文連結**  
📝 CodeGraph: Your codebase, understood  
👤 Jakedismo  
🔗 https://github.com/Jakedismo/codegraph-rust  

你有試過讓 AI 助手「看見」整個專案嗎？歡迎在留言區分享你的經驗或想法 👇  

#AI #CodeGraph #Rust #開發工具 #LLM #知識圖 #GitHubTrending #程式設計 #開源專案
