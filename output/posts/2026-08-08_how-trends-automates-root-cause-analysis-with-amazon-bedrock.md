---
title: How TReNDS automates root-cause analysis with Amazon Bedrock
source: AWS ML
url: https://aws.amazon.com/blogs/machine-learning/how-trends-automates-root-cause-analysis-with-amazon-bedrock/
model: tencent/hy3:free
generated_at: '2026-08-08T06:45:02.087481'
score: 96
---

📌 【AWS 實作案例】利用 Amazon Bedrock 打造自動化根因分析，告別手動追蹤 Log 的繁瑣流程

TL;DR：TReNDS 利用 Amazon Bedrock 與 Strands Agents SDK，實現自動化錯誤調查與程式碼比對。

當系統發生錯誤時，「知道出錯了」與「知道為什麼出錯」是兩回事。對於維運團隊來說，最耗時的往往不是接收警報，而是打開 CloudWatch Logs、閱讀 Stack Trace、在 GitHub 找對應的原始碼，並在腦中模擬執行路徑。對於簡單錯誤，這可能耗費 15 至 30 分鐘；若是跨服務的複雜問題，時間更是難以估計。

🤔 **從「被動監控」進化到「主動調查」**

TReNDS 中心（位於佐治亞州立大學、喬治亞理工學院與艾莫里大學的聯合研究中心）面臨著隨著應用程式規模擴大，錯誤調查壓力也隨之增加的挑戰。他們發現，基礎模型（Foundation Model, FM）不僅能摘要錯誤訊息，更能像工程師一樣，透過檢索上下文與原始碼，進行結構化的根因分析。

🧩 **Agentic Workflow：讓 AI 決定調查路徑**

TReNDS 建立了一套自動化架構，核心在於不再使用死板的預設規則（Rule-based），而是採用 Agent（代理）模式。

其技術架構流程如下：
1. **偵測階段**：應用程式在 Amazon EKS 執行，透過 FluentBit 將 Log 送往 Amazon CloudWatch。
2. **觸發階段**：CloudWatch 使用訂閱篩選器（Subscription Filters）監控 ERROR、Exception、FATAL 或 CRITICAL 等關鍵字，一旦匹配即觸發 AWS Lambda。
3. **調查階段**：Lambda 啟動由 Amazon Bedrock 驅動的 Strands Agent。
4. **整合階段**：Agent 根據錯誤訊息，自主決定需要調用的工具（Tools），例如從 GitHub 抓取原始碼或從同一個 Log Stream 抓取前後文。
5. **交付階段**：分析結果透過 Amazon SNS 發送給團隊。

💡 **關鍵技術：Strands Agents SDK 與工具調用**

這套系統之所以強大，是因為 Agent 具備了「閱讀程式碼」的能力。透過 Strands Agents SDK，工程師只需使用 `@tool` 裝飾器定義 Python 函式，並提供清楚的 Docstring（文件字串）與型別提示（Type hints），模型就能理解工具的用途並決定何時調用。

* **原始碼檢索（Source Code Retrieval）**：這是最關鍵的工具。Agent 能根據 Stack Trace 中的檔案路徑與行號，直接讀取 GitHub 上的原始碼，從而追蹤執行路徑，而不僅僅是進行字串比對。
* **上下文補完（Context Enrichment）**：Agent 會根據 Log Stream 抓取該容器在出錯前後的完整 Log 序列，確保分析時擁有完整的請求上下文與警告資訊。

⚠️ **合規性與資料安全**

由於 TReNDS 處理的是醫療研究相關數據，資料隱私至關重要（可能涉及 HIPAA 規範）。這套架構的優點在於，所有處理流程都在 AWS 帳戶內完成，Log 與原始碼都在既有的安全邊界內流動，不需要將敏感資料傳送到外部的 API 端點。

🎯 **實務啟示**

對於處理大規模微服務架構的工程團隊，這套模式具備高度參考價值：
- **從摘要轉向推理**：不要只讓 AI 幫你總結錯誤，要給予它存取原始碼與上下文的權限，讓它進行「推理」。
- **靈活性優於規則**：使用 Agent 架構可以避免寫下無止盡的 `if-else` 判斷邏輯，讓模型根據錯誤類型自行決定調查策略。
- **工具化（Tool-use）是核心**：AI 的能力上限取決於你提供的工具（如：GitHub API、Log 檢索工具）有多強大。

🔗 **來源**
- 標題：How TReNDS automates root-cause analysis with Amazon Bedrock
- 作者／機構：Vitaly Omelchenko @ TReNDS Center
- 連結：https://aws.amazon.com/blogs/machine-learning/how-trends-automates-root-cause-analysis-with-amazon-bedrock/

#AI #MachineLearning #AWS #AmazonBedrock #DevOps #RootCauseAnalysis #LLM #GenerativeAI #SRE #CloudComputing
