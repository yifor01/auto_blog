---
title: Nvidia launches free tool that links idle computers into a personal AI data
  center
source: The Verge AI
url: https://www.theverge.com/ai-artificial-intelligence/989435/nvidia-pair-personal-ai-router-home-local-llm-compute-tool-rtx-macbook
model: claude-code/sonnet
generated_at: '2026-09-03T20:18:25.347677'
score: 92
---

📌 Nvidia 推出免費工具 PAIR，把家裡閒置電腦串成個人 AI 叢集

TL;DR：Nvidia 開源工具 PAIR 讓家用 RTX 顯卡與 Mac 自動組隊，共同執行本地 LLM 推理任務。

家裡的遊戲主機、工作用筆電、還有那臺很少開機的桌機，平常大部分時間都在閒置。Nvidia 這次要做的，就是把這些散落各處的算力，串成一個能一起跑 AI 推理任務的家用叢集。

🤔 **問題：算力散落在家裡各處，卻沒被用上**

Nvidia 發表新工具 Personal AI Router（PAIR），一款免費工具，用來同步家中多臺電腦，協同處理本地 AI 推理任務，可搭配 Ollama、LM Studio 等工具使用。需要先澄清的是，儘管名稱裡有「Router」，PAIR 並不是一個硬體路由器，而是 Nvidia 開發的開源軟體，功能是在網路上探索相容的電腦、將它們連接起來，並讓它們準備好處理 agentic workflow 的運算需求。

🧩 **怎麼運作：閒置時搭把手，離線時自動退出**

相容裝置以 Nvidia GeForce GPU 為主，PAIR 支援 RTX 20 系列以上顯卡、RTX Pro GPU 以及 DGX Spark 系統，另外 Apple M4 以上晶片的裝置也能加入。PAIR 的關鍵設計是只在裝置閒置時動用其算力，避免干擾使用者當下的其他工作；這套分散式系統能讓多臺電腦並行處理大量運算請求，對於會把複雜任務拆解成多個小工作的 agentic workflow 特別有幫助，藉此避免單一 GPU 成為瓶頸。Nvidia 表示 PAIR 能隨裝置加入或離開網路而動態調整，例如當使用者在自己的桌機上開始玩遊戲時，系統會自動因應。

在一場媒體簡報中，Nvidia 產品經理 Seth Schneider 描述了一個情境：一個家庭裡，爸爸有 Nvidia RTX Spark 筆電與 DGX Spark 桌機、媽媽有一臺 RTX 5090 筆電、女兒有一臺遊戲桌機、兒子有一臺 MacBook Pro，Schneider 估計這樣一個家庭合計約有 165 teraflops 的閒置算力，「這真的是家家戶戶都閒置著的免費 token 寶庫」，即使把用電成本算進去也是如此。

安全性方面，PAIR 透過六位數配對碼將所有裝置配對，再以 mTLS（雙向傳輸層安全）加密通道，建立雙向可信任的加密通訊連線。PAIR beta 版本現已開放，支援 Windows、Linux 與 macOS。

💡 **理想的使用情境比想像中樸素**

被問到 PAIR 真正的目標使用者是誰、什麼樣的家用配置最實際時，Schneider 表示 Nvidia 預期多數 PAIR 使用者的組合會比示範情境樸素得多，大致是「一臺 MacBook 或 Windows 筆電，搭配一臺遊戲桌機」這種常見組合。除了 PAIR 之外，Nvidia 也宣布三款主流 AI agent 應用——Perplexity Portable Computer、Hermes Agent 與 OpenClaw——將在 Windows 上提供搭配 Nvidia GPU 的簡化本地安裝流程，減少使用者原本需要手動設定的步驟。

🎯 **實務啟示**

如果你手邊剛好有一臺閒置的遊戲桌機和一臺筆電，PAIR 提供了一條不必添購新硬體、就能把多臺異質裝置串成小型推理叢集的路徑，對想在本機跑 LLM、又受限於單機顯示卡記憶體的工程師或愛好者來說，值得留意這個 beta 工具的後續發展；但要注意，目前 Nvidia 自己給出的示範情境（多臺高階顯卡的家庭）偏向極端案例，實際效益仍取決於你家中裝置的組合與新鮮程度。

🔗 **來源**
- 標題：Nvidia launches free tool that links idle computers into a personal AI data center
- 作者／機構：Antonio G. Di Benedetto（The Verge）
- 連結：https://www.theverge.com/ai-artificial-intelligence/989435/nvidia-pair-personal-ai-router-home-local-llm-compute-tool-rtx-macbook

#Nvidia #PAIR #LocalLLM #EdgeAI #DistributedComputing #Ollama #LMStudio #RTX #HomeLab #AgenticWorkflow
