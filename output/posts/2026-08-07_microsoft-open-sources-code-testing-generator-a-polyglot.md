---
title: 'Microsoft Open Sources code-testing-generator: a Polyglot Unit-Test Agent
  That Hits 92.1% Task Completion Versus 78.9% for Stock Copilot'
source: MarkTechPost
url: https://www.marktechpost.com/2026/08/06/microsoft-open-sources-code-testing-generator/
model: tencent/hy3:free
generated_at: '2026-08-07T07:34:33.650561'
score: 97
---

📌 【Microsoft 開源新專案】多語言單元測試代理：任務完成率達 92.1%，表現優於 GitHub Copilot

TL;DR：Microsoft 開源 `code-testing-generator` 代理，透過 RPI 流程自動化測試生成與驗證，效能大幅超越 GitHub Copilot。

當你在 Prompt 輸入「產生單元測試」時，AI 往往不知道該用哪個框架、檔案位置或斷言（assertion）方式。Microsoft 針對這個開發痛點，推出了 `code-testing-generator`，這是一個能夠主動讀取專案結構、規劃、撰寫並驗證測試的代理（Agent）。

🧩 **RPI 流程：從讀取專案到驗證測試的自動化循環**

該代理採用「研究-規劃-實作」（Research-Plan-Implement, RPI）的流水線工作模式：
1. **研究 (Research)**：搜尋專案中需要測試的程式碼、偵測語言與測試框架、閱讀現有測試以掌握慣例，並找出實際的編譯與測試指令（確保測試能成功在 CI 環境執行，而非僅能在本地建置）。
2. **規劃 (Plan)**：根據研究結果決定策略。
3. **實作 (Implement)**：根據範圍選擇以下三種策略之一：
    - 直接撰寫並立即驗證。
    - 單次執行（Single pass）。
    - 迭代執行（Iterative，適用於大規模範圍或高覆蓋率目標）。

⚠️ **安全性與穩定性限制**
為了確保測試的安全性與可靠性，該代理被設定為：
- 絕不修改生產環境程式碼（Production code）。
- 避免生成會呼叫外部 URL、綁定連接埠（bind ports）或依賴時間間隔的測試。

📊 **效能表現：在模糊指令下展現強大適應力**

在 Microsoft 內部的 152 個任務基準測試中，`code-testing-generator` 的表現大幅領先：

| 測試類型 | `code-testing-generator` 完成數 | GitHub Copilot 完成數 |
| :--- | :--- | :--- |
| **總體任務完成率** | **92.1% (140/152)** | **78.9% (120/152)** |
| 模糊指令 (Vague prompts) | 88.8% (79/89) | 66.3% (59/89) |
| 詳細指令 (Detailed prompts) | 96.8% (61/63) | 96.8% (61/63) |
| 特定 Diff 任務 | 100% (15/15) | 0% (0/15) |

💡 **深入分析：更精簡、更聰明的測試生成**

有趣的是，雖然完成率更高，但該代理生成的測試行數反而更少（6,963 筆 vs 7,129 筆），卻達到了幾乎相同的程式碼覆蓋率（72.4% vs 72.2%），這代表其生成的測試更具效率，而非僅是堆疊程式碼。

在針對.NET 任務的測試中，使用該代理後，Claude Opus 模型的完成率從 35/45 提升至 43/45；GPT-5.5 則從 36/45 提升至 41/45。

🎯 **實務啟示**

`code-testing-generator` 目前以 `dotnet-test` 插件的形式收錄於 MIT 授權的 `dotnet/skills` 專案中。它並非一個託管服務，而是一個代理定義（Agent definition）與技能集（Skills），可以直接整合進你現有的開發代理流程中，且程式碼會保持在本地端執行，確保安全性。

🔗 **來源**
- 標題：Microsoft Open Sources code-testing-generator: a Polyglot Unit-Test Agent That Hits 92.1% Task Completion Versus 78.9% for Stock Copilot
- 作者／機構：Michal Sutter @ MarkTechPost
- 連結：https://www.marktechpost.com/2026/08/06/microsoft-open-sources-code-testing-generator/

#Microsoft #OpenSource #UnitTesting #AIagent #GitHubCopilot #SoftwareEngineering #Dotnet #MachineLearning #CodeQuality #DeveloperTools
