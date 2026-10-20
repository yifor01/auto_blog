---
title: How To Use Decision Models for Evals
source: Hamel Husain
url: https://hamel.dev/blog/posts/decision-model-evals/
model: claude-code/sonnet
generated_at: '2026-10-20T20:52:57.076916'
score: 92
---

📌 決策模型做 eval，閾值 0.50 是陷阱

TL;DR：決策模型省錢又快，但預設 0.50 閾值沒調過，等於把效能留在桌上。

你是否也直接拿 decision model 跑出的分數，用預設閾值 0.50 判定通過或失敗？Hamel Husain 的最新實測顯示，這個「預設」動作可能讓一個本來能完美分類的模型，實際表現直接掛零。

🤔 為什麼不能直接用 0.50

隨著 TypeSafe Jev、Perplexity Decider、Liquid d1、Cloudflare Clef、OpenAI Decisions API 等決策模型相繼登場，它們被視為 LLM judge 之外，更便宜、更快的自動化評測選項。每個模型對一筆 trace（對話與行動紀錄）回傳 0 到 1 的失敗機率分數，API 預設用 0.50 當門檻，高於門檻就判為失敗。

問題在於，各模型對「失敗」與「通過」兩類的分數分布不盡相同。文中舉例：如果一個模型把所有失敗案例都打在 0.40 分、所有通過案例打在 0.10 分，即便用 0.30 當門檻可以完美分類，預設的 0.50 卻會讓它什麼都抓不到。

🧩 用 100 筆租屋客服 trace 實測六款模型

作者用 100 筆公寓租賃 agent 的 trace，任務是找出含錯誤的對話（像是訂房失敗、未正確轉接真人客服），逐一測試 Jev 1.13、Perplexity Decider 1.1 27B、Liquid d1 與 d1-ultra、Cloudflare Clef Flash、OpenAI Decisions（GPT-6 Luna），每個模型吃到相同的評測標準。

評測採二元 pass/fail，用 F1 score（精確率與召回率的調和平均）作為主要指標，並額外設定「精確率與召回率都至少 80%」的業務底線，避免為了湊 F1 分數而犧牲其中一項到不可用的程度。

🧪 閾值怎麼調：交叉驗證找最佳 F1

作者的作法是：用已標記的 traces 和模型分數，做五折分層交叉驗證，在訓練集上找出同時滿足兩個 80% 底線、並最大化 F1 的閾值，再在驗證集上回報精確率、召回率與 F1，並與預設 0.50 比較。這個流程甚至可以直接寫成 prompt 交給 coding agent 執行，不需要重新呼叫模型 API。

📊 誰能同時滿足 80/80？Perplexity 最便宜，OpenAI 分數最高

在精確率與召回率都達到 80% 的候選名單中，Perplexity、Liquid d1-ultra 和 OpenAI Decisions 入選；Liquid d1 和 Clef Flash 即便調整閾值後仍未達標。調整後的比較結果：

| 模型 | F1（調優後） | 成本（每百次評測） |
| --- | --- | --- |
| Perplexity Decider | 0.79 | 0.82 美分 |
| OpenAI Decisions | 0.87 | 3.72 美分（約 4.5 倍） |

文中指出，在這三個候選者中，OpenAI Decisions 在這個任務上把失敗與通過兩類的分數分得最開，F1 最高；但 Perplexity 用約四分之一的成本就拿到接近的效果，形成一條成本與效能的 Pareto 前緣。

💡 分數能不能直接當「信心」用？看校準結果

如果想把模型分數當成機率來用（例如 0.80 分代表 80% 機率失敗），就需要檢查機率校準：同樣分數區間的 traces，實際失敗比例是否吻合。作者發現 Clef Flash 有一組 traces 平均預測失敗機率只有約 8%，但實際失敗率高達 60%，明顯低估風險；而 Jev 與 Liquid d1-ultra 在這份資料上本來就校準得不錯。對校準不佳的模型，可以用 Platt scaling 這類方法重新擬合分數曲線，讓它更貼近實際發生率。

⚠️ 這次比較沒看的事

作者刻意把延遲（latency）排除在比較之外，因為它受很多實驗控制不到的因素影響；文中的 F1 優化也只是「精確率與召回率等權重」的簡化假設，實務上多半不是對等重要，換成 F-beta 之類的指標，調出來的閾值與結果可能不同。

🎯 實務啟示

導入任何決策模型做自動化評測前，先用自己的標記資料跑一次閾值調優，而不是沿用 API 預設的 0.50；同時設定業務上能接受的精確率與召回率底線，再在合格的候選模型裡比較成本與效能，才會得到真正可用的分類器。

🔗 來源
- 標題：How To Use Decision Models for Evals
- 作者／機構：Hamel Husain
- 連結：https://hamel.dev/blog/posts/decision-model-evals/

#LLMEval #DecisionModels #MachineLearning #MLOps #AIEvaluation #F1Score #ModelCalibration #AIAgents #DataScience #PromptEngineering
