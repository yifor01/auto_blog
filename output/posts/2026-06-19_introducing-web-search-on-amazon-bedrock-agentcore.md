---
title: Introducing Web Search on Amazon Bedrock AgentCore
source: AWS ML
url: https://aws.amazon.com/blogs/machine-learning/introducing-web-search-on-amazon-bedrock-agentcore/
score: 103
model: google/gemma-4-31b-it:free
generated_at: '2026-06-19T20:02:59.452905'
---

📌 【AWS 最新發佈】Bedrock AgentCore 推出 Web Search，解決 AI Agent 知識過時問題

TL;DR：Bedrock AgentCore 推出的全託管 Web Search，讓 Agent 能透過 MCP 協議即時獲取網路資訊而無需自行維護搜尋 API。

AI Agent 雖然強大，但有個結構性缺陷：知識在訓練完成那一刻就「凍結」了。如果你問它今天的股價或一小時前剛發佈的新聞，僅依賴訓練數據的 Agent 將無法回答。

🤔 **擺脫「知識凍結」與繁瑣的基礎設施維護**

許多團隊嘗試為 Agent 加入網路搜尋功能，但自行構建通常意味著必須處理搜尋 API 的配置、管理對外認證，以及編寫繁瑣的結果解析（result-parsing）程式碼。

Amazon Bedrock AgentCore 推出 Web Search 功能，將這些複雜度全部封裝在一個全託管的連接器中，讓工程師能快速將 Agent 與即時網路資訊接軌。

🧩 **基於 MCP 協議的即插即用設計**

這項功能的技術核心在於其高度的整合性與標準化：

- **MCP 兼容性**：採用 Model Context Protocol (MCP) 協議，Agent 透過標準的 `tools/list` 呼叫即可發現搜尋工具，並像呼叫其他 MCP 工具一樣執行。
- **全託管索引**：後端由 Amazon 維護一個包含數百億份文件的專屬網頁索引，且內容在數分鐘內即會更新，確保資訊時效性。
- **簡化流程**：開發者不需要配置搜尋 API 或管理對外憑證，直接透過 AgentCore Gateway 連接即可使用。
- **混合檢索機制**：檢索過程可結合知識圖譜（knowledge graph）與針對模型上下文優化的語義片段提取（semantic snippet extraction）。

🛡️ **數據流向與隱私保障**

根據官方描述，該功能的隱私模型確保查詢過程不會離開 AWS 環境。應用程式透過 AgentCore Gateway（支援 IAM 或 JWT 認證）發送請求，流量經由託管連接器路由至 AWS 服務帳戶中的 Web Search 工具，全程維持在 AWS 內部。

🎯 **實務啟示**

對於開發 AI Agent 的工程師來說，這意味著可以將開發重心從「維護搜尋管線」轉移到「優化 Agent 行為」。如果你需要 Agent 處理即時數據（如金融行情、最新技術發佈），使用這種 MCP 兼容的託管工具能大幅減少基礎設施的維運成本（infrastructure overhead）。

🔗 **來源**
- 標題：Introducing Web Search on Amazon Bedrock AgentCore
- 作者／機構：Veda Raman @ AWS ML
- 連結：https://aws.amazon.com/blogs/machine-learning/introducing-web-search-on-amazon-bedrock-agentcore/

#AWS #AmazonBedrock #AIAgents #MCP #WebSearch #CloudComputing #LLM #RealTimeData #AgentCore #MachineLearning
