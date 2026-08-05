---
title: Automated web insight extraction with Amazon Bedrock AgentCore
source: AWS ML
url: https://aws.amazon.com/blogs/machine-learning/automated-web-insight-extraction-with-amazon-bedrock-agentcore/
model: tencent/hy3:free
generated_at: '2026-08-05T08:47:41.708153'
score: 85
---

📌 【AWS 技術分享】告別手動爬蟲：利用 Amazon Bedrock AgentCore 實現自動化網頁洞察提取

TL;DR：透過 Amazon Bedrock AgentCore Browser 渲染動態網頁，結合 AI 實現自動化趨勢監測與語義搜尋。

🤔 **傳統爬蟲難以應對的挑戰**

當設計團隊需要追蹤競爭對手產品，或行銷團隊需要監控內容趨勢時，手動檢查數十個網站不僅效率低下，更令人崩潰。雖然傳統的基於規則（rule-based）的爬蟲可以實現自動化，但它們過於依賴頁面結構；一旦網站重新設計或改用 JavaScript 渲染的前端架構，爬蟲管線（pipeline）往往會無預警失效，導致團隊在發現問題前就已經丟失了關鍵資訊。

🧩 **利用 AgentCore Browser 解決動態渲染問題**

為了應對現代網頁複雜的 JavaScript 渲染需求，本方案採用了 Amazon Bedrock AgentCore 的核心能力——AgentCore Browser。

- **全託管瀏覽器服務**：不同於在 Lambda 中執行無頭瀏覽器（headless browser），AgentCore 提供全託管的遠端瀏覽器服務。
- **Playwright + CDP 整合**：透過 Playwright 並經由 Chrome DevTools Protocol (CDP) 連接，可以穩定渲染包含大量 JavaScript 的頁面，確保 AI 接收到的是完整的網頁內容，而非破碎的 HTML。
- **高韌性管線**：由於瀏覽器能處理動態元素加載，這讓後續的 AI 資訊提取步驟變得更加可靠。

📊 **事件驅動的自動化架構流程**

此解決方案採用事件驅動架構（event-driven architecture），將「內容收集」與「AI 處理」解耦，使兩者能獨立擴展：

1. **RSS 同步與去重**：由 Amazon EventBridge 定期觸發 AWS Lambda，解析 RSS Feed 並將 URL Hash 存於 Amazon S3 進行去重。
2. **瀏覽器內容擷取**：Lambda 透過 WebSocket 連接 AgentCore Browser，渲染頁面、截圖並下載圖片，最後將結構化資料（含 metadata.json）存回 Amazon S3。
3. **內容清洗與預處理**：當 S3 觸發事件後，第二個 Lambda 會從 S3 讀取 HTML。針對大型檔案（>1 MB）使用 `html-to-text` 簡化，小型檔案則使用 Mozilla 的 `Readability` 函式庫提取主體內容，以減少 Token 消耗並提升 AI 輸出一致性。
4. **AI 洞察提取**：利用 Amazon Bedrock 生成摘要、識別主題與實體、提取可執行的洞察，並產生向量嵌入（vector embeddings）。
5. **語義檢索與索引**：將結果索引至 Amazon OpenSearch Serverless，支援關鍵字與向量搜尋。這意味著即便查詢語句與原文不完全匹配（例如搜尋「新興設計趨勢」），系統仍能找出相關內容。

⚠️ **安全性與生產環境建議**

由於系統會攝取來自第三方網站的外部內容，作者建議將抓取的文本視為「不可信輸入」，並利用 **Amazon Bedrock Guardrails** 作為控制點，在不更動 Prompt 的情況下，對 AI 產出的洞察進行安全性控管。

🎯 **實務啟示：從單一工具到整合生態系**

這套架構展示了如何將多種 AWS 服務整合為一個完整的產品級解決方案：
- **開發者介面**：透過 Amazon ECS (Fargate) 部署 React 前端，並利用 Amazon Cognito 進行身份驗證。
- **程式化存取**：透過部署在 ECS 上的 **Model Context Protocol (MCP)** 伺服器，讓其他的 AI 助手或工具能透過統一介面直接查詢此洞察資料庫。

🔗 **來源**
- 標題：Automated web insight extraction with Amazon Bedrock AgentCore
- 作者／機構：Louisa Liu @ AWS ML
- 連結：https://aws.amazon.com/blogs/machine-learning/automated-web-insight-extraction-with-amazon-bedrock-agentcore/

#AWS #AmazonBedrock #AgentCore #MachineLearning #WebScraping #GenerativeAI #OpenSearch #Serverless #LLM #DataEngineering
