---
title: microsoft/AI-Engineering-Coach
source: GitHub Trending
url: https://github.com/microsoft/AI-Engineering-Coach
score: 85
model: tencent/hy3:free
generated_at: '2026-07-21T08:34:07.339541'
---

📌 【Microsoft 開源專案】AI Engineer Coach：打造你的 AI 程式碼助手專屬儀錶板

TL;DR：這款工具能分析 AI 程式設計助手的 Session Log，將使用習慣轉化為可量化的開發洞察。

隨著 AI 輔助開發成為常態，我們究竟是在利用 AI 提升效率，還是在陷入低效率的重複勞動？Microsoft 推出的 AI Engineer Coach 試圖透過資料化的方式，回答這個問題。

🧩 **讀取本地 Log，將開發紀錄轉化為行動建議**

AI Engineer Coach 的設計核心在於「隱私」與「洞察」。它會讀取你在本地端進行的 AI Session Log，並將其轉換為具備行動價值的分析結果，且強調所有資料都不會離開你的個人電腦。

📊 **多維度的開發效能分析**

透過這個工具，你可以從以下幾個面向掌握自己的開發狀態：

- **追蹤進度**：包含練習分數、每週趨勢以及每日活動圖表。
- **偵測反模式 (Anti-patterns)**：針對提示詞品質 (Prompt Quality)、工作階段衛生 (Session Hygiene)、程式碼審查 (Code Review)、工具掌握度 (Tool Mastery) 以及上下文管理 (Context Management) 制定了 45 條規則進行檢查。
- **衡量輸出量**：可以依據程式語言、工作區、模型以及開發框架 (Harness) 來統計 AI 生成程式碼的數量。
- **技能發現**：識別重複使用的提示詞，並將其轉化為可重複使用的技能。
- **評估上下文健康度**：進行 Agentic readiness (代理就緒度) 檢查、指令檔 (Instruction-file) 審核，以及工作區上下文地圖 (Workspace Context Maps) 繪製。

🛠️ **安裝方式：需自行建置.vsix 檔案**

由於該擴充功能目前尚未釋出至 Marketplace 或 Release 頁面，使用者需要自行建置並安裝.vsix 檔案。

**路徑 1：使用 Dev Container 建置（無需本地 Node.js/npm 環境）**
1. 前提條件：需安裝 VS Code Dev Containers 擴充功能，以及 Docker 或 Podman。
2. 步驟：Clone 儲存庫並在 VS Code 中開啟 $\rightarrow$ 在容器中重新開啟 $\rightarrow$ 執行 `npm ci` 與 `npm run package`。

**路徑 2：本地建置**
1. 前提條件：需具備 VS Code、Node.js 與 npm。
2. 步驟：`git clone https://github.com/microsoft/ai-engineering-coach.git` $\rightarrow$ `cd ai-engineering-coach` $\rightarrow$ `npm ci` $\rightarrow$ `npm run package`。
3. 安裝：在 macOS / Linux 執行 `code --install-extension <建置好的 VSIX 檔案路徑>`。

🎯 **實務啟示**

對於追求高效開發的工程師而言，這是一個極佳的自我檢視工具。透過量化 AI 的使用行為，你可以發現自己是否過度依賴低品質的提示詞，或是哪些開發流程可以透過標準化 Prompt 來最佳化。

🔗 **來源**
- 標題：microsoft/AI-Engineering-Coach
- 連結：https://github.com/microsoft/AI-Engineering-Coach

#AI #Microsoft #AIEngineer #VSCode #OpenSource #Productivity #SoftwareEngineering #LLM #DeveloperTools #CodingAssistant
