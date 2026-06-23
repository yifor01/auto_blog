---
title: 'Shared infrastructure, isolated tenants: Pool model multi-tenancy with Amazon
  Bedrock AgentCore'
source: AWS ML
url: https://aws.amazon.com/blogs/machine-learning/shared-infrastructure-isolated-tenants-pool-model-multi-tenancy-with-amazon-bedrock-agentcore/
score: 87
model: google/gemma-4-31b-it:free
generated_at: '2026-06-23T20:31:38.472150'
---

📌 【AWS 技術分享】用 Amazon Bedrock AgentCore 打造隔離且可擴充套件的多租戶 AI 應用

TL;DR：透過 Tier → Tenant → User 三層架構，在共用基礎設施上實現租戶間的資料隔離與成本追蹤。

在開發 SaaS AI 應用時，工程師面臨的最大挑戰在於：如何在共用基礎設施的同時，確保不同客戶（租戶）之間的資料完全隔離？如果缺乏嚴格的隔離機制，不僅會面臨資料外洩的風險，還可能導致服務品質不均或成本失控。

🤔 **多租戶 AI 應用的核心挑戰**

在生產環境中，多租戶系統必須解決以下四個關鍵問題：
- **租戶隔離**：確保客戶 A 絕對無法存取客戶 B 的資料。
- **分級服務**：針對不同服務層級（如 Basic 與 Premium）提供不同的功能與服務品質。
- **精細化成本追蹤**：能準確計算每個租戶產生的費用。
- **租戶級別的可觀測性**：針對單一租戶進行效能監控與除錯。

🧩 **三層階層式隔離架構**

Amazon Bedrock AgentCore 提供了一套實作模式，透過建立「Tier → Tenant → User」的三層階層結構，在每個層級強制執行隔離：

1. **Tier (服務分級)**：將租戶依需求、使用模式或定價方案分組（例如：基礎版與進階版），定義該層級可使用的功能集與服務品質。
2. **Tenant (租戶)**：實現核心隔離層，確保租戶間的獨立性。
3. **User (使用者)**：在租戶內部進一步細分使用者許可權。

這種隔離機制會貫穿以下技術元件：
- **知識庫檔案 (Knowledge Base)**：確保檢索範圍僅限於該租戶的文件。
- **記憶體 (Memory)**：對話上下文與記憶紀錄的租戶級別隔離。
- **模型存取 (Model Access)**：根據層級控制可呼叫的模型能力。
- **成本追蹤 (Cost Tracking)**：將資源消耗精確對應到特定租戶。

💡 **從醫療 AI 實作看通用設計模式**

雖然此方案以服務多間診所與醫院的醫療 AI Agent 為範例，但其架構模式具有高度通用性。無論是開發 SaaS 平臺、服務多個事業單位的企業解決方案，或是針對不同組織的管理服務，都能套用這套「共用基礎設施、隔離租戶 (Pool model multi-tenancy)」的設計。

🎯 **實務啟示**

對於構建 AI SaaS 的工程師而言，不要試圖在應用層用簡單的 if/else 來區分租戶，而應在基礎架構層級（如知識庫與記憶體存取）就建立階層式隔離。透過定義 Tier 策略，可以更靈活地管理不同付費等級的功能差異，同時降低維運複雜度。

🔗 **來源**
- 標題：Shared infrastructure, isolated tenants: Pool model multi-tenancy with Amazon Bedrock AgentCore
- 作者／機構：Ashley Chen @ AWS ML
- 連結：https://aws.amazon.com/blogs/machine-learning/shared-infrastructure-isolated-tenants-pool-model-multi-tenancy-with-amazon-bedrock-agentcore/

#AWS #AmazonBedrock #AgentCore #MultiTenancy #SaaS #AIArchitecture #TenantIsolation #CloudComputing #GenAI #SoftwareArchitecture
