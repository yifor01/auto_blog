---
title: "Vercel Labs Introduces Zero, a Systems Programming Language Designed So AI Agents Can Read, Repair, and Ship Native Programs"
source: MarkTechPost
url: https://www.marktechpost.com/2026/05/17/vercel-labs-introduces-zero-a-systems-programming-language-designed-so-ai-agents-can-read-repair-and-ship-native-programs/
score: 83
model: tencent/hy3-preview:free
generated_at: 2026-05-17T19:39:19.755873
---

📌 **Vercel Labs 推出 Zero：專為 AI Agent 設計的系統程式語言**

AI 輔助開發工具正在改變我們寫程式的方式，但大多數編譯器仍把錯誤訊息當作給人類閱讀的文字來輸出。這意味著 AI Agent 必須先解析非結構化的錯誤訊息，才能決定該怎麼修復程式碼——一個既脆弱又低效的過程。Vercel Labs 的最新實驗語言 Zero 想要改變這個流程，讓編譯器的輸出本身就具備機器可讀的結構，從而讓 Agent 更自然地讀取、修復與交付原生程式。

🤔 **為什麼現有語言對 AI Agent 不友好？**

在典型的編寫‑編譯‑除錯迴圈中，人類開發者可以靠經驗快速從錯誤訊息中判斷問題所在。然而，錯誤訊息往往是：
- 非結構化的自由文字
- 格式會隨版本或編譯器變動而改變
- 沒有明確的「修復動作」描述

這些特徵讓 AI Agent 必須額外執行文字解析步驟，增加失誤機率，也降低了自動修復的可靠性。Zero 正是針對這個缺口而設計：從語言設計到編譯器與 CLI 工具鏈，都以「可被 Agent 直接消化」為首要目標。

🧪 **Zero 的核心設計：結構化診斷與統一工具鏈**

Zero 是一種系統程式語言，定位與 C、Rust 相近——它編譯成原生執行檔、提供顯式記憶體控制、適用於低階環境。與傳統語言不同的是，Zero 的編譯器預設會以 **JSON 格式** 輸出診斷資訊。舉例來說，執行 `zero check --json` 會得到類似以下結構的輸出（實際欄位來自原文描述）：

```json
{
  "code": "NAM003",
  "message": "human‑readable description",
  "location": { "line": 12, "column": 5 },
  "repair": {
    "id": "typed‑repair‑identifier",
    "details": "..."
  }
}
```

- 人類開發者仍可閱讀 `message` 來理解問題。
- AI Agent 則可以直接讀取穩定的 `code` 與 `repair` 欄位，決定具體的修復步驟，無需額外的文字解析或啟發式規則。

Zero 的 CLI 被設計成單一二進位檔案，包含以下子命令（皆為同一工具的不同模式）：
- `zero check`、`zero run`、`zero build`
- `zero graph`、`zero size`、`zero routes`
- `zero skills`、`zero explain`、`zero fix`、`zero doctor`

這意味著 Agent 在執行不同任務時，無需切換工具或記住多個指令；統一的介面降低了工作流程的認知負擔。

🔍 **核心發現：結構化輸出讓 Agent 更易於修復程式**

根據原文描述，Zero 的主要貢獻在於：**將編譯器的錯誤訊息與修復建議包裝成可預測的結構化資料**，這直接解決了 Agent 在傳統工具鏈中必須面對的「非結構化錯誤訊息」問題。雖然文件中未提供具體的效能基準或使用者研究數據，但設計意圖很明確——讓 Agent 能夠：
1. 快速辨識錯誤類型（透過穩定的代碼如 `NAM003`）。
2. 取得型別化的修復動作（`repair` 物件），從而產生更精準的程式碼變更。
3. 在不離開同一個 CLI 的情況下完成檢查、執行與建置等全流程。

💡 **深入分析：結構化診斷是 Agentic 工作流的基礎設施**

傳統語言的診斷輸出是為了人類的閱讀習慣而優化；這種設計在人機協作的情境下會產生額外的解析成本。Zero 的做法把「診斷」視為一種 **API**，而非 soltanto 日誌。這種思維與近年在 LLMs 工具鏈中的趨勢不謀而合——例如，函式呼叫工具（function calling）與結構化回應（JSON schema）正是為了讓模型能可靠地執行動作。Zero 將相同的理念帶到了系統程式語言的層級，意味著未來的 AI Agent 可能不再需要額外的「錯誤訊息解析器」或「啟發式修復規則」，而是直接依賴語言本身提供的契約。

⚠️ **研究限制：實驗階段、尚未廣泛採用**

- Zero 目前標示為 **實驗性語言**，尚未有穩定版本或長期支援計畫。
- 文件中未提及任何實際專案或商業採用案例，因此其在真實生產環境中的表現、編譯速度與 binary 大小等指標仍未經驗證。
- 由於缺乏社群與套件生態系統，開發者可能需要自行建構工具鏈或依賴有限的標準庫。

🎯 **實務啟示：關注結構化回應設計，為 Agent 準備更好的工具鏈**

即使 Zero 本身尚未成熟，它所提出的設計原則對當前的 AI 輔助開發已具啟發性：
- 在設計或選擇程式語言、框架或 CLI 工具時，考慮其輸出是否具備 **穩定、型別化的結構**（例如 JSON、Protocol Buffers）。
- 若正在打造內部的 Agent 工作流，優先提供 **可直接消化的診斷或回饋格式**，而非依賴後端文字解析。
- 關注語言或工具是否提供 **統一的入口點**（單一二進位或單一端點），以減少 Agent 在任務切換時的決策負擔。

🔗 **參考資訊**
📝 **標題**：Vercel Labs Introduces Zero, a Systems Programming Language Designed So AI Agents Can Read, Repair, and Ship Native Programs  
👤 **作者**：Michal Sutter（據 MarkTechPost 報導）  
🔗 **連結**：https://www.marktechpost.com/2026/05/17/vercel-labs-introduces-zero-a-systems-programming-language-designed-so-ai-agents-can-read-repair-and-ship-native-programs/  

你認為結構化診斷對 AI Agent 的實用性有多大？歡迎在留言區分享你看法 👇

#AI #AgenticWorkflow #SystemsProgramming #ZeroLanguage #VercelLabs #程式語言 #開發工具 #MachineLearning #GenAI #程式除錯
