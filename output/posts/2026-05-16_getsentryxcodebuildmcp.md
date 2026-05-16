---
title: "getsentry/XcodeBuildMCP"
source: GitHub Trending
url: https://github.com/getsentry/XcodeBuildMCP
score: 87
model: tencent/hy3-preview:free
generated_at: 2026-05-16T19:42:49.099318
---

📌 **XcodeBuildMCP：讓 AI 編程助手直接操作 Xcode 建置**

你是否曾試過讓 AI 編程工具（如 Cursor、Claude Code）幫忙寫 iOS 程式碼，卻發現它無法自行執行 `xcodebuild`、跑測試或處理簽名？這意味著開發者仍需手動切換終端機，才能完成完整的建置‑測試循環。

🤔 **AI 助手能寫程式，卻無法自行建置？這會削弱其真正的自動化價值**

隨著 Model Context Protocol（MCP）成為 AI 代理與外部工具溝通的標準，iOS/macOS 開發者卻缺乏一個能直接呼叫 Xcode 建置系統的 MCP 伺服器。若沒有這層橋接，AI 只能停留在程式碼生成階段，無法參與完整的 DevOps 流程。

🧪 **單一套件，同時提供 CLI 與 MCP 伺服器**

XcodeBuildMCP 透過 Homebrew 或 npm 全域安裝，即取得兩種使用方式：

- **CLI 模式**：在終端機直接執行 `xcodebuildmcp`，取得子命令來叫用 `xcodebuild`、執行測試或管理簽名。  
- **MCP 伺服器模式**：作為 MCP 伺服器啟動，讓符合 MCP 規格的客戶端（Cursor、Claude Code、Codex 等）透過標準協議呼叫同樣的建置工具。

安裝範例（任選其一）：

```
# Homebrew
brew tap getsentry/xcodebuildmcp
brew install xcodebuildmcp

# npm（需 Node.js 18+）
npm install -g xcodebuildmcp@latest
```

安裝後，`xcodebuildmcp --help` 可查看完整指令清單。若想讓 AI 代理自動知道如何使用這些工具，可執行 `xcodebuildmcp init` 安裝可選的「MCP Skill」或「CLI Skill」，分別為伺服器與 CLI 提供使用說明。

💡 **AI 現在能直接叫用 xcodebuild、跑測試、處理簽名**

透過這個 MCP 伺服器，AI 代理可以：

- 呼叫 `xcodebuild` 建置專案（包括支援 Swift Macro 的專案，因伺服器會要求 `xcodebuild` 跳過宏驗證以避免錯誤）  
- 執行單元測試或 UI 測試  
- 管理程式碼簽名與 provisioning profile（需符合一般簽名需求）  
- 取得建置日誌與錯誤訊息，供 AI 進行除錯或下一步決策

這意味著，開發者可以讓 AI 不只生成程式碼，還能自行完成「建置‑測試‑回饋」的閉環，顯著降低人工切換成本。

⚠️ **需求與限制：macOS 14.5+、Xcode 16.x+、Node.js 18+（Homebrew 安裝免除 Node 需求）**

- 只支援 macOS 14.5 以上與 Xcode 16.x 以上的環境。  
- 透過 npm 安裝時需要 Node.js 18+；使用 Homebrew 則無此需求。  
- 伺服器刻意要求 `xcodebuild` 跳過宏驗證，以避免在使用 Swift Macro 的專案上出錯；這是一種折衷方案，可能在極少數情況下掩藏真正的宏相關錯誤。  
- 簽名相關功能仍依賴開發者的憑證與 provisioning profile，伺服器本身不會產生或管理這些憑證。

🎯 **實務建議：先在個人專案上試用，再擴大至團隊 CI/CD**

1. 依照上述方式安裝 XcodeBuildMCP。  
2. 在您偏好的 AI 編程客戶端（Cursor、Claude Code、Codex）中加入 MCP 設定，指向本機的 `xcodebuildmcp` 伺服器（官方文件提供 Drop‑in 設定片段）。  
3. 測試讓 AI 產生一段簡易的 SwiftUI 視圖，然後請它呼叫 `xcodebuildmcp build` 來驗證編譯是否通過。  
4. 若流程順暢，可將同樣的設定加入團隊的共享開發環境或腳本，讓 AI 協助日常的功能開發與自動測試。

🔗 **專案連結**  
📂 getsentry/XcodeBuildMCP  
🔗 https://github.com/getsentry/XcodeBuildMCP  

你是否已在工作流程中嘗試讓 AI 參與建置與測試？歡迎在留言區分享你的經驗或遇到的挑戰 👇

#iOS #macOS #AI coding #ModelContextProtocol #Xcode #Cursor #ClaudeCode #DeveloperTools
