---
title: 'Black Forest Labs Releases FLUX 3 Action: A 7B Open-Weights World Action Model
  That Tops RoboLab-120'
source: MarkTechPost
url: https://www.marktechpost.com/2026/09/24/black-forest-labs-releases-flux-3-action-a-7b-open-weights-world-action-model-that-tops-robolab-120/
model: claude-code/sonnet
generated_at: '2026-09-25T20:43:48.816124'
score: 112
---

📌 【Black Forest Labs】7B世界動作模型FLUX 3 Action登頂RoboLab-120

TL;DR：FLUX 3 Action是7B開源世界動作模型，登頂RoboLab-120且可在24GB顯卡運行。

開源機器人策略過去長期得二選一：要嘛選會「預測世界」但很慢的世界動作模型，要嘛選跑得快、但表現普通的視覺-語言-動作模型。FLUX圖片模型背後的Black Forest Labs(BFL)這次想兩者兼得。

🤔 **世界動作模型與VLA的老問題**

開源機器人策略一向得做取捨。像NVIDIA Cosmos 3 Nano這類世界動作模型(World Action Model, WAM)在RoboLab排行榜上表現領先，任務成功率達36.8%，但predicting video的代價很高；VLA(視覺-語言-動作模型)像π0.5跑得快，卻只能達到28.0%的成功率。BFL在B200上測得，Cosmos 3 Nano(FP8)每秒機器人動作所需的處理時間，約為π0.5(BF16)的4.7倍。FLUX 3 Action保留了joint video與action prediction的做法，改用較小的backbone搭配蒸餾(distillation)來縮小速度差距。

🧩 **架構：從FLUX 3多模態骨幹到EE50動作空間**

FLUX 3 Action衍生自多模態的FLUX 3 backbone。其pretraining使用了圖片、影片、音訊資料，其中影片佔訓練token超過95%。文字、影片、機器人狀態被編碼成token，backbone輸出的future tokens被解碼成未來影格，action tokens則被解碼成機器人動作。一筆資料在模型中的流程大致如下：

1. 攝影機影格、機器人狀態、文字指令一併輸入模型
2. 三者被統一編碼為token序列
3. Backbone同時輸出future tokens與action tokens
4. Future tokens解碼為未來影片幀，action tokens解碼為下一段動作序列

Midtraining混合了pretraining資料(佔樣本36.95%)與動作對齊的影片(佔63.05%)，動作資料涵蓋遊戲錄影、第一人稱視角的人手影片、手持夾爪，以及跨14種載具形態(embodiments)的teleoperation資料。多數機器人資料共用一個50維度的末端執行器(end-effector)動作空間，稱為EE50。

一項消融實驗顯示pretraining的重要性：若不做pretraining、只用DROID資料訓練，RoboLab成績停留在1%以下；有了pretraining，同一套訓練流程可以達到11.6%。

📊 **RoboLab-120與真實機臺測試**

RoboLab-120由Isaac Sim中的120個桌面型任務組成，每個任務跑10次試驗，採用DROID風格的Franka機械手臂設置。

| 模型 | 類型 | RoboLab-120任務成功率 |
|---|---|---|
| FLUX 3 Action | WAM，7B | 42.92%(排行榜)；多種子平均42.24%±0.36(FP8導引蒸餾版) |
| Cosmos 3 Nano | WAM | 36.8% |
| π0.5 | VLA | 28.0% |

FLUX 3 Action比Cosmos 3 Nano領先6.1個百分點，參數量卻少了56%。

真實硬體方面，Positronic Robotics在一臺Franka機械手臂上做盲測，10個DROID任務、每個3次嘗試：

| 模型 | 成功次數/總次數 | 成功率 |
|---|---|---|
| FLUX 3 Action | 28/30 | 93.3% |
| Cosmos 3 Nano | 27/30 | 90% |
| DreamZero | 20/30 | 66.7% |
| π0.5 | 13/30 | 43.3% |

速度上，與Cosmos 3 Nano(FP8)相比，FLUX 3 Action的base與guidance-distilled checkpoint在消費級、工作站級、資料中心級GPU上快1.52至3.95倍。每次呼叫會產生32個動作、頻率15Hz，等同2.13秒的動作，而π0.5每次呼叫只產生1.0秒動作，因此BFL選擇用「real-time factor」而非單次呼叫延遲來比較速度。FP8版本的step-distilled checkpoint在工作站與資料中心GPU上比π0.5快1.34至2.28倍，不過在RTX 5090上反而比π0.5慢。

BFL也依循Su et al.(2026)的設定，測試了與GPT 6 Astra的混合控制，讓reasoner可以執行、編輯或取代策略預測的動作。FLUX 3 Action搭配低推理強度時，混合方案完成90%的episode，平均每次成功花費8.77美元、8分08秒；純Astra在最大推理強度下完成100%，但每次成功要花13.47美元、16分23秒。

🧩 **部署與微調**

DROID policy在H200上以BF16運行約需32GB GPU記憶體，搭配FP8量化與text encoder offload可以塞進24GB顯卡。授權採FLUX Kommunity License，限非商業用途。BFL提供三種recipe，各有BF16、FP8版本。團隊可用自己的示範資料微調，BFL公開了DROID recipe與SO-101 LoRA recipe，文件顯示一個SO-101夾取放置技能是從約200筆示範學來的。模型已與NVIDIA合作原生整合進Hugging Face LeRobot，並支援NVIDIA Jetson邊緣部署，文件中也附有遊戲操作與模擬無人機範例。

⚠️ **限制**

模型輸出的是關節目標(joint targets)，沒有內建速度、力量或工作空間限制，應用端必須自行加上這些安全限制。

🎯 **實務啟示**

FLUX 3 Action證明joint video-action prediction不必然犧牲速度。對機器人團隊來說，pretraining(尤其是用非機器人的影片與人手示範資料)對下游任務成功率的貢獻，遠大於只靠機器人示範資料硬train。若要落地部署，務必記得為模型輸出的動作額外包一層安全限制。

🔗 **來源**
- 標題：Black Forest Labs Releases FLUX 3 Action: A 7B Open-Weights World Action Model That Tops RoboLab-120
- 作者／機構：Asif Razzaq, MarkTechPost
- 連結：https://www.marktechpost.com/2026/09/24/black-forest-labs-releases-flux-3-action-a-7b-open-weights-world-action-model-that-tops-robolab-120/

#RoboticsAI #WorldModel #FLUX3 #BlackForestLabs #OpenWeights #RobotLearning #VLA #ImitationLearning #EdgeAI #RoboLab120
