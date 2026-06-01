---
title: "dmtrKovalenko/fff"
source: GitHub Trending
url: https://github.com/dmtrKovalenko/fff
score: 105
model: tencent/hy3-preview:free
generated_at: 2026-06-01T22:02:09.690882
---

📌 **fff：AI 代理也愛的超快檔案搜尋工具包**  

你以為 ripgrep 已經夠快？當 AI 需要反复搜尋程式碼時，傳統 CLI 會浪費大量時間。fff 把搜尋變成庫，讓 AI 代理直接呼叫，速度提升顯著。  

🤔 **為何檔案搜尋成為 AI 工作流的瓶頸**  
現代 AI 輔助編程（如 Claude Code、Cursor）經常需要在專案中查找符號、重複 grep 或讀取檔案內容。每次啟動外部程式都會產生啟動開銷與上下文切換，尤其在長時間運行的代理中，這些開銷會累積成顯著延遲。  

🧪 **fff 的核心設計：庫化、防錯字與 frecency**  
- **庫化介面**：透過 MCP server 將搜尋功能暴露為 `ffgrep`、`ffind`、`ffg-multi-grep`，AI 代理只需發出「use fff」即可直接呼叫，免除重複啟動成本。  
- **防錯字路徑與內容搜尋**：支援模糊匹配，減少因拼寫錯誤導致的遺漏結果。  
- **frecency 排名**：根據實際開啟紀錄（git touch history）自動提升常用檔案的權重，越用越快。  
- **背景觀察器與記憶索引**：在後台維護輕量級記憶內容索引，使得重複查詢無需重新掃描磁碟。  

🚀 **效能優勢：比傳統 CLI 快上許多**  
根據專案說明，在需要多次搜尋的長時間進程中，fff 的響應速度明顯優於 ripgrep 與 fzf，這正是它最初作為 Neovim 外掛受到歡迎的原因——現在同樣的優勢被搬移到 AI 代理的工作流中。  

💡 **為什麼 frecency 與預熱會帶來實際提升**  
傳統搜尋每次都從零開始掃描，而 fff 透過：  
1. **記憶實際開啟的檔案**：你常編輯的檔案在下次搜尋時會被優先匹配。  
2. **自動從 git touch 紀錄預熱**：在代理啟動時，根據最近變更的檔案建立暖身索引，減少首次查詢的延遲。  
3. **定義優先提示**：對看似函式或類別定義的行給予更高分數，幫助代理快速定義符號而非雜內容。  

⚠️ **目前已知的限制**  
- **依賴 MCP 生態**：只有支援 MCP（Model Context Protocol）的客戶端才能直接使用 fff 工具。  
- **主要針對 git 索引目錄**：預設行為假設工作目錄受 git 追蹤，非 git 專案可能需要額外設定。  
- **尚未見長期基準測試**：文件著重於「長時間 Process 中的重複搜尋」優勢，長期資源佔用與極端大規模碼庫的表現尚未在說明中詳述。  

🎯 **實務建議：如何在你的 AI 工作流中啟用 fff**  
1. **安裝 MCP server**（依作業系統選擇腳本）：  
   - Linux/macOS：`curl -L https://dmtrkovalenko.dev/install-fff-mcp.sh | bash`  
   - Windows PowerShell：`irm https://raw.githubusercontent.com/dmtrKovalenko/fff.nvim/main/install-mcp.ps1 | iex`  
2. **將以下提示加入專案的 CLAUDE.md（或等效設定）**：  
   ```
   For any file search or grep in the current git-indexed directory, use fff tools.
   ```  
3. **在代理對話中說「use fff」**，之後即可直接呼叫 `ffgrep`、`ffind`、`ff-multi-grep` 進行快速防錯字搜尋。  

🔗 **專案連結**  
📂 https://github.com/dmtrKovalenko/fff  
👤 作者：dmtrKovalenko  
📌 安裝腳本位置：`install-mcp.sh`（Linux/macOS）與 `install-mcp.ps1`（Windows）  

你的 AI 編碼助手是否已經在使用這樣的庫化搜尋？歡迎在留言區分享你的體驗或其他提升檔案搜尋效率的技巧！  

#AI #MCP #ファイル検索 #fff #ClaudeCode #Cursor #開發工具 #生產力提升
