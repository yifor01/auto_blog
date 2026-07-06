---
title: TauricResearch/TradingAgents
source: GitHub Trending
url: https://github.com/TauricResearch/TradingAgents
score: 91
model: google/gemma-4-31b-it:free
generated_at: '2026-07-06T20:30:36.232452'
---

📌 【開源專案】TradingAgents：建構多代理 LLM 金融交易框架

TL;DR：一個支援多模型、多資料來源且具備決策記錄與回測功能的 LLM 金融交易多代理框架。

在金融交易中，單一 LLM 往往難以同時兼顧研究、交易執行與資產配置。如何將複雜的交易流程拆解成不同職能的代理（Agents）協作，並確保資料獲取的正確性，是目前開發交易 AI 的核心挑戰。

🧩 **以職能分工的結構化代理設計**

TradingAgents 採用多代理（Multi-Agents）架構，將交易流程拆分為具備特定職能的結構化代理，包括：
- Research Manager：負責研究分析。
- Trader：負責執行交易。
- Portfolio Manager：負責管理投資組合。

此外，系統整合了 LangGraph 的 checkpoint resume 功能，允許在執行過程中恢復狀態，並提供持久化的決策日誌（persistent decision log）以追蹤交易邏輯。

📊 **廣泛的模型支援與資料整合**

該框架在模型相容性與資料獲取上具有高度彈性：
- 模型支援：涵蓋 GPT-5.5、Claude Sonnet 5、Fable 5、DeepSeek、Qwen、GLM、MiniMax、Mistral 以及任何 OpenAI 相容的端點，並支援遠端 Ollama。
- 資料供應商：整合了 Alpha Vantage（含 look-ahead 過濾）、FRED、Polymarket 及加密貨幣情緒分析來源。
- 基礎設施：提供 Docker 支援、環境變數配置（TRADINGAGENTS_*）以及 API-key 自動偵測。

💡 **針對交易穩定性的技術最佳化**

為了提升在金融場景下的可靠度，專案在近期更新中強化了多項穩定性機制：
- 資料正確性：實作了經過驗證的資料存取合約（verified data-access contract）與 ticker 路徑遍歷強化（path-traversal hardening）。
- 系統魯棒性：引入 graph-router 崩潰安全機制、可配置的 LLM 重試預算（retry budget），以及能感知圖形形狀（graph-shape-aware）的檢查點恢復功能。
- 回測精度：針對回測的日期忠實度（date fidelity）進行了最佳化，確保模擬結果更接近真實情況。

🎯 **實務啟示**

對於想要開發 AI 交易系統的工程師，該專案提供了將「研究 $\rightarrow$ 決策 $\rightarrow$ 執行」流程模組化的參考實作。特別是其對多模型（Multi-LLM）的整合與對資料洩漏（Look-ahead bias）的過濾處理，是建構金融 AI 系統時必須考慮的工程細節。

🔗 **來源**
- 標題：TauricResearch/TradingAgents
- 作者／機構：TauricResearch
- 連結：https://github.com/TauricResearch/TradingAgents

#AI #LLM #QuantitativeTrading #MultiAgent #LangGraph #FinancialAI #OpenSource #TradingBot #FinTech #MachineLearning
