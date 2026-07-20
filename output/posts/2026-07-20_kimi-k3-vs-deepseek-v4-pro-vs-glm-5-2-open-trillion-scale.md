---
title: 'Kimi K3 vs DeepSeek V4 Pro vs GLM-5.2: Open Trillion-Scale MoE Models Compared
  on Benchmarks, License, and Serving Cost'
source: MarkTechPost
url: https://www.marktechpost.com/2026/07/18/kimi-k3-vs-deepseek-v4-pro-vs-glm-5-2-open-trillion-scale-moe-models-compared-on-benchmarks-license-and-serving-cost/
score: 94
model: tencent/hy3:free
generated_at: '2026-07-20T08:52:35.246975'
---

📌 【MarkTechPost 整理】Kimi K3、DeepSeek V4 Pro、GLM-5.2 三款兆級 MoE 開源模型實測比較

TL;DR：三款中文實驗室開源 MoE 模型比能力、授權與推論成本，Kimi K3 智慧指數暫居開源第一。

三家來自中國的實驗室，如今同時站上開源權重（open-weight）排行榜頂端。當模型引數衝破兆級、上下文來到百萬 token，團隊真正要決定的從來不是「誰最強」，而是「能不能用、授權卡不卡、跑起來貴不貴」。

🤔 **三款模型都是稀疏 MoE，但規模差很大**

Moonshot AI 的 Kimi K3、DeepSeek 的 V4 Pro，以及智譜 AI（Zhipu AI）的 GLM-5.2，都是稀疏 Mixture-of-Experts（MoE）架構，具備百萬 token 上下文視窗，主攻長程編碼與 agent 工作負載。

所謂「兆級引數」並非三者皆然：
- Kimi K3：總引數 2.8T（2.8 兆），DeepSeek V4 Pro：1.6T。
- GLM-5.2：總引數 744B，是三者中總引數最小的一款；它入榜是因為在 K3 釋出前曾領先開源權重領域。

🧩 **各家架構與釋出重點**

- Kimi K3：2.8T 引數的 Stable LatentMoE 模型，每個 token 啟動 896 個專家中的 16 個；Moonshot 未公開確切的活躍引數量。特色包含原生視覺（native vision）、1M token 上下文、以及 always-on reasoning；Moonshot 稱其為首個開源 3T 等級模型。
- DeepSeek V4 Pro：1.6T 引數 MoE，活躍引數 49B，採用 384 個 routed experts 加 1 個 shared expert；具 1M token 上下文與 384K 最大輸出。另有較小的 V4 Flash 變體（總引數 284B、活躍 13B）應對低成本負載；權重已放於 Hugging Face。
- GLM-5.2：744B 引數 MoE，活躍引數約 40B，1M token 上下文；智譜提供 High 與 Max 兩種 reasoning 模式，並附 API 存取。

📊 **用同一套評測看智慧指數，K3 暫居開源之首**

各實驗室自行公佈的 benchmark 分數因評測框架不同而難以直接對比，文中採用中立的 Artificial Analysis Intelligence Index 作為共同比較基準：
- Kimi K3：約 57
- GLM-5.2：51
- DeepSeek V4 Pro（Max reasoning）：44

K3 整體排名第 3，僅次於 Claude Fable 5 與 GPT-5.6 Sol，與 Opus 4.8、GPT-5.5 相近；GLM-5.2 在 K3 釋出前曾穩坐開源權重第一。編碼基準呈現類似趨勢，但原文摘要在此處截斷，未提供完整資料。

⚠️ **比較時的兩個前提限制**

- 各廠商自報分數使用的 harness 不同，跨實驗室逐項比對並不嚴謹，只能依賴第三方統一評測。
- 摘要未提及三款模型的授權條款細節與實際推論成本數字，僅指出文章從「授權條款」與「serving cost」兩軸比較，具體內容需參考原文。

🎯 **實務啟示**

對 AI/ML 團隊來說，這三款模型代表開源權重首次在規模與長上下文上逼近頂級閉源模型。選型時不應只看總引數，活躍引數與變體（如 V4 Flash）才是影響推論成本與部署門檻的關鍵；若需穩定橫向比較，優先參考 Artificial Analysis Intelligence Index 這類統一基準，避開各廠商自報數字的框架偏差。

🔗 **來源**
- 標題：Kimi K3 vs DeepSeek V4 Pro vs GLM-5.2: Open Trillion-Scale MoE Models Compared on Benchmarks, License, and Serving Cost
- 作者／機構：Michal Sutter @ MarkTechPost
- 連結：https://www.marktechpost.com/2026/07/18/kimi-k3-vs-deepseek-v4-pro-vs-glm-5-2-open-trillion-scale-moe-models-compared-on-benchmarks-license-and-serving-cost/

#MoE #KimiK3 #DeepSeek #GLM #OpenWeights #LLM #Benchmark #MixtureOfExperts #ServingCost #ModelComparison
