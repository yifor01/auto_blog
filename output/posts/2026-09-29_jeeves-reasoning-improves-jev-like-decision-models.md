---
title: Jeeves. Reasoning improves Jev-like decision models
source: Hacker News
url: https://github.com/PostHog/jeeves
model: claude-code/sonnet
generated_at: '2026-09-29T21:42:39.675784'
score: 91
---

📌 Jeeves：讓Jev式分類器先想清楚再決定

TL;DR：PostHog開源9B推理分類器，決策前先思考，準確率贏過Jev與Kev-9B。

多數分類器要嘛快但不夠準，要嘛得靠額外的推理模型當備援。Jeeves想把「思考」這件事直接內建進分類器本身，而不是外掛一個更大的模型。

🤔 **Jev式模型的老問題：準但不夠準**

Jev-like模型能輸出校準過的決策機率，但準確率偏低，導致許多pipeline得依賴推理模型當fallback。Jeeves的做法是訓練一個Jev-like的Qwen3.5-9B（搭配LoRA與pointer head），用CISPO讓它在做決策前先進行推理，藉此提升分布外（out-of-domain）任務的表現。

🧩 **Pointer Head與特殊token的設計**

Jeeves把問題、狀態與答案選項套進Qwen的對話模板，讓模型先跑一段`<think>`推理鏈，推理結束後重新列出問題與選項，再由一個pointer head對每個選項評分：具體是在`<decide>`位置的hidden state做query投影，與每個選項`</opt>`位置的hidden state做key投影，計算縮放點積（scaled dot product）。這些特殊標記借用了Qwen tokenizer裡幾乎未被使用的稀有token（如`<|fim_prefix|>`等）。README提到的消融實驗（ablation）發現，若改用「State」這類一般文字取代特殊token，或省略推理後重複問題的步驟，效果都會變差。最終機率是選項分數的softmax，並除以一個在dev set上校準的溫度值。

訓練分兩階段：先做SFT（2個epoch，8張GPU跑596步），LoRA rank=16覆蓋Qwen3.5-9B所有投影層加pointer head，訓練資料來自12個公開資料集與合成政策資料共19,126題，其中一半附帶從base model取樣的推理鏈；接著用CISPO跑624步排程（在第402步提前停止），透過9,992題RL資料、每題8次rollout、溫度1、推理上限2,560 token進行強化學習。README特別提到，超過402步後calibration會因RL資料飽和而過度尖銳化，因此選擇在此提前停止。

為了加速推理，專案還附上受Orthrus啟發的diffusion drafter：不同於Orthrus只支援attention-only模型，Jeeves的drafter讓mask token能cross-attend Qwen3.5的Gated DeltaNet層的post-convolution key/value，藉此支援這類混合架構。

📊 **測試集與JevBench上的表現**

| 基準 | Kev-9B | Jev | Jeeves |
|---|---|---|---|
| Test overall（分布外＋held-out） | 0.822 | 0.857 | 0.889 |
| JevBench overall（231題公開） | 0.715* | 0.866 | 0.935 |
| JevBench hard（111題公開） | 0.451* | 0.730 | 0.865 |
| Held-out rule structures | 0.896 | 0.885 | 1.000 |
| Transfer overall（MMLU-Pro／buried state） | 0.579 | 0.800 | 0.746 |

（*標記為Kev-8B數字，官方未公布Kev-9B在JevBench的成績）

速度方面，不啟用思考時約0.3秒／請求，啟用思考後在一張H100上中位數約3.3秒；透過截斷推理鏈長度（`max_think`）與`nothink_threshold`可以在準確率與延遲間取捨，例如把`max_think`設為768並搭配nothink_threshold 0.9，dev集準確率從全推理的0.825降到0.806，但中位延遲從3.3秒縮到2.0秒。

🛠 **怎麼用：Jev相容API與Python SDK**

安裝後可直接下載官方權重並啟動伺服器（`python -m inference.serve`），或自行訓練後用`export.py`融合成獨立模型再serve。API走`/v1/systemone`端點，請求格式與Jev相容，同一次請求可混合yes/no（noul）、多選（choice）、評分（score）三種題型。專案也提供`sdk/`作為Jev官方Python SDK（typesafe-sdk）的直接替代品，介面幾乎一致。

⚠️ **並非全面領先**

數據顯示Jeeves並非在所有基準都贏過Jev：Transfer overall（0.746 vs 0.800）與MMLU-Pro（0.739 vs 0.840）上Jeeves反而低於Jev，說明它在分布遷移任務上的泛化仍有落差。此外完整推理模式延遲較高（中位3.3秒、p90達17.1秒），且FP8 kernel僅支援Hopper架構GPU，部署門檻不低。

🎯 **實務啟示**

如果你的pipeline正在用Jev式分類器搭配額外推理模型當fallback，Jeeves提供了一條把「思考」直接內建進分類器的路徑，且完整開源訓練程式碼與train/dev/test資料，方便直接復現或在自有資料上重新訓練。API與SDK都刻意做成Jev相容，遷移成本低；但上線前建議依自身任務對照上表，確認遷移後的表現是否真的優於既有方案。

🔗 **來源**
- 標題：Jeeves. Reasoning improves Jev-like decision models
- 作者／機構：PostHog（Hacker News 分享者：nicowaltz）
- 連結：https://github.com/PostHog/jeeves

#LLM #MachineLearning #Classification #ReinforcementLearning #Qwen #PostHog #ModelServing #Inference #AIEngineering #OpenSource
