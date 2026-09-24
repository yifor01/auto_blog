---
title: Deploy and manage coding agents at scale with the Unity Gateway CLI
source: Databricks
url: https://www.databricks.com/blog/deploy-and-manage-coding-agents-scale-unity-gateway-cli
model: claude-code/sonnet
generated_at: '2026-09-24T20:50:40.586783'
score: 79
---

📌 Databricks推出Unity Gateway CLI，一行指令治理所有coding agent

TL;DR：Unity Gateway CLI讓管理員集中管控模型與預算，開發者一個指令切換coding agent。

🎣 過去六個月，GPT-6、Claude Opus 5.5、Gemini 3.8、Grok 4.7相繼發布，外加Kimi K3、GLM-5、DeepSeek V4.1等開源權重模型上線——平均每五天就有一個新的frontier模型問世，負責開發者工具的團隊被夾在中間動彈不得。

🤔 標準化或開放，兩難的選擇
只選定一家供應商，就有可能錯過別處更好或更便宜的模型；支援多家agent與供應商雖然給了工程師選擇權，卻讓存取權限、預算控管、安全政策與使用紀錄散落在不同系統裡，難以統一管理。Databricks認為組織真正需要的是兩者兼具：能隨時採用最佳選項的自由，加上能跨數千名開發者統一治理的方式。

🧩 一個指令連上任何已核准的agent
Unity Gateway CLI（指令為ug）由管理員在Unity Gateway集中管理已核准的模型、工具與花費政策；開發者只要照舊工作方式，用`ug claude`或`ug codex`這樣的指令啟動任一已核准的agent，Unity Gateway便會處理authentication並自動套用發布好的設定。當有更好的模型或更有效率的工作流程出現，團隊可以一次對所有支援的agent推出，不必逐一重新設定。

管理面板位於Unity Gateway → Govern → Agent Configuration，管理員可在此設定default模型、MCP servers、skills、Smart Routing與花費政策；設定發布後，開發者能在已啟用的agent之間自由切換，不需個別設定。組織也可透過裝置管理部署ug，讓所有人一開始就套用同一套核准設定，管理員能鎖定特定設定，並支援以cohort為單位分階段推出新模型。

🧩 Smart Routing：簡單任務用便宜模型，困難任務用強模型
管理員可集中啟用Smart Routing，讓簡單工作交給較便宜的模型、困難工作交給能力更強的模型，且Smart Routing會分別為主session與被委派給subagent的工作選擇模型，開發者則可以留在慣用的coding agent裡，不用自己判斷每個任務該挑哪個模型。根據Databricks公布的Smart Routing評測，這套機制在其內部coding benchmark上帶來35%的成本節省。

📊 預算門檻與trace追蹤，找出被浪費的token
當花費達到設定的預算門檻，Unity Gateway可以讓較低成本的agent與模型自動成為新啟動工作階段的預設值，且不中斷正在進行中的工作；開發者可用`ug usage`查詢花費與剩餘預算。Unity Gateway還能擷取coding agent的trace，包含本地tool call與skill呼叫；管理員集中啟用tracing後，ug會設定受支援的client把trace匯出到lakehouse的統一trace table，團隊可用Genie找出重複的tool失敗、過大的回應等浪費token的來源並加以修復。Databricks自己的工程團隊透過Unity Gateway tracing搭配Genie One找出並修復七個MCP tool bug，估計每年省下120萬美元的AI花費與生產力損失。

⚠️ 素材侷限
這篇內容偏向產品發表，沒有提供更深入的技術架構細節，例如authentication的具體實作方式或完整支援的agent清單，這些細節需另行查閱官方quickstart文件。

🎯 對工程師的實務啟示
如果團隊正卡在「該不該讓工程師自由選coding agent」這個問題上，Unity Gateway這種把「模型汰換」與「預算控管」跟「開發者日常工作流程」脫鉤的設計值得參考——換模型不必逼所有人改變慣用介面。而Smart Routing與budget-triggered的降級預設，也是控管AI支出時可以直接借鏡的折衷做法。

🔗 來源
- 標題：Deploy and manage coding agents at scale with the Unity Gateway CLI
- 作者／機構：Databricks
- 連結：https://www.databricks.com/blog/deploy-and-manage-coding-agents-scale-unity-gateway-cli

#Databricks #UnityGateway #CodingAgents #DeveloperTooling #LLMOps #SmartRouting #MCP #AIGovernance #CostOptimization #EnterpriseAI
