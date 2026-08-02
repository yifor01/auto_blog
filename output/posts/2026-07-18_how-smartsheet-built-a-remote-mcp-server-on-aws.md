---
title: How Smartsheet built a remote MCP server on AWS
source: AWS ML
url: https://aws.amazon.com/blogs/machine-learning/how-smartsheet-built-a-remote-mcp-server-on-aws/
score: 81
model: tencent/hy3:free
generated_at: '2026-07-18T07:39:05.511619'
---

📌 【AWS ML 案例】Smartsheet 在 AWS 上打造遠端 MCP 伺服器

TL;DR：Smartsheet 用 AWS 架設遠端 MCP 伺服器，讓 AI 代理直接操作企業資料並省下大量 tokens。

企業團隊越來越依賴 AI agents 來處理日常工作，但多數既有的企業系統並不是為了讓 AI 直接存取資料而設計的。Smartsheet 作為數十萬組織使用的企業工作管理平臺，選擇自己補上這塊拼圖。

🤔 **企業 AI 代理缺的不是模型，而是結構化存取通道**

Smartsheet 指出，隨著企業採用 AI agents，這些代理需要結構化地存取像 Smartsheet 內部的資料，但大多數系統本身並未為此設計。為了橋接這個落差，他們在 AWS 上建了一個遠端 Model Context Protocol (MCP) 伺服器，讓 AI 客戶端能直接存取其資料與能力。

🧩 **同一套 MCP 層，內外部代理共用**

這個遠端 MCP 伺服器連線 Smartsheet 既有的 API 與中央智慧層（central intelligence layer），並在其上疊加一個為 AI 最佳化的介面。README 式的說明指出，該介面旨在降低 token 成本、減少 hallucination（幻覺），並協助 LLM 可靠地處理企業資料。

值得注意的是，Smartsheet 自身的 Smart Assist（產品內的 AI 體驗）與外部連線的 AI 客戶端（如 Amazon Quick、Claude Desktop）都跑在同一套基礎設施上，使用相同的工具、最佳化與智慧堆疊。這種「內外代理 parity（對等）」是刻意的架構選擇，而非偶然。

📊 **最佳化介面替內部遙測省下超過 30 億 tokens**

根據 Smartsheet 內部遙測資料，自從上線以來，透過這些 AI 最佳化措施，他們累計節省了超過 30 億個 tokens。文章涵蓋的架構高層檢視聚焦在 AWS 基礎設施，包含安全性、治理、擴展與部署，以及建在 AWS 上的 AI 專屬最佳化。

💡 **AI 助理與自主代理的兩種用法**

透過 Amazon Quick 與 Claude Desktop 這類 AI 助手，使用者可用自然語言與 Smartsheet 互動，例如分析專案資料、更新任務、建立表格、管理工作區等。另一方面，企業也在建置不需人工提示就能執行的自訂 AI agents，這些代理可在同人類使用的表格中自主運作，像是擷取需求、認領任務、附加測試結果、草擬檔案，將原本數週的工作流程壓縮到數天甚至數小時。

🎯 **對工程師的實務啟示**

若你所在的團隊正規劃讓 AI agents 接觸企業內部系統，Smartsheet 的做法提供一個可參考的骨架：不要為每個客戶端各寫一套整合，而是用一個遠端 MCP 伺服器統一對接既有 API，並在上面加一層為 LLM 設計的介面來控管成本與穩定性。內外代理共用同一基礎設施，也能降低長期維運複雜度。

🔗 **來源**
- 標題：How Smartsheet built a remote MCP server on AWS
- 作者／機構：Vasil Kosturski @ AWS ML
- 連結：https://aws.amazon.com/blogs/machine-learning/how-smartsheet-built-a-remote-mcp-server-on-aws/

#MCP #AWS #Smartsheet #AIAgents #EnterpriseAI #LLM #RemoteServer #TokenOptimization #ClaudeDesktop #AmazonQuick
