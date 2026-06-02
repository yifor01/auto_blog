---
title: "agentgateway/agentgateway"
source: GitHub Trending
url: https://github.com/agentgateway/agentgateway
score: 87
model: tencent/hy3-preview:free
generated_at: 2026-06-02T22:09:57.152781
---

📌 **【AgentGateway】統一代理解決方案**  

你以為只要把模型串起來就能建立多代理系統？實際上，安全、觀測與治理才是最大的瓶頸。  
Agentgateway 宣稱用一個開源代理搞定所有這些問題。  

🤔 **多代理系統的連接痛點**  
當開發者想要讓不同的 LLM、工具與其他代理互相溝通時，常需要自行處理協議轉換、身份驗證、流量控制以及日誌追蹤。這些零散的實作不僅增加開發負擔，也難以確保跨框架的一致性與合規性。  

🧪 **開源代理的核心架構**  
Agentgateway 是一個基於 AI-native 協議（MCP 與 A2A）建置的開源 proxy。它提供三個主要閘道：  
- **LLM Gateway**：透過統一的 OpenAI‑compatible API 路由至 OpenAI、Anthropic、Gemini、Bedrock 等供應商，內建預算控制、提示富化、負載平衡與容錯切換。  
- **MCP Gateway**：以 Model‑Context‑Protocol 連接 LLM 與外部工具或資料來源，支援 stdio、HTTP、SSE、Streamable HTTP 傳輸，並可整合 OpenAPI 以及進行 OAuth 認證。  
- **A2A Gateway**：利用 Agent‑to‑Agent 協議實現安全的代理間通訊，包含能力發現、模態協商與任務協作。  

此外，Agentgateway 還具備 **Inference Routing**（基於 Kubernetes Inference Gateway 的智慧路由，依據 GPU 使用率、KV 快取、LoRA 適配器與佇列深度決策）、**Guardrails**（多層內容過濾，結合 regex、OpenAI moderation、AWS Bedrock Guardrails、Google Model Armor 與自訂 webhook）以及 **Security & Observability**（JWT、API key、OAuth 認證、以 CEL 為基礎的細粒度 RBAC、速率限制、TLS 與 OpenTelemetry 的指標、日誌與追蹤）。  

💡 **快速上手與部署方式**  
專案提供兩種快速開始路徑：  
- **Standalone Quickstart**：幾分鐘內即可在本機啟動代理。  
- **Kubernetes Quickstart**：透過提供的 manifests 直接在 K8s 叢集上部署。  

⚠️ **目前已知的限制**  
- 專案剛釋出，社群與生態系統仍在早期階段。  
- 文件與範例主要聚焦於基本功能，進階自訂或特殊環境的適配度尚需社群回饋驗證。  
- 由於未附帶正式基準測試，實際效能在高流量或特殊硬體上的表現仍需實際評估。  

🎯 **對工程師的實務建議**  
- 若正在構建需要多種 LLM、工具或代理互通的系統，可先嘗試使用其統一 API 降低接口複雜度。  
- 利用內建的 Observability 功能，快速取得流量與安全狀態，減少自行搭建監控管道的成本。  
- 在生產環境前，建議先在 staging 環境驗證 Guardrails 與 Routing 政策是否符合業務需求。  

🔗 **專案連結**  
📦 Agentgateway：https://github.com/agentgateway/agentgateway  
📺 介紹影片（由專案頁面提供）  

你是否正在評估如何讓自己的 Agentic AI 系統更安全、易於觀測？歡迎在留言區分享你的看法或使用經驗 👇  

#AgentGateway #MCP #A2A #LLMGateway #AIInfrastructure #OpenSource #DevOps #Kubernetes #AIagents #GitHubTrending
