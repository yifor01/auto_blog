---
title: Sakana AI Releases Namazu Small, a 30B Model Built on Nemotron 3 Nano
source: MarkTechPost
url: https://www.marktechpost.com/2026/11/26/sakana-ai-namazu-small-30b-nemotron-3-nano/
model: claude-code/sonnet
generated_at: '2026-11-27T01:08:20.144919'
score: 95
---

📌 30B打敗120B？Sakana AI靠續訓練改寫效率劇本

TL;DR：Sakana AI以NVIDIA Nemotron 3 Nano為底續訓練出30B模型Namazu Small，自報25項benchmark平均成績超越NVIDIA自家120B的Nemotron 3 Super。

一個3B啟用參數的小模型，在網路研究類評測上把120B模型甩開將近一倍分數，這聽起來違反直覺，但Sakana AI在Namazu Small的發布資料裡就是這麼宣稱的。

🤔 **從別人的底座，練出自己的模型**

Sakana Namazu是Sakana AI的命名系列，代表「在開源模型基礎上，完成自家後訓練」的產品線。比較大的Namazu版本是基於Kimi K2.6打造，而這次發布的Namazu Small則是系列中較輕量的成員，起點是NVIDIA Nemotron 3 Nano的預訓練基礎模型，而不是NVIDIA已經做完後訓練的版本。Sakana團隊從這個預訓練base出發，自行進行continued pretraining（持續預訓練）與post-training（後訓練），沿用的是他們為原版Namazu開發的方法。目標很明確：日常對話、搭配網路搜尋的研究任務、以及長文件問答，被定位為一個reasoning model（推理模型），會先組織所需資訊再逐步推理出答案。

🧩 **底層仍是NVIDIA的混合架構**

Nemotron 3 Nano本身是一個hybrid Mamba-Transformer混合專家（MoE）模型，官方資料顯示總參數30B、啟用參數3B，支援長達1M token的context。Sakana選擇這個底座做續訓練，等於是在NVIDIA打好的基礎架構上，加上自己的資料與訓練手法重新雕琢。評測時，Namazu Small被拿來和兩個NVIDIA自家完成後訓練的模型比較：Nemotron 3 Nano（30B-A3B）與Nemotron 3 Super（120B-A12B），測試套件涵蓋三大類、共25項benchmark，所有成績均為Sakana自行報告。

📊 **網路研究類大幅領先，封閉知識類明顯落後**

成績呈現明顯的兩極化：

| 評測項目 | Namazu Small | Nemotron 3 Super | Nemotron 3 Nano |
|---|---|---|---|
| BrowseComp | 73.5 | 36.1 | 29.3 |
| DeepSearchQA | 84.3 | 65.4 | — |
| LLM-jp LongBench | 86.0 | — | 67.0 |
| FaithEval | 78.3 | 59.1 | — |
| SimpleQA Verified | 6.8 | 18.1 | 9.1 |
| Japanese SimpleQA | 8.0 | 24.9 | — |
| HealthBench | 40.6 | — | 47.5 |

在需要上網查資料與長文件引用的任務（如LongBench-Cite拿到80.2分、ALCE拿到60.2分）上，Namazu Small表現突出；但在封閉書本、僅憑模型內部知識作答的任務上明顯較弱，SimpleQA Verified僅6.8分，低於Super的18.1分與Nano的9.1分，Japanese SimpleQA與HealthBench也都低於對照模型。Sakana自己也承認，單靠模型內部知識的任務改善有限。整體而言，Namazu Small在25項測試中贏過Super的有13項，贏過Nano的則有22項。

⚠️ **數字是自報的，封閉知識是弱點**

所有評測成績均由Sakana自行公布，尚無第三方驗證。而且落差明顯集中在需要模型「憑記憶回答」而非「查資料再回答」的任務類型，顯示這次續訓練強化的是檢索與長文整合能力，而非模型本身的知識儲備。

🎯 **實務啟示**

如果你要打造的是搭配網路搜尋或長文件閱讀的agent應用，Namazu Small展示了一條用較小啟用參數、透過續訓練針對特定任務強化的路徑，值得關注；但若應用場景偏向封閉知識問答，這個模型目前看起來不是合適選擇，且建議在導入前自行驗證這些自報數據。

🔗 **來源**
- 標題：Sakana AI Releases Namazu Small, a 30B Model Built on Nemotron 3 Nano
- 作者／機構：Michal Sutter／MarkTechPost
- 連結：https://www.marktechpost.com/2026/11/26/sakana-ai-namazu-small-30b-nemotron-3-nano/

#SakanaAI #Nemotron #LLM #ReasoningModel #MixtureOfExperts #WebResearch #LongContext #NVIDIA #AIBenchmark #OpenModels
