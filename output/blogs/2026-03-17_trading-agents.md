---
title: "用 LLM 組一支交易團隊——TradingAgents 把華爾街的分工搬進你的 terminal"
date: "2026-03-17"
paper_url: "https://github.com/TauricResearch/TradingAgents"
paper_title: "TauricResearch/TradingAgents"
tags: [Agent, Trading, LLM, Multi-Agent, Finance]
tldr: "多 Agent 金融交易框架，模擬真實交易室分工"
---

投資銀行的交易樓層不是一個人在做決定。有人盯基本面，有人讀新聞，有人看 K 線，有人專門唱反調，最後由 portfolio manager 拍板。TradingAgents 這個開源框架做的事情，就是用 LLM agent 把這整套分工搬進程式碼裡。我花了一個小時翻了 repo，架構設計確實比大多數「LLM 做交易」的 side project 認真。但有一個很大的問題我必須先說：它沒有公布任何回測績效數據。

🏗️ 五層 Agent，模擬一間交易公司

整個 pipeline 拆成五層，每層都是獨立的 LLM agent：

第一層 Analyst Team，四個分析師各看不同維度。Fundamentals Analyst 看財報硬數字，Sentiment Analyst 讀市場情緒，News Analyst 追即時新聞事件，Technical Analyst 看均線和技術指標。四個人各寫各的分析報告，互相不干擾。

第二層 Researcher Team，這裡的設計最有意思。它不是把四份報告合在一起做摘要，而是刻意安排了一場多空辯論。一個 Bullish agent 和一個 Bearish agent 各自根據分析師的報告提出論點，互相挑戰對方的邏輯。

為什麼這樣做？因為 LLM 最常見的問題之一就是 confirmation bias，一旦產生了初步判斷，後續推理會一路順著那個方向滑下去。對立辯論至少逼模型考慮反面證據。這個想法不新（constitutional AI 裡也有類似的 red-teaming 概念），但用在金融決策的脈絡裡算是蠻合理的。

第三層 Trader Agent，把辯論結論轉化成具體建議，包括什麼時候進場、部位多大、停損停利設在哪。第四層 Risk Management 做風控檢查。第五層 Portfolio Manager 最後一道關卡，有權 approve 或 reject。

技術棧：Python 3.13，LangGraph 做 agent 編排，Alpha Vantage 串市場數據。

🔧 模型選擇很彈性

LLM 支援很開放，GPT-5.x、Gemini 3.x、Claude 4.x、Grok 4.x 都能用，也可以透過 OpenRouter 或 Ollama 跑本地模型。最新的 v0.2.1（2026 年 3 月）支援到 GPT-5.4、Gemini 3.1、Claude 4.6。

比較聰明的設計是區分了「deep thinking」和「quick thinking」兩種模型配置。需要深度推理的 agent（像 Researcher 辯論）用比較強的模型，制式步驟（像 Risk Management 檢查規則）用便宜快的模型。API 帳單差很多，這在實際使用中是很重要的考量。

🚨 最大的問號：績效數據在哪裡

這是我必須很直白說的：TradingAgents 沒有公開任何回測數字。沒有 Sharpe ratio，沒有 maximum drawdown，沒有跟 buy-and-hold 的比較。repo 的 README 也明確寫了「not financial advice」。

在量化交易領域，一個框架不拿數字說話，基本上就只是架構展示。你可以說 agent 分工設計很漂亮，但漂亮的架構不等於能賺錢。多空辯論聽起來合理，但如果最後 Portfolio Manager 的決策品質跟隨機差不多，那整套系統就是一個精緻的隨機數產生器。

我不是說它一定沒用，而是在沒有數字的情況下，沒辦法判斷它到底有沒有用。

另一個讓我猶豫的點：LLM 對即時性金融數據的理解能力到底有多好？模型訓練的 knowledge cutoff 是固定的，它怎麼正確解讀一份它從沒看過的財報格式？Analyst Agent 依賴 Alpha Vantage 的結構化數據還好，但 News Agent 和 Sentiment Agent 要處理的是非結構化的即時資訊，hallucination 風險不低。

🤔 那它的價值是什麼

我覺得 TradingAgents 的價值不在「能不能拿來賺錢」，而在「multi-agent 系統設計的參考實作」。

幾個設計模式值得偷：

→ agent 之間的分工與資訊流，怎麼讓多個 agent 各自分析再匯聚成決策
→ 對立辯論機制，這是目前處理 LLM confirmation bias 比較有效的方法之一
→ LangGraph 在多步驟 agent 編排的實際應用
→ deep/quick thinking 的模型分層，不是每個 agent 都需要最貴的模型

如果你在做任何「多角度分析再決策」的 agent 系統，不管是投資研究、風險評估還是內容審核，這些模式都可以參考。

但如果你真想拿它來交易？先自己跑 backtest。一個連自己都不公布績效的交易系統，不應該把真金白銀交給它。

多空辯論真的能提升決策品質，還是只是把同一個模型的 uncertainty 用更貴的方式展現出來？這是我想了一陣子還沒想通的問題。

🔗 GitHub：https://github.com/TauricResearch/TradingAgents

<!-- fb -->

投資銀行的交易樓層不是一個人在做決定。TradingAgents 用 LLM agent 把這整套分工搬進程式碼：四個 Analyst 各看基本面/情緒/新聞/技術面 → Bullish vs Bearish 多空辯論 → Trader 下單建議 → Risk Management 風控 → Portfolio Manager 拍板。

🔧 支援 GPT-5.x、Gemini 3.x、Claude 4.x，還能 Ollama 跑本地。區分 deep/quick thinking 模型配置控制 API 成本。

🚨 最大問號：沒有任何回測績效數據。沒有 Sharpe ratio、沒有 drawdown、沒有跟 buy-and-hold 的比較。漂亮的架構不等於能賺錢。

🤔 真正的價值在 multi-agent 系統設計：agent 分工模式、對立辯論處理 confirmation bias、LangGraph 編排、模型分層策略。做「多角度分析再決策」的 agent 系統都值得參考。

但想拿來交易？先自己跑 backtest 再說。

#GenAI #Agent #Trading #MultiAgent #LLM #Finance #LangGraph
