---
title: TauricResearch/TradingAgents
source: GitHub Trending
url: https://github.com/TauricResearch/TradingAgents
score: 85
model: google/gemma-4-31b-it:free
generated_at: '2026-06-28T19:26:16.743125'
---

📌 TradingAgents：支援多模型與多 Agent 的金融交易框架

TL;DR：一個整合多個 LLM 供應商與金融資料來源，透過多 Agent 協作實現交易決策的開源框架。

在金融交易中，單一模型往往難以兼顧研究、執行與風控，而 TradingAgents 試圖透過多 Agent 協作架構，將不同職能的 LLM 串聯起來，打造一個可配置的自動化交易流程。

🧩 **多 Agent 職能分工與結構化輸出**

根據專案更新紀錄，該框架定義了明確的 Agent 角色，並透過結構化輸出（Structured-output）來確保決策的穩定性，核心角色包含：
- Research Manager：負責研究管理。
- Trader：負責執行交易。
- Portfolio Manager：負責投資組合管理。

此外，系統整合了 LangGraph 的 checkpoint 功能，支援中斷後的恢復（resume），並配備持久化決策日誌（persistent decision log），讓交易邏輯具備可追溯性。

🌐 **極廣的模型相容性與資料對接**

TradingAgents 採取開放的供應商策略，旨在讓工程師能快速切換最適合的模型：
- 模型支援：涵蓋 GPT-5.x 系列、Gemini 3.x、Claude 4.x、Grok 4.x，以及 DeepSeek、Qwen、GLM、MiniMax 等模型。
- 供應商介面：支援 NVIDIA、Kimi、Groq、Mistral、Bedrock 及所有 OpenAI 相容的端點，並支援遠端 Ollama 與 Azure。
- 資料來源：整合了 FRED 與 Polymarket 等資料供應商，並提供驗證過的資料存取合約（verified data-access contract）。

⚙️ **工程實作與部署細節**

- 配置靈活性：透過 `TRADINGAGENTS_*` 環境變數進行配置，並支援 API key 的自動偵測。
- 部署與相容性：提供 Docker 映像檔以簡化部署，並針對 Windows 的 UTF-8 編碼問題進行了修復。
- 穩定性提升：匯入 CI gate 確保程式碼品質，並針對 ticker 路徑遍歷（path-traversal）進行了安全性加固。

🎯 **實務啟示**

對於想建構 AI 交易系統的工程師，TradingAgents 提供了一個成熟的「骨架」。其價值在於將模型接入、資料獲取、Agent 分工以及狀態管理（Checkpoint）這些基礎工程問題預先解決，開發者可以將重心放在調整交易策略與 Prompt 最佳化，而非底層的 API 串接。

🔗 **來源**
- 標題：TauricResearch/TradingAgents
- 作者／機構：TauricResearch
- 連結：https://github.com/TauricResearch/TradingAgents

#LLM #MultiAgent #AlgorithmicTrading #FinancialAI #LangGraph #OpenSource #TradingBot #QuantitativeAnalysis #FinTech #AIFramework
