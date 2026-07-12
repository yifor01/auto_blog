---
title: openai/codex
source: GitHub Trending
url: https://github.com/openai/codex
score: 91
model: google/gemma-4-31b-it:free
generated_at: '2026-07-12T08:02:45.378865'
---

📌 OpenAI Codex CLI：在本機跑的程式碼助理

TL;DR：Codex CLI 是 OpenAI 提供的本地程式設計助理，支援多平臺安裝，可直接在終端機或 IDE 中呼叫。

🧩 **本地化的 Codex 代理人**

OpenAI 針對想在自己的電腦上使用 Codex 的開發者，推出了「Codex CLI」這個指令列工具。它可以直接在本機執行，無需透過瀏覽器或遠端服務，適合想在 VS Code、Cursor、Windsurf 等編輯器內整合、或是想要桌面應用體驗的使用者。

💡 **多樣安裝管道，支援主流平臺**

- **Mac / Linux**：一行 curl 指令即可安裝  
  `curl -fsSL https://chatgpt.com/codex/install.sh | sh`
- **Windows**：使用 PowerShell 執行  
  `powershell -ExecutionPolicy ByPass -c " irm https://chatgpt.com/codex/install.ps1 | iex "`
- **npm**：`npm install -g @openai/codex`
- **Homebrew**：`brew install --cask codex`
- 也可直接下載 GitHub Release 中的二進位檔，依平臺選擇對應的壓縮檔（macOS Apple Silicon、x86_64、Linux x86_64、arm64），解壓後把執行檔重新命名為 `codex` 即可。

⚙️ **使用方式與 ChatGPT 計畫整合**

安裝完成後，直接在終端機輸入 `codex` 即可啟動。首次執行會要求登入，選擇「Sign」以使用你現有的 ChatGPT 訂閱。之後可在支援的 IDE 中安裝相應外掛，讓 Codex 以助理的形式即時產生程式碼、完成補全或回應開發問題。

🎯 **實務啟示**

- **離線或低網路環境**：因為核心執行在本機，對於網路不穩或需在受限環境中開發的團隊相對友好。
- **工具鏈整合**：支援 npm、Homebrew 以及直接下載二進位檔，讓 DevOps 流程可輕鬆將 Codex CLI 納入 CI/CD 或容器映像檔中。
- **與雲端服務的選擇**：若需要即時更新或雲端資源，OpenAI 仍提供 Codex Web（chatgpt.com/codex），開發者可依需求在本地與雲端之間切換。

🔗 來源
- 標題：openai/codex
- 作者／機構：OpenAI — openai
- 連結：https://github.com/openai/codex

#OpenAI #CodexCLI #LLM #DeveloperTools #LocalAI #IDEIntegration #CLI #GitHub #CodingAssistant #MachineLearning
