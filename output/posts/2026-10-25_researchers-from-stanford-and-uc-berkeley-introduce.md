---
title: 'Researchers from Stanford and UC Berkeley Introduce TokenGate: Token-Gated
  Attention Makes Long-Context Prefill Up to 11.3x Faster'
source: MarkTechPost
url: https://www.marktechpost.com/2026/10/25/stanford-berkeley-tokengate-learned-token-pruning-llm-prefill/
model: claude-code/sonnet
generated_at: '2026-10-25T19:43:11.030059'
score: 110
---

📌 史丹佛、UC Berkeley新模組：Prefill最快加速11.3倍

TL;DR：史丹佛與UC Berkeley推出可訓練token剪枝模組TokenGate，讓長文本prefill最快加速11.3倍。

長文本RAG與agent應用最怕的就是那一長段「還沒開始生成就要先等」的prefill時間。多數剪枝方法在速度與準確率之間只能二選一，史丹佛與UC Berkeley的研究團隊想問：如果讓模型自己學會「哪些token值得看」，是不是能兩者都要？

🤔 **Attention成本隨長度平方成長，剪枝卻容易傷準確率**

Transformer的做法是把每個token都推過每一層，attention成本隨輸入長度平方成長。現有的訓練無關（training-free）剪枝方法雖然便宜，但剪枝比例一高就開始掉準確率；想從架構層面解決，又常常得從頭預訓練一個新模型，成本太高。TokenGate的目標是在不碰原始模型架構的前提下，替既有LLM加上一個「可訓練」的剪枝模組。

🧩 **借用MoE router的梯度技巧，讓Top-K選擇可以被訓練**

TokenGate的forward pass分成3個階段，其中只有prompt裡的文件（document）部分可以被剪枝，問題（question）本身永遠不剪。問題在於Top-K選擇本身不可微分，等於擋住了端到端訓練的路。

研究團隊借用Mixture-of-Experts router的做法：把每個被保留token的分數，轉成該token在gate之上的attention logits偏置（bias）。這個偏置提供了一條梯度路徑，讓訓練訊號能回傳給打分器，再搭配一個可學習的per-head gain與一個可學習的temperature，用來修正「每個query現在只能看到更少key」這件事。

訓練時只用最單純的next-token loss，每一步同時平均「完整上下文」與「隨機預算」兩種loss，讓同一個訓練好的gate可以套用在不同的剪枝預算上，不必為每個預算重新訓練。

📊 **在Qwen3-1.7B上，連隨機剪枝都贏過對手的heuristic**

研究團隊在Qwen3-1.7B上，針對RepoBench-P、2WikiMultihopQA、MultiNews、BioDEX與needle-in-a-haystack（NIAH）五項任務測試，對照FastKV、SlimInfer、DASH、GemFilter、FlexPrefill、MInference等基線方法，且全部用同一套LoRA backbone比較。結果是TokenGate學出來的選擇器在同一層就贏過FastKV的heuristic；更特別的是，即使在TokenGate的backbone上改用隨機選K（random-K），分數也比對手高，研究團隊將這歸因於backbone與剪枝模組之間的「共同適應」(co-adaptation)。

在混合Gated DeltaNet與full-attention層的Qwen3.5-2B上，NIAH 32k測試中，在第3層做gating就能打平完整prefill的準確率，速度卻是完整prefill的3.8倍、FastKV的2.1倍；若把gating提前到第1或第2層，速度可衝到7.8倍，但準確率會有6%以內的落差。要注意FastKV只能剪attention層，而這些加速倍數是不同設定下的自報數據，不能直接相提並論。

| 設定 | 相對完整prefill速度 | 準確率影響 |
|---|---|---|
| 第3層gating | 3.8x | 打平 |
| 第1、2層gating | 7.8x | 落差6%以內 |

⚠️ **訓練變慢，但收斂反而更快**

訓練每一步比純LoRA慢1.3倍，但在5個任務中有4個反而收斂更快，平均訓練時間是1.8對2.2個A100小時。各方法的加速倍數也來自不同的實驗設定，論文附錄C.2列出各剪枝層數，跨方法比較時仍需謹慎解讀。

🎯 **想做長文本inference最佳化的團隊可以直接拿checkpoint試**

GitHub repo需要Python 3.10以上與CUDA PyTorch 2.9以上，選配的FlashAttention-2 key-bias kernel能加速Qwen3的dense推論，代價是1.0到1.1倍的呼叫成本；沒裝的話會自動退回FlexAttention。釋出的checkpoint涵蓋Qwen3-1.7B的全部5項任務，以及Qwen3.5-2B的NIAH版本，程式碼以Apache-2.0授權開源。對正在處理長context prefill瓶頸的工程團隊來說，這是一個可以直接插進現有LoRA pipeline、不用重新設計架構的選項。

🔗 **來源**
- 標題：Researchers from Stanford and UC Berkeley Introduce TokenGate: Token-Gated Attention Makes Long-Context Prefill Up to 11.3x Faster
- 作者／機構：Stanford University、UC Berkeley 研究團隊
- 連結：https://www.marktechpost.com/2026/10/25/stanford-berkeley-tokengate-learned-token-pruning-llm-prefill/

#TokenGate #LLM #Attention #LongContext #Prefill #TokenPruning #MachineLearning #DeepLearning #Qwen3 #OpenSource
