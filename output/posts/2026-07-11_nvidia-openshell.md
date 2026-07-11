---
title: NVIDIA/OpenShell
source: GitHub Trending
url: https://github.com/NVIDIA/OpenShell
score: 117
model: google/gemma-4-31b-it:free
generated_at: '2026-07-11T09:24:34.827350'
---

📌 NVIDIA OpenShell：為自主 AI Agent 提供安全沙箱執行環境  

TL;DR：OpenShell 讓 AI Agent 在受控的 YAML 政策下於本機或容器中執行，保護資料與網路，現在可用 Docker/Podman 安裝，適合想自行部署單一環境的開發者。  

在「AI Agent」逐漸成為服務核心的今天，最常被忽視的卻是執行時的安全與資料隔離。NVIDIA 直接釋出 OpenShell，提供一套以宣告式 YAML 政策防止未授權檔案存取、資料外洩與任意網路活動的沙箱機制，讓開發者可以在自己的機器上快速驗證 Agent，而不必擔心對基礎設施造成風險。  

🧩 **安全沙箱的核心設計**  
- **宣告式 YAML 政策**：使用者在 YAML 檔案中定義允許的檔案路徑、網路端點與憑證存取範圍，執行時由 OpenShell 依政策強制隔離。  
- **MicroVM‑backed 沙箱**：在支援的主機（macOS、WSL2 Windows、Linux）上，OpenShell 會透過 Docker、Podman 或本機虛擬化建立輕量 MicroVM，確保即使 Agent 嘗試逃逸也會被限制。  
- **Agent‑first 架構**：專案內建多項「skill」——例如閘道器故障排除、政策自動產生等——讓開發者直接帶著自己的 Agent 進入沙箱，無需額外撰寫安全層。

📦 **快速上手方式**  
1. **先備條件**：支援的作業系統 + Docker/Podman（或啟用本機虛擬化）。  
2. **二進位安裝（建議）**：  
   ```bash
   curl -LsSf https://raw.githubusercontent.com/NVIDIA/OpenShell/main/install.sh | sh
   ```  
3. **PyPI 安裝（需 uv）**：  
   ```bash
   uv tool install -U openshell
   ```  
   - 若想固定版本，可設定 `OPENSHELL_VERSION`（二進位）或在 `uv tool install` 後加上 `openshell==<version>`。  
4. **開發版**：亦提供追蹤 `main` 分支的 dev 版，可自行決定是否安裝。  

⚙️ **部署選項**  
- **單機模式**：目前僅支援「single‑player」模式，適合個人或小團隊測試。  
- **Kubernetes Helm Chart**：實驗性支援，仍在積極開發中，未來目標是支援多租戶企業部署。  

💡 **實務啟示**  
- 若你正開發需存取內部憑證或敏感資料的 AI Agent，先以 OpenShell 的沙箱跑一次，確保政策正確阻斷非授權的檔案與網路行為。  
- 由於目前仍是 Alpha 版，預期會有「rough edges」與破壞性變更，建議在正式環境前先在測試機上驗證升級流程。  
- 透過內建的 skill，你可以快速產生政策範本，減少手動撰寫 YAML 的錯誤機率。  

🔗 來源  
- 標題：NVIDIA/OpenShell  
- 作者／機構：NVIDIA — NVIDIA  
- 連結：https://github.com/NVIDIA/OpenShell  

#OpenShell #NVIDIA #AIAgents #Sandbox #Security #MicroVM #Docker #Podman #Kubernetes #YAMLPolicy #DevOps
