---
title: Nvidia launches new open models to run agents in the enterprise and on PCs
source: TechCrunch AI
url: https://techcrunch.com/2026/10/19/nvidia-launches-new-open-models-to-run-agents-in-the-enterprise-and-on-pcs/
model: claude-code/sonnet
generated_at: '2026-10-19T21:38:29.313253'
score: 102
---

📌 Nvidia 開源新模型：企業級 Agent 與 PC 本地 Agent 一次補齊

TL;DR：Nvidia 推出 120B 的 Nemotron 3.5 Super VL 與輕量 Bolt 系列,讓開放權重模型打進企業資料中心與消費級 AI PC。

當 OpenAI、Anthropic 這些前沿模型實驗室開始把目光轉向 Trainium、Cerebras 等其他晶片時,Nvidia 選擇反過來加碼推自己的開放權重模型——這次目標是企業 Agent,也是你家桌機裡的那張 RTX 顯示卡。

🤔 **為什麼 Nvidia 要自己做開放模型**

Nvidia 在週四發布一批新的開放權重模型,專門針對「常駐型」Agent 與邊緣運算場景設計。Nemotron 3.5 Super VL 是一個 1,200 億參數的大型模型,定位是企業級 Agent 使用;另一端則推出兩個輕量的 Bolt 模型,設計給搭載 Nvidia RTX Spark 晶片的新款 AI PC,以及搭載 DGX Spark 的工作站,這類裝置目前正透過 Microsoft、Dell 等合作夥伴推向消費者、程式開發者與企業知識工作者市場。

Nvidia 開放模型與軟體部門副總裁 Kari Briski 在發布部落格中表示：「任何想在 Nvidia 基礎設施上執行 Agent 的組織,現在都有一個對應自己需求層級的開放、最佳化模型,不必在能力與可部署性之間做取捨。」

🧩 **Super VL：用更少參數追上 Ultra 的準確度**

Nemotron 3.5 Super VL 雖然參數量比 Nemotron 3 Ultra 模型少,但 Nvidia 宣稱在 instruction-following 與工具使用任務上能達到相近的準確度。官方表示,在針對特定 Agentic 任務（包括文件智慧處理、財務會計、科學實驗、醫療保險理賠、安全攻擊防禦)完成 post-training 後,Super VL 執行任務的速度比 Anthropic 與 OpenAI 的對照模型（Opus 5、GPT 6.1 Sol、Luna、Astra)更快。

這類廠商自我宣稱的比較說法在每次新模型發布時都很常見,但 Nvidia 這次附上了一份實際使用 Super VL 的企業名單作為佐證,包括 Skydance、EY、Ramp、Crowdstrike、Perplexity 與 Salesforce。Briski 也強調開放模型相對封閉前沿模型的差異：「與封閉的前沿模型不同,組織可以用自己的資料對 Super VL 進行 post-training,部署在自己的基礎設施上,並真正擁有自己建構出來的東西。」

🧩 **Bolt 系列：把 Agent 塞進你的桌機**

兩款 Bolt 模型走的是另一條路線。Nemotron 3.5 Bolt 74B-A9B 24GB 是一個 740 億參數模型,設計用於本地端 Agentic 任務,在速度與推理能力之間取得平衡,可處理多步驟推理、工具呼叫與網頁瀏覽。體型最小的 Bolt E4B 則是針對對話型 Agent 設計。Super VL 與 Bolt 74B-A9B 現已上線,Bolt E4B 預計本月稍晚推出。

💡 **兩種市場、同一套算盤**

這並非 Nvidia 第一次發布與前沿實驗室競爭的開放權重模型——旗下 Nemotron 家族已涵蓋多模態 AI、推理、程式設計、數學與企業自動化等多個方向。文中點出背後的產業脈絡：越來越多成長中的前沿 AI 實驗室開始尋求 Nvidia 以外的運算選項,例如 AWS 的 Trainium、Cerebras,甚至自研晶片,而 Nvidia 正是藉由力推「企業自建資料中心跑開放模型」這個趨勢來維持自己在生態系中的位置。

至於 PC 端的 Bolt 模型,則瞄準另一個尚在萌芽的市場——消費級 AI 助理。文中提到,面對幾乎每天都有新 AI 助理推出的環境,注重隱私的消費者未必願意讓這類助理深度接觸自己的家庭、健康、財務等資訊,而本地執行正是 Nvidia 用來打開這塊市場的切入點：讓 PC 使用者「可以把日常工作交給 Agent 處理……不必把這些工作負載送上雲端」。

🎯 **實務啟示**

對企業工程團隊而言,Super VL 的賣點在於可自行 post-training、自行部署,適合不想把敏感資料送進封閉模型 API 的場景;對個人開發者與邊緣應用而言,Bolt 74B-A9B 與即將推出的 E4B 則提供了在本地 AI PC 上跑多步驟 Agent 任務的選項,值得在規劃本地推理方案時納入評估清單,但目前文中並未揭露精確的 benchmark 數字,實際能力仍需自行驗證。

🔗 **來源**
- 標題：Nvidia launches new open models to run agents in the enterprise and on PCs
- 作者：Julie Bort @ TechCrunch
- 連結：https://techcrunch.com/2026/10/19/nvidia-launches-new-open-models-to-run-agents-in-the-enterprise-and-on-pcs/

#Nvidia #Nemotron #OpenWeights #AIAgents #EdgeAI #AIPC #EnterpriseAI #RTX #DGXSpark #OpenSourceAI
