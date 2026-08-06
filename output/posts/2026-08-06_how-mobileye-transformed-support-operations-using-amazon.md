---
title: How Mobileye transformed support operations using Amazon Bedrock AgentCore
source: AWS ML
url: https://aws.amazon.com/blogs/machine-learning/how-mobileye-transformed-support-operations-using-amazon-bedrock-agentcore/
model: tencent/hy3:free
generated_at: '2026-08-06T08:40:02.657094'
score: 91
---

📌 【Mobileye 實戰案例】用 AI Agent 解決 66% 的例行查詢，響應時間縮短 90%

TL;DR：Mobileye 利用 Amazon Bedrock AgentCore 打造 AI 支援代理，將例行工單處理效率提升 90%。

自動駕駛先驅 Mobileye 全球已部署超過 2.3 億顆 EyeQ 晶片。隨著數據處理量激增，工程師每天需處理海量駕駛紀錄檔（drive-recording sessions），這導致了嚴重的支援瓶頸：66% 的工單只是單純的「狀態查詢」，工程師必須在多個系統間點擊 15 次以上，才能手動比對紀錄、視覺化工具與日誌。

🤔 **從手動點擊到自動化調查的轉型**

傳統的腳本（scripting）或規則型工作流（rule-based workflows）難以應對複雜的支援需求，因為它們缺乏理解變動上下文的能力。Mobileye 決定開發一個具備上下文理解能力的 AI Agent，目標是達成 95% 的分類準確率，並在 2 分鐘內完成回應。

🧩 **導入 Model Context Protocol (MCP) 實現即時調查**

Mobileye 的 AI Agent 不僅僅是分類工單，它更像是一個「智能調查員」。

- **核心架構**：使用 Anthropic Claude 模型，透過 Mobileye 內部的 LLM Gateway 進行受控存取。
- **關鍵技術：MCP**：透過 Model Context Protocol (MCP)，Agent 獲得了存取資料處理平臺 API 的權限，能即時查詢 session 狀態、檢索處理日誌並提取診斷資訊。
- **自動化流程**：
  1. 使用者提出查詢（例如：某次駕駛紀錄的處理進度）。
  2. Agent 透過 MCP 存取 API 進行資料檢索。
  3. Agent 分析檢索到的狀態、錯誤或日誌。
  4. Agent 直接回覆結果（例如：確認完成、提供錯誤原因與 Debug 建議、或引導補件流程）。

🏢 **混合雲架構：橋接地端系統與 AWS**

由於 Mobileye 的內部工單系統運行於地端（on-premises），無法直接從 AWS 存取，因此採用了混合雲架構：

- **地端組件**：處理本地工單作業，並作為連接 AWS 雲端 AI 處理能力的橋樑。
- **AWS 雲端組件**：利用 Amazon Bedrock AgentCore 提供無伺服器運算、安全性與可觀察性（observability）基礎設施。
- **內部服務**：提供數據連接與受控的模型存取權限。

📊 **從單點實驗演進為企業級平臺**

這項技術的成功讓 Mobileye 將其轉化為一個「自我服務平臺（self-service platform）」，讓公司內其他團隊也能快速部署自己的 AI Agent：

- **效能表現**：響應時間縮短 90%，且成功達到 95% 以上的準確率目標。
- **降低門檻**：Mobileye 雲端基礎設施團隊建立了一套內部託管服務，讓不具備 AWS 專業知識或憑證的開發者，也能在幾分鐘內部署出符合企業安全與成本管控標準的生產級 Agent。

🎯 **實務啟示**

對於正在規模化 AI Agent 應用的企業而言，Mobileye 的經驗顯示：解決 AI 落地難點的關鍵不在於僅僅訓練模型，而在於如何透過如 MCP 這樣的協定，讓 Agent 能夠安全地與現有的地端與雲端系統進行即時互動，並利用全託管平臺來消除基礎設施管理的負擔。

🔗 **來源**
- 標題：How Mobileye transformed support operations using Amazon Bedrock AgentCore
- 作者／機構：Adi Jabkowski @ AWS ML
- 連結：https://aws.amazon.com/blogs/machine-learning/how-mobileye-transformed-support-operations-using-amazon-bedrock-agentcore/

#AI #MachineLearning #AmazonBedrock #Mobileye #AIAgent #AWS #CloudComputing #GenerativeAI #MCP #DigitalTransformation
