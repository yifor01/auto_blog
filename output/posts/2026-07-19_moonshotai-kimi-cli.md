---
title: MoonshotAI/kimi-cli
source: GitHub Trending
url: https://github.com/MoonshotAI/kimi-cli
score: 77
model: tencent/hy3:free
generated_at: '2026-07-19T08:06:26.703835'
---

📌 【MoonshotAI 開源】Kimi CLI：終端機裡的 AI 程式開發代理

TL;DR：MoonshotAI 推出終端 AI agent，能讀寫程式碼、跑 shell、搜網頁，並將遷移至 Kimi Code CLI。

在終端機裡寫程式時，如果每個操作都要切換視窗、複製貼上，節奏很容易被切斷。MoonshotAI 把一個能自己規劃步驟的 AI agent 直接放進命令列，讓開發與終端操作在同一個介面完成。

🤔 **Kimi CLI 是什麼，又為何即將退場**

README 指出，Kimi CLI 是一個執行於終端機的 AI agent，用來協助完成軟體開發任務與終端操作。它能讀取與編輯程式碼、執行 shell 指令、搜尋與擷取網頁內容，並在執行過程中自主規劃與調整動作。

不過作者宣稱，Kimi CLI 正演進為同團隊推出的下一代終端 AI agent「Kimi Code CLI」。安裝 Kimi Code CLI 會自動遷移你的設定與會話紀錄；此專案將逐步收攏，但檔案與既有安裝仍可使用。

🧩 **核心能力與設計理念**

Kimi CLI 定位不只是一個 coding agent，也試圖成為 shell 本身：

- 終端 AI agent：可讀寫程式碼、執行 shell 指令、搜尋並擷取網頁，執行中能自主規劃與調整。
- Shell 命令模式：按下 Ctrl-X 可切換到此模式，直接執行 shell 指令而不離開 Kimi CLI；但 README 註明，內建 shell 指令如 cd 尚不支援。
- VS Code 整合：可透過 Kimi Code VS Code Extension 與 Visual Studio Code 整合。
- IDE 整合 via ACP：原生支援 Agent Client Protocol (ACP)，可搭配任何相容 ACP 的編輯器或 IDE 使用。

⚙️ **怎麼用：以 ACP 模式接上 IDE**

README 提供的做法如下：

1. 在終端機執行 Kimi CLI，並輸入 `/login` 完成登入。
2. 設定你的 ACP client，以指令 `kimi acp` 啟動 Kimi CLI 作為 ACP agent server。
3. 以 Zed 或 JetBrains 為例，加入對應設定即可串接（README 未列出完整設定內容）。

🎯 **實務啟示**

對習慣命令列的工程師，Kimi CLI 提供「不離開終端就能請 AI 改程式、跑指令、查檔案」的工作流；若你已在使用 Zed、JetBrains 或 VS Code，可透過 ACP 或擴充套件把 agent 接進現有 IDE。但要注意，此專案正逐步退場，新使用者應直接評估 Kimi Code CLI，以免設定與會話後續還要再遷移一次。

🔗 **來源**
- 標題：MoonshotAI/kimi-cli
- 作者／機構：MoonshotAI
- 連結：https://github.com/MoonshotAI/kimi-cli

#KimiCLI #MoonshotAI #AIAgent #Terminal #CLI #SoftwareDevelopment #ACP #VSCode #KimiCode #OpenSource
