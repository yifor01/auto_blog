---
title: Fission-AI/OpenSpec
source: GitHub Trending
url: https://github.com/Fission-AI/OpenSpec
score: 93
model: tencent/hy3-preview:free
generated_at: '2026-06-04T20:57:40.068264'
---

📌 【Fission-AI】OpenSpec：AI 引導的規格工作流程  

你有沒有過這種體驗：在會議室裡討論功能時，大家都同意要「做這件事」，但等到要寫規格文件時，卻發現需求變得模糊、設計圖稿被反覆修改，最後開發團隊還是得花很多時間在澄清與返工？  

🤔 **為什麼傳統規格文件總是變得過時或過於冗長？**  
許多團隊仍採用瀑布式的規格編寫：先寫長長的需求說明，再畫出詳細的設計圖，最後才交給工程師實作。這種流程在需求頻繁變動的環境中容易產生資訊斷層，也讓文件維護成本居高不下。  

🧪 **OpenSpec 的核心設計：fluid、iterative、easy、brownfield、scalable**  
根據專案說明，OpenSpec 以五個指導原則打造：  
- **fluid not rigid** – 規格可隨著想法自然流動，不被固定格式束縛。  
- **iterative not waterfall** – 支援逐步提出、修改與驗證，適合敏捷開發。  
- **easy not complex** – 透過簡單的 CLI 指令即可產出結構化 artefact。  
- **built for brownfield not just greenfield** – 可直接導入既有專案，不必從零開始。  
- **scalable from personal projects to enterprises** – 從個人實驗到大型團隊皆可使用。  

 **從一句話到可執行的清單：/opsx:propose 與 /opsx:apply 的實際流程**  
使用方式如下：  
1. 在終端機輸入 `/opsx:propose "your idea"`，AI 會為此想法建立一個專屬目錄，內含：  
   - `proposal.md` – 說明為何要做這件事以及變更內容。  
   - `specs/` – 需求與場景描述。  
   - `design.md` – 技術實作方向。  
   - `tasks.md` – 實作檢查清單。  
2. 接著執行 `/opsx:apply`，AI 會根據 `tasks.md` 逐項執行，並在完成後回報所有任務已完成。  
3. 若需要暫時結束此功能的開發週期，可使用 `/opsx:archive` 將產出的 artefact 移至歷史資料夾，同時更新規格文件，為下一個功能做好準備。  

💡 **artefact-Guided 工作流程如何減少來回溝通？**  
OpenSpec 將「想法」直接轉換為可追蹤的文件與任務清單，使得產品經理、設計師與工程師在同一個結構化 artefact 上進行討論。這種方式把需求的「為什麼」、設計的「怎麼做」以及實作的「什麼要做」都放在同一個版本控制的目錄中，減少了因文件分散或版本不一致導致的誤解。  

⚠️ **目前限制：依賴 Node.js 20+, 早期社群，功能仍在演進**  
- 必須安裝 Node.js 20.19.0 或以上版本才能使用全域 CLI。  
- 專案剛上線不久，社群文件與範例仍在積累中。  
- 雖然展示了基本的提議、實作與封存流程，但更進階的功能（如分支合併、衝突偵測、與既有 issue tracker 的深度整合）尚未在說明中提及。  

🎯 **實務啟示：適合需要快速啟動功能開發的團隊，可作為需求與設計的起點**  
- 對於希望減少規格文件撰寫時間、快速取得共識的團隊來說，OpenSpec 提供了一種「先有結構，再逐步填充」的方式。  
- 可以將其視為需求與設計的「草稿產生器」：先用 AI 產出初步 artefact，再由人類審閱、補充與調整，最後交給開發團隊執行。  
- 由於其 artefacts 是普通的 Markdown 檔案，易於納入既有的版本控制系統（Git），不會額外增加學習成本。  

🔗 **資源連結**  
📂 GitHub：https://github.com/Fission-AI/OpenSpec  
💬 Discord：加入 OpenSpec 官方討論群取得即時協助  
🐾 X（Twitter）：追蹤 @0xTab 獲取最新更新與使用技巧  

你是否曾嘗試讓 AI 幫忙產出規格文件？歡迎在留言區分享你的使用經驗或對此類工作流程的看法 👇  

#OpenSpec #AI工具 #規格管理 #軟體開發 #FissionAI #NodeJS #開發效率 #GitHubTrending
