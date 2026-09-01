---
title: Scale AV Perception Across Vehicle Platforms with NVIDIA Omniverse NuRec
source: NVIDIA Developer
url: https://developer.nvidia.com/blog/scale-av-perception-across-vehicle-platforms-with-nvidia-omniverse-nurec/
model: claude-code/sonnet
generated_at: '2026-09-01T10:47:43.551516'
score: 93
---

📌 【NVIDIA】跨車型感知適應，不用重新蒐集資料

TL;DR：NVIDIA Omniverse NuRec 用既有行車紀錄合成新車型視角，加速感知模型跨車型部署。

同一套自駕感知系統，換到不同車型上，看到的世界卻不一樣。感測器位置變了，紅綠燈可能出現在畫面的不同位置，路緣變得難以辨識，邊緣的行人也可能變得模糊不清。

🤔 **每換一款新車，就要重新收集一次資料嗎？**

自駕堆疊要擴展到新的車系與變體時，感測器位置、校準、視野、遮蔽、車身幾何與時序都會跟著改變，即使底層感知軟體不變，開發者仍必須因應這些差異。為每一款新車型收集並標註真實世界資料成本高昂，車輛開發初期甚至可能連車隊都還不存在，稀有場景也不一定能被捕捉到。真實世界的行車資料仍是驗證系統效能的根本依據，但在完整的目標車型資料集出現之前，合成資料可以幫助團隊提前讓模型適應新配置。

🧩 **NuRec 怎麼把舊資料變成新視角**

NuRec 使用 3D Gaussian splatting 從感測器資料重建真實世界場景，再用於模擬渲染。對於車型適應，NuRec 會重建既有車輛拍攝的行車紀錄，並從目標車輛的視角渲染出新的相機串流。文中提到兩項關鍵能力：

- **Novel-view synthesis（新視角合成）**：透過 gsplat 將 Gaussian 投影到指定相機模型，可以改變相機外參、內參、視野與鏡頭模型，支援 pinhole、fisheye、f-theta 等配置。
- **可重複使用的場景資料與標註**：重建後的場景保留原始的行車軌跡、每個相機的校準參數、動態物件軌跡與地圖資料，這些資產可用來對齊或調整新渲染畫面中的物件、車道、紅綠燈與道路邊界標籤。

🧩 **四步驟工作流程**

文章示範的流程分為四步：

1. 將重建後的行車資料與目標感測器組態配對。
2. 渲染目標視角。
3. 用 NVIDIA Harmonizer 精修畫面。
4. 用輸出結果訓練感知模型。

實作上，開發者可從 Hugging Face 上的 Physical AI NuRec Dataset 下載場景，該資料集包含超過 1,500 段神經重建的行車場景，每段約 20 秒，由六個相機視角重建而成：120 度前方廣角、30 度前方長焦、120 度左右側視角，以及 70 度左右後視角。下載場景後，透過 Docker 執行的 NuRec 容器分兩步驟操作：先用 `export-custom-rig-trajectory` 匯出目標相機的軌跡，再用 `--camera-id` 指定要渲染的相機，對單一目標相機做稀疏渲染以驗證設定是否正確。文中特別提醒，目標相機不需要與原始六個相機一一對應，可以有不同的位置、方向、解析度或校準參數，只要姿態表示在同一個 rig 座標系、鏡頭模型受支援即可。

⚠️ **並非所有視角都能渲染得一樣好**

文章提醒，相機若被放置在遠離觀測軌跡的位置，或朝向原始相機覆蓋不足的區域，渲染品質可能較差。這也呼應了合成資料的定位：它是用來輔助模型提前適應、找出哪些資料缺口需要真實收集，而不是完全取代真實世界資料的收集與驗證。

🎯 **實務啟示**

對於正在把感知堆疊擴展到多款車型的團隊，NuRec 提供了一條不必為每款車型重新收集標註資料的路徑：先用既有行車資料回答「這個場景從目標車型的視角看起來如何」「哪些既有行車資料已經覆蓋了新車型」「幾何變化在哪裡造成弱點」，再針對真正的資料缺口安排真實世界收集，藉此把有限的收集預算用在刀口上。

🔗 **來源**
- 標題：Scale AV Perception Across Vehicle Platforms with NVIDIA Omniverse NuRec
- 作者／機構：Michelle Horton, NVIDIA Developer
- 連結：https://developer.nvidia.com/blog/scale-av-perception-across-vehicle-platforms-with-nvidia-omniverse-nurec/

#NVIDIA #AutonomousDriving #Omniverse #NuRec #SyntheticData #GaussianSplatting #Perception #AVPerception #SimToReal #SelfDrivingCars
