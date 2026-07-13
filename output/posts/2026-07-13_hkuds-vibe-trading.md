---
title: HKUDS/Vibe-Trading
source: GitHub Trending
url: https://github.com/HKUDS/Vibe-Trading
score: 89
model: google/gemma-4-31b-it:free
generated_at: '2026-07-13T08:58:46.189924'
---

📌 Vibe‑Trading：一鍵式個人化交易代理，提供完整交易功能

TL;DR：Vibe‑Trading 是 HKUDS 開源的全功能交易機器人，支援 API、沙盒回測與多帳號，近期完成外部安全審計並加強硬化。

🧩 **完整交易代理、誰在用**

Vibe‑Trading 以「Your Personal Trading Agent」自居，讓使用者只需一條指令就能啟動具備下單、回測、帳號管理等功能的交易代理。README 中列出網站、檔案、示範與快速上手等資源，顯示其定位為即插即用的開發者與量化交易者工具。

📊 **近期安全硬化與功能更新**

- 2026‑07‑13 完成外部安全審計，所有 10 項審計缺失已在 `main` 分支修復（issue #476、discussion #468）。  
- Docker 採用多階段建置並鎖定映像檔摘要，確保建置環境可重現。  
- 回測沙箱使用 AST 硬化，阻斷網路、子程式、`eval`、環境變數與不安全檔案開啟，甚至在巢狀函式內同樣生效。  
- SSE（Server‑Sent Events）認證票證改為短期單次使用，提升即時資料傳輸安全。  
- Docker Compose 以唯讀根檔系統、移除多餘許可權並加入資源限制，加強容器防護。  
- `/correlation` API 加入驗證與速率限制，防止濫用。  
- 依賴套件使用雜湊鎖定，避免供應鏈攻擊。

⚙️ **核心功能亮點**

- **API / MCP**：提供統一介面讓外部系統呼叫下單、查詢與回測。  
- **Shadow Account**：支援虛擬帳號，方便測試與策略驗證。  
- **回測指標**：新增投資組合換手率於回測報表（#478），協助使用者評估策略實際交易成本。  
- **學術因子**：內建 Frazzini‑Pedersen 「betting‑against‑beta」因子（Alpha Zoo → 461），讓策略可直接引用已驗證的市場因子。  
- **TAP 模式**：可選擇性啟用 Alpaca 金鑰隔離（#377），提升金鑰管理安全性。  
- **即時示範**：提供 Demo 與 Quick‑Start，降低新手上手門檻。

⚠️ **安全警示**

README 明確提醒：X 帳號 `VibeTrading_HKU`、Virtuals 專案 `101845` 以及代幣合約 `0x640BDBF77b6447E8b7DB7894cED84BD1c40571f4` 均非官方資產，開發團隊未發行或背書任何代幣或 meme‑coin。使用者應避免購買、連線錢包或簽署相關交易。

🎯 實務啟示

- **快速原型**：開發者可透過 Docker 多階段映像直接部署，利用 Shadow Account 先行驗證策略，再切換至實盤。  
- **安全優先**：沙盒回測的 AST 硬化與容器硬化措施，適合對安全有高要求的金融機構或對外部資金管理平臺。  
- **策略擴充**：內建 Frazzini‑Pedersen 因子與投資組合換手率指標，讓量化研究者能快速加入學術因子與成本評估，減少自行實作負擔。

🔗 來源
- 標題：HKUDS/Vibe‑Trading
- 作者／機構：HKUDS
- 連結：https://github.com/HKUDS/Vibe-Trading

#VibeTrading #OpenSource #QuantTrading #Backtesting #Docker #Security #API #Alpaca #FrazziniPedersen #TradingAgent #CryptoSafety
