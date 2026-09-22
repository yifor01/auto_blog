---
title: How Trane gets building insights 60x faster with Amazon Bedrock AgentCore
source: AWS ML
url: https://aws.amazon.com/blogs/machine-learning/how-trane-gets-building-insights-60x-faster-with-amazon-bedrock-agentcore/
model: claude-code/sonnet
generated_at: '2026-09-22T20:39:16.374115'
score: 83
---

📌 HVAC 診斷從 20 分鐘變 20 秒，Trane 怎麼用 AgentCore 做到

TL;DR：Trane Technologies 用 Amazon Bedrock AgentCore 打造對話式代理，把多螢幕診斷流程壓縮成一句自然語言查詢。

管理全球數百萬臺連網 HVAC 設備是什麼概念？對 Trane 的技術人員來說，過去要回答一個維運問題，可能得在多個儀表板間切換、在層層選單裡鑽 20 分鐘。這種摩擦不只是體驗差，而是實際拖慢維修決策、造成企業層級的損失。

🤔 同一份資料，不同角色需要完全不同的視角

Trane Technologies 年營收超過 210 億美元，業務遍及 100 多個國家，旗下 Trane Cloud 彙整來自數百萬臺 HVAC 系統的即時效能資料，理論上足以支撐預測性維護與能源最佳化。但問題在於：現場技術人員需要冷媒壓力、故障碼這類診斷級精度；客戶經理需要正常運行時間、成本節省機會；建築業主則需要效能分數、永續指標這種高階摘要。既有的儀表板工具卻是「一套介面打天下」，逼每個角色都得在不屬於自己工作流程的畫面裡摸索，連基礎的跨設備比較都得靠人工手動串聯多個畫面。

🧩 用 Strands + AgentCore 搭出的多代理架構

Trane 工程團隊只花 3 到 4 週，就在 Amazon Bedrock AgentCore 與 Strands framework 上建出對話式代理，並用 AWS CDK 做基礎設施即程式碼部署。團隊選擇 Strands 負責 agent 行為的開發者 SDK 與編排邏輯，AgentCore 則接管底層的 managed runtime、記憶、工具閘道與生產環境基礎設施。為避免單體式設計的侷限，架構採用多代理設計：每個專門助理由自己的 system prompt 治理，只專注單一能力領域，且可透過 AgentCore Gateway 與 MCP 這類開放標準，接入更多 agent 或工具（例如工單管理系統、企業 CRM）。

打造這套系統時遇到四個架構挑戰：整合（要同時串接即時遙測資料、大型知識庫的智慧搜尋，還要能連到 CRM 等外部系統）、分離（agent 邏輯必須和後端工具執行解耦，才能獨立部署、劃清權責邊界）、上下文（要在診斷過程中維持對話狀態，卻不想自建複雜的向量資料庫基礎設施）、可觀測性（agent 在多步驟推理鏈中協調多個工具，一旦出錯很難定位是 API 憑證缺失、工具回應格式錯誤，還是模型幻覺）。

團隊在導入 AgentCore 前，也評估過用 Amazon ECS 或 AWS Lambda 自建，但那意味著要在運算層之上自行打造 session 隔離、自動擴縮、按 session 計費等邏輯。最終選擇 AgentCore 的關鍵有四點：managed runtime 免去基礎設施維運（不需要自建叢集，session 間也沒有閒置容量要付費）；內建 session memory 省去自建與維護外部向量資料庫的成本；AgentCore Gateway 提供原生工具編排，讓既有內部 API 不必逐一手寫整合就能變成 agent 可用的工具；框架無關的設計則讓團隊能用 Strands SDK，不被綁死在某個專有的編排層上。

📊 60 倍的 time-to-insight 改善

根據 Trane 內部與技術人員進行數週的實測基準，這套解法把原本 20 分鐘的多螢幕診斷流程，壓縮成 20 秒內完成的自然語言對話，相當於 time-to-insight 提升 60 倍。曾經需要人工在多個畫面間手動串聯的跨設備比較與診斷工作流程，如今透過單一自然語言查詢即可完成。

🎯 實務啟示

這個案例對正在評估企業級 agent 架構的工程團隊很有參考價值：與其自己在 ECS/Lambda 上手刻 session 隔離、記憶體管理和工具整合，用託管的 agent runtime 能省下大量重工。多代理設計（每個 agent 綁定單一領域 system prompt）也是應對「不同角色需要不同視角」這類需求分歧的實用模式，而不是硬把所有邏輯塞進一個巨大的 prompt。

🔗 來源
- 標題：How Trane gets building insights 60x faster with Amazon Bedrock AgentCore
- 作者／機構：Senthil Chinnaiyan（AWS ML Blog）
- 連結：https://aws.amazon.com/blogs/machine-learning/how-trane-gets-building-insights-60x-faster-with-amazon-bedrock-agentcore/

#AWS #BedrockAgentCore #AIAgents #Strands #HVAC #IoT #GenAI #EnterpriseAI #MultiAgent #TraneTechnologies
