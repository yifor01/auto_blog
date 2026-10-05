---
title: 'Yandex Introduces Sona: A Single Generative Recommender That Replaces Entire
  Recommendation Cascade'
source: MarkTechPost
url: https://www.marktechpost.com/2026/10/05/yandex-introduces-sona-a-single-generative-recommender-that-replaces-entire-recommendation-cascade/
model: claude-code/sonnet
generated_at: '2026-10-05T23:19:30.926126'
score: 95
---

📌 Yandex用一個生成式模型砍掉15個以上推薦元件

TL;DR:Yandex的Sona用單一transformer取代候選生成到排序的整條推薦鏈,並通過7天線上A/B驗證。

大多數推薦系統的架構是「接力賽」:候選生成器先跑一段,交給pre-ranker,再交給吃掉數百個特徵的重量級ranker。每一棒各自優化自己的目標,最後一棒能看到的東西,還得看前面幾棒放不放水。Yandex的做法是直接把整條接力賽換成一個人跑完全程。

🤔 **級聯架構的根本問題**

根據Yandex的Sona技術報告,級聯式(cascade)推薦系統的問題在於每個階段各自訓練、各自優化目標,ranker只能看到上游階段放行的候選。Yandex在Yandex Music這個場景的舊架構,就需要消耗數百個特徵,其中包括來自前代推薦transformer「Argus」的訊號。

🧩 **把候選生成與排序塞進同一個共享表示**

Sona的設計是讓候選生成與排序共用同一個使用者表示:encoder針對每個請求只讀取一次聽眾歷史,decoder負責生成候選,Ranking Module則用同一組encoder狀態對候選評分。整個系統不使用任何人工設計特徵,輸入只有紀錄下來的事件欄位(track ID、artist ID、時長、按讚、播放時間、介面旗標)以及學習得到的Semantic ID。在Yandex的智慧喇叭場景中,使用者甚至不需要先選擇歌手、曲風或心情就能開始播放,研究團隊將這稱為「純推薦」場景。

Semantic ID的作法沿用Rajput等人的formulation,每首歌被表示成3個離散代碼的tuple:一個凍結的多模態LLM以prefill-only模式讀取歌曲前90秒的mel-spectrogram,搭配標題、歌手與標籤資訊;接著一個4層的精煉transformer,用InfoNCE對協同過濾的歌曲對齊聆聽行為;最後用residual K-means把結果量化成3個各32,000筆entry的codebook。這個方法打敗了CLMR音訊baseline,Recall@1000從0.8111提升到0.8524。

Encoder需要處理8,192筆過去事件,但完整attention成本太高,因此深度分配並不平均:最近2,048筆事件用7層self-attention處理,較舊的事件只經過cross-attention與1層full-history layer。論文指出,這個設計在推論成本大約減半的情況下,保留了完整attention的大部分品質。2層的decoder透過寬度1,024的constrained beam search生成Semantic ID tuple,並用catalog trie擋掉不合法的前綴,每個tuple會展開成所有共享該代碼的歌曲,再由4層cross-attention組成的Ranking Module,針對共享的encoder memory對這些歌曲評分。

💡 **Rollout Distillation:排序能力從教師模型蒸餾而來**

Ranking Module的訓練來源是一個凍結的Teacher Ranker:一個0.6B參數、同樣不使用人工特徵的transformer,用一年的互動事件資料分兩階段訓練——先做next-item-prediction預訓練,再做multi-head排序微調。拿掉預訓練階段會讓weighted pair accuracy從0.6215掉到0.6153。

訓練過程中,目前的decoder生成beam候選,教師模型對這些候選加上實際曝光紀錄一起評分,Ranking Module再用mean absolute error去回歸這些分數,這個方法被稱為Rollout Distillation。整體joint loss是 L = L_NTP + L_rollout + L_impression,三項損失都會更新共享的encoder。到了上線服務階段,教師模型會被移除。訓練本身是online進行:事件以15分鐘為窗口聚合成session,餵給GPU trainer,新權重每10分鐘更新一次,端到端延遲中位數45分鐘、p99為60分鐘。線上服務跑在NVIDIA Triton Inference Server上搭配CUDA graphs,model FLOPs utilization達到41%。

📊 **7天線上實驗,成績統計顯著**

最終實驗在智慧喇叭上跑了7天線上A/B測試,每個分組隨機抽取15%使用者,Sona取代了超過15個候選生成器、pre-ranking階段與ranking階段,合併成一個服務中的transformer。報告指出,相對於production control,以下所有變化在統計上都顯著,其中Active Users的提升幅度是Argus先前在同一介面上帶來+1.93%增量的2.35倍。

⚠️ **並非首創,但整合程度更完整**

Sona不是第一個端到端生成式推薦系統上線的案例,Kuaishou的OneRec已經是單一encoder-decoder架構;Meta的HSTU Generative Recommenders在2024年就把推薦問題重新表述為針對使用者行為的序列transduction。Sona的差異在於同時做到完整取代整條級聯、完全不用人工特徵、且排序能力經過蒸餾並在線上驗證過。相較之下,OneRec仍仰賴人工設計的特徵路徑與帶reward model的RL,而Sona只用紀錄下來的事件欄位,並從凍結教師模型蒸餾排序能力。需留意的是,不同平臺與指標間的線上增益數字並不能直接互相比較。

🎯 **實務啟示**

如果你的推薦系統正苦於多階段級聯帶來的目標不一致與維護成本,Sona展示的「共享encoder狀態、候選生成與排序共用記憶」路線值得參考,尤其是用凍結教師模型做線上蒸餾、搭配10分鐘級的持續訓練更新,是一個在生產環境可行的折衷方案。

🔗 **來源**
- 標題:Yandex Introduces Sona: A Single Generative Recommender That Replaces Entire Recommendation Cascade
- 作者／機構:Asif Razzaq, MarkTechPost
- 連結:https://www.marktechpost.com/2026/10/05/yandex-introduces-sona-a-single-generative-recommender-that-replaces-entire-recommendation-cascade/

#Yandex #Sona #GenerativeRecommender #RecSys #SemanticID #MachineLearning #TransformerArchitecture #OnlineAB #RecommendationSystem #DeepLearning
