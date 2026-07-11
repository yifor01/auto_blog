---
title: agentscope-ai/agentscope
source: GitHub Trending
url: https://github.com/agentscope-ai/agentscope
score: 103
model: google/gemma-4-31b-it:free
generated_at: '2026-07-11T09:31:46.719169'
---

📌 **AgentScope 2.0 釋出：面向生產環境的靈活 Agent 架構**

TL;DR：AgentScope 2.0 釋出，強調事件驅動、許可權控制與隔離沙箱，讓 LLM 自主推理而非依賴嚴格指令。

當大多數框架還在糾結於如何強制 LLM 遵循特定步驟時，AgentScope 團隊選擇了一條更「放縱」的路：信任模型的推理能力。AgentScope 2.0 不再是一個單純的 Orchestrator，而是一個提供基礎設施支援（Infrastructure-as-a-Service）的平臺，讓 Agent 能在安全、隔離的環境中自由發揮。

🧩 **設計哲學：給模型空間，而非束縛**

傳統 Agent 框架往往透過嚴格的 Prompt Engineering 和固定的流程圖來約束模型行為，這在模型能力不足時是必要手段，但也限制了複雜任務的表現。

AgentScope 2.0 的核心設計理念是「Extensible Middleware System」。它提供可組合的 Hooks，讓開發者可以客製化 Agent 的 Reasoning-Acting Loop（推理-行動迴圈）。簡單來說，框架不決定模型「怎麼想」，而是提供一個穩定的執行環境，讓模型利用自身的 Reasoning 和 Tool Use 能力來解決問題。

🔒 **生產環境的關鍵：許可權與隔離**

對於企業級應用，安全性與穩定性是首要考量。AgentScope 2.0 針對此痛點引入了幾項關鍵機制：

1.  **Permission System（許可權系統）**：提供細粒度（Fine-grained）的配置，讓管理者能精確控制 Agent 可以訪問哪些工具和資源，防止惡意或誤導性的工具呼叫。
2.  **Workspace / Sandbox Support（沙箱支援）**：Agent 執行的程式碼與工具被隔離在獨立環境中。目前支援 Local、Docker、E2B 以及 OpenSandbox 作為後端，確保惡意程式碼不會影響主機環境。
3.  **Multi-tenancy & Multi-session（多租戶與多會話）**：支援生產級別的服務架構，不同租戶與會話之間完全隔離，適合高併發的商業場景。

🚀 **新功能亮點（2025-2026）**

根據 Release Notes，AgentScope 近期持續擴充生態系：

*   **記憶系統升級**：2026年6月支援 Agentic Memory，7月進一步整合 ReMe 長期記憶與 Mem0，解決 LLM 上下文限制問題。
*   **RAG 服務化**：支援分散式、多租戶、多會話的 RAG 服務，讓檢索增強生成不再只是單次查詢，而是可持續運作的系統服務。
*   **K8s 整合**：2026年7月更新支援基於 K8s 與 OpenSandbox 的工作空間，提升雲端部署的彈性。

⚠️ **限制與觀察**

目前素材未提供具體的 Benchmark 資料或與其他主流框架（如 LangChain、LlamaIndex）的直接效能對比。其優勢在於架構的靈活性與安全性設計，適合需要高度客製化邏輯與嚴格權控的生產環境，但對於追求快速原型開發的初學者，可能需要花費時間理解其 Middleware 機制。

🎯 **實務啟示**

如果你是正在建構企業級 Agent 系統的工程師，AgentScope 2.0 提供了一個值得考慮的基底：

1.  **安全優先**：利用其內建的許可權系統與沙箱機制，降低 Agent 失控風險。
2.  **信任模型**：減少過度設計的流程約束，讓模型在寬鬆的結構下發揮推理能力，可能獲得更自然的互動體驗。
3.  **擴充套件性**：其事件驅動架構（Event System）與 Human-in-the-loop 支援，便於後續整合前端介面與人工審核流程。

🔗 **來源**
- 標題：agentscope-ai/agentscope
- 作者／機構：agentscope-ai
- 連結：https://github.com/agentscope-ai/agentscope

#AgentScope #LLM #AgentFramework #ProductionReady #AI #MachineLearning #OpenSource #Sandbox #Memory #MultiTenancy
