---
title: "earendil-works/pi"
source: GitHub Trending
url: https://github.com/earendil-works/pi
score: 108
model: tencent/hy3-preview:free
generated_at: 2026-05-26T20:48:23.997366
---

📌 【earendil-works/pi】自擴展編程代理  

你見過能自行擴展功能的開源編程代理嗎？這個剛上 GitHub Trending 的專案，只要幾行指令就能啟動多模型 LLM 工具鏈。  
但它的真正用途，或許在於開發者共享真實的編程會話。  

🤔 **開源編程代理需要統一的工具鏈與可分享的使用紀錄**  
現有的 coding agent 常散落在不同的套件與腳本中，缺乏統一的多模型支援與會話紀錄機制，使得實驗難以重現且社群貢獻零散。  

🧪 **模組化單體倉庫提供三個核心套件：CLI、運行時與統一 LLM API**  
pi 倉庫包含 @earendil-works/pi-coding_agent（互動式命令列代理）、@earendil-works/pi-agent_core（負責工具呼叫與狀態管理的運行時）以及 @earendil-works/pi_ai（整合 OpenAI、Anthropic、Google 等供應商的統一 LLM 介紹）。所有套件均以 TypeScript 發布，附帶完整文檔與範例。  

🚀 **該專案提供自動封閉 issue/PR 的工作流程與每日維護者審查機制**  
為減少維護負擔，新開的 issue 與 pull request 預設會被自動封閉；維護者每日檢視這些自動封閉的項目，決定是否重新開啟或進一步處理。這樣的設計讓專案能在高流量下保持乾淨的追蹤狀態。  

💡 **透過會話共享工具，開發者可以將真實的編程過程貢獻回社群，補充玩具基準的不足**  
專案鼓勵使用者透過 badlogic/pi-share-hf 將自己的 pi-mono 編程會話發布至 Hugging Face。這樣的真實會話資料涵盖了工具使用、失敗與修復過程，比起合成基準更能反映實際開發情境。  

⚠️ **自動封閉機制可能誤殺合理貢獻，依賴維護者每日審查**  
由於所有新貢獻預設被封閉，誤判的風险存在；專案目前的緩解方式是維護者每日檢查，但這意味著社群貢獻的及時性仍受人工審查節奏限制。  

🎯 **工程師可直接透過 CLI 建立自己的編程代理，並使用 Hugging Face 工具發布開源會話**  
只要安裝 @earendil-works/pi-coding_agent，即可獲得互動式代理介面；配合 pi_ai 與 pi_agent_core，便能快速切換不同 LLM 後端。完成實驗後，使用 pi-share-hf 將會話上傳至 Hugging Face，為社群提供可重現的真實任務資料。  

🔗 **專案連結**  
📂 earendil-works/pi  
🔗 https://github.com/earendil-works/pi  

你已經試過 pi 來建構自己的編程助手了嗎？歡迎在留言區分享你的設定與體驗 👇  

#AI #CodingAgent #OpenSource #LLM #TypeScript #GitHubTrending
