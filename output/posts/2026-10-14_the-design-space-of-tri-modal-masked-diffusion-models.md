---
title: The Design Space of Tri-Modal Masked Diffusion Models
source: Apple ML
url: https://machinelearning.apple.com/research/tri-modal-masked-diffusion
model: claude-code/sonnet
generated_at: '2026-10-14T20:53:05.952106'
score: 99
---

📌 【Apple ML】首個從零訓練的文字、影像、語音三模態擴散模型

TL;DR:Apple 研究團隊發表首個從零開始預訓練的三模態 Masked Diffusion Model,並提出新的 batch size 重參數化方法。

當多數多模態生成模型還停留在「拿一個文字模型去微調出第二種模態」的做法時,Apple 的研究團隊問了一個更根本的問題:如果直接讓一個模型從零開始,同時在文字、影像、語音三種模態上學習,擴散模型的設計空間會長什麼樣子?

🤔 **核心問題:雙模態之外,三模態從零訓練行不行**

論文指出,discrete diffusion models(離散擴散模型)近年已成為 autoregressive 語言模型的有力替代方案,但既有工作多半是「初始化並微調一個單模態 base 模型」來做雙模態生成。這篇論文的切入點不同:研究團隊直接從零開始,在文字、image-text、audio-text 三種資料上預訓練第一個三模態 Masked Diffusion Model (MDM),系統性地探索這個設計空間。

🧩 **方法:系統性掃過 scaling laws、混合比例與噪聲排程**

研究團隊針對多模態擴散模型的設計空間做了系統性分析,涵蓋多模態 scaling laws、不同模態的混合比例(modality mixing ratios)、噪聲排程(noise schedules)、batch size 效應,並提供了最佳化的推理取樣預設值。

其中最關鍵的技術貢獻,是針對 batch size 分析得出的一套全新 stochastic differential equation (SDE) 重參數化方法。這套方法解決了近期研究中「需要手動調最佳 batch size」的痛點:它將 physical batch size(通常依硬體考量決定,例如 GPU 使用率、FLOP 效率、wall-clock 時間)與 logical batch size(用來平衡隨機最佳化過程中梯度變異數的量)解耦,讓兩者可以獨立選擇,而不必再為了訓練穩定性去反覆調整實際的 batch size。

📊 **3B 規模、6.4T tokens 的初步成果**

團隊預訓練了一個展示此統一設計能力的初步模型,規模為 3B 參數、訓練量 6.4T tokens,在文字生成、text-to-image (T2I) 與 text-to-speech (T2S) 任務上都取得不錯的成果。論文將此研究定位為「目前為止對多模態離散擴散模型進行的規模最大的系統性開放研究」。

⚠️ **侷限:目前仍是初步規模的展示模型**

論文本身將這個 3B/6.4T tokens 的模型定性為「preliminary model」,也就是用來驗證統一設計可行性的展示性成果,而非追求極致效能的最終模型,這意味著在更大規模下的表現仍有待後續研究驗證。

🎯 **實務啟示**

對於正在評估多模態生成架構的工程師,這篇論文最實用的部分或許是那套 SDE batch size 重參數化:如果你在訓練自己的 diffusion 模型時,也曾被「best batch size 到底該怎麼選」困擾,將 physical 與 logical batch size 解耦的思路,值得直接拿來參考,而不必等到三模態規模的場景才派上用場。

🔗 **來源**
- 標題:The Design Space of Tri-Modal Masked Diffusion Models
- 作者/機構:Apple ML 研究團隊(含 University of Cambridge、MIT、Google DeepMind 合作者),NeurIPS 2026
- 連結:https://machinelearning.apple.com/research/tri-modal-masked-diffusion

#AppleML #DiffusionModels #MultimodalAI #NeurIPS #MaskedDiffusion #GenerativeAI #ScalingLaws #TextToImage #TextToSpeech #DeepLearning
