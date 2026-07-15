---
title: agentgateway/agentgateway
source: GitHub Trending
url: https://github.com/agentgateway/agentgateway
score: 100
model: tencent/hy3:free
generated_at: '2026-07-15T08:11:27.270337'
---

📌 agentgateway：Agentic AI 完整連線方案

TL;DR：開源代理閘道，為 AI agent 通訊提供安全、可觀測與治理，跨框架即用。

🎣 當 AI agent 開始頻繁呼叫 LLM、串接工具、甚至彼此協作，你還在用拼湊的指令碼管控流量與許可權？一個基於 AI 原生協定的開源 proxy 宣稱能一次性解決連線與治理。

🤔 **Agentic AI 通訊缺乏統一治理層**
隨著 agent-to-LLM、agent-to-tool、agent-to-agent 等通訊模式在不同框架與環境中蔓延，安全性、可觀測性與治理往往得自行兜湊。agentgateway 定位為「首個完整的 Agentic AI 連線解決方案」，目標是為這些通訊提供 drop-in（即插即用）的安全、可觀測與治理能力，且聲稱適用於任何框架與環境。

🧩 **基於 MCP 與 A2A 協定的開源 Proxy**
README 指出，agentgateway 是建構在 AI-native protocols（MCP 與 A2A）之上的開源代理。其核心設計理念是以協定為中心，向上統整三類閘道功能：
- **LLM Gateway**：透過統一且 OpenAI-compatible 的 API 路由到各大 LLM 提供商（OpenAI、Anthropic、Gemini、Bedrock 等），並提供預算與花費控制、prompt 豐富化、負載平衡與故障轉移。
- **MCP Gateway**：經由 MCP 連線 LLM 與工具、外部資料源，支援 tool federation、stdio/HTTP/SSE/Streamable HTTP 傳輸、OpenAPI 整合與 OAuth 認證。
- **A2A Gateway**：使用 A2A 實現安全的 agent-to-agent 通訊，具備能力發現、模態協商與任務協作。
此外，還包含 **Inference Routing**（基於 Kubernetes Inference Gateway 擴充，依 GPU 利用率、KV cache、LoRA adapters、佇列深度決策自託管模型路由）、**Guardrails**（多層內容過濾，整合 regex、OpenAI moderation、AWS Bedrock Guardrails、Google Model Armor 與自訂 webhook）、以及 **Security & Observability**（JWT/API key/OAuth 認證、CEL 政策引擎的細粒度 RBAC、速率限制、TLS、OpenTelemetry 指標/日誌/追蹤）。

🧩 **提供 Standalone 與 Kubernetes 兩種快速部署**
專案 README 提到可透過 Standalone Quickstart 在數分鐘內開始使用，或經由 Kubernetes Quickstart 部署到 K8s 環境；摘要未提供進一步安裝指令或最小可行範例，實際整合方式需參考官方檔案。

🎯 **對工程師的實務價值**
若你正在建構多 agent 系統或需要統一管控 LLM 與工具呼叫，此專案將安全、可觀測與路由邏輯集中到一個代理層，有望降低跨框架串接的客製成本。在採用前，建議實際測試其宣稱的協定相容性與治理粒度是否符合生產需求。

🔗 **來源**
- 標題：agentgateway/agentgateway
- 作者／機構：agentgateway
- 連結：https://github.com/agentgateway/agentgateway

#AgenticAI #MCP #A2A #LLMGateway #OpenSource #Proxy #AIGovernance #Observability #Security #agentgateway
