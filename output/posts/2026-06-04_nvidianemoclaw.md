---
title: NVIDIA/NemoClaw
source: GitHub Trending
url: https://github.com/NVIDIA/NemoClaw
score: 122
model: tencent/hy3-preview:free
generated_at: '2026-06-04T20:33:41.170786'
---

📌 【NVIDIA】NemoClaw：在 OpenShell 沙箱中安全運行 AI Agent 的參考堆疊  

隨著 AI Agent 逐漸成為生產環境中的常見組件，如何在不犧牲安全性的前提下讓它們「長期在線」運行，成為工程師們共同面臨的挑戰。NVIDIA 今天在 GitHub Trending 上釋出的 NemoClaw，正是為了解決此問題而設計的開源參考堆疊。  

🤔 **安全與便利難以兼得？**  
許多現有方案要么提供彈性但缺乏嚴格的隔離機制，要么則過於封閉導致開發與部署變得繁瑣。這種兩難讓團隊在選擇 Agent 執行環境時，常常只能在「容易上手」與「安全可靠」之間做出妥協。  

🧪 **單一 CLI 提供完整生命週期管理**  
NemoClaw 透過一條指令整合了導引式上手、硬化藍圖、路由推論、網路政策以及生命週期管理五大功能。它支援兩種預設 Agent：  
- **OpenClaw**（預設）  
- **Hermes**（透過環境變數 `NEMOCLAW_AGENT=hermes` 或安裝後使用 `nemohermes` 別名啟用）  

所有設定與說明均可在官方文件中查閱，包括架構概覽、生態系統說明（OpenClaw、OpenShell 與 NemoClaw 如何組合）、以及更細緻的架構細節（Plugin 結構、藍圖生命週期、沙箱環境與主機端狀態）。  

💡 **「硬化藍圖」與「路由推論」是核心防護層**  
文件指出，NemoClaw 內建的藍圖經過加固，可限制 Agent 在沙箱內的資源存取與系統呼叫；而路由推論則允許管理員根據政策將推論請求導向不同的後端服務，進一步減少單點失敗或惡意利用的風險。這兩項機制共同構成了「安全運行 always‑on AI Agent」的基礎。  

⚠️ **僅為參考實作，實際效能與適配度需自行評估**  
NemoClaw 目前提供的是參考堆疊（reference stack），文件未附帶效能基準或大規模生產環境的驗證數據。使用者仍需依據自身硬體、軟體平台（見 Prerequisites 頁面）以及特定的網路與安全需求，進行對應的調整與壓力測試。  

🎯 **適合希望快速建立安全 Agent 執行平台的團隊**  
- 若你正在評估如何在 OpenShell 中部署長期運行的 AI Agent，NemoClaw 提供了一套可直接上手的藍圖與 CLI 工具。  
- 透過設定不同的 Agent（OpenClaw 或 Hermes），你可以依據功能需求選擇合適的預設配置。  
- 建議先閱讀「Overview」與「Architecture Overview」頁面，再根據「Prerequisites」檢查環境是否符合，最後透過單一 CLI 完成安裝與初始化。  

🔗 **資源連結**  
📦 專案：https://github.com/NVIDIA/NemoClaw  
📚 文件：同上連結內的 documentation 區段（含 Overview、Architecture、Ecosystem、Architecture Details、Prerequisites、Inference Options、Network Policies 等章節）  

你有在沙箱中運行 AI Agent 的經驗嗎？歡迎在留言區分享你對 NemoClaw 的看法或使用心得 👇  

#NVIDIA #NemoClaw #OpenShell #AIAgents #Sandbox #GenAI #開源工具 #安全部署 #Claude #Hermes #OpenClaw
