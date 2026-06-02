---
title: "NVIDIA/OpenShell"
source: GitHub Trending
url: https://github.com/NVIDIA/OpenShell
score: 127
model: tencent/hy3-preview:free
generated_at: 2026-06-02T21:27:05.105789
---

📌 【NVIDIA 最新開源】OpenShell：為自主 AI Agent 打造的安全沙箱  

你擔心 AI Agent 會偷走你的憑證或亂跑網路嗎？NVIDIA 開源的 OpenShell 宣稱能用 YAML 政策把它關在沙箱裡，讓你在本機就能安全測試與擴充自主代理。  

🤔 **AI Agent 安全的缺口**  
隨著自主 AI Agent 在開發與運維中的使用增加，如何防止它未經授權讀取檔案、外洩憑證或產生失控的網路流量，成為一個亟待解決的問題。通用的容器運行環境往往缺乏專門針對 Agent 行為的細緻管控。  

🧪 **OpenShell 的核心設計**  
OpenShell 提供一個沙箱化的執行環境，專門設計來保護你的資料、憑證與基礎設施。其安全管控採用宣告式的 YAML 政策，可明確禁止未授權的檔案存取、資料外洩與不受控的網路活動。專案採用「agent‑first」的理念，內建了從網關故障排除到政策生成等多種 Agent 技能，並鼓励社群貢獻擴充。  

📦 **宣告式 YAML 政策與內建 Agent 技能**  
- 透過 YAML 檔案定義存取權限與網路規則，讓政策易於閱讀與版本控制。  
- 隨附預設的 Agent 技能，涵蓋 gateway troubleshooting 與 policy generation 等場景，開發者可直接使用或在此基礎上擴充。  
- 目前處於 Alpha 階段，單人模式（one developer, one environment, one gateway），旨在讓個人先跑通環境，之後將朝多租戶企業部署發展。  

🚀 **如何在本機快速啟動**  
- **先決條件**：支援的宿主作業系統（macOS、Windows WSL 2 或 Linux），以及本地執行時環境（Docker、Podman 或已啟用 MicroVM 沙箱的主機虛擬化）。  
- **安裝方式**（任選其一）：  
  1. 二進位安裝（推薦）：`curl -LsSf https://raw.githubusercontent.com/NVIDIA/OpenShell/main/install.sh | sh`  
  2. 透過 PyPI（需要 uv）：`uv tool install -U openshell`  
- 若需指定版本，可設定環境變數 `OPENSHELL_VERSION` 或使用 `uv tool install openshell==<version>`。  
- 亦提供追蹤 `main` 分支的開發版，以及實驗性的 Helm chart（Kubernetes 部署路徑仍在積極開發中，預期會有變動）。  

⚠️ **目前仍為 Alpha，粗邊待磨**  
- 此為早期版本，預期會有粗糙的邊緣與可能的變更。  
- 文件明確說明「Expect rough edges」並提醒使用者做好準備。  
- 多租戶企業部署仍在規劃中，當前焦點是讓單一開發者能夠快速啟動自己的沙箱環境。  

🎯 **適合想安全實驗自主 Agent 的開發者**  
- 如果你需要一個可安裝、可透過 YAML 政策細緻管控的沙箱來測試或擴充 AI Agent，OpenShell 提供了現成的二進位與套件安裝方式。  
- 內建的 Agent 技能降低了起手門檻，而開放的政策讓你可以依照自身需求調整安全邊界。  
- 專案來自 NVIDIA，並在 GitHub Trending 上獲得關注，適合作為安全 Agent 開發的起點。  

🔗 **論文連結**  
📂 **專案**：NVIDIA/OpenShell  
🔗 **GitHub**：https://github.com/NVIDIA/OpenShell  

你有試過在本機 sandbox 裡跑 AI Agent 嗎？歡迎在留言區分享你的體驗或政策設定技巧 👇  

#NVIDIA #OpenShell #AIAgents #Sandbox #Security #開源 #DevOps #CloudNative
