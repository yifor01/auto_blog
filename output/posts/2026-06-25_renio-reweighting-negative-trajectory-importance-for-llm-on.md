---
title: 'ReNIO: Reweighting Negative Trajectory Importance for LLM On-Policy Distillation'
source: HuggingFace Daily Papers
url: https://huggingface.co/papers/2606.23104
score: 95
model: google/gemma-4-31b-it:free
generated_at: '2026-06-25T20:24:50.665227'
---

📌 ReNIO：透過負向軌跡重新加權，提升 LLM 在推理任務的蒸餾效能

TL;DR：利用 token 層級的機率比率對負向軌跡重新加權，最佳化 LLM 在數學與程式碼生成任務的 on-policy 蒸餾效果。

在大型語言模型（LLM）的蒸餾過程中，如何有效利用「錯誤的生成路徑」來指導模型避坑，一直是提升推理能力的核心挑戰。

🤔 **On-policy 蒸餾中的負向路徑問題**

在 on-policy 蒸餾流程中，模型會根據當前策略生成多條路徑（trajectories）。然而，並非所有失敗的路徑都具有相同的指導價值。若能精準識別並調整這些負向軌跡的權重，模型能更有效地學習哪些生成方向應被避免。

🧩 **ReNIO 的核心機制：Token 層級的重新加權**

ReNIO 提出了一套重新加權機制，旨在最佳化負向軌跡的重要性評估：

- 監控 Token 機率比率：透過計算 token 層級的機率比率（probability ratios）來重新評估負向軌跡的權重。
- 強化負向指導：不再將所有失敗路徑一視同仁，而是根據機率分佈對其重要性進行調整，使模型在蒸餾過程中能更精準地學習。

📊 **在數學與程式碼生成任務中表現提升**

根據研究結果，ReNIO 在以下兩類高邏輯要求的任務中展現出顯著的效能提升：
- 數學推理任務 (Mathematical Tasks)
- 程式碼生成任務 (Code Generation Tasks)

🎯 **實務啟示**

對於從事 LLM 蒸餾或對齊（Alignment）的工程師來說，ReNIO 提供了一個新的思考方向：在處理負面樣本時，不應僅將其視為「錯誤」而簡單排除或均等處理，透過 token 層級的機率分析來重新分配權重，可能是提升模型推理能力的一種有效手段。

🔗 **來源**
- 標題：ReNIO: Reweighting Negative Trajectory Importance for LLM On-Policy Distillation
- 連結：https://huggingface.co/papers/2606.23104

#LLM #Distillation #OnPolicy #Reasoning #Mathematics #CodeGeneration #ReNIO #MachineLearning #DeepLearning #NLP
