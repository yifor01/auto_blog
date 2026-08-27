---
title: 'Alibaba’s Qwen Team Releases Qwen3.8-Flash-Next: A 125B Multimodal MoE With
  6B Active Parameters Previewing the Qwen4 Architecture'
source: MarkTechPost
url: https://www.marktechpost.com/2026/08/26/alibabas-qwen-team-releases-qwen3-8-flash-next-a-125b-multimodal-moe-with-6b-active-parameters-previewing-the-qwen4-architecture/
model: claude-code/sonnet
generated_at: '2026-08-27T17:18:44.250086'
score: 107
---

📌 Qwen3.8-Flash-Next：180B 模型只啟動 6B，搶先預覽 Qwen4 架構

TL;DR：Qwen 團隊釋出多模態 MoE 模型 Qwen3.8-Flash-Next，訓練成本僅前代九分之一。

當多數團隊還在比拚參數量誰更大時，阿里巴巴 Qwen 團隊丟出了一個反過來的問題：能不能把 180B 的模型容量放在硬碟裡，卻只讓 6B 參數在每次推論時真正動起來？Qwen3.8-Flash-Next 給出的答案，也被團隊定位成 Qwen4 架構的早期預覽版本，如同當初 Qwen3-Next 之於 Qwen3.5 的角色。

🤔 **目標是每個 token 的成本，不是排行榜名次**

Qwen 團隊將這個開放權重的多模態 Mixture-of-Experts（MoE）模型明確定位為「為每 token 成本而生」。整體架構把一個 125B 的主幹模型、一個 51B 的 N-gram embedding 表，以及一個 4B 的多 token 預測（multi-token prediction）模組組合在一起，磁碟上總計約 180B 參數，但每個 token 實際只啟動 6B 參數。換句話說，稀疏啟動降低的是運算量，不是儲存需求。

🧩 **四項架構改動，加上 Muon 最佳化器**

驅動這次釋出的有四項改動：Gated DeltaNet 與 Qwen Sparse Attention 的混合設計、Gated Residual、N-gram Embedding，以及改用 Muon 最佳化器。MoE 層設有 512 個專家（experts），每次啟動 10 個路由專家加 1 個共享專家，專家中間層維度為 640。Qwen 團隊表示，這套架構讓訓練成本降到 Qwen3.7-Plus 的約九分之一。

📊 **跑分表現：程式碼與代理任務強，前沿推理仍有差距**

Qwen 官方公布的跑分數據如下：

| 類別 | 基準 | 分數 |
|---|---|---|
| 程式碼 | DeepSWE 1.1 | 58.7 |
| 程式碼 | SWE-bench Pro | 62.5 |
| 程式碼 | SWE-bench Multilingual | 81.0 |
| 程式碼 | LiveCodeBench v6 | 91.9 |
| 代理任務 | CoWorkBench | 73.9 |
| 代理任務 | JobBench | 55.7 |
| 代理任務 | Toolathlon Verified | 73.5 |
| 多模態 | AndroidWorld | 84.5 |
| 多模態 | LVBench | 76.6 |
| 多模態 | RealWorldQA | 88.5 |
| 多模態 | MathVision（含 code interpreter） | 95.7 |

不過這款模型並非全面領先：在 HLE 上，Claude Opus 4.6（Max）拿下 40.0 分，高於 Qwen3.8-Flash-Next 的 35.9 分；在 NL2Repo-Bench 上，DeepSeek-V4-Flash-0731 以 54.2 分領先 Qwen 的 48.1 分。前沿級的推理能力，仍是這個架構尚未追上的部分。

💡 **部署門檻不低，量化配置也有硬性限制**

儘管訓練成本降低，實際部署仍不輕鬆：FP8 checkpoint 大小為 172.78 GiB，BF16 版本則是 335.28 GiB。根據 vLLM 的建議，在 GB300 上 TP2 是可驗證的最低 FP8 設定，官方建議使用 TP4；在 8×H200 節點上則需使用 TEP8，因為單純的 TP8 與 checkpoint 採用的 128-wide 量化區塊不相容。至於推論效能，官方公告提到 QSA 核心在 1M token 情境下可帶來最高 7.6 倍的 prefill 加速與 4.9 倍的 decode 加速，SGLang cookbook 與 vLLM recipes 則引用了 10.2 倍與 6.6 倍的數字；這些倍數目前屬於廠商自報，尚待第三方獨立驗證。官方另表示，在 90% 前綴快取命中率下，prefill 吞吐量可達 Qwen3.7-Plus 的 8.6 倍。模型原生支援 262,144 token 上下文，搭配 YaRN 可延伸至 1,000,000 token。

🎯 **實務啟示**

Qwen3.8-Flash-Next 已支援 vLLM、SGLang、TokenSpeed、transformers serve，以及可跑 GGUF 量化版本的 llama.cpp，微調則可透過 Unsloth、Swift、LLaMA-Factory 進行，目前已用於 QwenWork 的「Standard」模式並可搭配 Qwen Code 使用。模型預設開啟 thinking mode，reasoning_effort 可選 xhigh、medium、low；官方建議 thinking mode 使用 temperature 1.0、top_p 0.95，instruct mode 則使用 temperature 0.7、top_p 0.80。對於想在推理成本與程式碼／代理任務能力間取得平衡、且能接受多卡部署門檻的團隊，這是一個值得納入評估清單的選項；但若任務高度仰賴前沿級推理能力，仍需留意它與頂尖模型之間的差距。

🔗 **來源**
- 標題：Alibaba's Qwen Team Releases Qwen3.8-Flash-Next: A 125B Multimodal MoE With 6B Active Parameters Previewing the Qwen4 Architecture
- 作者／機構：Asif Razzaq（MarkTechPost）
- 連結：https://www.marktechpost.com/2026/08/26/alibabas-qwen-team-releases-qwen3-8-flash-next-a-125b-multimodal-moe-with-6b-active-parameters-previewing-the-qwen4-architecture/

#Qwen #Qwen4 #MixtureOfExperts #OpenWeightLLM #MultimodalAI #LLMInference #vLLM #SGLang #ModelQuantization #AIInfrastructure
