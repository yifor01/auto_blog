---
title: 'Synthetic Sciences Releases OpenScience: An Open-Source, Model-Agnostic AI
  Workbench for Machine Learning, Biology, Physics, and Chemistry Research'
source: MarkTechPost
url: https://www.marktechpost.com/2026/07/05/synthetic-sciences-releases-openscience-an-open-source-model-agnostic-ai-workbench-for-machine-learning-biology-physics-and-chemistry-research/
score: 100
model: google/gemma-4-31b-it:free
generated_at: '2026-07-06T20:22:49.911962'
---

📌 OpenScience 開源科研 AI 工作臺  
TL;DR：OpenScience 提供開源、模型無關的瀏覽器 AI 工作臺，讓科研可在本地完成全流程。  

🎣 當 Anthropic 的 Claude Science 仍被視為封閉的科研助手時，一個開源替代方案悄然登場。它聲稱不需帳號、模型可自行選擇，全部資料留在自己的機器上。這預示著科研 AI 工具的所有權可能從單一廠商轉向社群。  

🤔 背景或問題  
科研領域對 AI 工具的需求日益增加，但現有方案多半綁定特定供應商，使用者難以掌控資料與模型選擇。Synthetic Sciences 因此提出 OpenScience，強調「工作流程開放、模型可互換、資料本地化」，以回應對供應商鎖定與資料隱私的擔憂。  

🧩 方法或架構  
OpenScience 是以瀏覽器為前端、以本地 Agent 執行時序為後端的工作臺。使用者只要提供研究目標，Agent 會依照文獻閱讀、假設形成、撰寫與執行程式碼、執行實驗、查詢科學資料庫以及撰寫結果的完整迴圈運作。其主要特點包括：  
- 模型無關：可使用任何前景或開放權重模型，僅需自行提供 API 金鑰。  
- 安裝方式：透過 npm 安裝，執行 `openscience` 開啟工作區；亦可直接使用 `npx synsci` 完成同一操作，無需全域安裝。  
- 本地伺服器：執行時在本機啟動伺服器，負責託管 UI、Agent 執行時序與工具層。工具層包含 Shell、編輯器、LSP、MCP 伺服器、科學聯結器與技能模組。  
- 模型路由：每個請求依工作區中的模型選擇器決定使用哪個模型，切換供應商或執行本地模型時無需更改其他設定。  
- 資料與狀態：所有會話、產出物與來源紀錄均儲存於磁碟，可透過連結分享。  
- 擴充性：檔案指出擴充性是第一級特徵（具體內容未進一步說明）。  

💡 深入分析  
從材料可見，OpenScience 的設計直接回應了兩個科研界常見疑慮：一是避免單一廠商綁定，二是確保研究資料不離開本機環境。透過模型無關與本地金鑰管理，使用者可以依據需求在開放權重模型與商業前景模型間自由切換，同時保持 API 金鑰不外洩。此外，工作臺將完整科研流程封裝在單一瀏覽器會話中，減少工具切換與環境配置的摩擦，有助於提升實驗的可重複性與團隊間的知識傳遞。  

⚠️ 限制  
目前公開的資訊未提供效能基準、使用者研究或社群採用程度的資料；亦未完整列出所謂「四項讓執行時適合實際工作」的具體內容。因此，關於該工具在大規模科研專案中的穩定性、長期維護與擴充生態系仍需後續觀察。  

🎯 實務啟示  
對於 AI/ML 工程師而言，OpenScience 提供一條可立即嘗試的路徑：  
1. 透過 `npm install -g openscience`（或直接 `npx synsci`) 安裝。  
2. 首次執行時選擇「Atlas 管理模式」、「自行提供的提供者金鑰」或「免費示範模型」。  
3. 在瀏覽器中設定研究目標，觀察 Agent 如何自動進行文獻閱讀、程式編寫與實驗執行。  
4. 依需求在模型選擇器中切換模型，所有金鑰與會話資料仍儲存在本機，可透過產生的連結與隊友共享成果。  
這樣的工作流程適合希望在不雲端上傳資料、又想靈活實驗不同基礎模型的科研團隊或個人開發者。  

🔗 來源  
- 標題：Synthetic Sciences Releases OpenScience: An Open-Source, Model-Agnostic AI Workbench for Machine Learning, Biology, Physics, and Chemistry Research  
- 作者／機構：Asif Razzaq  
- 連結：https://www.marktechpost.com/2026/07/05/synthetic-sciences-releases-openscience-an-open-source-model-agnostic-ai-workbench-for-machine-learning-biology-physics-and-chemistry-research/  

#OpenScience #AI工作臺 #模型無關 #開源科研 #本地化 #科研自動化 #npm安裝 #模型選擇 #資料隱私 #擴充性
