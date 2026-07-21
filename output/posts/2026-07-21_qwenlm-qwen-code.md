---
title: QwenLM/qwen-code
source: GitHub Trending
url: https://github.com/QwenLM/qwen-code
score: 124
model: tencent/hy3:free
generated_at: '2026-07-21T08:22:31.927469'
---

📌 【Alibaba Qwen 開源新專案】打造住在 Terminal 裡的 AI 編碼代理 (Coding Agent)

TL;DR：Qwen Code 是一個開源的終端機 AI Agent，內建自動記憶與多代理協作機制，並支援多種 API 與本地模型。

🚀 **不用安裝複雜環境，直接在終端機開啟 Agent 模式**

當開發者習慣於在 Terminal 進行操作時，Qwen Code 提供了一種「開箱即用」的 Agentic 工作流。它不只是單純的對話介面，而是具備了自動記憶 (Auto-Memory)、自動技能 (Auto-Skills)、子代理 (SubAgents)、代理團隊 (Agent Teams) 以及 Model Context Protocol (MCP) 的完整代理架構。

🧩 **高度靈活的架構與多協議支援**

Qwen Code 的設計核心在於「無供應商鎖定 (No vendor lock-in)」，開發者可以根據需求在執行期間切換不同的模型後端：

- **支援協議**：OpenAI、Anthropic、Gemini 以及 Qwen API。
- **支援來源**：任何第三方供應商或本地模型（如 Ollama、vLLM）。
- **多樣化介面**：除了 Terminal，還支援 IDE 擴充功能、桌面應用程式、守護行程 (daemon mode)、SDK，以及即時通訊機器人（如 Telegram、DingTalk、WeChat、Feishu）。

💡 **框架與模型同步演進的開源生態**

與單純使用 API 的工具不同，Qwen Code 採用的框架與底層的 Qwen 模型皆為開源，兩者同步演進。值得注意的是，Qwen Code 正在實踐「用 AI 迭代自身」的模式——利用自身的 Agent 與模型來提交 Issue、提交 Pull Request (PR)、進行程式碼審核 (Code Review) 以及執行測試。

🛠️ **快速上手與安裝方式**

安裝完成後，請重啟終端機以確保環境變數生效。

- **Linux / macOS**：
  `curl -fsSL https://qwen-code-assets.oss-cn-hangzhou.aliyuncs.com/installation/install-qwen-standalone.sh | bash`
- **Windows**：
  `irm https://qwen-code-assets.oss-cn-hangzhou.aliyuncs.com/installation/install-qwen-standalone.ps1 | iex`
- **NPM (需 Node.js 22+)**：
  `npm install -g @qwen-code/qwen-code@latest`
- **Homebrew (macOS / Linux)**：
  `brew install qwen-code`

使用方式：在終端機輸入 `qwen` 即可啟動互動式 UI；進入 session 後，可透過 `/auth` 指令配置 Provider 與 API Key。

🔗 **來源**
- 標題：QwenLM/qwen-code
- 作者／機構：Alibaba — QwenLM
- 連結：https://github.com/QwenLM/qwen-code

#AI #Coding #OpenSource #Qwen #Alibaba #CodingAgent #Terminal #DeveloperTools #LLM #SoftwareEngineering
