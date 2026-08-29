---
title: 'Hugging Face Unveils Microduck: A $399 Open-Source 25 cm Biped You Train with
  Reinforcement Learning'
source: MarkTechPost
url: https://www.marktechpost.com/2026/08/28/pollen-robotics-hugging-face-microduck-399-open-source-rl-biped-robot/
model: claude-code/sonnet
generated_at: '2026-08-29T11:59:48.401493'
score: 106
---

📌 【Hugging Face最新機器人】399美元開源雙足機器人，用強化學習練出走路

TL;DR：Pollen Robotics推出Microduck，25公分雙足機器人，訓練環境與sim-to-real流程全公開。

多數機器人新品發表只給你一支demo影片，Hugging Face旗下的Bordeaux機器人團隊Pollen Robotics這次反其道而行，直接把訓練迴圈整個公開。

🤔 **從桌上到地上：跟Reachy Mini反著做**

本週Pollen Robotics開放Microduck預購，這是一款25公分高的雙足機器人，走路、坐下、踢腳、直排輪、跌倒後自己站起來，每個動作都是在物理模擬器中訓練出的神經網路策略（policy），再匯出到硬體上執行。售價399美元，訓練環境、reward函式、domain randomization設定與sim-to-real流程全部公開在GitHub上。

Microduck是Pollen在Reachy Mini（已出貨超過1萬臺）之後的作品，但方向完全相反：Reachy Mini是設計來放桌上互動的桌寵，Microduck則是設計來離開桌面、摔倒、再自己爬起來的機器人。

🧩 **硬體規格與訓練架構**

| 項目 | 規格 |
|---|---|
| 尺寸／重量 | 25cm高、14cm寬、不到800g |
| 驅動 | 15顆馬達（腿、頸、頭）+可動喙部（可撿地上物品） |
| 運算 | Rockchip RK3566 + AI加速器、1GB RAM、32GB儲存 |
| 感測 | 前置攝影機（附拍攝指示燈）、雙IMU（機身+頭部）、8×8 ToF LiDAR、麥克風/喇叭、2組NFC天線、Wi-Fi/藍牙 |
| 電力 | 可拆式NP-F550電池，2600mAh，約可用1小時 |

開箱即附7個已訓練好的動作，透過隨附的遊戲手把操控，不用寫程式就能玩：走路、坐下站立、踢腳、抓取、直排輪、跌倒自復位。機器人本身不具備語音功能，但每臺在第一次開機時會生成專屬的音訊識別特徵，並永久保留。

策略是在microduck_rl這個repo中訓練，底層基於mjlab（MuJoCo Warp）並使用PPO演算法。Pollen表示在單張CUDA GPU上、以4096個平行模擬環境訓練，約1至2小時就能練出可用的步態；若手邊沒有GPU，也可以加上`--hf-jobs`參數把同一條訓練指令丟到Hugging Face Jobs上跑。

💡 **sim-to-real的關鍵：把馬達模型做真**

Sim-to-real的重點在致動器模型上。每顆伺服馬達採用BAM M6模型來模擬Dynamixel XL330，涵蓋電壓控制律、反電動勢（back-EMF），以及Coulomb、Stribeck與負載相關摩擦力，而不是用理想化的PD控制器。每個訓練環境還會隨機化電池電壓、負載下的電壓下降、指令延遲與摩擦力大小。齒隙（backlash）變體則會針對RL佈局中14個伺服關節，各自串接±1度（共2度）的齒輪間隙進行訓練——由於真實編碼器裝在間隙輸出端，觀測值本身就會反映這個誤差。

訓練完成的策略會匯出成ONNX格式，並把觀測正規化器（normalizer）直接烘進計算圖中；Pollen特別提醒不要部署手動轉換的checkpoint，原因就在這裡。機器人端由Rust執行環境驅動50Hz的控制迴圈與馬達匯流排，所有策略共用同一個61維的actor觀測空間：48維本體感覺加上twist指令（3維）、頭部姿態（4維）、身體姿態（6維）。正是這個共用介面,讓走路、復位、特技等不同策略可以在運行中即時熱切換；若某個環境用不到某個指令欄位,系統會補零而非直接捨棄。

官方公開的任務清單涵蓋13項：速度追蹤、站立、坐下站立、地面抓取、踢球（70mm、15g球,actor看不到球）、翻滾,以及5種直排輪相關環境。

⚠️ **公開的是訓練配方,不是保證的性能**

素材中並未提供任何量化的成功率或魯棒性數據,這部分仍待實際入手測試驗證。

🎯 **實務啟示**

對做機器人學習或RL研究的工程師來說,Microduck的價值不只是399美元的硬體,而是一整套可直接複製的sim-to-real配方——從致動器建模、domain randomization設定到ONNX匯出流程都公開可查,是低成本驗證RL遷移到真實硬體的現成案例。

🔗 **來源**
- 標題：Hugging Face Unveils Microduck: A $399 Open-Source 25 cm Biped You Train with Reinforcement Learning
- 作者／機構：Michal Sutter, MarkTechPost
- 連結：https://www.marktechpost.com/2026/08/28/pollen-robotics-hugging-face-microduck-399-open-source-rl-biped-robot/

#Robotics #ReinforcementLearning #OpenSource #HuggingFace #Sim2Real #PPO #EdgeAI #BipedRobot #MuJoCo #EmbodiedAI
