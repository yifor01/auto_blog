---
title: xAI Launches /goal in Grok Build, Adding Long-Running Autonomous Execution
  With Built-In Verification for Multi-Step Coding Tasks
source: MarkTechPost
url: https://www.marktechpost.com/2026/06/22/xai-launches-goal-in-grok-build-adding-long-running-autonomous-execution-with-built-in-verification-for-multi-step-coding-tasks/
score: 85
model: google/gemma-4-31b-it:free
generated_at: '2026-06-22T21:06:40.924838'
---

📌 xAI 為 Grok Build 推出 /goal 模式：實現長時程自主執行與多步驟驗證

TL;DR：Grok Build 新增 /goal 指令，讓 AI 能自主執行「計畫→行動→觀察→再計畫」迴圈直至完成複雜開發任務。

大多數的 AI 輔助程式設計體驗是碎片化的：你下指令，AI 執行，你檢查，然後再下下一個指令。這種反覆的互動迴圈在面對大型實作任務時極其低效。xAI 試圖打破這個迴圈，讓開發者能將整個目標「交接」給 AI。

🤔 **從「單次指令」轉向「目標導向」的自主執行**

xAI 在其終端機程式設計代理（coding agent）Grok Build 中推出了 `/goal` 模式。與傳統的單次 Prompt 不同，`/goal` 允許使用者定義一個最終目標，隨後 AI 會接管整個多步驟的工作流程。

其核心運作邏輯在於建立一個「觀察—計畫—行動」（observe–plan–act）的閉環：
1. **計畫**：將目標拆解為具體的進度檢查清單（progress checklist）。
2. **執行**：逐步執行清單中的任務。
3. **觀察與驗證**：透過檢查程式碼、檢視網頁或執行指令碼來驗證結果。
4. **動態調整**：當實際結果與預期不符時，AI 會自動重新計畫（replan）並修正路徑。

🧩 **Grok Build 的技術能力與整合**

`/goal` 並非獨立產品，而是 Grok Build 這一 CLI 工具中的一個模式。Grok Build 作為軟體工程的終端代理，具備以下技術特性：
- **本地 codebase 存取**：直接在終端機執行，能讀取本地檔案並執行命令。
- **平行處理**：能將大型工作委派給多個專業的子代理（subagents）平行執行。
- **擴展能力**：原生支援讀取 `AGENTS.md`、外掛、hooks、skills 以及 MCP（Model Context Protocol）伺服器，將代理連線至外部工具與資料。
- **控制機制**：提供「計畫模式」可在編輯前要求使用者核准計畫，並透過進度清單與導向指令（steering commands）解決長時程執行時的監控問題。

🎯 **實務啟示：開發者的角色轉變**

對於工程師而言，`/goal` 的引入將開發流程從「微觀管理（Micro-managing）」轉向「目標管理」。開發者的工作重點將從「告訴 AI 每一步怎麼做」轉變為「定義清晰的目標」與「監督最終驗證結果」。

然而，這種高度自主化帶來了可觀察性（observability）的挑戰。由於長時程執行會產生大量操作，開發者需依賴 Grok Build 提供的進度清單來監控進度，而非僅僅依賴單次輸出。

🔗 **來源**
- 標題：xAI Launches /goal in Grok Build, Adding Long-Running Autonomous Execution With Built-In Verification for Multi-Step Coding Tasks
- 作者／機構：Michal Sutter
- 連結：https://www.marktechpost.com/2026/06/22/xai-launches-goal-in-grok-build-adding-long-running-autonomous-execution-with-built-in-verification-for-multi-step-coding-tasks/

#xAI #GrokBuild #CodingAgent #CLI #AutonomousAI #SoftwareEngineering #MCP #DeveloperTools #AIProgramming #Automation
