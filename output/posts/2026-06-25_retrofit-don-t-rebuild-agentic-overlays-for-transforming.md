---
title: 'Retrofit, don’t rebuild: Agentic overlays for transforming legacy enterprise
  services'
source: AWS ML
url: https://aws.amazon.com/blogs/machine-learning/retrofit-dont-rebuild-agentic-overlays-for-transforming-legacy-enterprise-services/
score: 96
model: google/gemma-4-31b-it:free
generated_at: '2026-06-25T20:23:57.384805'
---

📌 【AWS 技術分享】不用重寫舊系統，用 Agentic Overlays 將 REST API 轉化為 AI Agent

TL;DR：透過「Agentic Overlays」薄層封裝，讓傳統 REST 服務無需重寫邏輯即可參與 A2A 自主協作。

企業內部的 REST API 與微服務雖然穩定且經過充分測試，但它們是為「客戶端-伺服器」的確定性互動而設計，完全不符合當前 AI Agent 之間需要協調、推理與結構化通訊的 A2A (Agent-to-Agent) 標準。

🤔 **REST API 與 A2A 通訊的本質衝突**

傳統的 REST 服務設計核心在於確定性 (Deterministic) 與無狀態的請求-回應流程，透過定義明確的端點與參數來執行 CRUD 操作。然而，新興的 A2A 框架要求 Agent 能透過後設資料（例如 Agent Card）互相發現並協商能力，這種自主協作的模式讓許多既有的 REST 服務被排除在 A2A 生態系之外。

🧩 **透過 Agentic Overlays 實現「舊瓶裝新酒」**

為了讓企業在不重寫業務邏輯、不重複開發程式碼且不執行平行基礎設施的前提下升級，AWS 與作者提出了一種實務方案：Agentic Overlays。

這是一種輕量級的封裝層 (Thin wrapper layers)，其核心功能如下：
- **協議轉換**：將傳統 REST 服務轉化為能參與 A2A 互動的 Agent。
- **工具化介面**：將現有的 REST API 暴露為與 Model Context Protocol (MCP) 相容的工具 (Tools)。
- **減少資源碎片化**：透過複用現有服務來降低基礎設施中的 Agent 擴散 (Agent sprawl) 問題。

💡 **對企業架構的實際影響**

這種「改造而非重建」的策略，讓企業能將穩定執行的舊有服務直接對接至自主 Agent 的協作網路中。開發者不再需要為了讓 AI Agent 呼叫某項功能而重新開發一整套微服務，而是透過 Overlay 層讓既有 API 具備被發現與協商的能力。

🎯 **實務啟示**

對於維護大量遺留系統 (Legacy systems) 的工程師來說，不要試圖將所有服務全部重構為 AI 原生架構。優先考慮建立 MCP 相容的封裝層，將穩定且成熟的 REST API 轉化為 Agent 工具，是將企業能力快速接入 A2A 生態系最經濟且風險最低的路徑。

🔗 **來源**
- 標題：Retrofit, don’t rebuild: Agentic overlays for transforming legacy enterprise services
- 作者／機構：Renuka Kumar / AWS ML
- 連結：https://aws.amazon.com/blogs/machine-learning/retrofit-dont-rebuild-agentic-overlays-for-transforming-legacy-enterprise-services/

#AWS #AI #AgenticWorkflow #RESTAPI #A2A #MCP #EnterpriseArchitecture #ModelContextProtocol #Microservices #LLM
