---
title: "Mend Releases AI Security Governance Framework: Covering Asset Inventory, Risk Tiering, AI Supply Chain Security, and Maturity Model"
source: MarkTechPost
url: https://www.marktechpost.com/2026/04/23/mend-releases-ai-security-governance-framework/
score: 68
model: tencent/hy3-preview:free
generated_at: 2026-04-25T19:29:43.723699
---

📌 【Mend 新框架】告別影子 AI，落實安全治理

當開發者用 GitHub Copilot 加速交付，當產品團隊悄悄在分支中嵌入第三方模型，安全團隊往往是最後一個知道的。這種「部署速度」與「治理速度」之間的巨大鴻溝，正是當前企業 AI 應用中最危險的死角。

🤔 **AI 資產看不見，風險治理就免談**

根據 Mend 最新發布的實務指南，大多數組織現在面臨的問題不是「要不要導入 AI」，而是「不知道組織內部到底有多少 AI 在跑」。這種未被官方核准或記錄的「影子 AI」（Shadow AI），正處理著真實數據、觸碰著真實系統。框架的核心前提非常直白：你無法治理你看不見的東西。

🧪 **從 Copilot 到自主 Agent 的全面資產盤點**

Mend 的框架擴大了「AI 資產」的定義，不再只局限於內部訓練的模型。它涵蓋了：
- AI 開發工具（如 Copilot, Codeium）
- 第三方 API（如 OpenAI, Google Gemini）
- 開源模型與 SaaS 內嵌功能（如 Notion AI）
- 內部模型與自主 AI Agent

為了讓盤點可行，框架強調發現這些工具必須是一個「非懲罰性」的過程，確保開發者敢於揭露，而非隱瞞。

 **1 到 3 級風險分級，拒絕一刀切**

這套框架最實用的地方在於「風險分級系統」。它不再將所有 AI 視為同等危險，而是根據五個維度進行評分：
1. 數據敏感度 (Data Sensitivity)
2. 決策權限 (Decision Authority)
3. 系統存取權 (System Access)
4. 外部暴露程度 (External Exposure)
5. 供應鏈來源 (Supply Chain Origin)

每個資產在這五個維度上被評為 1 到 3 分，總分決定了該資產所需的治理強度。這讓安全團隊能將資源集中在高風險區域，而不是被低風險工具淹沒。

💡 **從 AppSec Lead 視角出發的實戰手冊**

不同於學術論文，這份指南是寫給正在摸索起點的 AppSec Lead、工程經理和數據科學家。它不假設你已經有一套成熟的 AI 安全計畫，而是直接提供從零開始的劇本。對於那些苦於 AI 治理不知從何下手的團隊，這提供了一個清晰的結構化起點。

⚠️ **框架性質重於技術突破，落地細節待觀察**

必須指出的是，這是一份治理框架而非技術白皮書。它沒有提出新的模型架構或演算法，其新穎性相對有限。此外，框架的實際效用高度依賴於組織內部的執行力與工具整合能力，目前尚缺乏大規模的實證數據來驗證其長期效果。

🎯 **給工程主管的建議：先求有，再求好**

- 立即啟動「非懲罰性」的 AI 資產盤點，建立可視性。
- 導入風險分級機制，針對高決策權限與高敏感數據的 AI 資產重點監控。
- 將 AI 供應鏈安全納入現有的第三方風險管理流程中。

🔗 **參考資訊**
📝 AI Security Governance: A Practical Framework for Security and Development Teams
🏢 Mend (via MarkTechPost)
✍️ Asif Razzaq
🔗 詳細內容：https://www.marktechpost.com/2026/04/23/mend-releases-ai-security-governance-framework/

你的團隊目前是如何管理內部的 AI 工具使用？是靠政策規範，還是有自動化的資產盤點機制？歡迎分享你的經驗 👇

#AI安全 #AppSec #資訊安全 #AI治理 #Mend #影子AI #軟體工程 #技術管理
