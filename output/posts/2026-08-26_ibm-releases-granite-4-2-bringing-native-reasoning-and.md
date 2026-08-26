---
title: 'IBM Releases Granite 4.2: Bringing Native Reasoning and Agentic RL to Open
  Enterprise Models'
source: MarkTechPost
url: https://www.marktechpost.com/2026/08/25/ibm-releases-granite-4-2-bringing-native-reasoning-and-agentic-rl-to-open-enterprise-models/
model: claude-code/sonnet
generated_at: '2026-08-26T06:21:52.878023'
score: 111
---

📌 IBM Granite 4.2 開源上路：3B到30B全系列內建思考鏈與Agentic RL

TL;DR：IBM 以 Apache 2.0 釋出 Granite 4.2 推理模型家族，8B 與 30B 更額外訓練了能操作終端機、寫程式碼的 agentic 能力。

當多數企業級模型還在用「指令微調」包裝聊天機器人時，IBM 這次直接把 chain of thought 內建進模型骨架，還讓 8B 與 30B 版本在真實沙盒環境裡學會自己開終端機、跑網頁搜尋。這不是一次單純的版本升級。

🤔 從「會回答」到「會思考」的轉向

過去的 Granite 系列是強大的指令跟隨助理，Granite 4.2 則把明確推理（explicit reasoning）做成一等公民：每個模型都能在回答前先產生 chain of thought，並提供 thinking／non-thinking 切換開關，外加一個「低努力模式」，讓模型在簡單問題上只花少量推理預算，不浪費算力。

🧩 架構與訓練：15 兆 token 打底，多階段 RL 收尾

Granite 4.2 是 decoder-only 的密集 transformer，並非 MoE 或混合架構。核心組件包括 Grouped Query Attention（8 個 KV heads）、RoPE（θ = 10,000,000）、SwiGLU MLP、RMSNorm（ε = 1e-5）、未綁定（untied）的輸入輸出 embedding，以及 bfloat16 精度。3B 版本為 40 層、embedding size 2560；8B 同樣 40 層但 embedding size 拉到 4096；30B 則擴展到 64 層，MLP hidden size 達 32,768。官方架構表列出的序列長度為 131,072（128K）token，而五階段預訓練流程中，最後一階段更把上下文延伸到 512K token。

預訓練規模約為 15 兆 token，從零開始訓練。監督式微調（SFT）階段使用約 720 萬筆樣本、約 1000 億 token（其中約 650 億為可訓練 token），資料混合比例為 31.6% agentic、68.4% 非 agentic，agentic 資料中軟體工程（SWE）又佔了 69%。這些軌跡資料是透過 OpenHands、SWE-agent、Terminus-2、MiniSWE、Codex、Goose 等多種 harness 生成，並以 GPT-OSS-120B 與 Gemma 4 作為 LLM 評審把關品質，另外用 SHA-256 對 tools 與 messages 欄位做去重。

後訓練是一條多階段、多環境的強化學習鏈，而非單一 RL pass：每個階段都是獨立的非同步 GRPO 訓練，從前一個 checkpoint 熱啟動，用 leave-one-out baseline 取代價值網路，並以截斷重要性採樣（truncated importance sampling）限制 off-policy 偏移。順序依次為 RLVR、技能加強、SWE／終端機／搜尋，最後才是 RLHF。值得注意的是，agentic RL 這個區塊只套用在 8B 與 30B 上，3B 只接受基礎 RL 與對齊訓練——這個設計選擇也解釋了不同尺寸之間能力差距的主因。

訓練基礎設施使用 NeMo-RL 與 NeMo-Gym，跑在 CoreWeave 代管的 NVIDIA GB200 NVL72 叢集上，並搭配 IBM 自家 CodeAlchemy pipeline 產出的 1 兆 token 合成程式碼，以及推論端的推測解碼（speculative decoding）層加速服務。

📊 同場加映：470M 參數的語音模型

IBM 同步釋出兩個 4.7 億參數的 Granite Speech 5.0 Turbo CTC 模型，捨棄 LLM 骨幹，改用 connectionist temporal classification 直接把音訊映射到文字。IBM 表示在單張 H200 上的 RTFx 吞吐量接近 12,600，相較 Open ASR 排行榜目前速度領先者的約 6,000 有明顯提升，並提供 WebGPU 展示 demo。

🎯 實務啟示

三個尺寸皆採 Apache 2.0 授權，下載、微調、商業化生產都沒有授權門檻。對於需要在企業內部落地 agentic workflow（尤其是程式碼相關任務）的團隊，8B／30B 的 agentic RL 訓練資料組成（SWE 佔比極高）值得優先評估；若只是需要基礎推理與對齊能力，3B 也已足夠且成本更低。原生支援 OpenAI 相容的 function-calling 格式，理論上可直接接入既有 agent harness。

🔗 來源
- 標題：IBM Releases Granite 4.2: Bringing Native Reasoning and Agentic RL to Open Enterprise Models
- 作者／機構：Asif Razzaq, MarkTechPost
- 連結：https://www.marktechpost.com/2026/08/25/ibm-releases-granite-4-2-bringing-native-reasoning-and-agentic-rl-to-open-enterprise-models/

#IBM #GraniteAI #OpenSourceLLM #ReasoningModels #AgenticAI #ReinforcementLearning #Apache2 #LLM #EnterpriseAI #GRPO
