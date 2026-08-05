---
title: New release of LLM adds support for reasoning traces, OpenAI Responses, server-side
  tools, and smarter logging
source: Simon Willison
url: https://simonwillison.net/2026/Aug/4/new-release-of-llm/
model: tencent/hy3:free
generated_at: '2026-08-05T08:49:53.662206'
score: 83
---

📌 【LLM 0.32 重大更新】支援推理軌跡與伺服器端工具，LLM 正向 Agent 演進

TL;DR：LLM 0.32 引入推理軌跡可視化、OpenAI Responses 與伺服器端工具支援，大幅強化 Agent 實作能力。

Simon Willison 發布了 LLM 專案自啟動以來最重要的版本——0.32。這次更新不僅是功能堆疊，更從底層架構重新思考了對話紀錄的儲存方式，並讓 LLM 工具鏈更具備「Agent（代理）」的特質。

🧩 **推理過程不再是黑盒，可獨立於標準輸出顯示**

隨著推理模型（Reasoning Models）成為主流，觀察模型的「思考過程」變得至關重要。

- **推理軌跡可視化**：現在 LLM 在執行推理模型時，會將推理軌跡（Reasoning Traces）導向標準錯誤輸出（stderr）。
- **工程師優勢**：這讓開發者可以在不干擾標準輸出（stdout）的情況下，直接在終端機看到模型的思考邏輯，非常適合需要將輸出導向其他工具（pipe to another tool）的自動化流程。
- **自訂控制**：若不需要看到這些資訊，可以使用 `-R` 或 `--hide-reasoning` 參數關閉。

🛠️ **從單純的 Prompt 到強大的工具調用（Tool Use）**

LLM 現在能更流暢地整合來自不同供應商的伺服器端工具（Server-side tools），這對建構複雜工作流至關重要。

- **OpenAI 與 Anthropic 的整合**：
    - OpenAI 提供程式碼執行環境（Code execution environment）與網頁搜尋（WebSearch）工具。
    - `llm-anthropic` 插件現在支援 WebSearch、WebFetch、CodeExecution 以及 Anthropic MCP。
- **MCP 協定整合**：透過 Anthropic MCP，LLM 可以在單次請求中，對 `datasette-mcp` 插件發起 MCP 調用，實現更深層的互動。
- **一鍵測試相容端點**：新增 `llm openai` 指令，可以用單行指令對任何符合 OpenAI API 規範的端點進行測試。

📊 **採用類似 Git 的內容定址（Content-addressable）儲存機制**

隨著模型回傳的內容日益複雜（包含推理文字、工具調用、圖片附件等），傳統的儲存方式已不足以應付。

- **解決重複紀錄問題**：在對話模式中，每次請求都會攜帶完整的歷史紀錄，若傳統儲存會導致大量重複的 JSON 資料。
- **新的訊息儲存設計**：新版本採用了模仿 Git 的「內容定址訊息儲存（Content-addressable message store）」，能更高效地處理重複的訊息序列。
- **向下相容**：`llm logs` 指令已升級，能將新格式轉換回易於閱讀的格式。

🤖 **邁向 Agent 時代：工具鏈與人類審核**

作者提到，LLM 的設計正逐漸呈現出「Agent 形態」：

- **定義進化**：作者現在認同「LLM Agent 是透過循環執行工具來達成目標」的定義。
- **支援中斷與恢復**：新的工具鏈支援「等待人類審核（Human approval）」並從儲存的訊息歷史中恢復，這對於開發如 `Datasette Agent` 這類複雜代理系統是必要的。
- **API 抽象層升級**：Python API 現在支援 `model.prompt(messages=[])` 參數，讓開發者能直接操作訊息序列，而非受限於過於簡化的對話抽象。

🎯 **實務啟示**

對於需要開發 Agent 系統的工程師，LLM 0.32 提供了更底層、更靈活的控制權。透過支援 MCP 協定與更精細的訊息管理，開發者可以更輕鬆地處理複雜的工具調用與長對話歷史，而不必擔心資料冗餘或輸出格式混亂。

🔗 **來源**
- 標題：New release of LLM adds support for reasoning traces, OpenAI Responses, server-side tools, and smarter logging
- 作者／機構：Simon Willison
- 連結：https://simonwillison.net/2026/Aug/4/new-release-of-llm/

#LLM #AI #OpenAI #Anthropic #Agent #MCP #MachineLearning #Python #OpenSource #SoftwareEngineering
