---
title: Maximizing AI Factory Performance per Watt with NVIDIA DSX MaxLPS
source: NVIDIA Developer
url: https://developer.nvidia.com/blog/maximizing-ai-factory-performance-per-watt-with-nvidia-dsx-maxlps/
model: claude-code/sonnet
generated_at: '2026-08-22T06:24:14.917748'
score: 87
---

📌 【NVIDIA】AI工廠的瓶頸不是GPU數量,是每瓦產出

TL;DR:NVIDIA DSX MaxLPS 用動態功率分配與熱管理,在固定電力預算內榨出更多AI算力產出。

蓋一座百萬瓦等級的資料中心,多數人直覺以為多塞GPU就能多賺token。但NVIDIA的分析顯示,一座100MW的AI工廠,實際能轉換成算力產出的電力,可能只剩60MW。

🤔 靜態機櫃供電,為什麼會白白浪費電力

傳統資料中心的供電規劃,是假設每個機櫃都可能同時拉滿其標示的最大功率,藉此保護設施應付尖峰需求。但這種做法把每個機櫃當成獨立的「電力孤島」——一個被分配了多餘電力卻用不完的機櫃,無法把這份閒置電力借給隔壁真正需要它來產生token的機櫃。

NVIDIA以一座100MW AI工廠為例說明這個電力預算的流失過程:電網輸入100MW後,20MW分配給設施總務開銷,10MW消耗在機櫃損耗,另外10MW因故障、重啟、checkpointing等操作面的低效率而無法用於AI負載,最終只剩60MW真正提供給AI運算。訓練、後訓練與推論在不同階段(運算尖峰、記憶體受限執行、同步、checkpointing、prefill、decode、閒置間隙、網路受限通訊)對功率的需求都不同,但為了穩定性,機櫃仍必須依照工作負載的尖峰功率去配置,實際用電量在多數時間都低於這個上限。

🧩 MaxLPS的三層最佳化:動態分配、軟體調校、熱效率

DSX MaxLPS(Maximum Land Power Shell)是一整套涵蓋晶片、散熱、系統與軟體的技術組合,鎖定三個層面:

- 動態功率分配:持續監控並把閒置的功率餘裕重新分配給GPU
- 進階每瓦效能技術:透過軟體最佳化,在固定功率預算下提升工作負載層級的效能
- 45°C熱效率與站點設計:採用溫水液冷降低冷卻開銷,把PUE的改善直接轉換成同樣電力包絡下更多的運算量

其中負責動態分配的是Dynamic Power Software(DPS,目前為Developer Preview),它會對資料中心從電網、機櫃到節點、GPU的拓撲進行建模。維運人員先定義資源群組、功率預算與策略,DPS再持續比較「已分配功率」與「實際耗用量」,當某些GPU或機櫃用電低於保留額度時,便把這部分餘裕釋出給同一管理群組中的其他單位——整個站點的電力包絡不變,只是把既有電力用得更有效率。

DPS的控制迴圈包含:蒐集GPU、機櫃、群組層級的功率遙測資料、辨識未使用的容量、在策略允許範圍內重新分配、驗證是否符合核准的群組功率預算,並在電力事件或緊急狀況下盡力回應。NVIDIA舉例,一個540kW的站點若採靜態供電規劃會閒置170kW電力,而MaxLPS動態供電能把這部分餘裕回收,在相同的540kW電力預算內多部署一個機櫃。

另外,DSX Exchange是一套開源的事件匯流排(同樣為Developer Preview),把DPS與建築管理系統、電力監控系統、冷卻基礎設施、電網介面及運算排程器連接起來。MaxLPS運作不需要DSX Exchange,但兩者整合後能讓DPS取得季節性冷卻餘裕、設施功率事件等額外訊號。

除了機櫃層級的功率調度,MaxLPS也內建軟體層的效能調校:針對推論、訓練、記憶體受限、運算受限等常見資料中心運作模式,提供已驗證的工作負載功率設定檔(WPPS),維運人員不必為每項工作逐一調整功率、記憶體、頻率等節點行為。Application Performance and Power Manager(APPM)負責把選定的設定檔套用到參與的GPU,而NVIDIA Dynamo則可進一步最佳化推論服務在機櫃之間的效能與功耗表現。

📊 實測與推估數據

針對NVIDIA Vera Rubin NVL72 AI工廠,NVIDIA推估MaxLPS結合資料中心電力規劃,能在相同電力預算內帶來多達40%的Rubin GPU容量提升。在實測部分,GB200 NVL72以Kimi-K2.5工作負載測試,Vera Rubin NVL72以DeepSeek-R1測試:MaxLPS把GB200 NVL72的機櫃配置功率從125kW降到90kW,在維持工作負載吞吐量的前提下多部署39%的機櫃;Vera Rubin NVL72則從136kW降到101kW,多部署35%的機櫃。每瓦效能方面,GB200 NVL72提升約1.5倍,Vera Rubin NVL72提升約1.3至1.4倍。

💡 這不是新架構,而是把既有電力用得更聰明

值得留意的是,MaxLPS帶來的效能提升並非來自更強的晶片架構,而是透過軟體定義的方式,把原本被靜態供電規劃「困住」的機櫃層級餘裕,在整個機群範圍內重新調度。這種系統性的協調,比逐一手動調校每個機櫃的做法更能反映AI工廠的真實用電型態。

🎯 實務啟示

對負責大規模推論或訓練基礎設施的工程團隊來說,靜態功率配置很可能正在讓機群容量被閒置浪費。若團隊的AI工廠已面臨電力天花板,軟體層級的動態功率管理會是值得評估的方向,而不只是持續等待下一代硬體帶來效能提升。

🔗 來源
- 標題:Maximizing AI Factory Performance per Watt with NVIDIA DSX MaxLPS
- 作者/機構:Tanya Lenz,NVIDIA Developer
- 連結:https://developer.nvidia.com/blog/maximizing-ai-factory-performance-per-watt-with-nvidia-dsx-maxlps/

#NVIDIA #AIInfrastructure #DataCenter #PowerEfficiency #AIFactory #GPU #Inference #Sustainability #MachineLearning #CloudComputing
