---
title: Hmbown/CodeWhale
source: GitHub Trending
url: https://github.com/Hmbown/CodeWhale
score: 86
model: google/gemma-4-31b-it:free
generated_at: '2026-07-02T19:59:02.016834'
---

📌 **CodeWhale：支援多模型的終端機編碼代理，將 LLM 轉化為 TUI 開發助手**

TL;DR：一個用 Rust 編寫的開源終端機編碼代理，支援 DeepSeek、Claude、GPT 等多模型，可自動讀碼、編輯並執行指令。

想像你的終端機不只是輸入指令的地方，而是一個能閱讀整個專案、規劃多步驟任務、執行命令並在失敗時自我修正的 AI 助手。CodeWhale 正是將這種能力直接整合進 TUI (Terminal User Interface) 的工具。

🤔 **從 DeepSeek 專用工具演進至通用代理**

CodeWhale 最初是以 `deepseek-tui` 之名啟動，旨在圍繞 DeepSeek 的工作流建立一套編碼框架。由於社群（尤其是中國開發者）的積極採納與貢獻，作者發現這套框架的潛力遠超單一模型，因此將其擴充套件為支援多供應商的通用版本，並正式更名為 CodeWhale。

🧩 **核心功能與運作邏輯**

CodeWhale 扮演的是一個 Coding Agent 的角色，使用者將其指向特定的模型與專案後，它能執行以下迴圈：
- **感知與分析**：讀取專案程式碼並理解上下文。
- **執行與編輯**：直接進行程式碼修改並執行終端機指令。
- **驗證與修正**：檢查執行結果，若發現錯誤則進行自我修正。
- **任務規劃**：針對複雜需求規劃多步驟的執行路徑。

💡 **靈活的模型供應商整合**

該專案採取「開源模型優先」的設計理念，提供極高的模型適配靈活性：
- **本地部署**：完全支援 LAN 上的 vLLM、SGLang 或 Ollama，且無需 API Key 即可執行。
- **主流模型**：DeepSeek 與開源權重模型被視為一等公民，同時也透過相同的執行環境與工具集，完整支援 Claude、GPT、Kimi 與 GLM。
- **路由機制**：使用者只需選擇供應商與模型，CodeWhale 會自動解析對應的路由並執行。

⚙️ **安裝與部署方式**

專案使用 Rust 編寫，並提供 npm 封裝以便快速安裝（需 Node 18+）：
- 安裝指令：`npm install -g codewhale`
- 安裝後會提供 `codewhale`、`codew` 與 `codewhale-tui` 三個指令。
- 安裝過程會從 GitHub Releases 下載經過 SHA-256 驗證的二進位檔，或可選擇自行從原始碼編譯。

🎯 **實務啟示**

對於偏好在終端機開發、不希望離開 CLI 環境，且對模型隱私有要求（傾向使用本地 vLLM/Ollama）的工程師來說，CodeWhale 提供了一個低摩擦的整合方案，將 AI 代理的能力直接下沉到開發最底層的 shell 環境中。

🔗 **來源**
- 標題：Hmbown/CodeWhale
- 作者／機構：Hmbown
- 連結：https://github.com/Hmbown/CodeWhale

#AI #CodingAgent #Rust #TUI #DeepSeek #LLM #OpenSource #CLI #vLLM #Ollama
