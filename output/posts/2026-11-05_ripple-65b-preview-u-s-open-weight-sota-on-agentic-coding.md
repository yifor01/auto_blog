---
title: 'Ripple-65B Preview: U.S. Open-Weight SOTA on Agentic Coding'
source: Hacker News
url: https://www.ricursive.com/ripple
model: claude-code/sonnet
generated_at: '2026-11-05T22:54:28.390287'
score: 112
---

📌 美國開源陣營新王者：65B 密集模型打贏千億參數 MoE 大軍

TL;DR：Ricursive Intelligence 用 65B 密集 Transformer、3200萬美元訓練成本，拿下美國開源權重 agentic coding SOTA。

當同業不是燒到十億美元訓練模型、就是堆出 500B 甚至 975B 參數的 Mixture-of-Experts（MoE）架構時，一家名為 Ricursive Intelligence 的全端 AI 實驗室只用 65B 參數的密集模型，就在 TerminalBench 2.1 上衝到美國開源權重榜首。這篇技術部落格在 Hacker News 上累積 331 個讚、120 則留言，熱度不是沒有道理。

🤔 **訓練一個前沿模型，為什麼動輒上億美元**

2023 年 OpenAI 的 Sam Altman 曾說 GPT-4 訓練成本超過 1 億美元；隔年 Anthropic 的 Dario Amodei 預測前沿模型訓練成本將上看 10 億美元，並推估到 2026、2027 年會攀升到 100 億至 1000 億美元。Ricursive 在部落格中提到，像 Reflection 這類美國開源陣營對手，據報每月承諾投入 1.5 億美元的運算資源，其 Beam 模型光是預訓練加後訓練就花了 8 週。相較之下，Ripple-65B Preview 從零開始的全部研發成本，包含 ladder 實驗、資料配比、評測、除錯、合成資料生成與最終的 pretraining/posttraining 正式跑，總共只用了 3200 萬美元。

🧩 **選密集模型、不選 MoE，是刻意的架構決策**

Ripple 捨棄了業界流行的 MoE，改用現代化的密集 Transformer，理由是降低訓練與推論基礎設施的複雜度。模型採用「薄而深」的比例：d_model 僅 5120，但疊了 80 層。為了補強推理能力，團隊刻意多配置 attention head 數量，同時提高 sliding window attention（SWA）相對 global attention 的層數比例並縮小 SWA 視窗來抵銷額外成本。另外還加入了 FFN activation clipping、gated attention、global NoPE 與 value residuals 等設計。即便只用簡單的 sharding、沒有客製化 kernel、也沒有量化，整個訓練過程仍維持 40% 的 MFU（模型 FLOPs 使用率）。

🧩 **RL 不是靠暴力堆 rollout，而是靠效率**

後訓練上，Ricursive 沒有外購任何資料，全靠自建的合成資料管線、品質過濾與覆蓋率指標。其混合 RL 配方結合了 truncated importance sampling、score centering 與線性長度懲罰，並搭配高品質的長視野合成環境。最終只用 140 萬次 rollout，就把 TerminalBench 2.1 分數推到 80.5 分，比起前 SOTA Reflection Beam 所用的 rollout 數少了約 70 倍。架構之外的另一塊關鍵是「model laddering」：團隊從 AI2 的 Olmo 3 ladder 出發，經過 v1.0 到 v1.6 共六輪調整（批次大小與學習率縮放、pre+post norm、sigmoid gated attention、global NoPE、value residuals 等），再換上自建的程式碼高配比資料集，最終在 4B 規模下用 dolma_stack 交叉熵（CE）衡量，程式碼運算效率提升最多達 16 倍。

📊 **對照表：以小搏大的實測結果**

| 模型 | 參數規模 | TerminalBench 2.1 |
|---|---|---|
| Ripple-65B Preview | 65B（密集） | 80.52 |
| Reflection Beam | 501B | 80.1 |
| Meta Muse Spark Open | 816B | 76.4 |
| Thinking Machines Inkling | 975B | 63.8 |
| NVIDIA Nemotron 3 Ultra | 550B | 56.4 |

⚠️ **別忘了這仍是「Preview」，且數字都是自報**

以上分數均為 Ricursive 自行公布的結果，成本估算也是「盡力推估」而非逐項審計；模型本身仍標示為 Preview 版本，意味著後續可能還有調整空間。

🎯 **對工程師的實際意義**

密集模型的小參數量，讓 Ripple 能在像 NVIDIA DGX Spark 這類「高算力、低記憶體頻寬」的本地裝置上有效運行，這對想在地端跑 agentic coding 工作流的團隊是個實際選項。更值得借鏡的是其 model laddering 方法論：用小規模實驗篩選架構與資料策略，再外推到正式訓練，這套流程本身就是可被其他團隊複製的降低訓練成本手段。

🔗 **來源**
- 標題：Ripple-65B Preview: U.S. Open-Weight SOTA on Agentic Coding
- 作者／機構：Philpax（Ricursive Intelligence，經 Hacker News 轉貼討論）
- 連結：https://www.ricursive.com/ripple

#OpenWeightLLM #AgenticCoding #LLMTraining #DenseTransformer #TerminalBench #RicursiveIntelligence #Ripple65B #ReinforcementLearning #AIInfrastructure #MachineLearning
