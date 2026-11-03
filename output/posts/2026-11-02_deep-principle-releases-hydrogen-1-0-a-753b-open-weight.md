---
title: 'Deep Principle Releases Hydrogen-1.0: A 753B Open-Weight Model for Scientific
  Discovery'
source: MarkTechPost
url: https://www.marktechpost.com/2026/11/02/deep-principle-hydrogen-1-0-open-weight-scientific-model/
model: claude-code/sonnet
generated_at: '2026-11-03T00:01:04.902213'
score: 105
---

📌 Deep Principle 推出 Hydrogen-1.0：753B 開權重科學模型挑戰 GPT-6-Astra

TL;DR：753B 開權重科學研究模型，實驗結果宣稱在 FrontierScience-Research 贏過 GPT-6-Astra，但完整資料與訓練食譜未開放。

近期幾個備受矚目的 AI 科學發現成果都出自專有模型，但這些模型的「發現能力」本身並不開放給外界檢視。來自杭州材料 AI 公司 Deep Principle 的 Hydrogen-1.0，正是想補上這塊缺口：一個可重現、可被檢視的開放替代方案。

🤔 **為什麼需要一個開放的科學研究模型**

Deep Principle 團隊在模型卡中指出，目前推動 AI 科學成果的多是封閉系統，外部研究者無法驗證其推理過程或重現結果。Hydrogen-1.0 被定位為化學、材料科學與生命科學領域的研究助理，目標涵蓋問題框架設定、實驗規劃、結果分析到開放式探索，權重以 MIT License 發布。

🧩 **底層是 GLM-5.3，疊加 SFT 與 RL**

Hydrogen-1.0 是在 Z.ai 的 GLM-5.3 基礎上做 post-training 而成，資料來自 domain data、實驗室紀錄與 agent discovery trajectories 等來源。訓練管線結合 supervised fine-tuning 與 reinforcement learning：

- 基礎設施採用 Megatron 與 SGLang，同時支援 NVIDIA CUDA 與 AMD ROCm。
- 團隊讓 dynamic sparse attention 在 context-parallel 切分下維持因果性（causal）。
- Muon optimizer 的狀態依不同後端在 CPU、GPU、磁碟間搬移。
- RL 階段使用可恢復（resumable）rollout，每個 token 保留原始的行為 log-probability 用於重要性校正（importance correction）。
- 一個 layout adapter 把訓練用 checkpoint 轉換成 BF16 以及 128×128 blockwise FP8 的推理權重。

值得注意的是，完整資料集與訓練食譜並未隨模型一併釋出,外界能拿到的是權重與推理設定,而非可完整重現訓練過程的全部素材。

📊 **化學任務上的對比數據**

在公開基準上，Deep Principle 宣稱 Hydrogen-1.0 在 FrontierScience-Research 上超越 GPT-6-Astra；創辦團隊的貼文提到在 GPQA-Diamond 上拿到 93.0%，優於底層的 GLM-5.3，大致與 Kimi-K3 相當。

內部研究任務評測（與 GPT-6-Astra 在最大思考模式下比較）顯示：在過渡金屬錯合物設計任務中，模型需在 5 輪內追求更大的 HOMO-LUMO gap，Hydrogen-1.0 在第 5 輪達到平均 best-so-far gap 4.318 eV，GPT-6-Astra 為 3.689 eV，Kimi-K3 為 3.353 eV。在 117 題實驗規劃問題上，Hydrogen-1.0 得分高於 Kimi-K3；GPT-6-Astra 與 Opus-5.5 則因拒絕超過半數請求而被排除在比較之外。

技術文章還展示了 4 個示範：用 Python 建立 polyethylene 熔融模型並跑 GROMACS，偵測並修復拓樸錯誤後分析 40 ns 軌跡；擴展出一個涵蓋 27 個結構、30 個合理反應的 Ireland-Claisen 反應網路；根據 1H NMR 訊號，對 2-bromonaphthalene 的 7 個候選單甲醛化產物排序；以及為 12 瓶 Suzuki coupling 實驗撰寫 JSON 協定，其中虛擬實驗室的編譯步驟還能在執行前抓出「吸取卻沒換新吸頭」的操作錯誤。

🎯 **怎麼跑起來**

權重已上架 Hugging Face 與 ModelScope。團隊測試過用 SGLang 在 8 張 GPU 上以 tensor parallelism 8 進行 BF16 服務;NVFP4 格式針對 NVIDIA B200 / B300，MXFP4 則對應 AMD Instinct MI350X / MI355X。伺服器提供 OpenAI 相容 API,並可調整 reasoning_effort 參數,對想串接現有 agent 框架的工程師來說算是友善的落地門檻。

🔗 **來源**
- 標題：Deep Principle Releases Hydrogen-1.0: A 753B Open-Weight Model for Scientific Discovery
- 作者／機構：Asif Razzaq，MarkTechPost
- 連結：https://www.marktechpost.com/2026/11/02/deep-principle-hydrogen-1-0-open-weight-scientific-model/

#Hydrogen1 #DeepPrinciple #OpenWeightLLM #AIforScience #GLM #SGLang #Megatron #ScientificAI #MaterialsScience #LLMInference
