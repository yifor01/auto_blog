---
title: microsoft/mxc
source: GitHub Trending
url: https://github.com/microsoft/mxc
score: 76
model: google/gemma-4-31b-it:free
generated_at: '2026-07-13T09:10:40.061424'
---

📌 Microsoft eXecution Container (MXE) — 跨平臺沙盒執行框架的早期預覽  

TL;DR：MXC 讓開發者以統一的 JSON 設定與 TypeScript SDK，在 Windows、Linux、macOS 上以多種沙盒或 VM 後端安全執行不受信任程式碼，仍屬預覽版、政策仍會調整。

在開發 AI 產出或外掛時，常需要把外部模型或工具的程式碼隔離執行，避免對主機系統造成風險。Microsoft 最近將其自研的 Execution Container（MXC）開源，提供一套跨平臺、可自訂的沙盒執行介面，讓開發者在同一套 JSON 配置下選擇不同的容器型別。

🧩 **跨平臺與多樣化容器後端**  
- 支援 Windows、Linux、macOS 三大作業系統。  
- 後端可從 OS 原生的「ProcessContainer」到完整 VM（如 MicroVM、Hyperlight）皆可透過同一介面呼叫。  
- 針對 macOS 使用 Seatbelt，Linux 則提供 LXC、Bubblewrap，Windows 有 Windows Sandbox 等。

🗂 **JSON‑Based Configuration**  
- MXC 使用版本化的 JSON schema 定義執行引數與安全政策。  
- 透過 TypeScript SDK，開發者可程式化產生或修改這些設定檔，實作「policy‑driven」的沙盒化。  
- 目前支援的政策專案包括檔案系統（只讀 / 可寫路徑清單）與網路存取，Windows 尚未支援拒絕路徑。

⚙️ **主要功能概覽**  
- **跨平臺**：一次撰寫配置，即可在三種 OS 上部署。  
- **多容器後端**：ProcessContainer、Windows Sandbox、LXC、Bubblewrap、Seatbelt、MicroVM、Hyperlight、IsolationSession、WSLC。  
- **政策驅動**：以 JSON 明確列出允許的檔案路徑與網路連線，降低程式碼在執行時的攻擊面。  

⚠️ **早期預覽的限制**  
- 目前的 sandbox 政策在某些情況下過於寬鬆，未來會在正式版前加以收緊。  
- 仍在持續開發中，底層容器實作可能變動，官方會盡量減少相容性衝擊。  
- 雖然歡迎安全研究者合作，但現階段的 MXC profile 不應被視為完整的安全邊界。  

🎯 **實務啟示**  
- 若你的應用需要在本機或 CI 環境中安全執行外部模型或外掛，MXC 提供了即時可用的 API 與配置範本，可快速驗證概念。  
- 由於仍是預覽版，建議先在測試環境中試跑，並留意未來的政策更新與容器後端變更。  
- 透過 JSON + TypeScript 的組合，開發團隊能把安全政策寫進 CI/CD 流程，實現自動化的沙盒部署。  

🔗 **來源**  
- 標題：microsoft/mxc  
- 作者／機構：Microsoft — microsoft  
- 連結：https://github.com/microsoft/mxc  

#MXC #Sandbox #CrossPlatform #Container #TypeScript #JSON #Security #Microsoft #VM #Linux #macOS #Windows
