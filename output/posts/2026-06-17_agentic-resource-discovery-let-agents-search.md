---
title: 'Agentic Resource Discovery: Let agents search'
source: HuggingFace Blog
url: https://huggingface.co/blog/agentic-resource-discovery-launch
score: 103
model: google/gemma-4-31b-it:free
generated_at: '2026-06-17T20:31:57.766733'
---

📌 【Hugging Face 最新發布】不再硬編碼工具：Agentic Resource Discovery (ARD) 讓 AI Agent 學會「自主搜尋」

如果你現在開發 AI Agent，大概對 MCP (Model Context Protocol)、Skills 或 A2A (Agent-to-Agent) 這些協議並不陌生。但你有沒有發現一個共同的痛點：無論是呼叫工具還是對接其他 Agent，目前都預設「使用者或開發者已經知道要用什麼」。

這意味著你必須事先將工具的 URL 硬編碼在設定檔中，或手動安裝插件。但當工具數量從 5 個增加到 5,000 個時，這種「先安裝、後使用」的模式就徹底失效了。

🤔 **「先安裝，後使用」的擴展瓶頸**

目前的 Agent 能力配置模式存在明顯的規模化問題。開發者通常採取兩種做法：一種是將 MCP 伺服器 URL 直接寫死在 config 檔；另一種則是將所有可用工具的描述全部塞進 LLM 的 Context Window 讓模型自己挑。

前者缺乏靈活性，而後者則受限於 Context Budget（上下文視窗限制）。即便使用搜尋策略，但由於工具描述通常過於簡略，模型往往難以在大量相似功能中做出精確區分。

🧪 **ARD 規範：在 LLM 外部建立「發現層」**

為了打破這個瓶頸，由 Microsoft、Google、GoDaddy、Hugging Face 等產業領導者共同開發，提出了一套開放的草案規範：Agentic Resource Discovery (ARD)。

ARD 的核心理念是將「資源選擇」的過程移到 LLM 之外。它定義了一套標準，讓 Agent 與工具可以在聯邦式註冊表 (Federated Registries) 中被編目、索引並搜尋。

這意味著 Agent 不再需要預先安裝所有能力，而是在執行時 (Runtime) 根據需求，動態地發現並獲取所需的工具、技能或其他 Agent。

💡 **從「靜態配置」轉向「動態發現」**

ARD 的關鍵在於它不是一個特定的產品或商城，而是一個**共享的標準 (Shared Standard)**。

- **非中心化**：任何公司都可以獨立實現此標準。
- **互操作性**：任何符合標準的 Agent 或工具都能參與其中。
- **降低門檻**：Agent 能在執行過程中自主搜尋所需的資源，而非依賴開發者在開發階段就預測所有可能性。

⚠️ **目前仍為草案階段，實作細節持續演進**

需要注意的是，ARD 目前仍處於「草案 (Draft)」狀態。雖然已有多家大廠參與，但作為一套開放規範，其詳細的索引機制與聯邦註冊表的同步過程仍在持續定義與優化中。

🎯 **對開發者的實務啟示：構建大規模 Agent 生態的關鍵**

如果你正在構建需要處理數千個臨時表面 (ad-hoc surfaces) 的複雜 Agent 系統，ARD 提供了一個非常有價值的方向：

- **擺脫 Context 壓力**：不再需要為了讓 AI 知道有哪些工具而浪費昂貴的 Token。
- **解耦開發與部署**：工具的更新與增加不再需要修改 Agent 的核心配置，只要工具在註冊表中可被發現即可。
- **關注實作**：建議關注 Hugging Face 的實作方式，探索如何將自家的工具集轉化為可被 ARD 索引的資源。

🔗 **詳細資訊**
📝 Agentic Resource Discovery: Let agents search
👤 Hugging Face Blog
🔗 文章：https://huggingface.co/blog/agentic-resource-discovery-launch

你認為 AI Agent 的未來是「全能型（預裝所有工具）」還是「搜尋型（隨用隨找）」？歡迎在下方分享你的看法 👇

#AI #Agent #HuggingFace #ARD #MCP #LLM #軟體工程 #AIInfrastructure
