---
title: "Open source Kanban desktop app that runs parallel agents on every card"
source: Hacker News
url: https://www.kanbots.dev/
score: 102
model: tencent/hy3-preview:free
generated_at: 2026-05-23T19:36:34.567386
---

📌 **Open‑source Kanban 桌面應用：每張卡片都能啟動獨立的 AI 代理**

想像看看，每個任務卡片都能自己派出一個 AI 代理，在背景獨自工作，而你只需要專注於規劃。這個新開源工具讓這成為可能，並已在 Hacker News 上獲得 243 分、148 則留言的社群關注。

🤔 **開發者需要的不是更多手動操作，而是可視化的自動化流程**

現代開發流程常常在任務看板與程式碼產生之間來回切換。手動建立分支、提交 PR、等待檢查不僅耗時，也容易讓注意力分散。團隊希望有一種方式，能在看板上直接觸發 AI 輔助的程式碼工作，且每項任務互不干擾，讓開發者能夠專注於更高層次的設計與決策。

🧪 **基於工作區與工作樹的平行代理執行**

Kanbots 是一款 MIT 授權的開源桌面應用（macOS、Linux、Windows），使用方式極簡：將一個資料夾拖入即可產生看板。看板上的每張卡片都能派遣 **Claude Code** 或 **Codex** 代理，每個代理運行在獨立的 Git worktree 中，確保環境隔離。使用者亦可啟用「自動駕駛」模式，讓預先定義的人格（persona）自行拆解工作、平行執行，並在完成後自行檢查輸出，適合在離開電腦時讓背景工作自行進行。

🚀 **即時可見的任務進度與成本追蹤**

介面顯示每張卡片的狀態（待處理、進行中、審閱等），並提供簡易的成本指標（例如「$1.06 今日」），讓團隊能夠一眼看出哪些任務正在消費 AI 配額。應用內建的本地資料庫（.kanbots/db.sqlite）採用 local‑first 設計，且目前未收集遙測資料（0 telemetry），符合開發者對隱私與資料主權的期待。

🔍 **工作樹隔離是實現平行、安全代理的關鍵**

將每個代理放在獨立的 worktree 意味著它們各自擁有完整的檔案系統快照，互不影響。這種設計不僅避免了因共享依賴或環境變數導致的衝突，也使得代理能夠安全地執行潛在的破壞性操作（例如重寫核心模組），因為任何變更都限制在該 worktree 範圍內，無法波及主分支或其他卡片的工作區。

⚠️ **目前仍屬早期版本，功能與穩定度待社群驗證**

應用剛發布 v1.0，文件中提到僅支援兩種 CLI（Claude Code 與 Codex），且部分進階功能（例如跨團隊雲端版）尚未在說明中詳細展開。由於尚未有大規模使用案例或長期穩定度報告，實際在大型 monorepo 或複雜 CI 流程中的表現仍需社群進一步測試與回饋。

🎯 **適合想要將看板與 AI 代理結合的開發團隊**

- 若你的工作流程已經使用看板管理任務，可直接嘗試將卡片轉換為可執行的 AI 工作單元。  
- 在探索新功能或修復 Bug 時，讓代理先在獨立 worktree 中跑出初步實作，再由人工審閱與合併，可顯著減少來回切換成本。  
- 由於採用 MIT 授權且免費（歡迎贊助），團隊可在不增加授權負擔的情況下，先在內部專案上試驗其平行代理概念。

🔗 **資訊來源**
📦 Kanbots – Open source Kanban desktop app that runs parallel agents on every card  
👤 作者／維護者：vitriapp  
🌐 網站：https://www.kanbots.dev/  
（原始碼於 GitHub 上公開，詳見專案頁面）  

你有試過在看板上直接啟動 AI 代理嗎？歡迎在留言區分享你的使用經驗或改進建議 👇

#Kanbots #OpenSource #AIAgents #ClaudeCode #Codex #Kanban #DeveloperTools #MITLicensed #HackerNews
