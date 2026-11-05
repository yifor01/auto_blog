---
title: Le Chonk brings the brains. Studio puts it to work.
source: Mistral AI
url: https://mistral.ai/news/build-with-studio/
model: claude-code/sonnet
generated_at: '2026-11-05T22:50:44.807646'
pinned: true
---

📌 Mistral Studio 升級：把 Le Chonk 的智慧接上企業流程

TL;DR：Mistral Studio 新增 managed agents、workflows 與企業 context 功能，讓 Mistral Large 4（Le Chonk）能真正落地到生產環境。

多數工業 AI 專案卡在 pilot 階段，走不到生產環境，這是素材裡 Accenture 高層直接點出的現況。Mistral 這次想用一個平臺把「做出 demo」和「跑進生產線」之間的距離補起來。

🤔 **背景：模型強不代表用得上**
Mistral Large 4（Le Chonk）在程式碼能力、防禦性資安能力與複雜文件的推理上有進展，但這些能力要真正發揮作用，企業需要把模型接上自己的資料與系統。Mistral Studio 就是負責這件事的企業 AI 平臺，可以部署在雲端、企業自己的 VPC、地端或混合環境，讓企業保留對基礎設施與資料存取方式的控制權。

🧩 **三個積木：Agent 調查行動、Workflow 協調流程、App 給員工介面**
Studio 把這三者放在同一套基礎設施上運作。開發團隊先透過 connectors 與 MCP server 把模型接上企業資料與系統，再在這個基礎上建 agent、workflow、app，由 Studio 統一管理執行狀況，並讓團隊能檢視實際發生了什麼。透過新推出的 Mistral MCP server，開發者可以用 Mistral Vibe 或自己原本就在用的 coding agent 開發，先在本機測試，再用一行指令部署到 Studio 環境，hosting 與執行都交給 Studio 負責。

📊 **Managed agents：配備 skills、sandbox 與 subagent 的生產級 agent**
開發者現在可以在 Studio 裡建立能執行複雜多步驟任務的 agent，並為它配置 skills（把團隊的作業流程封裝進去）、可以跑程式碼的 sandbox，以及可以委派子任務的 subagent；hook 則讓開發者在執行的關鍵節點插入自訂邏輯，決定 agent 怎麼運作、怎麼跟既有系統整合。這套 runtime 沿用的是支撐「每週數百萬次 Mistral Vibe session」的既有基礎設施，開發者可以專心設計 agent 的能力與行為，同時設定它能存取的工具、資料與動作邊界。素材舉的例子是 Mistral 自己的工程團隊，在 Studio 裡建了一個調查生產事故的 agent：警報觸發後，它會依照團隊的 runbook 展開調查，在要執行敏感動作前先請求核准，並把調查結果貼到 Slack，讓工程師接手時已經有現成的脈絡可用，團隊因此每月省下數百小時。

📊 **Workflows：固定規則、agent 推理與人工決策可以混在一條流程裡**
Workflow 定義的是一個流程怎麼跑：哪些步驟走固定規則、哪裡需要 agent 推理、哪裡該交給人來決定，而且中斷的執行可以從斷點繼續，不用重跑。團隊可以直接在 Mistral Vibe 用自然語言描述一個流程，再用它來生成、測試、部署成 workflow，產生的程式碼可以檢視與編輯。這次更新也加入了來自企業系統的 event trigger，以及方便檢視流程邏輯的視覺化 graph。素材提到的例子是 Mistral 自己的 product operations 團隊：他們用 Studio 建了一個分類內部想法與客戶回饋的 workflow，模型先辨識出哪些是 bug、哪些是功能請求，再依路由規則分派給對應團隊，每週省下大約 35 小時的工時。

💡 **已在生產環境使用的客戶**
素材提到 ABANCA、Accenture、Alten、BNP Paribas、Capgemini、CMA CGM、Tata Consultancy Services 等客戶與合作夥伴已在生產環境使用 Studio。BNP Paribas 的 AI 與 IT 創新主管強調，他們把 Studio 跑在自己的基礎設施上，是因為這些系統處理的是最敏感的業務流程，需要保留完全控制權；CMA CGM 的 VP AI 則提到，他們跟 Mistral 工程師一起在貨運放行、客服與運輸單等流程上建立 AI 系統，用 Studio 讓每個新流程能在數週內（而不是數月）進入生產環境。

🎯 **實務啟示**
對工程師來說，這次更新的重點是把 skills、sandbox、subagent、hook 當成一等公民，搭配本機開發、一行指令部署的工作流程，把「寫 agent」和「維運 agent」的 runtime 責任分開。如果團隊正在評估企業內部的 agent 平臺，這套「本機開發 → MCP server 串接 → Studio 託管執行」的分工方式值得參考。

🔗 **來源**
- 標題：Le Chonk brings the brains. Studio puts it to work.
- 作者／機構：Mistral AI
- 連結：https://mistral.ai/news/build-with-studio/

#Mistral #MistralAI #EnterpriseAI #AIAgents #LLM #Workflow #MCP #AIOps #Automation #GenAI
