---
title: HKUDS/Vibe-Trading
source: GitHub Trending
url: https://github.com/HKUDS/Vibe-Trading
score: 80
model: google/gemma-4-31b-it:free
generated_at: '2026-06-27T19:37:32.268121'
---

📌 **【HKUDS】Vibe-Trading：將交易能力整合進 AI Agent 的開源交易框架**

TL;DR：一個讓 AI Agent 透過單一指令即可獲得完整交易能力、支援影子帳戶與多市場資料路由的開源框架。

目前的 AI Agent 雖然能分析資料，但要將分析轉化為實際的交易執行，通常需要複雜的 API 整合與邏輯對接。Vibe-Trading 旨在簡化這個過程，讓開發者能快速為 Agent 賦能，使其具備全面的交易能力。

🧩 **核心功能與設計理念**

Vibe-Trading 採取模組化設計，讓 Agent 能透過簡單指令執行交易任務。其核心能力包含：
- **影子帳戶 (Shadow Account)**：支援規則提取與程式碼生成，讓 Agent 能在模擬環境中驗證交易邏輯。
- **訊號引擎 (SignalEngine)**：能將提取的交易規則轉化為實際進入條件（例如 RSI 範圍、先前報酬率範圍），而非單純重複持倉節奏。
- **多市場資料路由**：透過 tushare loader 實現精準的資料導向，根據標的型別自動分流：
    - ETF/LOF $\rightarrow$ `fund_daily()`
    - 指數 (Indices) $\rightarrow$ `index_daily()`
    - 香港股票 $\rightarrow$ `hk_daily()`
    - 一般股票 $\rightarrow$ `daily()`
    （此設計解決了先前呼叫通用 `daily()` 函式時，非股票標的會靜默回傳空值的問題）。

💡 **近期技術改良：提升穩定性與精準度**

根據專案更新日誌，開發團隊近期針對以下實務問題進行了最佳化：
- **對抗內容過濾 (Content-filter resilience)**：在事件驅動 (event-driven) 與 Swarm 執行模式下，跳過單次 LLM 的內容審核攔截，並在過濾率過高時發出警告，且能識別 Gemini 的安全終止原因，避免整個分析流程因此中斷。
- **防止精度損失**：將影子帳戶的提取與程式碼生成統一使用相同的 `PRICE_FEATURES` 合約，並將 `prior_5d_return`（前 5 日報酬率）維持在小數四位數，防止規則與程式碼之間產生偏差。

🎯 **實務啟示**

對於開發交易 Agent 的工程師來說，Vibe-Trading 提供了兩個值得參考的實作方向：
1. **資料路由的嚴謹性**：在處理金融資料時，針對不同資產類別（ETF、指數、個股）使用專屬 API 介面，比使用通用介面更能有效避免空值回傳導致的分析錯誤。
2. **LLM 容錯處理**：針對 LLM 內建的安全過濾機制，透過識別特定終止原因（如 Gemini safety finish reasons）而非直接中斷程式，能顯著提升自動化交易分析的連續性。

🔗 **來源**
- 標題：Vibe-Trading: Your Personal Trading Agent
- 作者／機構：HKUDS
- 連結：https://github.com/HKUDS/Vibe-Trading

#AI #TradingBot #OpenSource #LLM #QuantitativeTrading #Agent #Python #Tushare #FinTech #HKUDS
