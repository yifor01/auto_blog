---
title: Building an agentic AI solution at Bluesight with Amazon Bedrock
source: AWS ML
url: https://aws.amazon.com/blogs/machine-learning/building-an-agentic-ai-solution-at-bluesight-with-amazon-bedrock/
score: 92
model: tencent/hy3:free
generated_at: '2026-07-14T08:01:07.167414'
---

這是一篇針對「產業新聞／部落格報導」型別的技術文章。

📌 【Bluesight 案例】利用 Amazon Bedrock 打造 Agentic AI，破解醫院合規資料的複雜挑戰

TL;DR：Bluesight 利用 Amazon Bedrock 打造 Prism 解決方案，實現跨產品線的 Agentic AI，解決醫院每年耗時 4,000 小時的合規審核問題。

🎣 **當合規審核變成資料大海撈針**

在醫療產業中，合規工作往往難以規模化。以管理 340B 藥價計畫（340B Drug Pricing Program）的醫院為例，要證明某筆採購符合豁免條件，必須同時比對多個來源：包括 FDA 短缺清單、ASHP 資料、庫存天數、基於機器學習的短缺預測，以及來自數百家醫院的缺貨訊號。對於單一機構而言，這項手動審核流程每年消耗超過 4,000 小時，規模化後的挑戰極其巨大。

🧩 **從單一產品原型演進至統一的 Agentic AI 解決方案**

Bluesight 擁有一系列專門解決醫療合規問題的產品（如 KitCheck、ControlCheck 等），但客戶需要的是一個能跨越產品邊界、同時對多個系統進行推理並提供洞察的 AI 層。

為了達成此目標，Bluesight 透過兩次 AWS 合作與 Amazon Bedrock AgentCore 技術，將技術架構從單一產品的 AI 原型，演進為名為 **Prism** 的統一 Agentic AI 解決方案。

📊 **Prism 的發展程序與影響**

- **初步嘗試**：最初的 AI 應用切入點是藥物流失（drug diversion）檢測。
- **產品落地**：專為 ControlCheck 開發的 Prism Assistant 已於 2026 年 5 月推出，目前已有 20 個醫療系統正在使用。
- **未來展望**：更複雜的跨產品線 Agentic AI 解決方案預計於 2026 年底推出。

🎯 **實務啟示**

對於需要處理跨系統、多來源資料的企業而言，從單一功能的 AI 助手（Assistant）轉向具備推理能力的 Agentic AI（代理式 AI），是解決複雜業務流程自動化（如跨產品線資料整合）的關鍵路徑。

🔗 **來源**
- 標題：Building an agentic AI solution at Bluesight with Amazon Bedrock
- 作者／機構：Vijay Venkatesh @ AWS ML
- 連結：https://aws.amazon.com/blogs/machine-learning/building-an-agentic-ai-solution-at-bluesight-with-amazon-bedrock/

#AI #AgenticAI #AmazonBedrock #AWS #HealthcareIT #Compliance #MachineLearning #DigitalTransformation #HealthTech #DataIntegration
