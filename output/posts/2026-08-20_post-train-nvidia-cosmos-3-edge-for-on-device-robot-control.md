---
title: Post-Train NVIDIA Cosmos 3 Edge for On-Device Robot Control
source: NVIDIA Developer
url: https://developer.nvidia.com/blog/post-train-nvidia-cosmos-3-edge-for-on-device-robot-control/
model: claude-code/sonnet
generated_at: '2026-08-20T06:30:41.384587'
score: 95
---

📌 【NVIDIA】後訓練 Cosmos 3 Edge,機器人不必等雲端 GPU

TL;DR:NVIDIA教學:後訓練4B模型Cosmos 3 Edge,讓機器人擺脫雲端GPU。

世界模型(world model)理論上是機器人學習物理互動的絕佳基礎,但體積往往大到只能待在資料中心,直到 NVIDIA 把它塞進了機器人本體。

🤔 世界模型很聰明,但塞不進機器人

機器人需要能適應自身感測器、環境與任務的策略(policy),而且要能在機載運算硬體上運作。世界模型雖然提供了物理互動的學習基礎,但模型體積常讓裝置端部署變得困難。部署到實體機器人有兩個實際限制:一是裝置記憶體,模型與執行期狀態必須塞進機器人可用的記憶體;二是控制延遲,整條推論管線的速度必須跟上機器人所需的控制頻率。

🧩 4B 模型,如何同時解決記憶體與延遲兩大限制

Cosmos 3 Edge 是 Cosmos 3 家族中的 4B 全模態(omni)模型,內建一個以 NVIDIA Nemotron 為基礎的 2B 推理器(reasoner)。它與 Cosmos 3 Nano、Cosmos 3 Super 使用同一套物理世界資料進行預訓練,因此一開始就具備物體如何移動、互動的基礎理解。關鍵在於它體積夠小,可以直接跑在 NVIDIA Jetson Thor 上。後訓練(post-training)正是用來同時解決記憶體與控制延遲這兩個限制:後訓練出的策略模型能塞進 Jetson Thor 的記憶體,讓推論直接在機器人本體完成,不必仰賴資料中心 GPU。

🧩 7.6 萬筆遙操作軌跡,四步驟後訓練流程

教學使用的資料集是 nvidia/Cosmos3-DROID,包含 7.6 萬筆成功的遙操作(teleoperated)軌跡,約 350 小時、涵蓋 86 種任務與 564 個場景,由 Franka Panda 機械手臂搭配 Robotiq 夾爪蒐集,以 LeRobotDataset v3.0 格式、640×360 解析度封裝。準備資料分三階段:過濾閒置與非任務畫面、篩選成功示範、訓練時套用隨機裁切、縮放與色彩抖動(color jitter)。

後訓練的關鍵設定包括:動作空間為 8 維絕對關節位置(7 關節加夾爪)、啟用本體感知(proprioception)、觀測畫面由腕部與兩個外部視角相機組成的 3-camera canvas(合成 540×640)、每次預測輸出 15Hz 下未來 32 個動作的 action chunk、學習率 2e-4、全域批次量 8192(32 樣本/rank × 256 rank,HSDP 32×8)、長餘弦衰減排程,每 1000 次迭代存一次檢查點。整套流程分四步:下載資料集、把基礎檢查點轉成分散式檢查點(DCP)格式、套用資料篩選、啟動訓練腳本。要從 Cosmos 3 Nano 的訓練腳本改成訓練 Edge 版本,只需三處修改:把 NANO_MODEL_CONFIG 換成 EDGE_MODEL_CONFIG、把基礎檢查點路徑指向 Cosmos 3 Edge 的 DCP 檢查點、重新命名啟動腳本。整套流程可從開源的 cosmos-framework repo 重現,釋出的檢查點也已上架 HuggingFace。

📊 訓練規模不小,但推論完全在機器人本體上

官方驗證的訓練規模並不小:64 個節點、每節點 4 張 GB200,共跑 6 萬次迭代、耗時約 68 小時(約 1.74 萬 GB200-小時),這是基礎模型等級的後訓練,不是單張 GPU 就能微調完成的工作。跑起來之後,在 NVIDIA Jetson AGX Thor T5000 上,DROID 動作策略以 640×540 解析度、15Hz 產生每個 action chunk 約需 1.53 秒,而單一 chunk 涵蓋約 2.13 秒的機器人動作,因為下一個 chunk 會在目前這個播放完之前就準備好,機械手臂能連續移動,過程中完全不需要資料中心 GPU 介入。在 RoboLab 的閉環(closed-loop)任務測試中,後訓練後的策略成功率為 22.9%。

🧩 9GB 權重,直接塞進 Thor 機載記憶體

策略透過一個使用 OpenPI 協定的 WebSocket 策略伺服器對外服務,這與整個 DROID 策略生態系使用的協定相同:客戶端送出觀測字典,伺服器回傳一個 action chunk。在 Edge 版本上,伺服器直接原生跑在 Jetson Thor 上,模型權重以 BF16 格式約 9GB,足以塞進 Thor 的機載記憶體,策略伺服器與控制端都能在機器人本體上運行,不需要資料中心 GPU 介入。

⚠️ 22.9% 的成功率說明這仍是起點

22.9% 的閉環成功率說明這仍是一個起點,而非成熟的量產方案。同時,雖然最終推論只需要 Jetson Thor,驗證用的訓練規模(64 節點、256 張 GB200)門檻相當高,對多數團隊而言,重現整套後訓練流程仍需要可觀的運算資源。

🎯 邊緣端機器人不必再等雲端 GPU 回應

對機器人團隊來說,這份教學展示的重點不只是「模型變小了」,而是一條完整、可重現的路徑:從下載資料、後訓練、轉換部署到用同一套協定服務策略,全程可以在開源的 cosmos-framework 中對照重現。如果場景需要在邊緣端做即時控制、又不想每個推論都打一次雲端 GPU,Cosmos 3 Edge 提供的是一個具體、可驗證的起點。

🔗 來源
- 標題:Post-Train NVIDIA Cosmos 3 Edge for On-Device Robot Control
- 作者／機構:Michelle Horton,NVIDIA Developer
- 連結:https://developer.nvidia.com/blog/post-train-nvidia-cosmos-3-edge-for-on-device-robot-control/

#NVIDIA #Cosmos3 #Robotics #EdgeAI #JetsonThor #WorldModels #OnDeviceAI #ImitationLearning #RobotPolicy #ReinforcementLearning
