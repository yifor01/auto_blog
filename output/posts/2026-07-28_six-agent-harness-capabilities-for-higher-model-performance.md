---
title: Six Agent Harness Capabilities for Higher Model Performance
source: NVIDIA Developer
url: https://developer.nvidia.com/blog/six-agent-harness-capabilities-for-higher-model-performance/
model: tencent/hy3:free
generated_at: '2026-07-28T08:26:27.343421'
score: 104
---

📌 【NVIDIA Labs 新框架】NOOA 釋出：透過物件導向架構，讓 Agent 的效能與記憶管理更強大

TL;DR：NVIDIA Labs 開源的 NOOA 框架透過物件導向設計，大幅提升 Agent 的效能與記憶管理效率。

🎣 **Agent 的成敗，架構設計比模型選擇更關鍵**

建構出優秀的 AI Agent 並不只是選對模型那麼簡單。Harness（框架/工具架構）的設計——包含 Context（上下文）的渲染方式、動作執行、狀態管理以及任務終止的判定——對最終結果的影響力，與模型本身一樣巨大。研究顯示，即使使用相同的底層模型，不同的架構設計可能導致 Benchmark（基準測試）結果出現雙位數的落差，並造成 Token 成本的顯著差異。

🧩 **NOOA：以物件導向設計為核心的 Agent 框架**

NVIDIA Labs 推出的 NOOA（Object-Oriented Agents）是一個開源的研發預覽版框架，其核心設計理念如下：

- **物件導向結構**：將 Agent 結構化為單一的 Python Class（類別）。
- **整合能力與狀態**：透過 Method（方法）、Field（欄位）與 Docstring（文件字串）來整合 Agent 的能力、狀態與 Prompt（提示詞）。
- **型別安全（Type Safety）**：使用 Type Annotation（型別註解）作為強制性的 Contract（契約），確保執行的一致性。
- **LLM 驅動迴圈**：對於標記為 Ellipses（省略號）的方法，會在執行時由 LLM 驅動完成其方法體。

📊 **具備長期記憶與高效 Context 管理**

NOOA 解決了 Agent 在處理複雜任務時常見的記憶與成本問題：

- **持久化記憶**：Agent 能在可讀性高的 SQLite 儲存中，策劃並保存具備型別與關聯性的長期記憶，實現知識累積。
- **高效上下文管理**：透過 Pass-by-reference（傳址呼叫）機制進行 Context 管理，有效避免了傳統框架中常見的 Context Compaction（上下文壓縮）或 Summarization（摘要）流水線的需求。

🚀 **在多項 Benchmark 中展現卓越效能**

在 SWE-bench Verified、CyberGym L1 以及 ARC-AGI-3 等基準測試中，NOOA 展現了領先的性能與效率：

- **高準確度與低成本**：與先前的 Harness 相比，NOOA 在提升準確度的同時，能有效降低 Token 成本。
- **可重現性**：提供可檢查的工作流與開放的評估方法論，讓社群可以進行重現與擴充。

🎯 **實務啟示**

對於工程師而言，NOOA 的出現提示我們：在開發 Agent 時，不應只專注於 Prompt Engineering，更應關注 Agent 的架構設計（Harness Design）。透過引入物件導向的開發模式與結構化的記憶管理，可以更有效地控制 Token 成本，並提升 Agent 在複雜任務下的穩定性。

🔗 **來源**
- 標題：Six Agent Harness Capabilities for Higher Model Performance
- 作者／機構：Michelle Horton / Ricardo Silveira Cabral and Paul Furgale @ NVIDIA
- 連結：https://developer.nvidia.com/blog/six-agent-harness-capabilities-for-higher-model-performance/

#AI #AgenticAI #GenerativeAI #NVIDIA #NOOA #Python #MachineLearning #LLM #OpenSource #SoftwareArchitecture
