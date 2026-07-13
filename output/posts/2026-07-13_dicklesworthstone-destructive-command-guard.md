---
title: Dicklesworthstone/destructive_command_guard
source: GitHub Trending
url: https://github.com/Dicklesworthstone/destructive_command_guard
score: 90
model: google/gemma-4-31b-it:free
generated_at: '2026-07-13T08:57:44.715269'
---

📌 防止 AI 程式編寫助手誤刪檔案的「Destructive Command Guard」  
TL;DR：dcg 提供跨平臺掛鉤，於 Claude、Codex、Gemini、Copilot 等 AI 編碼工具執行前攔截破壞性指令，保護專案不被意外刪除。

🧩 **AI 編碼工具的安全盲點**  
許多開發者已經在使用 Claude Code、Codex CLI、Gemini CLI、GitHub Copilot CLI、VS Code Copilot Chat、Cursor、Hermes Agent、Grok (xAI) 等 AI 代理協助寫程式。這些工具會直接在終端或 IDE 中執行指令，若提示不夠精確或模型誤判，可能會下達 `rm -rf`、`git reset --hard` 等破壞性指令，導致檔案或版本庫意外遺失。

🛡️ **dcg：在指令執行前先過濾**  
Destructive Command Guard（dcg）是一個高效能的掛鉤程式，會在上述 AI 代理發出指令前先行檢查，若偵測到可能造成檔案刪除或重大變更的命令，就阻止其執行。支援的環境包括：

- Claude Code  
- Codex CLI（版本 0.125.0 以上）  
- Gemini CLI  
- GitHub Copilot CLI  
- VS Code Copilot Chat（透過 VS Code 的 Claude‑hook 相容層）  
- Cursor IDE  
- Hermes Agent  
- Grok (xAI)（原生 `~/.grok/hooks/` 或 Claude 相容層）  
- Antigravity CLI (agy)（透過 `~/.gemini/config/hooks.json`）  
- OpenCode、Pi、Aider（限 Git hooks）與 Continue（僅偵測）

⚙️ **快速安裝與跨平臺支援**  
dcg 提供一鍵安裝指令碼，使用 `curl` 直接下載並執行 `install.sh`，自動偵測作業系統（Linux、macOS、WSL）下載相應二進位檔，並完成各 AI 代理的掛鉤設定。例如：

```bash
curl -fsSL "https://raw.githubusercontent.com/Dicklesworthstone/destructive_command_guard/main/install.sh?$(date +%s)" | bash -s -- --easy-mode
```

在原生 Windows 環境下，可改用 PowerShell 安裝指令碼（README 內有說明）。安裝完成後，dcg 會在每個支援的工具中注入檢查機制，確保所有指令在執行前先經過安全審核。

🎯 **實務啟示**  
- **即時防護**：在開發流程中加入 dcg，可在不改變既有 AI 工作流程的前提下，降低因誤指令導致的資料遺失風險。  
- **CI/CD 整合**：對於使用 Aider 或其他 Git hook 支援的工具，dcg 亦能在提交前檢查破壞性操作，避免將危險指令寫入版本歷史。  
- **跨工具一致性**：無論是本機 CLI、VS Code 外掛或雲端 IDE，dcg 的掛鉤方式保持一致，降低不同環境下的安全設定成本。  

🔗 來源  
- 標題：Dicklesworthstone/destructive_command_guard  
- 作者／機構：Dicklesworthstone  
- 連結：https://github.com/Dicklesworthstone/destructive_command_guard  

#AI #Security #DevOps #CLI #GitHooks #Claude #Codex #Gemini #Copilot #VSCode #Cursor #Hermes #Grok #OpenSource #Tooling
