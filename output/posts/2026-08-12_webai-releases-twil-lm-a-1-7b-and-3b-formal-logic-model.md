---
title: 'webAI Releases TwIL-LM: A 1.7B and 3B Formal-Logic Model Family for Autoformalization
  on Local Hardware'
source: MarkTechPost
url: https://www.marktechpost.com/2026/08/10/webai-releases-twil-lm-a-1-7b-and-3b-formal-logic-model-family-for-autoformalization-on-local-hardware/
model: claude-code/sonnet
generated_at: '2026-08-12T07:38:48.610006'
score: 85
---

📌 3B 模型打贏 gpt-oss-120b？webAI 形式邏輯模型 TwIL-LM 的真實戰績

TL;DR：webAI 釋出 1.7B 與 3B 的本地端形式邏輯推理模型 TwIL-LM，在部分測驗贏過 120B 模型，但非商用授權且勝負分佈並不單純。

一個 3B 參數的模型，在多項測驗上贏過 120B 的 gpt-oss——這聽起來像是又一次誇大的模型發表，但攤開 webAI 公布的完整數據後，故事比標題複雜得多。

🤔 **目標：把英文句子變成一階邏輯**

TwIL-LM 是 webAI 推出的兩個模型家族成員，鎖定的任務是 autoformalization：將英文敘述翻譯成一階邏輯（first-order logic），並判斷某個結論是否能從其前提推導出來。3B 版本 TwIL-LM3 是 SmolLM3-3B 的合併微調（merged fine-tune）；1.7B 版本則是針對 SmolLM2-1.7B-Instruct 的 PEFT LoRA adapter。兩者都設計為在本地端硬體運行，1.7B 提供 1.06 GB 的量化版本，3B 提供 1.78 GiB 的 Q4_K_M GGUF 版本。

需要注意的是，兩個 checkpoint 目前都是「webAI Non-Commercial License ver. 1.0」授權，僅限非商業用途，若要用於營利部署，需另外與 webAI 簽約。

🧩 **四階段訓練流程，其中一個參數決定了模型的個性**

模型卡揭露的訓練流程分四個階段進行：

1. 在合成的形式邏輯語料上做 LoRA 監督式微調（SFT）
2. Checkpoint fusion：對多個中間 SFT checkpoint 做參數空間的平均
3. WiSE-FT 插值：以 λ=0.25 的比例，將模型往回插值靠近原始 pretrained base
4. MGPO：一種 entropy-weighted 的 GRPO 強化學習階段，針對可程式化驗證器（programmatic verifier）訓練

最終公開的 checkpoint 是第 2071 步。其中 λ=0.25 這個數值相當關鍵：代表只保留了四分之一的微調位移量。webAI 的模型卡提到，曾有一組跳過插值步驟的實驗版本，領域內分數更高（macro gate 達 0.515），但代價是held-out 能力回吐了約 12 個百分點——這組版本最終並未公開釋出。

📊 **五項測驗成績單**

webAI 官方公布的五項形式推理測驗成績如下：

| 測驗項目 | 分數 |
|---|---|
| Rule induction | 96.4 |
| Semantic parsing | 87.6 |
| Lean formalization | 64.6 |
| Exact-format answering | 52.0 |
| Entailment labeling | 68.7 |

在 Track A（領域內形式邏輯）測驗中，TwIL-LM3 的六項平均分數為 0.4488，訓練流程實際 gate 用的 macro gate 分數為 0.4218。這個成績領先包含 LFM2.5-8B-A1B 在內、參數量更大的所有模型（0.4218 對 0.3757，且參數量只有對手的三分之一），但沒有領先兩個最大的模型：Qwen3-8B 的 macro gate 達 0.5336，不過其中大部分來自寬鬆匹配（loose-match）的計分方式，若換成 strict-7 的嚴格標準，兩者其實非常接近（0.2093 對 0.1971）；gpt-oss-120b 則在六項平均分數上以 0.5192 領先 TwIL-LM3 的 0.4488。

效率是 TwIL-LM3 最沒有爭議的優勢：它在 Track B 上生成的回應長度最短，平均 482 個 token，每秒可回答 32.9 題，相較之下 120B 模型每秒僅能回答 4.2 題。

TwIL-LM3 在領域內相對提升 26%（macro gate 由 0.336 提升到 0.422），同時 held-out 核心平均分數也提升 0.022，模型卡指出這是整個專案中唯一在兩個測驗軌道上同時進步的版本：

| Held-out 測驗 | 訓練前 | 訓練後 |
|---|---|---|
| LogicBench | 0.6467 | 0.7167 |
| GSM8K | 0.8833 | 0.8733 |
| IFEval | 0.6767 | 0.6433 |

1.7B 版本則是另一種取捨：macro-primary 分數由未調整 base 的 0.185 提升到 0.361，但 held-out 表現漲跌互見：

| Held-out 測驗 | 訓練前 | 訓練後 |
|---|---|---|
| LogicBench BQA | 0.563 | 0.590 |
| GSM8K | 0.413 | 0.380 |
| ARC-C（chain-of-thought） | 0.587 | 0.463 |

⚠️ **贏的是「效率」與「特定領域」，不是全面碾壓**

從數據可以看出，TwIL-LM3 的優勢集中在參數效率與推理速度，而非全面壓制大模型；GSM8K 與 IFEval 的小幅退步，以及 1.7B 版本在 GSM8K、ARC-C 上的下滑，都顯示形式邏輯專項微調對通用能力有一定代價。且目前授權僅限非商業用途，企業要落地商用仍需另行洽談。

🎯 **實務啟示**

如果你的應用場景明確落在形式邏輯驗證、自動形式化這類任務，且需要在本地端、低延遲、無法呼叫大型雲端模型的環境下運行，TwIL-LM 提供了一個參數量小、推理速度快的選項；但若任務涉及通用推理或數學能力，這次的微調結果提醒我們：領域專項訓練往往伴隨其他能力的取捨，選型前應針對自己的實際任務重新跑一次評測，而非只看單一 benchmark 的排行。

🔗 **來源**
- 標題：webAI Releases TwIL-LM: A 1.7B and 3B Formal-Logic Model Family for Autoformalization on Local Hardware
- 作者／機構：Asif Razzaq（MarkTechPost）
- 連結：https://www.marktechpost.com/2026/08/10/webai-releases-twil-lm-a-1-7b-and-3b-formal-logic-model-family-for-autoformalization-on-local-hardware/

#TwILLM #webAI #Autoformalization #FormalLogic #LocalLLM #SmolLM #LoRA #GRPO #EdgeAI #OpenWeights
