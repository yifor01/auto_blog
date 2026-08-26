---
title: 'Granite 4.2 LLMs: How They''re Built'
source: HuggingFace Blog
url: https://huggingface.co/blog/ibm-granite/granite-4-2
model: claude-code/sonnet
generated_at: '2026-08-26T06:21:52.878249'
score: 105
---

📌 拆解 Granite 4.2：IBM 官方揭露五階段預訓練與多環境 RL 管線全貌

TL;DR：IBM Granite 團隊親自撰文說明 Granite 4.2 的架構、訓練配方與 RL pipeline 細節，是理解這個開源推理模型家族「怎麼做出來的」第一手資料。

多數模型發布只給結果，很少公開到「哪一階段的學習率是多少」這種細節。Granite 團隊這篇技術文章罕見地把整條生產線攤開來講。

🤔 從指令跟隨到明確推理

Granite 4.2 是 Granite 家族第一批密集、decoder-only 的推理模型，3B、8B、30B 三個尺寸共用同一套架構設計與訓練流程（預訓練→SFT→多階段 RL），只是各自在自己的規模上跑一遍。每個模型都能產生 chain of thought，支援 thinking／non-thinking 切換，外加一個介於兩者之間、只花少量推理預算處理簡單問題的低努力模式，並原生支援 tool calling——透過 vLLM 等 OpenAI 相容端點服務時，會以 OpenAI function-calling 格式輸出工具呼叫，可直接接入現有 agent harness，另外也支援 SGLang。

🧩 架構細節：GQA + RoPE + SwiGLU 的密集 transformer

三個尺寸的核心組件一致：40 個 attention heads 搭配 8 個 KV heads 的 Grouped Query Attention、θ = 10,000,000 的 RoPE、SwiGLU 啟動的 MLP、RMSNorm（ε = 1e-5）、未綁定的輸入輸出 embedding、bfloat16 精度。具體來看，3B 為 40 層、embedding size 2560、attention head size 64、MLP hidden size 8192；8B 同為 40 層但 embedding size 4096、attention head size 128、MLP hidden size 12800；30B 則是 64 層、embedding size 4096、MLP hidden size 32768。三者序列長度都標示為 131,072（128K）。

🧪 預訓練與 SFT：15 兆 token、720 萬筆樣本

預訓練從零開始，約 15 兆 token，採五階段策略：第 1-2 階段是基礎預訓練，第 3-4 階段是逐步提高資料品質的「退火」式中期訓練，第 5 階段引入長上下文訓練，把上下文窗口延伸到 512K token。每個階段各有獨立的資料混合比例與學習率排程，整體趨勢是從廣泛的網路資料逐漸轉向更精煉的高品質來源。

SFT 階段的資料混合為 agentic 31.6%、非 agentic 68.4%，共約 720 萬筆樣本、約 1000 億 token（約 650 億可訓練）。agentic 語料涵蓋軟體工程（SWE，69%）、tool calling（12.1%）、終端機操作（8.0%）、數學（3.5%）、搜尋（0.8%）、行動（0.2%），由 OpenHands、OpenCode、Terminus-2、SWE-agent、OpenResearcher、MiniSWE、OpenSeeker、EnvScaler、Gemini CLI、Hermes、Codex、Goose 等多種 agent scaffold 與 harness 產生，並混合開源資料集與自研合成 RL 環境。非 agentic 語料則包含指令跟隨（18.8%）、程式碼（18.8%）、數學（14.6%）、多語言（7.0%）、科學（5.4%）、推理（3.0%）、安全（0.8%）。

資料品質控管分多道關卡：先統一格式化成 OpenAI Chat 格式，再用 GPT-OSS-120B 與 Gemma 4 作為 LLM 評審過濾低分樣本、幻覺內容、無效工具呼叫，接著套用特定資料集的啟發式規則，最後以 tools 與 messages 欄位的 SHA-256 雜湊做本地與全域去重。

訓練配置方面，序列打包長度 131,072、全域 batch size 128、學習率 warm-up 後維持在 1.0e-5 常數（第二階段為 3.0e-6）、warm-up 佔 2.5% 訓練步數，訓練約跑 2 個 epoch，並行策略為 TP=2、PP=1、CP=4 或 CP=2，動用 32 至 128 個節點（依模型大小），每節點 4 張 Grace/GB200。30B 模型額外多跑一輪針對 agentic coding 的第二階段 SFT，把 agentic、SWE、程式碼資料上採樣，同時保留約 16% 原始 SFT 語料作為 replay，再以 3.0e-6 的較低學習率額外訓練約一個 epoch。

📊 後訓練：多階段、多環境 RL pipeline

SFT 之後接上一條多階段、多環境的強化學習管線，逐步把模型從「會回答」推進到「能在真實環境裡採取行動」。

⚠️ 限制

文章截至目前段落尚未公布完整的評測結果數據，實際基準測試表現仍待官方後續補充。

🎯 實務啟示

這篇文章對想要複製或微調 agentic 訓練流程的團隊很有參考價值：資料混合比例、去重方法、多階段 RL 的 warm-start 策略都寫得相當具體，尤其是「agentic RL 只作用在 8B/30B」這個分工，說明了在資源有限時，把工具使用能力集中訓練在較大模型上是務實的取捨。

🔗 來源
- 標題：Granite 4.2 LLMs: How They're Built
- 作者／機構：Granite Team, IBM（Yousaf Shah、Swanand Kadhe、Riddhiman Moulick、Ashish Sunil Agrawal）
- 連結：https://huggingface.co/blog/ibm-granite/granite-4-2

#IBM #GraniteLLM #ReasoningModels #LLMTraining #ReinforcementLearning #SFT #AgenticAI #OpenSourceAI #TransformerArchitecture #MachineLearning
