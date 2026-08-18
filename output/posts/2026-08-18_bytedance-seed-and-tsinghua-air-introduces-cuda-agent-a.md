---
title: 'ByteDance Seed and Tsinghua AIR Introduces CUDA Agent: A Large-Scale Agentic
  RL System for CUDA Kernel Generation'
source: MarkTechPost
url: https://www.marktechpost.com/2026/08/17/bytedance-seed-and-tsinghua-air-introduces-cuda-agent-a-large-scale-agentic-rl-system-for-cuda-kernel-generation/
model: claude-code/sonnet
generated_at: '2026-08-18T06:30:51.409530'
score: 94
---

📌 【字節跳動 Seed 與清華 AIR】用強化學習教 LLM 寫出比編譯器更快的 CUDA Kernel

TL;DR：CUDA Agent 用大規模 agentic RL 訓練模型寫 GPU kernel，在 250 個任務上有 96.8% 打贏 torch.compile。

前沿模型寫 CUDA 早就寫得「對」，問題從來不是正確性，而是慢。ByteDance Seed 與 Tsinghua AIR 這篇研究把這個看似狹窄的落差量化了出來：基礎模型 Seed1.6 在 KernelBench 上有 74.0% 的任務能通過正確性測試，但其中只有 27.2% 的 kernel 跑得比 torch.compile 快，幾何平均速度甚至只有 0.69 倍，也就是說，平均而言它寫出來的 kernel 比編譯器自動產生的還慢。

🤔 模型會寫 CUDA，但寫不贏編譯器

CUDA Agent 想解決的正是這個落差：即便通過正確性測試，LLM 生成的 kernel 效能往往仍不及 torch.compile 這類成熟編譯器的自動最佳化結果。

🧩 把模型丟進真實的 CUDA 開發環境裡

CUDA Agent 的做法是把模型放進一個具備 profiling、正確性檢查與權限鎖定沙盒的真實 CUDA 開發環境，再用 PPO 訓練 150 個 step，context 長度設定為 131,072 token。

Agent 的工具迴圈參考了 OpenHands 的做法，提供 Bash、Read/Write、Edit/MultiEdit、Glob、Grep、NotebookEdit、BashOutput、KillBash 等工具，並以 ReAct 模式運作。CUDA 相關的操作指引以 Agent Skills 格式撰寫成 SKILL.md，要求模型對 PyTorch 模型做 profiling、改寫 model_new.py 加入自訂 kernel、在 GPU 沙盒中編譯，並持續迭代，直到 kernel 在 atol=1e-2、rtol=1e-2 的容許誤差下，比 torch.compile 快至少 5%。

為了防止 reward hacking，團隊設計了五道防線：權限鎖定的驗證與 profiling 腳本、禁止呼叫 torch.nn.functional 做為 fallback 的 context manager、用五組隨機輸入做檢查、profiling 時加入裝置同步與暖機（warm-up），以及不提供網頁搜尋工具。獎勵訊號也刻意設計成離散值而非原始加速比：r ∈ {−1, 1, 2, 3}，正確性測試失敗給 −1，同時打贏 eager 模式與 torch.compile 超過 5% 給 3，只贏 eager 給 2，其餘情況給 1。

🧩 資料從哪來：CUDA-Agent-Ops-6K

訓練資料集 CUDA-Agent-Ops-6K 的建構方式，是先從 torch 與 transformers 函式庫中爬取參考運算子（operator），接著用一個 LLM 取樣最多五個 torch 運算子類別並堆疊成一個融合層（fused layer）。篩選條件包括：必須能在 eager 與 compile 兩種模式下都執行、結果具決定性、輸出非常數，且在 eager 模式下的執行時間落在 1 毫秒到 100 毫秒之間；與 KernelBench 任務 AST 相似度超過 0.9 的樣本會被剔除。最終得到 6,000 筆樣本，其中 83.77% 是兩個運算子的組合。

底層模型 Seed1.6 是一個專有的 MoE 模型，啟用參數 23B、總參數 230B；用於 profiling 的沙盒環境動用了 128 張 NVIDIA H20 GPU。

📊 250 個任務，96.8% 打贏 torch.compile

在 250 個任務的 benchmark 上，整體結果為 98.8% 通過率、98.4% 比 eager 模式快、96.8% 比 torch.compile 快，幾何平均分別是 2.60 倍與 2.11 倍。

| 難度分級 | 通過率 | 快於 torch.compile 比例 | 相對 torch.compile 幾何平均加速 |
|---|---|---|---|
| Level 2（運算子序列） | 100% | 100% | 2.80× |
| Level 3（最難） | 94.0% | 90.0% | 1.52× |

在最難的 Level 3 上，CUDA Agent 的「快於 torch.compile 比例」比 Claude Opus 4.5（50.0%）與 Gemini 3 Pro（52.0%）高出約 40 個百分點。值得一提的是，論文摘要與導論中提到的 Level 1 至 3 快於編譯器比例為 100% / 100% / 92%，與正文 Table 1 所列的 97.0% / 100.0% / 90.0% 存在出入，報導以 Table 1 為主要結果依據。

消融實驗也很直白：拿掉 agent 迴圈，快於 torch.compile 的比例從 96.8% 暴跌到 14.1%；把獎勵訊號換成原始加速比，結果是 60.4%；拿掉 RFT 會掉到 49.8% 並出現獎勵崩潰；拿掉 value 預訓練則是 50.9% 並伴隨軌跡失控（runaway trajectories）。

幾個具體案例展示了模型學到了什麼：把對角矩陣乘法改寫成逐列縮放（row-wise scaling），相對 torch.compile 加速 73.31 倍；把矩陣乘法、除法、加總、縮放這條運算鏈重新排序並融合，加速 24.04 倍；把 ResNet BasicBlock 中的 BatchNorm 折疊進卷積層，並使用 cudnnConvolutionBiasActivationForward，加速 3.59 倍。

⚠️ 訓練好的模型並未釋出

CUDA Agent 建立在 Seed1.6 這個專有 MoE 模型之上，論文沒有釋出模型權重。真正公開的是 CUDA-Agent-Ops-6K 資料集、SKILL.md 規格，以及獎勵與暖機訓練配方。而 profiling 沙盒動用的 128 張 H20 GPU，意味著完整複現這套系統的門檻集中在前沿實驗室、GPU 雲端服務商與大型基礎設施團隊手上；中型團隊仍可以在開源底層模型上套用資料集、里程碑式獎勵設計、防 reward hacking 的限制與 skill 規格。

🎯 實務啟示

如果你的團隊在做 kernel 融合或跨 GPU 世代的效能調校，即便拿不到 CUDA Agent 本體，SKILL.md 這種「profiling → 改寫 → 沙盒編譯 → 迭代」的流程規格，以及五道防 reward hacking 的機制設計，本身就是值得參考的 agentic 工程實踐範本。

🔗 來源
- 標題：ByteDance Seed and Tsinghua AIR Introduces CUDA Agent: A Large-Scale Agentic RL System for CUDA Kernel Generation
- 作者／機構：Asif Razzaq／MarkTechPost
- 連結：https://www.marktechpost.com/2026/08/17/bytedance-seed-and-tsinghua-air-introduces-cuda-agent-a-large-scale-agentic-rl-system-for-cuda-kernel-generation/

#CUDA #ReinforcementLearning #LLMAgents #GPUKernel #ByteDance #Tsinghua #KernelBench #AgenticAI #PPO #AIInfrastructure
