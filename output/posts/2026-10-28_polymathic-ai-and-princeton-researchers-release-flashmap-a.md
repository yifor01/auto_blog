---
title: Polymathic AI and Princeton Researchers Release FlashMap, a Flow Map Drafter
  for 6.14x Faster LLM Decoding
source: MarkTechPost
url: https://www.marktechpost.com/2026/10/28/flashmap-flow-map-speculative-decoding/
model: claude-code/sonnet
generated_at: '2026-10-28T21:50:36.953038'
score: 101
---

📌 FlashMap：用連續流映射取代離散擴散 drafter，LLM 解碼最高加速 6.14 倍

TL;DR：FlashMap 一次生成整個 16-token 區塊做投機解碼（speculative decoding）草稿，Qwen3-8B 在 GSM8K 上最高加速 6.14 倍。

投機解碼的草稿模型（drafter）常把區塊內每個位置獨立猜測，問題是猜出「new diego」或「san york」這種語意不通的組合時，目標模型一到第二個 slot 就得打掉重練。Polymathic AI、Princeton 大學、USC ISI、NYU 與 Flatiron Institute 聯手提出的 FlashMap，想用一步生成整個區塊、且區塊內彼此一致的方式解決這個問題。

🤔 **區塊內的 token，該不該「獨立猜」**

標準的投機解碼讓小的 drafter 模型提出 K 個 token，目標模型再用 1 次平行前向傳播檢查全部 K 個，保留最長的匹配前綴，輸出結果與目標模型本身完全一致（lossless）。速度取決於兩件事：草稿被接受的 token 數量，以及產生這些草稿的成本。EAGLE-3 用自回歸方式逐個生成草稿，成本隨區塊長度增加；DFlash 則用 block diffusion 一次生成整個區塊，但它是獨立預測區塊內每個位置（研究團隊稱之為 factorized approximation）。例如續寫「new york」或「san diego」機率相同時，獨立的 drafter 有一半機率會生成「new diego」或「san york」這種不通的組合，導致目標模型在第二個 slot 就拒絕。

🧩 **一步生成整個一致的區塊**

FlashMap 建立在 Flow Map Language Models 之上，核心做法是把高斯噪聲（Gaussian noise）直接映射成完整的一個 16-token 區塊，每一個噪聲樣本會同時決定區塊內所有位置的模式（mode），因此區塊內的 token 彼此一致，不會出現「new diego」式的語意斷裂。drafter 本身是一個 6 層區塊的 diffusion transformer（DiT），embedding 維度 2048、16 個 attention head，讀取目標模型第 1、9、17、25、33 層的隱藏狀態（hidden states）。drafter 的 embedding 矩陣與 LM head 直接複製自目標模型，並保持凍結（frozen）。

📊 **訓練規模與實驗結果**

FlashMap 與作為對照的 DFlash 皆使用 Open-PerfectBlend 的 50 萬筆樣本訓練，所有模型與 ablation 加總的運算量約為 4,600 GPU 小時（H200）。研究團隊也在相同資料與設定下重新訓練了 EAGLE-3 與 DFlash，以確保對照公平。測試涵蓋數學、程式碼與對話共 9 個 benchmark，並在 temperature 0 與 1 下分別評估，另外用 shuffle test 檢驗草稿是否真正利用了 token 間的結構關聯。在 Qwen3-8B 上，研究團隊回報 GSM8K 最高達 6.14 倍的 lossless 加速。實驗顯示，FlashMap 在 2 個推理步驟（steps）時，就能保留 16 步教師模型（teacher）joint-structure 收益的大部分；但降到 1 步時，只能保留一小部分收益。另外，將 4 個噪聲樣本組成樹狀結構（tree）進行草稿，平均可再帶來 11% 的加速（此平均值為 MarkTechPost 依論文 Figure 1(c) 計算所得）。

🧩 **怎麼用**

FlashMap 套件僅需 torch 與 transformers>=4.56，可用 `uv pip install flashmap` 安裝，呼叫 `spec_generate` 即可在單張 GPU 上同時跑 drafter 與目標模型。專案頁面提供 vLLM 與 SGLang 兩種 serving 路徑，將 `num_steps` 設為 2 可以用些許速度換取更高的接受率；若要在 temperature 高於 0 時取樣，vLLM 需要設定 `"draft_sample_method": "probabilistic"`。Qwen3-8B 與 Qwen3-4B 的 drafter 權重已上傳 Hugging Face。

⚠️ **限制**

在 1 個推理步驟時，FlashMap 只能保留教師模型 joint-structure 收益的一小部分，代表若追求極致速度而壓低步數，品質上的收益會明顯打折。

🎯 **實務啟示**

如果你的推理服務已經在用 EAGLE 類的投機解碼做加速，FlashMap 提供了一個現成、附帶 vLLM/SGLang 插件與 Hugging Face 權重的替代 drafter 方案，值得針對自己的模型與 workload 實測其加速比與接受率的取捨。

🔗 **來源**
- 標題：Polymathic AI and Princeton Researchers Release FlashMap, a Flow Map Drafter for 6.14x Faster LLM Decoding
- 作者／機構：Asif Razzaq，MarkTechPost
- 連結：https://www.marktechpost.com/2026/10/28/flashmap-flow-map-speculative-decoding/

#SpeculativeDecoding #FlashMap #LLMInference #FlowMatching #DiffusionModels #Qwen3 #vLLM #SGLang #PrincetonUniversity #MachineLearning
