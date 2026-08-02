---
title: 'TimeLens2: Generalist Video Temporal Grounding with Multimodal LLMs'
source: HuggingFace Daily Papers
url: https://huggingface.co/papers/2607.17423
score: 98
model: tencent/hy3:free
generated_at: '2026-07-21T08:28:49.175284'
---

📌 【TimeLens2】打破 MLLM 侷限：讓多模態大模型能精準定位影片中的時間區間

TL;DR：TimeLens2 透過創新獎勵機制，讓 MLLM 能在不同影片與任務中，精準找出動作發生的時間區間。

🎣 **能看懂影片內容，卻說不出「何時發生」？**

目前的影片多模態大語言模型（MLLM）雖然已經可以描述影片中發生了什麼事，但卻很難精準指出支援該描述的「證據區間」究竟是在影片的哪段時間。這就是「影片時序定位」（Video Temporal Grounding）的挑戰：模型必須能在不同長度的影片、不同領域與不同查詢形式下，預測出一組包含變動數量時間區間的結果。

🧩 **將時間證據視為「區間集合」進行最佳化**

現有的訓練策略在處理這類「集合值任務」（Set-valued task）時常面臨困難：長影片的標籤往往依賴脆弱的單次標註，而強化學習（Reinforcement Learning）則容易在區間重疊或片段匹配上出現問題。

TimeLens2 提出了不同的處理方式：
- **時序證據集合化**：在整個監督與最佳化過程中，將時序證據視為一個「區間集合」。
- **TimeLens2-93K 訓練策略**：透過從字幕衍生出的建議（Proposals）、獨立定位、跨代理人共識（Cross-agent consensus）、語義驗證與邊界細化，建構出可靠的多片段監督機制。
- **雙重獎勵機制**：
  - **Temporal Wasserstein Reward**：計算合併區間支援下的精確一維 $W_1$ 距離，這提供了一種密集且無需進行片段匹配（Matching-free）的反饋，即便在預測數量不相等或片段破碎的情況下也能運作。
  - **Temporal IoU**：作為補充，提供精確的重疊度（Overlap）反饋。

📊 **超越參數規模，效能全面超越 SOTA**

在七項基準測試中，TimeLens2 展現了強大的泛化能力：
- **超越大規模模型**：TimeLens2-4B 與 8B 變體取得了 SOTA（State-of-the-art）表現，超越了參數規模高達 397B 的開源模型。
- **相對於 Backbone 的提升**：
  - 2B 變體提升了 14.2 mIoU。
  - 4B 變體提升了 13.0 mIoU。
  - 8B 變體提升了 18.1 mIoU。
  (以上皆相對於其 Qwen2-VL Backbone)

🎯 **實務啟示**

對於開發影片理解應用（如自動剪輯、影片搜尋、內容檢索）的工程師來說，TimeLens2 證明了透過更精確的時序獎勵設計，較小規模的模型也能在複雜的時間定位任務上，擊敗參數規模極大的模型。

🔗 **來源**
- 標題：TimeLens2: Generalist Video Temporal Grounding with Multimodal LLMs
- 連結：https://huggingface.co/papers/2607.17423

#AI #MachineLearning #MLLM #ComputerVision #VideoUnderstanding #TimeLens2 #TemporalGrounding #DeepLearning #ArtificialIntelligence #Research
