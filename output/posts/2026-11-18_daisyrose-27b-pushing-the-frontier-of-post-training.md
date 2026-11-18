---
title: 'DaisyRose-27B: Pushing the Frontier of Post-Training Efficiency'
source: HuggingFace Blog
url: https://huggingface.co/blog/RadixArk/daisyrose-27b-pushing-the-frontier-of-post-trainin
model: claude-code/sonnet
generated_at: '2026-11-18T23:37:47.961437'
score: 99
---

📌 DaisyRose-27B：RL後訓練讓Terminal-Bench翻倍

TL;DR：RadixArk用RL微調Qwen3.8-27B，Terminal-Bench翻倍。

只用1,200筆任務、144張H200練18天，就能讓一個27B模型在終端機操作的benchmark成績翻倍——這是RadixArk首款發布模型交出的成果。

🤔 背景：1,200筆任務、18天、144張H200練出的agent模型

RadixArk發布的DaisyRose-27B，是在Qwen3.8-27B基礎上，用自家強化學習框架Miles訓練而成。訓練目標是長流程（long-horizon）的agent任務，單次session最長可達1M tokens，整個訓練只用了1,200筆精選任務，耗時18天，動用144張H200 GPU。模型保留Qwen3.8-27B原本的架構、tokenizer、chat template、圖像理解能力與256K context window，更長的訓練session則透過harness summarization串接多個trajectory。

🧩 非同步RL訓練：128張GPU跑推理、16張學習，互不等待

訓練用全非同步（fully asynchronous）架構：128張H200跑agent任務的推理，另外16張跑trainer學習，推理持續產生新的trajectory，trainer持續從已有的trajectory學習，每一步訓練完，更新後的模型就重新發布給負責推理的128張GPU。訓練資料與Eigent AI合作打造，從其機器學習、軟體工程、科學等任務池出發，共同設計出數千個候選任務，最終篩選出約1,200筆進入訓練集。篩選標準有三：每個任務要對準原模型會犯的具體錯誤；每個任務需要多個相互依賴的步驟，逼模型做長程的推理、規劃與執行（單次嘗試最多1.5小時、超過100次工具呼叫、超過256K輸出token）；每個任務必須真正獎勵「解對問題」本身，團隊逐一檢視任務與模型的嘗試記錄，修掉或移除可以在沒解決問題的情況下通過的任務。

📊 數據：Terminal Bench 4.1 pass@1從5.6%衝上12.0%

| Benchmark | Qwen3.8-27B | DaisyRose-27B |
|---|---|---|
| Terminal Bench 4.1 | 5.6 | 12.0 |
| Terminal Bench 2.1 | 73.0 | 75.5 |
| DeepSWE v1.1 | 42.2 | 46.2 |
| SWE Bench Pro v2 | 91.3 | 94.7 |
| HLE (text-only) | 33.9 | 34.3 |
| IFBench | 79.5 | 82.4 |
| GPQA Diamond | 89.2 | 90.7 |

漲幅最大的是Terminal Bench 4.1，pass@1從5.6%提升到12.0%。分數採BF16與FP8兩種run中較高者，兩者差距在同時有評測的項目上都小於1分。訓練效率方面，這次release run的GPU peak compute有37%真正用在有效訓練工作上（MFU），他們測試的開源Megatron trainer在同等情況下只有16%，換算下來同樣的訓練所需GPU時間少57%；在MoE模型上差距更大，Qwen3.6-35B-A3B上快6.2倍，約300B參數的GLM-5.3-Flash上超過10倍。算上agent跑任務的時間，這次release run在144張GPU上整體達到每秒約16,800 tokens，開源trainer在同樣GPU上只有約8,300。整個訓練跑了數週，累積63,000 GPU小時，速度與效率全程保持穩定。

💡 深入分析：撐起訓練的，是一天最多1,566個的sandbox

每次訓練嘗試都在一個sandbox（任務環境的全新副本）裡執行命令、修改檔案再被評分。這套服務建立在開源的AgentENV專案上，團隊也回饋修正給上游。從9月中到11月中，總共跑了約944,000個sandbox，最高同時有1,566個在跑；服務規模從1臺機器擴展到最多12臺，其間上線了10次升級，幾乎都是在訓練仍在進行時完成的。九週下來，sandbox建立成功率達99%，10月底後更超過99.95%。團隊表示，這個專案的sandbox雲端基礎設施成本，比用熱門的雲端sandbox服務商低約80%，其中一個做法是讓每個sandbox的記憶體配置隨實際用量動態伸縮，讓更多sandbox能共用同一臺機器。

🎯 實務啟示：Apache 2.0開源，SGLang+DSpark就能跑

權重依Apache 2.0授權開源，提供BF16、FP8、NVFP4三種checkpoint格式，建議搭配SGLang與DSpark speculative decoding部署。使用方式與一般OpenAI相容client相同，模型預設會先在reasoning_content輸出推理過程，再於content給出最終答案。想自己訓練agent的團隊，也可以直接用開源的Miles框架。

🔗 來源
- 標題：DaisyRose-27B: Pushing the Frontier of Post-Training Efficiency
- 作者／機構：Jason Chen, RadixArk（HuggingFace Blog）
- 連結：https://huggingface.co/blog/RadixArk/daisyrose-27b-pushing-the-frontier-of-post-trainin

#DaisyRose27B #RadixArk #ReinforcementLearning #OpenSourceAI #Qwen #LLM #AgentTraining #TerminalBench #SGLang #PostTraining
