---
title: google-gemini/gemini-cli
source: GitHub Trending
url: https://github.com/google-gemini/gemini-cli
score: 99
model: google/gemma-4-31b-it:free
generated_at: '2026-07-13T08:51:08.712989'
---

📌 Gemini CLI：在終端機直接呼叫 Google Gemini 大模型

TL;DR：Gemini CLI 讓開發者用簡單指令在本機終端機即時對話 Gemini 3，支援搜尋、檔案與 Shell，免費配額 60 req/min、1 k req/天。

🎣 只要在命令列輸入 `gemini`，即能把文字提示送到 Google 最新的 Gemini 3 大模型，取得 1 M token 上下文與加強推理，且不需要額外 UI 或雲端服務。

🤔 為什麼要在 CLI 使用 Gemini？

- **免費配額**：個人 Google 帳號即可每分鐘 60 次、每日 1 000 次請求，足以支援日常開發與測試需求。  
- **模型效能**：內建 Gemini 3 系列，大幅提升推理能力與長上下文（最高 1 M token）。  
- **工具整合**：內建 Google Search 取證、檔案讀寫、Shell 指令與網頁抓取等功能，讓 AI 能直接操作本機資源。  
- **可擴充**：支援 MCP（Model Context Protocol），開發者可自行加入自訂工具或模型。  
- **終端機優先**：設計理念即「開發者在命令列工作」的情境，省去切換 UI 的摩擦。  
- **開源授權**：採用 Apache 2.0，企業與個人皆可自由商業或二次開發。

🧩 主要功能與架構概述（依 README 說明）

- **指令入口**：`gemini`（或 `npx @google/gemini-cli` 直接執行，免安裝）。  
- **模型呼叫**：CLI 內部透過 Google 提供的 API 金鑰與 GEMINI 3 端點溝通，將使用者提示轉成 HTTP 請求。  
- **內建工具**：  
  - `search`：自動使用 Google Search 為回應提供最新資訊。  
  - `file`：讀寫本機檔案，支援 `cat`, `write`, `append` 等操作。  
  - `shell`：執行任意 Shell 指令，結果可回傳給模型作為後續推理依據。  
  - `fetch`：抓取指定 URL 的內容，供模型分析。  
- **MCP 支援**：透過 Model Context Protocol，開發者可以自行註冊「工具」或「外部模型」讓 Gemini 在對話中呼叫。  

📦 安裝方式一覽

| 方法 | 指令 | 說明 |
|------|------|------|
| **即時執行** | `npx @google/gemini-cli` | 無需安裝，直接下載執行 |
| **npm 全域** | `npm install -g @google/gemini-cli` | 於全域環境安裝 `gemini` 指令 |
| **Homebrew** | `brew install gemini-cli` | macOS / Linux 推薦方式 |
| **MacPorts** | `sudo port install gemini-cli` | macOS 另一套件管理器 |
| **Conda** | `conda create -n gemini_env -c conda-forge nodejs && conda activate gemini_env && npm install -g @google/gemini-cli` | 受限環境（如企業內部）可用 Conda 建立隔離環境後安裝 |

⚠️ 限制與注意事項

- **配額限制**：免費層每分鐘 60 次、每日 1 000 次請求，若需要更高頻率需自行申請付費配額。  
- **執行環境**：需要 Node.js 環境；在受限企業網路下可能需要透過 Proxy 或 VPN 取得 Google API 存取權。  
- **功能範圍**：目前僅支援文字對話與上述內建工具，未提供多模態（影像、音訊）支援。  

🎯 實務啟示

- **快速原型**：開發者可在終端機直接詢問程式碼建議、除錯步驟或檔案說明，省去切換 IDE 或瀏覽器的時間。  
- **自動化指令碼**：結合 `shell` 與 `file` 工具，可讓 Gemini 協助產生或修改指令碼，實作「AI 助理」式的 CI/CD 步驟。  
- **資訊取證**：利用內建 `search`，在寫程式或撰寫報告時即時取得最新網路資訊，避免手動搜尋。  
- **擴充性**：若團隊已有自訂工具，只要實作 MCP 介面即可讓 Gemini 在對話中直接呼叫，打造專屬的 AI 工作流。  

🔗 來源
- 標題：google-gemini/gemini-cli
- 作者／機構：google-gemini
- 連結：https://github.com/google-gemini/gemini-cli

#GeminiCLI #GoogleGemini #LLM #AItools #CommandLine #OpenSource #MCP #NodeJS #DeveloperTools #AIassistant
