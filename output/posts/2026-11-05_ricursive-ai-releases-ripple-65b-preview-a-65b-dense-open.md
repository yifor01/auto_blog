---
title: 'Ricursive AI Releases Ripple-65B Preview: A 65B Dense Open-Weight Model Scoring
  80.5 on Terminal-Bench 2.1'
source: MarkTechPost
url: https://www.marktechpost.com/2026/11/04/ricursive-ripple-65b-preview-open-weight-model/
model: claude-code/sonnet
generated_at: '2026-11-05T22:54:28.390584'
score: 107
---

📌 Ripple-65B 開箱：三款檢查點、五階段後訓練，實測效能一次看懂

TL;DR：Ricursive 釋出三款 Ripple-65B 檢查點，並公開完整後訓練流程與地端推論效能數字。

如果你已經聽過 Ripple-65B Preview 在 TerminalBench 2.1 拿下 80.52 分、打贏一眾 500B 到 975B 的 MoE 大模型，下一個問題自然是：這個模型實際能不能用、怎麼部署、跑起來多快。MarkTechPost 的報導整理出更完整的釋出細節，從檢查點選項到推論速度都有具體數字。

🤔 **一句話回顧：密集模型打敗千億級對手**

Ripple-65B Preview 是 Ricursive Intelligence 從零訓練的 65B 密集模型，是其 AI 晶片設計平臺背後專有模型的通用版本。它在 TerminalBench 2.1 拿下的 80.52 分，是美國開源權重模型裡自報最高分，而每一個被它超越的 MoE 對手，總參數都在 501B 到 975B 之間。

🧩 **三個檢查點、全部 Apache 2.0**

這次釋出包含三個版本：指令微調的 BF16 模型、NVFP4 量化版本，以及 BF16 base 模型，三者都採 Apache 2.0 授權。預訓練語料為純文字，以英文與程式碼為主，序列長度為 8K。Ricursive 團隊表示，含 ladder 實驗、資料配比、評測、合成資料與最終訓練跑在內的全部研發成本是 3200 萬美元。

🧩 **後訓練五階段：從 midtraining 到 mixed RL**

後訓練流程依序走過 midtraining → long context → SFT → long-context SFT → mixed RL，其中長文本階段訓練序列長度拉到 2M。RL 配方結合 truncated importance sampling、score centering 與線性長度懲罰，整個流程沒有外購任何後訓練資料，全靠自建的合成資料管線。最終只用 140 萬次 rollout 就達到 80.5 分，Ricursive 估算這大約是 Reflection Beam（據報超過 1 億次 rollout）的 70 分之一。

📊 **換個官方量尺重新測一次，排名有變化**

Ricursive 團隊用 OpenCode 自行補測了一些缺漏的評測項目（如 SWE-bench Pro v2.0 Hard、DeepSWE 1.1，均用 Terminus 2 跑），並額外用官方 Terminus 2 工具、128K 上下文重新跑過一次 TerminalBench 2.1。結果多數對手分數下滑：Beam 掉到 70.8 分；但 Meta 的 Muse Spark Open 反而從 76.4 分升到 78.7 分，仍低於 Ripple 的 80.5 分。要注意的是，所有分數（包括 Ripple 自己的）都是各家自報，並非第三方審計。

📊 **推論效能：2 張 B200 跑出 250 tok/s**

在資料中心 GPU 上，量化前的模型在 2x NVIDIA B200、batch size 8 的設定下可達到 250 tok/s。實驗性的 NVFP4 檢查點只量化 MLP 層，attention 部分維持 BF16，官方將其定位為面向 NVIDIA DGX Spark 這類本地裝置的版本；另外還列出一個 DFlash2 變體。

💡 **架構：從 Olmo 3 的 Llama 式佈局換成 Gemma 3N 式設計**

Ripple 的 d_model 為 5120、共 80 層，走「薄而深」路線。報導指出，這個設計是從 Olmo 3 的 Llama 式佈局，轉向類似 Gemma 3N 的佈局以求穩定性。選擇密集 Transformer 而非 MoE，是為了降低基礎設施複雜度；即便只用簡單 sharding、沒有客製化 kernel、也沒有量化，訓練仍維持 40% MFU，在 4B 規模的 ladder 實驗中，程式碼運算效率比起 Olmo 3 ladder 基準提升達 16 倍。

⚠️ **部署管道仍在陸續上線**

權重已在 Hugging Face 公開，官方列出 Together AI、GMI Cloud、OpenRouter 為首批上架平臺，Fireworks 則會後續加入；不過報導指出，截稿時 Together AI 頁面仍標示「即將上線」，顯示部分管道還在就位中。

🎯 **對工程師的實務啟示**

比起單一個自報的榜首分數，三個檢查點（含量化版）加上官方工具重新測試的結果，給了更多可供交叉驗證的訊號：想在地端跑 agentic coding 的團隊，可以直接拿 NVFP4 版本評估記憶體與速度的取捨，而不用等第三方重新量化。

🔗 **來源**
- 標題：Ricursive AI Releases Ripple-65B Preview: A 65B Dense Open-Weight Model Scoring 80.5 on Terminal-Bench 2.1
- 作者／機構：Asif Razzaq（MarkTechPost）
- 連結：https://www.marktechpost.com/2026/11/04/ricursive-ripple-65b-preview-open-weight-model/

#Ripple65B #OpenWeightLLM #ModelRelease #Quantization #NVFP4 #AgenticCoding #LLMDeployment #Apache2 #HuggingFace #Benchmarking
