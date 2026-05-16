---
title: "dograh-hq/dograh"
source: GitHub Trending
url: https://github.com/dograh-hq/dograh
score: 103
model: tencent/hy3-preview:free
generated_at: 2026-05-16T19:26:50.551104
---

📌 Dograh：開源語音代理，2 分鐘上手  
你以為語音代理只能靠付費 SaaS？  
一行 Docker 指令就能讓你完全掌控代碼與資料。  
🔓 免供應商鎖定，隨時自行擴充 LLM / TTS / STT  

🤔 開源語音代理的缺失讓團隊被鎖在 SaaS  
現有的 Vapi、Retell 等方案都是封閉的雲端服務，使用者無法看到程式碼、無法自行部署，也難以調整語言模型、語音合成或語音辨識的提供者。這意味著一旦選定供應商，資料與功能都受限於其雲端政策與計費方式。  

🧪 透過 Drag‑and‑Drop 工作流程建構器，2 分鐘內跑出可用語音機器人  
Dograh 提供一個可視化的工作流程編輯器，開發者只需透過拖拉方式定義對話流程、選擇 LLM、STT 與 TTS 的提供者，然後透過一行 `docker run` 指令即可在本機或自有伺服器上啟動服務。根據專案說明，從下載到擁有一個可互動的語音代理僅需不到兩分鐘。  

🚀 BSD 2-Clause 授權、自架與 Bring‑your‑own‑model 的完整對比  
- 授權：BSD 2-Clause（完全開源）  
- 部署方式：可自架（一個 Docker 指令即可），與 Vapi、Retell 僅提供 SaaS 形成對比  
- 定價：自架時免費；若選擇使用官方雲端則依使用量計費  
- 模型與服務：可自行帶入任何 LLM、STT、TTS 提供者，或使用 Dograh 內建的堆疊  
- 原始碼層級客製化：每一行程式碼皆可修改、 fork、貢獻  
- 資料住放：所有資料存放於使用者自己的基礎設施，符合資料主權需求  
- 供應商鎖定：無（開源且可自架）  

💡 原始碼完全可修改、資料住放在自家基礎設施，零供應商鎖定  
因為專案採用 BSD 2-Clause 授權，開發者可以直接閱讀、修改、重新發布任何部分的程式碼。這不僅提供了透明度，也意味著語音管線的每一個環節——從語音辨識到語言理解、再到語音合成——都可以依據實際需求替換或優化，而不必受限於供應商的預設整合。  

⚠️ 需自行管理基礎設施與遙測選項（ENABLE_TELEMETRY=false）是使用上的考量  
雖然 Dograh 提供自架的彈性，但這也意味著使用者必須負責伺服器的安裝、更新與監控。專案說明中提到，預設會收集匿名使用資料以改進產品；若不願分享，可透過設定環境變數 `ENABLE_TELEMETRY=false` 來關閉遙測。  

🎯 對想掌控語音 AI 堆疊的工程師而言，Dograh 提供即時可用的開源替代方案  
對於希望避免供應商鎖定、想要完全掌握語音代理技術棧的團隊，Dograh 給出了一個可以在兩分鐘內啟動、原始碼完全開放、支援自行選擇模型與服務的解決方案。這使得在評估語音 AI 平台時，多了一個可直接下載、自行部署且無授權費用的選項。  

🔗 專案連結  
📂 GitHub：https://github.com/dograh-hq/dograh  
📖 文件：同上倉庫內的 Docs 目錄  
📺 產品演練（2 分鐘）：專案頁面內所提供的影片連結  
📊 比較表：專案 README 中的 Dograh vs Vapi vs Retell 對比  

#Dograh #開源 #語音代理 #SelfHosted #AI工程 #語音AI #GitHubTrending #BSD #VoiceAgent #LLM #TTS #STT
