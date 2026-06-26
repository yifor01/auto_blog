---
title: Deploy a Production-Ready NVIDIA AI-Q Blueprint on Oracle Cloud Infrastructure
source: NVIDIA Developer
url: https://developer.nvidia.com/blog/deploy-a-production-ready-nvidia-ai-q-blueprint-on-oracle-cloud-infrastructure/
score: 87
model: google/gemma-4-31b-it:free
generated_at: '2026-06-26T20:08:33.529264'
---

📌 【NVIDIA】將 AI-Q Blueprint 部署至 OCI，打造生產等級的長程 AI Agent

TL;DR：利用 Terraform 與 Helm 在 Oracle Cloud Infrastructure (OCI) 上部署 NVIDIA AI-Q，實現具備規劃與多代理協作能力的 AI 系統。

從只能單次回答問題，到能維持對話上下文，AI Agent 的演進速度極快。現在我們進入了「長程 Agent (Long-horizon agents)」的時代：系統不再只是聊天，而是能規劃多個步驟、將工作分配給子代理、在長任務中維持上下文，並在安全沙箱中執行工具。

🧩 **AI-Q Blueprint：基於多代理架構的開源參考設計**

NVIDIA AI-Q Blueprint 是一個開源的參考實作，旨在實現上述的長程 Agent 功能。它能根據需求提供快速且有引用的回答，或撰寫附有來源的深度研究報告。

該系統的核心技術棧包含：
- **基礎框架**：基於 LangChain Deep Agents 與 NVIDIA NeMo Agent Toolkit 構建。
- **多代理架構**：內部包含 Intent Router (意圖路由)、Shallow Research Agent (淺層研究代理)、Deep Agent (深層代理)、Planning Sub-agent (規劃子代理) 以及 Researcher Sub-agent (研究子代理)。

🚀 **在 OCI 上的部署路徑與技術實作**

對於希望將 AI-Q 從個人筆電遷移至雲端環境的開發者與平臺工程師，該指南提供了在 Oracle Cloud Infrastructure (OCI) 上的完整部署流程：

1. **基礎設施自動化**：使用 Terraform 建立所需的 OCI 雲端資源。
2. **工作負載部署**：使用 Helm 將 AI-Q 部署至 OKE (Oracle Container Engine for Kubernetes)。
3. **快速管理**：部署完成後即可獲得運作中的 AI-Q 終端節點，且僅需單一指令即可將所有資源移除。

⚠️ **部署前的必要準備**

在開始部署前，工程師需確保 OCI 租戶 (Tenancy) 具有適當的許可權與以下服務限額 (Service Limits)：
- **OKE**：一個增強型叢集 (Enhanced Cluster) 與一個節點池 (Node Pool)。
- **Block Volume**：至少 10 GB（由 OKE CSI 驅動程式為叢集內 PostgreSQL 動態配置）。
- **Load Balancer**：一個彈性負載平衡器。
- **Vault**：一個金庫 (Vault) 與對應的機密管理 (Secrets)。
- **API 金鑰**：需從 build.nvidia.com 獲取 NGC API key。

🎯 **實務啟示**

對於需要建構複雜 AI 工作流的團隊，AI-Q 的設計模式提供了一個可參考的範本：將任務由「意圖路由」分發至不同層級的代理（淺層 vs 深層），並透過子代理進行規劃與研究。這種模組化架構能有效處理需要長時間思考與多步驟執行的複雜任務，而非單純依賴單一 LLM 的一次性生成。

🔗 **來源**
- 標題：Deploy a Production-Ready NVIDIA AI-Q Blueprint on Oracle Cloud Infrastructure
- 作者／機構：Anurag Kuppala, Sanjay Basu and Felipe Garcia @ NVIDIA Developer
- 連結：https://developer.nvidia.com/blog/deploy-a-production-ready-nvidia-ai-q-blueprint-on-oracle-cloud-infrastructure/

#NVIDIA #OCI #AI #AIAgents #LangChain #NeMo #Kubernetes #Terraform #Helm #MultiAgentSystem
