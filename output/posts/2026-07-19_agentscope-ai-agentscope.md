---
title: agentscope-ai/agentscope
source: GitHub Trending
url: https://github.com/agentscope-ai/agentscope
score: 96
model: tencent/hy3:free
generated_at: '2026-07-19T08:04:26.161796'
---

📌 【agentscope-ai】AgentScope 2.0：為生產環境打造的 Agent 框架

TL;DR：AgentScope 2.0 提供沙盒、多租戶與許可權系統，讓 LLM Agent 直接上線營運。

當多數 Agent 框架還在示範專案階段打轉，AgentScope 2.0 直接把「能不能進生產環境」當成核心設計目標——事件匯流、沙盒隔離、多租戶服務一次到位。

🤔 **不只是實驗室玩具，而是 production-ready 框架**

AgentScope 2.0 是一套易於使用、具備生產可用性的 agent 框架，提供基礎抽象層來配合持續提升的模型能力，並內建多項支援機制。其設計理念是順應越來越具 agentic 特性的 LLM，善用模型自身的推理與工具呼叫能力，而非用嚴格提示詞與特定編排邏輯去限制模型。

🧩 **六大核心架構特性**

README 指出 AgentScope 2.0 包含以下內建支援：

- Event System（事件系統）→ 統一的事件匯流排，可串接前端並支援 human-in-the-loop。
- Permission System（許可權系統）→ 針對工具與資源提供細粒度、可設定的存取控制。
- Multi-tenancy & Multi-session Service（多租戶與多會話服務）→ 具備生產等級的服務隔離能力，區分不同租戶與會話。
- Workspace / Sandbox Support（工作區與沙盒支援）→ 在隔離環境中執行工具與程式碼，內建本地、Docker、E2B、OpenSandbox、Daytona 等後端。
- Extensible Middleware System（可擴充中介層系統）→ 透過可組合的 hooks 自訂並延伸 agent 的推理—行動迴圈。
- 設計取向 → 框架明確表示為「越來越具 agentic 的 LLM」而設計，不約束模型能力。

📊 **2026 年上半年的功能演進**

從專案新聞與檔案紀錄來看，AgentScope 2.0 在釋出後陸續擴充能力：

- 2026-05：AgentScope 2.0 正式釋出。
- 2026-06：陸續加入 Agent Team、RAG、分散式與多租戶多會話 RAG 服務、Agentic Memory，並整合 Mem0。
- 2026-07：支援 ReMe 長期記憶；工作區／沙盒擴充 K8s 與 OpenSandbox 後端，以及 Daytona 基礎的沙盒支援。

🎯 **實務啟示**

對打算把 LLM Agent 從 PoC 推上線的團隊，AgentScope 2.0 把多租戶隔離、沙盒執行與許可權管控列為內建特性，減少自行搭建基礎設施的負擔。若你的場景需要讓不同客戶共用同一套服務又要彼此隔離，或要在受控環境跑工具與程式碼，這套框架的抽象設計值得評估匯入。

🔗 **來源**
- 標題：agentscope-ai/agentscope
- 作者／機構：agentscope-ai
- 連結：https://github.com/agentscope-ai/agentscope

#AgentScope #AgentFramework #LLM #MultiTenancy #Sandbox #RAG #AgenticMemory #ProductionReady #Middleware #HumanInTheLoop
