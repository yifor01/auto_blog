---
title: TauricResearch/TradingAgents
source: GitHub Trending
url: https://github.com/TauricResearch/TradingAgents
score: 99
model: tencent/hy3:free
generated_at: '2026-07-14T07:58:16.844262'
---

📌 【開源專案】TradingAgents：整合多種 LLM 與資料來源的金融交易多代理人框架

TL;DR：一個支援多種模型與資料供應商，用於金融交易的多代理人 (Multi-Agents) 開源框架。

隨著大型語言模型 (LLM) 在決策任務中的表現日益精進，如何將 LLM 的推理能力與即時金融資料結合，成為開發自動化交易系統的關鍵。TauricResearch 推出的 TradingAgents 專案，正是為了實現這一目標而設計的框架。

🧩 **結構化決策的多代理人架構**

根據專案說明，TradingAgents 採用了結構化輸出 (Structured-output) 的代理人設計，主要包含以下核心角色：
- Research Manager (研究經理)
- Trader (交易員)
- Portfolio Manager (投資組合經理)

該框架利用 LangGraph 技術來管理代理人流程，並支援 Checkpoint resume 功能，讓交易決策過程具備可恢復性。

📊 **廣泛的模型與資料供應商支援**

TradingAgents 的強項在於其極高的相容性，能與當前主流的 AI 模型與金融資料來源進行整合：

**模型供應商 (Model Providers)：**
- 包括 OpenAI (支援 GPT-5.4/5.5 等系列)、NVIDIA、Kimi、Groq、Mistral、Bedrock、Azure、DeepSeek、Qwen、GLM、MiniMax、Fable 5 以及遠端 Ollama。

**資料供應商 (Data Vendors)：**
- 支援 Alpha Vantage、FRED、Polymarket 以及加密貨幣情緒來源 (Crypto sentiment sources)。

🚀 **持續演進的穩定性與安全性**

從專案更新紀錄來看，該框架正快速迭代以解決金融交易中的核心問題：
- **資料準確性**：包含 Alpha Vantage 的 look-ahead filtering（預視過濾）以及回測時的日期保真度 (Backtesting date fidelity)。
- **穩定性最佳化**：包含 graph-router 的崩潰防護 (crash-safety)、圖形形狀感知 (graph-shape-aware) 的檢查點恢復，以及可配置的 LLM 重試預算 (LLM retry budget)。
- **安全性與環境配置**：強化了 Ticker 路徑穿越 (path-traversal) 的防護，並支援透過環境變數進行 API Key 的自動偵測。

🎯 **實務啟示**

對於想要開發 AI 交易策略的工程師來說，TradingAgents 提供了一個標準化的「元件庫」，你不需要從零開始處理不同 API 的格式轉換或代理人間的溝通邏輯，只需透過配置即可快速整合最新的 LLM 模型與金融資料流。

🔗 **來源**
- 標題：TauricResearch/TradingAgents
- 連結：https://github.com/TauricResearch/TradingAgents

#AI #LLM #MultiAgent #FinTech #TradingAgents #OpenSource #LangGraph #AlgorithmicTrading #Python #MachineLearning
