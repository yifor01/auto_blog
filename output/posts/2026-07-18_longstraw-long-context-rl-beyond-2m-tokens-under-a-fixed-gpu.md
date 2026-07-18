---
title: 'LongStraw: Long-Context RL Beyond 2M Tokens under a Fixed GPU Budget'
source: HuggingFace Daily Papers
url: https://huggingface.co/papers/2607.14952
score: 105
model: tencent/hy3:free
generated_at: '2026-07-18T07:31:30.569067'
---

📌 【HuggingFace Papers】固定 GPU 預算下，長上下文 RL 突破 2M tokens

TL;DR：LongStraw 讓百萬級 token 的 RL 後訓練在固定 GPU 下可行，實測達 2.1M–4.46M positions。

推理系統的上下文長度已逼近百萬 tokens，但 RL 後訓練工作負載卻還卡在 256K tokens 以下，部署時才靠長度泛化硬撐。對 AI 代理而言，觀察、工具輸出、檔案與決策軌跡會隨時間不斷累積，這個落差格外致命。

🤔 **推理長度與 RL 後訓練的斷層**

摘要指出，推理系統（inference systems）正邁向 million-token context，而 post-training 工作負載常停留在 256K tokens 或更低，依賴部署時的 length generalization。此差距對 AI agents 特別關鍵，因其觀察、tool outputs、documents 與 prior decisions 會在長軌跡中持續堆疊。

🧩 **LongStraw：架構感知的執行堆疊**

LongStraw 是一套 architecture-aware execution stack，目標是在固定 GPU 預算下做 million-token RL 後訓練，並以 GRPO（Group Relative Policy Optimization）實作。其核心設計：
- 對 shared prompt 進行不帶 autograd 的評估（evaluates without autograd）
- 只保留後續 tokens 所需的 model-specific state
- 一次重播（replay）一條短 response 分支，以額外 replay 時間換取縮小 live training graph

📊 **8 張 H20 實測：2.1M positions，群組放大僅增 0.21GB**

在 8 張 H20 GPU 上，LongStraw 完成 grouped Qwen 的 scoring 與 response backward，於 group size 2 與 8 下皆達 2.1M positions；增大群組僅多佔 0.21GB 峰值記憶體，獨立壓力測試更達 4.46M positions。實作物件為 hybrid recurrent + full-attention 的 Qwen3.6-27B，以及 compressed-attention MoE 的 GLM-5.2。

於 32 張 H20 GPU 上，作者驗證了 GLM-5.2 全 78 層、2.1M-token prompt 的端到端 LongStraw 執行路徑。

⚠️ **目前只證明執行能力，非訓練正確性**

作者說明，這些實驗建立的是 execution capacity 而非完整訓練正確性：capture 的 prompt state 被 detached，且部分 distributed forward 與 gradient composition 路徑尚不完整。

🎯 **實務啟示**

若你在做長軌跡 agent 的 RL 後訓練，LongStraw 展示了一條不靠堆 GPU 也能跑百萬 token 的可行路徑：用狀態保留與分支重播換取記憶體上限的突破，值得關注後續補齊梯度路徑的版本。

🔗 **來源**
- 標題：LongStraw: Long-Context RL Beyond 2M Tokens under a Fixed GPU Budget
- 連結：https://huggingface.co/papers/2607.14952

#LongContext #RL #GRPO #GPU #LLM #Agent #PostTraining #Qwen #GLM #ExecutionStack
