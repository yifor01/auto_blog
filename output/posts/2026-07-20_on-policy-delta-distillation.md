---
title: On-Policy Delta Distillation
source: HuggingFace Daily Papers
url: https://huggingface.co/papers/2607.15161
score: 98
model: tencent/hy3:free
generated_at: '2026-07-20T08:50:45.612179'
---

📌 【HuggingFace Papers】用 Delta 訊號重做 On-Policy Distillation，推理 LLM 短期後訓練更強

TL;DR：OPD² 以教師與基底模型差異作為獎勵訊號，取代直接模仿，提升推理能力轉移。

傳統 on-policy distillation 直接讓學生模型模仿教師的輸出分佈，但這樣做其實綁手綁腳。一篇新論文指出，只要改變監督訊號的定義，就能在數學、科學與程式推理上穩定超越原有做法。

🤔 **On-Policy Distillation 的設計盲點**

On-policy distillation 是一種 reinforcement learning 的替代後訓練方法，它透過教師模型提供 token-level 的監督，來緩解 reward model 帶來的約束。然而論文指出，這個方法雖然已被廣泛研究與應用，其基礎設計仍未被充分探討，特別是直接模仿教師輸出分佈這件事本身可能並非最佳選擇。

🧩 **Delta 訊號：只萃取「推理微調帶來的改變」**

論文提出新的 distillation reward，稱為 delta signal，而非直接模仿教師的輸出分佈。Delta signal 的定義是：教師模型與其「在推理能力 instruction tuning 之前的基底模型」之間的差異。也就是說，它捕捉的是推理微調所引發的變化，因此能提供一個更直接的訊號，用於轉移 reasoning 能力。這個搭配新獎勵的蒸餾方法被命名為 On-Policy Delta Distillation（OPD²）。

📊 **跨領域推理基準的一致勝出**

作者在數學、科學與 code-reasoning 的基準上進行實驗，結果顯示 OPD² 持續優於常規的 on-policy distillation，並且能讓 reasoning LLM 僅透過短時間的後訓練期，就達到強悍的表現。摘要中未提供具體資料與對比數值，僅以「substantially improves」「consistently outperforms」描述趨勢。

🎯 **實務啟示**

對於想要用蒸餾方式把大型推理模型能力壓進小模型的團隊，OPD² 提供了一個明確可落地的替代方案：與其讓學生抄教師最終輸出，不如讓它學「教師相對於未微調基底模型多做了什麼改變」。作者宣稱程式碼將釋出於 GitHub（naver-ai/opd2），後續可直接參考實作。

🔗 **來源**
- 標題：On-Policy Delta Distillation
- 連結：https://huggingface.co/papers/2607.15161

#Distillation #OnPolicyDistillation #ReasoningLLM #ReinforcementLearning #PostTraining #DeltaSignal #OPD2 #MathReasoning #CodeReasoning #HuggingFacePapers
