---
title: "czlonkowski/n8n-mcp"
source: GitHub Trending
url: https://github.com/czlonkowski/n8n-mcp
score: 103
model: tencent/hy3-preview:free
generated_at: 2026-05-15T20:44:53.112808
---

📌 **n8n-MCP: AI×Workflow**

你有沒有想過，讓 Claude 直接幫你找 n8n 節點、寫工作流？這個新開源專案把 1,650 個節點的文件、屬性與操作全餵給 AI 助手。

🤔 **工作流自動化遇上 AI 需要一座橋樑**

n8n 作為熱門的低程式工作流平台，擁有超過 1,600 個內建與社群節點。但對 AI 模型而言，要正確理解每個節點的參數與可用操作並不直觀，這限制了 AI 輔助編排工作流的可能性。

🧪 **MCP 伺服器結構化節點知識**

n8n-MCP 實作了一個 Model Context Protocol (MCP) 伺服器，以 TypeScript 開發，提供以下結構化資料：  
- 1,650 個 n8n 節點（820 核心 + 830 社群，其中 741 已驗證）  
- 節點屬性：99% 覆蓋，含詳細 JSON Schema  
- 節點操作：63.6% 可用動作的文件  
- 官方文件覆蓋率 87%（包含 AI 相關節點）  
- 偵測到 265 種具 AI 能力的工具變體，並附完整說明  
- 從熱門範本萃取的 156 個排名配置作為真實案例  
- 2,352 個工作流範本庫，AI 中繼資料覆蓋率 99.96%  
- 社群節點搜尋，可依來源過濾  

💡 **為何這個橋樑對開發者有意義**

透過 MCP 標準，AI 助手（如 Claude、GPT‑4 等）可即時查詢節點的必填欄位、可選參數與可執行操作，從而在對話中產出符合 n8n 規格的工作流 JSON，或直接針對特定任務推薦節點組合。這降低了開發者查文件的成本，也讓 AI 能更精準地參與工作流設計與除錯。

⚠️ **專案目前的限制**

- 節點操作的覆蓋度仍為 63.6%，約三分之一的動作尚未有完整說明。  
- 文件覆蓋率 87%，表示仍有 13% 的官方說明未被納入。  
- 專案維護者指出，這是個人工專案，贊助才能持續跟上 n8n 的最新版本與社群節點更新。  
- 安全提醒：切勿在生產環境中直接編輯敏感憑證（原文警示：NEVER edit your production …）。

🎯 **實務啟示**

- 若你正在構建 AI 輔助的自動化平台，可考慮採用或參考此 MCP 伺服器作為節點知識庫。  
- 對於 n8n 使用者，將此伺服器部署後，可讓 AI 助手在聊天視窗中快速產出或驗證工作流，提升開發效率。  
- 專案歡迎贊助與 issue 回報，以維持文件與節點庫的同步更新。

🔗 **專案連結**
📂 czlonkowski/n8n-mcp  
👤 作者：czlonkowski  
🔗 https://github.com/czlonkowski/n8n-mcp  
⭐ 當天獲得 68 顆星（依據 GitHub Trending 觀測）

你會嘗試讓 AI 直接幫你寫 n8n 工作流嗎？歡迎在留言區分享你的想法 👇

#n8n #MCP #AIAssistant #WorkflowAutomation #OpenSource #TypeScript
