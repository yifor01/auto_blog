---
title: How Claude is uplifting biomolecular modeling
source: Anthropic Research
url: https://www.anthropic.com/research/claude-uplifts-biomolecular-modeling
model: claude-code/sonnet
generated_at: '2026-09-17T20:26:06.520702'
pinned: true
---

📌 【Anthropic】Claude 花不到四週優化 30 多個生物模型，速度平均快 4 倍

TL;DR：Claude 自主優化 30 多個開源結構預測與蛋白質設計模型，平均加速 4 倍，並開源全部程式碼。

過去讓 AI 設計一個能精準結合特定標靶的全新蛋白質，得砸下高達 1 萬美元、相當於 2500 個 NVIDIA H100 GPU 小時的算力，這樣的門檻幾乎把絕大多數研究者擋在門外。Anthropic 這次的做法是反過來優化模型本身，而執行優化的不是工程團隊，是 Claude。

🤔 昂貴的蛋白質設計，卡在算力

de novo 蛋白質結合體（binder）是透過運算設計、能緊密附著在特定標靶分子上並發揮活化、阻斷或遞送功能的小型蛋白質。Anthropic 先前展示過 Claude 能透過專家級的協調能力，指揮開源蛋白質設計與結構預測模型完成這類設計，但過程中允許 Claude 為每個標靶花費最高 1 萬美元的 Modal 算力，遠超一般蛋白質設計者能負擔的規模。為了讓這類研究更容易被更廣泛的社群使用，Anthropic 開始探索如何讓這些模型跑得更有效率。

🧩 針對 triangle attention 與 triangle multiplication 動刀

AlphaFold3、OpenFold3、Boltz-2 等現代結構預測模型，主要的運算時間與記憶體都花在 triangle attention 與 triangle multiplication 這兩個作用於三元組 token 的運算上。這兩個操作能建構生物分子系統的幾何關係，但運算量是立方成長的，系統大小加倍會讓時間與記憶體需求增加 8 倍，變成三倍則暴增 27 倍。

Anthropic 讓 Claude 開發了一套名為 FlashPairformer 的客製化 kernel，用來加速這兩個運算，並在此基礎之上，針對每個模型分別進行更細緻的優化，例如快取重複計算的結果、把無效分支簡化成常數輸出。整個過程由兩位熟悉生物分子建模、但完全沒有 kernel 工程或推論優化經驗的 Anthropic 技術人員監督，Claude 在不到四週內完成了超過 30 個開源模型的加速，涵蓋結構預測、蛋白質設計、蛋白質語言模型與基因體學任務。

📊 平均快 4 倍，部分場景輸出完全一致

| 項目 | 效能提升 |
|---|---|
| 結構預測模型平均加速（容許些微精度損失） | 約 4 倍 |
| 結構預測模型平均加速（輸出完全一致） | 約 1.6～2 倍 |
| FlashPairformer：triangle attention 加速（相較業界標準） | 2.7～2.9 倍 |
| FlashPairformer：triangle multiplication 加速（相較業界標準） | 1.7～3.2 倍 |
| 蛋白質設計整體所需算力 | 減少約兩個數量級的 GPU 小時 |

每個模型的加速版本都經過確認，在下游任務（如結構預測準確度）上沒有受到影響；預測介面的可接受標準採用 DockQ 分數大於 0.23。Claude 同時也優化了模型的記憶體使用效率，開發出低記憶體模式，讓單一 NVIDIA GPU node 就能準確預測超過 1 萬個 token（涵蓋胺基酸、核苷酸與小分子、離子的原子）規模的生物分子系統。

⚠️ 尚未涵蓋的比較對象

Anthropic 特別註明，ColabFold 1.6.3 同期釋出的選用加速 kernel 尚未被納入此次基準測試，代表目前的比較結果還不是業界最新方案的全貌。

💡 開源程式碼與百萬美元蛋白質設計競賽

Anthropic 已將所有優化後的程式碼開源，並發布技術報告供社群參考。同時，Anthropic 與長期舉辦開放蛋白質設計競賽的 Adaptyv Bio 共同贊助一項競賽，鎖定五個目前 AI 能力前緣的挑戰問題。在 Modal 與 Twist Bioscience 的支持下，雙方共同投入最高 100 萬美元的 Claude 額度、25 萬美元的 Modal 運算額度，並提供超過 5000 個設計的濕實驗室（wet lab）驗證。

🎯 實務啟示

這個案例說明一件事：推論優化與 kernel 工程不必然要由深諳硬體加速的專家團隊完成。只要有足夠的領域知識搭配前沿模型的自主優化能力，原本要花上數週、且優化成果難以在模型間轉移的工作，也可能被大幅壓縮。對做生物資訊或高效能運算的工程團隊來說，開源的 FlashPairformer 與優化程式碼是值得直接參考、甚至套用到自家模型的資源。

🔗 來源
- 標題：How Claude is uplifting biomolecular modeling
- 作者／機構：Anthropic
- 連結：https://www.anthropic.com/research/claude-uplifts-biomolecular-modeling

#Anthropic #Claude #ProteinDesign #StructurePrediction #AlphaFold #Bioinformatics #GPUOptimization #DrugDiscovery #OpenSource #AIforScience
