---
title: "anthropics/claude-code"
source: GitHub Trending
url: https://github.com/anthropics/claude-code
score: 108
model: tencent/hy3-preview:free
generated_at: 2026-05-28T21:01:02.297223
---

📌 【Anthropic 新推出】Claude Code：終端機中的 agentic 編程助手  

你是否想過，在終端機就能用自然語言讓 AI 幫你寫程式、解說程式碼、處理 Git？  
現在 Anthropic 釋出的 Claude Code 讓這成為可能，無需離開你的命令列環境。  

🤔 **產品動機**  
開發者越來越希望將 AI 助手直接融入日常工作流程，終端機作為最接近程式碼與 Git 的環境，卻缺乏能夠理解整個 codebase 並執行複雜任務的自然語言工具。Claude Code 想要填補這個空白，提供一個「終端機原生」的 agentic 編程體驗。  

🧪 **核心功能**  
根據專案說明，Claude Code 能：  
- 在終端機中理解你的程式碼基礎（codebase）  
- 透過自然語言指令執行例行任務（例如產生樣板程式、重構）  
- 說明複雜程式碼的運作方式  
- 處理 Git 工作流程（commit、push、branch 等）  
- 在 IDE 中或透過在 GitHub 上標記 @claude 使用  

💡 **使用方式與擴展**  
- 安裝：MacOS/Linux 建議使用 `curl -fsSL https://claude.ai/install.sh | bash`；Homebrew 為 `brew install --cask claude-code`；Windows 建議使用 PowerShell `irm https://claude.ai/install.ps1 | iex` 或 WinGet `winget install Anthropic.ClaudeCode`。（NPM 安裝方式已被標記為已棄用）  
- 安裝完成後，進入專案目錄執行 `claude` 即可啟動。  
- 倉庫內附帶多個 plugin，可透過自訂命令和 agent 擴充功能，詳細說明見 `plugins` 目錄。  

⚠️ **使用注意**  
- 專案文件中提到資料蒐集、使用與保留政策，建議在使用前閱讀官方文件以了解具體細節。  
- 如遇到問題，可內建使用 `/bug` 指令回報，或直接在 GitHub 提交 Issue。  
- 歡迎加入 Claude Developers Discord 以取得協助、分享經驗與討論專案。  

🎯 **實務建議**  
若你終日在終端機中編輯程式、執行腳本或管理 Git，Claude Code 提供了一種不離開命令列即可獲得 AI 說明與任務執行的方式。建議先閱讀官方安裝與使用文件，嘗試基本的自然語言指令（例如「解釋這個函式的作用」或「幫我建立新分支並提交變更」），再根據個人需求探索 plugin 的擴充可能性。  

🔗 **資源連結**  
📂 倉庫：https://github.com/anthropics/claude-code  
📖 官方文件（安裝、使用、plugin 與資料政策）：見倉庫 README 與 docs 目錄  
💬 Discord 社群：透過倉庫連結加入 Claude Developers  

#Anthropic #ClaudeCode #TerminalAI #開發者工具 #GitHubTrending #AI助手 #程式效率
