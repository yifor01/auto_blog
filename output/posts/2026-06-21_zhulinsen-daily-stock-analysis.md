---
title: ZhuLinsen/daily_stock_analysis
source: GitHub Trending
url: https://github.com/ZhuLinsen/daily_stock_analysis
score: 84
model: google/gemma-4-31b-it:free
generated_at: '2026-06-21T19:49:33.145713'
---

📌 **多市場 AI 股票分析系統：從資料聚合到自動化推送的完整實作**

TL;DR：一個整合多國股市資料與 LLM 的分析系統，支援自動生成決策報告並推送至多種通訊軟體。

對於量化交易者或個股投資者來說，最痛苦的往往不是缺乏資料，而是在海量的新聞、K 線與基本面資料中提取「可執行」的結論。當分析流程需要跨越多個網站且重複性極高時，自動化就成了剛需。

🧩 **多市場資料聚合與 AI 決策報告**

此專案建構了一個智慧分析系統，將市場行情與 AI 洞察結合，核心功能包含：

- **全方位決策報告**：AI 會產出包含核心結論、評分、趨勢分析、買賣點位、風險警報、催化因素及操作檢查清單的完整報告。
- **廣泛的市場覆蓋**：支援 A 股、港股、美股、ETF 以及日股（.T）與韓股（.KS / .KQ）。
- **資料維度**：聚合行情、K 線、技術指標、資金流、籌碼、新聞、公告與基本面。其中日韓股市主要透過 YFinance 提供日線與基礎行情，部分高階功能（如資金流、龍虎榜）會依市場邊界降級為不支援。

🤖 **靈活的 Agent 策略與模型整合**

系統不只是簡單的資料彙整，還引入了 Agent 機制來強化分析深度：

- **15 種內建策略**：支援均線、纏論、波浪、趨勢、熱點、事件、成長、預期等多種分析策略，可用於多輪追問。
- **模型高度相容**：支援 DeepSeek、Claude、Gemini、OpenAI 相容介面、通義千問以及 Ollama 本地模型。
- **搜尋與輿情整合**：整合 SerpAPI、Tavily、Brave 等搜尋工具，並可選配 Reddit、X、Polymarket 的社交輿情分析（僅限美股）。

⚙️ **自動化部署與推送流程**

開發者提供了多種部署路徑，讓使用者能快速將分析流程自動化：

- **部署方式**：支援 GitHub Actions（零成本、無需伺服器）、Docker、本地定時任務或 FastAPI 服務。
- **推送渠道**：分析結果可自動推送至企業微信、飛書、Telegram、Discord、Slack 或電子郵件。
- **互動介面**：提供 Web/桌面工作臺，可用於手動分析、檢視歷史報告、回測持倉及管理配置。

🎯 **實務啟示**

對於想要實作 AI 投資助手的工程師，這個專案提供了一個完整的「資料獲取 $\rightarrow$ AI 處理 $\rightarrow$ 自動推送」管線參考。特別是其對多個資料源（如 AkShare, YFinance, Tushare）的整合方式，以及利用 GitHub Actions 實現零成本定時分析的設計，是快速搭建個人金融監控系統的有效路徑。

🔗 **來源**
- 標題：daily_stock_analysis
- 作者／機構：ZhuLinsen
- 連結：https://github.com/ZhuLinsen/daily_stock_analysis

#StockAnalysis #AI #LLM #GitHubActions #QuantitativeTrading #FinancialAI #OpenSource #TradingBot #MarketAnalysis #Automation
